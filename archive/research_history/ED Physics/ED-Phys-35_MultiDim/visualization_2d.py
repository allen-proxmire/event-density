"""
visualization_2d.py
===================
2D visualization and diagnostics suite for the canonical Event Density PDE.

Provides publication-ready visualizations of:
  A. Fields        — heatmaps, contours, quiver plots, level-set overlays
  B. Spectra       — 2D amplitude spectrum, radial spectrum, anisotropy ellipse
  C. Geometry      — Hessian eigenvalue maps, filamentarity, curvature
  D. Horizons      — proximity fields, horizon masks, boundary overlays
  E. Diagnostics   — energy/mass/dissipation time series, invariant dashboards

Style conventions follow the ED-SIM atlas (generate_all_figures.py):
  - 300 DPI, tight layout
  - inferno for density, viridis for gradients, RdBu for signed fields
  - Centralized STYLE dict for fonts, sizes, grid
"""

import numpy as np
from typing import Dict, Optional, Tuple, List

# Lazy matplotlib import (ED-SIM convention)
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
    from matplotlib.patches import Ellipse
    from matplotlib.colors import Normalize, TwoSlopeNorm
    import matplotlib.gridspec as gridspec
    return Ellipse, Normalize, TwoSlopeNorm, gridspec


# =====================================================================
#  STYLE CONSTANTS (matching ED-SIM atlas)
# =====================================================================

STYLE = {
    "dpi": 300,
    "figsize_single": (7, 6),
    "figsize_wide": (14, 5),
    "figsize_tall": (7, 10),
    "figsize_square": (7, 7),
    "figsize_quad": (13, 11),
    "figsize_dashboard": (16, 12),
    "font_title": 13,
    "font_label": 11,
    "font_tick": 9,
    "font_legend": 9,
    "font_annotation": 8,
    "grid_alpha": 0.3,
    "grid_lw": 0.5,
    "line_lw": 1.5,
    "marker_s": 30,
    "cmap_density": "inferno",
    "cmap_gradient": "viridis",
    "cmap_signed": "RdBu_r",
    "cmap_horizon": "Reds",
    "cmap_spectral": "plasma",
    "cmap_curvature": "coolwarm",
}

ED_COLORS = {
    "blue": "#2166ac",
    "red": "#b2182b",
    "green": "#1b7837",
    "purple": "#762a83",
    "orange": "#e08214",
    "gray": "#999999",
}


def _setup_axes(ax, xlabel, ylabel, title):
    """Apply consistent axis styling."""
    ax.set_xlabel(xlabel, fontsize=STYLE["font_label"])
    ax.set_ylabel(ylabel, fontsize=STYLE["font_label"])
    ax.set_title(title, fontsize=STYLE["font_title"], fontweight="bold")
    ax.tick_params(labelsize=STYLE["font_tick"])


def _add_grid(ax):
    ax.grid(True, alpha=STYLE["grid_alpha"], linewidth=STYLE["grid_lw"])


def _make_xy_grid(params):
    """Build coordinate arrays from params."""
    x = np.linspace(0, params.Lx, params.Nx)
    y = np.linspace(0, params.Ly, params.Ny)
    return x, y, *np.meshgrid(x, y, indexing='ij')


# =====================================================================
#  A. FIELD VISUALIZATIONS
# =====================================================================

def plot_density_heatmap(rho, params, ax=None, title=None,
                         vmin=None, vmax=None, cmap=None):
    """
    Heatmap of the density field rho(x,y).

    Parameters
    ----------
    rho : (Nx, Ny) array
    params : EDParameters2D
    ax : optional matplotlib Axes
    title : optional title string
    vmin, vmax : color limits (auto if None)
    cmap : colormap (default: inferno)

    Returns
    -------
    ax : matplotlib Axes
    """
    plt = _import_plt()
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=STYLE["figsize_single"])
    if cmap is None:
        cmap = STYLE["cmap_density"]
    if title is None:
        title = r"Density $\rho(x,y)$"

    x, y, X, Y = _make_xy_grid(params)
    im = ax.pcolormesh(x, y, rho.T, shading='auto', cmap=cmap,
                       vmin=vmin, vmax=vmax)
    ax.set_aspect('equal')
    plt.colorbar(im, ax=ax, label=r"$\rho$", shrink=0.8)
    _setup_axes(ax, r"$x$", r"$y$", title)
    return ax


