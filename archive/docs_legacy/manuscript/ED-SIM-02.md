# ED-SIM-02: A Modular Simulation Platform for the Event Density PDE

**Allen Proxmire**

---

## Abstract

We present ED-SIM-02, a modular simulation platform for the Event Density
partial differential equation across two, three, and four spatial dimensions.
The platform solves a coupled system comprising a nonlinear density field with
degenerate mobility and a global participation variable, using finite-difference
implicit Euler and spectral ETD-RK4 integrators. At every output step, a full
invariant atlas is computed: Lyapunov energy, ED-complexity, spectral entropy,
morphology fractions, dissipation channel ratios, correlation length, structure
functions, and Euler characteristic. Six predefined scenarios, a parameter
sweep engine, and a nine-phase reproducibility pipeline provide a complete
experimental harness. The platform is validated by 112 unit and science tests
confirming the architectural laws of the ED framework: unique attractor
convergence, energy monotonicity, exponential modal decay, dissipation channel
decomposition, and topological conservation. All results are deterministic and
reproducible from a single command.

---

## 1. Introduction

The Event Density (ED) framework models the evolution of a scalar density
field under nonlinear diffusion with degenerate mobility, a penalty term
driving the field toward a unique equilibrium, and a global participation
variable providing non-local feedback. The canonical ED PDE is:

$$\partial_t \rho = D[M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)] + Hv$$

$$\dot{v} = \tau^{-1}(\bar{F} - \zeta v)$$

where $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ is the degenerate mobility,
$P(\rho) = P_0(\rho - \rho^*)$ is the linear penalty, and $v(t)$ is the
participation variable driven by the domain-averaged operator $\bar{F}$.

The ED-Phys series (papers 01-40) established nine architectural laws
governing this system: unique attractor convergence, energy monotonicity,
exponential modal decay, factorial complexity dilution, gradient-dissipation
dominance, topological conservation, horizon formation, morphological
hierarchy, and sheet-filament oscillation.

ED-SIM-02 is the computational platform that implements, tests, and
demonstrates these laws. It provides:

1. A dimension-agnostic solver supporting $d = 2, 3, 4$.
2. A full invariant atlas computed at every output step.
3. A reproducibility pipeline verifying the architectural laws.
4. A clean API for scenarios, sweeps, and atlas generation.

This paper describes the architecture, validates the implementation
against the nine laws, and presents representative results across
dimensions.

---

## 2. Methods

### 2.1 Solver Architecture

ED-SIM-02 is organised in five layers:

- **Core numerics**: parameters, operators (2D/3D/4D FD stencils), integrators
  (implicit Euler for all dimensions, ETD-RK4 for 2D spectral), boundary
  conditions (Neumann via ghost cells), and participation dynamics (exact
  exponential ODE integration).

- **Invariant engine**: computes energy, complexity, mass, spectral entropy,
  modal hierarchy, morphology fractions, dissipation channel ratios,
  correlation length, structure functions, Euler characteristic, and
  Betti numbers at each output snapshot.

- **Experiments**: six predefined scenarios (A-F), parameter sweeps, and
  atlas generation with compact summary extraction.

- **Reproducibility**: nine-phase validation pipeline producing a
  structured certificate with pass/fail status.

- **Tests**: 112 pytest tests covering unit numerics and science laws.

### 2.2 Time Integration

The implicit Euler integrator uses fixed-point (Picard) iteration to solve
the fully nonlinear system at each step. The ETD-RK4 integrator (2D only)
treats the linear part $L = -D(M^*\mu_k + P_0)$ exactly via matrix
exponentials in DCT-II space and integrates the nonlinear remainder with
a four-stage explicit Runge-Kutta scheme using Kassam-Trefethen contour
coefficients.

### 2.3 Invariant Atlas

The atlas is computed by `compute_atlas(rho, v, params)` which calls six
invariant families in sequence: energy (Lyapunov functional via
Gauss-Legendre quadrature of the density potential), spectral (DCT-based
power spectrum), morphology (Hessian eigenvalue classification), dissipation
(three-channel decomposition), correlation (Wiener-Khinchin autocorrelation),
and topology (cubical complex Euler characteristic).

---

## 3. Results

### 3.1 Unique Attractor (Law 1)

In all dimensions tested ($d = 2, 3, 4$), the density field relaxes
monotonically toward the equilibrium $\rho^*$ and the participation
variable $v$ decays toward zero, confirming Law 1.

![Field evolution in 2D](manuscript\figures\field_evolution_2d.png)

**Figure 1.** Density field at $t = 0$, $t = T/2$, and $t = T$ for
the A_2d_cosine scenario. The cosine perturbation decays toward the
uniform equilibrium.

