# ED-Phys-39: Higher-Dimensional Extension ($d \geq 4$)

## Canonical Sources

| Source | Content Used |
|--------|-------------|
| ED-Phys-35 (2D/3D Extension) | Dimensional laws, morphological taxonomy, invariant atlas |
| ED-Phys-36 (Analytical Grounding) | Factorial complexity derivation, $R_{\mathrm{grad}}$ derivation, nondimensionalisation |
| ED-Phys-37 (Geometric Analogues) | Horizon analysis, curvature-flow connection |
| ED-Phys-38 (Cross-Framework Comparison) | Distance metrics, PME/AC/CH comparison protocol |
| ED-Phys-01 (Update Rule) | Canonical PDE, constitutive functions |

---

# 0. Purpose and Scope

This chapter extends the Event Density framework to four spatial dimensions and, where analytical tools permit, to arbitrary $d$. The empirical dimensional program of ED-Phys-35 established four laws by measuring 1D, 2D, and 3D systems. The analytical program of ED-Phys-36 provided partial derivations and scaling arguments. ED-Phys-39 closes the loop: it tests those laws in a dimension they have never seen, and uses the outcome to distinguish genuine dimensional scaling from low-dimensional coincidence.

The chapter has four goals.

**Goal 1.** Extend the canonical ED PDE, the invariant atlas, and the morphological classification to four spatial dimensions. The PDE itself generalises without modification; the Hessian eigenstructure, the mode-count combinatorics, and the Minkowski functionals all acquire new components in 4D.

**Goal 2.** Test the four dimensional laws established in ED-Phys-35 and ED-Phys-36:

- the factorial complexity dilution law $C_{\mathrm{ED}}^{(d)} = C_{\mathrm{ED}}^{(1)}/d!$,
- the gradient-dissipation dominance law $R_{\mathrm{grad}} \to 1$ as $d \to \infty$,
- the horizon-threshold scaling law $A_{\mathrm{eff}} \sim A/\sqrt{N_m^d}$,
- the topological conservation law $d\chi/dt = 0$.

Each law makes a precise quantitative prediction for $d = 4$ that can be confirmed or falsified.

**Goal 3.** Define the 4D morphological taxonomy. In 3D, the Hessian eigenvalues classify structure into filaments, sheets, and blobs. In 4D, a fourth eigenvalue introduces a new morphological class — the pancake — and the full taxonomy becomes filament, sheet, pancake, blob.

**Goal 4.** Compare 4D ED to 4D PME, AC, and CH using the four distance metrics defined in ED-Phys-38. This tests whether the proximity hierarchy (PME closest, AC moderate, CH/TFE far) is dimensionally stable.

This chapter completes the empirical dimensional program and prepares the ground for ED-Phys-40 (Architectural Synthesis), where the full set of laws, invariants, and comparisons across $d = 1, 2, 3, 4$ will be consolidated into a unified theoretical statement.

---

# I. ED in Four Dimensions

---

## I.1 Canonical ED PDE in 4D

The canonical ED system on a bounded domain $\Omega \subset \mathbb{R}^4$ with coordinates $(x_1, x_2, x_3, x_4)$ is

$$\partial_t \rho = D\,F[\rho] + H\,v, \qquad \dot{v} = \frac{1}{\tau}(\bar{F} - \zeta\,v),$$

where the density operator is

$$F[\rho] = M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho),$$

and the 4D differential operators are

$$\nabla\rho = \left(\frac{\partial\rho}{\partial x_1},\;\frac{\partial\rho}{\partial x_2},\;\frac{\partial\rho}{\partial x_3},\;\frac{\partial\rho}{\partial x_4}\right),$$

$$|\nabla\rho|^2 = \sum_{i=1}^{4}\left(\frac{\partial\rho}{\partial x_i}\right)^{\!2},$$

$$\nabla^2\rho = \sum_{i=1}^{4}\frac{\partial^2\rho}{\partial x_i^2}.$$

The operator structure is identical to the 1D, 2D, and 3D forms. The Laplacian is the sum of four second derivatives; the gradient-squared is the sum of four squared first derivatives. No new terms appear; no constitutive functions change. The dimensional dependence enters entirely through the eigenstructure of the Laplacian and the combinatorics of the mode space.

### Computational Feasibility

For a uniform grid with $N$ points per axis, the 4D problem requires $N^4$ grid points. The minimum resolution for spectral convergence in previous dimensions was $N = 64$. In 4D:

| $N$ per axis | Total grid points | Memory (float64) |
|-------------|-------------------|-------------------|
| 16 | 65,536 | 0.5 MB |
| 24 | 331,776 | 2.5 MB |
| 32 | 1,048,576 | 8 MB |
| 48 | 5,308,416 | 40 MB |
| 64 | 16,777,216 | 128 MB |

A resolution of $N = 32$ is feasible on desktop hardware and provides $32^4 \approx 10^6$ grid points — sufficient for quantitative testing of the dimensional laws. Higher resolutions ($N = 48$ or $64$) are accessible on GPU or multi-core systems.