def plot_density_contour(rho, params, ax=None, n_levels=15, title=None,
                         filled=True, show_labels=True):
    """
    Contour plot of rho(x,y).
    """
    plt = _import_plt()
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=STYLE["figsize_single"])
    if title is None:
        title = r"Density contours $\rho(x,y)$"

    x, y, X, Y = _make_xy_grid(params)
    if filled:
        cs = ax.contourf(X, Y, rho, levels=n_levels, cmap=STYLE["cmap_density"])
        plt.colorbar(cs, ax=ax, label=r"$\rho$", shrink=0.8)
    else:
        cs = ax.contour(X, Y, rho, levels=n_levels, colors='k', linewidths=0.5)
    if show_labels and not filled:
        ax.clabel(cs, inline=True, fontsize=STYLE["font_annotation"])
    ax.set_aspect('equal')
    _setup_axes(ax, r"$x$", r"$y$", title)
    return ax


def plot_gradient_quiver(rho, params, ax=None, title=None,
                         stride=4, scale=None, color_by_magnitude=True):
    """
    Quiver plot of the gradient field nabla rho.

    Parameters
    ----------
    stride : plot every `stride`-th arrow
    scale : quiver scale factor (auto if None)
    color_by_magnitude : color arrows by |nabla rho|
    """
    plt = _import_plt()
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=STYLE["figsize_single"])
    if title is None:
        title = r"Gradient field $\nabla\rho$"

    from invariants_2d import _grad_components
    gx, gy = _grad_components(rho, params.hx, params.hy)
    mag = np.sqrt(gx**2 + gy**2)

    x, y, X, Y = _make_xy_grid(params)
    s = stride
    Xs, Ys = X[::s, ::s], Y[::s, ::s]
    Gx, Gy = gx[::s, ::s], gy[::s, ::s]
    Ms = mag[::s, ::s]

    if color_by_magnitude:
        q = ax.quiver(Xs, Ys, Gx, Gy, Ms, cmap=STYLE["cmap_gradient"],
                      scale=scale, alpha=0.85)
        plt.colorbar(q, ax=ax, label=r"$|\nabla\rho|$", shrink=0.8)
    else:
        ax.quiver(Xs, Ys, Gx, Gy, scale=scale, alpha=0.7, color=ED_COLORS["blue"])

    ax.set_aspect('equal')
    _setup_axes(ax, r"$x$", r"$y$", title)
    return ax


def plot_level_sets(rho, params, ax=None, levels=None, n_levels=10,
                    title=None, show_gradient=False, stride=6):
    """
    Level-set overlay: contour lines with optional gradient arrows.
    """
    plt = _import_plt()
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=STYLE["figsize_single"])
    if title is None:
        title = r"Level sets of $\rho$"
    if levels is None:
        levels = n_levels

    x, y, X, Y = _make_xy_grid(params)

    # Background heatmap
    im = ax.pcolormesh(x, y, rho.T, shading='auto',
                       cmap=STYLE["cmap_density"], alpha=0.4)
    # Contour lines
    cs = ax.contour(X, Y, rho, levels=levels, colors='white',
                    linewidths=0.8, alpha=0.9)
    ax.clabel(cs, inline=True, fontsize=6, fmt='%.3f')

    if show_gradient:
        from invariants_2d import _grad_components
        gx, gy = _grad_components(rho, params.hx, params.hy)
        s = stride
        ax.quiver(X[::s, ::s], Y[::s, ::s], gx[::s, ::s], gy[::s, ::s],
                  color='cyan', alpha=0.6, scale=None)

    ax.set_aspect('equal')
    _setup_axes(ax, r"$x$", r"$y$", title)
    return ax


