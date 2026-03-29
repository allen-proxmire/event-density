# What Is Event Density?

## Overview

Event Density (ED) is an ontological framework for density-driven dynamics. It asks a single question: **what are the minimal primitives from which physically recognisable structure arises?**

The answer is four objects and three channels. From these, a unique canonical PDE is derived, and its structural consequences are compared — not fitted — to known physical laws.

---

## The Four Primitives

### 1. Density

A real-valued scalar field on a bounded domain:

$$\rho: \Omega \times [0,T] \to [0, \rho_{\max}]$$

The field is bounded above by a capacity limit $\rho_{\max}$. It represents the local concentration of "becoming" at each point.

### 2. Mobility

A degenerate diffusion coefficient:

$$M(\rho) = M_0(\rho_{\max} - \rho)^\beta$$

The mobility vanishes at the capacity bound, creating regions where transport halts. These regions are called **horizons**.

### 3. Penalty

A linear restoring force:

$$P(\rho) = P_0(\rho - \rho^*)$$

The penalty drives the field toward a unique equilibrium density $\rho^*$. Unlike double-well potentials, the ED penalty is monostable: there is one equilibrium, not two.

### 4. Participation

A global scalar variable $v(t)$, driven by the domain-averaged operator and feeding back uniformly into the PDE. This is the minimal non-local extension of a purely local diffusion equation.

---

## The Seven Axioms

The canonical PDE is not postulated. It is derived from seven structural axioms:

| Axiom | Title | Content |
|-------|-------|---------|
| P1 | Locality | The operator at each point depends only on local values and derivatives |
| P2 | Isotropy | The operator is invariant under rotations and reflections |
| P3 | Gradient-driven flow | The flux is $J = -M(\rho)\nabla\rho$ with state-dependent mobility |
| P4 | Dissipative structure | There exists a Lyapunov functional with $dE/dt \leq 0$ |
| P5 | Single scalar field | The system evolves one real-valued scalar |
| P6 | Minimal coupling | The global mode $v(t)$ couples additively with minimal structure |
| P7 | Dimensional consistency | Constitutive functions are independent of spatial dimension |

These seven axioms uniquely determine the canonical ED PDE.

---

## The Canonical PDE

$$\partial_t \rho = D\,F[\rho] + H\,v, \qquad \dot{v} = \frac{1}{\tau}\bigl(\bar{F} - \zeta\,v\bigr)$$

where

$$F[\rho] = M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho)$$

and $\bar{F} = |\Omega|^{-1}\int_\Omega F[\rho]\,d^d x$.

The first two terms of $F$ combine into a divergence: $M\nabla^2\rho + M'|\nabla\rho|^2 = \nabla\cdot[M(\rho)\nabla\rho]$.

---

## The Three Channels

The PDE decomposes into three constitutive channels:

| Channel | Operator | What it does | Physical analogue |
|---------|----------|-------------|-------------------|
| **Mobility** | $\nabla\cdot[M(\rho)\nabla\rho]$ | Nonlinear diffusion with degenerate mobility | Porous-medium equation |
| **Penalty** | $-P(\rho)$ | Exponential relaxation toward $\rho^*$ | RC circuit / Debye decay |
| **Participation** | $+Hv(t)$ | Global telegraph oscillation | RLC circuit |

Each channel can be activated or silenced independently by setting the relevant parameter to zero. This makes the framework falsifiable: every structural prediction can be tested by turning channels on and off.

---

## Why ED Is Unique

ED is the only known scalar PDE that simultaneously possesses:

1. **Degenerate mobility** creating free boundaries (horizons)
2. **Monostable penalty** driving a unique attractor
3. **Global participation** creating telegraph oscillation
4. **Five simultaneous Lyapunov functionals**
5. **The property that it is not a gradient flow of any of them**

No comparison PDE — not the porous-medium equation, not Allen-Cahn, not Cahn-Hilliard, not Fokker-Planck — combines all five features.

---

## What ED Is Not

- ED is not a spacetime theory (no metric, no curvature, no geodesics)
- ED is not a quantum theory (no Hilbert space, no superposition, no entanglement)
- ED is not a gravitational theory (no Einstein equations, no Newtonian potential)
- ED is not a statistical mechanics (no partition function, no detailed balance)
- ED is not a variational theory (it has Lyapunov functionals but is not a gradient flow)

ED is a **constitutive architecture**: a specific choice of mathematical objects whose structural consequences are then compared to known physics.
