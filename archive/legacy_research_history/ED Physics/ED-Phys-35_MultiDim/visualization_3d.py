"""
visualization_3d.py
===================
3D visualization and diagnostics suite for the canonical Event Density PDE.

Provides publication-ready visualizations of:
  A. Fields    — orthogonal slices, isosurfaces, max-intensity projections
  B. Spectra   — 3D spectrum slices, radial spectrum, anisotropy ellipsoid
  C. Geometry  — morphology maps, curvature slices, Hessian eigenvalues
  D. Horizons  — proximity slices, horizon mask overlays, connected components
  E. Diagnostics — time-series, invariant dashboards, snapshot sequences

Style conventions match visualization_2d.py and the ED-SIM atlas.
All 3D volume data is rendered via 2D slices (pure Matplotlib, no VTK required).
"""

import numpy as np
from typing import Dict, Optional, Tuple, List

_MPL_IMPORTED = False

def _ensure_mpl():
    global _MPL_IMPORTED
    if not _MPL_IMPORTED:
        import matplotlib
        matplotlib.use("Agg")
        _MPL_IMPORTED = True

def _import_plt():
    _ensure_mpl()
    import matplotlib.pyplot as plt
    return plt

def _import_mpl_extras():
    _ensure_mpl()
    from matplotlib.colors import TwoSlopeNorm
    from matplotlib.patches import FancyArrowPatch
    return TwoSlopeNorm, FancyArrowPatch


# =====================================================================
#  STYLE (shared with visualization_2d.py)
# =====================================================================

STYLE = {
    "dpi": 300,
    "figsize_single": (7, 6),
    "figsize_wide": (16, 5),
    "figsize_tri": (16, 5),
    "figsize_quad": (13, 11),
    "figsize_dashboard": (16, 14),
    "font_title": 13,
    "font_label": 11,
    "font_tick": 9,
    "font_legend": 9,
    "font_annotation": 8,
    "grid_alpha": 0.3,
    "grid_lw": 0.5,
    "line_lw": 1.5,
    "cmap_density": "inferno",
    "cmap_gradient": "viridis",
    "cmap_signed": "RdBu_r",
    "cmap_horizon": "Reds",
    "cmap_spectral": "plasma",
    "cmap_curvature": "coolwarm",
    "cmap_morphology": "Set2",
}

ED_COLORS = {
    "blue": "#2166ac", "red": "#b2182b", "green": "#1b7837",
    "purple": "#762a83", "orange": "#e08214", "gray": "#999999",
}


def _setup_axes(ax, xlabel, ylabel, title):
    ax.set_xlabel(xlabel, fontsize=STYLE["font_label"])
    ax.set_ylabel(ylabel, fontsize=STYLE["font_label"])
    ax.set_title(title, fontsize=STYLE["font_title"], fontweight="bold")
    ax.tick_params(labelsize=STYLE["font_tick"])

def _add_grid(ax):
    ax.grid(True, alpha=STYLE["grid_alpha"], linewidth=STYLE["grid_lw"])


def _slice_index(N, frac):
    """Convert a fraction [0,1] to an integer slice index."""
    return max(0, min(N - 1, int(round(frac * (N - 1)))))


# =====================================================================
#  A. FIELD VISUALIZATIONS
# =====================================================================

