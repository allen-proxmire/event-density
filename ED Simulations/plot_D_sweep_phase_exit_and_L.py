"""
plot_D_sweep_phase_exit_and_L.py
=================================
Composite figure from the 4×4 Scenario-D mobility-noise sweep.

Layout
------
    x-axis  :  mobility exponent  n  = {0.5, 1.0, 2.0, 4.0}   (log scale)
    y-axis  :  noise amplitude    σ  = {0.01, 0.02, 0.05, 0.10} (log scale)
    fill    :  phase-exit step  (plasma_r, Gouraud-smooth pcolormesh)
    lines   :  final homogeneity scale L  (white contours, labelled)
    dots    :  gray  = data point that reached phase 3
               orange= data point that did NOT exit within 500 steps
    hatch   :  no-exit region (grey + diagonal hatch)
    ridge   :  saddle-ridge annotation if detectable on the interpolated surface

Note: the sweep used σ ∈ {0.01, 0.02, 0.05, 0.10}; these are the actual
grid values plotted on the y-axis regardless of what labels the caller uses.

Output
------
    results/phase2D/D_sweep_phase_exit_and_L.png
"""

from __future__ import annotations

import csv
import importlib
from pathlib import Path

import matplotlib as mpl
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.ticker as ticker
import numpy as np

_have_scipy = importlib.util.find_spec("scipy") is not None
if _have_scipy:
    from scipy.interpolate import RegularGridInterpolator as _RGI
    from scipy.ndimage import gaussian_filter as _gf
else:
    _RGI = None
    _gf  = None

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR  = Path(__file__).parent
SUMMARY_CSV = SCRIPT_DIR / "results" / "phase2D" / "summary.csv"
OUT_PNG     = SCRIPT_DIR / "results" / "phase2D" / "D_sweep_phase_exit_and_L.png"

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------

rows: list[dict] = []
with SUMMARY_CSV.open(encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append({
            "n":       float(row["mobility_exp"]),
            "sigma":   float(row["noise_amp"]),
            "exit":    None if row["phase_exit_step"] == "None"
                            else int(row["phase_exit_step"]),
            "final_L": float(row["final_L"]),
        })

# Sorted unique axis values
exponents   = sorted({r["n"]     for r in rows})   # [0.5, 1.0, 2.0, 4.0]
sigmas      = sorted({r["sigma"] for r in rows})   # [0.01, 0.02, 0.05, 0.10]
nn, ns      = len(exponents), len(sigmas)

# 2-D grids  (rows=sigma index, cols=n index)  — σ on y, n on x
exit_grid    = np.full((ns, nn), np.nan)
L_grid       = np.full((ns, nn), np.nan)
no_exit_grid = np.zeros((ns, nn))

for r in rows:
    ci = exponents.index(r["n"])      # column (x)
    ri = sigmas.index(r["sigma"])     # row    (y)
    L_grid[ri, ci] = r["final_L"]
    if r["exit"] is not None:
        exit_grid[ri, ci] = float(r["exit"])
    else:
        no_exit_grid[ri, ci] = 1.0

# Sentinel for no-exit cells during interpolation (just above real max=416)
EXIT_SENTINEL = 500.0
exit_fill = np.where(np.isnan(exit_grid), EXIT_SENTINEL, exit_grid)

# ---------------------------------------------------------------------------
# Interpolation in log-log space → 120×120 fine grid
# ---------------------------------------------------------------------------

log_n   = np.log10(np.array(exponents, dtype=float))  # x
log_sig = np.log10(np.array(sigmas,    dtype=float))  # y

n_fine   = np.linspace(log_n.min(),   log_n.max(),   120)
sig_fine = np.linspace(log_sig.min(), log_sig.max(), 120)

# MeshGrid: SigF = rows (y), NF = cols (x)
NF, SigF = np.meshgrid(n_fine, sig_fine)   # each (120, 120)
X_plot = 10 ** NF     # n values    (x)
Y_plot = 10 ** SigF   # sigma values(y)


def _interp2d(data: np.ndarray) -> np.ndarray:
    """
    Bilinear interpolation of a (ns × nn) array onto the (120×120) fine grid.
    data rows = sigma axis, data cols = n axis.
    """
    if _have_scipy:
        rgi = _RGI(
            (log_sig, log_n), data,
            method="linear", bounds_error=False, fill_value=None,
        )
        pts = np.stack([SigF.ravel(), NF.ravel()], axis=-1)
        return rgi(pts).reshape(SigF.shape)
    # Fallback: manual bilinear
    out = np.empty(SigF.shape)
    for i, ls in enumerate(sig_fine):
        for j, ln in enumerate(n_fine):
            ri0 = max(0, np.searchsorted(log_sig, ls) - 1)
            ri1 = min(ns - 1, ri0 + 1)
            ci0 = max(0, np.searchsorted(log_n, ln) - 1)
            ci1 = min(nn - 1, ci0 + 1)
            if ri0 == ri1 or ci0 == ci1:
                out[i, j] = data[ri0, ci0]
            else:
                fr = (ls - log_sig[ri0]) / (log_sig[ri1] - log_sig[ri0])
                fc = (ln - log_n[ci0])   / (log_n[ci1]   - log_n[ci0])
                out[i, j] = (
                    (1-fr)*(1-fc)*data[ri0, ci0]
                  + (1-fr)*fc   *data[ri0, ci1]
                  + fr   *(1-fc)*data[ri1, ci0]
                  + fr   *fc    *data[ri1, ci1]
                )
    return out


exit_interp = _interp2d(exit_fill)
L_interp    = _interp2d(L_grid)
mask_interp = _interp2d(no_exit_grid)

no_exit_region = mask_interp >= 0.50

# ---------------------------------------------------------------------------
# Saddle-ridge detection
# ---------------------------------------------------------------------------
# Work on the exited-region surface only (exclude no-exit sentinel values).
# Smooth lightly then look for a ridge = local max of |∇(exit)| projected
# perpendicular to the no-exit boundary.  We also locate the global max of
# exit_interp within the exited region as the "ridge peak".

exit_exited = np.where(no_exit_region, np.nan, exit_interp)

# Global max within exited region
valid_mask = ~np.isnan(exit_exited)
if valid_mask.any():
    peak_flat  = np.nanargmax(exit_exited)
    peak_i, peak_j = np.unravel_index(peak_flat, exit_exited.shape)
    peak_n   = X_plot[peak_i, peak_j]     # x-coord
    peak_sig = Y_plot[peak_i, peak_j]     # y-coord
    peak_val = int(np.nanmax(exit_exited))
    has_peak = True
else:
    has_peak = False

# Ridge line: contour of exit = peak_val - small_margin within exited region
RIDGE_LEVEL = peak_val - 20 if has_peak else None   # step just below peak

# ---------------------------------------------------------------------------
# Style constants
# ---------------------------------------------------------------------------

NOEXIT_COLOR  = "#cbcbcb"
CMAP_EXIT     = mpl.colormaps["plasma_r"]
EXIT_MIN, EXIT_MAX = 80.0, 420.0
NORM_EXIT     = mcolors.Normalize(vmin=EXIT_MIN, vmax=EXIT_MAX)
LEVELS_L      = [150, 300, 500, 750, 1000]
LEVELS_EXIT_LINES = [84, 167, 250, 333, 416]

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(9.2, 6.6))
fig.patch.set_facecolor("#f2f2f2")
ax.set_facecolor("#f2f2f2")