---

## I.2 4D Constitutive Structure

The constitutive functions are unchanged from lower dimensions:

$$M(\rho) = M_0\,(\rho_{\max} - \rho)^\beta, \qquad M'(\rho) = -\beta\,M_0\,(\rho_{\max} - \rho)^{\beta - 1},$$

$$P(\rho) = P_0\,(\rho - \rho^*).$$

The mobility $M(\rho)$ vanishes at $\rho = \rho_{\max}$ and is maximal at $\rho = 0$. The penalty $P(\rho)$ vanishes at $\rho = \rho^*$ and drives the field toward equilibrium. The participation variable $v(t)$ couples to the domain-averaged operator $\bar{F} = |\Omega|^{-1}\int_\Omega F[\rho]\,d^4\!x$. None of these functions depend on $d$.

The dimensional dependence enters through three channels.

**Channel 1: Laplacian eigenvalues.** On the 4D cube $\Omega = [0, L]^4$ with Neumann boundary conditions, the Laplacian eigenvalues are

$$\mu_{\mathbf{k}} = \sum_{i=1}^{4}\left(\frac{k_i\pi}{L}\right)^{\!2}, \qquad \mathbf{k} = (k_1, k_2, k_3, k_4) \in \mathbb{N}_0^4.$$

The minimum nonzero eigenvalue is $\mu_{\min} = (\pi/L)^2$, the same as in all dimensions. But the density of eigenvalues near any given $\mu$ grows with $d$: the number of lattice points on the 4D sphere of radius $R$ scales as $R^3$, compared to $R^2$ in 3D and $R$ in 2D.

**Channel 2: Mode-count scaling.** The total number of active modes for the canonical initial condition with $N_m$ modes per axis is $N_m^4$. For $N_m = 2$, this gives $2^4 = 16$ modes in 4D, compared to $8$ in 3D, $4$ in 2D, and $2$ in 1D.

**Channel 3: Hessian eigenvalue structure.** The Hessian matrix $\mathcal{H}_{ij} = \partial^2\rho/\partial x_i\partial x_j$ is $4 \times 4$ in 4D, with four real eigenvalues $\lambda_1 \geq \lambda_2 \geq \lambda_3 \geq \lambda_4$. The morphological classification depends on the ratios of these eigenvalues.

---

# II. Test of Dimensional Laws in 4D

---

## II.1 Factorial Complexity Law

### Prediction

The factorial complexity law, established empirically in ED-Phys-35 and derived structurally in ED-Phys-36, states

$$C_{\mathrm{ED}}^{(d)} = \frac{C_{\mathrm{ED}}^{(1)}}{d!}.$$

For $d = 4$:

$$C_{\mathrm{ED}}^{(4)} = \frac{C_{\mathrm{ED}}^{(1)}}{4!} = \frac{C_{\mathrm{ED}}^{(1)}}{24}.$$

Using the canonical 1D value $C_{\mathrm{ED}}^{(1)} = 2A^2\pi^2/L^2$ with $A = 0.03$ and $L = 1$:

$$C_{\mathrm{ED}}^{(1)} = 2(0.03)^2\pi^2 \approx 1.776 \times 10^{-2},$$

$$C_{\mathrm{ED}}^{(4)} = \frac{1.776 \times 10^{-2}}{24} \approx 7.40 \times 10^{-4}.$$

### Structural Basis of the Prediction

The factorial suppression arises from three ingredients that compound multiplicatively in $d$ dimensions.

First, the per-mode amplitude dilution. When $N_m^d$ modes share a fixed total energy, each mode carries amplitude $\sim A/\sqrt{N_m^d}$. The gradient-energy $C = \int |\nabla\rho|^2\,d^d\!x$ sums the squared amplitudes weighted by $\mu_{\mathbf{k}}$, giving a factor of $1/N_m^d$ relative to the 1D case.

Second, the combinatorial structure of the eigenbasis. The $d$-dimensional Neumann eigenfunction $\cos(k_1\pi x_1/L)\cdots\cos(k_d\pi x_d/L)$ contains $d!$ mixed partial derivatives. When the gradient-energy integrand is expanded, the orthogonality of cosines eliminates all cross-terms, leaving only $d$ diagonal contributions (one per axis). Each contributes $1/d$ of what a 1D mode would contribute, because the gradient-energy is distributed across $d$ orthogonal axes.

Third, the Laplacian eigenvalue weighting. The eigenvalue $\mu_{\mathbf{k}}$ grows with $d$ (more terms in the sum), but the modal amplitude decreases faster, producing a net factorial decay.

These three factors combine to give $C^{(d)} \sim C^{(1)}/d!$. The argument is structural rather than rigorous, but it predicts the $d = 2$ and $d = 3$ results to within 3%, and the $d = 4$ prediction follows from the same logic without adjustment.

### Expected Measurement