def plot_slice_triplet(field, params, title=None, cmap=None, label=None,
                       vmin=None, vmax=None, savepath=None,
                       slice_fracs=(0.5, 0.5, 0.5)):
    """
    Three orthogonal slices through a 3D scalar field.

    Produces a 1x3 figure: (a) xy-slice at z=frac, (b) xz at y=frac, (c) yz at x=frac.

    Parameters
    ----------
    field : (Nx, Ny, Nz) array
    params : EDParameters3D
    slice_fracs : (frac_z, frac_y, frac_x) for each slice (0=min, 1=max)
    """
    plt = _import_plt()
    fig, axes = plt.subplots(1, 3, figsize=STYLE["figsize_tri"])
    if cmap is None:
        cmap = STYLE["cmap_density"]
    if label is None:
        label = r"$\rho$"
    if title is None:
        title = "Orthogonal slices"

    Nx, Ny, Nz = field.shape
    fz, fy, fx = slice_fracs
    iz = _slice_index(Nz, fz)
    iy = _slice_index(Ny, fy)
    ix = _slice_index(Nx, fx)

    x = np.linspace(0, params.Lx, Nx)
    y = np.linspace(0, params.Ly, Ny)
    z = np.linspace(0, params.Lz, Nz)

    kw = dict(shading='auto', cmap=cmap, vmin=vmin, vmax=vmax)

    # (a) xy-slice at z=iz
    im0 = axes[0].pcolormesh(x, y, field[:, :, iz].T, **kw)
    axes[0].set_aspect('equal')
    _setup_axes(axes[0], "$x$", "$y$", f"(a) $z={z[iz]:.2f}$")

    # (b) xz-slice at y=iy
    im1 = axes[1].pcolormesh(x, z, field[:, iy, :].T, **kw)
    axes[1].set_aspect('equal')
    _setup_axes(axes[1], "$x$", "$z$", f"(b) $y={y[iy]:.2f}$")

    # (c) yz-slice at x=ix
    im2 = axes[2].pcolormesh(y, z, field[ix, :, :].T, **kw)
    axes[2].set_aspect('equal')
    _setup_axes(axes[2], "$y$", "$z$", f"(c) $x={x[ix]:.2f}$")

    fig.subplots_adjust(right=0.92)
    cbar_ax = fig.add_axes([0.94, 0.15, 0.015, 0.7])
    fig.colorbar(im0, cax=cbar_ax, label=label)

    fig.suptitle(title, fontsize=STYLE["font_title"] + 2, fontweight="bold", y=1.02)
    fig.tight_layout(rect=[0, 0, 0.92, 0.97])

    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


def plot_density_slices(rho, params, title=None, savepath=None, **kwargs):
    """Convenience: orthogonal slices of the density field rho(x,y,z)."""
    if title is None:
        title = r"Density $\rho$ — orthogonal slices"
    return plot_slice_triplet(rho, params, title=title, label=r"$\rho$",
                              cmap=STYLE["cmap_density"], savepath=savepath,
                              **kwargs)


def plot_gradient_magnitude_slices(rho, params, title=None, savepath=None, **kwargs):
    """Orthogonal slices of |nabla rho|."""
    from invariants_3d import _grad_components_3d
    gx, gy, gz = _grad_components_3d(rho, params.hx, params.hy, params.hz)
    grad_mag = np.sqrt(gx**2 + gy**2 + gz**2)
    if title is None:
        title = r"$|\nabla\rho|$ — orthogonal slices"
    return plot_slice_triplet(grad_mag, params, title=title,
                              label=r"$|\nabla\rho|$",
                              cmap=STYLE["cmap_gradient"], savepath=savepath,
                              **kwargs)


def plot_max_intensity_projection(field, params, title=None, cmap=None,
                                   label=None, savepath=None):
    """
    Maximum-intensity projections along each axis.

    A lightweight 3D-to-2D rendering: project the maximum value along
    each axis onto the perpendicular plane.
    """
    plt = _import_plt()
    fig, axes = plt.subplots(1, 3, figsize=STYLE["figsize_tri"])
    if cmap is None:
        cmap = STYLE["cmap_density"]
    if label is None:
        label = "max"
    if title is None:
        title = "Max-intensity projections"

    x = np.linspace(0, params.Lx, params.Nx)
    y = np.linspace(0, params.Ly, params.Ny)
    z = np.linspace(0, params.Lz, params.Nz)

    projs = [
        (np.max(field, axis=2), x, y, "$x$", "$y$", "(a) proj along $z$"),
        (np.max(field, axis=1), x, z, "$x$", "$z$", "(b) proj along $y$"),
        (np.max(field, axis=0), y, z, "$y$", "$z$", "(c) proj along $x$"),
    ]

    vmin = field.min(); vmax = field.max()
    for ax, (proj, u, v, xl, yl, t) in zip(axes, projs):
        im = ax.pcolormesh(u, v, proj.T, shading='auto', cmap=cmap,
                           vmin=vmin, vmax=vmax)
        ax.set_aspect('equal')
        _setup_axes(ax, xl, yl, t)

    fig.subplots_adjust(right=0.92)
    cbar_ax = fig.add_axes([0.94, 0.15, 0.015, 0.7])
    fig.colorbar(im, cax=cbar_ax, label=label)
    fig.suptitle(title, fontsize=STYLE["font_title"] + 2, fontweight="bold", y=1.02)
    fig.tight_layout(rect=[0, 0, 0.92, 0.97])

    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


