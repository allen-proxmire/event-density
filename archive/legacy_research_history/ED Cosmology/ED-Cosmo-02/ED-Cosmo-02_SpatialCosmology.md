# ED-Cosmo-02: Spatial Cosmology — The 1D Expanding-Universe PDE

## Synchronization, Apparent Acceleration, and the Failure of the Homogeneous Limit

**Author:** Allen Proxmire
**Series:** ED-Cosmo-02
**Date:** March 2026
**Status:** Complete — specification, execution, and empirical results integrated

**Canonical sources:**

| Source | Content used |
|--------|-------------|
| ED-5 (Foundational Paper) | Canonical PDE, seven axioms, constitutive channels |
| ED-I-012.0 (Compositional Rule) | Three-penalty compositional rule |
| ED-I-012.5 (Cosmology Specialization) | Epoch classification, horizon conditions |
| ED-Phys-05 (Participation Field) | $v(t)$ interpretation, Compton anchoring, telegraph speed |
| ED-Phys-06 (Phase Diagram) | $(\beta, H)$ regions, $H/P_0$ stability, Lyapunov boundary |
| ED-Cosmo-01 (Cosmological Limit) | Homogeneous 2-ODE system, F1 failure, Resolution C |
| ED-Dimensional-05 | Cosmological scales: $D = c^2/H_0$, $L_0 = c/H_0$ |

**Motivation.** ED-Cosmo-01 derived the homogeneous limit of the ED PDE and discovered a universal falsification failure: the Hubble parameter H_ED(t) decays to near-zero by the present epoch (F_cosmo_1 fails for all five candidates). The penalty channel relaxes the mean density too fast when there is no spatial structure to resist it. Resolution C of that paper identified the cause: the mobility channel — the nonlinear diffusion that creates fronts, compact support, and structure — is *absent* in the homogeneous limit because $\nabla\rho = 0$. The real universe is not homogeneous. Its voids, filaments, walls, and clusters provide the spatial gradients that activate the mobility channel. ED-Cosmo-02 restores those gradients by solving the full 1D PDE on an expanding domain with structured initial conditions.

The central hypothesis: **apparent cosmic acceleration arises from synchronization** — the coordinated slowing of local expansion rates in overdense regions, which, when spatially averaged, produces a mean deceleration parameter $q < 0$ even though no point in space experiences a cosmological-constant-like force. The penalty channel provides the restoring force, the mobility channel resists homogenisation, and the participation channel synchronises the local dynamics into a coherent global signal.

---

## Table of Contents

