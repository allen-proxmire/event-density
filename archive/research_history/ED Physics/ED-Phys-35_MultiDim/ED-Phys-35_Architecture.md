# ED-Phys-35: Architectural Specification for the 2D/3D Event Density PDE

**Phase 1 — Mathematical and Numerical Architecture**
**Canonical sources:** ED-Phys-01 (Update Rule), Appendix C (PDE Analysis), edsim_core.py, edsim_parameters.py

---

## 1. The Canonical ED PDE in Arbitrary Spatial Dimension

### 1.1 Coupled System

The canonical ED system on a bounded domain $\Omega \subset \mathbb{R}^d$ ($d = 1, 2, 3$) is the coupled PDE-ODE pair:

$$
\begin{cases}
\partial_t \rho = D\,F[\rho] + H\,v, \\[6pt]
\dot{v} = \dfrac{1}{\tau}\bigl(F[\rho] - \zeta\,v\bigr),
\end{cases}
$$

where $D + H = 1$, $\tau > 0$, $\zeta > 0$, and the **density operator** is:

$$
F[\rho] \;:=\; \nabla\!\cdot\!\bigl[M(\rho)\,\nabla\rho\bigr] \;-\; P(\rho)
\;=\; M(\rho)\,\nabla^2\rho \;+\; M'(\rho)\,|\nabla\rho|^2 \;-\; P(\rho).
$$

The scalar participation variable $v(t) \in \mathbb{R}$ couples to the spatial average $\bar{F} = |\Omega|^{-1}\!\int_\Omega F[\rho]\,dx$ via the exact exponential integrator derived in edsim_core.py.

### 1.2 Constitutive Functions

| Function | Definition | Parameters |
|----------|-----------|------------|
| **Mobility** | $M(\rho) = M_0\,(\rho_{\max} - \rho)^\beta$ | $M_0 > 0$, $\beta > 1$ |
| **Mobility derivative** | $M'(\rho) = -\beta\,M_0\,(\rho_{\max} - \rho)^{\beta-1}$ | |
| **Penalty** (linear) | $P(\rho) = P_0\,(\rho - \rho^*)$ | $P_0 > 0$, $0 < \rho^* < \rho_{\max}$ |
| **Penalty** (power-law) | $P(\rho) = \alpha\,\gamma_{\exp}\,\rho^{\gamma_{\exp}-1}$ | $0 < \gamma_{\exp} < 1$ |

The linear penalty is used in the edsim_core.py canonical solver. The power-law penalty appears in the ED-Phys-01 update rule and ED-12 papers. Both must be supported.

**Mobility parameterization note:** Two conventions exist in the codebase:
- `edsim_parameters.py`: $M(\rho) = M_0\,(\rho_{\max} - \rho)^\beta$ (absolute form)
- `ed_phys_operators.py`: $M(\rho) = M_0\,(1 - \rho/\rho_{\max})^{n_{\text{mob}}}$ (normalized form)

These are equivalent only when $\rho_{\max} = 1$ (the canonical default). For general $\rho_{\max}$, the relationship is $M_0^{(\text{abs})} = M_0^{(\text{norm})} / \rho_{\max}^{n_{\text{mob}}}$. The 2D/3D solver must accept both parameterizations. We adopt the `edsim_parameters.py` convention (absolute form) as canonical and convert internally when needed.

### 1.3 Smoothness and Domain Assumptions

**From Appendix C (PDE Analysis):**

- **State space:** $\mathcal{X} = H^s(\Omega) \times \mathbb{R}$ with $s > d/2 + 2$.
  - $d = 1$: $s > 2.5$ (so $s \geq 3$)
  - $d = 2$: $s > 3$ (so $s \geq 4$)
  - $d = 3$: $s > 3.5$ (so $s \geq 4$)
- **Admissible region:** $0 < \rho(x) < \rho_{\max}$ for all $x \in \overline{\Omega}$.
- **Constitutive smoothness:** $M \in C^\infty([0, \rho_{\max}])$, $P \in C^\infty(\mathbb{R})$.
- **Domain geometry:**
  - $d = 1$: $\Omega = [0, L]$ (interval)
  - $d = 2$: $\Omega = [0, L_x] \times [0, L_y]$ (rectangle)
  - $d = 3$: $\Omega = [0, L_x] \times [0, L_y] \times [0, L_z]$ (box)