def plot_isosurface_contours(rho, params, levels=None, n_levels=5,
                              title=None, savepath=None):
    """
    Isosurface visualisation via contour plots on multiple z-slices.

    Shows the contour lines of rho on 6 evenly-spaced z-planes,
    arranged in a 2x3 grid.
    """
    plt = _import_plt()
    if title is None:
        title = r"Isosurface contours of $\rho$"
    if levels is None:
        levels = n_levels

    Nx, Ny, Nz = rho.shape
    x = np.linspace(0, params.Lx, Nx)
    y = np.linspace(0, params.Ly, Ny)
    z = np.linspace(0, params.Lz, Nz)
    X2, Y2 = np.meshgrid(x, y, indexing='ij')

    n_slices = min(6, Nz)
    z_indices = np.linspace(0, Nz - 1, n_slices, dtype=int)
    nrows = 2; ncols = 3
    fig, axes = plt.subplots(nrows, ncols, figsize=(14, 9))
    axes = axes.ravel()

    for i, iz in enumerate(z_indices):
        if i < len(axes):
            cs = axes[i].contourf(X2, Y2, rho[:, :, iz], levels=levels,
                                  cmap=STYLE["cmap_density"])
            axes[i].contour(X2, Y2, rho[:, :, iz], levels=levels,
                           colors='white', linewidths=0.3, alpha=0.5)
            axes[i].set_aspect('equal')
            _setup_axes(axes[i], "$x$", "$y$", f"$z={z[iz]:.2f}$")

    for i in range(len(z_indices), nrows * ncols):
        axes[i].axis('off')

    fig.suptitle(title, fontsize=STYLE["font_title"] + 2, fontweight="bold")
    fig.tight_layout()
    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


def plot_field_overview_3d(rho, params, title=None, savepath=None):
    """
    Four-panel 3D field overview: density slices, gradient slices,
    max-intensity projection, and isosurface contours.

    Returns list of figures.
    """
    figs = []
    t = title or ""
    figs.append(plot_density_slices(rho, params,
        title=f"{t} Density slices" if t else None,
        savepath=savepath.replace('.png', '_slices.png') if savepath else None))
    figs.append(plot_gradient_magnitude_slices(rho, params,
        title=f"{t} Gradient slices" if t else None,
        savepath=savepath.replace('.png', '_grad.png') if savepath else None))
    figs.append(plot_max_intensity_projection(rho, params,
        title=f"{t} Max projection" if t else None,
        savepath=savepath.replace('.png', '_mip.png') if savepath else None))
    return figs


# =====================================================================
#  B. SPECTRAL VISUALIZATIONS
# =====================================================================

def plot_spectrum_3d(a, Lx, Ly, Lz, ax=None, title=None, log_scale=True,
                     slice_axis=2, slice_idx=0):
    """
    2D slice through the 3D modal energy spectrum.

    Default: kz=0 plane (the most energetic modes for Neumann BCs).
    """
    plt = _import_plt()
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=STYLE["figsize_single"])
    if title is None:
        ax_names = ['x', 'y', 'z']
        title = f"Spectral energy ($k_{{{ax_names[slice_axis]}}}$={slice_idx})"

    E = a ** 2
    if slice_axis == 0:
        E_slice = E[slice_idx, :, :]
        xl, yl = r"$k_y$", r"$k_z$"
    elif slice_axis == 1:
        E_slice = E[:, slice_idx, :]
        xl, yl = r"$k_x$", r"$k_z$"
    else:
        E_slice = E[:, :, slice_idx]
        xl, yl = r"$k_x$", r"$k_y$"

    if log_scale:
        E_plot = np.log10(np.maximum(E_slice, 1e-30))
        cb_label = r"$\log_{10}|a|^2$"
    else:
        E_plot = E_slice
        cb_label = r"$|a|^2$"

    im = ax.imshow(E_plot.T, origin='lower', aspect='auto',
                   cmap=STYLE["cmap_spectral"])
    plt.colorbar(im, ax=ax, label=cb_label, shrink=0.8)
    _setup_axes(ax, xl, yl, title)
    return ax