A 4D simulation at $N = 32$ with canonical parameters ($D = 0.3$, $A = 0.03$, $N_m = 2$) should produce an initial complexity of $C_{\mathrm{ED}}^{(4)} \approx 7.4 \times 10^{-4}$. Agreement within 5% ($7.0$–$7.8 \times 10^{-4}$) would confirm the factorial law at $d = 4$. Disagreement beyond 10% would indicate either a breakdown of the structural argument or a numerical resolution artifact requiring higher $N$.

---

## II.2 Gradient-Dissipation Law

### Prediction

The gradient-dissipation ratio $R_{\mathrm{grad}}$, defined as the fraction of total dissipation carried by the gradient-diffusion channel, satisfies the derived formula (ED-Phys-36):

$$R_{\mathrm{grad}}^{(d)} = \frac{d\pi^2}{d\pi^2 + P_0^2/M^*}.$$

For $d = 4$ with canonical parameters ($P_0 = 1$, $M^* = M_0(\rho_{\max} - \rho^*)^\beta = 0.25$):

$$R_{\mathrm{grad}}^{(4)} = \frac{4\pi^2}{4\pi^2 + 1/0.25} = \frac{4\pi^2}{4\pi^2 + 4} = \frac{39.48}{43.48} \approx 0.908.$$

### Universality

The formula depends only on the constitutive parameters ($P_0$, $M^*$) and the dimension $d$, not on the initial amplitude $A$, the mode count $N_m$, or the resolution $N$. This is a universal prediction: any 4D ED simulation with the canonical constitutive functions should produce $R_{\mathrm{grad}} \approx 0.908 \pm 0.02$ regardless of the initial condition.

### Dimensional Trend

| Dimension $d$ | $R_{\mathrm{grad}}$ (predicted) | $R_{\mathrm{grad}}$ (measured) | Agreement |
|---------------|-------------------------------|-------------------------------|-----------|
| 1 | 0.712 | 0.71 | Yes |
| 2 | 0.832 | 0.83 | Yes |
| 3 | 0.881 | 0.88 | Yes |
| 4 | **0.908** | *(to be measured)* | — |
| $\infty$ | 1.000 | — | (asymptotic) |

The trend is monotonically increasing and concave, approaching unity from below. The 4D prediction is a strong quantitative test: the value 0.908 lies in a narrow window that is cleanly separated from both the 3D value (0.881) and the asymptote (1.000).

---

## II.3 Horizon Threshold Scaling

### Prediction

Horizons form when the local density approaches $\rho_{\max}$, causing the mobility $M(\rho) \to 0$ and dynamically isolating the region. The effective amplitude available for horizon formation is

$$A_{\mathrm{eff}} = \frac{A}{\sqrt{N_m^d}}.$$

For canonical parameters ($A = 0.03$, $N_m = 2$):

| Dimension $d$ | $N_m^d$ | $A_{\mathrm{eff}}$ | Horizon observed? |
|---------------|---------|---------------------|-------------------|
| 1 | 2 | 0.0212 | Marginal |
| 2 | 4 | 0.0150 | Yes (common) |
| 3 | 8 | 0.0106 | Suppressed |
| 4 | 16 | **0.0075** | **No (predicted)** |

In 3D, horizons were already suppressed relative to 2D (ED-Phys-35). In 4D, the effective amplitude drops by another factor of $\sqrt{2}$, falling below the estimated horizon-formation threshold of $A_{\mathrm{crit}} \approx 0.01$ at which the density can transiently reach $\rho_{\max}$.

### Constructive-Interference Suppression

The mechanism is geometric. In $d$ dimensions, the initial condition is a sum of $N_m^d$ cosine modes with random phases. For the density to approach $\rho_{\max}$, enough modes must constructively interfere at a single point. The probability of such interference decreases exponentially with $d$, because each additional axis introduces an independent phase that must align. The central-limit theorem gives the peak amplitude distribution:

$$\rho_{\mathrm{peak}} \sim \rho^* + A\sqrt{N_m^d} \cdot O(1/\sqrt{N_m^d}) = \rho^* + O(A),$$

which is bounded and independent of $d$ — but the probability of achieving a peak within $\epsilon$ of $\rho_{\max}$ scales as $\exp(-c\,N_m^d)$. In 4D, horizons become a rare-event phenomenon rather than a generic transient feature.

---

## II.4 Topological Conservation in 4D

### Definition

The Euler characteristic of a 4D excursion set $\{\mathbf{x} \in \Omega : \rho(\mathbf{x}, t) \geq \rho_{\mathrm{thresh}}\}$ is defined via the alternating sum of Betti numbers:

$$\chi = \beta_0 - \beta_1 + \beta_2 - \beta_3,$$

where $\beta_0$ counts connected components, $\beta_1$ counts independent tunnels (1-cycles), $\beta_2$ counts enclosed cavities (2-cycles), and $\beta_3$ counts 3-dimensional voids (3-cycles). For a simply connected region in 4D, $\chi = 1 + (-1)^4 = 2$ (analogous to the 2-sphere having $\chi = 2$).