For the spectral solver, we additionally require $\Omega$ to be a $d$-dimensional box. For finite-difference methods, the rectangular assumption is sufficient but not strictly necessary (unstructured grids could extend this, but are out of scope for Phase 2).

---

## 2. Explicit Operator Expressions in 2D and 3D

### 2.1 Gradient

$$
\nabla\rho =
\begin{cases}
\bigl(\partial_x\rho\bigr) & d = 1, \\[4pt]
\bigl(\partial_x\rho,\; \partial_y\rho\bigr)^T & d = 2, \\[4pt]
\bigl(\partial_x\rho,\; \partial_y\rho,\; \partial_z\rho\bigr)^T & d = 3.
\end{cases}
$$

### 2.2 Gradient Magnitude Squared

$$
|\nabla\rho|^2 =
\begin{cases}
(\partial_x\rho)^2 & d = 1, \\[4pt]
(\partial_x\rho)^2 + (\partial_y\rho)^2 & d = 2, \\[4pt]
(\partial_x\rho)^2 + (\partial_y\rho)^2 + (\partial_z\rho)^2 & d = 3.
\end{cases}
$$

### 2.3 Laplacian

$$
\nabla^2\rho =
\begin{cases}
\partial_{xx}\rho & d = 1, \\[4pt]
\partial_{xx}\rho + \partial_{yy}\rho & d = 2, \\[4pt]
\partial_{xx}\rho + \partial_{yy}\rho + \partial_{zz}\rho & d = 3.
\end{cases}
$$

### 2.4 Mobility-Weighted Divergence (Full Expansion)

The identity $\nabla\!\cdot\![M(\rho)\,\nabla\rho] = M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2$ holds in all dimensions. Written out:

**2D:**
$$
\nabla\!\cdot\![M(\rho)\,\nabla\rho]
= M(\rho)\,(\partial_{xx}\rho + \partial_{yy}\rho)
\;+\; M'(\rho)\,\bigl[(\partial_x\rho)^2 + (\partial_y\rho)^2\bigr]
$$

**3D:**
$$
\nabla\!\cdot\![M(\rho)\,\nabla\rho]
= M(\rho)\,(\partial_{xx}\rho + \partial_{yy}\rho + \partial_{zz}\rho)
\;+\; M'(\rho)\,\bigl[(\partial_x\rho)^2 + (\partial_y\rho)^2 + (\partial_z\rho)^2\bigr]
$$

### 2.5 Complete PDE (Expanded)

**2D:**
$$
\partial_t\rho = D\Bigl[
  M(\rho)\,(\partial_{xx}\rho + \partial_{yy}\rho)
  + M'(\rho)\,((\partial_x\rho)^2 + (\partial_y\rho)^2)
  - P(\rho)
\Bigr] + H\,v
$$

**3D:**
$$
\partial_t\rho = D\Bigl[
  M(\rho)\,(\partial_{xx}\rho + \partial_{yy}\rho + \partial_{zz}\rho)
  + M'(\rho)\,((\partial_x\rho)^2 + (\partial_y\rho)^2 + (\partial_z\rho)^2)
  - P(\rho)
\Bigr] + H\,v
$$

### 2.6 Nonlinear Penalty Term P(rho)

**Linear penalty** (canonical edsim):
$$
P(\rho) = P_0\,(\rho - \rho^*)
$$
No spatial derivative dependence. Pointwise evaluation, identical in all dimensions.

**Power-law penalty** (ED-Phys-01/ED-12):
$$
P(\rho) = \alpha\,\gamma_{\exp}\,\max(\rho, \varepsilon)^{\gamma_{\exp}-1}
$$
The $\max(\cdot, \varepsilon)$ floor ($\varepsilon \approx 10^{-10}$) prevents the $\rho^{\gamma_{\exp}-1}$ singularity at $\rho = 0$.

---

## 3. Boundary Condition Specification

### 3.1 Periodic Boundary Conditions

**Mathematical statement:** $\rho$ and all its derivatives are periodic on $\Omega$.

| Dimension | Condition |
|-----------|-----------|
| 1D | $\rho(0,t) = \rho(L,t)$ |
| 2D | $\rho(0,y,t) = \rho(L_x,y,t)$, $\rho(x,0,t) = \rho(x,L_y,t)$ |
| 3D | Periodic in each of $x$, $y$, $z$ independently |

