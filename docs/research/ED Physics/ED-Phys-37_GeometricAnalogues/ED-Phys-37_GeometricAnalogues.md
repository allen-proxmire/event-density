# ED-Phys-37: Geometric and Gravitational Analogues of Event Density

## Canonical Sources

| Source | Content Used |
|--------|-------------|
| ED-Phys-35 (2D/3D Extension) | Horizon detection, morphological taxonomy, sheet-filament oscillation |
| ED-Phys-36 (Analytical Grounding) | Dimensional laws, nondimensionalisation, positioning framework |
| ED-Phys-01 (Update Rule) | Canonical PDE, constitutive functions, mobility structure |
| ED-12.5 (Cosmology from the Compositional Rule) | Nonlinear diffusion, Friedmann analogue, horizon conditions |
| Appendix C (PDE Analysis) | Quasilinear parabolic theory, Lyapunov stability, maximum principle |

---

# 0. Purpose and Scope

This chapter has two narrowly defined goals.

**Goal 1.** Identify structural analogues between the canonical ED PDE and three families of geometric and gravitational evolution equations: mean curvature flow, Ricci flow, and the horizon geometry of general relativity. In each case, the comparison is made at the level of PDE structure — shared operator forms, shared regularity classes, shared qualitative behaviour — and never at the level of ontological identity.

**Goal 2.** Clarify, with equal precision, what the ED system is *not*. It is not a metric theory: there is no metric tensor, no covariant derivative, no geodesic equation. It is not a curvature theory: the Laplacian $\nabla^2\rho$ is not a Ricci scalar, the mobility $M(\rho)$ is not a metric component, and the density $\rho$ is not a curvature potential. It is not a gravitational theory: the horizons that form in ED are diffusion barriers, not null surfaces of a Lorentzian spacetime. Every analogy in this chapter is structural, not physical.

The chapter is organised into four sections. Section I compares the ED PDE to geometric evolution equations. Section II compares ED horizon formation to gravitational horizon geometry. Section III compares the ED morphological taxonomy to the cosmic web classification in large-scale structure. Section IV catalogues the limitations of every analogy and makes explicit what ED cannot claim on the basis of structural similarity alone.

This chapter prepares the ground for ED-Phys-38 (cross-framework quantitative comparison) and ED-Phys-39 (higher-dimensional extension to $d \geq 4$).

Throughout, we work with the canonical ED system on $\Omega \subset \mathbb{R}^d$:

$$\partial_t \rho = D\,\bigl[M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho)\bigr] + H\,v,$$

with mobility $M(\rho) = M_0\,(\rho_{\max} - \rho)^\beta$, penalty $P(\rho) = P_0\,(\rho - \rho^*)$, and participation coupling $\dot{v} = \tau^{-1}(\bar{F} - \zeta v)$.

---

# I. Geometric Analogies

---

## I.1 ED vs Mean Curvature Flow

### The Mean Curvature Flow Equation

Mean curvature flow (MCF) evolves a hypersurface $\Sigma_t \subset \mathbb{R}^{d+1}$ by moving each point in the direction of the inward unit normal with speed equal to the mean curvature $H$:

$$\frac{\partial \mathbf{X}}{\partial t} = H\,\hat{\mathbf{n}}.$$

For the graph of a function $u(x_1, \ldots, x_d, t)$, this becomes

$$\partial_t u = \left(1 + |\nabla u|^2\right)^{-1/2}\,\nabla\!\cdot\!\left(\frac{\nabla u}{\sqrt{1 + |\nabla u|^2}}\right),$$

which, in the small-gradient limit $|\nabla u| \ll 1$, reduces to the heat equation $\partial_t u = \nabla^2 u$.

### Structural Similarity

The principal part of the ED density operator is $M(\rho)\,\nabla^2\rho$. In both MCF and the ED system, the evolution is driven by a Laplacian term — second spatial derivatives acting as a curvature proxy. Both equations are parabolic, both smooth initial data, and both dissipate a natural energy functional:

- MCF dissipates the area functional $\mathcal{A}[\Sigma] = \int_\Sigma d\sigma$.
- ED dissipates the Lyapunov functional $\mathcal{E}[\rho, v] = \int_\Omega \Phi(\rho)\,d^d\!x + \frac{\tau H}{2}v^2$.

In both cases, the evolution can be understood as gradient flow with respect to an appropriate geometric structure: MCF is the $L^2$ gradient flow of area; ED is a weighted gradient flow of $\mathcal{E}$ with respect to a mobility-dependent metric.

### Structural Difference

Three features distinguish the ED system from MCF:

**Degenerate mobility.** The coefficient of $\nabla^2\rho$ in the ED system is $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$, which vanishes at $\rho = \rho_{\max}$. In MCF, the coefficient $(1 + |\nabla u|^2)^{-1/2}$ is bounded below by zero but never vanishes for finite gradients. The degeneracy of $M$ produces horizon formation — a phenomenon with no direct MCF analogue.

**Penalty term.** The ED operator includes $-P(\rho)$, a zeroth-order reaction term that drives $\rho$ toward the equilibrium $\rho^*$. MCF has no such term: surfaces evolve purely by curvature, with no preferred "target" surface. The penalty fundamentally changes the long-time behaviour: ED converges to a unique equilibrium, while MCF can shrink surfaces to extinction (the round point).

**Participation coupling.** The global variable $v(t)$ in the ED system introduces non-local feedback — the spatial average $\bar{F}$ of the density operator feeds back into the evolution at every point. MCF is purely local: the velocity at each point depends only on the local curvature.

### Summary

The analogy between ED and MCF is genuine at the level of the principal operator: both are curvature-driven smoothing flows. The analogy breaks at three points — degeneracy, penalty, and non-locality — each of which introduces qualitatively new behaviour in the ED system.

---

## I.2 ED vs Ricci Flow

### The Ricci Flow Equation

Hamilton's Ricci flow evolves a Riemannian metric $g_{ij}$ on a manifold $\mathcal{M}$ by

$$\partial_t g_{ij} = -2\,R_{ij},$$

where $R_{ij}$ is the Ricci curvature tensor. In the coordinate-free formulation, Ricci flow smooths the metric by dissipating regions of high curvature. In dimension $d = 3$, Perelman's monotonicity results establish that an entropy functional

$$\mathcal{F}[g, f] = \int_\mathcal{M} \bigl(R + |\nabla f|^2\bigr)\,e^{-f}\,d\mu_g$$

is non-decreasing along the flow (when coupled to a backwards heat equation for $f$).

### Structural Similarity

The ED system and Ricci flow share two structural features:

**Gradient-energy dissipation.** Both flows dissipate a functional that measures spatial inhomogeneity. In Ricci flow, this is the curvature integral $\int R\,d\mu$. In ED, this is the ED-complexity $C_{\mathrm{ED}} = \int |\nabla\rho|^2\,d^d\!x$, which decreases monotonically during the gradient-dominated phase of the evolution.

**Parabolic regularisation.** Both flows are quasilinear parabolic: they smooth initial data instantaneously (for $t > 0$, the solution is smoother than the initial data). Both satisfy short-time existence and uniqueness theorems under mild regularity assumptions. Both can develop singularities — neck pinches in Ricci flow, horizon formation in ED — where the coefficient of the principal part degenerates.

### Structural Difference

The differences are fundamental and must be stated plainly.

**Tensorial vs scalar.** Ricci flow evolves a symmetric 2-tensor field $g_{ij}$ (a metric). The ED system evolves a single scalar field $\rho$. There is no tensorial structure in the ED PDE, no notion of contravariant/covariant indices, and no metric compatibility condition. The Ricci tensor $R_{ij}$ involves second derivatives of $g_{ij}$ contracted against the metric itself — a self-referential structure that has no analogue in a scalar equation.

**Curvature contraction vs Laplacian.** The operator $-2R_{ij}$ in Ricci flow is a nonlinear second-order operator on the metric with a specific algebraic structure (the contracted Bianchi identity). The operator $M(\rho)\nabla^2\rho$ in ED is a linear second-order operator on a scalar, weighted by a state-dependent coefficient. The two operators share the property of being second-order and parabolic, but their internal algebraic structure is entirely different.