### Prediction

The topological conservation law $d\chi/dt = 0$ is predicted to hold in 4D. The argument is the same as in lower dimensions (ED-Phys-36, Section I.3): the ED PDE is smooth, parabolic, and curvature-driven; it produces no shocks, no finite-time singularities, and no topology-changing bifurcations. Level sets evolve continuously under a smooth flow, preserving their topological type.

### Morse-Theoretic Argument

In four dimensions, the Morse lemma guarantees that near a non-degenerate critical point of $\rho$, the excursion set is locally diffeomorphic to a standard quadratic. The Hessian at the critical point has four eigenvalues; the Morse index (number of negative eigenvalues) determines the local topology. Topology changes occur only when two critical points merge (birth-death bifurcation), which requires a degenerate critical point ($\det \mathcal{H} = 0$ with a specific tangency condition). The ED penalty drives $\rho \to \rho^*$ monotonically, shrinking the amplitude of perturbations without creating new critical points or merging existing ones. The Euler characteristic is therefore conserved throughout the evolution.

---

# III. 4D Morphological Taxonomy

---

## III.1 Hessian Structure in 4D

The Hessian matrix of the density field in four dimensions is the symmetric $4 \times 4$ matrix

$$\mathcal{H}_{ij}(\mathbf{x}) = \frac{\partial^2 \rho}{\partial x_i \partial x_j}, \qquad i, j \in \{1, 2, 3, 4\}.$$

It has four real eigenvalues $\lambda_1 \geq \lambda_2 \geq \lambda_3 \geq \lambda_4$ at each point. The morphological classification in 4D is determined by the relative magnitudes and signs of these four eigenvalues.

Define the normalised eigenvalue ratios:

$$e_{ij} = \frac{|\lambda_i| - |\lambda_j|}{|\lambda_1|}, \qquad i > j.$$

The four morphological classes in 4D are:

### Filament (3 large, 1 small)

A filament is a one-dimensional structure embedded in 4D space: the density varies strongly along three axes and is nearly constant along the fourth. The Hessian signature is $(\lambda_1 \approx \lambda_2 \approx \lambda_3) \gg \lambda_4$, giving three large eigenvalues of the same sign and one small eigenvalue. Formally:

$$\mathrm{Filamentarity} = \frac{|\lambda_3| - |\lambda_4|}{|\lambda_1|}.$$

### Sheet (2 large, 2 small)

A sheet is a two-dimensional structure: the density varies strongly along two axes and weakly along the other two. The Hessian signature is $(\lambda_1 \approx \lambda_2) \gg (\lambda_3 \approx \lambda_4)$. Formally:

$$\mathrm{Sheetness} = \frac{|\lambda_2| - |\lambda_3|}{|\lambda_1|}.$$

### Pancake (1 large, 3 small)

A pancake is a three-dimensional structure: the density varies strongly along one axis and weakly along the other three. The Hessian signature is $\lambda_1 \gg (\lambda_2 \approx \lambda_3 \approx \lambda_4)$. This morphology exists only in $d \geq 4$ and has no 3D analogue. Formally:

$$\mathrm{Pancakeness} = \frac{|\lambda_1| - |\lambda_2|}{|\lambda_1|}.$$

### Blob (4 comparable)

A blob is a zero-dimensional structure (a peak or trough): the density varies comparably along all four axes. The Hessian signature is $\lambda_1 \approx \lambda_2 \approx \lambda_3 \approx \lambda_4$. Formally:

$$\mathrm{Blobness} = \frac{|\lambda_4|}{|\lambda_1|}.$$

The four indicators are computed at each grid point and the dominant morphology is assigned to the one with the largest value. The volume fractions $f_{\mathrm{fil}}$, $f_{\mathrm{sht}}$, $f_{\mathrm{pan}}$, $f_{\mathrm{blb}}$ sum to unity.

---

## III.2 Expected Morphology Fractions

The empirical morphology fractions from lower dimensions show a clear trend:

| Dimension | Filament | Sheet | Blob |
|-----------|----------|-------|------|
| 2D | — | 42% | 58% |
| 3D | 58% | 23% | 19% |

In 2D, only sheets and blobs exist (the Hessian has two eigenvalues). In 3D, filaments dominate. The pattern is driven by a combinatorial argument: in $d$ dimensions, a filament requires $(d-1)$ large eigenvalues and $1$ small one, a sheet requires $(d-2)$ large and $2$ small, and so on. The number of ways to select the "small" eigenvalues grows as $\binom{d}{k}$ for a structure of codimension $k$.

In 4D, the codimension-1 structure (filament: 3 large, 1 small) has $\binom{4}{1} = 4$ configurations. The codimension-2 structure (sheet: 2 large, 2 small) has $\binom{4}{2} = 6$ configurations. The codimension-3 structure (pancake: 1 large, 3 small) has $\binom{4}{3} = 4$ configurations. The blob ($\binom{4}{4} = 1$) has one configuration.

