"""
plot_D_L_contours.py
====================
Final-L contour lines across the (n, σ) plane from the 4×4 Scenario-D sweep.

Design
------
    background : phase-exit surface at 35 % alpha (spatial context only)
    primary    : bold L-contour lines, clearly labelled
    grey field : no-exit region (L contours drawn everywhere; exit surface muted)

    x-axis  :  mobility exponent  n  = {0.5, 1.0, 2.0, 4.0}
    y-axis  :  noise amplitude    σ  = {0.01, 0.02, 0.05, 0.10}

Output
------
    results/phase2D/D_L_contours.png
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
OUT_PNG     = SCRIPT_DIR / "results" / "phase2D" / "D_L_contours.png"

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------

rows: list[dict] = []
with SUMMARY_CSV.open(encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rows.append({
            "n":       float(row["mobility_exp"]),
            "sigma":   float(row["noise_amp"]),
            "exit":    None if row["phase_exit_step"] == "None"
                            else int(row["phase_exit_step"]),
            "final_L": float(row["final_L"]),
        })

exponents = sorted({r["n"]     for r in rows})
sigmas    = sorted({r["sigma"] for r in rows})
nn, ns    = len(exponents), len(sigmas)

exit_grid    = np.full((ns, nn), np.nan)
L_grid       = np.full((ns, nn), np.nan)
no_exit_grid = np.zeros((ns, nn))

for r in rows:
    ci = exponents.index(r["n"])
    ri = sigmas.index(r["sigma"])
    L_grid[ri, ci] = r["final_L"]
    if r["exit"] is not None:
        exit_grid[ri, ci] = float(r["exit"])
    else:
        no_exit_grid[ri, ci] = 1.0

EXIT_FILL = np.where(np.isnan(exit_grid), 500.0, exit_grid)

# ---------------------------------------------------------------------------
# Interpolation (log-log, 160×160)
# ---------------------------------------------------------------------------

log_n   = np.log10(np.array(exponents, dtype=float))
log_sig = np.log10(np.array(sigmas,    dtype=float))
n_fine   = np.linspace(log_n.min(),   log_n.max(),   160)
sig_fine = np.linspace(log_sig.min(), log_sig.max(), 160)
NF, SF   = np.meshgrid(n_fine, sig_fine)
X_plot, Y_plot = 10**NF, 10**SF


def _interp(data: np.ndarray) -> np.ndarray:
    if _have_scipy:
        rgi = _RGI((log_sig, log_n), data,
                   method="linear", bounds_error=False, fill_value=None)
        return rgi(np.stack([SF.ravel(), NF.ravel()], axis=-1)).reshape(SF.shape)
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
L_interp    = _interp(L_grid)
mask_interp = _interp(no_exit_grid)
no_exit_rgn = mask_interp >= 0.50

exit_bg = np.ma.masked_where(no_exit_rgn, exit_interp)

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(8.2, 5.8))
fig.patch.set_facecolor("#f2f2f2")
ax.set_facecolor("#c8c8c8")   # matches no-exit grey

# ── 1. Phase-exit background at reduced alpha (context only) ───────────────
cmap_bg = mpl.colormaps["plasma_r"].copy()
cmap_bg.set_bad(color="#c8c8c8")

pcm = ax.pcolormesh(
    X_plot, Y_plot, exit_bg,
    cmap=cmap_bg,
    norm=mcolors.Normalize(vmin=84, vmax=416),
    shading="gouraud",
    alpha=0.32,          # heavily muted — just for spatial reference
    zorder=2,
)

# ── 2. L contour lines — primary visual element ────────────────────────────
LEVELS_L = [150, 300, 500, 750, 1000]

# choose a perceptually distinct palette for the L lines
L_colors = ["#1a1aff", "#0099cc", "#00bb55", "#cc7700", "#cc0000"]
#            L=150       L=300      L=500      L=750      L=1000

cl = ax.contour(
    X_plot, Y_plot, L_interp,
    levels=LEVELS_L,
    colors=L_colors,
    linewidths=2.2,
    zorder=5,
)

# label each contour with a clean white-backed box
fmt = {lv: f"L = {lv}" for lv in LEVELS_L}
labels = ax.clabel(
    cl,
    fmt=fmt,
    fontsize=9,
    inline=True,
    inline_spacing=6,
    use_clabeltext=True,
)
for lbl in labels:
    lbl.set_bbox(dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.80))
    lbl.set_fontweight("bold")

# ── 3. No-exit region border ───────────────────────────────────────────────
ax.contour(
    X_plot, Y_plot, mask_interp,
    levels=[0.499],
    colors=["#444444"],
    linewidths=[1.4],
    linestyles=["--"],
    zorder=6,
)
ax.contourf(
    X_plot, Y_plot, mask_interp,
    levels=[0.499, 1.5],
    hatches=["////"],
    colors="none",
    zorder=7,
)

# ── 4. Actual data-point markers ───────────────────────────────────────────
for r in rows:
    fc = "#888888" if r["exit"] is None else "white"
    ax.scatter(r["n"], r["sigma"],
               s=50, color=fc, edgecolors="#222222",
               linewidths=0.8, zorder=10)

# ── 5. Axes ────────────────────────────────────────────────────────────────
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
    "Scenario D  —  Final homogeneity scale  L\n"
    "n ∈ {0.5, 1, 2, 4}  ×  σ ∈ {0.01, 0.02, 0.05, 0.10}",
    fontsize=12, fontweight="bold", pad=12,
)

# ── 6. Colorbar for the muted background (labelled as "exit step context") ─
cbar = fig.colorbar(pcm, ax=ax, pad=0.025, fraction=0.046,
                    ticks=[84, 167, 250, 333, 416], alpha=1.0)
cbar.set_label("Phase-exit step  (background context)", fontsize=8.5)
cbar.ax.tick_params(labelsize=8)
# make the colorbar patch match the actual alpha-blended appearance
cbar.solids.set_alpha(0.32)

# ── 7. Legend for L lines ──────────────────────────────────────────────────
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

line_handles = [
    mlines.Line2D([], [], color=c, linewidth=2.2,
                  label=f"L = {lv}")
    for lv, c in zip(LEVELS_L, L_colors)
]
h_noexit = mpatches.Patch(
    facecolor="#c8c8c8", edgecolor="#444444",
    hatch="////", linewidth=0.8,
    label="No exit within 500 steps",
)
ax.legend(
    handles=line_handles + [h_noexit],
    loc="lower right",
    fontsize=8.5,
    framealpha=0.88,
    edgecolor="#aaaaaa",
    handlelength=2.0,
    title="Homogeneity scale",
    title_fontsize=8,
)

# ── 8. Save ────────────────────────────────────────────────────────────────
fig.tight_layout()
OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"Saved: {OUT_PNG}")
plt.close(fig)
