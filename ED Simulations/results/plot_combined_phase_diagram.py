"""
plot_combined_phase_diagram.py
==============================
Combines the 4×4 sweep data into a single contour-style phase diagram:

    • Filled contours  — phase-exit step (plasma_r colormap)
    • Contour lines    — final homogeneity scale L (white, labelled)
    • Hatched region   — cells that never exited to phase 3 within 500 steps

Axes use log scale; the 4×4 grid is bilinearly interpolated in log-log
space to 100×100 for smooth contour rendering.

Output:
    results/phase2D/combined_phase_diagram.png
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

# scipy is optional — fall back to numpy bilinear if unavailable
_have_scipy = importlib.util.find_spec("scipy") is not None
if _have_scipy:
    from scipy.interpolate import RegularGridInterpolator as _RGI
else:
    _RGI = None  # handled below

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR  = Path(__file__).parent
SUMMARY_CSV = SCRIPT_DIR / "results" / "phase2D" / "summary.csv"
OUT_PNG     = SCRIPT_DIR / "results" / "phase2D" / "combined_phase_diagram.png"

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------

rows: list[dict] = []
with SUMMARY_CSV.open(encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append({
            "n":       float(row["mobility_exp"]),
            "noise":   float(row["noise_amp"]),
            "exit":    None if row["phase_exit_step"] == "None"
                            else int(row["phase_exit_step"]),
            "final_L": float(row["final_L"]),
        })

exponents    = sorted({r["n"]     for r in rows})   # [0.5, 1.0, 2.0, 4.0]
noise_levels = sorted({r["noise"] for r in rows})   # [0.01, 0.02, 0.05, 0.10]
ny, nx = len(exponents), len(noise_levels)

exit_grid    = np.full((ny, nx), np.nan)
L_grid       = np.full((ny, nx), np.nan)
no_exit_grid = np.zeros((ny, nx))          # 1 = no-exit, 0 = exited

for r in rows:
    yi = exponents.index(r["n"])
    xi = noise_levels.index(r["noise"])
    L_grid[yi, xi] = r["final_L"]
    if r["exit"] is not None:
        exit_grid[yi, xi] = float(r["exit"])
    else:
        no_exit_grid[yi, xi] = 1.0

# Sentinel value for no-exit cells during interpolation (above real max=416)
EXIT_SENTINEL = 500.0
exit_fill = np.where(np.isnan(exit_grid), EXIT_SENTINEL, exit_grid)

# ---------------------------------------------------------------------------
# Interpolation helpers
# ---------------------------------------------------------------------------

log_n     = np.log10(np.array(exponents,    dtype=float))
log_noise = np.log10(np.array(noise_levels, dtype=float))

# Fine grid: 120×120 in log-log space
n_fine     = np.linspace(log_n.min(),     log_n.max(),     120)
noise_fine = np.linspace(log_noise.min(), log_noise.max(), 120)
NN, NoiseF = np.meshgrid(n_fine, noise_fine, indexing="ij")   # (120, 120)
X_plot = 10 ** NoiseF   # noise on x-axis
Y_plot = 10 ** NN       # n on y-axis


def _interp(data: np.ndarray) -> np.ndarray:
    """Bilinear interpolation in log-log space onto the fine grid."""
    if _have_scipy:
        rgi = _RGI(
            (log_n, log_noise), data,
            method="linear", bounds_error=False, fill_value=None,
        )
        pts = np.stack([NN.ravel(), NoiseF.ravel()], axis=-1)
        return rgi(pts).reshape(NN.shape)
    else:
        # Manual bilinear via numpy
        out = np.empty(NN.shape)
        for i, ln in enumerate(n_fine):
            for j, lno in enumerate(noise_fine):
                # find surrounding indices
                yi0 = max(0, np.searchsorted(log_n, ln) - 1)
                yi1 = min(len(log_n) - 1, yi0 + 1)
                xi0 = max(0, np.searchsorted(log_noise, lno) - 1)
                xi1 = min(len(log_noise) - 1, xi0 + 1)
                if yi0 == yi1 or xi0 == xi1:
                    # on the boundary: nearest
                    out[i, j] = data[yi0, xi0]
                else:
                    fy = (ln  - log_n[yi0])     / (log_n[yi1]     - log_n[yi0])
                    fx = (lno - log_noise[xi0]) / (log_noise[xi1] - log_noise[xi0])
                    out[i, j] = (
                        (1-fy)*(1-fx)*data[yi0, xi0]
                      + (1-fy)*fx   *data[yi0, xi1]
                      + fy   *(1-fx)*data[yi1, xi0]
                      + fy   *fx    *data[yi1, xi1]
                    )
        return out


exit_interp    = _interp(exit_fill)
L_interp       = _interp(L_grid)
mask_interp    = _interp(no_exit_grid)

# No-exit region: interpolated mask > 0.5
no_exit_region = mask_interp >= 0.50

# Keep exit_interp unmasked — the no-exit overlay drawn on top will cover those cells
exit_plot = exit_interp

# ---------------------------------------------------------------------------
# Colormap & levels
# ---------------------------------------------------------------------------

NOEXIT_COLOR = "#d0cece"

# Phase-exit levels: anchor to actual distinct values, clip range exactly at data min/max
LEVELS_EXIT = [84, 120, 167, 210, 250, 290, 333, 375, 416]
CMAP_EXIT   = mpl.colormaps["plasma_r"]
NORM_EXIT   = mcolors.Normalize(vmin=84, vmax=416)

# Final-L contour levels (log-spaced to cover ~92–1063)
LEVELS_L = [150, 250, 400, 600, 900]

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(9.0, 6.4))
fig.patch.set_facecolor("#f4f4f4")
ax.set_facecolor("#f4f4f4")

# ── filled phase-exit contours ─────────────────────────────────────────────
# pcolormesh gives smooth Gouraud-interpolated fill without level-boundary artefacts
pcm = ax.pcolormesh(
    X_plot, Y_plot, exit_plot,
    cmap=CMAP_EXIT, norm=NORM_EXIT,
    shading="gouraud",
    zorder=2,
)
# Thin phase-exit iso-lines at the actual discrete values
ax.contour(
    X_plot, Y_plot, exit_plot,
    levels=LEVELS_EXIT,
    colors=["#00000030"],
    linewidths=0.5,
    zorder=2,
)

# ── no-exit: solid grey fill ───────────────────────────────────────────────
ax.contourf(
    X_plot, Y_plot, mask_interp,
    levels=[0.499, 1.5],
    colors=[NOEXIT_COLOR],
    zorder=3,
)
# hatch overlay (separate contourf call; colors='none' keeps fill transparent)
ax.contourf(
    X_plot, Y_plot, mask_interp,
    levels=[0.499, 1.5],
    hatches=["////"],
    colors="none",
    zorder=4,
)
# dashed boundary around no-exit region
ax.contour(
    X_plot, Y_plot, mask_interp,
    levels=[0.499],
    colors=["#555555"],
    linewidths=[1.8],
    linestyles=["--"],
    zorder=5,
)

# ── final-L contour lines ──────────────────────────────────────────────────
cl = ax.contour(
    X_plot, Y_plot, L_interp,
    levels=LEVELS_L,
    colors="white",
    linewidths=1.3,
    linestyles="solid",
    alpha=0.90,
    zorder=6,
)
ax.clabel(
    cl, fmt=lambda v: f"L={int(v)}",
    fontsize=8.5, inline=True, inline_spacing=5,
    use_clabeltext=True,
)

# ── data points ───────────────────────────────────────────────────────────
for r in rows:
    fc = "#555555" if r["exit"] is None else "white"
    ax.scatter(
        r["noise"], r["n"],
        s=55, color=fc, edgecolors="#111111",
        linewidths=0.9, zorder=10, marker="o",
    )

# ── axes (log scale) ──────────────────────────────────────────────────────
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.0075, 0.14)
ax.set_ylim(0.37, 5.2)

ax.set_xticks(noise_levels)
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{v:g}"))
ax.set_yticks(exponents)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{v:g}"))
ax.tick_params(axis="both", which="both", labelsize=10)

ax.set_xlabel("Noise amplitude  σ  (noise_amp)", fontsize=12, labelpad=8)
ax.set_ylabel("Mobility exponent  n  (mobility_exp)", fontsize=12, labelpad=8)
ax.set_title(
    "Scenario D  –  Phase-exit step (filled) & final homogeneity scale L (lines)\n"
    "mobility + Langevin  |  4×4 parameter sweep, bilinear interpolation",
    fontsize=12, fontweight="bold", pad=14,
)

# ── colorbar ──────────────────────────────────────────────────────────────
cbar = fig.colorbar(pcm, ax=ax, pad=0.025, fraction=0.046,
                    ticks=[84, 167, 250, 333, 416])
cbar.set_label(
    "Phase-exit step  (first step in phase 3-structure_formation)",
    fontsize=9,
)
cbar.ax.tick_params(labelsize=8)

# ── legend ────────────────────────────────────────────────────────────────
h_noexit = mpatches.Patch(
    facecolor=NOEXIT_COLOR, edgecolor="#555555",
    hatch="////", linewidth=0.8,
    label="No exit within 500 steps",
)
h_Lline = mlines.Line2D(
    [], [], color="white", linewidth=1.5,
    label="Final-L contour  (homogeneity scale)",
)
h_pt_exit = mlines.Line2D(
    [], [], marker="o", color="w",
    markerfacecolor="white", markeredgecolor="#111111",
    markersize=7, linewidth=0,
    label="Data point  (phase 3 reached)",
)
h_pt_no = mlines.Line2D(
    [], [], marker="o", color="w",
    markerfacecolor="#555555", markeredgecolor="#111111",
    markersize=7, linewidth=0,
    label="Data point  (no exit)",
)
ax.legend(
    handles=[h_noexit, h_Lline, h_pt_exit, h_pt_no],
    loc="lower left",
    fontsize=8.5,
    framealpha=0.88,
    edgecolor="#aaaaaa",
    handlelength=2.2,
)

# ── save ──────────────────────────────────────────────────────────────────
fig.tight_layout()
OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
print(f"Saved: {OUT_PNG}")
plt.close(fig)