**Implementation:** Ghost cells wrap around: the right ghost cell copies the leftmost interior cell, and vice versa. In the spectral method, periodicity is automatically satisfied by the Fourier (DFT) basis. For Neumann-based DCT, periodic BCs require switching to the DFT.

**Physical use:** Cosmological simulations (spatial homogeneity assumption).

### 3.2 Neumann (No-Flux) Boundary Conditions

**Mathematical statement:** $\partial_\nu\rho = 0$ on $\partial\Omega$ (zero normal derivative).

| Dimension | Condition |
|-----------|-----------|
| 1D | $\partial_x\rho\big|_{x=0} = \partial_x\rho\big|_{x=L} = 0$ |
| 2D | $\partial_x\rho\big|_{x=0,L_x} = 0$, $\partial_y\rho\big|_{y=0,L_y} = 0$ |
| 3D | $\partial_x\rho\big|_{x=0,L_x} = 0$, $\partial_y\rho\big|_{y=0,L_y} = 0$, $\partial_z\rho\big|_{z=0,L_z} = 0$ |

**Implementation (FD):** Ghost-point reflection. For a boundary at index 0 in direction $k$:
$$
\rho_{\text{ghost}} = \rho_1 \quad\Longrightarrow\quad
\text{Lap}_{0} = \frac{2(\rho_1 - \rho_0)}{h_k^2}
$$
This matches the existing 1D implementation in edsim_core.py.

**Implementation (Spectral):** The DCT-I basis $\cos(k\pi x/L)$ automatically satisfies Neumann BCs. In 2D/3D, use the $d$-dimensional DCT-I (product of 1D DCTs along each axis).

**Physical use:** Default for the edsim canonical solver. Mass-conserving.

### 3.3 Dirichlet (Fixed) Boundary Conditions

**Mathematical statement:** $\rho\big|_{\partial\Omega} = \rho_{\text{bdy}}$ (typically $\rho_{\text{bdy}} = \rho_{\min}$ for absorbing walls).

| Dimension | Condition |
|-----------|-----------|
| 1D | $\rho(0,t) = \rho(L,t) = \rho_{\text{bdy}}$ |
| 2D | $\rho = \rho_{\text{bdy}}$ on all four edges |
| 3D | $\rho = \rho_{\text{bdy}}$ on all six faces |

**Implementation (FD):** Boundary values are held constant; only interior nodes are updated. The Laplacian stencil at boundary-adjacent nodes uses the fixed boundary value directly.

**Implementation (Spectral):** Requires the DST (Discrete Sine Transform) basis $\sin(k\pi x/L)$, which has homogeneous Dirichlet BCs built in. For non-homogeneous Dirichlet, subtract a lift function.

**Physical use:** Horizon studies, absorbing boundaries.

### 3.4 Mixed Boundary Conditions

Any combination of the above per face is supported in the FD solver. For the spectral solver, mixing requires domain decomposition or a hybrid approach (not recommended for Phase 2).

---

## 4. Stability Considerations

### 4.1 Stiff Terms

| Term | Stiffness | Reason |
|------|-----------|--------|
| $M(\rho)\,\nabla^2\rho$ | **Highly stiff** | Diffusion operator; eigenvalues scale as $O(h^{-2})$. CFL for explicit: $\Delta t < h^2/(2d\,M_0)$. |
| $M'(\rho)\,|\nabla\rho|^2$ | **Mildly stiff** | Nonlinear; bounded by $O(h^{-2})$ through gradient approximation, but coefficients are moderate in practice. |
| $P(\rho)$ | **Non-stiff** (linear) / **Mildly stiff** (power-law) | Linear penalty is $O(1)$. Power-law penalty has $O(\varepsilon^{\gamma_{\exp}-1})$ bound near $\rho = 0$. |
| $H\,v$ (participation) | **Non-stiff** | ODE coupling; exponential integrator handles it exactly. |

### 4.2 Implicit/Semi-Implicit Treatment Requirements

**Required implicit:** The diffusion term $M(\rho)\,\nabla^2\rho$ MUST be treated implicitly or semi-implicitly. Without this, the $O(h^{-2})$ eigenvalues force $\Delta t = O(h^2/d)$, which becomes prohibitive in 2D ($O(h^4)$ total work per unit time for explicit) and catastrophic in 3D ($O(h^6)$ total work).

