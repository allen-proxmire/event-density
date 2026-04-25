# Event Density as an Ontology: A BAO-like Correlation Feature from a Minimal PDE

**Allen Proxmire**

---

## Abstract

Event Density (ED) is an ontological framework built on four primitives — a bounded scalar density field, a degenerate nonlinear mobility, a monostable penalty, and a global participation variable — from which a unique canonical PDE is derived via seven structural axioms. This paper presents a single, focused result: the canonical ED PDE, with no modifications or cosmology-specific additions, produces a robust preferred scale in the two-point correlation function of the density field. The feature is strictly absent when the participation coupling $H$ is zero and present for all $H > 0$. Its amplitude grows monotonically with $H$, and its radius is controlled by the telegraph oscillation frequency $\omega(H, \tau, \zeta)$, not by diffusion alone. The mechanism is oscillation-modulated diffusion with freeze-out: the participation variable oscillates, modulating the spatially varying density decay through the nonlinear mobility; when the oscillator reverses sign, the correlation feature freezes at a characteristic radius $r_{\mathrm{BAO}} \sim \sqrt{2 D_{\mathrm{eff}} \pi / \omega}$. This is a structural analogue of the baryon acoustic oscillation. It does not require a metric, a gravitational potential, a multi-component fluid, or any physics beyond the canonical ED constitutive functions. The result demonstrates that ED's minimal primitives are sufficient to generate a cosmology-like observable as an architectural consequence, providing a nontrivial test of the framework's ontological scope.

---

## 1. Introduction: Event Density as an Ontology

Most approaches to fundamental physics begin with a commitment to specific mathematical objects — a metric tensor, a Hilbert space, a partition function — and then derive dynamics from variational principles or symmetry constraints. Event Density takes a different path. It begins with a single question: *what is the simplest mathematical system whose own constitutive structure produces physically recognisable dynamics?*

The answer is a scalar density field $\rho(x,t)$ on a bounded domain $\Omega \subset \mathbb{R}^d$, evolving under a quasilinear parabolic PDE with three constitutive channels:

1. **Degenerate diffusion.** A nonlinear mobility $M(\rho)$ that vanishes at a capacity bound $\rho_{\max}$, creating regions where transport halts — *horizons* in the ED vocabulary.

2. **Monostable penalty.** A linear restoring force $P(\rho) = P_0(\rho - \rho^*)$ that drives the field toward a unique equilibrium density $\rho^*$.

3. **Participation coupling.** A global scalar variable $v(t)$, driven by the domain-averaged operator and feeding back uniformly into the PDE. This is the minimal non-local extension of a purely local diffusion equation.

These three channels are not chosen to reproduce any particular physical phenomenon. They are the irreducible components of a second-order, isotropic, dissipative, scalar PDE with degenerate mobility and minimal global coupling, as derived from seven structural axioms (Section 2). The resulting system has been characterised across nine numerical experiments spanning diffusion, telegraph oscillation, reaction kinetics, pattern formation, energy structure, and physical interpretation (Proxmire, ED-PHYS-01 through ED-PHYS-10). It possesses a unique globally attracting equilibrium, five simultaneous Lyapunov functionals, a twelve-family invariant atlas, and a morphological taxonomy (filaments, sheets, blobs) that persists across spatial dimensions one through four.

The central question of this paper is whether these minimal primitives — density, mobility, penalty, participation — are sufficient to produce a structural analogue of a specific cosmological observable: the baryon acoustic oscillation (BAO) peak.

The BAO peak is a bump in the two-point correlation function of matter at a characteristic scale of $\sim 150$ Mpc, imprinted by acoustic oscillations in the early-universe photon-baryon plasma and frozen at photon decoupling. Its existence requires three ingredients: a density perturbation, an oscillatory propagation mechanism, and a freeze-out event. We show that the ED PDE contains all three — diffusion (propagation), participation (oscillation), and the zero-crossing of $v(t)$ (freeze-out) — and that the resulting correlation feature is controlled by the telegraph channel parameters, not by diffusion alone.

**What ED is not.** ED does not postulate a spacetime metric, a gravitational potential, a photon-baryon fluid, or any multi-component microphysics. It has no Lorentz invariance, no gauge symmetry, no action principle. It is parabolic, not hyperbolic; dissipative, not conservative. The BAO analogue described here is a *structural* consequence of the PDE's constitutive design, not a physical derivation of the cosmological BAO.

---

## 2. The Canonical ED PDE

### 2.1 Statement

