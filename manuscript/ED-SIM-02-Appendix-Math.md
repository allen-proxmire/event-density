# Mathematical Appendix: ED-SIM-02

This appendix is auto-generated from the `edsim.math` package.

## A.1  Modal Hierarchy

The spectral decomposition of the density field reveals the modal cascade structure of the ED transient.

- **Primary mode index:** 1
- **Primary amplitude (t=0):** 7.108619e-01
- **Hierarchy ratio (A_1/A_2):** 1.00
- **Energy concentration (top 10%):** 1.0000
- **Inertial range:** [2.00, 42.45]
- **Inertial exponent alpha:** 6.213
- **Dissipative cutoff:** 3.00

**Top modal decay rates:**

| Mode index | |k| | sigma_k |
|-----------|-----|---------|
| 201 | 10.82 | 8.4361 |
| 294 | 10.82 | 8.4361 |
| 70 | 6.32 | 7.8512 |
| 194 | 6.32 | 7.8512 |
| 240 | 17.46 | 7.1246 |
| 519 | 17.46 | 7.1246 |
| 238 | 15.65 | 6.4145 |
| 455 | 15.65 | 6.4145 |

## A.2  Transient Classification

**Classification:** Type IV: Multi-scale burst
**Confidence:** 0.80

**Transient invariants:**

| Invariant | Value |
|-----------|-------|
| Relaxation time tau | 0.250000 |
| Modal turnover rate | 8.0000 |
| Entropy drop Delta H | 0.4957 |
| Entropy slope dH/dt | 0.9914 |
| Correlation growth exponent | 0.1608 |
| Energy curvature (mean d^2E/dt^2) | 7.404415e-02 |
| Plateau fraction | 0.0000 |
| Mode switches | 4 |

**Evidence:**

- energy_curvature: 0.07404415440683561
- plateau_fraction: 0.0
- mode_switches: 4
- hierarchy_ratio: 1.0
- entropy_slope: 0.9913942053925942

## A.3  Architectural Derivation

## Architectural Derivation: P1-P7 => Canonical PDE

### Axioms

**P1 (Locality):** The evolution of rho at each point depends only on rho and its spatial derivatives evaluated at that point.
  - Consequence: The operator F[rho] is a local differential operator.  No integral terms, no action at a distance.
  - Form: $F[\rho](x) = f(\rho(x), \nabla\rho(x), \nabla^2\rho(x))$

**P2 (Isotropy):** The evolution law has no preferred spatial direction.  F[rho] is invariant under rotations and reflections.
  - Consequence: F depends on rho, |nabla rho|^2, and nabla^2 rho, but not on individual partial derivatives.  No anisotropic terms.
  - Form: $F[\rho \circ R] = F[\rho] \circ R \quad \forall R \in O(d)$

**P3 (Gradient-driven flow):** The flux of rho is proportional to nabla rho, modulated by a state-dependent mobility M(rho) >= 0.
  - Consequence: The principal part of F is nabla . (M(rho) nabla rho), which expands to M nabla^2 rho + M' |nabla rho|^2.
  - Form: $J = -M(\rho)\,\nabla\rho, \quad \nabla\!\cdot\!J = M\,\nabla^2\rho + M'\,|\nabla\rho|^2$

**P4 (Dissipative structure):** There exists a Lyapunov functional E[rho] such that dE/dt <= 0 along all solutions.
  - Consequence: The penalty P(rho) and mobility M(rho) are related via the density potential Phi(rho) = int P/M ds.  The system is gradient-flow-like.
  - Form: $\frac{dE}{dt} = -\int \frac{|\nabla\rho|^2}{M(\rho)} - \int \frac{P(\rho)^2}{M(\rho)} \leq 0$

**P5 (Single scalar field):** The system evolves a single real-valued scalar field rho(x, t) on a bounded domain Omega.
  - Consequence: No vector fields, no tensor fields, no multi-component order parameters.  The PDE is scalar, not a system.
  - Form: $\rho: \Omega \times [0, T] \to [0, \rho_{\max}]$

**P6 (Minimal coupling):** The global mode v(t) is driven by the domain-averaged operator F_bar and feeds back additively into the local PDE.
  - Consequence: The (rho, v) system is the minimal non-local extension of the local PDE.  The coupling is linear in v.
  - Form: $\dot{v} = \tau^{-1}(\bar{F} - \zeta v), \quad \partial_t\rho \ni +H\,v$

**P7 (Dimensional consistency):** The PDE is well-posed and dimensionally consistent in all spatial dimensions d = 1, 2, 3, 4.  No d-dependent constitutive functions are introduced.
  - Consequence: The same M(rho), P(rho), and participation structure apply in all dimensions.  Dimensional effects enter only through the Laplacian eigenstructure and mode counting.
  - Form: $M, P, H, \tau, \zeta \text{ are independent of } d$

### Derivation Steps

**Step 1** (uses P5): By P5, the state is a single scalar rho(x,t) on Omega.
  $\rho: \Omega \times [0,T] \to [0, \rho_{\max}]$

**Step 2** (uses P1): By P1, the local operator F depends only on rho and its derivatives at each point.
  $F[\rho](x) = f(\rho, \nabla\rho, \nabla^2\rho)$

**Step 3** (uses P2): By P2, F is isotropic: it depends on |nabla rho|^2 and nabla^2 rho, not on individual partials.
  $F = f(\rho, |\nabla\rho|^2, \nabla^2\rho)$

**Step 4** (uses P3): By P3, the flux is J = -M(rho) nabla rho, giving the divergence-form principal part.
  $\nabla\!\cdot\!(M\nabla\rho) = M\nabla^2\rho + M'|\nabla\rho|^2$

**Step 5** (uses P4): By P4, the system must be dissipative.  The simplest zeroth-order term compatible with a Lyapunov functional is a linear penalty P(rho) = P0(rho - rho*).
  $F = M\nabla^2\rho + M'|\nabla\rho|^2 - P(\rho)$

**Step 6** (uses P6): By P6, the global mode v(t) couples additively, giving the full PDE and the v-equation.
  $\partial_t\rho = D\,F[\rho] + H\,v, \quad \dot{v} = \tau^{-1}(\bar{F} - \zeta v)$

**Step 7** (uses P7): By P7, the constitutive functions M, P are dimension-independent.  The PDE is valid for all d = 1, 2, 3, 4.
  $M(\rho) = M_0(\rho_{\max}-\rho)^\beta, \quad P(\rho) = P_0(\rho - \rho^*) \quad \forall d$

### Result

$$
\begin{align}
\partial_t \rho &= D\,F[\rho] + H\,v, \\
\dot{v} &= \frac{1}{\tau}(\bar{F} - \zeta\,v), \\
F[\rho] &= M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho), \\
M(\rho) &= M_0\,(\rho_{\max} - \rho)^\beta, \\
P(\rho) &= P_0\,(\rho - \rho^*).
\end{align}
$$

## A.4  The Nine Architectural Laws

## The Nine Architectural Laws

### Law 1: Unique attractor

**Statement:** The coupled (rho, v) system possesses a unique globally attracting equilibrium rho = rho*, v = 0 for all initial conditions in [0, rho_max].

$$
\rho(x,t) \to \rho^*, \quad v(t) \to 0 \quad \text{as } t \to \infty
$$

- **Derivation:** partial
- **Dimensions:** Holds for all d.
- **Universality:** All constitutive parameters with P0 > 0, M0 > 0.

### Law 2: Monotone energy decay

**Statement:** The Lyapunov functional E[rho] = int Phi(rho) dV is non-increasing along all solutions: dE/dt <= 0.

$$
\frac{dE}{dt} = -D\int\frac{|\nabla\rho|^2}{M(\rho)}\,dV - D\int\frac{P(\rho)^2}{M(\rho)}\,dV \leq 0
$$

