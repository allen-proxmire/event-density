# ED-Phys-35: 3D Invariant Atlas

**Module:** `invariants_3d.py`
**Tests:** `test_invariants_3d.py` (32/32 PASS)

---

## A. Spectral Invariants

### A1. Modal Amplitudes `modal_amplitudes_3d()`

3D Neumann eigenbasis expansion: $u = \rho - \rho^* = \sum a_{k_x,k_y,k_z}\,\phi_{k_x}\phi_{k_y}\phi_{k_z}$.
L^2-normalised via DCT-I. Parseval verified to 1.0000.

### A2. Spectral Entropy `spectral_entropy_3d()`

$H = -\sum p_\mathbf{k} \ln p_\mathbf{k}$, where $p_\mathbf{k} = |a_\mathbf{k}|^2 / E_\text{total}$.

### A3. Renyi Entropy `renyi_entropy_3d()`

$H_q = \frac{1}{1-q}\ln\sum p_\mathbf{k}^q$. Ordering $H_{0.5} \geq H_1 \geq H_2$ verified.

### A4. Geometric Norms `geometric_norms_3d()`

$G_\alpha = \sum |\mathbf{k}|^{2\alpha} |a_\mathbf{k}|^2$ with $|\mathbf{k}|^2 = (k_x\pi/L_x)^2 + (k_y\pi/L_y)^2 + (k_z\pi/L_z)^2$.

### A5. Spectral Anisotropy `spectral_anisotropy_3d()`

3x3 spectral inertia tensor $I_{ij} = \langle k_i k_j \rangle_E$, eigenvalues $\lambda_1 \geq \lambda_2 \geq \lambda_3$:

| Index | Formula | Meaning |
|-------|---------|---------|
| Planarity | $1 - \lambda_2/\lambda_1$ | Energy concentrated in a plane |
| Linearity | $1 - \lambda_3/\lambda_2$ | Energy concentrated in a line |
| Isotropy | $\lambda_3/\lambda_1$ | Equal energy in all directions |

Verified: multi-mode cos(x)+cos(y)+cos(z) gives isotropy = 1.000; x-only gives linearity = 1.000.

### A6. Modal Hierarchy `modal_hierarchy_3d()`

Radially-binned energy spectrum $E(|\mathbf{k}|)$ and power-law decay rate $\beta$.

---

## B. Dynamical Invariants

### B1. ED-Complexity `ed_complexity_3d()`

$C_\text{ED} = \int_\Omega |\nabla\rho|^2\,dV$, computed via 3-component central differences.

### B2. Effective ED-Complexity `ed_complexity_effective_3d()`