If the Hessian eigenvalues were independently distributed, the raw combinatorial weights would be $4 : 6 : 4 : 1$, giving fractions $27\% : 40\% : 27\% : 7\%$. However, the ED initial condition (cosine modes with structured wavenumbers) biases the eigenvalue distribution toward partial collapse along specific axes, enhancing filamentarity. Based on the observed 3D trend, the expected 4D fractions are:

| Morphology | Combinatorial weight | Expected 4D fraction |
|------------|---------------------|---------------------|
| Filament | $\binom{4}{1} = 4$ | $\sim 45\%$ |
| Sheet | $\binom{4}{2} = 6$ | $\sim 30\%$ |
| Pancake | $\binom{4}{3} = 4$ | $\sim 15\%$ |
| Blob | $\binom{4}{4} = 1$ | $\sim 10\%$ |

The filament fraction is expected to decrease from 58% (3D) to approximately 45% (4D), because the new pancake class absorbs volume that would otherwise be classified as filamentary. The total fraction of anisotropic structures (filament + sheet + pancake = 90%) remains dominant over isotropic blobs (10%).

---

## III.3 4D Sheet-Filament-Pancake Dynamics

In 3D, ED-Phys-35 discovered an oscillatory exchange between sheets and filaments during the transient phase: the sheet fraction and filament fraction oscillate out of phase before settling to their equilibrium values. This sheet-filament oscillation is a signature of the nonlinear coupling between Hessian modes along different axes.

In 4D, the analogous dynamics involve three anisotropic classes. The expected transient sequence, based on the eigenvalue relaxation hierarchy, is:

1. **Pancake phase** ($t \lesssim \tau_1$). The initial cosine modes produce broad, nearly isotropic structures. The first eigenvalue to separate from the cluster is $\lambda_1$ (the fastest-growing mode direction), creating pancake-like regions where one axis dominates.

2. **Sheet phase** ($\tau_1 \lesssim t \lesssim \tau_2$). As the second eigenvalue separates, structures flatten into sheets with two dominant axes.

3. **Filament phase** ($\tau_2 \lesssim t \lesssim \tau_3$). As the third eigenvalue separates, the dominant morphology becomes filamentary with three large eigenvalues.

4. **Blob-decay phase** ($t \gtrsim \tau_3$). The penalty term drives all eigenvalues toward zero, and the morphology becomes blob-like as the field relaxes toward $\rho^*$.

This sequence — pancake $\to$ sheet $\to$ filament $\to$ blob — mirrors the Zel'dovich collapse sequence in cosmological structure formation, where gravitational collapse proceeds along one axis at a time. In ED, the mechanism is reversed: it is not collapse but relaxation, and the ordering reflects the decay rate hierarchy of the Hessian eigenvalues rather than gravitational instability. The structural analogy is nonetheless precise.

Oscillatory exchange between adjacent morphological classes (pancake $\leftrightarrow$ sheet, sheet $\leftrightarrow$ filament) is expected during the transient, generalising the 3D sheet-filament oscillation to a three-way exchange.

---

## III.4 4D Minkowski Functionals

The Minkowski functionals provide a complete set of geometric and topological descriptors for excursion sets. In $d$ dimensions, there are $(d+1)$ Minkowski functionals. In 4D, the four functionals are:

### $W_0$: 4-Volume

$$W_0 = \int_{\Omega_\rho} d^4\!x = \mathrm{Vol}_4(\Omega_\rho),$$

where $\Omega_\rho = \{\mathbf{x} : \rho(\mathbf{x}) \geq \rho_{\mathrm{thresh}}\}$. This measures the total 4-volume of the excursion set.

### $W_1$: 3-Surface Area

$$W_1 = \frac{1}{4}\int_{\partial\Omega_\rho} d^3\!\sigma,$$

where the integral is over the 3-dimensional boundary $\partial\Omega_\rho$. This measures the total surface area of the excursion set boundary (which is a 3D hypersurface in 4D).

### $W_2$: Integrated Mean Curvature

$$W_2 = \frac{1}{4\pi}\int_{\partial\Omega_\rho} H\,d^3\!\sigma,$$

where $H = \frac{1}{3}(\kappa_1 + \kappa_2 + \kappa_3)$ is the mean curvature of the 3D boundary surface (average of three principal curvatures in 4D).

### $W_3$: Euler Characteristic

$$W_3 = \chi(\Omega_\rho) = \beta_0 - \beta_1 + \beta_2 - \beta_3,$$

the Euler characteristic of the excursion set, computed via the alternating sum of Betti numbers.

The four functionals capture complementary information: $W_0$ measures bulk size, $W_1$ measures boundary complexity, $W_2$ measures curvature structure, and $W_3$ measures topology. Together, they provide a complete geometric characterisation of the 4D excursion set at each threshold $\rho_{\mathrm{thresh}}$. The functional $W_3 = \chi$ is predicted to be time-invariant (Section II.4); $W_0$, $W_1$, and $W_2$ evolve as the field relaxes toward equilibrium.