def plot_radial_spectrum_3d(a, Lx, Ly, Lz, ax=None, title=None, n_bins=20):
    """Radially-averaged energy spectrum E(|k|) in 3D."""
    plt = _import_plt()
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=STYLE["figsize_single"])
    if title is None:
        title = "Radial energy spectrum (3D)"

    E = a ** 2
    Kx, Ky, Kz = a.shape
    kx = np.arange(Kx) * np.pi / Lx
    ky = np.arange(Ky) * np.pi / Ly
    kz = np.arange(Kz) * np.pi / Lz
    k_mag = np.sqrt(kx[:, None, None]**2 + ky[None, :, None]**2
                    + kz[None, None, :]**2).ravel()
    E_flat = E.ravel()

    mask = k_mag > 0
    k_pos = k_mag[mask]; E_pos = E_flat[mask]
    if len(k_pos) < 2:
        return ax

    edges = np.linspace(k_pos.min(), k_pos.max(), n_bins + 1)
    k_bins = 0.5 * (edges[:-1] + edges[1:])
    E_binned = np.array([np.sum(E_pos[(k_pos >= edges[b]) & (k_pos < edges[b+1])])
                         for b in range(n_bins)])

    m = E_binned > 0
    if np.any(m):
        ax.semilogy(k_bins[m], E_binned[m], 'o-', color=ED_COLORS["blue"],
                    lw=STYLE["line_lw"], ms=4)
    _setup_axes(ax, r"$|\mathbf{k}|$", r"$E(|\mathbf{k}|)$", title)
    _add_grid(ax)
    return ax