$C_\text{ED}^\text{eff} = \int (P'/M)\,|\nabla\rho|^2\,dV$.

### B3--B4. Dissipation Channels and Ratios

$D_\text{grad} = D\,P^{*\prime}\,C_\text{ED}$, $D_\text{pen} = D\,(P^{*\prime})^2/M^*\int(\rho-\rho^*)^2\,dV$, $D_\text{part} = H\,\zeta\,v^2$. Ratios sum to 1.000000 (verified).

### B5. Local Growth Rate `local_growth_rate_3d()`

$\sigma(\mathbf{x}) = M'(\rho)\nabla^2\rho/M(\rho) - P'(\rho)/M(\rho)$.

### B6. Participation Metrics `participation_metrics_3d()`

Steady-state $v_{ss}$, excess, pumping rate, damping rate — identical to 2D.

---

## C. Geometric Invariants (3D-specific)

### C1. Hessian Eigenvalues `hessian_eigenvalues_3d()`

Full 3x3 Hessian $H_{ij} = \partial^2\rho/\partial x_i\partial x_j$ at each grid point. Six unique second derivatives via FD. Eigenvalues computed via `np.linalg.eigvalsh` on the vectorised $(N^3, 3, 3)$ array.

Returns $(\lambda_1, \lambda_2, \lambda_3)$ sorted $\lambda_1 \geq \lambda_2 \geq \lambda_3$.

### C2. Morphology Classification `morphology_3d()`

Eigenvalues sorted by **magnitude** $|\lambda_1| \geq |\lambda_2| \geq |\lambda_3|$:

| Measure | Formula | Meaning |
|---------|---------|---------|
| Filamentarity $F$ | $(|\lambda_2| - |\lambda_3|) / |\lambda_1|$ | Two large eigenvalues, one small |
| Sheetness $S$ | $(|\lambda_1| - |\lambda_2|) / |\lambda_1|$ | One dominant eigenvalue |
| Blobness $B$ | $|\lambda_3| / |\lambda_1|$ | All eigenvalues comparable |

Classification: at each point, the dominant measure determines morphology (FILAMENT, SHEET, or BLOB). Volume fractions reported.

Verified: x-only cos(pi x) gives sheetness = 1.000, filamentarity = 0.000.

### C3. Curvature Invariants `curvature_invariants_3d()`

**Mean curvature** of iso-surfaces $\rho = c$:

$$H = \frac{(\rho_{yy}+\rho_{zz})\rho_x^2 + (\rho_{xx}+\rho_{zz})\rho_y^2 + (\rho_{xx}+\rho_{yy})\rho_z^2 - 2(\rho_{xy}\rho_x\rho_y + \rho_{xz}\rho_x\rho_z + \rho_{yz}\rho_y\rho_z)}{2\,|\nabla\rho|^3}$$

**Gaussian curvature** (via the cofactor matrix of the bordered Hessian):

$$K = \frac{\rho_{xx}(\rho_{yy}\rho_{zz} - \rho_{yz}^2) - \rho_{xy}(\rho_{xy}\rho_{zz} - \rho_{yz}\rho_{xz}) + \rho_{xz}(\rho_{xy}\rho_{yz} - \rho_{yy}\rho_{xz})}{|\nabla\rho|^4}$$

Both weighted by $|\nabla\rho|$ to suppress singularities. Reports RMS and max.

### C4. Twist Tensor `twist_tensor_3d()`

Three off-diagonal second derivatives: $\omega_{xy} = \partial^2\rho/\partial x\partial y$, $\omega_{xz}$, $\omega_{yz}$. Frobenius norm $\sqrt{\omega_{xy}^2 + \omega_{xz}^2 + \omega_{yz}^2}$ measures total twist.

Verified: x-only mode has zero twist; isotropic cos(pi x)cos(pi y)cos(pi z) has nonzero twist.

### C5. Geometric Anisotropy `anisotropy_geometric_3d()`

3x3 structure tensor $T_{ij} = \langle g_i\,g_j \rangle$. Eigenvalues $\sigma_1 \geq \sigma_2 \geq \sigma_3$ give planarity, linearity, isotropy (same indices as spectral anisotropy).

### C6. Horizon Detector `horizon_detector_3d()`

$H_\text{prox} = 1 - M(\rho)/M^*$. Reports max proximity, volume fraction, margin, and number of connected components (via `scipy.ndimage.label`).

---

## D. Topological Invariants (3D-only)

### D1. Minkowski Functionals `minkowski_functionals_3d()`

For the excursion set $\{\rho > \text{threshold}\}$:

| Functional | Symbol | Computation |
|------------|--------|-------------|
| Volume | $V$ | Voxel count $\times h_x h_y h_z$ |
| Surface area | $S$ | Face-counting between excursion and complement |
| Integrated mean curvature | $B$ | $S / (4\pi)$ (normalised approximation) |
| Euler characteristic | $\chi$ | $V_\text{count} - E_\text{count} + F_\text{count} - C_\text{count}$ (digital topology) |

The Euler characteristic distinguishes topology: $\chi = 1$ for a single connected blob, $\chi = 0$ for a torus, $\chi = 2$ for a sphere. Verified: Gaussian blob gives $\chi = 1$.

---

## E. Correlation Invariants

### E1. Correlation Lengths `correlation_lengths_3d()`

Autocorrelation via 3D FFT. E-folding distances $\xi_x, \xi_y, \xi_z$ along each axis.

Verified: isotropic cos gives $\xi_x = \xi_y = \xi_z = 0.155$; x-only gives $\xi_y = \xi_z = 3\xi_x$.

### E2. Structure Functions `structure_functions_3d()`

$S_p(r) = \langle |\rho(\mathbf{x}+\mathbf{r}) - \rho(\mathbf{x})|^p \rangle$ averaged over 6 axis-aligned directions. Default orders $p \in \{2, 4\}$.

---

## F. Top-Level API

| Function | Returns |
|----------|---------|
| `compute_spectral_invariants_3d(rho, params)` | amplitudes, entropy, Renyi, norms, anisotropy, hierarchy |
| `compute_geometric_invariants_3d(rho, params)` | morphology, curvature, twist, anisotropy, horizons, correlations, Minkowski |
| `compute_dynamical_invariants_3d(rho, v, F_bar, params)` | complexity, dissipation, participation, growth rates |
| `compute_invariants_3d(rho, v, F_bar, params)` | All of the above + structure functions |

---

## Validation Summary

32 tests, **32 PASS, 0 FAIL**:

| Test | Result |
|------|--------|
| Parseval identity | ratio = 1.0000 |
| Renyi ordering $H_{0.5} \geq H_1 \geq H_2$ | verified |
| Multi-mode isotropy = 1.000 | verified |
| x-only linearity = 1.000 | verified |
| x-only sheetness = 1.000 | verified |
| Morphology fractions sum to 1.0 | verified |
| Dissipation ratios sum to 1.0 | verified |
| Isotropic $\xi_x = \xi_y = \xi_z$ | verified |
| Minkowski $\chi = 1$ for blob | verified |
| Evolved field: entropy, complexity, ratios | all correct |
