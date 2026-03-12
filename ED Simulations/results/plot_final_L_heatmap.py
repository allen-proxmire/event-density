"""
plot_final_L_heatmap.py
=======================
Reads results/phase2D/summary.csv and saves a final-L heatmap to
results/phase2D/final_L_heatmap.png.

Axes:
    x  --  noise_amp     [0.01, 0.02, 0.05, 0.10]
    y  --  mobility_exp  [0.5,  1.0,  2.0,  4.0 ]   (low n at bottom)

Color:
    Sequential "viridis" colormap — bright yellow = large L (more homogeneous
    / well-mixed field), dark purple = small L (persistent fine-scale structure).
"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR  = Path(__file__).parent
SUMMARY_CSV = SCRIPT_DIR / "results" / "phase2D" / "summary.csv"
OUT_PNG     = SCRIPT_DIR / "results" / "phase2D" / "final_L_heatmap.png"

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
            "final_L": float(row["final_L"]),
        })

exponents    = sorted({r["n"]     for r in rows})   # [0.5, 1.0, 2.0, 4.0]
noise_levels = sorted({r["noise"] for r in rows})   # [0.01, 0.02, 0.05, 0.10]

ny, nx = len(exponents), len(noise_levels)
L_grid = np.full((ny, nx), np.nan)

for r in rows:
    yi = exponents.index(r["n"])
    xi = noise_levels.index(r["noise"])
    L_grid[yi, xi] = r["final_L"]

# ---------------------------------------------------------------------------
# Colormap
# ---------------------------------------------------------------------------

vmin = float(np.nanmin(L_grid))
vmax = float(np.nanmax(L_grid))

cmap = mpl.colormaps["viridis"].copy()
norm = mcolors.Normalize(vmin=vmin, vmax=vmax)

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(7.0, 5.5))
fig.patch.set_facecolor("#f8f8f8")
ax.set_facecolor("#f8f8f8")

im = ax.imshow(
    L_grid,
    origin="lower",
    aspect="auto",
    cmap=cmap,
    norm=norm,
    interpolation="nearest",
    extent=[-0.5, nx - 0.5, -0.5, ny - 0.5],
    zorder=2,
)

# ---- cell annotations ----
for yi in range(ny):
    for xi in range(nx):
        val = L_grid[yi, xi]
        rgba = cmap(norm(val))
        lum  = 0.299 * rgba[0] + 0.587 * rgba[1] + 0.114 * rgba[2]
        color = "white" if lum < 0.55 else "#1a1a1a"
        ax.text(
            xi, yi, f"{val:.1f}",
            ha="center", va="center",
            fontsize=10, fontweight="bold", color=color,
            zorder=5,
        )

# ---- axes cosmetics ----
ax.set_xticks(range(nx))
ax.set_xticklabels([str(v) for v in noise_levels], fontsize=10)
ax.set_yticks(range(ny))
ax.set_yticklabels([str(v) for v in exponents], fontsize=10)

ax.set_xlabel("Noise amplitude  (noise_amp)", fontsize=11, labelpad=8)
ax.set_ylabel("Mobility exponent  (mobility_exp  n)", fontsize=11, labelpad=8)

ax.set_title(
    "Final homogeneity scale L  at step 500\nScenario D  (mobility + Langevin)",
    fontsize=13, fontweight="bold", pad=14,
)

# ---- grid lines ----
for x in np.arange(-0.5, nx, 1):
    ax.axvline(x, color="#aaaaaa", linewidth=0.6, zorder=1)
for y in np.arange(-0.5, ny, 1):
    ax.axhline(y, color="#aaaaaa", linewidth=0.6, zorder=1)
ax.set_xlim(-0.5, nx - 0.5)
ax.set_ylim(-0.5, ny - 0.5)

# ---- colorbar ----
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, pad=0.02, fraction=0.046)
cbar.set_label("L  (homogeneity scale = 1/G,  larger = smoother field)", fontsize=9)
cbar.ax.tick_params(labelsize=8)

# ---- layout & save ----
fig.tight_layout()
OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
print(f"Saved: {OUT_PNG}")
plt.close(fig)