def plot_field_quad(rho, params, title=None, savepath=None):
    """
    Four-panel field overview: density heatmap, contours, gradient quiver,
    and gradient magnitude.

    Returns the figure.
    """
    plt = _import_plt()
    fig, axes = plt.subplots(2, 2, figsize=STYLE["figsize_quad"])

    # (a) Density heatmap
    plot_density_heatmap(rho, params, ax=axes[0, 0],
                         title=r"(a) Density $\rho$")

    # (b) Contour
    plot_density_contour(rho, params, ax=axes[0, 1],
                         title=r"(b) Contours")

    # (c) Gradient quiver
    plot_gradient_quiver(rho, params, ax=axes[1, 0],
                         title=r"(c) $\nabla\rho$")

    # (d) Gradient magnitude
    from invariants_2d import _grad_components
    gx, gy = _grad_components(rho, params.hx, params.hy)
    grad_mag = np.sqrt(gx**2 + gy**2)
    x, y, _, _ = _make_xy_grid(params)
    im = axes[1, 1].pcolormesh(x, y, grad_mag.T, shading='auto',
                                cmap=STYLE["cmap_gradient"])
    plt.colorbar(im, ax=axes[1, 1], label=r"$|\nabla\rho|$", shrink=0.8)
    axes[1, 1].set_aspect('equal')
    _setup_axes(axes[1, 1], r"$x$", r"$y$", r"(d) $|\nabla\rho|$")

    if title:
        fig.suptitle(title, fontsize=STYLE["font_title"] + 2, fontweight="bold", y=1.01)
    fig.tight_layout()

    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


# =====================================================================
#  B. SPECTRAL VISUALIZATIONS
# =====================================================================

def plot_spectrum_2d(a, Lx, Ly, ax=None, title=None, log_scale=True,
                     Kx_show=None, Ky_show=None):
    """
    2D amplitude spectrum |a_{kx,ky}|^2 as a heatmap.

    Parameters
    ----------
    a : (Kx, Ky) modal amplitude array
    log_scale : use log10 color scale
    Kx_show, Ky_show : crop to this many modes
    """
    plt = _import_plt()
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=STYLE["figsize_single"])
    if title is None:
        title = r"Modal energy $|a_{k_x,k_y}|^2$"

    E = a ** 2
    Kx, Ky = E.shape
    if Kx_show:
        E = E[:Kx_show, :]
    if Ky_show:
        E = E[:, :Ky_show]

    if log_scale:
        E_plot = np.log10(np.maximum(E, 1e-30))
        label = r"$\log_{10}|a|^2$"
    else:
        E_plot = E
        label = r"$|a|^2$"

    im = ax.imshow(E_plot.T, origin='lower', aspect='auto',
                   cmap=STYLE["cmap_spectral"],
                   extent=[0, E_plot.shape[0], 0, E_plot.shape[1]])
    plt.colorbar(im, ax=ax, label=label, shrink=0.8)
    _setup_axes(ax, r"$k_x$", r"$k_y$", title)
    return ax


def plot_radial_spectrum(a, Lx, Ly, ax=None, title=None, n_bins=20):
    """
    Radially-averaged energy spectrum E(|k|).
    """
    plt = _import_plt()
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=STYLE["figsize_single"])
    if title is None:
        title = "Radial energy spectrum"

    from invariants_2d import spectral_entropy_radial
    k_bins, E_binned = spectral_entropy_radial(a, Lx, Ly, n_bins=n_bins)

    mask = E_binned > 0
    if np.any(mask):
        ax.semilogy(k_bins[mask], E_binned[mask], 'o-',
                    color=ED_COLORS["blue"], lw=STYLE["line_lw"], ms=4)
    ax.set_xlim(left=0)
    _setup_axes(ax, r"$|k|$", r"$E(|k|)$", title)
    _add_grid(ax)
    return ax