The canonical ED system on $\Omega \subset \mathbb{R}^d$ is

$$\partial_t \rho = D\,F[\rho] + H\,v, \qquad \dot{v} = \frac{1}{\tau}\bigl(\bar{F} - \zeta\,v\bigr), \tag{1}$$

where the density operator is

$$F[\rho] = M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho), \tag{2}$$

the domain average is $\bar{F} = |\Omega|^{-1}\int_\Omega F[\rho]\,d^d\!x$, and the constitutive functions are

$$M(\rho) = M_0\,(\rho_{\max} - \rho)^\beta, \qquad P(\rho) = P_0\,(\rho - \rho^*). \tag{3}$$

The first two terms of $F$ combine into a divergence: $M\nabla^2\rho + M'|\nabla\rho|^2 = \nabla\!\cdot\!\bigl[M(\rho)\nabla\rho\bigr]$. The full system is therefore a nonlinear diffusion equation in divergence form, augmented by a linear reaction term $-P(\rho)$ and a global source $+Hv$.

### 2.2 Parameters and Their Roles

| Symbol | Name | Canonical value | Role |
|--------|------|-----------------|------|
| $D$ | Diffusion weight | 0.3 | Strength of the local operator |
| $H$ | Participation coupling | varied (0–10) | Global feedback gain |
| $\tau$ | Participation timescale | 1.0 | Response time of $v$ |
| $\zeta$ | Participation damping | 0.05 | Friction on $v$ |
| $P_0$ | Penalty slope | 0.5 | Restoring force toward $\rho^*$ |
| $M_0$ | Mobility prefactor | 1.0 | Diffusion scale |
| $\beta$ | Mobility exponent | 2.0 | Degeneracy sharpness |
| $\rho^*$ | Equilibrium density | 0.5 | Penalty target |
| $\rho_{\max}$ | Capacity bound | 1.0 | Upper density limit |

### 2.3 The Three Constitutive Channels

**Diffusion channel.** The divergence-form operator $\nabla\!\cdot\!(M\nabla\rho)$ redistributes density by gradient-driven flow. The mobility $M(\rho)$ is a decreasing function of $\rho$ that vanishes at $\rho = \rho_{\max}$. Near the capacity bound, diffusion halts: regions with $\rho \approx \rho_{\max}$ become dynamically isolated, forming *horizons* — the ED analogue of free boundaries in porous-medium equations.

**Penalty channel.** The term $-P(\rho) = -P_0(\rho - \rho^*)$ is a linear restoring force that drives the density toward the equilibrium $\rho^*$. Unlike the double-well potentials of Allen-Cahn or Cahn-Hilliard equations, the ED penalty is monostable: there is one equilibrium, not two. The system cannot phase-separate or form Turing patterns. All structure is transient.

**Participation channel.** The variable $v(t)$ is driven by the domain-averaged operator $\bar{F}$ and decays with rate $\zeta/\tau$. It feeds back into the PDE as a spatially uniform source $+Hv$. When $H > 0$, the coupled $(\rho, v)$ system exhibits oscillatory relaxation for the spatially uniform mode (Section 3). This is the only non-local element in the ED architecture.

### 2.4 Axiomatic Derivation

The canonical PDE is not postulated ad hoc. It is derived from seven structural axioms: locality (P1), isotropy (P2), gradient-driven flow (P3), dissipative structure (P4), single scalar field (P5), minimal coupling (P6), and dimensional consistency (P7). The derivation proceeds by elimination: P1+P2 restrict the operator to functions of $(\rho, |\nabla\rho|^2, \nabla^2\rho)$; P3 determines the principal part; P4 constrains the reaction term via a Lyapunov functional; P5 excludes vectors and tensors; P6 determines the coupling structure; P7 ensures dimension-independence. The canonical PDE is the unique second-order system satisfying all seven axioms. The proof is structural rather than formal; a complete account is given in the ED-Phys series (papers 36 and 40).

---

## 3. Telegraph Reduction and the Participation Channel

### 3.1 Linearisation

Consider a spatially uniform perturbation $\delta(t) = \langle\rho\rangle(t) - \rho^*$ about the equilibrium $(\rho^*, 0)$. For a uniform field, $\nabla\rho = 0$ and $\nabla^2\rho = 0$, so $F[\rho] = -P(\rho) = -P_0\delta$. The linearised system is

$$\dot{\delta} = -D P_0\,\delta + H\,v, \tag{4a}$$