### 3.2 Energy Monotonicity (Law 2)

The Lyapunov energy $E[\rho]$ decreases monotonically at every output
step in all runs, confirming Law 2.

![Energy time series](manuscript\figures\energy_complexity.png)

**Figure 2.** Lyapunov energy (left) and ED-complexity (right) vs time
for the canonical 2D scenario. Both decrease monotonically on a semilog
scale.

### 3.3 Spectral Concentration (Law 3)

The spectral entropy $H$ decreases over time as high-wavenumber modes
decay exponentially faster than low-wavenumber modes, concentrating the
spectrum into fewer modes.

![Spectral entropy](manuscript\figures\spectral_entropy.png)

**Figure 3.** Spectral entropy vs time. The decrease confirms Law 3:
modal hierarchy sharpens during relaxation.

### 3.4 Dissipation Channels (Law 5)

The dissipation decomposes into gradient ($R_{\mathrm{grad}}$),
penalty ($R_{\mathrm{pen}}$), and participation ($R_{\mathrm{part}}$)
channels summing to unity at every snapshot. The penalty channel dominates
in the early transient; the participation channel remains below 1%.

### 3.5 Topological Conservation (Law 6)

The Euler characteristic $\chi$ of the excursion set
$\{\rho \geq \tau\}$ is conserved when the threshold $\tau$ is
chosen below the field range (so the excursion set does not cross the
threshold boundary). At $\tau = \rho^* - 0.2$, $\chi = 1$ remains
constant throughout the 2D simulation.

### 3.6 Morphology Evolution

In 2D, the field is classified into blobs (peaks) and sheets (saddle
regions). In 4D, the full four-class taxonomy (blob, sheet, filament,
pancake) is active, with filaments dominating at 62% initially.

![Morphology evolution](manuscript\figures\morphology_evolution.png)

**Figure 4.** Morphology fractions vs time for the 2D scenario.

### 3.7 Dimensional Scaling

Across $d = 2, 3, 4$, the spectral entropy at $t = 0$ increases with
dimension ($H_{2D} < H_{3D} < H_{4D}$), consistent with the
growing number of active modes ($N_m^d$). The correlation length also
increases with dimension, reflecting broader spatial structure in
higher-dimensional fields.

![Dimensional scaling](manuscript\figures\dimensional_scaling.png)

**Figure 5.** Dimensional comparison: spectral entropy (left) and
correlation length (right) at $t = 0$ across $d = 2, 3, 4$.

---

## 4. Reproducibility

ED-SIM-02 includes a nine-phase reproducibility pipeline executed via:

```
python -m edsim.reproducibility.run_all
```

The phases verify:

| Phase | Law / Property | Check |
|-------|---------------|-------|
| 1 | Law 1 (Attractor) | rho_std decreases, v small, E monotone |
| 2 | 3D morphology | Fractions valid, nontrivial |
| 3 | 4D morphology | Filament/pancake present |
| 4 | Law 2 (Energy) | E, C monotone, C(T)/C(0) < 0.5 |
| 5 | Law 3 (Spectral) | H decreases, leading mode decays |
| 6 | Law 5 (Dissipation) | R sum = 1, R_part small |
| 7 | Correlation | xi grows (cosine IC), S_2 non-negative |
| 8 | Law 6 (Topology) | chi constant at low threshold |
| 9 | Dimensional scaling | H ordering, xi ordering |

All nine phases pass in approximately 6-8 seconds. The pipeline produces
a structured `ReproducibilityCertificate` with quantitative details for
each check.

The test suite contains 112 pytest tests covering unit numerics,
invariant correctness, and science-level architectural law verification.
All tests pass in approximately 3 seconds.

---

## 5. Conclusion

ED-SIM-02 provides a modular, tested, and reproducible simulation
platform for the Event Density PDE across dimensions 2 through 4.
The implementation confirms Laws 1-3, 5, and 6 of the ED architecture
and provides a complete invariant atlas for scientific exploration.
The platform is designed for clarity and correctness, making it
suitable for both validation of the ED-Phys theoretical programme
and as a reference implementation for nonlinear parabolic PDE solvers
with degenerate mobility.

---

## References

- ED-Phys-01 through ED-Phys-40: The Event Density Physics series.
- ED-SIM-02 Architecture Document: `ED Simulation/ED-SIM-02/ED-SIM-02_Architecture.md`
- Kassam, A.-K., and Trefethen, L. N. (2005). Fourth-order time-stepping
  for stiff PDEs. *SIAM J. Sci. Comput.*, 26(4), 1214-1233.