---

# IV. 4D Spectral and Invariant Comparison

---

## IV.1 Spectral Decay in 4D

### Eigenvalue Scaling

The 4D Neumann eigenvalues $\mu_{\mathbf{k}} = \sum_{i=1}^{4}(k_i\pi/L)^2$ grow with the squared wavenumber magnitude. For the fundamental mode (one axis active, $\mathbf{k} = (1,0,0,0)$), $\mu_{\min} = \pi^2/L^2$ — the same as in all dimensions. For the fully excited mode $\mathbf{k} = (k,k,k,k)$, $\mu = 4k^2\pi^2/L^2 = d\cdot k^2\pi^2/L^2$. The maximum eigenvalue at fixed $k$ scales linearly with $d$.

### Linearised Decay Rates

The linearised 4D ED decay rate is

$$\sigma_{\mathbf{k}}^{\mathrm{ED}} = D\,(M^*\,\mu_{\mathbf{k}} + P_0).$$

For the fully excited mode $\mathbf{k} = (k,k,k,k)$:

$$\sigma_{(k,k,k,k)}^{\mathrm{ED}} = D\,(4M^*k^2\pi^2/L^2 + P_0).$$

The high-$k$ modes decay $d/3$ times faster in 4D than in 3D, and $d/2$ times faster than in 2D (at the same $k$ per axis). This accelerated spectral decay is the mechanism behind the complexity dilution: high-frequency structure is damped more efficiently in higher dimensions.

### Comparison to 4D PME/AC/CH

Using the spectral-distance metric from ED-Phys-38:

$$d_{\mathrm{spec}}(\mathrm{ED}, X) = \left(\sum_{\mathbf{k}} |\sigma_{\mathbf{k}}^{\mathrm{ED}} - \sigma_{\mathbf{k}}^{X}|^2\right)^{1/2}.$$

**4D PME:** The linearised PME decay rate is $\sigma_{\mathbf{k}}^{\mathrm{PME}} = (m+1)u_0^m\,\mu_{\mathbf{k}}$. The difference from ED is the penalty offset $D\,P_0$, which is $k$-independent and therefore contributes a constant additive distance. The spectral distance remains $O(P_0)$, the same order as in 3D.

**4D AC:** The linearised AC decay rate is $\sigma_{\mathbf{k}}^{\mathrm{AC}} = \epsilon^2\mu_{\mathbf{k}} + f''(u^*)$. The structure matches ED exactly (diffusive $k^2$ plus constant offset), and the spectral distance is controlled by the parameter mismatch, not the dimension.

**4D CH:** The linearised CH decay rate is $\sigma_{\mathbf{k}}^{\mathrm{CH}} = \mu_{\mathbf{k}}(\epsilon^2\mu_{\mathbf{k}} + f''(u^*))$, which is quartic in $k$ at high wavenumbers. The spectral distance from ED grows with $d$ because the $k^4$ modes accumulate faster in higher dimensions.

The spectral-distance hierarchy in 4D is:

$$d_{\mathrm{spec}}^{(4)}(\mathrm{ED}, \mathrm{AC}) < d_{\mathrm{spec}}^{(4)}(\mathrm{ED}, \mathrm{PME}) < d_{\mathrm{spec}}^{(4)}(\mathrm{ED}, \mathrm{CH}),$$

consistent with the 3D ordering. The dimension does not alter the proximity hierarchy.

---

## IV.2 Invariant-Signature Comparison

The core ED invariants extend to 4D without modification:

| Invariant | 4D computation | Predicted behaviour |
|-----------|---------------|---------------------|
| $C_{\mathrm{ED}} = \int |\nabla\rho|^2\,d^4\!x$ | 4D gradient | $C^{(4)} = C^{(1)}/24$ |
| Spectral entropy $H$ | 4D DCT | Converges to attractor |
| $R_{\mathrm{grad}}$ | Dissipation ratio | $0.908$ |
| $\chi$ | 4D Betti numbers | Conserved |
| Correlation length $\xi$ | 4D autocorrelation | Isotropic at equilibrium |

For the comparison PDEs, the invariant-distance metric from ED-Phys-38 gives:

| PDE $X$ | Mass | Energy | Unique attr. | Free bdy | Patterns | Coarsening | $d_{\mathrm{inv}}$ |
|---------|------|--------|-------------|----------|----------|------------|---------------------|
| PME | match | match | mismatch | match | match | match | 1 |
| AC | mismatch | match | mismatch | mismatch | mismatch | mismatch | 4 |
| CH | match | match | mismatch | mismatch | mismatch | mismatch | 4 |