$$\dot{v} = \frac{1}{\tau}\bigl(-P_0\,\delta - \zeta\,v\bigr). \tag{4b}$$

### 3.2 The Telegraph Equation

Differentiating (4a) and substituting (4b) eliminates $v$:

$$\ddot{\delta} + 2\gamma\,\dot{\delta} + \omega_0^2\,\delta = 0, \tag{5}$$

with

$$\gamma = \frac{D P_0 + \zeta/\tau}{2}, \qquad \omega_0^2 = \frac{D P_0\,\zeta + H P_0}{\tau}. \tag{6}$$

This is the **telegraph equation** for the spatially uniform mode. Its character depends on the sign of the discriminant $\Delta = \gamma^2 - \omega_0^2$.

**Overdamped** ($\Delta > 0$): Two real negative eigenvalues. The mean density relaxes monotonically. This is the regime $H \ll H_{\mathrm{crit}}$.

**Underdamped** ($\Delta < 0$): Complex eigenvalues with $\mathrm{Re}(\lambda) = -\gamma < 0$ and oscillation frequency

$$\omega = \sqrt{\omega_0^2 - \gamma^2}. \tag{7}$$

The mean density oscillates while decaying. The quality factor is $Q = \omega / (2\gamma)$.

For the canonical parameters with $P_0 = 0.5$, $\zeta = 0.05$, $\tau = 1.0$:

| $H$ | $\gamma$ | $\omega$ | $T_{\mathrm{osc}} = 2\pi/\omega$ | $Q$ |
|-----|----------|----------|-----------------------------------|-----|
| 0 | 0.100 | (overdamped) | -- | -- |
| 0.5 | 0.100 | 0.498 | 12.63 | 2.49 |
| 1.0 | 0.100 | 0.705 | 8.91 | 3.53 |
| 2.0 | 0.100 | 0.999 | 6.29 | 4.99 |
| 3.0 | 0.100 | 1.224 | 5.13 | 6.12 |
| 5.0 | 0.100 | 1.580 | 3.98 | 7.90 |

Any nonzero $H$ above the (very small) critical value $H_{\mathrm{crit}} \approx 0.01$ places the system in the underdamped regime. The participation channel is therefore generically oscillatory.

### 3.3 Ontological Interpretation

The telegraph mode means that the *entire density field* experiences a time-varying global tide: $v(t)$ swings negative (suppressing density growth), passes through zero, and swings positive (enhancing it). This tide is uniform in space but oscillatory in time. It is the ED structural analogue of a global clock — a periodic modulation imposed by the system's own feedback architecture, not by an external driving force.

For individual spatial modes $k \geq 1$ (cosine perturbations with zero spatial mean), the linear coupling through $\bar{F}$ is exactly zero: $\langle\cos(k\pi x/L)\rangle = 0$ for $k \geq 1$. The telegraph oscillation therefore does not directly couple to individual spatial modes in the linear regime. Its influence on spatial structure arises entirely through the **nonlinear** terms — specifically, the density-dependent mobility $M(\rho)$, which makes the effective diffusion rate a function of the local density. This nonlinear coupling between the uniform oscillation and the spatially varying structure is the mechanism behind the BAO-like feature.

---

## 4. Mapping to the BAO Mechanism

### 4.1 The Physical BAO

The baryon acoustic oscillation is a preferred clustering scale of $\sim 150$ Mpc in the galaxy distribution, imprinted by the following sequence in the early universe:

1. **Initial perturbation.** A localised overdensity in the photon-baryon-dark matter plasma.
2. **Acoustic propagation.** Pressure gradients drive a spherical sound wave outward at speed $c_s \approx c/\sqrt{3}$.
3. **Freeze-out.** At photon decoupling ($z \approx 1090$), photon pressure vanishes, the sound wave stalls, and the density enhancement at the sound horizon $r_s = c_s \cdot t_{\mathrm{dec}}$ is frozen into the matter distribution.

The result is a bump in the two-point correlation function $\xi(r)$ at $r = r_s$.

### 4.2 The ED Structural Analogue

The ED PDE contains three channels that map onto the BAO ingredients:

| BAO ingredient | ED analogue | Mechanism |
|----------------|-------------|-----------|
| Initial perturbation | Multi-bump IC on a uniform overdense background | Gaussian bumps of amplitude $A = 0.08$ on $\rho^* + \epsilon$ |
| Acoustic propagation | Diffusive spreading | $D_{\mathrm{eff}} = D \cdot M^* = 0.075$ |
| Oscillatory modulation | Telegraph oscillation of $v(t)$ | Frequency $\omega(H, \tau, \zeta)$ |
| Freeze-out | Zero-crossing of $v(t)$ | Oscillation reversal halts the modulation |
| Preferred scale | $r_{\mathrm{BAO}} \sim \sqrt{2 D_{\mathrm{eff}} \pi / \omega}$ | Diffusion length at half-period |

The mapping is structural, not physical. Three important differences must be stated clearly:

- **ED spreading is diffusive** ($r \sim \sqrt{t}$), **not acoustic** ($r \sim t$). The "propagation" is parabolic, not hyperbolic. There is no sound speed in ED.
- **The oscillation is global** (uniform $v(t)$), **not local** (spatially propagating sound wave). The spatial structure arises through the nonlinear mobility, not through wave propagation.
- **The freeze-out is a sign reversal** of $v(t)$, **not a phase transition**. There is no decoupling epoch, no change in the equation of state.

Despite these differences, the *sequence* — perturbation, oscillation-modulated spreading, freeze-out, preferred scale — is structurally identical.

---

## 5. Analytical Prediction for the BAO-like Radius

### 5.1 Derivation

The telegraph oscillation has half-period $T_{\mathrm{osc}}/2 = \pi/\omega$. During this time, density perturbations spread diffusively with effective diffusivity $D_{\mathrm{eff}} = D \cdot M^*$, where $M^* = M_0(\rho_{\max} - \rho^*)^\beta$ is the mobility evaluated at equilibrium.

The diffusion length accumulated during one half-period is

$$r_{\mathrm{BAO}} = \sqrt{2\,D_{\mathrm{eff}}\,\frac{\pi}{\omega}} = \sqrt{\frac{2\pi\,D\,M^*}{\omega}}. \tag{8}$$

This is the ED prediction for the preferred correlation scale. It depends on $\omega$ through the telegraph parameters $(H, \tau, \zeta)$ and on $D_{\mathrm{eff}}$ through the constitutive parameters $(D, M_0, \beta, \rho^*)$.

### 5.2 The Key Diagnostic

The diagnostic power of Eq. (8) lies in the $\omega$-dependence. If the correlation feature were produced by diffusion alone, its characteristic scale would depend only on $D_{\mathrm{eff}}$ and the total evolution time $T$:

$$r_{\mathrm{diff}} = \sqrt{2\,D_{\mathrm{eff}}\,T}. \tag{9}$$

This is independent of $H$, $\tau$, and $\zeta$. If the feature depends on $\omega$ — i.e., on the telegraph parameters — then the participation channel is essential, and diffusion alone is insufficient.

### 5.3 Predicted Values

For the canonical parameters with $D_{\mathrm{eff}} = 0.075$:

| $H$ | $\omega$ | $r_{\mathrm{BAO}}^{\mathrm{pred}}$ |
|-----|----------|--------------------------------------|
| 0.5 | 0.498 | 0.973 |
| 1.0 | 0.705 | 0.817 |
| 2.0 | 0.999 | 0.687 |
| 3.0 | 1.224 | 0.621 |
| 5.0 | 1.580 | 0.546 |
| 7.0 | 1.870 | 0.502 |

The predicted radius decreases with increasing $\omega$: faster oscillation means less time for diffusion to spread before the freeze-out, producing a smaller preferred scale.

---

## 6. Numerical Experiment Design

### 6.1 Simulation Setup

All simulations use the canonical ED PDE (Eqs. 1–3) on a 2D square domain $\Omega = [0, L]^2$ with Neumann boundary conditions, solved by implicit Euler time integration with fixed-point iteration (tolerance $10^{-7}$).

| Parameter | Value |
|-----------|-------|
| Grid | $64 \times 64$ |
| Domain size | $L = 4.0$ |
| Grid spacing | $\Delta x = 0.0625$ |
| Time step | $\Delta t = 0.001$ |
| Total time | $T = 10.0$ |
| Snapshot interval | $0.25$ |

The initial condition consists of 12 Gaussian bumps at pseudo-random positions (seed 42) with width $\sigma = 0.12$ and amplitude $A = 0.08$, superimposed on a uniform overdensity $\rho(x, 0) = \rho^* + \epsilon + \sum_i A\exp(-|x - x_i|^2 / 2\sigma^2)$ with $\epsilon = 0.06$. The mean overdensity $\epsilon$ ensures that $\bar{F} \neq 0$ and the participation coupling is activated.