**No diffeomorphism invariance.** Ricci flow is invariant under the full diffeomorphism group of $\mathcal{M}$; any coordinate system is as good as any other, and the flow respects the geometric structure of the manifold. The ED system is formulated on a fixed Euclidean domain with a fixed Cartesian grid. There is no diffeomorphism invariance, no general covariance, and no background independence.

### Summary

The analogy between ED and Ricci flow is limited to the broadest structural level: both are quasilinear parabolic equations that smooth curvature-like quantities and dissipate gradient energy. Beyond this, the two frameworks diverge in every technical detail — tensorial vs scalar, self-referential vs state-dependent, diffeomorphism-invariant vs coordinate-fixed.

---

## I.3 ED as a Degenerate Geometric PDE

The most precise classification of the ED PDE is not as a geometric evolution equation (in the sense of MCF or Ricci flow) but as a **degenerate parabolic equation with free boundaries**.

### Connection to the Porous-Medium Equation

The porous-medium equation (PME)

$$\partial_t u = \nabla\!\cdot\!(u^m\,\nabla u), \qquad m > 1,$$

evolves a non-negative scalar field $u$ with a diffusion coefficient $u^m$ that vanishes where $u = 0$. The ED system, rewritten in terms of the "headroom" $\delta = \rho_{\max} - \rho$, takes the form

$$\partial_t \delta = -D\,\nabla\!\cdot\!(M_0\,\delta^\beta\,\nabla\delta) + D\,P_0\,(\rho_{\max} - \rho^* - \delta) - H\,v.$$

The principal part $\nabla\!\cdot\!(\delta^\beta\,\nabla\delta)$ has exactly the structure of the PME with $m = \beta$. For the canonical value $\beta = 2$, this is the PME with $m = 2$.

### Free Boundaries and Finite Propagation

The PME with $m > 1$ exhibits finite propagation speed: the support of $u$ expands at a finite rate, and the boundary of the support (the "free boundary" or "interface") is a moving surface. In the ED context, the interface where $\rho = \rho_{\max}$ (equivalently, $\delta = 0$) is the horizon surface. The degenerate diffusion coefficient $M(\rho) \to 0$ means that density cannot propagate across the horizon — it is a one-way barrier.

This connection is mathematically precise. The theory of degenerate parabolic equations (Vázquez, 2007) provides existence, uniqueness, regularity, and interface propagation results for the PME. These results apply directly to the ED system after the substitution $\delta = \rho_{\max} - \rho$, modulo the penalty and participation terms (which are lower-order perturbations).

### Connection to the Thin-Film Equation

The thin-film equation

$$\partial_t h = -\nabla\!\cdot\!(h^n\,\nabla\nabla^2 h), \qquad n > 0,$$

governs the spreading of a viscous film of thickness $h$. Like the ED system, it has degenerate mobility ($h^n \to 0$ as $h \to 0$), free boundaries, and curvature-driven dynamics. The thin-film equation is fourth-order (biharmonic), while the ED system is second-order (Laplacian). Nevertheless, the shared feature of degeneracy-induced free boundaries makes the thin-film equation a closer structural relative of the ED system than either MCF or Ricci flow.

### Summary

The ED PDE is most accurately classified as a degenerate parabolic equation in the family of the porous-medium equation, augmented by a penalty term and a global participation coupling. Its horizons are free boundaries of the PME type, not null surfaces of a Lorentzian manifold. This classification locates ED within a well-studied mathematical framework and provides access to the extensive regularity and asymptotics theory of degenerate diffusion.

---

# II. Horizon Analogies

---

## II.1 ED Horizons

### Definition

An ED horizon is a region of the spatial domain $\Omega$ where the mobility function $M(\rho)$ approaches zero:

$$\mathcal{H}(t) = \bigl\{\mathbf{x} \in \Omega : M\bigl(\rho(\mathbf{x}, t)\bigr) < \epsilon\,M^*\bigr\},$$

for a threshold $\epsilon > 0$ (typically $\epsilon = 0.1$). Within $\mathcal{H}$, the density $\rho$ is close to the capacity bound $\rho_{\max}$, and the diffusion coefficient $D\,M(\rho)$ is negligibly small.

