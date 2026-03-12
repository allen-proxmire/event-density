"""
plot_phase_exit_heatmap.py
==========================
Reads results/phase2D/summary.csv and saves a phase-exit heatmap to
results/phase2D/phase_exit_heatmap.png.

Axes:
    x  --  noise_amp     [0.01, 0.02, 0.05, 0.10]
    y  --  mobility_exp  [0.5,  1.0,  2.0,  4.0 ]   (low n at bottom)

Color:
    Cells where the run *did* exit to phase-3 are colored by phase_exit_step
    using a sequential colormap.  Cells where the run never exited are shown
    in a distinct "no-exit" color with a hatched pattern.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
import numpy as np

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR  = Path(__file__).parent
SUMMARY_CSV = SCRIPT_DIR / "results" / "phase2D" / "summary.csv"
OUT_PNG     = SCRIPT_DIR / "results" / "phase2D" / "phase_exit_heatmap.png"

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------

rows: list[dict] = []
with SUMMARY_CSV.open(encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append({
            "n":     float(row["mobility_exp"]),
            "noise": float(row["noise_amp"]),
            "exit":  None if row["phase_exit_step"] == "None" else int(row["phase_exit_step"]),
        })

exponents    = sorted({r["n"]     for r in rows})   # [0.5, 1.0, 2.0, 4.0]
noise_levels = sorted({r["noise"] for r in rows})   # [0.01, 0.02, 0.05, 0.10]

# Build 2-D arrays  (rows = n index, cols = noise index)
ny, nx = len(exponents), len(noise_levels)
exit_grid = np.full((ny, nx), np.nan)   # NaN  =>  no-exit cell

for r in rows:
    yi = exponents.index(r["n"])
    xi = noise_levels.index(r["noise"])
    if r["exit"] is not None:
        exit_grid[yi, xi] = r["exit"]

# ---------------------------------------------------------------------------
# Colormap: "exited" cells use plasma; "no-exit" cells drawn separately
# ---------------------------------------------------------------------------

NOEXIT_COLOR = "#d0d0d0"          # light grey for masked cells
HATCH        = "////"             # diagonal hatch for no-exit

valid_exits = exit_grid[np.isfinite(exit_grid)]
vmin = float(valid_exits.min()) if valid_exits.size else 0.0
vmax = float(valid_exits.max()) if valid_exits.size else 500.0

cmap_base = mpl.colormaps["plasma_r"].copy()
norm      = mcolors.Normalize(vmin=vmin, vmax=vmax)

# Masked array: NaN positions won't be drawn by imshow
masked = np.ma.masked_where(np.isnan(exit_grid), exit_grid)

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(7.0, 5.5))
fig.patch.set_facecolor("#f8f8f8")
ax.set_facecolor("#f8f8f8")

# ---- draw "exited" cells ----
im = ax.imshow(
    masked,
    origin="lower",
    aspect="auto",
    cmap=cmap_base,
    norm=norm,
    interpolation="nearest",
    extent=[-0.5, nx - 0.5, -0.5, ny - 0.5],
    zorder=2,
)

# ---- draw "no-exit" cells (grey + hatch) ----
for yi in range(ny):
    for xi in range(nx):
        if np.isnan(exit_grid[yi, xi]):
            rect = mpatches.FancyBboxPatch(
                (xi - 0.5, yi - 0.5), 1.0, 1.0,
                boxstyle="square,pad=0",
                facecolor=NOEXIT_COLOR,
                edgecolor="#888888",
                hatch=HATCH,
                linewidth=0.8,
                zorder=3,
            )
            ax.add_patch(rect)

# ---- cell annotations ----
for yi in range(ny):
    for xi in range(nx):
        val = exit_grid[yi, xi]
        if np.isnan(val):
            txt   = "no exit"
            color = "#555555"
            fw    = "normal"
            fs    = 8
        else:
            txt   = f"step {int(val)}"
            # pick white or black depending on background lightness
            rgba  = cmap_base(norm(val))
            lum   = 0.299 * rgba[0] + 0.587 * rgba[1] + 0.114 * rgba[2]
            color = "white" if lum < 0.55 else "#1a1a1a"
            fw    = "bold"
            fs    = 9
        ax.text(
            xi, yi, txt,
            ha="center", va="center",
            fontsize=fs, fontweight=fw, color=color,
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
    "Phase-exit step:  Scenario D  (mobility + Langevin)",
    fontsize=13, fontweight="bold", pad=14,
)

# ---- grid lines between cells ----
for x in np.arange(-0.5, nx, 1):
    ax.axvline(x, color="#aaaaaa", linewidth=0.6, zorder=1)
for y in np.arange(-0.5, ny, 1):
    ax.axhline(y, color="#aaaaaa", linewidth=0.6, zorder=1)
ax.set_xlim(-0.5, nx - 0.5)
ax.set_ylim(-0.5, ny - 0.5)

# ---- colorbar ----
sm = plt.cm.ScalarMappable(cmap=cmap_base, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, pad=0.02, fraction=0.046)
cbar.set_label("Phase-exit step (first step in phase 3)", fontsize=9)
cbar.ax.tick_params(labelsize=8)

# ---- legend patch for no-exit ----
no_exit_patch = mpatches.Patch(
    facecolor=NOEXIT_COLOR, edgecolor="#888888",
    hatch=HATCH, label="Did not reach phase 3 within 500 steps",
)
ax.legend(
    handles=[no_exit_patch],
    loc="upper left",
    fontsize=8,
    framealpha=0.85,
    edgecolor="#aaaaaa",
)

# ---- layout & save ----
fig.tight_layout()
OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
print(f"Saved: {OUT_PNG}")
plt.close(fig)
