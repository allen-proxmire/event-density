# ED-Phys-35: 2D Invariant Atlas

**Module:** `invariants_2d.py`
**Tests:** `test_invariants_2d.py` (33/33 PASS)

---

## A. Spectral Invariants (1D extensions)

### A1. Modal Amplitudes `modal_amplitudes_2d()`

**Definition:** Expand the perturbation $u = \rho - \rho^*$ in the 2D Neumann eigenbasis:

$$u(x,y) = \sum_{k_x, k_y} a_{k_x, k_y}\, \phi_{k_x}(x)\, \phi_{k_y}(y)$$

where $\phi_0(x) = 1/\sqrt{L_x}$ and $\phi_k(x) = \sqrt{2/L_x}\cos(k\pi x/L_x)$ for $k \geq 1$. Amplitudes are $L^2$-normalised so that $\sum |a_{k_x,k_y}|^2 = \|u\|^2_{L^2}$ (Parseval identity verified to machine precision in tests).

**Implementation:** 2D DCT-I with the corrected normalisation from Phase 2.

### A2. Spectral Entropy `spectral_entropy_2d()`

$$H = -\sum_{k_x, k_y} p_{k_x, k_y} \ln p_{k_x, k_y}, \qquad p_{k_x, k_y} = \frac{|a_{k_x, k_y}|^2}{\sum |a|^2}$$

$H = 0$ for a single-mode field; $H = \ln K$ for uniform distribution. Extends the 1D invariant family (Appendix C.4, Proposition C.29) to 2D.

### A3. Renyi Entropy `renyi_entropy_2d()`

$$H_q = \frac{1}{1-q}\ln\Bigl(\sum p_k^q\Bigr), \qquad q \in \{0.5, 1, 2, 3, 4\}$$

The ordering $H_{0.5} \geq H_1 \geq H_2$ is verified in tests. Multi-scale probes of spectral concentration.

### A4. Radial Spectral Entropy `spectral_entropy_radial()`

Bin the modal energy by wavenumber magnitude $|k| = \sqrt{k_x^2 + k_y^2}$ and compute the entropy of the binned distribution. Captures the isotropic spectral shape independently of anisotropy.

### A5. Geometric Norms `geometric_norms_2d()`

$$G_\alpha = \sum_{(k_x,k_y) \neq (0,0)} |k|^{2\alpha}\, |a_{k_x,k_y}|^2$$

with $\alpha \in \{-2, -1, 0, 1, 2, 3, 4\}$. Negative $\alpha$ weight large-scale structure; positive $\alpha$ weight gradient structure. $G_1$ equals the ED-complexity $C_{\text{ED}} = \int |\nabla u|^2\, dA$.

### A6. Modal Hierarchy `modal_hierarchy_2d()`

Sort modes by radial wavenumber $|k|$, bin the energy, and check for monotone decay. Fits a power-law $E(|k|) \sim |k|^{-\beta}$ and reports the decay exponent $\beta$.

### A7. Spectral Anisotropy `spectral_anisotropy()`

$$A_{\text{spec}} = \frac{E_x - E_y}{E_x + E_y + E_{\text{diag}}}$$

where $E_x = \sum_{k_x > 0} E_{k_x, 0}$ (pure x-modes), etc. Also computes the **spectral eccentricity** from the eigenvalues of the spectral inertia tensor $I_{ij} = \langle k_i k_j \rangle_E$. Verified: $A = 0$ for isotropic fields, $A = 1$ for x-only modes.

### A8. ED-Complexity `modal_complexity_2d()`

$$C_{\text{ED}} = \sum_{k_x, k_y} \mu_{k_x, k_y}\, |a_{k_x, k_y}|^2 = \int |\nabla u|^2\, dA$$

Spectral form of the bare ED-complexity.

---

## B. Dynamical Invariants (1D extensions)

### B1. ED-Complexity (Physical) `ed_complexity_2d()`

$$C_{\text{ED}} = \int_\Omega |\nabla\rho|^2\, dA$$

Computed via central-difference gradient and trapezoidal integration.

### B2. Effective ED-Complexity `ed_complexity_effective_2d()`