**Semi-implicit strategy (recommended, matches edsim_core.py):**
- **Implicit:** The linear part of diffusion: $M_{\text{frozen}}\,\nabla^2\rho^{n+1}$, where $M_{\text{frozen}} = M(\rho^n)$ is evaluated at the current time level.
- **Explicit:** The nonlinear correction $M'(\rho^n)\,|\nabla\rho^n|^2$, the penalty $P(\rho^n)$, and the participation coupling $H\,v^n$.

This is the IMEX (Implicit-Explicit) splitting already used in the 1D Crank-Nicolson and Implicit Euler solvers.

**For the spectral method:** The ETD-RK4 approach handles the linear stiff part exactly via exponential integrators, then treats nonlinear terms with explicit RK4 substeps. This extends naturally to $d$ dimensions.

### 4.3 Effect of Dimensionality on Stability

| Factor | 1D | 2D | 3D |
|--------|-----|-----|-----|
| Explicit CFL | $\Delta t < h^2/(2M_0)$ | $\Delta t < h^2/(4M_0)$ | $\Delta t < h^2/(6M_0)$ |
| Implicit solve cost | Tridiagonal $O(N)$ | Sparse $O(N^2)$ per ADI sweep, or FFT $O(N^2\log N)$ | Sparse $O(N^3)$ per ADI sweep, or FFT $O(N^3\log N)$ |
| Memory | $O(N)$ | $O(N^2)$ | $O(N^3)$ |
| Gradient stencil width | 3-point | 5-point (2nd order) | 7-point (2nd order) |

**Key implication:** In 3D with $N = 256$, a single field requires $256^3 \approx 16.7$M floating-point values ($\approx 134$ MB at float64). Multiple auxiliary arrays (Laplacian, gradient squared, mobility, RHS) multiply this by $5$--$8\times$. GPU memory becomes a binding constraint.

### 4.4 Positivity and Boundedness

The physical constraint $0 < \rho < \rho_{\max}$ is not automatically preserved by any standard discretization. After each time step:
$$
\rho^{n+1}_\mathbf{j} \;\leftarrow\; \text{clamp}\bigl(\rho^{n+1}_\mathbf{j},\; \varepsilon,\; \rho_{\max} - \varepsilon\bigr)
$$
with $\varepsilon \approx 10^{-12}$. This matches `enforce_bounds()` in edsim_core.py.

---

## 5. Discretization Strategy

### 5.1 Candidate Methods

#### 5.1.1 Finite Difference (FD)

**Approach:** Second-order central differences on a uniform Cartesian grid. Diffusion treated implicitly via a banded linear solve.

| Aspect | Assessment |
|--------|------------|
| **Clarity** | Excellent. Direct translation of the 1D stencils in edsim_core.py and ed_phys_operators.py to $d$-dimensional index arrays. |
| **Stability** | Good with IMEX splitting. Implicit diffusion removes the CFL constraint on $\Delta t$. |
| **Boundary conditions** | All three types (periodic, Neumann, Dirichlet) are straightforward via ghost cells. |
| **Performance (2D)** | The implicit solve requires either ADI splitting (tridiagonal sweeps in each direction) or a sparse direct/iterative solver. ADI is $O(N^2)$ per step. Competitive for $N \leq 512$. |
| **Performance (3D)** | ADI is $O(N^3)$ per step but requires 3 sweeps. For $N \geq 128$, this is slower than FFT-based approaches. |
| **GPU friendliness** | Explicit stencil evaluation is trivially parallel. Implicit tridiagonal sweeps parallelize via batched Thomas algorithm (one independent tridiagonal system per row/column). Good GPU fit. |

**ADI (Alternating Direction Implicit) Detail:**
In 2D, split the implicit diffusion into two half-steps:
$$
\frac{\rho^{n+1/2} - \rho^n}{\Delta t/2} = D\,M(\rho^n)\,\partial_{xx}\rho^{n+1/2} + D\,M(\rho^n)\,\partial_{yy}\rho^n + \text{explicit terms}
$$
$$
\frac{\rho^{n+1} - \rho^{n+1/2}}{\Delta t/2} = D\,M(\rho^n)\,\partial_{xx}\rho^{n+1/2} + D\,M(\rho^n)\,\partial_{yy}\rho^{n+1} + \text{explicit terms}
$$
Each half-step requires only tridiagonal solves along one direction. This extends to 3D with three sub-steps.

