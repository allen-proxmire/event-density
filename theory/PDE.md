# The Canonical Event Density PDE

This document is the authoritative statement of the Event Density PDE. Every empirical and theoretical claim in this repository ultimately reduces to it.

---

## 1. The equation

The canonical ED system is a single semilinear PDE on a bounded scalar field $\rho(\mathbf{x},t)$, coupled to a global participation variable $v(t)$:

$$
\boxed{
\;\;
\partial_t \rho \;=\; D \cdot \bigl[\, M(\rho)\,\nabla^2\rho \;+\; M'(\rho)\,|\nabla\rho|^2 \;-\; P(\rho)\, \bigr] \;+\; H \cdot v
\;\;}
$$

$$
\boxed{\;\;\dot v \;=\; \frac{1}{\tau}\, \bigl(\, \bar F(\rho) \;-\; \zeta\,v\,\bigr) \;\;}
$$

with constitutive functions

$$
M(\rho) \;=\; M_0\,(\rho_{\max} - \rho)^{\beta}, \qquad
P(\rho) \;=\; P_0\,(\rho - \rho^\ast).
$$

That is the entire system. There are **eight scalar parameters** ($D, M_0, \beta, \rho_{\max}, P_0, \rho^\ast, H, \tau, \zeta$ — eight if $H$ is set by the global feedback, nine otherwise) and **no fitted couplings**. Where the PDE has been compared to data — soft matter (UDM), galaxy cluster mergers (Galaxy-15), galactic rotation curves (ED-Data-Galaxy series) — the parameters are fixed independently from one observable per regime, then the rest is prediction.

---

## 2. The four ingredients

The PDE is built from exactly four primitives:

| Primitive | Symbol | Role |
|-----------|--------|------|
| **Density** | $\rho(\mathbf{x},t)$ | Bounded scalar field; the state variable |
| **Mobility** | $M(\rho)$ | Degenerate diffusion that vanishes at the packing capacity $\rho_{\max}$, creating compact-support free boundaries |
| **Penalty** | $P(\rho)$ | Monostable restoring force toward a unique equilibrium $\rho^\ast$ |
| **Participation** | $v(t)$ | Global feedback variable (single ODE) creating non-local oscillatory dynamics |

These four primitives are the minimal set: removing any one collapses the system to a known sub-class (linear diffusion, pure decay, or trivial dynamics). Adding a fifth would violate one of the constraints below.

---

## 3. The seven structural constraints

The canonical PDE is *uniquely selected* by the following seven constraints. These are not assumed independently — they are consequences of the choice to derive a minimal field theory of "becoming." The detailed derivation is in `papers/Foundations_of_Event_Density/paper.md` and the universality proofs are in `papers/Foundations_of_Event_Density/Appendices/appendix_D_Universality Class.md`.

| # | Constraint | Statement |
|---|-----------|-----------|
| **C1** | Locality | The right-hand side at $\mathbf{x}$ depends only on $\rho$ and its derivatives at $\mathbf{x}$ (no integral kernels except via $v$) |
| **C2** | Isotropy | The PDE is invariant under spatial rotations |
| **C3** | Gradient-driven flow | The non-source dynamics derive from a flux $\mathbf{J} = -D M(\rho)\nabla\rho$ (Fick form) |
| **C4** | Dissipative structure | Multiple Lyapunov functionals exist; energy decays monotonically along trajectories |
| **C5** | Single scalar field | The state variable is one bounded scalar $\rho \in [0, \rho_{\max}]$ (no vector or tensor fields, no spinors) |
| **C6** | Minimal coupling | Constitutive functions $M$ and $P$ are functions of $\rho$ alone, not of $\rho$ and its derivatives mixed |
| **C7** | Dimensional consistency | The PDE admits a universal nondimensional reduction $D \cdot T_0 / L_0^2 = D_{\rm nd}$ at every physical scale |

A full statement (with proofs of independence and sufficiency) is in `papers/Foundations_of_Event_Density/Appendices/appendix_A_Proofs of Independence Results.md` and `papers/Foundations_of_Event_Density/Appendices/appendix_B_Proofs of Sufficiency Results.md`.

**Uniqueness theorem.** Constraints C1–C7 select the canonical PDE uniquely among all evolution equations on $\rho$. See `papers/Foundations_of_Event_Density/Appendices/appendix_D_Universality Class.md`, Theorem D.19.

---

## 4. The three channels

The right-hand side of the canonical PDE has three structurally distinct contributions, each of which can be exercised in isolation by setting the other parameters to zero:

### 4.1 Mobility channel

```
∂_t ρ = D · [ M(ρ) ∇²ρ + M'(ρ) |∇ρ|² ]
      = D · ∇·[ M(ρ) ∇ρ ]
```

With the constitutive form $M(\rho) = M_0(\rho_{\max}-\rho)^{\beta}$, this is the **porous-medium equation (PME)** with exponent $m = \beta + 1$ (in the variable $u = \rho_{\max}-\rho$). Solutions have compact support, sharp fronts, and self-similar Barenblatt spreading $R(t) \sim t^{1/(m+1)}$.

**Empirical correspondence:** the mobility law $D(c) = D_0(1 - c/c_{\max})^\beta$ across 10 chemically distinct soft-matter systems (UDM result; $R^2 > 0.986$). See `papers/Universal_Mobility_Law/`.

### 4.2 Penalty / wake channel

```
∂_t ρ = -D · P₀ · (ρ − ρ*)
```

With a moving baryonic source coupled in, this becomes a diffusion-decay-source equation whose steady-state is an exponential wake of length $\ell = D / v$ behind the source. In isolation (uniform initial conditions), it gives **exponential (Debye / RC) decay** $\rho(t) = \rho^\ast + (\rho_0 - \rho^\ast) e^{-D P_0 t}$ with zero error vs analytic.

**Empirical correspondence:** the cluster-merger lensing-mass offset $\ell = D_T / v_{\rm current}$, tested against 7 well-measured clusters and the Finner+25 aggregate sample of 58 subclusters. See `papers/Cluster_Merger_Lag_Evidence/`.

### 4.3 Participation channel

```
τ v̇ + ζ v = F̄(ρ),     coupling back through  H · v
```

Decoupled from $\rho$, the participation channel admits the second-order form $\tau \ddot v + \zeta \dot v + v = 0$, the **damped telegraph / RLC oscillation**, whose envelope is $e^{-\zeta t / 2\tau}$ and frequency $\omega = \sqrt{1/\tau - (\zeta/2\tau)^2}$. Numerical-vs-analytic match is exact to machine precision.

**Empirical correspondence:** RLC-circuit transfer functions and oscillatory phenomena across regimes. See `papers/Numerical_Atlas/paper.md`, Sections C.6–C.7.

These three channels are computationally verified in `analysis/notebooks/02_three_channels.ipynb`.

---

## 5. Architectural interpretation

The canonical PDE is the formal expression of a single ontological commitment: **the universe is made of becoming, and ED is the field theory of the rate of becoming.** Density $\rho$ is the local rate of micro-event production. Mobility quantifies how that rate spreads. Penalty enforces a unique equilibrium rate. Participation captures global, non-local feedback.

Three architectural facts follow directly from the constitutive structure (proved in `papers/Foundations_of_Event_Density/Appendices/appendix_C_PDE Analysis.md`):

- **Architectural sufficiency.** Each channel reduces *exactly* to a foundational physical equation when isolated. The reductions hold for *all* parameter values — they are not parameter-tuned. The structural correspondences are built into the constitutive architecture, not imposed.

- **Lyapunov dissipation.** The PDE admits five independent Lyapunov functionals (energy, mobility-weighted variance, penalty integral, gradient norm, $L^2$ norm), all monotonically decreasing along trajectories. The system is *not* a single gradient flow.

- **Bifurcation structure.** The discriminant surface $\Delta = (\zeta / 2\tau)^2 - 1/\tau = 0$ separates the under-damped (oscillating participation) from the over-damped (purely decaying) regimes. The bifurcation geometry is universal in the $(D, \zeta, \tau)$ parameter space.

The full architectural analysis is in `papers/Foundations_of_Event_Density/paper.md`; the rigorous PDE analysis (well-posedness, spectral structure, three-stage convergence theorem) is in `papers/Foundations_of_Event_Density/Appendices/appendix_C_PDE Analysis.md`.

---

## 6. Dimensional summary

The canonical PDE in physical (SI) units is

$$
\partial_t \rho \;=\; D_{\rm phys}\, \bigl[\, M(\rho)\,\nabla^2\rho \;+\; M'(\rho)\,|\nabla\rho|^2 \;-\; P(\rho)\, \bigr] \;+\; H_{\rm phys}\, v,
$$

with five independent dimensional scales:

| Scale | Symbol | Units | Physical meaning |
|-------|--------|-------|------------------|
| Length | $L_0$ | m | Coherence length of the field |
| Time | $T_0$ | s | Characteristic relaxation time |
| Density max | $\rho_{\max}$ | m$^{-3}$ (or scale-specific) | Packing capacity |
| Diffusivity | $D_{\rm phys}$ | m²/s | Constitutive mobility scale |
| Participation source | $H_{\rm phys}$ | (depends on regime) | Coupling between $\rho$ and $v$ |

Under universal nondimensionalization $\tilde t = t/T_0$, $\tilde {\mathbf x} = \mathbf{x}/L_0$, the system reduces to

$$
\partial_{\tilde t}\, \tilde\rho \;=\; D_{\rm nd}\, \bigl[\, M(\tilde\rho)\,\tilde\nabla^2 \tilde\rho \;+\; \cdots \,\bigr] \;+\; H_{\rm nd}\,\tilde v
$$

with the nondimensional invariant

$$
\boxed{\;\;D_{\rm nd} \;=\; \frac{D_{\rm phys}\, T_0}{L_0^2} \;\;}
$$

### The five-regime atlas

The same PDE admits a consistent dimensional interpretation across **five physical regimes** spanning **61 orders of magnitude** in length:

| Regime | $L_0$ | $T_0$ | Anchor | Detailed mapping |
|--------|-------|-------|--------|------------------|
| Quantum | $\hbar / 2mc$ | $\hbar / 2mc^2$ | Reduced Compton scale | `papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md` |
| Planck | $\sqrt{\hbar G/c^3}$ | $\sqrt{\hbar G/c^5}$ | Planck length / time | `papers/Dimensional_Atlas/regimes/ED-Dimensional-02_Planck_Regime.md` |
| Condensed matter | thermal diffusivity scale | molecular relaxation time | UDM mobility law | `papers/Dimensional_Atlas/regimes/ED-Dimensional-03_Condensed_Matter_Regime.md` |
| Galactic | $v_{\rm circ} \cdot L_0 \sim$ kpc | $L_0 / v_{\rm circ}$ | Mistele weak-lensing extent | `papers/Dimensional_Atlas/regimes/ED-Dimensional-04_Galactic_Regime.md` |
| Cosmological | $c^2 / H_0$ | $1/H_0$ | Hubble scale | `papers/Dimensional_Atlas/regimes/ED-Dimensional-05_Cosmological_Regime.md` |

Across all five regimes, the nondimensional invariant $D_{\rm nd} = 0.3$ holds *exactly*. This is not a fit; it is a structural identity built into the canonical PDE under nondimensionalization, derived in `papers/Dimensional_Atlas/paper.md`.

---

## 7. Where to read further

- **`/papers/Foundations_of_Event_Density/`** — the axiomatic derivation, the foundational paper, and the formal appendices (proofs, universality class, PDE analysis, numerical methods, glossary, references). Companion ontology paper at **`/papers/Event_Density_Ontology_and_Axioms/`**.
- **`/papers/Dimensional_Atlas/`** — the five regime mappings + the master atlas synthesis.
- **`/papers/Numerical_Atlas/`** — the computational atlas: well-posedness, spectral decay, modal hierarchy, Lyapunov dissipation, bifurcation surface, three-stage convergence — all numerically realized.
- **`/papers/Universal_Mobility_Law/`** — empirical confirmation in the soft-matter regime (mobility channel).
- **`/papers/Cluster_Merger_Lag_Evidence/`** — empirical confirmation in the galactic regime (penalty/wake channel).
- **`/theory/README.md`** — short overview of how the PDE underlies the three flagship empirical results.
- **`/analysis/notebooks/02_three_channels.ipynb`** — runnable demonstration of all three channels in isolation.