def plot_anisotropy_ellipse(spec_anis, ax=None, title=None):
    """
    Visualise spectral anisotropy as an ellipse from the inertia tensor.

    Parameters
    ----------
    spec_anis : dict from spectral_anisotropy() containing Ixx, Iyy, Ixy
    """
    plt = _import_plt()
    Ellipse, _, _, _ = _import_mpl_extras()
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    if title is None:
        title = "Spectral anisotropy"

    Ixx = spec_anis['Ixx']
    Iyy = spec_anis['Iyy']
    Ixy = spec_anis['Ixy']

    # Eigenvalues and angle
    trace = Ixx + Iyy
    det = Ixx * Iyy - Ixy**2
    disc = max(trace**2 - 4 * det, 0.0)
    lam1 = 0.5 * (trace + np.sqrt(disc))
    lam2 = 0.5 * (trace - np.sqrt(disc))

    if abs(Ixx - Iyy) > 1e-15:
        angle_rad = 0.5 * np.arctan2(2 * Ixy, Ixx - Iyy)
    else:
        angle_rad = 0.0
    angle_deg = np.degrees(angle_rad)

    # Scale for visibility
    scale = 1.0 / max(np.sqrt(lam1), 1e-10)
    w = 2 * np.sqrt(max(lam1, 0)) * scale
    h = 2 * np.sqrt(max(lam2, 0)) * scale

    ell = Ellipse((0, 0), w, h, angle=angle_deg,
                  facecolor=ED_COLORS["blue"], alpha=0.3,
                  edgecolor=ED_COLORS["blue"], linewidth=2)
    ax.add_patch(ell)

    lim = max(w, h) * 0.7
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5, ls='--')
    ax.axvline(0, color='gray', lw=0.5, ls='--')

    ecc = spec_anis['eccentricity']
    A = spec_anis['anisotropy']
    ax.text(0.05, 0.95, f"$A_{{spec}}$ = {A:.3f}\necc = {ecc:.3f}",
            transform=ax.transAxes, fontsize=STYLE["font_annotation"],
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    _setup_axes(ax, r"$k_x$", r"$k_y$", title)
    return ax


def plot_spectral_overview(a, Lx, Ly, spec_anis=None, savepath=None):
    """
    Three-panel spectral overview: 2D spectrum, radial spectrum, anisotropy ellipse.
    """
    plt = _import_plt()
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    plot_spectrum_2d(a, Lx, Ly, ax=axes[0], title="(a) 2D spectrum")
    plot_radial_spectrum(a, Lx, Ly, ax=axes[1], title="(b) Radial spectrum")

    if spec_anis is not None:
        plot_anisotropy_ellipse(spec_anis, ax=axes[2], title="(c) Anisotropy")
    else:
        axes[2].text(0.5, 0.5, "No anisotropy data", ha='center', va='center',
                     transform=axes[2].transAxes)
        axes[2].set_title("(c) Anisotropy")

    fig.tight_layout()
    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


# =====================================================================
#  C. GEOMETRIC VISUALIZATIONS
# =====================================================================

def plot_hessian_eigenvalues(rho, params, ax=None, which='max', title=None):
    """
    Hessian eigenvalue map.

    Parameters
    ----------
    which : 'max' for lambda_1 (largest), 'min' for lambda_2, 'det' for determinant
    """
    plt = _import_plt()
    _, _, TwoSlopeNorm, _ = _import_mpl_extras()
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=STYLE["figsize_single"])

    from invariants_2d import hessian_eigenvalues_2d
    lam1, lam2 = hessian_eigenvalues_2d(rho, params.hx, params.hy)

    x, y, _, _ = _make_xy_grid(params)

    if which == 'max':
        field = lam1
        label = r"$\lambda_1$ (max)"
    elif which == 'min':
        field = lam2
        label = r"$\lambda_2$ (min)"
    elif which == 'det':
        field = lam1 * lam2
        label = r"$\lambda_1 \lambda_2$ (det)"
    else:
        raise ValueError(f"Unknown which={which}")

    if title is None:
        title = f"Hessian {label}"

    vabs = max(abs(np.min(field)), abs(np.max(field)))
    if vabs < 1e-15:
        vabs = 1.0
    norm = TwoSlopeNorm(vmin=-vabs, vcenter=0, vmax=vabs)
    im = ax.pcolormesh(x, y, field.T, shading='auto',
                       cmap=STYLE["cmap_signed"], norm=norm)
    plt.colorbar(im, ax=ax, label=label, shrink=0.8)
    ax.set_aspect('equal')
    _setup_axes(ax, r"$x$", r"$y$", title)
    return ax