#### 5.1.2 Spectral (FFT-Based)

**Approach:** Expand $\rho$ in the appropriate transform basis (DCT for Neumann, DFT for periodic, DST for Dirichlet). Diffusion is diagonal in spectral space. Nonlinear terms evaluated pseudospectrally.

| Aspect | Assessment |
|--------|------------|
| **Clarity** | Good, but requires careful handling of transform types and de-aliasing. |
| **Stability** | Excellent. ETD-RK4 treats the stiff linear part exactly. No CFL constraint from diffusion. |
| **Boundary conditions** | Neumann (DCT) and periodic (DFT) are natural. Dirichlet (DST) is straightforward for homogeneous case. Mixed BCs are difficult. |
| **Performance (2D)** | $O(N^2 \log N)$ per evaluation. The ETD-RK4 scheme requires 4 nonlinear evaluations per step but allows much larger $\Delta t$. Net performance is excellent for smooth solutions. |
| **Performance (3D)** | $O(N^3 \log N)$ per evaluation. Still competitive due to the large $\Delta t$ allowed by ETD. |
| **GPU friendliness** | cuFFT provides highly optimized $d$-dimensional transforms. Pseudospectral evaluation is pointwise-parallel. Excellent GPU fit. |

**De-aliasing:** The 3/2-rule (already used in SpectralState) pads the spectral coefficients to $\lfloor 3N/2 \rfloor$ physical points before evaluating nonlinearities, then truncates back. In $d$ dimensions, this applies independently along each axis.

#### 5.1.3 Hybrid (FD Nonlinear + FFT Diffusion)

**Approach:** Evaluate $M'(\rho)\,|\nabla\rho|^2$ and $P(\rho)$ with finite differences in physical space. Solve the diffusion step $M_{\text{frozen}}\,\nabla^2\rho = \text{RHS}$ spectrally via FFT.

| Aspect | Assessment |
|--------|------------|
| **Clarity** | Moderate. Mixing two spatial representations adds conceptual overhead. |
| **Stability** | Good. Diffusion is exact in spectral space. |
| **Boundary conditions** | Constrained by the spectral solve (must match DCT/DFT/DST). |
| **Performance** | Two FFTs per step (forward + inverse) plus pointwise nonlinear evaluation. Comparable to pure spectral. |
| **GPU friendliness** | Good. Both FFT and pointwise ops are GPU-native. |

### 5.2 Recommendation

**Primary solver: Spectral ETD-RK4** (extension of the existing Method B).

Rationale:
1. **Already proven in 1D.** The SpectralState class in edsim_core.py implements ETD-RK4 with DCT-I, de-aliasing, and exact participation integration. The 2D/3D generalization is a natural tensor-product extension.
2. **No CFL constraint.** The exponential integrator handles the stiff diffusion exactly, allowing $\Delta t$ orders of magnitude larger than explicit FD.
3. **Spectral accuracy.** For smooth ED fields, the spectral method achieves exponential convergence, meaning far fewer grid points are needed for the same accuracy.
4. **GPU performance.** Multi-dimensional FFTs are the best-optimized numerical kernels on GPUs (cuFFT, VkFFT).

**Secondary solver: FD with ADI** (extension of the existing Method A / Crank-Nicolson).

Rationale:
1. **Validation.** Having two independent solvers enables cross-verification (as in the current 1D suite).
2. **Boundary flexibility.** FD handles mixed and non-standard BCs more easily.
3. **Robustness.** For solutions with sharp gradients near $\rho_{\max}$ (horizon formation), where spectral methods may develop Gibbs oscillations, FD is more robust.

### 5.3 Time Stepping Summary

| Solver | Diffusion | Nonlinear + Penalty | Participation $v$ |
|--------|-----------|--------------------|--------------------|
| **Spectral ETD-RK4** | Exact (exponential integrator) | Explicit (4 RK substeps, pseudospectral) | Exact (exponential integrator) |
| **FD Crank-Nicolson** | Semi-implicit (ADI tridiagonal) | Explicit | Exact (exponential integrator) |
| **FD Implicit Euler** | Fully implicit (ADI tridiagonal) | Explicit | Exact (exponential integrator) |

