# What Is Event Density?

## Overview

Event Density (ED) is a **constrained generative ontology** for density-driven dynamics. It asks a single question: **what are the minimal primitives from which physically recognisable structure arises?**

The answer is four primitive objects and three constitutive channels. From these, a canonical PDE is derived via seven structural axioms, and its structural consequences are compared — not fitted — to known physical laws.

---

## The Four Primitives

The ED system is built on four irreducible objects:

| Primitive | Symbol | Type | Role |
|-----------|--------|------|------|
| Density | $\rho(x,t)$ | Bounded scalar field on $\Omega \subset \mathbb{R}^d$ | State variable |
| Mobility | $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ | Constitutive function, $\geq 0$ | Degenerate transport coefficient |
| Penalty | $P(\rho) = P_0(\rho - \rho^*)$ | Constitutive function | Monostable restoring force |
| Participation | $v(t)$ | Global scalar | Non-local feedback variable |

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

1. **P1 — Locality.** The operator at each point depends only on local values and spatial derivatives of $\rho$.
2. **P2 — Isotropy.** The operator is invariant under rotations and reflections: it depends on $\rho$, $|\nabla\rho|^2$, and $\nabla^2\rho$ only.
3. **P3 — Gradient-driven flow.** The flux is $J = -M(\rho)\nabla\rho$ with a non-negative, state-dependent mobility.
4. **P4 — Dissipative structure.** There exists a Lyapunov functional $E[\rho]$ with $dE/dt \leq 0$ along all solutions.
5. **P5 — Single scalar field.** The system evolves one real-valued bounded scalar $\rho(x,t)$.
6. **P6 — Minimal coupling.** A global mode $v(t)$ couples additively into the density equation with minimal dynamical structure.
7. **P7 — Dimensional consistency.** The constitutive functions $M(\rho)$ and $P(\rho)$ are independent of spatial dimension $d$.

These seven axioms determine the canonical ED PDE. The axioms constrain the *class* of admissible constitutive functions; the canonical forms $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ and $P(\rho) = P_0(\rho - \rho^*)$ are the simplest representatives of that class (see [Limitations and Scope](#limitations-and-scope) below).

---

## The Canonical PDE

> **Density evolution:**
> $$\partial_t \rho = D\bigl[\nabla\cdot(M(\rho)\,\nabla\rho) - P(\rho)\bigr] + H\,v$$
>
> **Participation ODE:**
> $$\dot{v} = \frac{1}{\tau}\bigl(\bar{F} - \zeta\,v\bigr)$$
>
> **where** $\bar{F} = |\Omega|^{-1}\int_\Omega F[\rho]\,d^d x$ is the domain-averaged density operator.

Equivalently, the local density operator expands as:

$$F[\rho] = M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho)$$

The first two terms combine into a divergence: $M\nabla^2\rho + M'|\nabla\rho|^2 = \nabla\cdot[M(\rho)\nabla\rho]$.

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

---

## Limitations and Scope

### Global participation variable

The participation variable $v(t)$ is a single global scalar. ED currently describes single-domain systems where $v$ couples uniformly to all points. A spatially varying participation field $v(x,t)$ — enabling multi-domain or multi-scale dynamics — is a natural future extension but is not part of the current framework.

### Constitutive under-specification

Axioms P1–P7 constrain the *class* of admissible constitutive functions but do not uniquely determine the functional forms of $M(\rho)$ and $P(\rho)$. The canonical choices — $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ (monomial mobility) and $P(\rho) = P_0(\rho - \rho^*)$ (linear penalty) — are the simplest representatives of that admissible class. Other forms satisfying the axioms (e.g., exponential mobility, nonlinear penalty) would produce a different member of the same PDE family. The nine architectural laws have been verified only for the canonical constitutive functions.

### The canonical PDE is one member of an admissible family

The axioms define a family of PDEs, not a single equation. The canonical PDE is distinguished by constitutive simplicity (lowest-order monomial and linear forms), not by axiomatic uniqueness alone. Claims of structural universality — such as the nine laws — apply to the canonical representative and may or may not extend to the full admissible class.
