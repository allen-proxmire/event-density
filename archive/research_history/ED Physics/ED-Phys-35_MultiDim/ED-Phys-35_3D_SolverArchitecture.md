# ED-Phys-35: 3D Solver Architecture

**Module:** `edsim_solver_3d.py`
**Tests:** `test_solver_3d.py` (14/14 PASS)

---

## 1. The 3D PDE

The canonical ED system on $\Omega = [0,L_x] \times [0,L_y] \times [0,L_z]$:

$$\partial_t \rho = D\,F[\rho] + H\,v, \qquad \dot{v} = \frac{1}{\tau}(\bar{F} - \zeta\,v)$$

where $D + H = 1$ and

$$F[\rho] = \nabla\!\cdot\![M(\rho)\,\nabla\rho] - P(\rho)
= M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho)$$

### 3D Operator Expansions

$$\nabla^2\rho = \partial_{xx}\rho + \partial_{yy}\rho + \partial_{zz}\rho$$

$$|\nabla\rho|^2 = (\partial_x\rho)^2 + (\partial_y\rho)^2 + (\partial_z\rho)^2$$

### Constitutive Functions (unchanged from 1D/2D)

| Function | Expression |
|----------|-----------|
| Mobility | $M(\rho) = M_0\,(\rho_{\max} - \rho)^\beta$ |
| Mobility deriv | $M'(\rho) = -\beta\,M_0\,(\rho_{\max} - \rho)^{\beta-1}$ |
| Penalty | $P(\rho) = P_0\,(\rho - \rho^*)$ |

---

## 2. Spatial Operators

### 2.1 Finite Difference (7-point stencil)

The Laplacian at grid point $(i,j,k)$:

$$\nabla^2\rho_{i,j,k} = \frac{\rho_{i+1,j,k} + \rho_{i-1,j,k} - 2\rho_{i,j,k}}{h_x^2}
+ \frac{\rho_{i,j+1,k} + \rho_{i,j-1,k} - 2\rho_{i,j,k}}{h_y^2}
+ \frac{\rho_{i,j,k+1} + \rho_{i,j,k-1} - 2\rho_{i,j,k}}{h_z^2}$$

Boundary conditions via `np.pad(rho, 1, mode='reflect')` (Neumann) or `mode='wrap'` (periodic). The padded array has shape $(N_x+2, N_y+2, N_z+2)$; the interior slice `p[1:-1, 1:-1, 1:-1]` aliases the original grid.

The gradient squared uses central differences with the same padding:

$$|\nabla\rho|^2_{i,j,k} = \left(\frac{\rho_{i+1}-\rho_{i-1}}{2h_x}\right)^2 + \left(\frac{\rho_{j+1}-\rho_{j-1}}{2h_y}\right)^2 + \left(\frac{\rho_{k+1}-\rho_{k-1}}{2h_z}\right)^2$$

### 2.2 Spectral (3D DCT-I)

Neumann eigenvalues:

$$\mu_{k_x,k_y,k_z} = \left(\frac{k_x\pi}{L_x}\right)^2 + \left(\frac{k_y\pi}{L_y}\right)^2 + \left(\frac{k_z\pi}{L_z}\right)^2$$

The Laplacian in spectral space: $\widehat{\nabla^2 u} = -\mu\,\hat{u}$ (pointwise multiply).

The 3D DCT-I uses `scipy.fft.dctn(u, type=1)` with the corrected normalisation from Phase 2 (exact roundtrip verified to $3.5 \times 10^{-17}$).

De-aliasing: 3/2-rule per axis. A $K \times K \times K$ spectral grid maps to a $\lfloor 3K/2 \rfloor^3$ physical grid.

---

## 3. Time Integrators

### 3.1 ETD-RK4 (Primary)

Cox-Matthews scheme. Identical to 2D except all arrays are 3D:

$$\hat{u}^{n+1} = e^{c\Delta t}\,\hat{u}^n + \Delta t\bigl(\phi_1\,a + 2\phi_2(b+c) + \phi_3\,d\bigr)$$

where $c_{k_x,k_y,k_z} = -D\,M^*\,\mu_{k_x,k_y,k_z}$ and $\phi_1, \phi_2, \phi_3$ are the standard ETD weight functions precomputed at initialisation.

The nonlinear residual $\hat{N}$ is computed pseudospectrally: transform to physical, evaluate $M'|\nabla\rho|^2$ and $(P - P^{*\prime}u)$ via FD on the de-aliased grid, transform back.

### 3.2 Crank-Nicolson with Douglas-Gunn ADI (Secondary)

