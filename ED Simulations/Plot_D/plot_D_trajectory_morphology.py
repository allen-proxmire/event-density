"""
plot_D_trajectory_morphology.py
================================
4-panel trajectory-morphology figure from the Scenario-D sweep.

One representative run per regime is re-simulated to its mid-evolution step:

  Panel A  Hyper-coherent     n=0.5, σ=0.01  t=42   (exit//2,  exit=84)
  Panel B  Stable-coherent    n=1.0, σ=0.02  t=83   (exit//2,  exit=167)
  Panel C  Marginal / saddle  n=2.0, σ=0.05  t=208  (exit//2,  exit=416)
  Panel D  Non-individuating  n=1.0, σ=0.10  t=250  (fixed mid, no exit)

Each panel shows:
  • viridis heatmap of the ED density field ρ(x,y)
  • White quiver arrows showing the local gradient ∇ρ (flow toward density peaks)
  • Regime label and (n, σ, t) annotation

All panels share a single colorbar (global vmin/vmax across the four fields).

Simulation parameters (identical to Phase2D sweep)
---------------------------------------------------
  alpha=0.03, beta=0.20, gamma=0.5, dt=0.05
  boundary='periodic', mode='mobility', seed=77
  init: init_random_noise(lo=0.3, hi=0.7)

Output
------
    results/phase2D/D_trajectory_morphology.png
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from ED_Lattice import EDLattice, EDParams

OUT_PNG = SCRIPT_DIR / "results" / "phase2D" / "D_trajectory_morphology.png"

# ---------------------------------------------------------------------------
# Run definitions — one per regime
# ---------------------------------------------------------------------------

RUNS = [
    dict(
        label      = "Hyper-coherent",
        n          = 0.5,
        sigma      = 0.01,
        exit_step  = 84,
        mid_step   = 42,      # 84 // 2
    ),
    dict(
        label      = "Stable-coherent",
        n          = 1.0,
        sigma      = 0.02,
        exit_step  = 167,
        mid_step   = 83,      # 167 // 2
    ),
    dict(
        label      = "Marginal / saddle",
        n          = 2.0,
        sigma      = 0.05,
        exit_step  = 416,
        mid_step   = 208,     # 416 // 2
    ),
    dict(
        label      = "Non-individuating",
        n          = 1.0,
        sigma      = 0.10,
        exit_step  = None,
        mid_step   = 250,     # fixed mid-point (no exit)
    ),
]

# Regime accent colours (match D_regime_map.png)
REGIME_COLORS = {
    "Hyper-coherent":    "#2563eb",
    "Stable-coherent":   "#16a34a",
    "Marginal / saddle": "#d97706",
    "Non-individuating": "#6b7280",
}

# ---------------------------------------------------------------------------
# Simulate each run to its mid-step and capture the field
# ---------------------------------------------------------------------------

def _build_lattice(n: float, sigma: float) -> EDLattice:
    """Reproduce the exact EDLattice construction used in the Phase2D sweep."""
    params = EDParams(
        alpha        = 0.03,
        beta         = 0.20,
        gamma        = 0.5,
        dt           = 0.05,
        boundary     = "periodic",
        mode         = "mobility",
        noise_scale  = sigma,
        mobility_exp = n,
    )
    lat = EDLattice(rows=64, cols=64, params=params, seed=77)
    lat.init_random_noise(lo=0.3, hi=0.7)
    return lat


fields: list[np.ndarray] = []
for run in RUNS:
    print(f"  Simulating  {run['label']:22s}  n={run['n']}, s={run['sigma']} "
          f" -> t={run['mid_step']} ...")
    lat = _build_lattice(run["n"], run["sigma"])
    lat.run(steps=run["mid_step"])
    fields.append(lat.p.copy())
    s = lat.stats
    print(f"    G={s['G']:.5f}  L={s['L']:.1f}  phase={s['phase']}")

# ---------------------------------------------------------------------------
# Global colour range (shared across all four panels)
# ---------------------------------------------------------------------------

vmin = min(f.min() for f in fields)
vmax = max(f.max() for f in fields)
print(f"\n  Global field range: [{vmin:.4f}, {vmax:.4f}]")

# ---------------------------------------------------------------------------
# Helper: quiver overlay
# ---------------------------------------------------------------------------

STRIDE  = 5          # arrow grid spacing in pixels
Q_SCALE = 1.0 / (STRIDE * 0.38)   # scale so max arrow ≈ stride × 0.38 data-units


def _add_quiver(ax: plt.Axes, field: np.ndarray) -> None:
    """
    Overlay ∇ρ gradient arrows on *ax* (imshow coordinate system).

    Steps:
      1. Compute (gy, gx) = np.gradient(field) — gy along rows, gx along cols
      2. Sample on a strided sub-grid offset by stride//2 to avoid edges
      3. Normalise by the panel-local maximum gradient magnitude
      4. Plot with scale_units='xy' so arrow length is in data units
    """
    gy, gx = np.gradient(field)

    offs    = STRIDE // 2
    q_rows  = np.arange(offs, field.shape[0], STRIDE)
    q_cols  = np.arange(offs, field.shape[1], STRIDE)
    QC, QR  = np.meshgrid(q_cols, q_rows)       # x=col, y=row (imshow coords)

    u = gx[offs::STRIDE, offs::STRIDE]           # col-gradient → x-direction
    v = gy[offs::STRIDE, offs::STRIDE]           # row-gradient → y-direction

    # Trim to match meshgrid shape (in case array isn't evenly divisible)
    nr, nc = QC.shape
    u = u[:nr, :nc]
    v = v[:nr, :nc]

    # Per-panel normalisation: longest arrow = 1.0 unit
    mag_max = np.hypot(u, v).max()
    if mag_max > 1e-10:
        u = u / mag_max
        v = v / mag_max

    ax.quiver(
        QC, QR, u, v,
        color       = "white",
        alpha       = 0.68,
        scale       = Q_SCALE,
        scale_units = "xy",
        pivot       = "mid",
        headwidth   = 3.2,
        headlength  = 4.0,
        headaxislength = 3.5,
        zorder      = 5,
    )


# ---------------------------------------------------------------------------
# Figure  2×2 + colorbar
# ---------------------------------------------------------------------------

FIG_BG   = "#1a1a1a"
PANEL_BG = "#0d0d0d"

fig = plt.figure(figsize=(11.2, 9.8))
fig.patch.set_facecolor(FIG_BG)

gs = gridspec.GridSpec(
    2, 3,
    figure      = fig,
    width_ratios = [1, 1, 0.055],
    wspace      = 0.08,
    hspace      = 0.16,
    left        = 0.04,
    right       = 0.96,
    top         = 0.90,
    bottom      = 0.05,
)
panel_axes = [
    fig.add_subplot(gs[0, 0]),
    fig.add_subplot(gs[0, 1]),
    fig.add_subplot(gs[1, 0]),
    fig.add_subplot(gs[1, 1]),
]
cax = fig.add_subplot(gs[:, 2])

# ---------------------------------------------------------------------------
# Render each panel
# ---------------------------------------------------------------------------

for ax, run, field in zip(panel_axes, RUNS, fields):
    ax.set_facecolor(PANEL_BG)
    color = REGIME_COLORS[run["label"]]

    # ── Field heatmap ──────────────────────────────────────────────────
    ax.imshow(
        field,
        cmap          = "viridis",
        vmin          = vmin,
        vmax          = vmax,
        origin        = "upper",
        interpolation = "nearest",
        aspect        = "auto",
    )

    # ── Gradient quiver ────────────────────────────────────────────────
    _add_quiver(ax, field)

    # ── Regime label (top, accent colour) ─────────────────────────────
    ax.text(
        0.50, 0.975,
        run["label"],
        transform  = ax.transAxes,
        fontsize   = 11,
        fontweight = "bold",
        color      = color,
        ha         = "center",
        va         = "top",
        bbox       = dict(
            boxstyle    = "round,pad=0.28",
            fc          = PANEL_BG,
            ec          = color,
            alpha       = 0.88,
            linewidth   = 1.6,
        ),
        zorder = 8,
    )

    # ── Parameter + step annotation (bottom) ──────────────────────────
    if run["exit_step"] is not None:
        detail = f"exit step = {run['exit_step']}"
    else:
        detail = "no exit within 500 steps"

    ax.text(
        0.50, 0.025,
        f"n = {run['n']},  σ = {run['sigma']}   ·   t = {run['mid_step']}  ({detail})",
        transform  = ax.transAxes,
        fontsize   = 7.8,
        color      = "white",
        ha         = "center",
        va         = "bottom",
        bbox       = dict(
            boxstyle  = "round,pad=0.22",
            fc        = PANEL_BG,
            ec        = "#555555",
            alpha     = 0.80,
        ),
        zorder = 8,
    )

    # ── Spine colour → regime colour ───────────────────────────────────
    for spine in ax.spines.values():
        spine.set_edgecolor(color)
        spine.set_linewidth(2.2)

    ax.set_xticks([])
    ax.set_yticks([])

# ---------------------------------------------------------------------------
# Shared colorbar
# ---------------------------------------------------------------------------

sm = mpl.cm.ScalarMappable(
    cmap = mpl.cm.viridis,
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax),
)
sm.set_array([])

cb = fig.colorbar(sm, cax=cax)
cb.set_label("ED density  ρ", color="white", fontsize=10, labelpad=10)
cb.ax.yaxis.set_tick_params(color="white", labelsize=8)
plt.setp(cb.ax.yaxis.get_ticklabels(), color="white")
cb.outline.set_edgecolor("#555555")

# ---------------------------------------------------------------------------
# Figure-level title and subtitle
# ---------------------------------------------------------------------------

fig.text(
    0.47, 0.955,
    "Scenario D  —  Trajectory Morphology at Mid-Phase",
    ha         = "center",
    va         = "bottom",
    fontsize   = 13,
    fontweight = "bold",
    color      = "white",
)
fig.text(
    0.47, 0.924,
    "Background: ED density field ρ(x,y)   ·   Arrows: ∇ρ gradient flow (toward density peaks)",
    ha       = "center",
    va       = "bottom",
    fontsize = 8.5,
    color    = "#aaaaaa",
)

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------

OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(
    OUT_PNG,
    dpi         = 150,
    bbox_inches = "tight",
    facecolor   = fig.get_facecolor(),
)
print(f"\nSaved: {OUT_PNG}")
plt.close(fig)