# ── 1. Smooth phase-exit fill (pcolormesh, Gouraud shading) ────────────────
pcm = ax.pcolormesh(
    X_plot, Y_plot, np.where(no_exit_region, np.nan, exit_interp),
    cmap=CMAP_EXIT, norm=NORM_EXIT,
    shading="gouraud",
    zorder=2,
)

# ── 2. Faint iso-step lines for reference ──────────────────────────────────
ax.contour(
    X_plot, Y_plot,
    np.where(no_exit_region, np.nan, exit_interp),
    levels=LEVELS_EXIT_LINES,
    colors=["#00000022"],
    linewidths=0.6,
    zorder=3,
)

# ── 3. No-exit region: grey fill + diagonal hatch ─────────────────────────
ax.contourf(
    X_plot, Y_plot, mask_interp,
    levels=[0.499, 1.5],
    colors=[NOEXIT_COLOR],
    zorder=4,
)
ax.contourf(
    X_plot, Y_plot, mask_interp,
    levels=[0.499, 1.5],
    hatches=["////"],
    colors="none",
    zorder=5,
)
# dashed boundary
ax.contour(
    X_plot, Y_plot, mask_interp,
    levels=[0.499],
    colors=["#444444"],
    linewidths=[1.6],
    linestyles=["--"],
    zorder=6,
)

# ── 4. Final-L contour lines (white, labelled) ────────────────────────────
cl = ax.contour(
    X_plot, Y_plot, L_interp,
    levels=LEVELS_L,
    colors="white",
    linewidths=1.4,
    linestyles="solid",
    alpha=0.92,
    zorder=7,
)
ax.clabel(
    cl,
    fmt=lambda v: f"L={int(v)}",
    fontsize=8.5,
    inline=True,
    inline_spacing=4,
    use_clabeltext=True,
)