### Physical Consequences

Within the horizon region:

1. **Diffusion halts.** The principal term $M(\rho)\nabla^2\rho \to 0$, so the density field cannot redistribute itself. The region becomes "frozen" — dynamically isolated from its surroundings.

2. **Gradient self-interaction persists.** The term $M'(\rho)|\nabla\rho|^2$ remains nonzero (since $M'(\rho)$ does not vanish at $\rho_{\max}$ for $\beta > 1$). This creates a residual inward pressure at the horizon boundary.

3. **One-way influence.** Density can flow into the horizon region (increasing $\rho$ toward $\rho_{\max}$) but cannot flow out (because $M \to 0$ suppresses outward diffusion). This is the structural one-way property that motivates the name "horizon."

### Empirical Findings (ED-Phys-35)

The multi-dimensional simulations revealed that horizon formation depends strongly on both dimension and initial-condition complexity:

| Dimension | Nm | A = 0.03 | Horizons? |
|-----------|-----|----------|-----------|
| 2D | 4 (16 modes) | $A_{\mathrm{peak}} \sim A$ | Yes |
| 3D | 2 (8 modes) | $A_{\mathrm{peak}} \sim A$ | No |

The horizon threshold rises with dimension because the per-mode amplitude $A/\sqrt{N_m^d}$ decreases with $d$, reducing the constructive interference maximum. In 2D, multi-mode superposition routinely pushed $\rho$ past $\rho_{\max}$; in 3D with comparable total amplitude, no horizons formed.

---

## II.2 Structural Analogy to Event Horizons

### The Gravitational Event Horizon

In general relativity, an event horizon is the boundary of the causal past of future null infinity. It is a null hypersurface — a surface of zero metric signature — that separates the spacetime into a region from which light can escape and a region from which it cannot. The defining property is causal: no signal from inside the horizon can reach an external observer.

### The Structural Parallel

The ED horizon shares one structural feature with the gravitational event horizon: **it is a surface beyond which a form of propagation is suppressed.**

| Feature | GR Event Horizon | ED Horizon |
|---------|------------------|------------|
| Suppressed quantity | Light (null geodesics) | Density diffusion |
| Mechanism | Metric signature (null surface) | Degenerate mobility ($M \to 0$) |
| Direction | Inward (trapped surface) | Inward (density accumulates) |
| One-way property | Causal (no escape) | Diffusive (no redistribution) |
| Codimension | 1 (hypersurface) | 1 (iso-surface $\rho = \rho_{\max}$) |

The parallel is structural, not physical. The GR horizon is defined by the causal structure of a Lorentzian spacetime; the ED horizon is defined by the degeneracy of a diffusion coefficient in a Euclidean domain. There is no light cone, no metric signature, no null geodesic in the ED system.

### What the Analogy Can and Cannot Do

The analogy is useful for **importing intuition**: the concept of a one-way barrier, the idea that the interior of the horizon is dynamically isolated, the observation that the horizon surface has its own geometric structure (curvature, topology). These concepts transfer from GR to ED at the structural level.

