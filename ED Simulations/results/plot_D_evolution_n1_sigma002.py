"""
plot_D_evolution_n1_sigma002.py
================================
Re-runs Scenario D with n=1.0, σ=0.02 (same seed and params as the sweep)
and captures the ED field at steps 0, 50, 100, 200, 300, 400, 500.

Output
------
    results/phase2D/D_evolution_n1_sigma002.png   (2×4 grid, last cell empty)
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

mpl.use("Agg")

# ---------------------------------------------------------------------------
# Locate the simulation package
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from ED_Lattice import EDLattice, EDParams   # noqa: E402

# ---------------------------------------------------------------------------
# Simulation parameters  (identical to run_scenario_D defaults)
# ---------------------------------------------------------------------------

MOBILITY_EXP = 1.0
NOISE_AMP    = 0.02
SEED         = 77

params = EDParams(
    alpha=0.03,
    beta=0.20,
    gamma=0.5,
    dt=0.05,
    boundary="periodic",
    mode="mobility",
    noise_scale=NOISE_AMP,
    mobility_exp=MOBILITY_EXP,
)
lat = EDLattice(rows=64, cols=64, params=params, seed=SEED)
lat.init_random_noise(lo=0.3, hi=0.7)

# ---------------------------------------------------------------------------
# Capture field at target steps by running in segments
# ---------------------------------------------------------------------------

TARGET_STEPS = [0, 50, 100, 200, 300, 400, 500]

# step-0 snapshot before any integration
snapshots: dict[int, np.ndarray] = {0: lat.p.copy()}

# segment lengths between consecutive targets
prev = 0
for step in TARGET_STEPS[1:]:
    seg = step - prev
    lat.run(steps=seg)
    snapshots[step] = lat.p.copy()
    prev = step
    print(f"  Captured step {step:4d}  t={lat.time:6.2f}  "
          f"p_hat={lat.stats['p_hat']:.4f}  G={lat.stats['G']:.5f}")

# ---------------------------------------------------------------------------
# Global colour scale (consistent across all panels)
# ---------------------------------------------------------------------------

all_vals = np.concatenate([s.ravel() for s in snapshots.values()])
VMIN = float(all_vals.min())
VMAX = float(all_vals.max())
CMAP = "viridis"

# ---------------------------------------------------------------------------
# Figure:  2 rows × 4 cols  (7 panels + 1 empty for colourbar)
# ---------------------------------------------------------------------------

NCOLS, NROWS = 4, 2
fig, axes = plt.subplots(
    NROWS, NCOLS,
    figsize=(14.0, 7.8),
    gridspec_kw={"wspace": 0.06, "hspace": 0.28},
)
fig.patch.set_facecolor("#f0f0f0")

norm = mcolors.Normalize(vmin=VMIN, vmax=VMAX)

for idx, step in enumerate(TARGET_STEPS):
    row, col = divmod(idx, NCOLS)
    ax = axes[row, col]
    ax.set_facecolor("#181818")

    im = ax.imshow(
        snapshots[step],
        origin="lower",
        cmap=CMAP,
        norm=norm,
        aspect="equal",
        interpolation="nearest",
    )

    t_val = step * params.dt
    ax.set_title(
        f"step {step}   (t = {t_val:.2f})",
        fontsize=9.5, fontweight="bold", pad=5,
        color="#222222",
    )
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_linewidth(0.6)
        spine.set_edgecolor("#999999")

# ---------------------------------------------------------------------------
# Empty cell [1, 3]: turn it into the colourbar host
# ---------------------------------------------------------------------------

# hide the empty axes
empty_ax = axes[1, 3]
empty_ax.set_visible(False)

# place a colourbar axes inside the same grid cell
# get its bounding box in figure-fraction coordinates
pos = empty_ax.get_position()           # Bbox in figure coords
cb_left   = pos.x0 + pos.width  * 0.12
cb_bottom = pos.y0 + pos.height * 0.08
cb_width  = pos.width  * 0.25
cb_height = pos.height * 0.84

cbar_ax = fig.add_axes([cb_left, cb_bottom, cb_width, cb_height])
sm = plt.cm.ScalarMappable(cmap=CMAP, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, cax=cbar_ax)
cbar.set_label("ED density  ρ(x, y)", fontsize=9, labelpad=6)
cbar.ax.tick_params(labelsize=8)

# small descriptive text next to the colourbar
fig.text(
    pos.x0 + pos.width * 0.55,
    pos.y0 + pos.height * 0.50,
    f"n = {MOBILITY_EXP}\nσ = {NOISE_AMP}\nseed = {SEED}",
    ha="left", va="center",
    fontsize=8.5, color="#444444",
    linespacing=1.6,
)

# ---------------------------------------------------------------------------
# Supertitle
# ---------------------------------------------------------------------------

fig.suptitle(
    f"Scenario D  —  Time Evolution  (n = {MOBILITY_EXP},  σ = {NOISE_AMP})",
    fontsize=14, fontweight="bold", y=1.005,
)

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------

OUT = SCRIPT_DIR / "results" / "phase2D" / "D_evolution_n1_sigma002.png"
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"\nSaved: {OUT}")
plt.close(fig)