# ── 5. Saddle-ridge contour (if found) ────────────────────────────────────
if has_peak and RIDGE_LEVEL is not None:
    ridge_surface = np.where(no_exit_region, np.nan, exit_interp)
    rc = ax.contour(
        X_plot, Y_plot, ridge_surface,
        levels=[RIDGE_LEVEL],
        colors=["#ffee55"],
        linewidths=[2.2],
        linestyles=["-."],
        zorder=8,
    )
    # Label the ridge contour
    ax.clabel(
        rc,
        fmt=f"ridge ≈ step {RIDGE_LEVEL}",
        fontsize=8, inline=True,
        use_clabeltext=True,
    )
    # Mark the peak point
    ax.scatter(
        [peak_n], [peak_sig],
        s=120, marker="*", color="#ffee55",
        edgecolors="#333333", linewidths=0.8,
        zorder=12,
        label=f"Ridge peak  (step {peak_val})",
    )
    ax.annotate(
        f"saddle\nridge peak\nstep {peak_val}",
        xy=(peak_n, peak_sig),
        xytext=(peak_n * 0.65, peak_sig * 1.55),
        fontsize=7.5, color="#ffee55",
        fontweight="bold",
        arrowprops=dict(
            arrowstyle="->", color="#ffee55", lw=1.2,
            connectionstyle="arc3,rad=0.25",
        ),
        bbox=dict(boxstyle="round,pad=0.3", fc="#333333", ec="#ffee55", alpha=0.80),
        zorder=13,
    )

# ── 6. Data points ────────────────────────────────────────────────────────
for r in rows:
    if r["exit"] is None:
        color, edge, marker, size, lbl = "#ff8c00", "#662200", "o", 80, None
    else:
        color, edge, marker, size, lbl = "#e0e0e0", "#222222", "o", 60, None
    ax.scatter(
        r["n"], r["sigma"],
        s=size, color=color, edgecolors=edge,
        linewidths=0.9, marker=marker,
        zorder=15,
    )

# ── 7. Axes ───────────────────────────────────────────────────────────────
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.38, 5.5)
ax.set_ylim(0.007, 0.14)

ax.set_xticks(exponents)
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{v:g}"))
ax.set_yticks(sigmas)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{v:g}"))
ax.tick_params(axis="both", which="both", labelsize=10.5)

ax.set_xlabel("Mobility exponent  n", fontsize=12, labelpad=8)
ax.set_ylabel("Noise amplitude  σ", fontsize=12, labelpad=8)
ax.set_title(
    "Scenario D  —  Phase-exit step & homogeneity scale L\n"
    "4×4 sweep: n ∈ {0.5, 1, 2, 4}  ×  σ ∈ {0.01, 0.02, 0.05, 0.10}",
    fontsize=12, fontweight="bold", pad=14,
)

# ── 8. Colorbar ───────────────────────────────────────────────────────────
cbar = fig.colorbar(
    pcm, ax=ax, pad=0.025, fraction=0.046,
    ticks=[84, 167, 250, 333, 416],
    extend="neither",
)
cbar.set_label(
    "Phase-exit step  (first step entering phase 3-structure_formation)",
    fontsize=9,
)
cbar.ax.tick_params(labelsize=8.5)

# ── 9. Legend ─────────────────────────────────────────────────────────────
h_exit = mlines.Line2D(
    [], [], marker="o", color="w",
    markerfacecolor="#e0e0e0", markeredgecolor="#222222",
    markersize=7, linewidth=0,
    label="Data point  —  phase 3 reached",
)
h_noexit_pt = mlines.Line2D(
    [], [], marker="o", color="w",
    markerfacecolor="#ff8c00", markeredgecolor="#662200",
    markersize=8, linewidth=0,
    label="Data point  —  no exit within 500 steps",
)
h_noexit_region = mpatches.Patch(
    facecolor=NOEXIT_COLOR, edgecolor="#444444",
    hatch="////", linewidth=0.8,
    label="No-exit region",
)
h_L = mlines.Line2D(
    [], [], color="white", linewidth=1.5,
    label="Final-L contour  (homogeneity scale)",
)
handles = [h_noexit_region, h_noexit_pt, h_exit, h_L]
if has_peak:
    h_ridge = mlines.Line2D(
        [], [], color="#ffee55", linewidth=2.0,
        linestyle="-.", label=f"Saddle ridge  (≈ step {RIDGE_LEVEL})",
    )
    handles.append(h_ridge)

ax.legend(
    handles=handles,
    loc="upper left",
    fontsize=8.5, framealpha=0.88,
    edgecolor="#aaaaaa",
    handlelength=2.0,
)

# ── 10. Save ──────────────────────────────────────────────────────────────
fig.tight_layout()
OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
print(f"Saved: {OUT_PNG}")
plt.close(fig)