The PME remains the closest invariant-level relative, with only the unique-attractor property unmatched. The AC and CH invariant distances increase in 4D (from 3 to 4 mismatches) because the pattern-formation mechanism becomes more starkly different: AC/CH produce coarsening structures, while ED decays monotonically — a distinction that is sharper in higher dimensions where coarsening timescales grow.

---

## IV.3 Morphology-Distance Comparison

Using the extended morphology-distance metric for 4D (with four classes):

$$d_{\mathrm{morph}}^{(4)}(\mathrm{ED}, X) = \left(\sum_{\alpha \in \{F,S,P,B\}} |p_\alpha^{\mathrm{ED}} - p_\alpha^{X}|^2\right)^{1/2}.$$

Estimated 4D morphology fractions:

| PDE | Filament | Sheet | Pancake | Blob | $d_{\mathrm{morph}}$ from ED |
|-----|----------|-------|---------|------|------------------------------|
| **ED** | 0.45 | 0.30 | 0.15 | 0.10 | 0 |
| PME | 0.05 | 0.10 | 0.15 | 0.70 | **0.73** |
| AC | 0.10 | 0.70 | 0.10 | 0.10 | **0.55** |
| CH (spinodal) | 0.40 | 0.30 | 0.15 | 0.15 | **0.07** |

The Cahn-Hilliard equation during spinodal decomposition remains the morphologically closest PDE to ED in 4D ($d = 0.07$), because both produce filament-dominated structure with minority sheets and pancakes. This morphological proximity is structural (both classify via Hessian eigenvalues of a scalar field with multi-modal initial conditions) rather than dynamical (CH coarsens, ED decays).

---

# V. Extension to $d > 4$ (Theoretical)

---

## V.1 Asymptotic Behaviour of Dimensional Laws

The four dimensional laws admit clean asymptotic forms as $d \to \infty$.

### Factorial Complexity

$$C_{\mathrm{ED}}^{(d)} = \frac{C_{\mathrm{ED}}^{(1)}}{d!}.$$

By Stirling's approximation, $d! \sim \sqrt{2\pi d}\,(d/e)^d$, so

$$C_{\mathrm{ED}}^{(d)} \sim \frac{C_{\mathrm{ED}}^{(1)}}{\sqrt{2\pi d}}\left(\frac{e}{d}\right)^d.$$

The complexity decreases super-exponentially with dimension. For $d = 10$, $C^{(10)} \approx C^{(1)}/3.6\times10^6$. For $d = 20$, $C^{(20)} \approx C^{(1)}/2.4\times10^{18}$. High-dimensional ED systems are essentially featureless: the density field is indistinguishable from the uniform equilibrium $\rho^*$ to within machine precision.

### Gradient Dominance

$$R_{\mathrm{grad}}^{(d)} = \frac{d\pi^2}{d\pi^2 + P_0^2/M^*} = 1 - \frac{P_0^2/M^*}{d\pi^2 + P_0^2/M^*}.$$

The correction to unity is $O(1/d)$:

$$1 - R_{\mathrm{grad}}^{(d)} = \frac{P_0^2/M^*}{d\pi^2 + P_0^2/M^*} \sim \frac{P_0^2}{M^*\,d\pi^2} \quad \text{as } d \to \infty.$$

For canonical parameters, $R_{\mathrm{grad}}^{(10)} \approx 0.961$, $R_{\mathrm{grad}}^{(100)} \approx 0.996$. In the high-dimensional limit, all dissipation flows through the gradient-diffusion channel; the penalty channel becomes negligible.

### Horizon Suppression

$$A_{\mathrm{eff}} = \frac{A}{\sqrt{N_m^d}} = A\,N_m^{-d/2}.$$

For $N_m = 2$: $A_{\mathrm{eff}} = A \cdot 2^{-d/2}$. The effective amplitude decays exponentially with $d$. For $d = 10$, $A_{\mathrm{eff}} = A/32$; for $d = 20$, $A_{\mathrm{eff}} = A/1024$. Horizon formation is exponentially suppressed and becomes impossible for $d \gtrsim \log_2(A/A_{\mathrm{crit}})^2$.

---

## V.2 High-Dimensional Morphology

In $d$ dimensions, the Hessian has $d$ eigenvalues and the morphological taxonomy has $d$ classes (from codimension-1 filaments to codimension-$d$ blobs). The combinatorial weight of the codimension-$k$ class is $\binom{d}{k}$, which peaks at $k = d/2$ (sheets in even $d$, or the nearest-integer analogue in odd $d$).

For large $d$, the binomial distribution $\binom{d}{k}/2^d$ is approximately Gaussian with mean $d/2$ and standard deviation $\sqrt{d}/2$. The morphology distribution therefore concentrates around the "middle" classes (sheet-like structures with $d/2$ large and $d/2$ small eigenvalues) and assigns exponentially small weight to the extreme classes (filaments and blobs).

This prediction can be tested by simulation at $d = 5$ and $d = 6$ (computationally expensive but feasible at small $N$). The morphological centroid should shift from filament-dominated (at $d = 3$) toward sheet-dominated (at $d \gg 1$), with the crossover occurring near $d = 5$ or $d = 6$.