def plot_filamentarity_field(rho, params, ax=None, title=None):
    """
    Filamentarity field: F(x,y) = 1 - |lambda_min|/|lambda_max|.
    """
    plt = _import_plt()
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=STYLE["figsize_single"])
    if title is None:
        title = "Filamentarity $F(x,y)$"

    from invariants_2d import hessian_eigenvalues_2d
    lam1, lam2 = hessian_eigenvalues_2d(rho, params.hx, params.hy)
    abs_max = np.maximum(np.abs(lam1), np.abs(lam2))
    abs_min = np.minimum(np.abs(lam1), np.abs(lam2))
    F = np.where(abs_max > 1e-15, 1.0 - abs_min / abs_max, 0.0)

    x, y, _, _ = _make_xy_grid(params)
    im = ax.pcolormesh(x, y, F.T, shading='auto', cmap='YlOrRd',
                       vmin=0, vmax=1)
    plt.colorbar(im, ax=ax, label="$F$", shrink=0.8)
    ax.set_aspect('equal')
    _setup_axes(ax, r"$x$", r"$y$", title)
    return ax


def plot_curvature_field(rho, params, ax=None, title=None):
    """
    Level-set curvature field kappa(x,y).
    """
    plt = _import_plt()
    _, _, TwoSlopeNorm, _ = _import_mpl_extras()
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=STYLE["figsize_single"])
    if title is None:
        title = r"Level-set curvature $\kappa(x,y)$"

    from invariants_2d import level_set_curvature_2d, _grad_components
    gx, gy = _grad_components(rho, params.hx, params.hy)
    grad_mag = np.sqrt(gx**2 + gy**2)

    from invariants_2d import _pad_neumann
    p = _pad_neumann(rho)
    hx, hy = params.hx, params.hy
    rho_xx = (p[2:, 1:-1] + p[:-2, 1:-1] - 2.0*p[1:-1, 1:-1]) / (hx*hx)
    rho_yy = (p[1:-1, 2:] + p[1:-1, :-2] - 2.0*p[1:-1, 1:-1]) / (hy*hy)
    rho_xy = (p[2:, 2:] - p[2:, :-2] - p[:-2, 2:] + p[:-2, :-2]) / (4*hx*hy)
    num = rho_xx * gy**2 - 2*rho_xy*gx*gy + rho_yy * gx**2
    kappa = num / (grad_mag**3 + 1e-15)
    # Mask low-gradient regions
    kappa_masked = np.where(grad_mag > 0.01 * np.max(grad_mag), kappa, 0.0)

    x, y_arr, _, _ = _make_xy_grid(params)
    vabs = np.percentile(np.abs(kappa_masked[kappa_masked != 0]), 95) if np.any(kappa_masked != 0) else 1.0
    if vabs < 1e-15:
        vabs = 1.0
    norm = TwoSlopeNorm(vmin=-vabs, vcenter=0, vmax=vabs)
    im = ax.pcolormesh(x, y_arr, kappa_masked.T, shading='auto',
                       cmap=STYLE["cmap_curvature"], norm=norm)
    plt.colorbar(im, ax=ax, label=r"$\kappa$", shrink=0.8)
    ax.set_aspect('equal')
    _setup_axes(ax, r"$x$", r"$y$", title)
    return ax


def plot_geometry_2d(rho, params, savepath=None):
    """
    Four-panel geometric overview: Hessian max eigenvalue, determinant,
    filamentarity, and curvature.
    """
    plt = _import_plt()
    fig, axes = plt.subplots(2, 2, figsize=STYLE["figsize_quad"])

    plot_hessian_eigenvalues(rho, params, ax=axes[0, 0], which='max',
                            title=r"(a) $\lambda_{\max}$")
    plot_hessian_eigenvalues(rho, params, ax=axes[0, 1], which='det',
                            title=r"(b) $\lambda_1 \lambda_2$ (peaks vs saddles)")
    plot_filamentarity_field(rho, params, ax=axes[1, 0],
                            title="(c) Filamentarity $F$")
    plot_curvature_field(rho, params, ax=axes[1, 1],
                        title=r"(d) Level-set curvature $\kappa$")

    fig.tight_layout()
    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


# =====================================================================
#  D. HORIZON & PROXIMITY VISUALIZATIONS
# =====================================================================

