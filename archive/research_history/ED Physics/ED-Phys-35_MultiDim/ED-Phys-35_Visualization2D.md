# ED-Phys-35: 2D Visualization Suite

**Module:** `visualization_2d.py`
**Tests:** `test_visualization_2d.py` (21/21 PASS)
**Output:** `test_output_viz/` (7 composite PNG figures)

---

## Style Conventions

Follows the ED-SIM atlas (`generate_all_figures.py`):

| Setting | Value |
|---------|-------|
| DPI | 300 |
| Density colormap | `inferno` |
| Gradient colormap | `viridis` |
| Signed fields | `RdBu_r` (diverging) |
| Horizon | `Reds` |
| Spectra | `plasma` |
| Curvature | `coolwarm` |
| Title font | 13pt bold |
| Label font | 11pt |
| Grid | alpha=0.3, lw=0.5 |

Palette constants in `ED_COLORS`: blue (#2166ac), red (#b2182b), green (#1b7837), purple (#762a83), orange (#e08214).

---

## A. Field Visualizations

### `plot_density_heatmap(rho, params)`
Heatmap of $\rho(x,y)$ using `pcolormesh` with the inferno colormap. Equal aspect ratio, colorbar labelled $\rho$. Accepts `vmin/vmax` for fixed color limits across animation frames.

### `plot_density_contour(rho, params)`
Filled contour plot (default 15 levels) or line contours with inline labels.

### `plot_gradient_quiver(rho, params)`
Quiver plot of $\nabla\rho$ computed via central differences with Neumann BCs. Arrows subsampled by `stride` (default 4). Arrows colored by $|\nabla\rho|$ using viridis.

### `plot_level_sets(rho, params)`
Level-set overlay: semi-transparent density heatmap background with white contour lines and optional gradient arrows (`show_gradient=True`).

### `plot_field_quad(rho, params)` — Composite
Four-panel overview:
- (a) Density heatmap
- (b) Contour plot
- (c) Gradient quiver
- (d) Gradient magnitude $|\nabla\rho|$

---

## B. Spectral Visualizations

### `plot_spectrum_2d(a, Lx, Ly)`
2D modal energy $|a_{k_x,k_y}|^2$ as a heatmap. Default log10 color scale using the plasma colormap. Cropping via `Kx_show/Ky_show`.

### `plot_radial_spectrum(a, Lx, Ly)`
Radially-averaged energy $E(|k|)$ on a semilog axis. Bins modes by wavenumber magnitude.

### `plot_anisotropy_ellipse(spec_anis)`
Visualises the spectral inertia tensor as an ellipse. Semi-axes proportional to eigenvalues of $I_{ij} = \langle k_i k_j \rangle_E$. Annotates the anisotropy index $A_{\text{spec}}$ and eccentricity.

### `plot_spectral_overview(a, Lx, Ly, spec_anis)` — Composite
Three-panel overview:
- (a) 2D spectrum
- (b) Radial spectrum
- (c) Anisotropy ellipse

---

## C. Geometric Visualizations

### `plot_hessian_eigenvalues(rho, params, which='max')`
Maps of Hessian eigenvalues using a diverging colormap centered at zero. Options: `'max'` ($\lambda_1$), `'min'` ($\lambda_2$), `'det'` ($\lambda_1\lambda_2$, distinguishing peaks/valleys from saddles).

### `plot_filamentarity_field(rho, params)`
Filamentarity $F(x,y) = 1 - |\lambda_{\min}|/|\lambda_{\max}|$ on a $[0,1]$ scale using the YlOrRd colormap. $F = 0$ for isotropic curvature, $F = 1$ for filamentary structure.

### `plot_curvature_field(rho, params)`
Level-set curvature $\kappa(x,y)$ using a diverging colormap. Low-gradient regions are masked to suppress noise at critical points. Color limits set at 95th percentile.

### `plot_geometry_2d(rho, params)` — Composite
Four-panel overview:
- (a) $\lambda_{\max}$ (Hessian)
- (b) $\lambda_1\lambda_2$ (peaks vs saddles)
- (c) Filamentarity $F$
- (d) Level-set curvature $\kappa$

---

## D. Horizon Visualizations

### `plot_horizon_proximity(rho, params)`
Horizon proximity field $H_{\text{prox}} = 1 - M(\rho)/M^*$ on a $[0,1]$ scale using the Reds colormap. Annotates max proximity and horizon margin.

### `plot_horizon_mask(rho, params)`
Binary horizon overlay on a density background. Regions where $M(\rho) < \text{threshold} \cdot M^*$ are highlighted in red with a contour boundary. Reports horizon area fraction.

### `plot_horizon_2d(rho, params)` — Composite
Two-panel overview: proximity field + binary mask.

---

## E. Diagnostic Plots

### `plot_time_series(results)`
Four-panel time-series from `run_simulation_2d()` output:
- (a) Energy (total, potential, kinetic) on semilog scale
- (b) Mass conservation
- (c) Participation variable $v(t)$
- (d) Spatial average $\bar{F}[\rho](t)$

### `plot_invariants_2d(inv)` — Dashboard
Six-panel invariant dashboard from `compute_invariants_2d()`:
- (a) 2D modal energy spectrum
- (b) Dissipation ratio bar chart
- (c) Geometric norms $G_\alpha$ vs $\alpha$
- (d) Text summary of all scalar invariants
- (e) Structure functions $S_p(r)$
- (f) Local growth rate statistics

### `plot_snapshot_evolution(rho_snapshots, times, params)`
Multi-panel density evolution at selected times with shared colorbar. Automatically selects `n_show` evenly-spaced frames.

---

## API Design

All single-panel functions follow the pattern:

```python
def plot_xxx(data, params, ax=None, title=None, **kwargs):
    """If ax is None, creates a new figure. Returns the ax."""
```

This enables both standalone use and composition into multi-panel figures. Composite functions return the `fig` and accept `savepath` for direct export.

---

## Generated Outputs

| File | Size | Content |
|------|------|---------|
| `field_quad.png` | 173 KB | 4-panel field overview |
| `geometry_quad.png` | 87 KB | 4-panel geometric overview |
| `horizon_overview.png` | 43 KB | 2-panel horizon overview |
| `spectral_overview.png` | 73 KB | 3-panel spectral overview |
| `time_series.png` | 164 KB | 4-panel diagnostic time series |
| `snapshot_evolution.png` | 72 KB | 6-frame density evolution |
| `invariant_dashboard.png` | 168 KB | 6-panel invariant dashboard |

All at 150 DPI (test mode). Production mode uses 300 DPI.

---

## Validation

21 rendering tests, **21 PASS, 0 FAIL**:

- 6 field visualizations (heatmap, contour, quiver, level-set, level-set+gradient, quad)
- 4 spectral visualizations (2D spectrum, radial, ellipse, overview)
- 5 geometric visualizations (Hessian max, det, filamentarity, curvature, quad)
- 3 horizon visualizations (proximity, mask, overview)
- 3 diagnostic visualizations (time series, snapshots, invariant dashboard)
