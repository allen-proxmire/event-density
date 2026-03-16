"""
ED-Phys-02: Visualization Hooks
==================================
Canonical source: ED-Phys-01 §9

Plotting functions for 1D and 2D simulation results.
These are HOOKS only — they define the interface and plotting logic
but do NOT auto-generate images. Call them explicitly when needed.

Requires matplotlib (not imported at module level to keep the
simulator dependency-free).
"""

import numpy as np
from ed_phys_engine import SimulationResult
from ed_phys_diagnostics import extract_time_series
from ed_phys_operators import discrete_grad_squared, discrete_grad_magnitude


# ============================================================
# 1D Visualization Hooks
# ============================================================

def plot_1d_density(
    rho: np.ndarray,
    ax=None,
    title: str = "Event Density ρ(x)",
    **kwargs,
):
    """Line plot of ρ(x) for a 1D field.

    Parameters
    ----------
    rho : np.ndarray, shape (N,)
    ax : matplotlib Axes or None (creates new figure)
    """
    import matplotlib.pyplot as plt
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 4))
    ax.plot(rho, **kwargs)
    ax.set_xlabel("Lattice site x")
    ax.set_ylabel("ρ(x)")
    ax.set_title(title)
    return ax


def plot_1d_gradient(
    rho: np.ndarray,
    dx: float = 1.0,
    ax=None,
    title: str = "|∇ρ|(x)",
    **kwargs,
):
    """Line plot of |∇ρ| for a 1D field."""
    import matplotlib.pyplot as plt
    grad_mag = discrete_grad_magnitude(rho, dx, boundary="periodic")
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 4))
    ax.plot(grad_mag, **kwargs)
    ax.set_xlabel("Lattice site x")
    ax.set_ylabel("|∇ρ|")
    ax.set_title(title)
    return ax


def plot_1d_curvature(
    rho: np.ndarray,
    dx: float = 1.0,
    ax=None,
    title: str = "∇²ρ (curvature proxy)",
    **kwargs,
):
    """Line plot of ∇²ρ for a 1D field (curvature proxy)."""
    import matplotlib.pyplot as plt
    from ed_phys_operators import discrete_laplacian
    lap = discrete_laplacian(rho, dx, boundary="periodic")
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 4))
    ax.plot(lap, color="green", **kwargs)
    ax.axhline(0, color="gray", linewidth=0.5, linestyle="--")
    ax.set_xlabel("Lattice site x")
    ax.set_ylabel("∇²ρ")
    ax.set_title(title)
    return ax


def plot_1d_triple(
    rho: np.ndarray,
    dx: float = 1.0,
    title: str = "1D ED State",
):
    """Three-panel plot: ρ(x), |∇ρ|, ∇²ρ."""
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
    plot_1d_density(rho, ax=axes[0], title="ρ(x)")
    plot_1d_gradient(rho, dx, ax=axes[1], title="|∇ρ|(x)")
    plot_1d_curvature(rho, dx, ax=axes[2], title="∇²ρ(x)")
    fig.suptitle(title, fontsize=14)
    plt.tight_layout()
    return fig, axes


# ============================================================
# 2D Visualization Hooks
# ============================================================

def plot_2d_density(
    rho: np.ndarray,
    ax=None,
    title: str = "Event Density ρ(x,y)",
    **kwargs,
):
    """Heatmap of ρ(x,y) for a 2D field."""
    import matplotlib.pyplot as plt
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 7))
    im = ax.imshow(rho.T, origin='lower', aspect='equal',
                   cmap='inferno', **kwargs)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(title)
    plt.colorbar(im, ax=ax, label="ρ")
    return ax


def plot_2d_gradient(
    rho: np.ndarray,
    dx: float = 1.0,
    ax=None,
    title: str = "|∇ρ|(x,y)",
    **kwargs,
):
    """Heatmap of gradient magnitude for a 2D field."""
    import matplotlib.pyplot as plt
    grad_mag = discrete_grad_magnitude(rho, dx, boundary="periodic")
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 7))
    im = ax.imshow(grad_mag.T, origin='lower', aspect='equal',
                   cmap='viridis', **kwargs)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(title)
    plt.colorbar(im, ax=ax, label="|∇ρ|")
    return ax


def plot_2d_horizon_candidates(
    rho: np.ndarray,
    rho_max: float,
    dx: float = 1.0,
    threshold: float = 0.9,
    ax=None,
    title: str = "Horizon Candidates (M(ρ) ≈ 0)",
    **kwargs,
):
    """Heatmap highlighting cells where ρ/ρ_max > threshold (near-saturation).

    These are horizon candidates: regions where mobility → 0.
    """
    import matplotlib.pyplot as plt
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 7))
    horizon_mask = (rho / rho_max) > threshold
    im = ax.imshow(horizon_mask.T.astype(float), origin='lower',
                   aspect='equal', cmap='Reds', vmin=0, vmax=1, **kwargs)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(title)
    plt.colorbar(im, ax=ax, label=f"ρ/ρ_max > {threshold}")
    return ax


def plot_2d_triple(
    rho: np.ndarray,
    rho_max: float = 100.0,
    dx: float = 1.0,
    title: str = "2D ED State",
):
    """Three-panel plot: ρ, |∇ρ|, horizon candidates."""
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))
    plot_2d_density(rho, ax=axes[0], title="ρ(x,y)")
    plot_2d_gradient(rho, dx, ax=axes[1], title="|∇ρ|(x,y)")
    plot_2d_horizon_candidates(rho, rho_max, dx, ax=axes[2])
    fig.suptitle(title, fontsize=14)
    plt.tight_layout()
    return fig, axes


# ============================================================
# Time Series Plots
# ============================================================

def plot_time_series(result: SimulationResult, save_path: str | None = None):
    """Multi-panel time series of all diagnostics.

    Panels:
    1. ρ̂(t) — mean density (thinning)
    2. G(t) — mean gradient (inflation decay)
    3. a(t) — scale factor proxy
    4. basins — structure count
    5. gradient energy
    6. thinning rate
    """
    import matplotlib.pyplot as plt

    ts = extract_time_series(result)
    if not ts:
        print("No diagnostic data to plot.")
        return

    fig, axes = plt.subplots(3, 2, figsize=(14, 12))

    panels = [
        ("rho_mean", "ρ̂(t) — Mean Density", "ρ̂"),
        ("grad_mean", "G(t) — Mean Gradient", "|∇ρ|"),
        ("scale_factor_proxy", "a(t) — Scale Factor Proxy", "1/G"),
        ("n_basins", "Structures (Local Minima)", "count"),
        ("grad_energy", "Gradient Energy Σ|∇ρ|²", "E_grad"),
        ("thinning_rate", "Thinning Rate Δ(Σρ)", "Δρ_total"),
    ]

    steps = ts["steps"]
    for ax, (key, title, ylabel) in zip(axes.flat, panels):
        ax.plot(steps, ts[key])
        ax.set_title(title)
        ax.set_ylabel(ylabel)
        ax.set_xlabel("Step")
        ax.grid(True, alpha=0.3)

    fig.suptitle("ED-Phys Simulation Diagnostics", fontsize=14)
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight')

    return fig, axes