def plot_horizon_proximity(rho, params, ax=None, title=None):
    """
    Horizon proximity field: H_prox(x,y) = 1 - M(rho)/M*.
    """
    plt = _import_plt()
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=STYLE["figsize_single"])
    if title is None:
        title = "Horizon proximity"

    from invariants_2d import horizon_detector_2d
    hz = horizon_detector_2d(rho, params)
    H_prox = hz['proximity_field']

    x, y, _, _ = _make_xy_grid(params)
    im = ax.pcolormesh(x, y, H_prox.T, shading='auto',
                       cmap=STYLE["cmap_horizon"], vmin=0, vmax=1)
    plt.colorbar(im, ax=ax, label=r"$H_{\mathrm{prox}}$", shrink=0.8)
    ax.set_aspect('equal')
    _setup_axes(ax, r"$x$", r"$y$", title)

    # Annotate stats
    ax.text(0.02, 0.98,
            f"max = {hz['max_proximity']:.3f}\nmargin = {hz['horizon_margin']:.2e}",
            transform=ax.transAxes, fontsize=STYLE["font_annotation"],
            va='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
    return ax


def plot_horizon_mask(rho, params, ax=None, title=None, threshold=0.1):
    """
    Binary horizon mask: regions where M(rho) < threshold * M*.
    """
    plt = _import_plt()
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=STYLE["figsize_single"])
    if title is None:
        title = f"Horizon mask ($M < {threshold:.0%}\\, M^*$)"

    M_vals = params.M(rho)
    mask = (M_vals < threshold * params.M_star).astype(float)

    x, y, _, _ = _make_xy_grid(params)
    # Background: density
    ax.pcolormesh(x, y, rho.T, shading='auto',
                  cmap=STYLE["cmap_density"], alpha=0.5)
    # Overlay: horizon mask
    ax.contourf(np.linspace(0, params.Lx, params.Nx),
                np.linspace(0, params.Ly, params.Ny),
                mask.T, levels=[0.5, 1.5],
                colors=[ED_COLORS["red"]], alpha=0.4)
    ax.contour(np.linspace(0, params.Lx, params.Nx),
               np.linspace(0, params.Ly, params.Ny),
               mask.T, levels=[0.5],
               colors=[ED_COLORS["red"]], linewidths=1.5)

    frac = np.mean(mask)
    ax.text(0.02, 0.98, f"Horizon fraction: {frac:.1%}",
            transform=ax.transAxes, fontsize=STYLE["font_annotation"],
            va='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

    ax.set_aspect('equal')
    _setup_axes(ax, r"$x$", r"$y$", title)
    return ax


def plot_horizon_2d(rho, params, savepath=None):
    """
    Two-panel horizon overview: proximity field + mask.
    """
    plt = _import_plt()
    fig, axes = plt.subplots(1, 2, figsize=STYLE["figsize_wide"])
    plot_horizon_proximity(rho, params, ax=axes[0], title="(a) Proximity")
    plot_horizon_mask(rho, params, ax=axes[1], title="(b) Horizon mask")
    fig.tight_layout()
    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


# =====================================================================
#  E. DIAGNOSTIC TIME SERIES & INVARIANT DASHBOARDS
# =====================================================================

def plot_time_series(results, savepath=None):
    """
    Four-panel time-series diagnostics from run_simulation_2d output.

    Panels: (a) Energy, (b) Mass, (c) Participation v, (d) F_bar.
    """
    plt = _import_plt()
    fig, axes = plt.subplots(2, 2, figsize=STYLE["figsize_quad"])

    times = np.array(results['times'])

    # (a) Energy
    E_total = [e['total'] for e in results['energy_history']]
    E_pot = [e['potential'] for e in results['energy_history']]
    E_kin = [e['kinetic'] for e in results['energy_history']]
    axes[0, 0].semilogy(times, E_total, color=ED_COLORS["blue"],
                         lw=STYLE["line_lw"], label="Total")
    axes[0, 0].semilogy(times, E_pot, '--', color=ED_COLORS["red"],
                         lw=1.0, label="Potential")
    axes[0, 0].semilogy(times, E_kin, ':', color=ED_COLORS["green"],
                         lw=1.0, label="Kinetic")
    axes[0, 0].legend(fontsize=STYLE["font_legend"])
    _setup_axes(axes[0, 0], r"$t$", r"$\mathcal{E}$", "(a) Energy")
    _add_grid(axes[0, 0])

    # (b) Mass
    axes[0, 1].plot(times, results['mass_history'], color=ED_COLORS["blue"],
                    lw=STYLE["line_lw"])
    _setup_axes(axes[0, 1], r"$t$", "Mass", "(b) Mass")
    _add_grid(axes[0, 1])

    # (c) Participation v
    axes[1, 0].plot(times, results['v_history'], color=ED_COLORS["purple"],
                    lw=STYLE["line_lw"])
    _setup_axes(axes[1, 0], r"$t$", r"$v$", "(c) Participation")
    _add_grid(axes[1, 0])

    # (d) F_bar
    axes[1, 1].plot(times, results['F_bar_history'], color=ED_COLORS["orange"],
                    lw=STYLE["line_lw"])
    axes[1, 1].axhline(0, color='gray', lw=0.5, ls='--')
    _setup_axes(axes[1, 1], r"$t$", r"$\bar{F}$", r"(d) $\bar{F}[\rho]$")
    _add_grid(axes[1, 1])

    fig.tight_layout()
    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


def plot_invariants_2d(inv, params=None, savepath=None):
    """
    Full invariant dashboard from compute_invariants_2d() output.

    Six panels covering spectral, dynamical, and geometric invariants.
    """
    plt = _import_plt()
    fig, axes = plt.subplots(2, 3, figsize=STYLE["figsize_dashboard"])

    spec = inv['spectral']
    dyn = inv['dynamical']
    geo = inv['geometric']
    sf = inv['structure_functions']

    # (a) 2D spectrum
    a = spec['modal_amplitudes']
    E = a ** 2
    K = min(16, E.shape[0])
    E_show = np.log10(np.maximum(E[:K, :K], 1e-30))
    im = axes[0, 0].imshow(E_show.T, origin='lower', aspect='auto',
                            cmap=STYLE["cmap_spectral"])
    plt.colorbar(im, ax=axes[0, 0], label=r"$\log_{10}|a|^2$", shrink=0.7)
    _setup_axes(axes[0, 0], r"$k_x$", r"$k_y$", "(a) Modal energy")

    # (b) Dissipation ratios (bar chart)
    dr = dyn['dissipation_ratios']
    bars = axes[0, 1].bar(['Gradient', 'Penalty', 'Participation'],
                          [dr['R_grad'], dr['R_pen'], dr['R_part']],
                          color=[ED_COLORS["blue"], ED_COLORS["red"], ED_COLORS["green"]])
    axes[0, 1].set_ylim(0, 1)
    _setup_axes(axes[0, 1], "", "Fraction", "(b) Dissipation ratios")

    # (c) Geometric norms
    gn = spec['geometric_norms']
    alphas = sorted(gn.keys())
    vals = [gn[a] for a in alphas]
    axes[0, 2].semilogy(alphas, [max(v, 1e-30) for v in vals], 'o-',
                        color=ED_COLORS["purple"], lw=STYLE["line_lw"])
    _setup_axes(axes[0, 2], r"$\alpha$", r"$G_\alpha$", "(c) Geometric norms")
    _add_grid(axes[0, 2])

    # (d) Spectral entropy + anisotropy text
    ax_text = axes[1, 0]
    sa = spec['spectral_anisotropy']
    mh = spec['modal_hierarchy']
    fil = geo['filamentarity']
    cl = geo['correlation_lengths']
    hz = geo['horizon']
    lines = [
        f"Spectral entropy H = {spec['spectral_entropy']:.4f}",
        f"Renyi H_2 = {spec['renyi_2']:.4f}",
        f"Spectral anisotropy = {sa['anisotropy']:.4f}",
        f"Eccentricity = {sa['eccentricity']:.4f}",
        f"Modal decay rate = {mh['decay_rate']:.2f}",
        f"ED complexity = {dyn['ed_complexity']:.4e}",
        f"",
        f"Filamentarity = {fil['filamentarity_mean']:.4f}",
        f"Saddle fraction = {fil['saddle_fraction']:.4f}",
        f"Corr xi_x = {cl['xi_x']:.4f}, xi_y = {cl['xi_y']:.4f}",
        f"Horizon max prox = {hz['max_proximity']:.4f}",
    ]
    ax_text.text(0.05, 0.95, "\n".join(lines), transform=ax_text.transAxes,
                 fontsize=STYLE["font_annotation"] + 1, va='top',
                 fontfamily='monospace')
    ax_text.axis('off')
    ax_text.set_title("(d) Invariant summary", fontsize=STYLE["font_title"],
                      fontweight="bold")

    # (e) Structure functions
    r_lags = sf['r_lags']
    for p_order in [2, 4]:
        if p_order in sf:
            mask = sf[p_order] > 0
            if np.any(mask):
                axes[1, 1].loglog(r_lags[mask], sf[p_order][mask],
                                  'o-', lw=1.2, ms=3, label=f"$S_{p_order}$")
    axes[1, 1].legend(fontsize=STYLE["font_legend"])
    _setup_axes(axes[1, 1], r"$r$", r"$S_p(r)$", "(e) Structure functions")
    _add_grid(axes[1, 1])

    # (f) Growth rate stats
    lgr = dyn['local_growth_rate_stats']
    part = dyn['participation']
    diss = dyn['dissipation_channels']
    bars2_labels = [r"$\sigma_{\min}$", r"$\sigma_{\max}$", r"$\sigma_{\mathrm{mean}}$"]
    bars2_vals = [lgr['min'], lgr['max'], lgr['mean']]
    colors2 = [ED_COLORS["green"] if v < 0 else ED_COLORS["red"] for v in bars2_vals]
    axes[1, 2].barh(bars2_labels, bars2_vals, color=colors2, alpha=0.7)
    axes[1, 2].axvline(0, color='gray', lw=0.5)
    _setup_axes(axes[1, 2], "Rate", "", "(f) Local growth rates")

    fig.tight_layout()
    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig


def plot_snapshot_evolution(rho_snapshots, times, params,
                           n_show=6, savepath=None):
    """
    Multi-panel snapshot evolution: density heatmaps at selected times.
    """
    plt = _import_plt()
    n_total = len(rho_snapshots)
    indices = np.linspace(0, n_total - 1, min(n_show, n_total), dtype=int)
    n = len(indices)
    ncols = min(n, 3)
    nrows = (n + ncols - 1) // ncols

    fig, axes = plt.subplots(nrows, ncols,
                             figsize=(5 * ncols, 4.5 * nrows))
    if n == 1:
        axes = np.array([axes])
    axes = np.atleast_2d(axes)

    vmin = min(r.min() for r in rho_snapshots)
    vmax = max(r.max() for r in rho_snapshots)
    x = np.linspace(0, params.Lx, params.Nx)
    y = np.linspace(0, params.Ly, params.Ny)

    for panel_idx, snap_idx in enumerate(indices):
        row, col = divmod(panel_idx, ncols)
        ax = axes[row, col]
        im = ax.pcolormesh(x, y, rho_snapshots[snap_idx].T,
                           shading='auto', cmap=STYLE["cmap_density"],
                           vmin=vmin, vmax=vmax)
        ax.set_aspect('equal')
        t = times[snap_idx]
        ax.set_title(f"$t = {t:.3f}$", fontsize=STYLE["font_title"])
        ax.tick_params(labelsize=STYLE["font_tick"])

    # Hide unused panels
    for panel_idx in range(len(indices), nrows * ncols):
        row, col = divmod(panel_idx, ncols)
        axes[row, col].axis('off')

    # Shared colorbar
    fig.subplots_adjust(right=0.92)
    cbar_ax = fig.add_axes([0.94, 0.15, 0.015, 0.7])
    fig.colorbar(im, cax=cbar_ax, label=r"$\rho$")

    fig.suptitle("Density evolution", fontsize=STYLE["font_title"] + 2,
                 fontweight="bold")
    fig.tight_layout(rect=[0, 0, 0.92, 0.96])

    if savepath:
        fig.savefig(savepath, dpi=STYLE["dpi"], bbox_inches="tight")
    return fig