$$C_{\text{ED}}^{\text{eff}} = \int_\Omega \frac{P'(\rho)}{M(\rho)}\, |\nabla\rho|^2\, dA$$

State-dependent weighting by the constitutive ratio.

### B3. Dissipation Channels `dissipation_channels_2d()`

Three channels, extending edsim_diagnostics.py:

| Channel | Formula | Role |
|---------|---------|------|
| Gradient | $D_{\text{grad}} = D\, P^{*\prime}\, C_{\text{ED}}$ | Diffusive smoothing |
| Penalty | $D_{\text{pen}} = D\, (P^{*\prime})^2 / M^*\, \int ({\rho - \rho^*})^2 dA$ | Relaxation to $\rho^*$ |
| Participation | $D_{\text{part}} = H\, \zeta\, v^2$ | Participation damping |

### B4. Dissipation Ratios `dissipation_ratios_2d()`

$R_{\text{grad}} + R_{\text{pen}} + R_{\text{part}} = 1$. Verified to sum to 1.000000 in tests.

### B5. Local Growth Rate `local_growth_rate_2d()`

$$\sigma(x,y) = \frac{M'(\rho)}{M(\rho)}\, \nabla^2\rho - \frac{P'(\rho)}{M(\rho)}$$

Pointwise Lyapunov-like growth rate. Negative everywhere for stable attractors.

### B6. Transient Complexity `transient_complexity_2d()`

$$T_C(t) = \frac{d}{dt} C_{\text{ED}}(t)$$

$T_C < 0$: gradient smoothing (inflation). $T_C > 0$: structure formation.

### B7. Participation Metrics `participation_metrics_2d()`

Steady-state $v_{ss} = (\tau/\zeta)\, \bar{F}$, excess $v - v_{ss}$, pumping rate $H\,\bar{F}$, damping rate $H\,\zeta\,v/\tau$.

---

## C. Geometric Invariants (2D-only)

### C1. Vorticity/Twist Structure `vorticity_structure_2d()`

The mixed partial derivative $\omega_H = \partial^2\rho / \partial x\, \partial y$ measures off-diagonal curvature (twist) of the density field. Regions with large $|\omega_H|$ have saddle-like or spiral structure.

- $\omega_H = 0$ everywhere for x-only or y-only modes (verified)
- $\omega_H \neq 0$ for coupled modes like $\cos(\pi x)\cos(\pi y)$ (verified)

### C2. Hessian Eigenvalues `hessian_eigenvalues_2d()`

Eigenvalues $(\lambda_1, \lambda_2)$ of the Hessian matrix $H_{ij} = \partial^2\rho / \partial x_i \partial x_j$ at each point. Classification:

- $\lambda_1, \lambda_2 > 0$: local valley
- $\lambda_1, \lambda_2 < 0$: local peak
- $\lambda_1\,\lambda_2 < 0$: saddle

### C3. Filamentarity `filamentarity_2d()`

$$F = 1 - \frac{|\lambda_{\min}|}{|\lambda_{\max}|}$$

$F = 0$ for isotropic curvature (peaks/valleys); $F = 1$ for perfectly filamentary structure (all curvature in one direction). Also reports sheetness fraction (both eigenvalues same sign) and saddle fraction.

- x-only mode: $F = 1.000$ (verified)
- Isotropic cosine: $F = 0.437$ (verified)

### C4. Geometric Anisotropy `anisotropy_geometric_2d()`

Structure tensor: $T_{ij} = \langle (\partial_i\rho)(\partial_j\rho) \rangle$. Eigenvalues $\sigma_1 \geq \sigma_2$:

$$A_{\text{geom}} = 1 - \sigma_2 / \sigma_1$$

$A_{\text{geom}} = 0$ for isotropic gradients; $A_{\text{geom}} = 1$ for unidirectional gradients.

- Isotropic cosine: $A = 0.000$ (verified)
- x-only mode: $A = 1.000$ (verified)

### C5. Level-Set Curvature `level_set_curvature_2d()`

$$\kappa = \frac{\rho_{xx}\,\rho_y^2 - 2\,\rho_{xy}\,\rho_x\,\rho_y + \rho_{yy}\,\rho_x^2}{|\nabla\rho|^3}$$

The curvature of the level curve $\rho(x,y) = c$ passing through each point. Weighted by $|\nabla\rho|$ to suppress noise at critical points. Reports RMS, max, and mean curvature.

### C6. Horizon Detector `horizon_detector_2d()`

Horizon proximity: $H_{\text{prox}} = 1 - M(\rho)/M^*$. Approaches 1 where $\rho \to \rho_{\max}$ and mobility vanishes. Reports:
- Max proximity (0.988 for near-$\rho_{\max}$ field, verified)
- Horizon area fraction
- Horizon margin $\min(\rho_{\max} - \rho)$

---

## D. Correlation Invariants (2D-only)

### D1. Correlation Lengths `correlation_lengths_2d()`

Autocorrelation function via FFT: $C(r_x, r_y) = \langle u(x,y)\, u(x+r_x, y+r_y) \rangle / \langle u^2 \rangle$

Correlation lengths $\xi_x, \xi_y$ are the $e$-folding distances along each axis. The ratio $\xi_x / \xi_y$ measures correlation anisotropy.

- Isotropic cosine: $\xi_x / \xi_y = 1.000$ (verified)
- x-only mode: $\xi_y / \xi_x = 3.37$ (verified; y is infinitely correlated, x has period-limited correlation)

### D2. Structure Functions `structure_functions_2d()`

$$S_p(r) = \langle |\rho(\mathbf{x} + \mathbf{r}) - \rho(\mathbf{x})|^p \rangle$$

Isotropic average over 4 directions. For smooth fields, $S_p(r) \sim r^p$ at small $r$. Anomalous scaling ($S_p \sim r^{\zeta_p}$ with $\zeta_p \neq p$) indicates intermittency. Orders $p \in \{1, 2, 3, 4\}$ by default.

---

## E. Top-Level API

| Function | Returns |
|----------|---------|
| `compute_spectral_invariants_2d(rho, params)` | modal amplitudes, entropy, Renyi, geometric norms, anisotropy, hierarchy, complexity |
| `compute_geometric_invariants_2d(rho, params)` | twist, filamentarity, geometric anisotropy, curvature, horizons, correlation lengths |
| `compute_dynamical_invariants_2d(rho, v, F_bar, params)` | complexity, dissipation channels/ratios, participation, growth rates |
| `compute_invariants_2d(rho, v, F_bar, params)` | All of the above + structure functions |

---

## Validation Summary

33 tests, **33 PASS, 0 FAIL**. Key verifications:

| Test | Result |
|------|--------|
| Parseval identity | ratio = 1.0000 |
| Renyi ordering $H_{0.5} \geq H_1 \geq H_2$ | verified |
| Isotropic $A_{\text{spec}} = 0$, x-only $A_{\text{spec}} = 1$ | exact |
| Isotropic $A_{\text{geom}} = 0$, x-only $A_{\text{geom}} = 1$ | exact |
| x-only filamentarity = 1.0 | exact |
| Correlation length ratio = 1.0 for isotropic | exact |
| Dissipation ratios sum to 1.0 | exact |
| Uniform field: all dissipation channels = 0 | exact |
| Near-$\rho_{\max}$ horizon proximity > 0.98 | verified |
| Evolved field entropy finite, complexity decayed | verified |