---

## 6. Data Structures for 2D and 3D Fields

### 6.1 Array Shapes

All field arrays are NumPy ndarrays (CPU) or CuPy/PyTorch tensors (GPU). The convention is **row-major (C order)**, with the fastest-varying index last.

| Quantity | 1D Shape | 2D Shape | 3D Shape |
|----------|----------|----------|----------|
| $\rho$ (interior) | `(Nx,)` | `(Nx, Ny)` | `(Nx, Ny, Nz)` |
| $\rho$ (with ghosts) | `(Nx+2,)` | `(Nx+2, Ny+2)` | `(Nx+2, Ny+2, Nz+2)` |
| Spectral $\hat{\rho}$ | `(Kx,)` | `(Kx, Ky)` | `(Kx, Ky, Kz)` |
| Physical (de-aliased) | `(Px,)` | `(Px, Py)` | `(Px, Py, Pz)` |

Where:
- `Nx, Ny, Nz` = number of interior grid points per axis
- `Kx = Nx` (spectral modes, DCT) or `Kx = Nx` (DFT)
- `Px = floor(3*Kx/2)` (de-aliased physical grid, per axis)

### 6.2 Ghost Cells / Padding

**FD solver:** One layer of ghost cells on each side of each axis.

```
Layout (2D, Neumann):
  ghost_top
  [  interior Nx x Ny  ]
  ghost_bottom

  ghost_left  |  interior  |  ghost_right
```

Implementation via `np.pad(rho, pad_width=1, mode=...)`:
- `mode='wrap'` for periodic
- `mode='reflect'` for Neumann (reflecting)
- `mode='constant'` with `constant_values=rho_bdy` for Dirichlet

This matches the existing `_pad()` function in ed_phys_operators.py.

**Spectral solver:** No ghost cells needed. The transform basis encodes the boundary conditions implicitly. De-aliasing padding is in spectral space (zero-padding high modes before IFFT).

### 6.3 Memory Layout

**CPU (NumPy):**
- Use contiguous C-order arrays (`np.ascontiguousarray`).
- For ADI sweeps along axis $k$, the array should be transposed so that axis $k$ is contiguous. In practice, use `np.swapaxes` before the tridiagonal solve, then swap back.
- Pre-allocate all auxiliary arrays (Laplacian, gradient squared, mobility, RHS, etc.) once at initialization. Do not allocate per-step.

**GPU (CuPy/PyTorch):**
- Use float64 for accuracy (matching the canonical edsim).
- Pre-allocate a work buffer struct containing all needed arrays:

```python
@dataclass
class FieldBuffers:
    """Pre-allocated work arrays for one time step."""
    rho:       ndarray  # (Nx, Ny[, Nz])   -- current density
    rho_new:   ndarray  # (Nx, Ny[, Nz])   -- updated density
    lap:       ndarray  # (Nx, Ny[, Nz])   -- Laplacian
    grad_sq:   ndarray  # (Nx, Ny[, Nz])   -- |grad rho|^2
    M_vals:    ndarray  # (Nx, Ny[, Nz])   -- mobility M(rho)
    Mp_vals:   ndarray  # (Nx, Ny[, Nz])   -- M'(rho)
    P_vals:    ndarray  # (Nx, Ny[, Nz])   -- P(rho)
    F_rho:     ndarray  # (Nx, Ny[, Nz])   -- F[rho]
    rhs:       ndarray  # (Nx, Ny[, Nz])   -- right-hand side
    rho_hat:   ndarray  # (Kx, Ky[, Kz])   -- spectral coefficients
    rho_phys:  ndarray  # (Px, Py[, Pz])   -- de-aliased physical grid
```

**Memory estimates:**

| Resolution | Dimension | Fields (11 arrays) | Total (float64) |
|------------|-----------|--------------------|-----------------:|
| $N = 256$ | 2D | $11 \times 256^2$ | $\approx 5.8$ MB |
| $N = 512$ | 2D | $11 \times 512^2$ | $\approx 23$ MB |
| $N = 128$ | 3D | $11 \times 128^3$ | $\approx 185$ MB |
| $N = 256$ | 3D | $11 \times 256^3$ | $\approx 1.47$ GB |

