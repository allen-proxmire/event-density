# ED-Phys-35: 3D Visualization Suite

**Module:** `visualization_3d.py`
**Tests:** `test_visualization_3d.py` (18/18 PASS)
**Output:** `test_output_viz3d/` (24 PNG files)

---

## Design Principles

3D volume data is rendered via **2D slices and projections** (pure Matplotlib, no VTK/Mayavi required). This ensures portability across all environments and compatibility with the ED-SIM atlas pipeline.

Three primary rendering strategies:
1. **Orthogonal slice triplets** — xy, xz, yz planes at configurable positions
2. **Maximum-intensity projections** (MIP) — project max value along each axis
3. **Multi-z contour grids** — isosurface-like views across z-planes

Style matches `visualization_2d.py` and the ED-SIM atlas conventions.

---

## A. Field Visualizations (5 functions)

### `plot_slice_triplet(field, params)` — Core engine
Three-panel orthogonal slices with shared colorbar. `slice_fracs=(fz, fy, fx)` controls the slice positions (default: mid-planes at 0.5). Used by all other slice functions.

### `plot_density_slices(rho, params)`
Density $\rho$ on xy, xz, yz mid-planes. Inferno colormap.

### `plot_gradient_magnitude_slices(rho, params)`
$|\nabla\rho|$ computed via 3-component central differences. Viridis colormap.

### `plot_max_intensity_projection(field, params)`
Three-panel MIP: projects `max(field, axis=k)` for $k = z, y, x$. Useful for identifying high-density peaks and filaments that may not intersect the mid-plane.

### `plot_isosurface_contours(rho, params)`
2x3 grid of filled contour plots on 6 evenly-spaced z-planes. White contour overlays for isovalue visibility. Approximates isosurface rendering.

### `plot_field_overview_3d(rho, params)` — Composite
Produces 3 figures: density slices, gradient slices, and MIP.

---

## B. Spectral Visualizations (4 functions)

### `plot_spectrum_3d(a, Lx, Ly, Lz)`
2D slice through the 3D modal energy $|a_\mathbf{k}|^2$. Default: $k_z = 0$ plane (most energetic for Neumann BCs). Log10 color scale, plasma colormap.

### `plot_radial_spectrum_3d(a, Lx, Ly, Lz)`
Radially-binned energy $E(|\mathbf{k}|)$ on semilog axis. Bins modes by 3D wavenumber magnitude.

### `plot_anisotropy_ellipsoid(spec_anis)`
Three-panel ellipse projections of the spectral inertia tensor onto the $(k_x,k_y)$, $(k_x,k_z)$, and $(k_y,k_z)$ planes. Annotates isotropy, planarity, and linearity indices.

### `plot_spectral_overview_3d(a, Lx, Ly, Lz, spec_anis)` — Composite
Two figures: spectrum slice + radial plot, and anisotropy ellipsoid.

---

## C. Geometric Visualizations (4 functions)

### `plot_morphology_slices(rho, params)`
Three-panel mid-z slices of filamentarity $F$, sheetness $S$, and blobness $B$, each on a $[0,1]$ scale with distinct colormaps (YlOrRd, YlGnBu, Purples).

### `plot_curvature_slices(rho, params)`
Two-panel mid-z slices of mean curvature $H$ and Gaussian curvature $K$ of iso-surfaces. Diverging colormap centered at zero, low-gradient regions masked.

### `plot_hessian_eigenvalue_slices(rho, params)`
Three-panel mid-z slices of the Hessian eigenvalues $\lambda_1 \geq \lambda_2 \geq \lambda_3$. RdBu diverging colormap centered at zero.

### `plot_geometry_3d(rho, params)` — Composite
Produces 3 figures: morphology, curvature, and Hessian eigenvalues.

---

## D. Horizon Visualizations (3 functions)

### `plot_horizon_slices(rho, params)`
Orthogonal slices of the horizon proximity field $H_\text{prox} = 1 - M(\rho)/M^*$ on a $[0,1]$ Reds scale. Annotates max proximity, horizon volume fraction, and connected component count.

### `plot_horizon_mask_slices(rho, params)`
Binary horizon overlay on mid-z density slice. Regions where $M < 10\%\,M^*$ are filled in red with a contour boundary. Reports horizon volume fraction.

### `plot_horizon_3d(rho, params)` — Composite
Two figures: proximity slices + mask.

---

## E. Diagnostics (2 functions)

### `plot_time_series_3d(results)`
Four-panel time series from `run_simulation_3d()`: (a) Energy (total/potential/kinetic, semilog), (b) Mass, (c) Participation $v$, (d) $\bar{F}[\rho]$.

### `plot_invariants_3d(inv, params)` — Dashboard
Six-panel invariant dashboard from `compute_invariants_3d()`:
- (a) Spectral energy ($k_z = 0$ slice)
- (b) Dissipation ratio bar chart
- (c) Geometric norms $G_\alpha$ vs $\alpha$
- (d) Text summary of all scalar invariants
- (e) Structure functions $S_p(r)$
- (f) Morphology pie chart (filament/sheet/blob fractions)

---

## API Summary

| Function | Panels | Input | Output |
|----------|--------|-------|--------|
| `plot_density_slices` | 1x3 | rho, params | fig |
| `plot_gradient_magnitude_slices` | 1x3 | rho, params | fig |
| `plot_max_intensity_projection` | 1x3 | field, params | fig |
| `plot_isosurface_contours` | 2x3 | rho, params | fig |
| `plot_field_overview_3d` | 3 figs | rho, params | [fig] |
| `plot_spectrum_3d` | 1 | a, L's | ax |
| `plot_radial_spectrum_3d` | 1 | a, L's | ax |
| `plot_anisotropy_ellipsoid` | 1x3 | spec_anis | fig |
| `plot_spectral_overview_3d` | 2 figs | a, L's, spec_anis | [fig] |
| `plot_morphology_slices` | 1x3 | rho, params | fig |
| `plot_curvature_slices` | 1x2 | rho, params | fig |
| `plot_hessian_eigenvalue_slices` | 1x3 | rho, params | fig |
| `plot_geometry_3d` | 3 figs | rho, params | [fig] |
| `plot_horizon_slices` | 1x3 | rho, params | fig |
| `plot_horizon_mask_slices` | 1 | rho, params | fig |
| `plot_horizon_3d` | 2 figs | rho, params | [fig] |
| `plot_time_series_3d` | 2x2 | results | fig |
| `plot_invariants_3d` | 2x3 | inv, params | fig |

All single-panel functions accept `ax=None` (creates figure) or an existing axes for composition. Composite functions return the `fig` (or list of figs) and accept `savepath`.

---

## Validation

18 rendering tests, **18 PASS, 0 FAIL**, producing 24 PNG files (1.3 MB total at 150 DPI test mode).