- **Derivation:** derived
- **Dimensions:** Holds for all d.
- **Universality:** All parameters.

### Law 3: Spectral concentration

**Statement:** The spectral entropy H = -sum p_k log p_k decreases over time as energy concentrates into low-k modes.

$$
H(t_2) \leq H(t_1) \quad \forall\, t_2 > t_1
$$

- **Derivation:** empirical
- **Dimensions:** Holds for all d; initial H increases with d.
- **Universality:** Canonical constitutive functions.

### Law 4: Factorial complexity dilution

**Statement:** The initial ED-complexity C^(d) scales as C^(1)/d! with spatial dimension d.

$$
C_{\text{ED}}^{(d)} = \frac{C_{\text{ED}}^{(1)}}{d!}
$$

- **Derivation:** partial
- **Dimensions:** Explicit: d!
- **Universality:** Isotropic Neumann eigenbasis with fixed A, Nm.

### Law 5: Gradient-dissipation dominance

**Statement:** The gradient dissipation channel R_grad increases with d and approaches 1 asymptotically.

$$
R_{\text{grad}}^{(d)} = \frac{d\pi^2}{d\pi^2 + P_0^2/M^*} \to 1
$$

- **Derivation:** derived
- **Dimensions:** Explicit: linear in d.
- **Universality:** All parameters with P0, M* > 0.

### Law 6: Topological conservation

**Statement:** The Euler characteristic chi of excursion sets is constant in time: d chi/dt = 0.

$$
\frac{d\chi}{dt} = 0, \quad \chi = \sum_{k=0}^{d-1}(-1)^k \beta_k
$$

- **Derivation:** partial
- **Dimensions:** Holds for all d (Morse theory).
- **Universality:** Smooth solutions with non-degenerate critical points.

### Law 7: Horizon formation

**Statement:** Horizons (regions where M(rho) -> 0) form when the effective amplitude exceeds a d-dependent threshold.

$$
A_{\text{eff}} = A / \sqrt{N_m^d} > A_{\text{crit}}
$$

- **Derivation:** empirical
- **Dimensions:** Exponentially suppressed with d.
- **Universality:** Degenerate mobility with beta > 0.

### Law 8: Morphological hierarchy

**Statement:** In d >= 2, the Hessian eigenvalue structure produces a stratified morphology: filaments dominate in 3D, sheets and blobs fill the remainder.

$$
f_{\text{fil}} > f_{\text{sht}} > f_{\text{blb}} \quad (d=3)
$$

- **Derivation:** empirical
- **Dimensions:** New classes appear with each d.
- **Universality:** Multi-modal initial conditions.

### Law 9: Sheet-filament oscillation

**Statement:** In d >= 3, the morphology fractions exhibit oscillatory exchange between sheets and filaments during the transient.

$$
\exists\, t_1 < t_2 < t_3: f_{\text{sht}}(t_2) > f_{\text{sht}}(t_1), f_{\text{sht}}(t_3) < f_{\text{sht}}(t_2)
$$

- **Derivation:** empirical
- **Dimensions:** d >= 3 only.
- **Universality:** Multi-modal ICs with Nm >= 2.


## A.5  Law Verification

Verification against the canonical 2D cosine scenario:

| Law | Name | Passed | Key detail |
|-----|------|--------|------------|
| 1 | Unique attractor | PASS | rho_std = 2.2630e-02 |
| 2 | Monotone energy decay | PASS | violations = 0 |
| 3 | Spectral concentration | PASS | delta_H = 0.4957 |
| 4 | Factorial complexity dilution | PASS | A0 = 7.1086e-01 |
| 5 | Gradient-dissipation dominance | PASS | sum = 1.0000 |
| 6 | Topological conservation | FAIL | n_unique = 2 |
| 7 | Horizon formation | FAIL | error = 0.4024 |
| 8 | Morphological hierarchy | PASS | classes = 2 |
| 9 | Sheet-filament oscillation | PASS | change = 0.000322 |
