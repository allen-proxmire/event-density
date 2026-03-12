"""
plot_D_phase_exit_surface.py
============================
Clean phase-exit surface figure from the 4×4 Scenario-D sweep.
No overlays — just the exit-step heatmap, axis labels, and colorbar.

    x-axis  :  mobility exponent  n  = {0.5, 1.0, 2.0, 4.0}
    y-axis  :  noise amplitude    σ  = {0.01, 0.02, 0.05, 0.10}
    color   :  phase-exit step  (plasma_r; no-exit cells in grey)

Output
------
    results/phase2D/D_phase_exit_surface.png
"""

from __future__ import annotations

import csv
import importlib
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.ticker as ticker
import numpy as np

_have_scipy = importlib.util.find_spec("scipy") is not None
if _have_scipy:
    from scipy.interpolate import RegularGridInterpolator as _RGI

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR  = Path(__file__).parent
SUMMARY_CSV = SCRIPT_DIR / "results" / "phase2D" / "summary.csv"
OUT_PNG     = SCRIPT_DIR / "results" / "phase2D" / "D_phase_exit_surface.png"

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------

rows: list[dict] = []
with SUMMARY_CSV.open(encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rows.append({
            "n":     float(row["mobility_exp"]),
            "sigma": float(row["noise_amp"]),
            "exit":  None if row["phase_exit_step"] == "None"
                          else int(row["phase_exit_step"]),
        })

exponents = sorted({r["n"]     for r in rows})   # x
sigmas    = sorted({r["sigma"] for r in rows})   # y
nn, ns    = len(exponents), len(sigmas)

# grid: rows=sigma (y), cols=n (x)
exit_grid    = np.full((ns, nn), np.nan)
no_exit_grid = np.zeros((ns, nn))

for r in rows:
    ci = exponents.index(r["n"])
    ri = sigmas.index(r["sigma"])
    if r["exit"] is not None:
        exit_grid[ri, ci] = float(r["exit"])
    else:
        no_exit_grid[ri, ci] = 1.0

# sentinel fill for interpolation
EXIT_FILL = np.where(np.isnan(exit_grid), 500.0, exit_grid)

# ---------------------------------------------------------------------------
# Interpolate to fine grid (log-log space)
# ---------------------------------------------------------------------------

log_n   = np.log10(np.array(exponents, dtype=float))
log_sig = np.log10(np.array(sigmas,    dtype=float))

n_fine   = np.linspace(log_n.min(),   log_n.max(),   160)
sig_fine = np.linspace(log_sig.min(), log_sig.max(), 160)
NF, SF   = np.meshgrid(n_fine, sig_fine)          # (160, 160)
X_plot, Y_plot = 10**NF, 10**SF


def _interp(data: np.ndarray) -> np.ndarray:
    if _have_scipy:
        rgi = _RGI((log_sig, log_n), data,
                   method="linear", bounds_error=False, fill_value=None)
        return rgi(np.stack([SF.ravel(), NF.ravel()], axis=-1)).reshape(SF.shape)
    # fallback bilinear
    out = np.empty(SF.shape)
    for i, ls in enumerate(sig_fine):
        for j, ln in enumerate(n_fine):
            ri0 = max(0, np.searchsorted(log_sig, ls) - 1)
            ri1 = min(ns - 1, ri0 + 1)
            ci0 = max(0, np.searchsorted(log_n,   ln) - 1)
            ci1 = min(nn - 1, ci0 + 1)
            if ri0 == ri1 or ci0 == ci1:
                out[i, j] = data[ri0, ci0]
            else:
                fr = (ls - log_sig[ri0]) / (log_sig[ri1] - log_sig[ri0])
                fc = (ln - log_n[ci0])   / (log_n[ci1]   - log_n[ci0])
                out[i, j] = ((1-fr)*(1-fc)*data[ri0,ci0]
                            +(1-fr)*fc    *data[ri0,ci1]
                            +fr    *(1-fc)*data[ri1,ci0]
                            +fr    *fc    *data[ri1,ci1])
    return out


exit_interp = _interp(EXIT_FILL)
mask_interp = _interp(no_exit_grid)
no_exit_rgn = mask_interp >= 0.50

# mask no-exit cells so they render as the colormap "bad" color (grey)
exit_plot = np.ma.masked_where(no_exit_rgn, exit_interp)

# ---------------------------------------------------------------------------
# Colormap: plasma_r with grey for masked (no-exit) cells
# ---------------------------------------------------------------------------

CMAP = mpl.colormaps["plasma_r"].copy()
CMAP.set_bad(color="#c8c8c8")
NORM = mcolors.Normalize(vmin=84, vmax=416)

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(8.0, 5.8))
fig.patch.set_facecolor("#f2f2f2")
ax.set_facecolor("#c8c8c8")      # background matches no-exit grey

pcm = ax.pcolormesh(
    X_plot, Y_plot, exit_plot,
    cmap=CMAP, norm=NORM,
    shading="gouraud",
)

# ---------------------------------------------------------------------------
# Axes (log scale, explicit tick labels)
# ---------------------------------------------------------------------------

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.38, 5.5)
ax.set_ylim(0.007, 0.14)

ax.set_xticks(exponents)
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{v:g}"))
ax.set_yticks(sigmas)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{v:g}"))
ax.tick_params(axis="both", which="both", labelsize=11)

ax.set_xlabel("Mobility exponent  n", fontsize=12, labelpad=8)
ax.set_ylabel("Noise amplitude  σ", fontsize=12, labelpad=8)
ax.set_title(
    "Scenario D  —  Phase-exit step surface\n"
    "n ∈ {0.5, 1, 2, 4}  ×  σ ∈ {0.01, 0.02, 0.05, 0.10}  "
    "(grey = no exit within 500 steps)",
    fontsize=12, fontweight="bold", pad=12,
)

# ---------------------------------------------------------------------------
# Colorbar
# ---------------------------------------------------------------------------

cbar = fig.colorbar(pcm, ax=ax, pad=0.025, fraction=0.046,
                    ticks=[84, 167, 250, 333, 416])
cbar.set_label(
    "Phase-exit step  (first step in phase 3-structure_formation)",
    fontsize=9,
)
cbar.ax.tick_params(labelsize=9)

# add a "no exit" swatch below the colorbar
cbar.ax.annotate(
    "grey = no exit",
    xy=(0.5, -0.07), xycoords="axes fraction",
    ha="center", va="top", fontsize=8, color="#555555",
)

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------

fig.tight_layout()
OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"Saved: {OUT_PNG}")
plt.close(fig)