Three sub-steps per time step, each treating one direction implicitly:

**Step 1 (x-implicit):**
$$(I - c_x\,\text{diag}(M^n)\,L_{xx})\,\rho^* = \rho^n + \tfrac{dt\,D}{2}(M^n L_{yy}\rho^n + M^n L_{zz}\rho^n) + dt\,S^n$$

**Step 2 (y-implicit):**
$$(I - c_y\,\text{diag}(M^n)\,L_{yy})\,\rho^{**} = \rho^* - \tfrac{dt\,D}{2}\,M^n L_{yy}\rho^n$$

**Step 3 (z-implicit):**
$$(I - c_z\,\text{diag}(M^n)\,L_{zz})\,\rho^{n+1} = \rho^{**} - \tfrac{dt\,D}{2}\,M^n L_{zz}\rho^n$$

where $c_\alpha = dt\,D/(2h_\alpha^2)$ and $S^n = D\,M'\,|\nabla\rho|^2 - D\,P + H\,v$.

Each sub-step is a batch of independent tridiagonal solves: Step 1 has $N_y \times N_z$ systems of size $N_x$, Step 2 has $N_x \times N_z$ systems of size $N_y$, Step 3 has $N_x \times N_y$ systems of size $N_z$.

---

## 4. Design Choices

### 4.1 Memory Management

| Grid | Points | Per-array (f64) | 10 arrays |
|------|--------|-----------------|-----------|
| $32^3$ | 32,768 | 0.3 MB | 3 MB |
| $64^3$ | 262,144 | 2.1 MB | 21 MB |
| $128^3$ | 2,097,152 | 16.8 MB | 168 MB |

The spectral solver with 3/2-rule de-aliasing multiplies the physical-grid memory by $(3/2)^3 \approx 3.4\times$. For $N=64$: total working memory ~70 MB; for $N=128$: ~570 MB.

**Memory optimisations:**
- `store_snapshots=False` by default in `run_simulation_3d()` — only the final state is stored.
- FD operators use a single padded array (created once per operator call, not per-step).
- Spectral weights ($\exp, \phi_1, \phi_2, \phi_3$) precomputed once at initialisation.

### 4.2 API Parity with 2D

| 2D | 3D | Change |
|----|----|--------|
| `EDParameters2D` | `EDParameters3D` | +Nz, Lz, hz |
| `laplacian_fd_2d()` | `laplacian_fd_3d()` | 5-pt -> 7-pt stencil |
| `grad_squared_fd_2d()` | `grad_squared_fd_3d()` | +z component |
| `SpectralState2D` | `SpectralState3D` | 3D tensor-product eigenvalues |
| `step_cn_fd_2d()` | `step_cn_fd_3d()` | 2 ADI sweeps -> 3 (Douglas-Gunn) |
| `step_2d()` | `step_3d()` | dispatcher |
| `run_simulation_2d()` | `run_simulation_3d()` | +store_snapshots flag |

### 4.3 CFL Bounds (explicit, for reference)

$$\Delta t < \frac{h^2}{6\,M_0} \qquad \text{(3D explicit CFL)}$$

The ETD-RK4 and CN methods are unconditionally stable for the diffusion term, so this bound does not apply. The explicit nonlinear terms have a much weaker restriction that is satisfied by typical $\Delta t$ values.

---

## 5. Validation Summary

14 tests, **14 PASS, 0 FAIL**:

| Test | Result | Detail |
|------|--------|--------|
| DCT roundtrip | PASS | err = $3.5 \times 10^{-17}$ |
| Constant roundtrip | PASS | err = $3.5 \times 10^{-17}$ |
| Lap(const) = 0 | PASS | exact |
| |grad(const)|^2 = 0 | PASS | exact |
| FD Laplacian O(h^2) | PASS | err = $2.2 \times 10^{-2}$, h^2 = $1.0 \times 10^{-3}$ |
| Uniform stays uniform (ETD) | PASS | dev = 0 |
| Uniform stays uniform (CN) | PASS | dev = $3.1 \times 10^{-15}$ |
| z-invariant preserves symmetry | PASS | z-std = $1.1 \times 10^{-15}$ |
| Energy monotone (ETD) | PASS | 0/10 increases |
| Energy monotone (CN) | PASS | 0/10 increases |
| ETD vs CN agreement | PASS | rel diff = 2.0% |
| Memory estimate | PASS | $64^3$ ~ 21 MB |
| run_simulation_3d | PASS | completes in 0.3s |
| Energy decays | PASS | E_ratio = 0.77 |