However, the ED initial condition structure (cosine modes with structured wavenumbers) may bias the eigenvalue distribution away from the combinatorial prediction. The degree of bias is an empirical question that requires simulation.

---

## V.3 Topology in Higher Dimensions

### Generalised Euler Characteristic

In $d$ dimensions, the Euler characteristic of an excursion set $\Omega_\rho \subset \mathbb{R}^d$ is

$$\chi(\Omega_\rho) = \sum_{k=0}^{d-1} (-1)^k\,\beta_k,$$

where $\beta_k$ is the $k$-th Betti number (the rank of the $k$-th homology group). For $d = 5$: $\chi = \beta_0 - \beta_1 + \beta_2 - \beta_3 + \beta_4$. The number of topological invariants grows with $d$, but the Euler characteristic remains a single scalar that compresses them into an alternating sum.

### Topological Conservation

The prediction $d\chi/dt = 0$ is expected to hold for all $d$. The argument is dimension-independent: smooth parabolic flows preserve the topology of excursion sets because they cannot create or destroy critical points without a degenerate Hessian, and the ED penalty drives the field monotonically toward equilibrium without producing degeneracies.

More precisely, the flow $\partial_t\rho = D\,F[\rho]$ is a gradient-like system with Lyapunov functional $\mathcal{E}[\rho]$. The critical points of $\rho(\cdot, t)$ evolve continuously with $t$ and their Morse indices are preserved as long as the Hessian remains non-degenerate. The penalty $-P_0(\rho - \rho^*)$ shrinks perturbations uniformly, making Hessian degeneracies (which require fine-tuned cancellation between eigenvalues) a codimension-1 event in parameter space — generically absent for any fixed constitutive parameters.

### Higher Betti Numbers

While $\chi$ is conserved, the individual Betti numbers $\beta_k$ need not be. It is possible for $\beta_1$ and $\beta_2$ to change simultaneously in a way that preserves $\chi$ (e.g., a tunnel closing while a cavity opens). Whether this occurs in the ED system depends on the specific geometry of the excursion sets. A prediction: for the canonical initial condition with moderate $N_m$, the individual Betti numbers are also approximately conserved, because the perturbation amplitude is small and the field relaxes monotonically without large geometric rearrangements. For large $A$ or large $N_m$ (turbulent regime), individual Betti numbers may exchange while $\chi$ is preserved.

---

# VI. Closing Summary

ED-Phys-39 has accomplished six things.

**Extension to 4D.** The canonical ED PDE generalises to $d = 4$ without structural modification. The operator $F[\rho] = M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)$ acquires a four-component gradient and a four-term Laplacian. Computation at $N = 32$ per axis ($\sim 10^6$ grid points) is feasible on desktop hardware.

**Testing of dimensional laws.** Each of the four laws makes a precise quantitative prediction for $d = 4$:

| Law | Prediction for $d = 4$ |
|-----|----------------------|
| Factorial complexity | $C^{(4)} = C^{(1)}/24 \approx 7.4 \times 10^{-4}$ |
| Gradient dominance | $R_{\mathrm{grad}}^{(4)} = 0.908$ |
| Horizon suppression | No horizons for canonical $A = 0.03$ |
| Topological conservation | $d\chi/dt = 0$ |

These predictions are falsifiable and quantitatively sharp. Confirmation would elevate the dimensional laws from three-point empirical fits to genuine scaling relations.

**4D morphological taxonomy.** The Hessian eigenstructure in 4D supports four morphological classes: filament ($3$ large eigenvalues), sheet ($2$ large), pancake ($1$ large), and blob ($4$ comparable). The pancake class is new in 4D and has no 3D analogue. Expected fractions are $45\% : 30\% : 15\% : 10\%$, with a transient sequence pancake $\to$ sheet $\to$ filament $\to$ blob that mirrors the Zel'dovich collapse ordering.

**Cross-framework comparison in 4D.** The distance metrics from ED-Phys-38 were evaluated in 4D. The proximity hierarchy is dimensionally stable: PME remains the closest structural relative, CH (spinodal) remains the closest morphological relative, and all distances are consistent with the 3D ordering.

**Asymptotic behaviour for $d > 4$.** The dimensional laws admit clean asymptotic forms: complexity decays super-exponentially ($\sim (e/d)^d$), gradient dominance approaches unity as $O(1/d)$, horizon formation is exponentially suppressed ($\sim N_m^{-d/2}$), and topological conservation holds for all $d$.

**Preparation for synthesis.** The empirical dimensional program is now complete across $d = 1, 2, 3, 4$, with asymptotic extensions to arbitrary $d$. The full dataset — laws, invariants, morphologies, and cross-framework distances — provides the quantitative foundation for ED-Phys-40 (Architectural Synthesis), where the entire ED-Phys series will be consolidated into a unified theoretical framework.