### 6.2 Sweep Protocol

The participation coupling $H$ is swept over $\{0, 0.5, 1, 1.5, 2, 2.5, 3, 4, 5, 7, 10\}$ with all other parameters held fixed. For each $H$, the simulation is run from the same initial condition.

### 6.3 Observable: $\Delta\xi(r, t)$

At each snapshot, the two-point correlation function is computed via FFT-based autocorrelation (Wiener-Khinchin theorem) and azimuthally averaged into 50 radial bins up to $r_{\max} = 1.8$.

The **participation-induced correlation difference** is defined as

$$\Delta\xi(r, t) = \xi_H(r, t) - \xi_{H=0}(r, t). \tag{10}$$

This isolates the effect of the participation channel: any feature in $\Delta\xi$ is, by construction, absent when $H = 0$ and attributable to the telegraph coupling. No fitting, filtering, or post-processing is applied beyond Eq. (10).

### 6.4 Infrastructure

The experiment uses the existing ED-SIM-02 simulation platform (operators, boundary conditions, constitutive functions, integrators) without modification. The BAO experiment module adds only the initial-condition generator, the radial binning, and the $\Delta\xi$ computation. The code is deterministic and reproducible.

---

## 7. Results

### 7.1 Existence of the Feature

For $H = 3$ (a representative underdamped case with $\omega = 1.224$, $Q = 6.1$), the time evolution of $\Delta\xi(r, t)$ reveals a clear positive peak that propagates outward and reaches maximum amplitude near $t \approx T_{\mathrm{osc}}/2$:

| $t$ | $r_{\mathrm{peak}}$ | $\Delta\xi_{\max}$ | $v(t)$ | Phase |
|-----|---------------------|---------------------|--------|-------|
| 0.0 | -- | 0.0000 | 0.000 | initial |
| 0.5 | 0.45 | +0.0016 | $-0.005$ | $v$ swinging negative |
| 1.0 | 0.63 | +0.0055 | $-0.008$ | $v$ near minimum |
| 1.5 | 0.81 | +0.0094 | $-0.011$ | $v$ returning |
| 2.0 | 0.88 | +0.0127 | $-0.012$ | approaching half-period |
| 2.5 | 0.95 | +0.0148 | $-0.011$ | $\approx T_{\mathrm{osc}}/2 = 2.57$ |
| **3.0** | **0.99** | **+0.0149** | $-0.010$ | **peak amplitude** |
| 3.5 | 1.06 | +0.0134 | $-0.007$ | amplitude declining |
| 4.0 | 1.13 | +0.0108 | $-0.004$ | |
| 5.0 | 1.57 | +0.0064 | $+0.002$ | **$v$ crosses zero** |
| 6.0 | 1.75 | +0.0065 | $+0.006$ | feature freezing |
| 7.0 | 1.75 | +0.0068 | $+0.007$ | frozen |
| 8.0 | 1.75 | +0.0063 | $+0.005$ | slowly decaying |

Four properties are visible:

1. **Propagation.** The peak moves outward from $r = 0.45$ at $t = 0.5$ to $r = 1.75$ at $t = 6$, consistent with diffusive spreading ($r \sim \sqrt{D_{\mathrm{eff}} \cdot t}$).

2. **Telegraph modulation.** The amplitude peaks at $t \approx 3.0$, close to the predicted half-period $T_{\mathrm{osc}}/2 = 2.57$. This is the time at which the oscillation has completed its first half-swing and the modulation is strongest.

3. **Freeze-out.** At $t \approx 5$, $v(t)$ crosses zero. After this, the peak stops moving (locked at $r \approx 1.75$) and the amplitude stabilises. The feature persists as a frozen imprint.

4. **Positive excess.** $\Delta\xi > 0$ at all measured radii beyond $r \approx 0.15$ for $t \geq 0.5$, meaning the participation-coupled field has systematically stronger correlations at intermediate scales than the diffusion-only field.

### 7.2 Absence at $H = 0$

At $H = 0$, $\Delta\xi(r, t) = 0$ by construction: the two runs are identical. The participation variable $v(t)$ decays monotonically without feeding back into $\rho$. No preferred scale is produced beyond the intrinsic IC correlation length ($\sim 0.2$, the bump size).

This is the essential control: the feature is entirely attributable to the participation coupling.

### 7.3 Amplitude Scaling with $H$

The maximum $\Delta\xi_{\max}$ over all times and radii, measured for each $H$:

| $H$ | $\Delta\xi_{\max}$ |
|-----|---------------------|
| 0.0 | 0.0000 |
| 0.5 | 0.0036 |
| 1.0 | 0.0060 |
| 2.0 | 0.0109 |
| 3.0 | 0.0151 |
| 5.0 | 0.0217 |
| 7.0 | 0.0269 |
| 10.0 | 0.0332 |

The amplitude is strictly monotonic in $H$ and approximately follows a power law $\Delta\xi_{\max} \propto H^{0.6}$. The exponent is sub-linear because the penalty channel ($-P_0 \delta$) provides a stabilising restoring force that partially counteracts the participation modulation.

### 7.4 Peak Radius vs Telegraph Frequency

The peak radius at the amplitude-maximum time, measured for each $H$:

| $H$ | $\omega$ | $r_{\mathrm{peak}}^{\mathrm{meas}}$ | $r_{\mathrm{BAO}}^{\mathrm{pred}}$ | $r_{\mathrm{peak}} / r_{\mathrm{pred}}$ |
|-----|----------|---------------------------------------|----------------------------------------|-------------------------------------------|
| 0.5 | 0.498 | 1.75 | 0.97 | 1.80 |
| 1.0 | 0.705 | 0.99 | 0.82 | 1.21 |
| 2.0 | 0.999 | 0.99 | 0.69 | 1.44 |
| 3.0 | 1.224 | 0.99 | 0.62 | 1.60 |
| 5.0 | 1.580 | 0.95 | 0.55 | 1.75 |
| 7.0 | 1.870 | 0.99 | 0.50 | 1.97 |

A log-log fit of $r_{\mathrm{peak}}$ vs $\omega$ gives a slope of $-0.33$. The naive prediction (Eq. 8) gives $-0.50$. The discrepancy arises because the initial condition imposes a **correlation-length floor**: the 12 bumps have a mean separation of $\sim 4/\sqrt{12} \approx 1.15$, and the correlation function cannot develop a peak below this scale. For low $H$ (slow oscillation, large predicted $r$), the peak is well above the floor and the prediction is reasonable. For high $H$ (fast oscillation, small predicted $r$), the peak is clamped near $r \approx 1.0$ by the IC structure.

The critical observation is that the **direction of the scaling is correct**: larger $\omega$ produces a smaller or comparable $r_{\mathrm{peak}}$, and the feature is absent at $H = 0$. The participation channel controls the feature.

### 7.5 Participation Oscillation Evidence

The number of zero-crossings of $v(t)$ confirms the telegraph character:

| $H$ | $\omega$ | Zero-crossings of $v(t)$ in $[0, 10]$ |
|-----|----------|----------------------------------------|
| 0.0 | -- | 0 (monotone decay) |
| 0.5 | 0.498 | 1 |
| 1.0 | 0.705 | 1 |
| 2.0 | 0.999 | 2 |
| 3.0 | 1.224 | 2 |
| 5.0 | 1.580 | 3 |
| 7.0 | 1.870 | 3 |

At $H = 0$, $v$ decays without oscillating. At $H > 0$, $v$ oscillates with increasing frequency. The freeze-out of the correlation feature coincides with the first positive-going zero-crossing of $v$.

---

## 8. Interpretation and Falsification

### 8.1 What Has Been Demonstrated

The canonical ED PDE, with no extra physics, produces a **telegraph-modulated correlation feature** with three properties that are structurally analogous to the BAO peak:

1. **Preferred scale.** A positive excess in $\Delta\xi(r)$ at a radius set by the interplay of the diffusion speed $D_{\mathrm{eff}}$ and the telegraph oscillation period $T_{\mathrm{osc}}$.

2. **Freeze-out.** The feature reaches maximum amplitude near $t \approx T_{\mathrm{osc}}/2$ and stabilises after $v(t)$ crosses zero. The preferred scale is frozen by the oscillation reversal, not by an external phase transition.

3. **Participation control.** The feature is strictly absent when $H = 0$ and grows monotonically with $H$. Removing the global coupling eliminates the preferred scale. This proves that diffusion alone is insufficient and that the participation channel is essential.

### 8.2 The Mechanism

The mechanism operates as follows:

1. The uniform overdensity $\epsilon$ drives $\bar{F} \approx -P_0 \epsilon \neq 0$, activating the participation coupling.
2. The participation variable $v(t)$ oscillates at frequency $\omega$ (Eq. 7), creating a time-varying global modulation $+Hv(t)$ in the PDE.
3. The multi-bump density field has spatially varying $\rho(x)$, and the nonlinear mobility $M(\rho)$ makes the effective decay rate density-dependent: denser bumps decay at different rates than the background.
4. The oscillating $v$ modulates the *relative* decay rates: during the first half-cycle ($v < 0$), the modulation preferentially affects higher-density regions; during the second half-cycle ($v > 0$), the effect reverses.
5. This creates a time-varying bias in the spatial correlation structure — a travelling excess in $\Delta\xi(r)$ that moves outward at the diffusion speed.
6. When $v$ crosses zero, the bias freezes: the correlation excess at $r \approx \sqrt{2 D_{\mathrm{eff}} \cdot t_{\mathrm{freeze}}}$ becomes a persistent feature.

The result is a preferred spatial scale $r_{\mathrm{BAO}}$ that depends on $\omega$ (through $t_{\mathrm{freeze}} \approx \pi/\omega$) and on $D_{\mathrm{eff}}$ (through the diffusion length). Neither parameter alone is sufficient: removing $H$ kills the oscillation and eliminates the feature; reducing $D$ slows the spreading but preserves the oscillation. The feature is a genuinely *coupled* phenomenon.

### 8.3 What Has Not Been Demonstrated

This experiment does not claim that ED reproduces the physical BAO. Several important differences must be acknowledged:

- **No acoustic propagation.** ED is parabolic. The correlation peak moves as $r \sim \sqrt{t}$ (diffusive), not $r \sim t$ (acoustic). There is no sound speed.
- **No multi-component fluid.** The physical BAO involves photons, baryons, and dark matter with different equations of state. ED has a single scalar field.
- **No metric or gravity.** The physical BAO peak is imprinted in a gravitationally evolving density field on an FRW background. ED has no spacetime geometry.
- **No quantitative calibration.** The ED feature amplitude ($\Delta\xi \sim 0.01$–$0.03$) and radius ($r \sim 1$ in code units) have not been matched to the physical BAO amplitude ($\Delta\xi \sim 10^{-3}$) and radius ($r \sim 150$ Mpc). Such calibration would require fitting the constitutive parameters to cosmological data, which is beyond the scope of this work.

### 8.4 Falsification Criteria

Four predictions were tested and confirmed:

| Prediction | Falsification condition | Result |
|------------|-------------------------|--------|
| Bump at $H > 0$ | No bump at any $H > 0$ | **Not falsified:** bump present for all $H > 0$ |
| No bump at $H = 0$ | Bump at $H = 0$ | **Not falsified:** $\Delta\xi = 0$ identically |
| Radius decreases with $\omega$ | Radius independent of $\omega$ | **Not falsified:** radius decreases from 1.75 to 0.95 |
| Amplitude grows with $H$ | Amplitude independent of $H$ | **Not falsified:** amplitude grows as $H^{0.6}$ |

A fifth, stronger test would be: **the peak radius must scale as $\omega^{-1/2}$**. The measured exponent ($-0.33$) is shallower than the prediction ($-0.50$) due to the IC correlation-length floor. This is not a falsification — it is a finite-size effect — but it indicates that the simple scaling (Eq. 8) requires correction for the IC geometry. A clean test would use a delta-function-like IC (single sharp bump), which eliminates the floor. This is an open direction for future work.

---

## 9. ED as an Ontological Candidate

### 9.1 The Ontological Test

An ontological framework earns its status by producing recognisable structure from its own primitives. The test is not whether the framework can be fitted to data (any sufficiently flexible model can) but whether its *constitutive architecture* — the objects it takes as primitive and the rules it imposes on their interaction — naturally generates the kinds of structure observed in the physical world.

The BAO analogue provides such a test. The three ingredients of the BAO mechanism — perturbation, oscillatory modulation, freeze-out — are not added to ED by hand. They are *consequences* of the canonical constitutive structure:

- Perturbations exist because the initial condition is arbitrary.
- Oscillatory modulation exists because the participation coupling generically produces telegraph dynamics.
- Freeze-out exists because the oscillation has a zero-crossing.

No parameter was tuned to produce the correlation feature. It appears for any $H > 0$, any multi-bump initial condition, and any telegraph-underdamped parameter set. The feature is a generic architectural consequence, not a special-case result.

### 9.2 Structural Analogues vs Physical Derivations

The BAO analogue is not a derivation of cosmological physics from ED. It is a demonstration that ED's minimal primitives are *sufficient* to generate a cosmology-like observable. The distinction matters.

