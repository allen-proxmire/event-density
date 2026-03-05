"""
plot_D_regime_map.py
====================
Regime-classification figure from the 4×4 Scenario-D sweep.

Classification rules (applied in order):
  4  Non-individuating  : exit_step is None  — no coherent structure within 500 steps
  1  Hyper-coherent     : exit_step ≤ 100    — near-instant phase transition, very high L
  3  Marginal / saddle  : exit_step > 300    — sluggish transition, near no-exit boundary
  2  Stable-coherent    : 100 < exit ≤ 300   — reliable structure formation

The background is a Voronoi (nearest-neighbour) partition of the log-log
parameter plane, illustrating how the regimes would extend between samples.
Actual data points are overlaid with regime-specific markers and per-cell
annotations showing (exit step, final L).

Output
------
    results/phase2D/D_regime_map.png
"""

from __future__ import annotations

import csv
import importlib
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
import numpy as np

_have_scipy = importlib.util.find_spec("scipy") is not None
if _have_scipy:
    from scipy.spatial import cKDTree

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR  = Path(__file__).parent
SUMMARY_CSV = SCRIPT_DIR / "results" / "phase2D" / "summary.csv"
OUT_PNG     = SCRIPT_DIR / "results" / "phase2D" / "D_regime_map.png"

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

# ---------------------------------------------------------------------------
# Classify each cell
# ---------------------------------------------------------------------------

HYPER_THRESH    = 100    # exit_step ≤ this → Hyper-coherent
MARGINAL_THRESH = 300    # exit_step > this (but not None) → Marginal/saddle


def _classify(exit_step, final_L) -> int:
    if exit_step is None:
        return 4                         # Non-individuating
    if exit_step <= HYPER_THRESH:
        return 1                         # Hyper-coherent
    if exit_step > MARGINAL_THRESH:
        return 3                         # Marginal / saddle
    return 2                             # Stable-coherent


for r in rows:
    r["regime"] = _classify(r["exit"], r["final_L"])

# ---------------------------------------------------------------------------
# Grid setup (log-log)
# ---------------------------------------------------------------------------

exponents = sorted({r["n"]     for r in rows})   # [0.5, 1.0, 2.0, 4.0]
sigmas    = sorted({r["sigma"] for r in rows})   # [0.01, 0.02, 0.05, 0.10]

log_n   = np.log10(np.array(exponents, dtype=float))
log_sig = np.log10(np.array(sigmas,    dtype=float))

# Fine grid for Voronoi background
N_FINE = 300
n_fine   = np.linspace(log_n.min(),   log_n.max(),   N_FINE)
sig_fine = np.linspace(log_sig.min(), log_sig.max(), N_FINE)
NF, SF   = np.meshgrid(n_fine, sig_fine)
X_plot, Y_plot = 10**NF, 10**SF

# ---------------------------------------------------------------------------
# Voronoi (nearest-neighbour) fill
# ---------------------------------------------------------------------------

pt_log_n   = np.array([np.log10(r["n"])     for r in rows])
pt_log_sig = np.array([np.log10(r["sigma"]) for r in rows])
pt_regime  = np.array([r["regime"]          for r in rows], dtype=float)

query_pts = np.column_stack([NF.ravel(), SF.ravel()])

if _have_scipy:
    tree = cKDTree(np.column_stack([pt_log_n, pt_log_sig]))
    _, idx = tree.query(query_pts)
else:
    # Manual fallback: argmin Euclidean distance in log-log space
    idx = np.array([
        np.argmin((pt_log_n - qn)**2 + (pt_log_sig - qs)**2)
        for qn, qs in query_pts
    ])

regime_map = pt_regime[idx].reshape(NF.shape)

# ---------------------------------------------------------------------------
# Colour scheme  (regime 1..4)
# ---------------------------------------------------------------------------

REGIME_COLORS = {
    1: "#2563eb",   # Hyper-coherent      — strong blue
    2: "#16a34a",   # Stable-coherent     — forest green
    3: "#d97706",   # Marginal / saddle   — amber
    4: "#9ca3af",   # Non-individuating   — cool grey
}
REGIME_NAMES = {
    1: "Hyper-coherent",
    2: "Stable-coherent",
    3: "Marginal / saddle",
    4: "Non-individuating",
}
REGIME_DESC = {
    1: f"exit ≤ {HYPER_THRESH} steps",
    2: f"{HYPER_THRESH} < exit ≤ {MARGINAL_THRESH}",
    3: f"exit > {MARGINAL_THRESH} steps",
    4: "no exit within 500 steps",
}
REGIME_MARKERS = {1: "D", 2: "o", 3: "^", 4: "X"}
REGIME_EDGE    = {
    1: "#1e3a8a",   # dark blue
    2: "#14532d",   # dark green
    3: "#78350f",   # dark amber
    4: "#374151",   # dark slate
}

# Discrete colormap: regimes 1→4 → 4 colours
_clrs = [REGIME_COLORS[k] for k in [1, 2, 3, 4]]
regime_cmap = mcolors.ListedColormap(_clrs)
regime_norm = mcolors.BoundaryNorm([0.5, 1.5, 2.5, 3.5, 4.5], ncolors=4)

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(8.6, 6.2))
fig.patch.set_facecolor("#f2f2f2")
ax.set_facecolor("#f2f2f2")