The analogy is **not useful for importing dynamics**: the area theorem of GR horizons (Hawking's theorem), the Penrose process, Hawking radiation, and the laws of black-hole thermodynamics have no analogues in the ED system. These results depend on the Lorentzian metric structure, the Einstein field equations, and quantum field theory on curved spacetime — none of which are present in the ED framework.

---

## II.3 Horizon Geometry and Curvature

### Hessian Structure at the Horizon

The local geometry of the ED horizon $\mathcal{H}$ can be characterised by the Hessian of the density field $\rho$ restricted to the horizon surface. At a point $\mathbf{x}_0 \in \partial\mathcal{H}$, the Hessian $H_{ij} = \partial^2\rho / \partial x_i \partial x_j$ has $d$ eigenvalues $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_d$.

For the canonical ED system in 3D (ED-Phys-35), the horizon boundary typically has:

- One large positive eigenvalue (the direction of maximum density increase, pointing into the horizon).
- Two smaller eigenvalues (the tangential curvatures of the horizon surface).

This eigenvalue structure determines the local morphology of the horizon: spherical horizons have $\lambda_2 \approx \lambda_3$; elongated horizons have $\lambda_2 \gg \lambda_3$ (filament-like); flattened horizons have $\lambda_2 \approx \lambda_1$ (sheet-like).

### Comparison to Extrinsic Curvature

In GR, the geometry of a spatial cross-section of the event horizon is described by the induced metric and the extrinsic curvature tensor $K_{ij}$. The extrinsic curvature measures how the horizon surface is embedded in the ambient spacetime, and its trace (the expansion $\theta = g^{ij}K_{ij}$) determines whether the horizon is expanding, static, or contracting.

The ED Hessian eigenvalues play an analogous role: they describe how the level set $\rho = \rho_{\max} - \epsilon$ is embedded in the ambient Euclidean space, and their signs determine the local geometry (convex, concave, saddle) of the near-horizon region.

The analogy is geometric, not physical. The GR extrinsic curvature is defined with respect to a spacetime metric and involves the normal to a null surface. The ED Hessian eigenvalues are defined with respect to a flat Euclidean metric and involve the curvature of a level set. The shared mathematical structure — eigenvalues of a second fundamental form classifying local geometry — is the content of the analogy.

---

# III. Sheet/Filament/Blob Analogy to the Cosmic Web

---

## III.1 ED Morphology (Recap)

The ED-Phys-35 simulations in 3D classified the morphology of the density field at each spatial point by the eigenvalues of the Hessian $H_{ij} = \partial^2\rho / \partial x_i\partial x_j$. Sorting the eigenvalues by magnitude $|\lambda_1| \geq |\lambda_2| \geq |\lambda_3|$, three morphological indices are defined:

$$\text{Filamentarity: } F = \frac{|\lambda_2| - |\lambda_3|}{|\lambda_1|}, \qquad
\text{Sheetness: } S = \frac{|\lambda_1| - |\lambda_2|}{|\lambda_1|}, \qquad
\text{Blobness: } B = \frac{|\lambda_3|}{|\lambda_1|}.$$

The dominant morphology at each point is determined by which index is largest. For the canonical single-mode isotropic initial condition $\rho = \rho^* + A\cos(\pi x)\cos(\pi y)\cos(\pi z)$ evolved to late time:

| Morphology | Volume fraction |
|------------|----------------|
| Filament | **58%** |
| Sheet | 23% |
| Blob | 19% |

For multi-mode initial conditions ($N_m = 2$, eight modes), the morphology at late time shifts to **sheet-dominated** (49%), with filaments at 41% and blobs at 10%.

---

## III.2 Cosmic Web Analogy

### The Cosmic Web Classification

In observational and computational cosmology, the large-scale structure of the universe is classified into four morphological types: clusters (nodes), filaments, sheets (walls), and voids. The classification is performed by computing the tidal tensor — the Hessian of the gravitational potential $\Phi$ — at each point:

$$T_{ij} = \frac{\partial^2 \Phi}{\partial x_i \partial x_j}.$$

The eigenvalues $\lambda_1 \geq \lambda_2 \geq \lambda_3$ of $T_{ij}$ classify the morphology:

| Type | Eigenvalue signature | Physical interpretation |
|------|---------------------|----------------------|
| Cluster | $\lambda_1 > 0,\, \lambda_2 > 0,\, \lambda_3 > 0$ | Gravitational collapse in all 3 directions |
| Filament | $\lambda_1 > 0,\, \lambda_2 > 0,\, \lambda_3 < 0$ | Collapse in 2 directions, expansion in 1 |
| Sheet | $\lambda_1 > 0,\, \lambda_2 < 0,\, \lambda_3 < 0$ | Collapse in 1 direction, expansion in 2 |
| Void | $\lambda_1 < 0,\, \lambda_2 < 0,\, \lambda_3 < 0$ | Expansion in all 3 directions |

This classification scheme (Hahn et al. 2007, Forero-Romero et al. 2009) is standard in computational cosmology.

### The Structural Similarity

The ED morphological classification and the cosmic web classification share the same mathematical core: both classify a scalar field by the eigenvalues of its Hessian matrix. The ED density $\rho$ plays the structural role of the gravitational potential $\Phi$, and the ED Hessian $\partial^2\rho/\partial x_i\partial x_j$ plays the role of the tidal tensor $T_{ij}$.

The shared structure is:

1. A scalar field on $\mathbb{R}^3$.
2. Its Hessian at each point.
3. The eigenvalue signature as a morphological classifier.
4. The resulting taxonomy: filaments, sheets, and blobs/clusters/voids.

### The Structural Difference

The difference is equally fundamental:

**Persistence.** Cosmic web structures are gravitationally bound and persist indefinitely (filaments and clusters are the endpoints of gravitational collapse). ED structures are transient: they are decaying relics of the initial condition, driven toward the homogeneous equilibrium $\rho = \rho^*$ by the penalty term $P(\rho)$. The ED system does not form structure; it dismantles it.

**Self-gravity.** The cosmic web is shaped by the Poisson equation $\nabla^2\Phi = 4\pi G\rho_m$, which creates a self-consistent feedback between the matter density and the gravitational potential. The ED system has no self-gravity: the Hessian of $\rho$ is a diagnostic quantity, not a dynamical driver.

**Sign conventions.** In cosmology, positive tidal eigenvalues indicate gravitational collapse (infall). In ED, positive Hessian eigenvalues indicate local minima (valleys in the density landscape). The physical interpretation of the eigenvalue signs is reversed, even though the mathematical classification is the same.

---

## III.3 Sheet-Filament Oscillation

### The ED Observation

In the 3D simulations of ED-Phys-35, multi-mode initial conditions exhibited an oscillatory exchange between sheet-dominated and filament-dominated morphology during the transient relaxation:

| Time | Dominant morphology | Filament frac | Sheet frac |
|------|-------------------|---------------|------------|
| $t = 0.00$ | **Sheet** | 0.38 | 0.45 |
| $t = 0.10$ | **Filament** | 0.46 | 0.33 |
| $t = 0.20$ | **Filament** | 0.47 | 0.30 |
| $t = 0.30$ | **Sheet** | 0.40 | 0.40 |
| $t = 0.40$ | **Sheet** | 0.39 | 0.46 |
| $t = 0.50$ | **Sheet** | 0.41 | 0.49 |

The oscillation arises because higher spectral modes (which contribute differently to the Hessian eigenvalue ratios) decay at different rates. As each mode's contribution drops below a critical level, the dominant morphology shifts.

### Cosmological Analogy: Zel'dovich Collapse

In the Zel'dovich approximation to gravitational structure formation, the collapse of a density perturbation proceeds sequentially along the three eigenvectors of the deformation tensor. The first axis to collapse forms a **sheet** (a "pancake" in the original Zel'dovich terminology). The second axis collapse converts the sheet into a **filament**. The third axis collapse completes the process, forming a **cluster** (blob).