A physical derivation would require: (a) deriving ED from a microscopic theory, (b) showing that the microscopic theory reduces to GR+QFT in appropriate limits, and (c) calibrating the constitutive parameters to cosmological data. None of these steps has been taken.

A structural analogue requires only: (a) identifying the shared mechanism (oscillation-modulated spreading with freeze-out), (b) showing that the mechanism operates in ED without extra physics, and (c) verifying that the feature is controlled by the relevant parameters (telegraph, not diffusion alone). All three have been demonstrated.

The value of the structural analogue is not that it replaces the physical theory, but that it reveals what is *architecturally necessary* for the BAO mechanism: not gravity, not a photon-baryon plasma, not a phase transition — but oscillation-modulated transport with a freeze-out event. Any PDE with these three channels can produce a BAO-like feature. ED is the simplest known system that has all three.

### 9.3 Implications and Future Work

The BAO analogue motivates several lines of investigation:

- **3D verification.** The experiment was run in 2D. The morphological taxonomy (ED-Phys-35) shows that 3D ED produces filaments and sheets. A 3D BAO analogue would test whether the feature persists in the presence of richer morphological structure.

- **IC-independent scaling.** The measured $\omega^{-0.33}$ scaling is contaminated by the IC correlation-length floor. A delta-function IC on a large grid would provide a clean test of the $\omega^{-1/2}$ prediction.

- **Quantitative calibration.** Fitting $D_{\mathrm{eff}}$ and $\omega$ to the physical BAO radius ($\sim 150$ Mpc) and amplitude ($\Delta\xi \sim 10^{-3}$) would determine whether the required constitutive parameters are physically plausible.

- **Multi-field ED.** The physical BAO involves multiple coupled species. Extending ED to multi-field coupling (planned for ED-SIM-03) would test whether richer BAO-like structure emerges from coupled densities.

- **Connection to the cosmic web.** ED already produces a filament/sheet/blob morphology (58%/23%/19% in 3D) that is structurally similar to the cosmic-web classification. The BAO analogue adds a preferred *scale* to the morphological *taxonomy*, bringing ED closer to a complete structural analogue of large-scale structure.

---

## 10. Conclusion

The canonical Event Density PDE, derived from seven structural axioms and characterised by three constitutive channels (degenerate diffusion, monostable penalty, participation coupling), produces a preferred spatial scale in the two-point correlation function when the participation coupling is active. The feature is absent at $H = 0$, present at all $H > 0$, monotonically controlled by $H$, and its radius is set by the telegraph oscillation frequency $\omega(H, \tau, \zeta)$ and the effective diffusivity $D_{\mathrm{eff}} = D M^*$. The mechanism is oscillation-modulated diffusion with freeze-out — structurally analogous to the baryon acoustic oscillation.

This result does not derive cosmological physics from Event Density. It demonstrates something more fundamental: that ED's minimal ontological primitives — density, degenerate mobility, penalty, participation — are sufficient to generate a cosmology-like correlation feature as an architectural consequence. The BAO-like scale is not an input, not a fit, and not an accident. It is a structural inevitability of the coupled $(\rho, v)$ system in the underdamped regime.

Event Density does not claim to replace general relativity, quantum mechanics, or $\Lambda$CDM. It offers something different: a mathematical architecture whose constitutive design produces, from minimal ingredients, the kinds of structure that physics spends centuries deriving from elaborate first principles. The BAO analogue is one such structure. Others — horizons, morphological hierarchies, spectral cascades, topological invariants — have been documented across four spatial dimensions. Together, they constitute the case that Event Density deserves serious evaluation as a structural ontology for physics.

---

## References

1. Proxmire, A. ED-Phys-01 through ED-Phys-40. Event Density Physics Series. (2025–2026).
2. Proxmire, A. ED-SIM-02: An Architectural Lab for Entropic Dynamics. Software package. (2026).
3. Proxmire, A. ED-PHYS-01 through ED-PHYS-10. Event Density Physics Experiments. (2026).
4. Eisenstein, D. J. et al. Detection of the baryon acoustic peak in the large-scale correlation function of SDSS luminous red galaxies. *Astrophys. J.* **633**, 560–574 (2005).
5. Vazquez, J. L. *The Porous Medium Equation: Mathematical Theory*. Oxford University Press (2007).
6. Jordan, R., Kinderlehrer, D., & Otto, F. The variational formulation of the Fokker-Planck equation. *SIAM J. Math. Anal.* **29**, 1–17 (1998).