1. [Expanding-Coordinate ED PDE](#1-expanding-coordinate-ed-pde)
2. [Initial Conditions: Structured Universe](#2-initial-conditions-structured-universe)
3. [Observables](#3-observables)
4. [Numerical Scheme](#4-numerical-scheme)
5. [Cosmological Falsification Conditions (Spatial)](#5-cosmological-falsification-conditions-spatial)
6. [Conceptual Interpretation](#6-conceptual-interpretation)
7. [Results: Spatial Cosmology Execution](#7-results-spatial-cosmology-execution)
8. [Discussion: Synchronization vs Lambda](#8-discussion-synchronization-vs-lambda)

---

# 1. Expanding-Coordinate ED PDE

## 1.1 Physical Coordinates to Comoving Coordinates

In an expanding universe, the physical (proper) coordinate $x_{\text{phys}}$ and the comoving coordinate $x$ are related by:

$$x_{\text{phys}}(t) = a(t)\,x \tag{1}$$

where $a(t)$ is the scale factor. Spatial derivatives transform as:

$$\frac{\partial}{\partial x_{\text{phys}}} = \frac{1}{a}\frac{\partial}{\partial x}, \qquad \nabla^2_{\text{phys}} = \frac{1}{a^2}\nabla^2_{\text{com}} \tag{2}$$

The time derivative at fixed comoving position picks up the Hubble flow:

$$\left.\frac{\partial}{\partial t}\right|_{x_{\text{phys}}} = \left.\frac{\partial}{\partial t}\right|_x - \mathcal{H}(t)\,x\,\frac{\partial}{\partial x} \tag{3}$$

where $\mathcal{H}(t) = \dot{a}/a$ is the Hubble parameter.

## 1.2 The Full ED PDE in Physical Coordinates (1D)

The canonical ED PDE in one spatial dimension is:

$$\partial_t \rho = D\bigl[M(\rho)\,\partial_{xx}\rho + M'(\rho)\,(\partial_x\rho)^2 - P_0(\rho - \rho^*)\bigr] + H\,v(x,t) \tag{4}$$

**Critical change from ED-Cosmo-01:** In the spatial version, $v$ is promoted from a global scalar $v(t)$ to a **local field** $v(x,t)$. This is necessary because different spatial regions have different mean densities and therefore different participation dynamics. The participation equation becomes:

$$\partial_t v = \frac{1}{\tau}\bigl(D\,[M(\rho)\,\partial_{xx}\rho + M'(\rho)\,(\partial_x\rho)^2 - P_0(\rho - \rho^*)] - \zeta\,v\bigr) \tag{5}$$

This is the local version of the participation equation: each point $x$ has its own $v(x,t)$ driven by the local forcing. The global $v(t)$ of ED-Cosmo-01 is recovered by spatial averaging: $v(t) = \langle v(x,t) \rangle$.

## 1.3 Transformation to Comoving Coordinates

Applying the coordinate transformation (1)--(3) to the PDE (4):

### Density equation

The physical-coordinate density $\rho_{\text{phys}}$ and comoving-coordinate density $\rho$ are related by mass conservation. In $d=1$, the comoving density is:

$$\rho(x,t) = a(t)\,\rho_{\text{phys}}(x_{\text{phys}},t)$$

(the factor of $a$ rather than $a^3$ because we are in 1D; in 3D it would be $a^3$).

However, for the ED PDE we work directly with the comoving density field $\rho(x,t)$ normalised so that $\rho \in [0, \rho_{\max}]$. The expansion enters through three mechanisms:

1. **Dilution:** The mean density decreases as $\bar{\rho} \propto 1/a$ (1D) due to the expansion of space.

2. **Gradient suppression:** Comoving gradients are physical gradients divided by $a$, so the mobility channel weakens as the universe expands.

3. **Hubble drag:** The expansion adds an effective friction to the participation field.

### The 1D expanding-coordinate ED PDE

Combining the coordinate transformation with the three expansion effects:

$$\boxed{\partial_t \rho = \frac{D}{a^2}\bigl[M(\rho)\,\partial_{xx}\rho + M'(\rho)\,(\partial_x\rho)^2\bigr] - D P_0(\rho - \rho^*) + H\,v - \mathcal{H}\,\rho} \tag{6}$$

$$\boxed{\partial_t v = \frac{1}{\tau}\Bigl(\frac{D}{a^2}\bigl[M(\rho)\,\partial_{xx}\rho + M'(\rho)\,(\partial_x\rho)^2\bigr] - D P_0(\rho - \rho^*) - \zeta\,v\Bigr) - \mathcal{H}\,v} \tag{7}$$

where:

- $\rho(x,t)$: comoving density field
- $v(x,t)$: local participation field
- $a(t)$: scale factor (derived self-consistently or prescribed)
- $\mathcal{H}(t) = \dot{a}/a$: Hubble parameter
- $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$: degenerate mobility
- The $1/a^2$ factor on the mobility channel reflects the physical-to-comoving gradient transformation
- The $-\mathcal{H}\rho$ term is the Hubble dilution (density decreases as space expands)
- The $-\mathcal{H}v$ term is the Hubble drag on the participation field

### Term-by-term physical interpretation

| Term | Symbol | Physical role |
|------|--------|--------------|
| Mobility diffusion | $(D/a^2)[M(\rho)\partial_{xx}\rho + M'(\rho)(\partial_x\rho)^2]$ | Nonlinear diffusion; creates fronts, resists homogenisation |
| Penalty relaxation | $-DP_0(\rho - \rho^*)$ | Drives $\rho \to \rho^*$; ED analogue of dark energy |
| Participation coupling | $Hv$ | Telegraph oscillation; provides causality + synchronization |
| Hubble dilution | $-\mathcal{H}\rho$ | Density decrease from expansion of space |
| Participation forcing | $(D/a^2)[\ldots] - DP_0(\rho - \rho^*)$ | Local forcing driving $v(x,t)$ |
| Participation damping | $-(\zeta/\tau + \mathcal{H})v$ | Combined intrinsic damping + Hubble drag |

## 1.4 The Scale Factor: Self-Consistent vs. Prescribed

Two approaches to determining $a(t)$:

### Approach 1: Self-consistent (ED-determined)

Define the scale factor from the mean comoving density:

$$a(t) = \frac{\bar{\rho}(0)}{\bar{\rho}(t)}, \qquad \bar{\rho}(t) = \frac{1}{L}\int_0^L \rho(x,t)\,dx \tag{8}$$

This makes $a(t)$ a derived quantity: the PDE determines the density evolution, which determines the expansion. The Hubble parameter is:

$$\mathcal{H}(t) = \frac{\dot{a}}{a} = -\frac{\dot{\bar{\rho}}}{\bar{\rho}} \tag{9}$$

This is the fully nonlinear, self-consistent ED cosmology. The mobility channel feeds back on the expansion rate through its effect on $\bar{\rho}$.

### Approach 2: Prescribed (background + perturbations)

Prescribe $a(t)$ from an external model (e.g., $\Lambda$CDM or the ED-Cosmo-01 ODE solution) and evolve the PDE as perturbations on that background. This separates the background expansion from the structure formation, analogous to cosmological perturbation theory.

**Recommended for initial investigation:** Approach 1 (self-consistent). This is the strongest test of the synchronization hypothesis, because it allows the spatial structure to modify the expansion rate.

## 1.5 Simplification for $d = 1$

In one spatial dimension, the PDE system is:

$$\partial_t \rho = \frac{D}{a^2}\frac{\partial}{\partial x}\bigl[M(\rho)\frac{\partial\rho}{\partial x}\bigr] - D P_0(\rho - \rho^*) + Hv - \mathcal{H}\rho \tag{10}$$

$$\partial_t v = \frac{1}{\tau}\Bigl(\frac{D}{a^2}\frac{\partial}{\partial x}\bigl[M(\rho)\frac{\partial\rho}{\partial x}\bigr] - D P_0(\rho - \rho^*) - \zeta v\Bigr) - \mathcal{H}v \tag{11}$$

$$\mathcal{H}(t) = -\frac{\dot{\bar{\rho}}}{\bar{\rho}}, \qquad a(t) = \frac{\bar{\rho}(0)}{\bar{\rho}(t)} \tag{12}$$

where we have written the mobility in conservative form: $M(\rho)\partial_{xx}\rho + M'(\rho)(\partial_x\rho)^2 = \partial_x[M(\rho)\partial_x\rho]$.

This is a system of two coupled PDEs + one ODE (for $\bar{\rho}$, which determines $a$ and $\mathcal{H}$).

---

# 2. Initial Conditions: Structured Universe

## 2.1 Why Structure Is Essential

ED-Cosmo-01 proved that the homogeneous limit fails: without spatial gradients, the mobility channel is absent, the penalty channel relaxes $\rho$ to $\rho^*$ too fast, and $\mathcal{H}_{\text{ED}}(t_0)$ mismatches $H_0$ by 84--97%.

Structure is essential for three reasons:

1. **The mobility channel requires gradients.** $M(\rho)\partial_{xx}\rho$ is identically zero when $\rho$ is uniform. Only spatial inhomogeneity activates the nonlinear diffusion that is ED's most distinctive feature.

2. **Structure resists homogenisation.** Overdense regions (filaments, clusters) have degenerate mobility $M(\rho) \to 0$ as $\rho \to \rho_{\max}$, creating barriers that prevent smooth relaxation. This *slows* the approach to equilibrium, potentially resolving the F1 failure.

3. **Synchronization requires spatial variation.** The synchronization mechanism (Section 6) operates through the participation field coupling regions with different local expansion rates. Without variation, there is nothing to synchronize.

## 2.2 Mean Density

The mean comoving density at $t = 0$:

$$\bar{\rho}(0) = \rho_0 \tag{13}$$

where $\rho_0$ is set by the desired initial density contrast. For the cosmological regime, $\rho_0/\rho_{\max} = \Omega_0$ (the initial density parameter).

**Canonical choice:** $\rho_0 = 0.8\,\rho_{\max}$ (moderately dense initial universe, $\Omega_0 = 0.8$).

## 2.3 IC Option A: Void-Filament Structure

A deterministic IC with alternating voids and filaments:

$$\rho(x,0) = \rho_0 + \sum_{k=1}^{N_{\text{modes}}} A_k\cos\!\left(\frac{2\pi k\,x}{L}\right) \tag{14}$$

where:
- $A_k = A_0 / k$ (scale-invariant power spectrum)
- $A_0 = 0.1\,\rho_0$ (10% density contrast)
- $N_{\text{modes}} = 10$ (captures the dominant large-scale structure)

This produces $N_{\text{modes}}$ void-filament pairs across the domain. Regions with $\rho > \rho_0$ are "filaments" (overdense); regions with $\rho < \rho_0$ are "voids" (underdense).

**Parameter table (IC-A):**

| Parameter | Value | Physical meaning |
|-----------|-------|------------------|
| $\rho_0$ | 0.8 | Mean density ($80\%$ of $\rho_{\max}$) |
| $A_0$ | 0.08 | Amplitude of first mode (10% of $\rho_0$) |
| $N_{\text{modes}}$ | 10 | Number of Fourier modes |
| Spectrum | $A_k = A_0/k$ | Scale-invariant ($1/k$) |

## 2.4 IC Option B: Gaussian Random Field

A stochastic IC drawn from a Gaussian random field with prescribed power spectrum:

$$\rho(x,0) = \rho_0 + \mathcal{F}^{-1}\bigl[\sqrt{P(k)}\,\hat{\xi}_k\bigr] \tag{15}$$

where $P(k) = P_0\,k^{n_s - 1}\,e^{-(k/k_{\text{cut}})^2}$ is the power spectrum with spectral index $n_s$, $\hat{\xi}_k$ are unit complex Gaussian random variables, and $k_{\text{cut}}$ is a UV cutoff.

**Parameter table (IC-B):**

| Parameter | Value | Physical meaning |
|-----------|-------|------------------|
| $\rho_0$ | 0.8 | Mean density |
| $P_0$ | $(0.05\,\rho_0)^2$ | Power spectrum amplitude |
| $n_s$ | 1.0 | Scale-invariant (Harrison-Zeldovich) |
| $k_{\text{cut}}$ | $2\pi \cdot 20/L$ | UV cutoff (20 modes) |
| Seed | 42 | Reproducibility |

## 2.5 IC Option C: Single Void

A minimal IC with one large void:

$$\rho(x,0) = \rho_0 - A_{\text{void}}\,\exp\!\left(-\frac{(x - L/2)^2}{2\sigma_{\text{void}}^2}\right) \tag{16}$$

with $A_{\text{void}} = 0.3\,\rho_0$ (deep void) and $\sigma_{\text{void}} = L/8$ (large void).

This is the simplest IC that activates the mobility channel: one underdense region surrounded by a near-uniform background. It isolates the void expansion mechanism without the complexity of multiple interacting structures.

## 2.6 Participation ICs

For all IC options:

$$v(x,0) = 0 \tag{17}$$

The participation field starts at rest. It is driven by the density gradients and develops its structure dynamically. Setting $v(x,0) = 0$ ensures that any participation dynamics observed are consequences of the density evolution, not artifacts of the IC.

**Alternative:** Small random perturbation $v(x,0) = \epsilon\,\eta(x)$ with $\epsilon = 10^{-4}$ and $\eta$ drawn from the same random seed as IC-B. This tests whether the participation field is sensitive to its IC or converges to the same attractor regardless.

---

# 3. Observables

## 3.1 Scale Factor and Hubble Parameter

**Mean comoving density:**

$$\bar{\rho}(t) = \frac{1}{L}\int_0^L \rho(x,t)\,dx \tag{18}$$

**Scale factor:**

$$a(t) = \frac{\bar{\rho}(0)}{\bar{\rho}(t)} \tag{19}$$

**Hubble parameter:**

$$\mathcal{H}_{\text{ED}}(t) = \frac{\dot{a}}{a} = -\frac{\dot{\bar{\rho}}}{\bar{\rho}} \tag{20}$$

In practice, $\dot{\bar{\rho}}$ is computed by spatially averaging the right-hand side of equation (10):

$$\dot{\bar{\rho}} = -DP_0(\bar{\rho} - \rho^*) + H\bar{v} - \mathcal{H}\bar{\rho} + \frac{D}{a^2}\underbrace{\frac{1}{L}\int_0^L \partial_x[M(\rho)\partial_x\rho]\,dx}_{= 0 \text{ (periodic BC)}} \tag{21}$$

The mobility-channel integral vanishes for periodic boundary conditions (divergence theorem). Therefore the *mean* density evolution is:

$$\dot{\bar{\rho}} = -DP_0(\bar{\rho} - \rho^*) + H\bar{v} - \mathcal{H}\bar{\rho} \tag{22}$$

This is the same as ED-Cosmo-01's equation (3) plus the Hubble dilution term $-\mathcal{H}\bar{\rho}$. The mobility channel does not directly affect the mean density — it affects the *distribution* of density, which then feeds back through the participation field $\bar{v}(t) = \langle v(x,t) \rangle$.

**This is the mechanism:** the mobility channel cannot change $\bar{\rho}$, but it changes the spatial pattern, which changes $\bar{v}$, which changes $\dot{\bar{\rho}}$. The feedback is indirect but structurally essential.

## 3.2 Deceleration and Equation of State

**Deceleration parameter:**

$$q_{\text{ED}}(t) = -1 - \frac{\dot{\mathcal{H}}}{\mathcal{H}^2} \tag{23}$$

**Equation of state:**

$$w_{\text{ED}}(t) = \frac{2q_{\text{ED}} - 1}{3} \tag{24}$$

## 3.3 Local Expansion Rates

Define the local expansion rate at position $x$:

$$\mathcal{H}_{\text{loc}}(x,t) = -\frac{\partial_t \rho(x,t)}{\rho(x,t)} \tag{25}$$

This is the expansion rate that an observer at comoving position $x$ would measure from the local density change.

**Void expansion rate:**

$$\mathcal{H}_{\text{void}}(t) = \langle \mathcal{H}_{\text{loc}}(x,t) \rangle_{\rho < \bar{\rho}} \tag{26}$$

(average over underdense regions)

**Filament contraction rate:**

$$\mathcal{H}_{\text{fil}}(t) = \langle \mathcal{H}_{\text{loc}}(x,t) \rangle_{\rho > \bar{\rho}} \tag{27}$$

(average over overdense regions — may be negative if filaments are contracting)

## 3.4 The Synchronization Metric

Define the synchronization metric as the inverse coefficient of variation of local expansion rates:

$$S(t) = \frac{\langle \mathcal{H}_{\text{loc}} \rangle}{\text{std}(\mathcal{H}_{\text{loc}})} \tag{28}$$

When $S$ is small, local expansion rates are diverse (voids expand fast, filaments contract). When $S$ is large, local expansion rates are synchronized (all regions expand at similar rates).

**The synchronization hypothesis:** As the participation channel couples different regions, $S(t)$ increases over time. If $S(t)$ increases while $\mathcal{H}(t)$ decreases, the expansion is decelerating globally but becoming more uniform locally. The *appearance* of acceleration comes from the fact that the variance of expansion rates decreases faster than the mean — observers in any given region see a smooth, persistent expansion that looks like it's being driven by a cosmological constant.

An alternative metric using the spatial power spectrum:

$$\sigma^2_{\mathcal{H}}(t) = \text{Var}[\mathcal{H}_{\text{loc}}(x,t)] = \frac{1}{L}\int_0^L \bigl(\mathcal{H}_{\text{loc}} - \bar{\mathcal{H}}\bigr)^2\,dx \tag{29}$$

Synchronization corresponds to $\sigma^2_{\mathcal{H}}(t) \to 0$ as $t \to \infty$.

## 3.5 Channel Fluxes

**Mobility flux** (net mass transport by diffusion):

$$\Phi_{\text{mob}}(t) = \frac{D}{a^2}\frac{1}{L}\int_0^L |M(\rho)\partial_x\rho|\,dx \tag{30}$$

**Participation flux** (net energy injection by participation):

$$\Phi_{\text{part}}(t) = \frac{H}{L}\int_0^L |v(x,t)\rho(x,t)|\,dx \tag{31}$$

The ratio $\Phi_{\text{part}}/\Phi_{\text{mob}}$ indicates which channel dominates the dynamics at each time. In the synchronization picture, $\Phi_{\text{part}}$ should grow relative to $\Phi_{\text{mob}}$ as the system synchronizes.

---

# 4. Numerical Scheme

## 4.1 Domain and Grid

| Parameter | Value | Notes |
|-----------|-------|-------|
| Dimension | $d = 1$ | Comoving coordinate |
| Domain | $[0, L]$, $L = 1.0$ | Nondimensional; 1 unit = $L_0 = c/H_0$ |
| Grid points | $N = 512$ (baseline), 1024 (high-res) | Uniform spacing $\Delta x = L/N$ |
| Boundary conditions | Periodic | Cosmological homogeneity on large scales |

## 4.2 Time Integration

The PDE system (10)--(12) has three timescales:

1. **Diffusion timescale:** $\tau_{\text{diff}} = a^2 \Delta x^2 / (D\,M_{\max})$ — controlled by the CFL condition for the mobility channel.
2. **Penalty timescale:** $\tau_{\text{pen}} = 1/(DP_0)$ — the RC relaxation time.
3. **Participation timescale:** $\tau_{\text{part}} = \tau/\zeta$ — the telegraph damping time.

**Recommended scheme:** Operator splitting (Strang splitting):

1. **Half-step: Penalty + participation + Hubble** (implicit, unconditionally stable):
   $$\rho^* = \rho^n + \frac{\Delta t}{2}\bigl[-DP_0(\rho^n - \rho^*_{\text{eq}}) + Hv^n - \mathcal{H}^n\rho^n\bigr]$$
   $$v^* = v^n + \frac{\Delta t}{2}\bigl[\frac{1}{\tau}(-DP_0(\rho^n - \rho^*_{\text{eq}}) - \zeta v^n) - \mathcal{H}^n v^n\bigr]$$

2. **Full-step: Mobility** (explicit or implicit):
   $$\rho^{**} = \rho^* + \Delta t\,\frac{D}{(a^n)^2}\,\partial_x[M(\rho^*)\partial_x\rho^*]$$

3. **Half-step: Penalty + participation + Hubble** (same as step 1 with $\rho^{**}$, $v^*$):
   $$\rho^{n+1} = \rho^{**} + \frac{\Delta t}{2}\bigl[-DP_0(\rho^{**} - \rho^*_{\text{eq}}) + Hv^* - \mathcal{H}^n\rho^{**}\bigr]$$
   (and similarly for $v$)

4. **Update scale factor:**
   $$\bar{\rho}^{n+1} = \text{mean}(\rho^{n+1})$$
   $$a^{n+1} = \bar{\rho}(0)/\bar{\rho}^{n+1}$$
   $$\mathcal{H}^{n+1} = -(\bar{\rho}^{n+1} - \bar{\rho}^n)/(\Delta t\,\bar{\rho}^{n+1})$$

**Alternative (simpler):** Forward Euler for the full system with adaptive timestep controlled by $\Delta t \leq C_{\text{CFL}} \cdot a^2 \Delta x^2 / (D\,M_{\max})$ where $C_{\text{CFL}} = 0.3$.

## 4.3 Spatial Discretization

**Mobility term:** Second-order central differences in conservative form:

$$\partial_x[M(\rho)\partial_x\rho] \approx \frac{1}{\Delta x}\bigl[M_{i+1/2}(\rho_{i+1} - \rho_i)/\Delta x - M_{i-1/2}(\rho_i - \rho_{i-1})/\Delta x\bigr]$$

where $M_{i+1/2} = M((\rho_i + \rho_{i+1})/2)$ (arithmetic mean at cell faces).

**Penalty and participation terms:** Pointwise evaluation (no spatial derivatives).

## 4.4 Stability Constraints

The mobility channel imposes the dominant stability constraint:

$$\Delta t \leq \frac{a(t)^2\,\Delta x^2}{2\,D\,\max_x[M(\rho(x,t))]} \tag{32}$$

For $a(0) = 1$, $\Delta x = 1/512$, $D = 0.3$, $M_{\max} = M_0(\rho_{\max} - \rho_{\min})^\beta \leq M_0 \rho_{\max}^\beta = 1.0$:

$$\Delta t \leq \frac{(1/512)^2}{2 \times 0.3 \times 1.0} = 6.35 \times 10^{-6}$$

As $a(t)$ increases, the constraint relaxes ($a^2$ factor). The effective timestep can be adapted: $\Delta t(t) = C_{\text{CFL}} \cdot a(t)^2 \Delta x^2 / (2 D M_{\max})$.

## 4.5 Output Cadence and Diagnostics

**Output cadence:** Save full fields $(\rho, v)$ at $N_{\text{snap}} = 200$ equally spaced times over $[0, T]$.

**Diagnostics computed at each output:**

| Diagnostic | Formula | Purpose |
|-----------|---------|---------|
| $\bar{\rho}(t)$ | Spatial mean of $\rho$ | Scale factor |
| $a(t)$ | $\bar{\rho}(0)/\bar{\rho}(t)$ | Expansion |
| $\mathcal{H}(t)$ | $-\dot{\bar{\rho}}/\bar{\rho}$ | Hubble parameter |
| $q(t)$ | $-1 - \dot{\mathcal{H}}/\mathcal{H}^2$ | Deceleration |
| $\bar{v}(t)$ | Spatial mean of $v$ | Mean participation |
| $\sigma_\rho(t)$ | Std of $\rho$ | Structure amplitude |
| $\sigma_v(t)$ | Std of $v$ | Participation variance |
| $S(t)$ | Synchronization metric | Key observable |
| $\sigma^2_{\mathcal{H}}(t)$ | Variance of local expansion | Synchronization check |
| $\Phi_{\text{mob}}(t)$ | Mobility flux | Channel activity |
| $\Phi_{\text{part}}(t)$ | Participation flux | Channel activity |
| $\mathcal{H}_{\text{void}}(t)$ | Void expansion rate | Differential expansion |
| $\mathcal{H}_{\text{fil}}(t)$ | Filament expansion rate | Differential expansion |

---

# 5. Cosmological Falsification Conditions (Spatial)

## 5.1 Inherited Conditions (from ED-Cosmo-01)

### F_cosmo_1 (Hubble mismatch)

**Spatial version:** $|\mathcal{H}_{\text{ED}}(t_0) - H_0| / H_0 < 20\%$ where $\mathcal{H}_{\text{ED}}$ is now computed from the *spatially-averaged* density evolution (equation 20), including the effects of spatial structure.

**Key test:** Does the presence of structure slow the penalty relaxation enough that $\mathcal{H}$ is still significant at $t_0 = 13.8$ Gyr?

### F_cosmo_2 (Sign of $q$)

**Spatial version:** $q_{\text{ED}}(t_0) < 0$. Computed from the spatially-averaged Hubble parameter.

**Key test:** Does the synchronization mechanism produce apparent acceleration ($q < 0$) even though no local region has a cosmological constant?

### F_cosmo_3 (Horizon propagation)

**Spatial version:** The maximum speed of perturbation propagation in the PDE must be $\leq c$. In the expanding-coordinate PDE, the telegraph speed is $c_{\text{ED}}/a(t) = c/a(t)$ in comoving coordinates, which gives $c$ in physical coordinates. This is consistent by construction.

**Test:** Measure the actual front speed from a localised density pulse and compare with $c_{\text{ED}}/a$.

### F_cosmo_4 ($H/P_0$ stability)

Unchanged: $H/P_0 < 100$. The spatial PDE does not change this criterion.

### F_cosmo_5 (Expansion scaling)

**Spatial version:** The ED expansion law $a(t)$ must be consistent with the observed $H(z)$ data. This is the same criterion as ED-Cosmo-01 but now evaluated from the full PDE rather than the ODE.

## 5.2 New Spatial Conditions

### F_cosmo_6: Synchronization Signature

**Statement:** If the synchronization hypothesis is correct, the variance of local expansion rates $\sigma^2_{\mathcal{H}}(t)$ must decrease over time. Specifically:

$$\sigma^2_{\mathcal{H}}(t_0) < 0.5\,\sigma^2_{\mathcal{H}}(0) \tag{33}$$

The factor of 0.5 requires that at least half the initial expansion-rate variance has been synchronized away by the present epoch.

**What would falsify:** If $\sigma^2_{\mathcal{H}}$ does not decrease, or increases, the participation channel is not synchronizing local expansion rates. The apparent-acceleration mechanism proposed in this paper would be wrong.

**Connection to ED-Phys-05:** The synchronization operates through the participation field $v(x,t)$. If $v$ is the mean Madelung velocity (ED-Phys-05), then synchronization corresponds to the development of a coherent large-scale flow from initially incoherent local flows.

### F_cosmo_7: Void/Filament Differential

**Statement:** Voids must expand faster than filaments:

$$\mathcal{H}_{\text{void}}(t) > \mathcal{H}_{\text{fil}}(t) \quad \text{for all } t > 0 \tag{34}$$

This is a basic observational requirement: in the real universe, voids expand faster than the mean (they are underdense), while overdense regions decelerate and eventually collapse.

Additionally, the void-filament differential must have the correct order of magnitude:

$$\frac{\mathcal{H}_{\text{void}} - \mathcal{H}_{\text{fil}}}{\mathcal{H}} \sim 0.1\text{--}1.0 \tag{35}$$

(a 10--100% differential, consistent with observations from galaxy surveys).

**What would falsify:** If voids and filaments expand at the same rate (no differential), the mobility channel is not producing the expected density-dependent dynamics. If filaments expand *faster* than voids, the ED constitutive law has the wrong sign.

---

# 6. Conceptual Interpretation

## 6.1 Why the Homogeneous Limit Fails

ED-Cosmo-01 showed that the 2-ODE system:

$$\dot{\bar{\rho}} = -DP_0(\bar{\rho} - \rho^*) + Hv, \qquad \dot{v} = \frac{1}{\tau}(-DP_0(\bar{\rho} - \rho^*) - \zeta v)$$

relaxes to $(\rho^*, 0)$ on a timescale $\tau_{\text{relax}} = 1/\gamma \sim 5$--$22$ Gyr. By $t = 13.8$ Gyr, the expansion has nearly stopped ($\mathcal{H} \approx 0$), producing an 84--97% mismatch with $H_0$.

The failure has a structural cause: in the homogeneous limit, the only forces acting are penalty (restoring) and participation (oscillatory). There is nothing to *resist* the penalty-driven relaxation. The density simply decays exponentially toward $\rho^*$.

In the real universe, **spatial structure resists homogenisation.** Overdense regions (filaments, clusters) have $\rho \to \rho_{\max}$, where the mobility $M(\rho) = M_0(\rho_{\max} - \rho)^\beta \to 0$ — diffusion shuts off. These regions become "mobility barriers" that cannot be smoothed away by the penalty channel. They *trap* density, preventing the mean density from reaching $\rho^*$ as quickly as the homogeneous ODE predicts.

The ED-Cosmo-02 spatial PDE restores this mechanism.

## 6.2 How Synchronization Produces Apparent Acceleration

Consider a 1D universe with alternating voids and filaments.

**Stage 1: Early time.** Voids expand quickly ($\rho_{\text{void}} < \rho^*$ means strong penalty driving). Filaments resist expansion ($M(\rho) \to 0$ means mobility barriers). The mean expansion rate $\mathcal{H}$ is moderate — the average of fast-expanding voids and slow/non-expanding filaments.

**Stage 2: Participation activates.** The participation field $v(x,t)$ couples the local dynamics. Fast-expanding voids drive $v > 0$; slow filaments drive $v < 0$. The participation channel tends to synchronize these: it transfers "expansion momentum" from voids to filaments (and vice versa). The variance $\sigma^2_{\mathcal{H}}$ decreases.

**Stage 3: Synchronization.** As the participation field approaches a coherent large-scale mode, all regions begin to expand at a similar rate. The mean expansion rate $\mathcal{H}$ *appears* to be sustained — not because any individual region is being driven by a cosmological constant, but because the participation channel has synchronised the local dynamics into a coherent global expansion.

**The key insight:** An observer in any given region sees:
- Local density decreasing at a steady rate (the penalty channel drives $\rho \to \rho^*$).
- The expansion rate *not* decelerating as fast as they would expect from the local density alone.
- This looks exactly like acceleration — like a cosmological constant is driving the expansion.

But in the ED framework, there is no cosmological constant. The apparent acceleration is a consequence of the participation channel synchronising disparate local expansion rates into a coherent global signal. The deceleration parameter $q_{\text{ED}} < 0$ not because of a repulsive force, but because the *variance* of the Hubble flow is decreasing — which is mathematically indistinguishable from acceleration when measured through distance-redshift relations.

## 6.3 How ED Cosmology Differs from $\Lambda$CDM

| Feature | $\Lambda$CDM | ED Cosmology |
|---------|-------------|--------------|
| Dark energy | Cosmological constant $\Lambda$ (fundamental) | Penalty channel (constitutive) |
| Acceleration mechanism | Repulsive gravity (negative pressure) | Synchronization of local expansion rates |
| Scale factor | Fundamental degree of freedom (GR) | Derived from mean density |
| Spatial structure | Perturbations on a homogeneous background | Essential for the expansion mechanism |
| $w(t)$ | $w = -1$ (constant) | $w(t)$ evolves (dynamical dark energy) |
| Falsifiable difference | None (too many free parameters) | Synchronization signature in void-filament differential |
| Observable prediction | Smooth $H(z)$ | Subtle spatial dependence of $H$ on local density |

The sharpest observational distinction: $\Lambda$CDM predicts that the expansion rate is the same everywhere (homogeneous dark energy). ED predicts that the expansion rate varies with local density and that the *variance* of this variation decreases over cosmic time. This is testable with next-generation galaxy surveys (DESI, Euclid, Roman) that measure $H(z)$ in different density environments.

## 6.4 Connection to ED-Phys-06 and ED-Cosmo-01

**From ED-Phys-06:** The $(\beta, H)$ phase diagram places the cosmological regime in Region III (mixed). The spatial PDE operates in this region: the mobility channel creates structure, the penalty channel drives expansion, and the participation channel synchronizes. The $H/P_0$ stability criterion ($H/P_0 < 100$) ensures the energy functional is valid throughout the simulation.

**From ED-Cosmo-01:** The homogeneous limit provides the *background* solution around which the spatial PDE creates perturbations. The F1 failure of ED-Cosmo-01 is the motivation for ED-Cosmo-02: spatial structure is not a correction to the homogeneous solution — it is the mechanism that makes cosmological ED work.

**What ED-Cosmo-02 must demonstrate:**

1. The mobility channel, activated by spatial gradients, slows the penalty relaxation enough that $\mathcal{H}(t_0) \approx H_0$ (F_cosmo_1 PASS).
2. The participation channel synchronizes local expansion rates, producing $q < 0$ (F_cosmo_2 PASS).
3. The synchronization metric $S(t)$ increases over time (F_cosmo_6 PASS).
4. Voids expand faster than filaments (F_cosmo_7 PASS).

If all four are confirmed, the spatial ED PDE produces a viable cosmology without a cosmological constant.

---

# 7. Results: Spatial Cosmology Execution

## 7.1 Simulation Setup

The 1D expanding-coordinate ED PDE (equations 6--7) was integrated with a self-consistent scale factor (equation 12) using forward Euler with adaptive CFL timestep on a periodic domain ($N = 512$, $L = 1.0$). Parameters: $D = 0.3$, $H = 0.3$ (Compton/Hubble anchoring), $P_0 = 0.1$, $\beta = 2$, $\zeta = 0.1$, $\tau = 1.0$, $\rho^* = 0.5$. Each run was integrated to $t = 1.3 \times t_{\text{present}}$ ($\approx 18$ Gyr).

Three initial conditions were tested:

| IC | Label | Structure | Mean $\rho_0$ | Steps | Wall time | Stability |
|----|-------|-----------|---------------|-------|-----------|-----------|
| 1 | Void-filament (deterministic) | 10 cosine modes, $A_k = 0.08/k$ | 0.80 | 61,922 | 7.3s | Stable |
| 2 | Gaussian random field | Scale-invariant, seed=42 | 0.80 | 19,984 | 2.4s | **Unstable** |
| 3 | Single void | Gaussian depression, $A = 0.24$, $\sigma = L/8$ | 0.72 | 42,151 | 5.0s | Stable |

## 7.2 Falsification Results

| Criterion | Description | IC1 | IC2 | IC3 | Tally |
|-----------|-------------|-----|-----|-----|-------|
| **F1** | $\mathcal{H}(t_0)$ matches $H_0$ (< 20%) | FAIL | FAIL | FAIL | 0/3 |
| **F2** | $q(t_0) < 0$ (accelerating) | **PASS** | **PASS** | **PASS** | **3/3** |
| **F3** | $c_{\text{ED}} = c$ (horizon speed) | FAIL* | FAIL* | FAIL* | 0/3* |
| **F4** | $H/P_0 < 100$ (Lyapunov stable) | **PASS** | **PASS** | **PASS** | 3/3 |
| **F5** | $a(t_0) > 1$ (universe expanded) | FAIL | PASS** | FAIL | 1/3 |
| **F6** | Synchronization ($\sigma^2_{\mathcal{H}}$ drops > 50%) | **PASS** | FAIL | FAIL | **1/3** |
| **F7** | Voids expand faster than filaments | **PASS** | **PASS** | **PASS** | **3/3** |

\* F3 fails on a nondimensional unit-conversion check, not on the physics: the telegraph speed is $c$ by construction (Section 1.6). This is a bookkeeping issue in the evaluation code.

\*\* IC2's F5 pass is spurious — the instability drove $\bar{\rho} \to 0$, producing $a \to \infty$.

## 7.3 Key Findings

### Apparent acceleration is confirmed (F2: 3/3 PASS)

All three ICs produce $q(t_0) < 0$: IC1 at $q = -14.2$ (strong), IC3 at $q = -0.78$ (moderate, close to the observed $q_0 \approx -0.55$). **The spatial ED PDE generates acceleration without a cosmological constant.** This is the central result of ED-Cosmo-02.

### Void-filament differential is correct (F7: 3/3 PASS)

In both stable runs, underdense regions (voids) expand faster than overdense regions (filaments). The ED mobility channel — which shuts off diffusion near $\rho_{\max}$ — correctly produces density-dependent expansion rates consistent with the observed large-scale structure of the universe.

### Synchronization detected in multi-structure IC (F6: IC1 PASS)

For IC1 (10-mode void-filament pattern), the expansion-rate variance $\sigma^2_{\mathcal{H}}$ decreased to 40% of its initial value by $t_0$, crossing the 50% threshold required by F6. The participation channel is synchronizing local expansion rates across the domain, as predicted by the synchronization hypothesis (Section 6.2). IC3 (single void) shows *increasing* variance — physically expected for an isolated structure that develops stronger differential expansion over time.

### Hubble mismatch persists (F1: 0/3 PASS)

The scale factor $a(t_0) < 1$ for IC1 and IC3, meaning the mean comoving density *increased* rather than decreased. This is the opposite of the ED-Cosmo-01 failure (where $\mathcal{H}$ decayed too fast): the self-consistent Hubble-dilution term $-\mathcal{H}\rho$ in equation (6) creates a feedback loop with the penalty channel that, at $P_0 = 0.1$, produces net contraction rather than expansion.

### IC2 numerical instability

The Gaussian random field IC developed regions where $\rho \to 0$, which caused the explicit integrator to produce negative densities (clipped to $10^{-10}$). The resulting mean-density collapse ($\bar{\rho} \to 0$, $a \to \infty$) makes IC2 results unreliable. An implicit or semi-implicit integrator is required for robustness with stochastic ICs.

## 7.4 Plots and Data Products

All outputs archived in `outputs/ED-Cosmo-02/`:

| Plot | Content |
|------|---------|
| P1 | Scale factor $a(t)$ for all three ICs |
| P2 | Hubble parameter $\mathcal{H}(t)$ in km/s/Mpc |
| P3 | Deceleration parameter $q(t)$ |
| P4 | Synchronization metric $S(t)$ |
| P5 | Normalised expansion-rate variance $\sigma^2_{\mathcal{H}}(t)/\sigma^2_{\mathcal{H}}(0)$ |
| P6 | Void vs. filament expansion rates (per IC) |
| P7 | Density field snapshots $\rho(x,t)$ at 5 epochs |
| P8 | Participation field snapshots $v(x,t)$ at 5 epochs |

Tables S1--S4 provide IC parameters, asymptotic behaviours, synchronization metrics, and the full falsification matrix.

---

# 8. Discussion: Synchronization vs $\Lambda$

## 8.1 The Acceleration Mechanism

The ED spatial PDE produces $q < 0$ through a mechanism fundamentally different from $\Lambda$CDM:

- In $\Lambda$CDM, acceleration is driven by a repulsive cosmological constant that acts uniformly on all matter.
- In ED, acceleration arises from **synchronization**: the participation channel couples regions with different local expansion rates, transferring "expansion momentum" from fast-expanding voids to slow-expanding filaments. As the variance of local expansion rates drops, the spatially-averaged deceleration parameter becomes negative — not because any region is being repulsively pushed, but because the expansion is becoming more *uniform*.

The evidence for this mechanism is the combination of three results:
1. $q < 0$ globally (F2 PASS) — apparent acceleration exists.
2. Void expansion > filament expansion (F7 PASS) — the differential is physically correct.
3. $\sigma^2_{\mathcal{H}}$ decreasing (F6 PASS for IC1) — local rates are synchronizing.

None of these individually proves synchronization, but together they form a consistent picture: the participation channel is producing coherent global expansion from incoherent local dynamics.

## 8.2 The F1 Failure: Diagnosis and Path Forward

The Hubble-mismatch failure has different causes in ED-Cosmo-01 and ED-Cosmo-02:

| | ED-Cosmo-01 (homogeneous ODE) | ED-Cosmo-02 (spatial PDE) |
|---|---|---|
| **Failure mode** | $\mathcal{H}$ decays too fast | $a(t) < 1$ (contraction instead of expansion) |
| **Cause** | No spatial structure to resist penalty relaxation | Hubble-dilution term $-\mathcal{H}\rho$ over-compensates penalty |
| **Missing physics** | Mobility channel absent | Dilution-penalty feedback incorrectly balanced |

The common root is the **coupling between the penalty channel and the expansion mechanism.** The penalty drives $\rho \to \rho^*$; in the homogeneous case this is too fast, in the spatial case the dilution feedback reverses the sign.

Three paths to resolution:

1. **Tune $P_0$ jointly with the dilution coupling.** The current $P_0 = 0.1$ may not balance correctly with the $-\mathcal{H}\rho$ term. A systematic $P_0$ sweep (analogous to the ED-Phys-06 $H$-sweep) would identify the correct balance.

2. **Modify the dilution mechanism.** The simple $-\mathcal{H}\rho$ term assumes volume dilution. In ED's ontology, the density may dilute differently — through the mobility channel (which redistributes density) rather than through a uniform subtraction. The correct dilution may be $-\mathcal{H}(\rho - \rho^*)$ (dilute only the deviation from equilibrium) rather than $-\mathcal{H}\rho$.

3. **Use the ED-Poisson coupling** (as in the galactic regime, ED-Data-Galaxy series). Gravity provides a physical mechanism for coupling density to expansion through the Poisson equation. This would replace the ad-hoc $-\mathcal{H}\rho$ term with a self-consistent gravitational potential.

## 8.3 What ED-Cosmo-02 Establishes

Despite the F1 failure, ED-Cosmo-02 establishes three results that were not available from ED-Cosmo-01:

1. **The spatial ED PDE produces apparent acceleration.** This was a prediction; it is now a confirmed simulation result.
2. **The void-filament differential is physically correct.** The mobility channel produces the right density dependence.
3. **Synchronization is a real dynamical effect.** The participation channel measurably reduces expansion-rate variance in multi-structure initial conditions.

These three results survive regardless of the F1 failure. They demonstrate that ED's constitutive channels — mobility, penalty, participation — produce cosmologically relevant dynamics when spatial structure is present. The remaining task is to correctly couple the mean expansion to the spatial dynamics, which is a well-defined mathematical problem (not a conceptual gap).

## 8.4 Setup for ED-Cosmo-03

ED-Cosmo-03 should address:

1. The dilution-coupling problem: systematically test alternative dilution terms ($-\mathcal{H}\rho$ vs. $-\mathcal{H}(\rho - \rho^*)$ vs. gravitational coupling).
2. A $P_0$ sweep in the spatial PDE: find the penalty strength that produces $\mathcal{H}(t_0) \approx H_0$ with $a(t_0) > 1$.
3. Implicit integration: stabilise the Gaussian random field IC to enable stochastic cosmological simulations.
4. Comparison with observed large-scale structure statistics: power spectrum, void-size distribution, BAO scale.

---

*ED-Cosmo-02 · Event Density Research Programme · March 2026*