The sequence is: void $\to$ sheet $\to$ filament $\to$ cluster.

In the ED system, the sequence is reversed in direction (structures are decaying, not forming) but shares the same mathematical skeleton: the temporal ordering of eigenvalue dominance. The sheet-filament oscillation in ED is the time-reverse of the Zel'dovich collapse sequence, viewed through the lens of a dissipative rather than accretive system.

### Limits of the Analogy

The Zel'dovich collapse is a one-way process: once a sheet forms, it persists and subsequently collapses further into a filament. The ED oscillation is a two-way process: the morphology can oscillate between sheet and filament because the dynamics are reversible at the level of eigenvalue ordering (even though the total energy is monotonically decreasing). The oscillation damps over time as the system approaches the unique attractor, so it is a transient phenomenon rather than a persistent dynamical feature.

---

# IV. Limitations of the Analogy

---

## IV.1 ED Is Not a Metric Theory

The analogies of Sections I–III are structural comparisons between the ED PDE and geometric/gravitational frameworks. They do not imply that ED is a metric theory. Specifically:

**No metric tensor.** The ED system evolves a scalar field $\rho(\mathbf{x}, t)$ on a fixed Euclidean domain. There is no dynamical metric $g_{ij}$, no notion of distances determined by the density field, and no metric compatibility condition.