### 6.4 GPU-Specific Considerations

1. **Kernel fusion:** The pointwise evaluations $M(\rho)$, $M'(\rho)$, $P(\rho)$, and $F[\rho] = M \cdot \text{Lap} + M' \cdot |\nabla\rho|^2 - P$ should be fused into a single GPU kernel to avoid multiple memory round-trips.

2. **Batched tridiagonal solves (ADI):** For the FD solver in 2D, the $x$-direction implicit sweep consists of $N_y$ independent tridiagonal systems of size $N_x$. Use `cuSPARSE gtsv2StridedBatch` or equivalent batched Thomas solver. In 3D, each sweep direction produces $N_j \times N_k$ independent systems.

3. **FFT plans:** Pre-compute and cache FFT plans (FFTW wisdom / cuFFT plans) at initialization. For the DCT, use `scipy.fft.dctn` / `cupyx.scipy.fft.dctn` with `type=1` (Neumann) or `type=2` (periodic via half-shift). The $d$-dimensional transform is the tensor product of 1D transforms.

4. **Memory coalescing:** Ensure the innermost array axis aligns with the GPU thread block dimension. For 3D arrays in C order `(Nx, Ny, Nz)`, the $z$-axis is contiguous and should be the primary parallelization dimension for stencil kernels.