def plot_anisotropy_ellipsoid(spec_anis, ax=None, title=None):
    """
    Visualise 3D spectral anisotropy as three orthogonal ellipse projections.

    The inertia tensor eigenvalues define an ellipsoid; we plot its projections
    onto the (kx,ky), (kx,kz), and (ky,kz) planes.
    """
    plt = _import_plt()
    from matplotlib.patches import Ellipse
    if title is None:
        title = "Spectral anisotropy ellipsoid"

    eigvals = spec_anis['eigenvalues']
    lam = np.maximum(eigvals, 1e-30)
    radii = np.sqrt(lam)
    scale = 1.0 / max(radii.max(), 1e-10)

    fig, axes = plt.subplots(1, 3, figsize=STYLE["figsize_tri"])
    plane_labels = [("$k_x$", "$k_y$", 0, 1),
                    ("$k_x$", "$k_z$", 0, 2),
                    ("$k_y$", "$k_z$", 1, 2)]
    panel_titles = ["(a) $k_x$-$k_y$", "(b) $k_x$-$k_z$", "(c) $k_y$-$k_z$"]

    for ax_i, (xl, yl, i, j) in zip(axes, plane_labels):
        w = 2 * radii[i] * scale
        h = 2 * radii[j] * scale
        ell = Ellipse((0, 0), w, h, facecolor=ED_COLORS["blue"],
                      alpha=0.3, edgecolor=ED_COLORS["blue"], linewidth=2)
        ax_i.add_patch(ell)
        lim = max(w, h) * 0.7
        ax_i.set_xlim(-lim, lim); ax_i.set_ylim(-lim, lim)
        ax_i.set_aspect('equal')
        ax_i.axhline(0, color='gray', lw=0.5, ls='--')
        ax_i.axvline(0, color='gray', lw=0.5, ls='--')

    for ax_i, (xl, yl, _, _), pt in zip(axes, plane_labels, panel_titles):
        _setup_axes(ax_i, xl, yl, pt)

    iso = spec_anis.get('isotropy', 0)
    pla = spec_anis.get('planarity', 0)
    lin = spec_anis.get('linearity', 0)
    axes[0].text(0.02, 0.98, f"iso={iso:.3f}\npla={pla:.3f}\nlin={lin:.3f}",
                 transform=axes[0].transAxes, fontsize=STYLE["font_annotation"],
                 va='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    fig.suptitle(title, fontsize=STYLE["font_title"] + 2, fontweight="bold", y=1.02)
    fig.tight_layout()
    return fig


def plot_spectral_overview_3d(a, Lx, Ly, Lz, spec_anis=None, savepath=None):
    """Three-panel spectral overview: kz=0 slice, radial spectrum, anisotropy."""
    plt = _import_plt()
    figs = []

    fig1, axes1 = plt.subplots(1, 2, figsize=(12, 5))
    plot_spectrum_3d(a, Lx, Ly, Lz, ax=axes1[0], title="(a) Spectrum ($k_z$=0)")
    plot_radial_spectrum_3d(a, Lx, Ly, Lz, ax=axes1[1], title="(b) Radial spectrum")
    fig1.tight_layout()
    figs.append(fig1)

    if spec_anis is not None:
        fig2 = plot_anisotropy_ellipsoid(spec_anis, title="Anisotropy ellipsoid")
        figs.append(fig2)

    if savepath:
        figs[0].savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
        if len(figs) > 1:
            figs[1].savefig(savepath.replace('.png', '_ellipsoid.png'),
                           dpi=STYLE["dpi"], bbox_inches="tight")
    return figs


# =====================================================================
#  C. GEOMETRIC VISUALIZATIONS
# =====================================================================

def plot_morphology_slices(rho, params, title=None, savepath=None):
    """
    Morphology classification slices: filamentarity, sheetness, blobness
    on the mid-z plane.
    """
    plt = _import_plt()
    from invariants_3d import hessian_eigenvalues_3d

    lam1, lam2, lam3 = hessian_eigenvalues_3d(rho, params.hx, params.hy, params.hz)
    a1 = np.abs(lam1); a2 = np.abs(lam2); a3 = np.abs(lam3)
    stk = np.sort(np.stack([a1, a2, a3], axis=-1), axis=-1)
    a3s = stk[..., 0]; a2s = stk[..., 1]; a1s = stk[..., 2]
    a1s_safe = np.maximum(a1s, 1e-15)
    F = np.clip((a2s - a3s) / a1s_safe, 0, 1)
    S = np.clip((a1s - a2s) / a1s_safe, 0, 1)
    B = np.clip(a3s / a1s_safe, 0, 1)

    iz = rho.shape[2] // 2
    x = np.linspace(0, params.Lx, params.Nx)
    y = np.linspace(0, params.Ly, params.Ny)

    fig, axes = plt.subplots(1, 3, figsize=STYLE["figsize_tri"])
    for ax, field, lbl, cm in [
        (axes[0], F[:, :, iz], "Filamentarity $F$", "YlOrRd"),
        (axes[1], S[:, :, iz], "Sheetness $S$", "YlGnBu"),
        (axes[2], B[:, :, iz], "Blobness $B$", "Purples"),
    ]:
        im = ax.pcolormesh(x, y, field.T, shading='auto', cmap=cm, vmin=0, vmax=1)
        ax.set_aspect('equal')
        plt.colorbar(im, ax=ax, shrink=0.7)
        _setup_axes(ax, "$x$", "$y$", lbl)

    if title is None:
        title = "Morphology (mid-$z$ slice)"
    fig.suptitle(title, fontsize=STYLE["font_title"] + 2, fontweight="bold", y=1.02)
    fig.tight_layout()
    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


def plot_curvature_slices(rho, params, title=None, savepath=None):
    """Mean curvature H and Gaussian curvature K on the mid-z plane."""
    plt = _import_plt()
    TwoSlopeNorm, _ = _import_mpl_extras()
    from invariants_3d import _grad_components_3d, _second_derivs_3d

    gx, gy, gz = _grad_components_3d(rho, params.hx, params.hy, params.hz)
    grad_mag = np.sqrt(gx**2 + gy**2 + gz**2)
    rxx, ryy, rzz, rxy, rxz, ryz = _second_derivs_3d(rho, params.hx, params.hy, params.hz)

    g2 = grad_mag**2 + 1e-30
    g3 = g2 * np.sqrt(g2)
    H_field = ((ryy+rzz)*gx**2 + (rxx+rzz)*gy**2 + (rxx+ryy)*gz**2
               - 2*(rxy*gx*gy + rxz*gx*gz + ryz*gy*gz)) / (2.0 * g3)

    g4 = g2**2
    K_field = (rxx*(ryy*rzz - ryz**2)
             - rxy*(rxy*rzz - ryz*rxz)
             + rxz*(rxy*ryz - ryy*rxz)) / (g4 + 1e-30)

    # Mask low-gradient regions
    w = grad_mag / max(np.max(grad_mag), 1e-15)
    H_masked = H_field * w
    K_masked = K_field * w

    iz = rho.shape[2] // 2
    x = np.linspace(0, params.Lx, params.Nx)
    y = np.linspace(0, params.Ly, params.Ny)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    for ax, field, lbl in [(axes[0], H_masked[:,:,iz], "Mean curvature $H$"),
                            (axes[1], K_masked[:,:,iz], "Gaussian curvature $K$")]:
        vabs = np.percentile(np.abs(field[field != 0]), 95) if np.any(field != 0) else 1.0
        if vabs < 1e-15: vabs = 1.0
        norm = TwoSlopeNorm(vmin=-vabs, vcenter=0, vmax=vabs)
        im = ax.pcolormesh(x, y, field.T, shading='auto',
                           cmap=STYLE["cmap_curvature"], norm=norm)
        ax.set_aspect('equal')
        plt.colorbar(im, ax=ax, shrink=0.7)
        _setup_axes(ax, "$x$", "$y$", lbl)

    if title is None:
        title = "Curvature (mid-$z$ slice)"
    fig.suptitle(title, fontsize=STYLE["font_title"] + 2, fontweight="bold", y=1.02)
    fig.tight_layout()
    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


def plot_hessian_eigenvalue_slices(rho, params, title=None, savepath=None):
    """Mid-z slices of the three Hessian eigenvalues."""
    plt = _import_plt()
    TwoSlopeNorm, _ = _import_mpl_extras()
    from invariants_3d import hessian_eigenvalues_3d
    lam1, lam2, lam3 = hessian_eigenvalues_3d(rho, params.hx, params.hy, params.hz)

    iz = rho.shape[2] // 2
    x = np.linspace(0, params.Lx, params.Nx)
    y = np.linspace(0, params.Ly, params.Ny)

    fig, axes = plt.subplots(1, 3, figsize=STYLE["figsize_tri"])
    for ax, field, lbl in [(axes[0], lam1[:,:,iz], r"$\lambda_1$ (max)"),
                            (axes[1], lam2[:,:,iz], r"$\lambda_2$ (mid)"),
                            (axes[2], lam3[:,:,iz], r"$\lambda_3$ (min)")]:
        vabs = max(abs(field.min()), abs(field.max()))
        if vabs < 1e-15: vabs = 1.0
        norm = TwoSlopeNorm(vmin=-vabs, vcenter=0, vmax=vabs)
        im = ax.pcolormesh(x, y, field.T, shading='auto',
                           cmap=STYLE["cmap_signed"], norm=norm)
        ax.set_aspect('equal')
        plt.colorbar(im, ax=ax, shrink=0.7)
        _setup_axes(ax, "$x$", "$y$", lbl)

    if title is None:
        title = "Hessian eigenvalues (mid-$z$ slice)"
    fig.suptitle(title, fontsize=STYLE["font_title"] + 2, fontweight="bold", y=1.02)
    fig.tight_layout()
    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


def plot_geometry_3d(rho, params, savepath=None):
    """Composite: morphology + curvature + Hessian (3 figures)."""
    figs = []
    sp = savepath
    figs.append(plot_morphology_slices(rho, params,
        savepath=sp.replace('.png', '_morph.png') if sp else None))
    figs.append(plot_curvature_slices(rho, params,
        savepath=sp.replace('.png', '_curv.png') if sp else None))
    figs.append(plot_hessian_eigenvalue_slices(rho, params,
        savepath=sp.replace('.png', '_hess.png') if sp else None))
    return figs


# =====================================================================
#  D. HORIZON VISUALIZATIONS
# =====================================================================

def plot_horizon_slices(rho, params, title=None, savepath=None):
    """Orthogonal slices of the horizon proximity field."""
    from invariants_3d import horizon_detector_3d
    hz = horizon_detector_3d(rho, params)
    H_prox = 1.0 - np.clip(params.M(rho) / max(params.M_star, 1e-15), 0, 1)

    fig = plot_slice_triplet(H_prox, params,
                             title=title or "Horizon proximity",
                             cmap=STYLE["cmap_horizon"],
                             label=r"$H_{\mathrm{prox}}$",
                             vmin=0, vmax=1, savepath=savepath)

    plt = _import_plt()
    # Annotate with summary stats
    fig.axes[0].text(0.02, 0.98,
                     f"max={hz['max_proximity']:.3f}\nfrac={hz['horizon_fraction']:.3f}\n"
                     f"comps={hz['n_components']}",
                     transform=fig.axes[0].transAxes, fontsize=STYLE["font_annotation"],
                     va='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


def plot_horizon_mask_slices(rho, params, threshold=0.1, title=None, savepath=None):
    """Binary horizon mask overlaid on density, mid-z slice."""
    plt = _import_plt()
    M_v = params.M(rho)
    mask = (M_v < threshold * params.M_star).astype(float)

    iz = rho.shape[2] // 2
    x = np.linspace(0, params.Lx, params.Nx)
    y = np.linspace(0, params.Ly, params.Ny)

    fig, ax = plt.subplots(1, 1, figsize=STYLE["figsize_single"])
    ax.pcolormesh(x, y, rho[:, :, iz].T, shading='auto',
                  cmap=STYLE["cmap_density"], alpha=0.5)

    if np.any(mask[:, :, iz] > 0):
        ax.contourf(np.linspace(0, params.Lx, params.Nx),
                    np.linspace(0, params.Ly, params.Ny),
                    mask[:, :, iz].T, levels=[0.5, 1.5],
                    colors=[ED_COLORS["red"]], alpha=0.4)
        ax.contour(np.linspace(0, params.Lx, params.Nx),
                   np.linspace(0, params.Ly, params.Ny),
                   mask[:, :, iz].T, levels=[0.5],
                   colors=[ED_COLORS["red"]], linewidths=1.5)

    frac = np.mean(mask)
    ax.text(0.02, 0.98, f"Horizon vol frac: {frac:.1%}",
            transform=ax.transAxes, fontsize=STYLE["font_annotation"],
            va='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
    ax.set_aspect('equal')
    thr_pct = int(threshold * 100)
    _setup_axes(ax, "$x$", "$y$",
                title or f"Horizon mask (mid-z, M < {thr_pct}% M*)")
    fig.tight_layout()
    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


def plot_horizon_3d(rho, params, savepath=None):
    """Composite: proximity slices + mask."""
    figs = []
    sp = savepath
    figs.append(plot_horizon_slices(rho, params,
        savepath=sp.replace('.png', '_prox.png') if sp else None))
    figs.append(plot_horizon_mask_slices(rho, params,
        savepath=sp.replace('.png', '_mask.png') if sp else None))
    return figs


# =====================================================================
#  E. DIAGNOSTICS
# =====================================================================

def plot_time_series_3d(results, savepath=None):
    """Four-panel time-series: energy, mass, participation v, and F_bar."""
    plt = _import_plt()
    fig, axes = plt.subplots(2, 2, figsize=STYLE["figsize_quad"])
    times = np.array(results['times'])

    E_total = [e['total'] for e in results['energy_history']]
    E_pot = [e['potential'] for e in results['energy_history']]
    E_kin = [e['kinetic'] for e in results['energy_history']]
    axes[0, 0].semilogy(times, E_total, color=ED_COLORS["blue"],
                         lw=STYLE["line_lw"], label="Total")
    axes[0, 0].semilogy(times, E_pot, '--', color=ED_COLORS["red"], lw=1, label="Pot")
    axes[0, 0].semilogy(times, E_kin, ':', color=ED_COLORS["green"], lw=1, label="Kin")
    axes[0, 0].legend(fontsize=STYLE["font_legend"])
    _setup_axes(axes[0, 0], "$t$", r"$\mathcal{E}$", "(a) Energy")
    _add_grid(axes[0, 0])

    axes[0, 1].plot(times, results['mass_history'], color=ED_COLORS["blue"],
                    lw=STYLE["line_lw"])
    _setup_axes(axes[0, 1], "$t$", "Mass", "(b) Mass")
    _add_grid(axes[0, 1])

    axes[1, 0].plot(times, results['v_history'], color=ED_COLORS["purple"],
                    lw=STYLE["line_lw"])
    _setup_axes(axes[1, 0], "$t$", "$v$", "(c) Participation")
    _add_grid(axes[1, 0])

    axes[1, 1].plot(times, results['F_bar_history'], color=ED_COLORS["orange"],
                    lw=STYLE["line_lw"])
    axes[1, 1].axhline(0, color='gray', lw=0.5, ls='--')
    _setup_axes(axes[1, 1], "$t$", r"$\bar{F}$", r"(d) $\bar{F}[\rho]$")
    _add_grid(axes[1, 1])

    fig.tight_layout()
    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


def plot_invariants_3d(inv, params=None, savepath=None):
    """
    Invariant dashboard for 3D: 6 panels covering spectral, dynamical,
    and geometric invariants.
    """
    plt = _import_plt()
    fig, axes = plt.subplots(2, 3, figsize=STYLE["figsize_dashboard"])

    spec = inv['spectral']
    dyn = inv['dynamical']
    geo = inv['geometric']
    sf = inv['structure_functions']

    # (a) Spectrum slice (kz=0)
    a = spec['modal_amplitudes']
    E = a ** 2
    K = min(8, E.shape[0])
    E_show = np.log10(np.maximum(E[:K, :K, 0], 1e-30))
    im = axes[0, 0].imshow(E_show.T, origin='lower', aspect='auto',
                            cmap=STYLE["cmap_spectral"])
    plt.colorbar(im, ax=axes[0, 0], label=r"$\log_{10}|a|^2$", shrink=0.7)
    _setup_axes(axes[0, 0], r"$k_x$", r"$k_y$", "(a) Spectrum ($k_z$=0)")

    # (b) Dissipation ratios
    dr = dyn['dissipation_ratios']
    axes[0, 1].bar(['Grad', 'Pen', 'Part'],
                   [dr['R_grad'], dr['R_pen'], dr['R_part']],
                   color=[ED_COLORS["blue"], ED_COLORS["red"], ED_COLORS["green"]])
    axes[0, 1].set_ylim(0, 1)
    _setup_axes(axes[0, 1], "", "Fraction", "(b) Dissipation ratios")

    # (c) Geometric norms
    gn = spec['geometric_norms']
    alphas = sorted(gn.keys())
    axes[0, 2].semilogy(alphas, [max(gn[a], 1e-30) for a in alphas], 'o-',
                        color=ED_COLORS["purple"], lw=STYLE["line_lw"])
    _setup_axes(axes[0, 2], r"$\alpha$", r"$G_\alpha$", "(c) Geometric norms")
    _add_grid(axes[0, 2])

    # (d) Text summary
    ax_t = axes[1, 0]
    sa = spec['spectral_anisotropy']
    morph = geo['morphology']
    hz = geo['horizon']
    cl = geo['correlation_lengths']
    curv = geo['curvature']
    lines = [
        f"Spectral entropy = {spec['spectral_entropy']:.4f}",
        f"Renyi H_2 = {spec['renyi_2']:.4f}",
        f"Isotropy = {sa['isotropy']:.4f}",
        f"Planarity = {sa['planarity']:.4f}",
        f"Linearity = {sa['linearity']:.4f}",
        f"",
        f"Filament frac = {morph['filament_fraction']:.3f}",
        f"Sheet frac = {morph['sheet_fraction']:.3f}",
        f"Blob frac = {morph['blob_fraction']:.3f}",
        f"H_curv rms = {curv['mean_curvature_rms']:.4f}",
        f"Horizon max = {hz['max_proximity']:.4f}",
        f"xi = ({cl['xi_x']:.3f},{cl['xi_y']:.3f},{cl['xi_z']:.3f})",
        f"C_ED = {dyn['ed_complexity']:.4e}",
    ]
    ax_t.text(0.05, 0.95, "\n".join(lines), transform=ax_t.transAxes,
              fontsize=STYLE["font_annotation"] + 1, va='top', fontfamily='monospace')
    ax_t.axis('off')
    ax_t.set_title("(d) Invariant summary", fontsize=STYLE["font_title"], fontweight="bold")

    # (e) Structure functions
    r_lags = sf['r_lags']
    for p in [2, 4]:
        if p in sf:
            m = sf[p] > 0
            if np.any(m):
                axes[1, 1].loglog(r_lags[m], sf[p][m], 'o-', lw=1.2, ms=3,
                                  label=f"$S_{p}$")
    axes[1, 1].legend(fontsize=STYLE["font_legend"])
    _setup_axes(axes[1, 1], "$r$", "$S_p(r)$", "(e) Structure functions")
    _add_grid(axes[1, 1])

    # (f) Morphology pie chart
    morph_vals = [morph['filament_fraction'], morph['sheet_fraction'], morph['blob_fraction']]
    morph_labels = ['Filament', 'Sheet', 'Blob']
    morph_colors = [ED_COLORS["red"], ED_COLORS["blue"], ED_COLORS["green"]]
    axes[1, 2].pie(morph_vals, labels=morph_labels, colors=morph_colors,
                   autopct='%1.0f%%', startangle=90,
                   textprops={'fontsize': STYLE["font_annotation"] + 1})
    axes[1, 2].set_title("(f) Morphology", fontsize=STYLE["font_title"], fontweight="bold")

    fig.tight_layout()
    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig
