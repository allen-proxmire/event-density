# ED-Phys-05 Execution: Solving the Participation Field

## From Conceptual Analysis to Complete, Testable, Falsifiable Framework

**Author:** Allen Proxmire
**Series:** ED-Phys-05 (Execution Phase)
**Date:** March 2026
**Status:** Complete derivation with numerical experiment specifications
**Prerequisite:** ED-Phys-05 conceptual analysis; ED-SIM-02 simulation engine (v0.1.0, 112 tests passing)

---

## Table of Contents

1. [The Madelung Mapping: Complete Derivation](#1-the-madelung-mapping-complete-derivation)
2. [Anchoring H to the Compton Frequency](#2-anchoring-h-to-the-compton-frequency)
3. [Interpreting γ Across Regimes](#3-interpreting-γ-across-regimes)
4. [Key Predictions: Derivation and Falsification](#4-key-predictions-derivation-and-falsification)
5. [Coherence Tests: Detailed Protocols](#5-coherence-tests-detailed-protocols)
6. [Numerical Experiment Templates](#6-numerical-experiment-templates)
7. [Completed Interpretation: Final Statement](#7-completed-interpretation-final-statement)

---

# 1. The Madelung Mapping: Complete Derivation

## 1.1 The ED Coupled System as Implemented

The ED-SIM-02 codebase implements the following coupled system (see `edsim/core/operators.py` line 324 and `edsim/core/participation.py` lines 39–40):

**Density equation:**

$$\partial_t \rho = D\,F_{\text{local}}[\rho] + H\,v(t)$$

where $F_{\text{local}}[\rho] = M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho)$ combines the mobility and penalty channels.

**Participation equation:**

$$\dot{v} = \frac{1}{\tau}\bigl(\bar{F} - \zeta\,v\bigr)$$

where $\bar{F} = \langle D\,F_{\text{local}}[\rho] \rangle$ is the volume-averaged local forcing, computed as `np.mean(F)` (see `participation.py` line 71).

The codebase uses the $(\tau, \zeta)$ parameterisation. The connection to the standard telegraph parameters $(\gamma, \omega_0)$ used in the conceptual analysis is (see `rc_debye.py` lines 113–114):

$$\gamma = \frac{D P_0 + \zeta/\tau}{2}, \qquad \omega_0^2 = \frac{D P_0 \zeta + H P_0}{\tau}$$

The exact exponential integrator for $v(t)$ is:

$$v(t + \Delta t) = v(t)\,e^{-\zeta\Delta t/\tau} + \frac{\bar{F}}{\zeta}\bigl(1 - e^{-\zeta\Delta t/\tau}\bigr)$$

This is the exact solution of the linear ODE for constant $\bar{F}$ over the timestep $\Delta t$.

## 1.2 The Madelung Equations

Write the quantum wave function as $\psi = \sqrt{\rho}\,e^{iS/\hbar}$ where $\rho(\mathbf{x},t) = |\psi|^2$ is the probability density and $S(\mathbf{x},t)$ is the phase. The Schrödinger equation $i\hbar\partial_t\psi = -(\hbar^2/2m)\nabla^2\psi + V\psi$ separates into:

**Continuity equation:**

$$\partial_t \rho + \nabla\!\cdot\!(\rho\,\mathbf{u}) = 0 \tag{M1}$$

**Hamilton–Jacobi equation:**

$$\partial_t S + \frac{|\nabla S|^2}{2m} + V + Q = 0 \tag{M2}$$

where $\mathbf{u} = \nabla S/m$ is the Madelung velocity field and $Q = -(\hbar^2/2m)(\nabla^2\sqrt{\rho}/\sqrt{\rho})$ is the quantum potential.

The Euler form of (M2) is obtained by taking $\nabla/m$ of both sides:

$$\partial_t \mathbf{u} + (\mathbf{u}\cdot\nabla)\mathbf{u} = -\frac{1}{m}\nabla(V + Q) \tag{M3}$$

The Madelung system has two field-valued degrees of freedom: $\rho(\mathbf{x},t)$ and $\mathbf{u}(\mathbf{x},t)$.

## 1.3 Spatial Averaging of the Euler Equation

Define the spatial average over a domain $\Omega$ with volume $|\Omega|$:

$$\langle f \rangle = \frac{1}{|\Omega|}\int_\Omega f\,d^d x$$

Apply $\langle\cdot\rangle$ to (M3):

$$\frac{d\langle\mathbf{u}\rangle}{dt} = -\frac{1}{m}\langle\nabla(V + Q)\rangle - \langle(\mathbf{u}\cdot\nabla)\mathbf{u}\rangle \tag{1}$$

The left-hand side uses:

$$\langle\partial_t\mathbf{u}\rangle = \frac{d}{dt}\langle\mathbf{u}\rangle$$

which holds because the domain $\Omega$ is fixed (Neumann or periodic boundaries in ED-SIM-02).

**Decomposition of the nonlinear advection term.** Write $\mathbf{u} = \langle\mathbf{u}\rangle + \mathbf{u}'$ where $\mathbf{u}'$ is the fluctuation ($\langle\mathbf{u}'\rangle = 0$ by construction). Then:

$$(\mathbf{u}\cdot\nabla)\mathbf{u} = (\langle\mathbf{u}\rangle\cdot\nabla)\langle\mathbf{u}\rangle + (\langle\mathbf{u}\rangle\cdot\nabla)\mathbf{u}' + (\mathbf{u}'\cdot\nabla)\langle\mathbf{u}\rangle + (\mathbf{u}'\cdot\nabla)\mathbf{u}'$$

Taking the spatial average:

$$\langle(\mathbf{u}\cdot\nabla)\mathbf{u}\rangle = \underbrace{(\langle\mathbf{u}\rangle\cdot\nabla)\langle\mathbf{u}\rangle}_{\text{mean advection}} + \underbrace{\langle(\mathbf{u}'\cdot\nabla)\mathbf{u}'\rangle}_{\text{Reynolds stress}} \tag{2}$$

The cross terms vanish: $\langle(\langle\mathbf{u}\rangle\cdot\nabla)\mathbf{u}'\rangle = (\langle\mathbf{u}\rangle\cdot\nabla)\langle\mathbf{u}'\rangle = 0$ and similarly $\langle(\mathbf{u}'\cdot\nabla)\langle\mathbf{u}\rangle\rangle = \langle\mathbf{u}'\rangle\cdot\nabla\langle\mathbf{u}\rangle = 0$ (since $\langle\mathbf{u}\rangle$ is spatially constant, its gradient vanishes).

The mean advection term also vanishes because $\langle\mathbf{u}\rangle$ is spatially uniform: $(\langle\mathbf{u}\rangle\cdot\nabla)\langle\mathbf{u}\rangle = 0$.

This leaves:

$$\frac{d\langle\mathbf{u}\rangle}{dt} = -\frac{1}{m}\langle\nabla(V + Q)\rangle - \langle(\mathbf{u}'\cdot\nabla)\mathbf{u}'\rangle \tag{3}$$

Equation (3) is exact. The first term is the mean force. The second term — the Reynolds stress — represents the effect of velocity fluctuations on the mean flow. It is the *closure problem*: we cannot evaluate $\langle(\mathbf{u}'\cdot\nabla)\mathbf{u}'\rangle$ without knowing the full spatial structure of $\mathbf{u}'$.

## 1.4 The Mean-Field Closure: From Madelung to ED

**Assumption 1 (Linear damping closure).** Replace the Reynolds stress with a linear drag on the mean velocity:

$$\langle(\mathbf{u}'\cdot\nabla)\mathbf{u}'\rangle \approx \frac{\zeta}{\tau}\langle\mathbf{u}\rangle \tag{A1}$$

This is the simplest closure that:
- Is dissipative (extracts energy from the mean flow into fluctuations)
- Vanishes when $\mathbf{u}$ is spatially uniform ($\mathbf{u}' = 0 \Rightarrow$ Reynolds stress = 0)
- Has a single free parameter (the ratio $\zeta/\tau$, which sets the effective friction)

**Assumption 2 (Force identification).** Identify the mean force with the ED spatial-average forcing:

$$-\frac{1}{m}\langle\nabla(V + Q)\rangle \longleftrightarrow \frac{H}{\tau}\bar{F}[\rho] \tag{A2}$$

This maps the quantum potential gradient to the penalty channel and the external potential gradient to the mobility/diffusion channel, with $H/\tau$ as the proportionality constant.

**Assumption 3 (Scalar reduction).** Project the vector equation onto a single scalar:

$$\langle\mathbf{u}\rangle \longleftrightarrow v(t) \tag{A3}$$

In $d = 1$ this is exact. In $d > 1$, it amounts to tracking only one component of the mean velocity, or equivalently, working with the magnitude in situations where the mean flow is unidirectional.

**Result.** Under assumptions A1–A3, equation (3) becomes:

$$\dot{v} = \frac{1}{\tau}\bigl(\bar{F} - \zeta\,v\bigr) \tag{4}$$

This is exactly the ED participation equation as implemented in `edsim/core/participation.py`.

## 1.5 Assumptions Required for the Mapping

| # | Assumption | Mathematical statement | Physical meaning |
|---|-----------|----------------------|-----------------|
| A1 | Linear damping closure | $\langle(\mathbf{u}'\cdot\nabla)\mathbf{u}'\rangle = (\zeta/\tau)\langle\mathbf{u}\rangle$ | Velocity fluctuations act as friction on mean flow |
| A2 | Force identification | $-\langle\nabla(V+Q)\rangle/m = (H/\tau)\bar{F}[\rho]$ | Mean quantum/potential force maps to ED forcing |
| A3 | Scalar reduction | $\langle\mathbf{u}\rangle \to v(t) \in \mathbb{R}$ | Track global scalar, not vector field |

**Additional implicit assumptions:**
- The domain $\Omega$ is fixed with Neumann or periodic boundaries (no moving boundaries).
- The density field $\rho$ remains positive and bounded ($0 < \rho \leq \rho_{\max}$).
- The velocity field $\mathbf{u} = \nabla S/m$ is irrotational (guaranteed by the Madelung structure).

## 1.6 Where the Mapping Breaks

The mapping breaks in three identifiable regimes:

**Regime 1: Rich spatial structure in $\mathbf{u}(\mathbf{x},t)$.** When the velocity field has strong spatial variation — interference fringes, vortex lattices (in multiply-connected domains), or multi-valued phase — the Reynolds stress $\langle(\mathbf{u}'\cdot\nabla)\mathbf{u}'\rangle$ is large and poorly approximated by linear damping. In this regime, the full Madelung system carries information that ED's scalar $v(t)$ cannot represent.

*Physical implication:* ED should underperform Schrödinger in describing interference experiments with many spatial modes. The participation field averages over the interference pattern, capturing only the net drift.

**Regime 2: Topological defects in $S(\mathbf{x},t)$.** When the phase $S$ has branch cuts (quantised vortices in 2D, vortex lines in 3D), the velocity field $\mathbf{u} = \nabla S/m$ has singularities. The spatial average $\langle\mathbf{u}\rangle$ is well-defined but may not represent the dynamics. Vortex–antivortex annihilation, for example, changes the topology of the flow without necessarily changing $\langle\mathbf{u}\rangle$.

*Physical implication:* ED cannot describe quantum turbulence or vortex dynamics. These require the full field $\mathbf{u}(\mathbf{x},t)$.

**Regime 3: Multiple length scales.** When the system has well-separated length scales (e.g., a slowly varying envelope modulating a rapid oscillation), the spatial average conflates the fast and slow dynamics. The closure A1 implicitly assumes a single characteristic scale for the velocity fluctuations.

*Physical implication:* ED is a single-scale theory. Multi-scale quantum systems (WKB regime, semiclassical limit) may require a hierarchy of participation fields or a spatially-resolved generalisation.

**What the breakdowns imply for ED as a physics framework:** The breakdowns define ED's domain of validity. ED is *not* a replacement for the full Schrödinger equation in all regimes — it is a mean-field theory that captures the global flow dynamics and trades spatial resolution for structural clarity. The breakdowns are predictions: they identify experiments where ED and Schrödinger must disagree, which are testable.

---

# 2. Anchoring $H$ to the Compton Frequency

## 2.1 The Telegraph Propagation Speed

The coupled ED system, linearised around equilibrium $\rho = \rho^*$, $v = 0$, with perturbation $\delta(\mathbf{x},t) = \rho - \rho^*$ and participation $v(t)$, gives:

$$\partial_t \delta = D\nabla^2\delta - D P_0 \delta + H v \tag{5}$$

$$\dot{v} = \frac{1}{\tau}\bigl(D\langle\nabla^2\delta - P_0\delta\rangle - \zeta v\bigr) \tag{6}$$

For a single Fourier mode $\delta \propto e^{i\mathbf{k}\cdot\mathbf{x}}$, we have $\langle\nabla^2\delta\rangle = -k^2\langle\delta\rangle$ and $\langle\delta\rangle = \delta$ (for a single-mode perturbation spanning the domain). Substituting and eliminating $v$ by differentiating (5) and using (6):

$$\ddot{\delta} + \Bigl(Dk^2 + DP_0 + \frac{\zeta}{\tau}\Bigr)\dot{\delta} + \frac{\zeta}{\tau}(Dk^2 + DP_0)\delta + \frac{H}{\tau}(Dk^2 + DP_0)\delta = 0$$

Rearranging:

$$\ddot{\delta} + \underbrace{\Bigl(Dk^2 + DP_0 + \frac{\zeta}{\tau}\Bigr)}_{2\gamma_{\text{eff}}(k)}\dot{\delta} + \underbrace{\Bigl[\frac{\zeta + H}{\tau}(Dk^2 + DP_0)\Bigr]}_{\omega^2(k)}\delta = 0 \tag{7}$$

This is a damped oscillator for each wavenumber $k$. The dispersion relation in the high-$k$ limit gives the propagation speed:

$$c_{\text{ED}}^2 = \lim_{k\to\infty}\frac{\omega^2(k)}{k^2} = \frac{(\zeta + H)D}{\tau} \tag{8}$$

For $H \gg \zeta$ (the participation-dominated regime):

$$c_{\text{ED}}^2 \approx \frac{H\,D}{\tau} \tag{9}$$

In the simplified parameterisation where $\tau = 1$ (as used in several analogues), this reduces to:

$$c_{\text{ED}}^2 = H \cdot D \tag{10}$$

## 2.2 Dimensional Analysis

In the quantum regime:

| Quantity | Symbol | Dimensions | Quantum value |
|----------|--------|-----------|--------------|
| Diffusion coefficient | $D$ | $[L^2\,T^{-1}]$ | $\hbar/(2m)$ |
| Participation coupling | $H$ | $[T^{-1}]$ | to be determined |
| Telegraph speed | $c_{\text{ED}}$ | $[L\,T^{-1}]$ | target: $c$ |

From equation (10):

$$[c_{\text{ED}}]^2 = [H] \cdot [D] = [T^{-1}] \cdot [L^2 T^{-1}] = [L^2 T^{-2}] \;\checkmark$$

Setting $c_{\text{ED}} = c$:

$$c^2 = H \cdot \frac{\hbar}{2m}$$

$$\boxed{H = \frac{2mc^2}{\hbar}} \tag{11}$$

The right-hand side is twice the Compton angular frequency:

$$H = 2\omega_C, \qquad \omega_C = \frac{mc^2}{\hbar}$$

## 2.3 Verification Across Particle Masses

The product $D \cdot H$ must equal $c^2$ independent of particle mass:

$$D \cdot H = \frac{\hbar}{2m} \cdot \frac{2mc^2}{\hbar} = c^2 \;\checkmark$$

The mass cancels identically. Numerically:

| Particle | $m$ (kg) | $D = \hbar/(2m)$ (m²/s) | $H = 2mc^2/\hbar$ (s⁻¹) | $\sqrt{DH}$ (m/s) |
|----------|----------|--------------------------|--------------------------|---------------------|
| Electron | $9.109 \times 10^{-31}$ | $5.789 \times 10^{-5}$ | $1.553 \times 10^{21}$ | $2.998 \times 10^{8}$ |
| Proton | $1.673 \times 10^{-27}$ | $3.153 \times 10^{-8}$ | $2.854 \times 10^{24}$ | $2.998 \times 10^{8}$ |
| Muon | $1.884 \times 10^{-28}$ | $2.800 \times 10^{-7}$ | $3.213 \times 10^{23}$ | $2.998 \times 10^{8}$ |
| Planck mass | $2.176 \times 10^{-8}$ | $2.422 \times 10^{-27}$ | $3.712 \times 10^{43}$ | $2.998 \times 10^{8}$ |

The result $\sqrt{DH} = c$ is exact for all masses. This is not a numerical coincidence — it is an algebraic identity.

## 2.4 Why This Anchoring Is Structurally Required

**The parabolic problem.** Without participation ($H = 0$), the ED density equation $\partial_t\rho = D\nabla\!\cdot\!(M(\rho)\nabla\rho) - DP(\rho)$ is parabolic. Parabolic PDEs have infinite propagation speed: a compactly supported perturbation produces nonzero $\rho$ everywhere at any $t > 0$ (modulo the degenerate mobility, which provides finite speed via the free boundary, but only in the nonlinear PME regime).

This is the same mathematical pathology as the Schrödinger equation itself: probability density "leaks" instantaneously to spatial infinity, though with exponentially small amplitude.

**The telegraph resolution.** With $H > 0$, the coupled $(\rho, v)$ system becomes hyperbolic at short times (equation 7 is a damped wave equation in the high-$k$ limit). The telegraph structure provides a finite maximum propagation speed $c_{\text{ED}} = \sqrt{DH/\tau}$.

**The uniqueness of the Compton anchoring.** In any regime where the speed of light is the causal limit, the requirement $c_{\text{ED}} = c$ uniquely determines $H$:

$$H = \frac{c^2\,\tau}{D} \tag{12}$$

With $\tau = 1$ and $D = \hbar/(2m)$ in the quantum regime, this gives $H = 2mc^2/\hbar$ — the Compton frequency. This is the *only* value of $H$ that makes the quantum-regime ED PDE causal.

**What this means for ED.** The participation channel is not optional in the quantum regime. It is required by causality. Setting $H = 0$ gives a mathematically consistent but physically inadmissible theory (superluminal probability propagation). The Compton anchoring closes this gap: it fixes $H$ uniquely, leaving $\gamma$ (equivalently $\zeta/\tau$) as the only remaining free parameter in the quantum-regime participation channel.

## 2.5 Consequences for the Quantum Regime

1. **The ED PDE has a built-in speed limit.** At times $t \lesssim \tau/\zeta$ (before damping sets in), the density perturbation propagates as a wave at speed $c$. At times $t \gg \tau/\zeta$, it transitions to diffusive spreading. The crossover timescale is $t_{\text{cross}} = \tau/\zeta$.

2. **The oscillation frequency is fixed.** In the uniform limit, the telegraph frequency is $\omega_0 = \sqrt{(\zeta + H)DP_0/\tau}$. With $H = 2\omega_C \gg \zeta$, this gives $\omega_0 \approx \sqrt{2\omega_C D P_0/\tau}$. For the electron ($\omega_C \approx 7.76 \times 10^{20}$ rad/s), this is an extremely high frequency — structurally reminiscent of Zitterbewegung.

3. **The ratio $\gamma/H$ controls quantum coherence.** When $\gamma/H \ll 1$ (underdamped), the system is wave-like and coherent. When $\gamma/H \sim 1$, the system is at the edge of overdamping. When $\gamma/H \gg 1$ (overdamped), the telegraph equation reduces to the diffusion equation and the participation channel is effectively absent. In the language of quantum mechanics, $\gamma/H$ measures the degree of decoherence.

## 2.6 Consequences for ED as a Whole

The Compton anchoring in the quantum regime suggests a universal anchoring principle across all regimes:

$$H_{\text{causal}} = \frac{c^2\,\tau}{D} \tag{13}$$

| Regime | $D$ | $H_{\text{causal}}$ (with $\tau = 1$) | Physical name |
|--------|-----|------|------|
| Quantum | $\hbar/(2m)$ | $2mc^2/\hbar$ | Twice Compton frequency |
| Planck | $\sqrt{\hbar G/c}$ | $c^2/\sqrt{\hbar G/c} = \sqrt{c^5/(\hbar G)}$ | Planck frequency |
| Condensed matter | $\kappa$ (thermal diff.) | $c^2/\kappa$ | Very large (causality not limiting in practice) |
| Galactic | $v_{\text{circ}} L_0$ | $c^2/(v_{\text{circ}} L_0)$ | Characteristic frequency |
| Cosmological | $c^2/H_0$ | $H_0$ | Hubble frequency |

The condensed-matter and galactic regimes are non-relativistic, so the causal bound $c_{\text{ED}} \leq c$ is satisfied automatically for any reasonable $H$. The Compton anchoring is binding only in regimes where relativistic effects matter. In non-relativistic regimes, $H$ is a free parameter constrained by experiment, not by causality.

---

# 3. Interpreting $\gamma$ Across Regimes

## 3.1 The Role of $\gamma$ in the Architecture

The effective damping rate in the telegraph equation is:

$$\gamma = \frac{DP_0 + \zeta/\tau}{2}$$

It controls two things:

1. **The damping envelope** of telegraph oscillations: $\delta(t) \propto e^{-\gamma t}\cos(\omega t + \phi)$
2. **The wave-to-diffusion crossover time**: $t_{\text{cross}} \sim 1/\gamma$

At times $t \ll 1/\gamma$, the system is wave-like (coherent, oscillatory). At times $t \gg 1/\gamma$, it is diffusion-like (incoherent, monotonically relaxing). $\gamma$ is therefore the *decoherence rate* — the rate at which the system loses wave-like character.

## 3.2 Quantum Regime: $\gamma$ as Decoherence Rate

**Physical interpretation:** $\gamma$ is the rate at which the mean velocity $v(t) = \langle\mathbf{u}\rangle$ decorrelates from the true velocity field $\mathbf{u}(\mathbf{x},t)$. In quantum-mechanical language, this is the decoherence rate — the timescale on which a pure state (coherent, well-defined phase) evolves into a mixed state (incoherent, phase randomised).

**Connection to standard physics:** In the Lindblad formalism for open quantum systems, the master equation for the density matrix $\hat{\rho}$ contains dissipative terms that damp off-diagonal elements at a rate $\gamma_{\text{Lindblad}}$. The ED damping $\gamma$ maps to this Lindblad decoherence rate.

**Can $\gamma$ be derived from ED parameters?** In the codebase, $\gamma = (DP_0 + \zeta/\tau)/2$, which depends on both the penalty strength $P_0$ and the participation parameters $(\zeta, \tau)$. The penalty contribution $DP_0/2$ is fixed by the density-channel physics. The participation contribution $\zeta/(2\tau)$ is the genuinely free part.

**How to constrain $\gamma$ experimentally:** Decoherence rates are measured in quantum-optics and atom-trap experiments. For a specific quantum system (e.g., trapped ion, neutral atom in optical lattice), the measured decoherence rate provides an independent value for $\gamma$. Comparing this with the ED prediction $\gamma = (DP_0 + \zeta/\tau)/2$ would constrain $\zeta/\tau$.

**Typical values:** For a trapped ion ($\gamma_{\text{decoherence}} \sim 10^3$ s⁻¹) with $D_{\text{electron}} \sim 10^{-5}$ m²/s and $H = 2\omega_C \sim 10^{21}$ s⁻¹, the ratio $\gamma/H \sim 10^{-18}$, deep in the underdamped (coherent) regime. This is consistent: quantum systems maintain coherence over many Compton periods.

## 3.3 Condensed Matter: $\gamma$ as Viscous Damping

**Physical interpretation:** $\gamma$ is the rate at which the mean drift velocity of a colloidal ensemble decays due to viscous friction. In a suspension of particles with radius $a$ in a fluid of viscosity $\eta$, the Stokes drag gives a friction coefficient $\gamma_{\text{Stokes}} = 6\pi\eta a/m_{\text{eff}}$ per unit mass.

**Connection to standard physics:** The Langevin equation for a colloidal particle is $m\ddot{x} = -\gamma_{\text{Stokes}} m\dot{x} + F(t) + \xi(t)$. The ED participation equation $\dot{v} = -({\zeta}/{\tau})v + ({1}/{\tau})\bar{F}$ has the same structure with $\zeta/\tau \leftrightarrow \gamma_{\text{Stokes}}$ and $\bar{F}/\tau \leftrightarrow F/m$.

**Can $\gamma$ be derived from ED parameters?** Not from the ED PDE alone. In condensed matter, $\gamma$ depends on material properties (viscosity, particle size, temperature) that are external to the ED architecture. It must be measured or derived from a microscopic theory.

**How to constrain $\gamma$ experimentally:** Dynamic light scattering (DLS) at finite concentration measures the collective diffusion coefficient $D_{\text{coll}}$ and the relaxation rate. The ratio of these gives $\gamma$ directly. Alternatively, field-cycling NMR relaxometry measures the correlation time $\tau_c = 1/\gamma$.

**Typical values:** For micron-sized colloidal particles in water at room temperature, $\gamma_{\text{Stokes}} \sim 10^7$ s⁻¹. The collective diffusion coefficient $D \sim 10^{-12}$ m²/s. If the causal bound applied (which it doesn't — condensed matter is non-relativistic), $H_{\text{causal}} \sim 10^{29}$ s⁻¹. In practice, $H$ is much smaller and must be fitted from telegraph-oscillation experiments.

## 3.4 Galactic Regime: $\gamma$ as Dynamical Friction

**Physical interpretation:** $\gamma$ is the rate at which the bulk streaming velocity of matter in a galaxy halo decays due to gravitational interactions with surrounding matter. This is the Chandrasekhar dynamical friction timescale.

**Connection to standard physics:** Chandrasekhar's formula gives the deceleration of a mass $M$ moving through a background of density $\rho_{\text{bg}}$:

$$\frac{d\mathbf{v}}{dt} = -\frac{4\pi G^2 M \rho_{\text{bg}} \ln\Lambda}{v^2}\hat{\mathbf{v}}$$

For $v \sim v_{\text{circ}}$, this gives $\gamma_{\text{dyn}} \sim 4\pi G^2 M \rho_{\text{bg}} \ln\Lambda / v_{\text{circ}}^3$, which depends on the local halo density and the circular velocity.

**Can $\gamma$ be derived from ED parameters?** Not from the ED PDE alone, but the galactic-regime anchoring provides constraints. The equilibrium BTFR prediction $V_{\text{flat}}^4 \propto M_b$ holds when $v(t)$ has reached equilibrium, i.e., when $t \gg 1/\gamma$. The merger-lag prediction depends on the absolute value of $\gamma$: faster $\gamma$ means shorter relaxation after a merger.

**How to constrain $\gamma$ observationally:**
1. Measure the scatter in the BTFR as a function of merger age. The relaxation timescale $\tau_{\text{eq}} = 1/\gamma$ determines how quickly post-merger systems return to the BTFR.
2. Compare rotation curves of galaxies with different star-formation activity at fixed baryonic mass. The deviation from the equilibrium BTFR is proportional to $e^{-\gamma t_{\text{activity}}}$.

**Typical values:** For a Milky Way-like galaxy, $\gamma_{\text{dyn}} \sim (500\,\text{Myr})^{-1} \sim 6 \times 10^{-17}$ s⁻¹. This gives a relaxation time of $\sim 500$ Myr after a merger — long enough to be observable in post-merger morphological features.

## 3.5 Cosmological Regime: $\gamma$ as Expansion Damping

**Physical interpretation:** $\gamma$ is the rate at which peculiar velocities are damped by the Hubble expansion. In an expanding universe, a freely streaming particle's peculiar velocity decays as $v_{\text{pec}} \propto 1/a(t)$, giving an effective $\gamma \sim H_0$ (the Hubble constant).

**Connection to standard physics:** In the Friedmann framework, the deceleration equation gives:

$$\frac{\ddot{a}}{a} = -\frac{4\pi G}{3}(\rho + 3p/c^2) + \frac{\Lambda c^2}{3}$$

The Hubble parameter $H(t) = \dot{a}/a$ acts as a damping rate for density perturbations: $\ddot{\delta} + 2H\dot{\delta} = 4\pi G\rho\delta$ (linearised growth equation). The factor $2H$ is the effective $\gamma$ for cosmological perturbations.

**Can $\gamma$ be derived from ED parameters?** In the cosmological regime, if $H_{\text{ED}} = H_0$ (the Hubble frequency, from equation 13), then $\gamma \sim H_0$ as well — the natural damping timescale is the Hubble time. This would mean $\gamma/H_{\text{ED}} \sim 1$, placing the cosmological regime near the critical damping boundary. This is physically significant: it means cosmological dynamics is at the edge of the wave-to-diffusion transition.

**How to constrain $\gamma$ observationally:** Precision measurements of the growth rate of structure $f\sigma_8(z)$ from galaxy surveys (DESI, Euclid) constrain the effective damping of density perturbations. If ED's telegraph structure produces oscillatory corrections to the standard growth rate, $\gamma$ determines their amplitude and frequency.

**Typical value:** $\gamma \sim 2H_0 \approx 4.6 \times 10^{-18}$ s⁻¹, giving a damping timescale $\sim 1/(2H_0) \sim 7$ Gyr.

## 3.6 Summary: $\gamma$ Across Regimes

| Regime | $\gamma$ interpretation | Derivable from ED? | How to measure |
|--------|------------------------|--------------------|----|
| Quantum | Decoherence rate | Partially ($DP_0/2$ is fixed; $\zeta/(2\tau)$ is free) | Quantum coherence experiments |
| Condensed matter | Viscous damping rate | No (depends on material properties) | DLS, NMR relaxometry |
| Galactic | Dynamical friction rate | No (depends on halo properties) | BTFR scatter vs. merger age |
| Cosmological | Hubble damping rate | Possibly ($\gamma \sim H_0$ from self-consistency) | $f\sigma_8(z)$ measurements |

**Key conclusion:** $\gamma$ is the one ED parameter that cannot be fixed by the architecture alone in non-relativistic regimes. It must be measured or derived from a microscopic theory in each regime. This makes $\gamma$ the primary target for experimental confrontation: any regime where $\gamma$ can be independently measured provides a consistency check on the ED framework.

---

# 4. Key Predictions: Derivation and Falsification

## 4.1 Prediction 1: Finite-Speed Probability Propagation (Quantum)

### Derivation

From the telegraph dispersion relation (equation 7), the phase velocity at wavenumber $k$ is:

$$v_{\text{phase}}(k) = \frac{\omega(k)}{k}$$

where $\omega(k)$ is the real part of the complex frequency. In the high-$k$ limit:

$$\omega^2(k) \approx \frac{HD}{\tau}k^2 \quad \Longrightarrow \quad v_{\text{phase}} \to \sqrt{\frac{HD}{\tau}} = c_{\text{ED}}$$

The group velocity is:

$$v_{\text{group}}(k) = \frac{d\omega}{dk} \to c_{\text{ED}} \quad \text{as } k \to \infty$$

Both converge to $c_{\text{ED}} = c$ in the quantum regime with $H = 2\omega_C$, $\tau = 1$.

**The wavefront speed** (the speed of the leading edge of a propagating disturbance) is bounded by the maximum group velocity:

$$v_{\text{front}} \leq c_{\text{ED}} = c$$

This is the key result: **the ED density field has a strict speed limit**.

### Scaling

$$c_{\text{front}} = c = 2.998 \times 10^8 \text{ m/s} \quad \text{(exact, mass-independent)}$$

The arrival time of a density perturbation at distance $L$ is bounded below by:

$$t_{\text{arr}} \geq \frac{L}{c}$$

Compare to standard Schrödinger (parabolic): $t_{\text{arr}} = 0$ for any $L$ (instantaneous spreading).

### Observable

The leading edge of a propagating probability wavefront in a tunnelling or time-of-flight experiment. Specifically, the density $\rho(L, t)$ at a fixed detector distance $L$ from the source:

- **ED prediction:** $\rho(L, t) = 0$ for $t < L/c$. Sharp onset at $t = L/c$.
- **Schrödinger prediction:** $\rho(L, t) > 0$ for all $t > 0$. No sharp onset.

### Falsification condition

If quantum probability density is detected at distance $L$ from a localised source at a time $t < L/c$, with amplitude exceeding $e^{-L/\lambda_C}$ (where $\lambda_C = \hbar/(mc)$ is the Compton wavelength), the Compton anchoring is falsified. The exponential threshold excludes the regime where relativistic quantum field theory (pair creation) introduces ambiguity.

## 4.2 Prediction 2: Telegraph Oscillations in Dense Colloids (Condensed Matter)

### Derivation

In a concentration relaxation experiment, define $\delta(t) = \langle\rho\rangle(t) - \rho^*$ as the deviation from equilibrium. Without participation ($H = 0$), the relaxation is exponential:

$$\delta(t) = \delta_0\,e^{-DP_0 t} \quad \text{(Fickian, monotonic)}$$

With participation ($H > 0$), the coupled system gives the telegraph equation (Section 2.1):

$$\ddot{\delta} + 2\gamma\,\dot{\delta} + \omega_0^2\,\delta = 0$$

In the underdamped case ($\omega_0 > \gamma$), the solution is:

$$\delta(t) = \delta_0\,e^{-\gamma t}\cos(\omega t + \phi), \qquad \omega = \sqrt{\omega_0^2 - \gamma^2}$$

### Scaling

The oscillation frequency scales as:

$$\omega \approx \sqrt{\frac{HP_0}{\tau}} \quad \text{(for } H \gg \zeta\text{)}$$

The number of observable oscillation cycles before damping is:

$$N_{\text{osc}} = \frac{\omega}{2\pi\gamma} = \frac{1}{2\pi}\sqrt{\frac{\omega_0^2}{\gamma^2} - 1}$$

For $N_{\text{osc}} \geq 1$ (at least one full oscillation), we need $\omega_0 \geq \sqrt{4\pi^2 + 1}\,\gamma \approx 6.3\,\gamma$.

### Observable

The time-dependent mean concentration $\langle\rho\rangle(t)$ in a step-relaxation experiment. Prepare a colloidal suspension at concentration $\rho_0 \neq \rho^*$, release, and track the relaxation with confocal microscopy or DLS.

- **ED prediction (H > 0):** Damped oscillation with $N_{\text{osc}} \geq 1$ cycles.
- **Fick prediction (H = 0):** Monotonic exponential decay.

The critical experimental parameter is the volume fraction $\phi$: collective hydrodynamic interactions (which ED's $H$ represents) strengthen with increasing $\phi$. The prediction is that telegraph oscillations should appear above a critical volume fraction $\phi_c$.

### Falsification condition

If concentration relaxation is monotonic at all volume fractions $\phi \in [0, 0.6]$ and all measurement timescales down to $\Delta t \sim 1/\gamma_{\text{Stokes}}$, the participation channel is absent in colloidal systems.

## 4.3 Prediction 3: Activity-Dependent Rotation Curves (Galaxies)

### Derivation

At galactic equilibrium ($\dot{v} = 0$), the participation field satisfies:

$$v_{\text{eq}} = \frac{\bar{F}}{\zeta}$$

The BTFR scaling $V_{\text{flat}}^4 = a_{\text{ED}} G M_b$ holds when $v(t) = v_{\text{eq}}$.

For a galaxy with recent activity (star formation rate SFR, accretion rate $\dot{M}$), the baryonic mass changes on a timescale $\tau_{\text{act}}$. The participation field lags behind:

$$v(t) = v_{\text{eq}}(M_b(t)) + \Delta v \cdot e^{-t/\tau_{\text{eq}}}$$

where $\tau_{\text{eq}} = \tau/\zeta = 1/\gamma$ is the equilibration time and $\Delta v$ is the mismatch at the onset of activity.

The fractional deviation from the equilibrium BTFR is:

$$\frac{\Delta V_{\text{flat}}}{V_{\text{flat}}} \propto \frac{\Delta v}{v_{\text{eq}}} \propto \frac{\dot{M}_b/M_b}{\gamma} = \frac{\text{sSFR}}{\gamma}$$

where sSFR is the specific star formation rate.

### Scaling

$$\frac{\Delta V_{\text{flat}}}{V_{\text{flat}}} \sim \frac{\text{sSFR}}{\gamma} \tag{14}$$

For a galaxy with sSFR $\sim 10^{-10}$ yr⁻¹ and $\gamma \sim (500\,\text{Myr})^{-1} = 2 \times 10^{-9}$ yr⁻¹:

$$\frac{\Delta V_{\text{flat}}}{V_{\text{flat}}} \sim \frac{10^{-10}}{2 \times 10^{-9}} = 0.05 = 5\%$$

This is a 5% scatter in $V_{\text{flat}}$ at fixed $M_b$, correlated with star formation activity.

### Observable

The BTFR residual $\Delta\log V_{\text{flat}}$ as a function of sSFR or specific $H\alpha$ luminosity, at fixed baryonic mass. Data: SPARC rotation curves cross-matched with star-formation indicators from SDSS or MaNGA.

- **ED prediction:** Positive correlation between BTFR residual and sSFR ($\Delta V > 0$ for active galaxies).
- **$\Lambda$CDM prediction:** No systematic correlation (halo mass doesn't track sSFR on short timescales).
- **MOND prediction:** No correlation (gravity is instantaneous).

### Falsification condition

If the BTFR residual shows no correlation with sSFR at the $2\sigma$ level in a sample of $N \geq 100$ galaxies with measured rotation curves and sSFR, the temporal-tension mechanism is falsified.

## 4.4 Prediction 4: Merger Lag (Galaxies)

### Derivation

When two galaxies merge, the combined baryonic mass jumps from $M_{b,1}$ and $M_{b,2}$ to $M_{b,\text{merged}} = M_{b,1} + M_{b,2}$, but the participation field $v(t)$ remains at its pre-merger value. The BTFR predicts:

$$V_{\text{flat,eq}}^4 \propto M_{b,\text{merged}}$$

but the observed rotation velocity immediately post-merger is:

$$V_{\text{flat,obs}} < V_{\text{flat,eq}}$$

because $v(t)$ has not yet caught up to the new equilibrium. The deficit decays exponentially:

$$V_{\text{flat,obs}}(t) = V_{\text{flat,eq}} - \Delta V \cdot e^{-\gamma(t - t_{\text{merge}})}$$

### Scaling

The initial deficit is:

$$\frac{\Delta V}{V_{\text{flat,eq}}} \sim 1 - \left(\frac{M_{b,1}^{1/4} + M_{b,2}^{1/4}}{(M_{b,1} + M_{b,2})^{1/4}}\right)$$

For an equal-mass merger ($M_{b,1} = M_{b,2} = M$):

$$\frac{\Delta V}{V_{\text{flat,eq}}} \sim 1 - \frac{2}{2^{1/4}} = 1 - 2^{3/4} \approx 1 - 1.68... $$

This gives $\Delta V / V < 0$, meaning the system is *below* the BTFR, which is the expected direction: the merged system hasn't yet developed the full rotation velocity corresponding to its new mass.

More precisely, the deficit for equal-mass merger is:

$$\frac{V_{\text{obs}}}{V_{\text{eq}}} \sim \frac{(M)^{1/4}}{(2M)^{1/4}} = 2^{-1/4} \approx 0.84$$

So the initial velocity is $\sim 16\%$ below equilibrium. The relaxation timescale is $\tau_{\text{eq}} = 1/\gamma \sim 500$ Myr.

### Observable

The BTFR residual of morphologically-identified post-merger galaxies as a function of estimated time-since-merger (from tidal feature age, shell age, or disturbance index).

- **ED prediction:** Post-merger galaxies scatter below the BTFR, with deviation $\propto e^{-\gamma t_{\text{merge}}}$.
- **$\Lambda$CDM prediction:** Post-merger relaxation is governed by dark-matter halo virialisation ($\sim 1$–$2$ Gyr), not baryonic mass.
- **MOND prediction:** Instantaneous response; no merger lag.

### Falsification condition

If post-merger BTFR residuals are uncorrelated with estimated merger age in a sample of $N \geq 30$ post-merger galaxies, or if the residuals are positive (above the BTFR) rather than negative, the merger-lag prediction is falsified.

## 4.5 Prediction 5: Oscillatory Deceleration Parameter (Cosmology)

### Derivation

In the cosmological regime, the spatially-averaged ED equation with $\rho = \rho(t)$ (homogeneous) is:

$$\dot{\rho} = -DP_0(\rho - \rho^*) + Hv$$
$$\dot{v} = \frac{1}{\tau}\bigl(-DP_0(\rho - \rho^*) - \zeta v\bigr)$$

Mapping $\rho$ to the cosmological energy density and $v$ to the expansion rate, the telegraph structure produces damped oscillations in $\rho(t)$ and $v(t)$ around the equilibrium.

The deceleration parameter in the Friedmann framework is $q = -\ddot{a}a/\dot{a}^2$. If $v(t) \propto H(t) = \dot{a}/a$, then oscillations in $v(t)$ produce oscillations in $q(t)$:

$$q(t) = q_{\Lambda\text{CDM}}(t) + \Delta q_0\,e^{-\gamma t}\cos(\omega t + \phi) \tag{15}$$

### Scaling

With $D = c^2/H_0$ and $H_{\text{ED}} = H_0$, the telegraph frequency is:

$$\omega \sim \sqrt{\frac{H_0 \cdot P_0}{\tau}} \cdot c/\sqrt{H_0} = c\sqrt{P_0/(H_0\tau)}$$

The oscillation period in redshift space depends on the ratio $P_0/(H_0\tau)$. For $P_0 \sim H_0$ and $\tau \sim 1/H_0$:

$$\omega \sim H_0, \qquad T_{\text{osc}} \sim 2\pi/H_0 \sim 4 \times 10^{10} \text{ yr}$$

The damping timescale is $1/\gamma \sim 1/(2H_0) \sim 7$ Gyr. So the oscillation would have $N_{\text{osc}} \sim \omega/(2\pi\gamma) \sim 1$ cycle — marginally observable.

### Observable

The deceleration parameter $q(z)$ measured from Type Ia supernova distance-redshift data at $z < 2$. The ED prediction is a damped sinusoidal deviation from the smooth $\Lambda$CDM curve.

The amplitude of the deviation is:

$$|\Delta q_0| \sim \frac{\Delta\rho_0}{\rho_{\text{crit}}} \cdot e^{-\gamma t_0}$$

where $\Delta\rho_0$ is the initial density perturbation amplitude and $t_0$ is the current age of the universe.

### Falsification condition

If $q(z)$ is smooth to within the measurement precision of Rubin Observatory LSST ($\Delta q \lesssim 0.01$ at $z < 1$) over a $\sim 10$-year survey baseline with $\sim 10^5$ supernovae, and no oscillatory residual is detected, the cosmological telegraph prediction is not supported at the $\Delta q = 0.01$ level.

---

# 5. Coherence Tests: Detailed Protocols

## 5.1 Test 1: Single-Peak vs. Two-Peak Coherence Test

### Purpose

Directly test the identification $v(t) \leftrightarrow \langle\mathbf{u}\rangle$ by comparing systems where the mean velocity is well-defined (single peak) vs. identically zero by symmetry (two symmetric peaks).

### Initial conditions

**IC-A (Single peak):**

$$\rho_A(\mathbf{x}) = \rho^* + A\,\exp\left(-\frac{|\mathbf{x} - \mathbf{x}_0|^2}{2\sigma^2}\right)$$

with $\mathbf{x}_0 = (0.35, 0.5)$ (off-centre, to break symmetry and allow drift), $A = 0.2$, $\sigma = 0.08$.

**IC-B (Two symmetric peaks):**

$$\rho_B(\mathbf{x}) = \rho^* + A\,\exp\left(-\frac{|\mathbf{x} - \mathbf{x}_1|^2}{2\sigma^2}\right) + A\,\exp\left(-\frac{|\mathbf{x} - \mathbf{x}_2|^2}{2\sigma^2}\right)$$

with $\mathbf{x}_1 = (0.3, 0.5)$, $\mathbf{x}_2 = (0.7, 0.5)$ (symmetric about centre), same $A$ and $\sigma$.

### Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| $d$ | 2 | Standard 2D test |
| $N$ | $[128, 128]$ | Adequate resolution |
| $D$ | 0.3 | Canonical value |
| $M_0$ | 1.0 | Standard mobility |
| $\beta$ | 2.0 | Canonical mobility exponent |
| $P_0$ | 1.0 | Standard penalty |
| $\rho^*$ | 0.5 | Equilibrium density |
| $\rho_{\max}$ | 1.0 | Saturation density |
| $H$ | 5.0 | Strong participation |
| $\zeta$ | 0.5 | Moderate damping |
| $\tau$ | 1.0 | Unit timescale |
| $T$ | 2.0 | Total simulation time |
| $\Delta t$ | 0.001 | Timestep |

### Observables

1. **$v_A(t)$ and $v_B(t)$** — the participation field time series for each IC.
2. **Peak amplitude ratio:** $R_v = \max|v_A(t)| / \max|v_B(t)|$.
3. **$\bar{F}_A(t)$ and $\bar{F}_B(t)$** — the spatial-average forcing for each IC.
4. **Energy trajectories** $E_A(t)$, $E_B(t)$ — to confirm both reach the same attractor.

### Expected outcomes if interpretation is correct

- $R_v \gg 1$: the single peak drives much stronger $v(t)$ than the symmetric pair.
- $v_B(t) \approx 0$ at early times (symmetry forces $\bar{F}_B \approx 0$), with possible late-time activation as the peaks merge and break symmetry.
- Both ICs converge to the same equilibrium ($\rho \to \rho^*$, $v \to 0$) at $t \gg 1/\gamma$.

### What would falsify the interpretation

- If $R_v \approx 1$ (equal $v(t)$ amplitudes despite different symmetry), the mean-velocity interpretation is wrong — $v(t)$ responds to something other than the net drift.
- If $v_B(t)$ is large at early times despite perfect symmetry, the coupling $H\bar{F}$ is sensitive to curvature or variance, not just the mean forcing.

## 5.2 Test 2: $H$-Transition Sweep

### Purpose

Map the transition from diffusion-dominated ($H = 0$) to participation-dominated ($H \gg 1$) dynamics. Identify the critical $H_c$ where telegraph behaviour first appears.

### Initial condition

Barenblatt-like compact bump:

$$\rho(\mathbf{x}) = \rho^* + A\,\max\Bigl(1 - \frac{|\mathbf{x} - \mathbf{x}_c|^2}{R_0^2}, 0\Bigr)^{1/\beta}$$

with $A = 0.3$, $R_0 = 0.2$, $\mathbf{x}_c = (0.5, 0.5)$.

### Parameters

Fixed: $d = 2$, $N = [128, 128]$, $D = 0.3$, $M_0 = 1.0$, $\beta = 2.0$, $P_0 = 0.01$, $\rho^* = 0.5$, $\rho_{\max} = 1.0$, $\zeta = 0.1$, $\tau = 1.0$, $T = 5.0$, $\Delta t = 0.001$.

Swept: $H \in [0, 0.1, 0.5, 1, 2, 5, 10, 20, 50, 100, 200]$.

### Observables

For each $H$:

1. **$v(t)$ time series** — amplitude, frequency (via FFT), damping rate.
2. **Front position $R(t)$** — defined as the radius enclosing 90% of the mass anomaly.
3. **$\langle\rho\rangle(t)$** — mean density vs. time (oscillatory or monotonic?).
4. **Energy $E(t)$** — check Law 2 (monotonic decrease) at each $H$.
5. **Number of oscillation cycles** before $|v(t)| < 0.01 v_{\max}$.

### Expected outcomes

| $H$ range | Expected behaviour |
|----------|-------------------|
| $H = 0$ | Pure PME spreading, $v(t) = 0$, $R(t) \propto t^{\alpha_R}$ |
| $0 < H \lesssim H_c$ | Weak $v(t)$ oscillation, negligible effect on $R(t)$ |
| $H \sim H_c$ | Onset of detectable oscillation; $R(t)$ begins to show modulation |
| $H \gg H_c$ | Strong oscillation, $R(t)$ oscillates, $\langle\rho\rangle(t)$ oscillates |

The critical $H_c$ is defined as the smallest $H$ for which the FFT of $v(t)$ shows a peak with amplitude $> 10\times$ the noise floor.

### What would falsify the interpretation

If oscillation appears discontinuously (no smooth onset), or if $v(t)$ oscillation amplitude does not scale smoothly with $H$, the telegraph interpretation may need revision.

## 5.3 Test 3: Propagation Speed Measurement

### Purpose

Directly measure the finite propagation speed $c_{\text{ED}} = \sqrt{DH/\tau}$ by tracking the arrival time of a density pulse at increasing distances.

### Initial condition

Narrow Gaussian pulse:

$$\rho(\mathbf{x}) = \rho^* + A\,\exp\left(-\frac{(x_1 - x_{\text{src}})^2}{2\sigma^2}\right)$$

with $A = 0.3$, $\sigma = 0.01$ (narrow in $x_1$ direction), $x_{\text{src}} = 0.05$.

Use a quasi-1D domain: $N = [1024, 4]$, $L = [4.0, 0.1]$ to minimise transverse effects while keeping 2D.

### Parameters

| Parameter | Value |
|-----------|-------|
| $d$ | 2 (quasi-1D) |
| $N$ | $[1024, 4]$ |
| $L$ | $[4.0, 0.1]$ |
| $D$ | 0.3 |
| $M_0$ | 1.0 |
| $\beta$ | 0.0 (linear mobility, to get clean telegraph without PME complications) |
| $P_0$ | 0.1 |
| $\rho^*$ | 0.5 |
| $\rho_{\max}$ | 1.0 |
| $H$ values | $[0, 1, 5, 10, 50, 100]$ |
| $\zeta$ | 0.1 |
| $\tau$ | 1.0 |
| $T$ | 5.0 |
| $\Delta t$ | 0.0005 |

Detector positions: $x_{\text{det}} = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]$.

### Observables

1. **Arrival time $t_{\text{arr}}(x_{\text{det}})$** — defined as the first time $\rho(x_{\text{det}}, t) > \rho^* + \epsilon$ with $\epsilon = 0.001$.
2. **Arrival-time scaling**: plot $t_{\text{arr}}$ vs. $x_{\text{det}}$.
   - Diffusive: $t_{\text{arr}} \propto x_{\text{det}}^2$
   - Telegraph: $t_{\text{arr}} \propto x_{\text{det}}$ (linear, finite speed)
3. **Extracted speed**: slope of $t_{\text{arr}}$ vs. $x_{\text{det}}$ in the linear regime.
4. **Comparison with prediction**: $c_{\text{pred}} = \sqrt{DH/\tau}$.

### Expected outcomes

| $H$ | $c_{\text{pred}} = \sqrt{0.3 H}$ | Scaling of $t_{\text{arr}}$ |
|-----|---|---|
| 0 | $\infty$ (diffusion) | $\propto x^2$ |
| 1 | 0.55 | Transitional |
| 5 | 1.22 | $\propto x$ |
| 10 | 1.73 | $\propto x$ |
| 50 | 3.87 | $\propto x$ |
| 100 | 5.48 | $\propto x$ |

The transition from $t_{\text{arr}} \propto x^2$ to $t_{\text{arr}} \propto x$ is the signature of the telegraph-to-diffusion crossover.

### What would falsify the interpretation

If the extracted speed does not match $\sqrt{DH/\tau}$ to within 10%, or if $t_{\text{arr}}$ remains $\propto x^2$ even at large $H$, the finite-speed prediction is wrong.

## 5.4 Test 4: Temporal Tension Potential Map

### Purpose

Map the effective inter-peak interaction potential $V_{\text{eff}}(d, H)$ as a function of separation $d$ and participation coupling $H$.

### Initial condition

Two identical Gaussian peaks at separation $d_{\text{sep}}$:

$$\rho(\mathbf{x}) = \rho^* + A\left[\exp\left(-\frac{|\mathbf{x} - \mathbf{x}_L|^2}{2\sigma^2}\right) + \exp\left(-\frac{|\mathbf{x} - \mathbf{x}_R|^2}{2\sigma^2}\right)\right]$$

with $\mathbf{x}_L = (0.5 - d_{\text{sep}}/2, 0.5)$, $\mathbf{x}_R = (0.5 + d_{\text{sep}}/2, 0.5)$, $A = 0.15$, $\sigma = 0.06$.

### Parameters

Fixed: $d = 2$, $N = [128, 128]$, $D = 0.3$, $M_0 = 1.0$, $\beta = 2.0$, $P_0 = 1.0$, $\rho^* = 0.5$, $\rho_{\max} = 1.0$, $\zeta = 0.5$, $\tau = 1.0$, $T = 2.0$, $\Delta t = 0.001$.

Swept:
- $d_{\text{sep}} \in [0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80]$
- $H \in [0, 0.5, 1.0, 2.0, 3.0, 5.0, 7.0, 10.0]$

Total: $9 \times 8 = 72$ runs.

### Observables

1. **Drift rate** $\dot{d}_{\text{sep}}(t)$: linear fit to $d_{\text{sep}}(t)$ over $t \in [0.1T, 0.5T]$ (early-time, before significant merging).
2. **Drift sign**: positive = repulsion, negative = attraction.
3. **$v(t)$ correlation with $\dot{d}_{\text{sep}}$**: Pearson correlation $r(v, \dot{d}_{\text{sep}})$.
4. **Effective force** $F_{\text{eff}}(d_{\text{sep}}, H) = \dot{d}_{\text{sep}}$ (proportional to force at low Reynolds number).

### Expected outcomes

| $H$ | Small $d_{\text{sep}}$ | Large $d_{\text{sep}}$ |
|-----|-----|------|
| 0 | Repulsion (diffusive spreading, tail overlap) | Weak repulsion (tails don't overlap) |
| $H > 0$ small | Repulsion weakened | Near zero |
| $H > 0$ large | Attraction (temporal tension dominates) | Weak attraction |

The phase boundary $\dot{d}_{\text{sep}} = 0$ defines a curve in $(d_{\text{sep}}, H)$ space. Inside the curve: attraction. Outside: repulsion. If the curve closes, there is a potential well and an equilibrium separation $d_{\text{eq}}(H)$.

### What would falsify the interpretation

If $v(t)$ is uncorrelated with $\dot{d}_{\text{sep}}$ ($|r| < 0.3$), the drift is not driven by the participation channel. If the drift sign does not change with $H$, temporal tension is not a pair interaction.

## 5.5 Test 5: Architectural Law Survival

### Purpose

Test whether the nine architectural laws (Laws L1–L9 from the Foundational Paper) hold across the full range of participation coupling, or whether some break at high $H$.

### Protocol

Run the full ED-SIM-02 reproducibility pipeline (`python -m edsim certify`) at each $H$ value, with $H$ injected by modifying the default parameters.

**Note:** The current reproducibility pipeline uses default parameters including a specific $H$ value. This test requires running the pipeline with modified $H$.

### Parameters

$H \in [0, 0.5, 1.0, 5.0, 10.0, 50.0, 100.0]$. All other parameters at their default values for each phase.

### Observables

For each $H$, record pass/fail for all 9 phases:

| Phase | Law | Pass criterion |
|-------|-----|---------------|
| 1 | L1: Unique attractor (2D) | $\text{std}(\rho) < 0.5 \cdot \text{std}(\rho_0)$ |
| 2 | L1: Unique attractor (3D) + morphology | Blob + sheet fractions valid |
| 3 | L4: 4D morphology | Filament/pancake present |
| 4 | L2: Energy + complexity monotonicity | $C(T)/C(0) < 0.5$ |
| 5 | L3: Spectral entropy decrease | $H_{\text{spec}}(T) < H_{\text{spec}}(0)$ |
| 6 | L5: Dissipation channel sum | $R_{\text{grad}} + R_{\text{pen}} + R_{\text{part}} = 1 \pm 0.01$ |
| 7 | L7: Correlation length growth | $\xi(T) > \xi(0)$ |
| 8 | L6: Topological conservation | $\chi$ conserved at low threshold |
| 9 | Dimensional scaling | $H(4D) > H(3D) > H(2D)$ |

### Expected outcomes

| $H$ range | Expected | Reasoning |
|----------|----------|-----------|
| $H \leq 1$ | All 9 pass | Small perturbation to default dynamics |
| $1 < H \leq 10$ | 8–9 pass | Participation channel becomes significant; L5 should show increasing $R_{\text{part}}$ |
| $10 < H \leq 100$ | 7–9 pass | Strong participation may delay attractor convergence (L1) or modulate energy monotonicity (L2) |
| $H > 100$ | Possible failures in L1, L2 | Very strong participation may inject energy or prevent convergence |

### What would falsify the interpretation

If Law L2 (energy monotonicity) fails at any $H$, the participation channel injects energy and the Lyapunov structure breaks. This would be a fundamental architectural limit, not just a quantitative deviation. It would imply that the participation channel, at high coupling, is incompatible with the ED energy functional.

---

# 6. Numerical Experiment Templates

## 6.1 Template 1: Propagation Speed Measurement

```
ALGORITHM: measure_propagation_speed(H_values, detector_positions)

INPUT:
    H_values: list of participation coupling strengths
    x_det: list of detector positions along x-axis
    params: base EDParameters (quasi-1D, beta=0, narrow pulse IC)
    epsilon: detection threshold (default 0.001)

OUTPUT:
    speed_table: dict mapping H -> measured speed c_ED

FOR EACH H in H_values:
    1. SET params.H = H
    2. CONSTRUCT initial condition:
       rho_0 = rho_star + A * exp(-(x - x_src)^2 / (2*sigma^2))
       Broadcast along y-axis for quasi-1D
    3. INITIALISE v_0 = 0
    4. INITIALISE arrival_times = empty dict

    5. FOR EACH timestep t_n:
        a. Advance rho, v by one step (implicit Euler)
        b. FOR EACH x_d in x_det NOT YET DETECTED:
            IF mean(rho[:, x_d_index]) > rho_star + epsilon:
                arrival_times[x_d] = t_n

    6. EXTRACT speed:
        IF len(arrival_times) >= 3:
            Fit t_arr vs x_det:
              - Linear fit: t_arr = x_det / c_meas + t_0
              - Quadratic fit: t_arr = x_det^2 / (4*D_eff)
            Compare R^2 of both fits
            IF linear R^2 > quadratic R^2:
                c_measured = 1 / slope_of_linear_fit
                regime = "telegraph"
            ELSE:
                c_measured = infinity
                regime = "diffusive"

    7. COMPARE c_measured with c_predicted = sqrt(D * H / tau)
    8. STORE result: {H, c_predicted, c_measured, regime, relative_error}

RETURN speed_table
```

## 6.2 Template 2: $H$-Transition Sweep

```
ALGORITHM: sweep_H_transition(H_values)

INPUT:
    H_values: list of H from 0 to 200
    params: base EDParameters (Barenblatt IC, beta=2, P0=0.01)

OUTPUT:
    sweep_results: list of dicts with oscillation data per H

FOR EACH H in H_values:
    1. SET params.H = H
    2. CONSTRUCT Barenblatt IC:
       rho_0 = rho_star + A * max(1 - |x - x_c|^2 / R0^2, 0)^(1/beta)
    3. INITIALISE v_0 = 0
    4. RUN full simulation, recording at each output step:
       - v(t), rho_mean(t), E(t), front_position R(t)

    5. ANALYSE v(t):
        a. Compute FFT of v(t) over t in [T/4, T]  (skip transient)
        b. Find peak frequency omega_peak
        c. Compute peak amplitude A_peak
        d. Count zero-crossings -> N_oscillations
        e. Fit envelope: |v(t)| ~ A0 * exp(-gamma_eff * t)
           Extract gamma_eff

    6. ANALYSE R(t):
        a. Fit R(t) ~ t^alpha in the early phase (t < T/2)
        b. Check for oscillatory modulation: compute R_detrended(t)
        c. FFT of R_detrended to check for omega_peak match

    7. CHECK Law L2: is E(t) monotonically decreasing?

    8. STORE: {H, omega_peak, A_peak, N_osc, gamma_eff,
               alpha_R, R_oscillates, E_monotone}

IDENTIFY H_c: smallest H where A_peak > 10 * noise_floor

RETURN sweep_results, H_c
```

## 6.3 Template 3: Coherence Test

```
ALGORITHM: coherence_test(H)

INPUT:
    H: participation coupling strength
    params: base EDParameters (d=2, N=[128,128])

OUTPUT:
    coherence_result: dict with v-amplitude comparison

1. CONSTRUCT IC-A (single off-centre peak):
    rho_A = rho_star + A * exp(-|x - x_off|^2 / (2*sigma^2))
    where x_off = (0.35, 0.5)

2. CONSTRUCT IC-B (two symmetric peaks):
    rho_B = rho_star + A * [exp(-|x-x_L|^2/(2*sigma^2))
                          + exp(-|x-x_R|^2/(2*sigma^2))]
    where x_L = (0.3, 0.5), x_R = (0.7, 0.5)

3. RUN simulation A:
    Evolve rho_A with params.H = H
    Record v_A(t), F_bar_A(t), E_A(t) at each output step

4. RUN simulation B:
    Evolve rho_B with params.H = H
    Record v_B(t), F_bar_B(t), E_B(t) at each output step

5. COMPUTE amplitude ratio:
    R_v = max(|v_A|) / max(|v_B| + machine_epsilon)
    R_F = max(|F_bar_A|) / max(|F_bar_B| + machine_epsilon)

6. COMPUTE symmetry-breaking time for IC-B:
    t_break = first time when |v_B(t)| > 0.1 * max(|v_A|)
    (If never: t_break = infinity)

7. CHECK convergence:
    Both ICs should reach same attractor:
    |E_A(T) - E_B(T)| / E_A(T) < 0.01

8. STORE: {H, R_v, R_F, t_break,
           v_A_max, v_B_max, E_final_match}

INTERPRETATION:
    IF R_v > 5: strong support for mean-velocity interpretation
    IF R_v ~ 1: falsifies mean-velocity interpretation
    IF t_break < T/2: symmetry broken early (nonlinear effects)
    IF t_break = inf: symmetry maintained (linear regime)

RETURN coherence_result
```

---

# 7. Completed Interpretation: Final Statement

## 7.1 What $v(t)$ Is

**$v(t)$ is the spatially-averaged Madelung velocity — the mean directed flow of whatever $\rho$ describes.**

In the quantum regime, $v(t) = \langle\nabla S/m\rangle$, the Ehrenfest mean velocity. In condensed matter, it is the mean drift velocity of the particle ensemble. In the galactic regime, it is the mean peculiar velocity or bulk streaming motion. In cosmology, it is the mean expansion rate.

The identification is derived (Section 1) by spatially averaging the Madelung–Euler equation and applying a linear-damping closure for the Reynolds stress. The three required assumptions — linear damping (A1), force identification (A2), and scalar reduction (A3) — are stated explicitly. The mapping holds exactly when the velocity field is spatially uniform and breaks when it has rich spatial structure (interference, vortices, multi-scale dynamics).

$v(t)$ is not a new kind of physical quantity. It is the oldest one — momentum, projected to a global scalar. What is new is that ED treats this global momentum as a coupled dynamical variable with its own ODE, feeding back uniformly on the density field.

## 7.2 What $H$ Must Be

**In any regime where causality requires a finite propagation speed, $H$ is uniquely fixed by:**

$$H = \frac{c^2\,\tau}{D}$$

In the quantum regime with $D = \hbar/(2m)$ and $\tau = 1$:

$$H = \frac{2mc^2}{\hbar} = 2\omega_C$$

This is the Compton frequency. It is not a fit — it is the unique value that makes the ED telegraph equation propagate at the speed of light. The derivation is in Section 2.

In non-relativistic regimes (condensed matter, galactic), $H$ is a free parameter constrained by experiment, not by causality.

## 7.3 What $\gamma$ Means

**$\gamma$ is the decoherence rate — the timescale on which the mean flow loses memory of its initial condition.**

It arises from the mean-field closure (assumption A1): the Reynolds stress from velocity fluctuations acts as friction on the mean velocity. Physically:

| Regime | $\gamma$ is... | Measurable via... |
|--------|------------|------------------|
| Quantum | Decoherence rate | Coherence-time experiments |
| Condensed matter | Viscous damping rate | DLS, NMR relaxometry |
| Galactic | Dynamical friction rate | BTFR scatter vs. merger age |
| Cosmological | Hubble damping rate | $f\sigma_8(z)$ growth-rate measurements |

$\gamma$ cannot be derived from the ED architecture alone (except possibly in the cosmological regime where $\gamma \sim H_0$). It is the one parameter that must be measured in each regime. This makes it the primary target for experimental confrontation.

## 7.4 What ED Predicts Because of $v(t)$

Five specific, falsifiable predictions arise from the participation field:

| # | Prediction | Regime | Observable | Standard physics says... |
|---|-----------|--------|-----------|------------------------|
| 1 | Probability propagation at speed $c$ (not $\infty$) | Quantum | Tunnelling arrival time | Infinite speed (parabolic) |
| 2 | Damped oscillation in concentration relaxation | Condensed matter | $\langle\rho\rangle(t)$ in step experiment | Monotonic exponential decay |
| 3 | BTFR scatter correlated with star-formation activity | Galactic | $\Delta V_{\text{flat}}$ vs. sSFR | No correlation |
| 4 | Post-merger BTFR deficit decaying as $e^{-\gamma t}$ | Galactic | $\Delta V_{\text{flat}}$ vs. merger age | Different timescale or no lag |
| 5 | Oscillatory correction to $q(z)$ | Cosmological | Supernova Hubble diagram residuals | Smooth $q(z)$ |

Each prediction has a derivation (Section 4), a scaling law, an identified observable, and a falsification condition.

## 7.5 What Would Falsify This Entire Interpretation

The interpretation can be falsified at three levels:

**Level 1: The mean-velocity identification fails.** If the coherence test (Test 1, Section 5.1) shows $R_v \approx 1$ — equal $v(t)$ amplitudes for symmetric and asymmetric initial conditions — then $v(t)$ does not correspond to the mean flow. The entire Madelung mapping is wrong.

**Level 2: The Compton anchoring fails.** If the propagation speed measurement (Test 3, Section 5.3) gives $c_{\text{ED}} \neq \sqrt{DH/\tau}$, or if quantum tunnelling experiments show superluminal probability tails inconsistent with a finite-speed wavefront, then $H \neq 2\omega_C$ and the causality argument is wrong.

**Level 3: The predictions all fail.** If none of the five predictions in Section 4 is confirmed — no telegraph oscillations in colloids, no activity dependence in the BTFR, no merger lag, no oscillatory $q(z)$, and tunnelling arrival times inconsistent with $c_{\text{ED}} = c$ — then the participation channel, while mathematically consistent, does not correspond to any physical mechanism. ED would then be a pure-diffusion theory with an extraneous oscillatory degree of freedom.

**The strongest single test:** Test 3 (propagation speed). If the numerically measured wavefront speed matches $\sqrt{DH/\tau}$ across a range of $H$ values, the telegraph structure is confirmed within the simulation engine, and the physical predictions follow from the dimensional anchoring. If it fails, the entire framework is in question.

---

## Appendix: Notation Concordance

The codebase and the theoretical analysis use slightly different notation. This concordance table maps between them.

| Theory (this document) | Codebase (`edsim/`) | Relationship |
|---|---|---|
| $\gamma$ (telegraph damping) | `gamma` = `(D*P0 + zeta/tau)/2` | Derived quantity |
| $\omega_0$ (natural frequency) | `omega0_sq` = `(D*P0*zeta + H*P0)/tau` | $\omega_0 = \sqrt{\omega_0^2}$ |
| $\zeta$ (participation friction) | `params.zeta` | Direct parameter |
| $\tau$ (participation timescale) | `params.tau` | Direct parameter |
| $H$ (participation coupling) | `params.H` | Direct parameter |
| $v(t)$ (participation field) | `v` in integrators | Direct variable |
| $\bar{F}$ (spatial average forcing) | `F_avg` = `np.mean(D * F_local)` | Computed at each step |
| $D$ (diffusion coefficient) | `params.D` | Direct parameter |
| $P_0$ (penalty strength) | `params.P0` | Direct parameter |
| $M_0$ (mobility prefactor) | `params.M0` | Direct parameter |
| $\beta$ (mobility exponent) | `params.beta` | Direct parameter |
| $c_{\text{ED}}$ (telegraph speed) | Not computed | $= \sqrt{DH/\tau}$ |

---

*ED-Phys-05 Execution Phase · Event Density Research Programme · March 2026*