**No curvature tensor.** The Hessian $\partial^2\rho/\partial x_i\partial x_j$ is not a Riemann tensor, a Ricci tensor, or a scalar curvature. It is the second-derivative matrix of a scalar function — a fundamentally different mathematical object. The classification of morphology by Hessian eigenvalues is a geometric diagnostic, not a statement about the curvature of spacetime.

**No geodesics.** There is no geodesic equation, no notion of parallel transport, and no connection in the ED system. The density field does not define a geometry through which other objects propagate.

## IV.2 ED Is Not a Gravitational Theory

**No Einstein equation.** The ED PDE is a parabolic diffusion equation, not a hyperbolic wave equation. There is no analogue of the Einstein field equation $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$, no matter-geometry coupling, and no principle of equivalence.

**No Lorentzian structure.** The ED system lives in Euclidean space with a fixed background. There is no light cone, no causal structure, no distinction between timelike and spacelike, and no null surface. The "horizons" in ED are degeneracy surfaces of a diffusion coefficient, not causal boundaries of a Lorentzian manifold.

**No gravitational waves.** The ED PDE does not support wave-like solutions. It is purely dissipative: perturbations decay exponentially, they do not propagate. There is no analogue of gravitational radiation.

## IV.3 ED Is Not a Cosmological Model

**No expansion.** The ED system is defined on a fixed domain $\Omega$ with fixed size. There is no scale factor, no Hubble parameter, and no expansion history. The Friedmann analogue identified in ED-12.5 is a structural correspondence between the homogeneous-limit ODE and the Friedmann equation, not a claim that the ED system describes an expanding universe.

**No dark matter or dark energy.** The constitutive functions $M(\rho)$ and $P(\rho)$ are specified by construction, not derived from a matter content. The ED system does not predict the existence or behaviour of dark matter or dark energy.

**No primordial perturbations.** The initial conditions in ED are specified externally (cosine modes, Gaussian bumps, random fields). There is no mechanism analogous to quantum fluctuations during inflation, no Harrison-Zel'dovich spectrum, and no prediction of the CMB anisotropy pattern.

## IV.4 What the Analogies Are Good For

Given the extensive disclaimers of Sections IV.1–IV.3, it is worth stating clearly what the structural analogies *can* do.

**Import mathematical intuition.** The theory of mean curvature flow, Ricci flow, and degenerate parabolic equations provides a large body of results on existence, uniqueness, regularity, singularity formation, and asymptotic behaviour. The structural parallels with the ED PDE allow these results to be imported (with appropriate modification) into the ED framework. The PME connection (Section I.3) is particularly productive in this regard.

**Guide invariant design.** The cosmic web classification by tidal-tensor eigenvalues directly inspired the ED morphological taxonomy (filament, sheet, blob). The Minkowski functionals, originally developed for large-scale structure analysis, are now part of the 3D ED invariant atlas. Structural analogies generate diagnostic tools.

**Identify falsifiable distinctions.** By stating precisely where the analogies fail, we identify the features that make the ED system distinct from its geometric and gravitational relatives. These distinctions — degenerate mobility, penalty relaxation, participation coupling, unique attractor — are the architectural features that define what ED is, as opposed to what it resembles.

## IV.5 Closing

ED-Phys-37 has mapped the structural landscape between the ED PDE and three families of geometric and gravitational evolution equations. The analogies are genuine at the level of PDE structure (parabolic, curvature-driven, energy-dissipating) and at the level of diagnostic tools (Hessian eigenvalue classification, free-boundary geometry). They are not valid at the level of physical content: ED has no metric, no gravity, no causal structure, and no cosmological dynamics.

The value of these analogies is methodological, not ontological. They import mathematical tools, guide invariant design, and sharpen the definition of the ED framework by contrast with established theories. The next chapter, ED-Phys-38, will move from qualitative structural comparison to quantitative cross-framework analysis: measuring the numerical distance between ED predictions and the predictions of the theories discussed here.