# ── 1. Voronoi background ──────────────────────────────────────────────────
ax.pcolormesh(
    X_plot, Y_plot, regime_map,
    cmap=regime_cmap, norm=regime_norm,
    shading="nearest",
    alpha=0.78,
    zorder=2,
)

# ── 2. Regime-boundary lines (contour of discrete regime_map) ─────────────
for boundary in [1.5, 2.5, 3.5]:
    ax.contour(
        X_plot, Y_plot, regime_map,
        levels=[boundary],
        colors=["#1a1a1a"],
        linewidths=[1.5],
        linestyles=["--"],
        alpha=0.60,
        zorder=4,
    )

# ── 3. Per-cell annotations ────────────────────────────────────────────────
#   Text colour: white on blue (regime 1), dark on others

def _cell_txt_color(regime: int) -> str:
    return "#ffffff" if regime == 1 else "#111111"


for r in rows:
    exit_str = f"step {r['exit']}" if r["exit"] is not None else "no exit"
    L_str    = f"L = {r['final_L']:.0f}"
    ax.text(
        r["n"], r["sigma"],
        f"{exit_str}\n{L_str}",
        ha="center", va="center",
        fontsize=7.0,
        color=_cell_txt_color(r["regime"]),
        fontweight="normal",
        linespacing=1.5,
        zorder=8,
    )

# ── 4. Data-point markers ──────────────────────────────────────────────────
for r in rows:
    ax.scatter(
        r["n"], r["sigma"],
        marker=REGIME_MARKERS[r["regime"]],
        s=95,
        color=REGIME_COLORS[r["regime"]],
        edgecolors=REGIME_EDGE[r["regime"]],
        linewidths=1.4,
        zorder=10,
    )

# ── 5. Saddle-peak star ────────────────────────────────────────────────────
SADDLE_N, SADDLE_SIG, SADDLE_STEP = 2.0, 0.05, 416

ax.scatter(
    [SADDLE_N], [SADDLE_SIG],
    marker="*", s=260,
    color="#fde047",          # bright yellow
    edgecolors="#1a1a1a",
    linewidths=1.0,
    zorder=12,
)
ax.annotate(
    f"saddle peak\nn = {SADDLE_N},  σ = {SADDLE_SIG}\nstep {SADDLE_STEP}",
    xy=(SADDLE_N, SADDLE_SIG),
    xytext=(SADDLE_N * 0.56, SADDLE_SIG * 1.70),
    fontsize=7.5,
    color="#fde047",
    fontweight="bold",
    ha="center",
    arrowprops=dict(
        arrowstyle="->", color="#fde047", lw=1.2,
        connectionstyle="arc3,rad=-0.18",
    ),
    bbox=dict(boxstyle="round,pad=0.35", fc="#1a1a1a", ec="#fde047", alpha=0.88),
    zorder=13,
)

# ── 6. Axes ────────────────────────────────────────────────────────────────
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
    "Scenario D  —  Dynamical Regime Map\n"
    "n ∈ {0.5, 1, 2, 4}  ×  σ ∈ {0.01, 0.02, 0.05, 0.10}",
    fontsize=12, fontweight="bold", pad=14,
)

# ── 7. Threshold note (bottom of axes) ────────────────────────────────────
ax.text(
    0.01, 0.01,
    f"Thresholds: hyper-coherent ≤ {HYPER_THRESH} steps  |  "
    f"marginal > {MARGINAL_THRESH} steps",
    transform=ax.transAxes,
    fontsize=6.8, color="#555555", ha="left", va="bottom",
    zorder=14,
)

# ── 8. Legend ──────────────────────────────────────────────────────────────
legend_handles: list = []

for regime in [1, 2, 3, 4]:
    h = mlines.Line2D(
        [], [],
        marker=REGIME_MARKERS[regime],
        linestyle="none",
        markerfacecolor=REGIME_COLORS[regime],
        markeredgecolor=REGIME_EDGE[regime],
        markeredgewidth=1.3,
        markersize=9,
        label=f"{REGIME_NAMES[regime]}   [{REGIME_DESC[regime]}]",
    )
    legend_handles.append(h)

# Saddle-peak star entry
legend_handles.append(
    mlines.Line2D(
        [], [],
        marker="*", linestyle="none",
        markerfacecolor="#fde047",
        markeredgecolor="#1a1a1a",
        markeredgewidth=0.8,
        markersize=13,
        label=f"Saddle peak  (n={SADDLE_N}, σ={SADDLE_SIG}, step {SADDLE_STEP})",
    )
)

# Dashed-line entry for regime boundaries
legend_handles.append(
    mlines.Line2D(
        [], [],
        linestyle="--", color="#1a1a1a",
        linewidth=1.4, alpha=0.60,
        label="Regime boundary",
    )
)

ax.legend(
    handles=legend_handles,
    loc="lower right",
    fontsize=8.2,
    framealpha=0.92,
    edgecolor="#aaaaaa",
    handlelength=1.8,
    title="Dynamical regime",
    title_fontsize=9,
)

# ── 9. Save ────────────────────────────────────────────────────────────────
fig.tight_layout()
OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"Saved: {OUT_PNG}")
plt.close(fig)