5. **Precision:** Start with float64 (matching the canonical solver's $\varepsilon \approx 10^{-12}$ bounds enforcement). Float32 may be adequate for visualization-only runs, saving $2\times$ memory and gaining $\sim 2\times$ throughput on consumer GPUs.

---

## 7. Spectral ETD-RK4: 2D/3D Extension Details

### 7.1 Eigenvalue Structure

For the linearization about $\rho = \rho^*$ with Neumann BCs on $[0,L_x] \times [0,L_y] \times [0,L_z]$:

$$
\mu_{\mathbf{k}} = \left(\frac{k_x\pi}{L_x}\right)^2 + \left(\frac{k_y\pi}{L_y}\right)^2 + \left(\frac{k_z\pi}{L_z}\right)^2, \qquad \mathbf{k} = (k_x, k_y, k_z) \in \mathbb{N}_0^d
$$

The linear decay constants are:
$$
c_{\mathbf{k}} = -D\,M^*\,\mu_{\mathbf{k}}
$$

And the modal constants:
$$
\alpha_{\mathbf{k}} = M^*\,\mu_{\mathbf{k}} + P^{*\prime}
$$

All ETD weight functions ($\exp(c_{\mathbf{k}}\,\Delta t)$, $\phi_1$, $\phi_2$, $\phi_3$) are evaluated pointwise on the $d$-dimensional spectral grid. This is a trivial tensor-product extension of the 1D SpectralState.

### 7.2 Multi-Dimensional DCT

The $d$-dimensional DCT-I of $u$ on an $N_1 \times N_2 \times \cdots \times N_d$ grid:
$$
\hat{u}_{\mathbf{k}} = \text{DCT-I}^{(d)}[u] = \text{DCT-I}_{x_1}\!\bigl[\text{DCT-I}_{x_2}\!\bigl[\cdots\text{DCT-I}_{x_d}[u]\cdots\bigr]\bigr]
$$

In NumPy/SciPy: `scipy.fft.dctn(u, type=1, axes=range(d))`.

### 7.3 Pseudospectral Nonlinear Evaluation

At each RK substep:
1. Transform $\hat{u}_{\mathbf{k}} \to u(\mathbf{x})$ on the de-aliased grid (zero-pad to $3/2 \times$ in each axis, then IDCT).
2. Compute $\rho = u + \rho^*$.
3. Evaluate pointwise: $M(\rho)$, $M'(\rho)$, $P(\rho)$.
4. Compute $\nabla^2 u$ and $|\nabla u|^2$ in physical space (spectral derivatives via multiplication by $-\mu_{\mathbf{k}}$ for Laplacian; or finite differences on the de-aliased grid).
5. Form the nonlinear residual $N = M(\rho)\,\nabla^2 u + M'(\rho)\,|\nabla u|^2 - P(\rho) - [\text{linear part}]$.
6. Transform $N(\mathbf{x}) \to \hat{N}_{\mathbf{k}}$ (DCT, then truncate to $N$ modes).

---

## 8. FD ADI Solver: 2D/3D Extension Details

### 8.1 Crank-Nicolson with ADI Splitting (2D)

Full step from $\rho^n$ to $\rho^{n+1}$:

**Half-step 1 (implicit in $x$):**
$$
\Bigl(I - \tfrac{\Delta t}{2}\,D\,\text{diag}(M^n)\,\delta_{xx}\Bigr)\,\rho^{n+1/2}
= \rho^n + \tfrac{\Delta t}{2}\,D\,M^n\,\delta_{yy}\rho^n
+ \Delta t\,\bigl(D\,M'^n\,|\nabla\rho^n|^2 - D\,P^n + H\,v^n\bigr)
$$

**Half-step 2 (implicit in $y$):**
$$
\Bigl(I - \tfrac{\Delta t}{2}\,D\,\text{diag}(M^n)\,\delta_{yy}\Bigr)\,\rho^{n+1}
= \rho^{n+1/2} + \tfrac{\Delta t}{2}\,D\,M^n\,\delta_{xx}\rho^{n+1/2}
- \tfrac{\Delta t}{2}\,D\,M^n\,\delta_{yy}\rho^n
$$

Each half-step requires solving $N_y$ (resp. $N_x$) independent tridiagonal systems — directly extending the 1D `solve_banded` approach.

### 8.2 Douglas-Gunn ADI (3D)

For 3D, the Peaceman-Rachford ADI generalizes to the Douglas-Gunn scheme with three sub-steps (implicit in $x$, then $y$, then $z$), each requiring batched tridiagonal solves. The structure is analogous to 2D with one additional sweep.

---

## 9. Validation Strategy

The 2D/3D solver must reproduce the following known behaviors:

1. **Spatially-homogeneous limit:** If $\rho(\mathbf{x}, 0) = \text{const}$, the PDE reduces to the ODE pair $(d\bar\rho/dt, \dot{v})$. All 2D/3D solvers must reproduce the 1D homogeneous-mode eigenvalues and oscillation frequencies from edsim_parameters.py.

2. **1D embedding:** A 2D simulation with initial condition $\rho(x, y, 0) = \rho_0(x)$ (uniform in $y$) must produce identical results to the 1D solver for all time. Same for 3D with dependence on one axis only.

3. **Energy functional:** The Lyapunov functional $\mathcal{E}[\rho, v] = \int_\Omega \Phi(\rho)\,dx + \frac{\tau\,H}{2}\,v^2$ must be non-increasing (modulo floating-point precision and clamping artifacts). (The kinetic term uses $\tau H/2$, matching `edsim_core.py` `energy()`.)

4. **Spectral vs. FD cross-verification:** For identical parameters and initial conditions, Method A and Method B must agree within their respective truncation error bounds.

5. **Convergence order:** Spatial refinement study confirming $O(h^2)$ for FD and spectral (exponential) convergence for the spectral solver.

---

## 10. Summary of Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Primary solver | Spectral ETD-RK4 | Proven in 1D, no CFL constraint, spectral accuracy, GPU-friendly |
| Secondary solver | FD Crank-Nicolson + ADI | Cross-validation, boundary flexibility, robustness near horizons |
| Implicit splitting | IMEX: diffusion implicit, rest explicit | Removes dominant stiffness at minimal complexity |
| Array convention | C-order, last-axis-fastest | NumPy default, GPU-coalesced for $z$-axis kernels |
| Ghost cell strategy | `np.pad` with mode selection | Matches existing ed_phys_operators.py pattern |
| Boundary condition default | Neumann (DCT-I for spectral) | Consistent with edsim_core.py canonical solver |
| Positivity enforcement | Clamp to $[\varepsilon, \rho_{\max} - \varepsilon]$ | Matches edsim_core.py `enforce_bounds()` |
| Participation integrator | Exact exponential | Matches `advance_v()` in edsim_core.py |
| De-aliasing | 3/2-rule (zero-pad in spectral space) | Matches SpectralState in edsim_core.py |
| Precision | float64 default, float32 optional | Accuracy for bounds enforcement; float32 for fast visualization |

---

*End of Phase 1 Architectural Specification.*
*Phase 2 will implement this architecture as a dimension-generic Python module.*
