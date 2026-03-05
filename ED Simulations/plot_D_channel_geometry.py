"""
plot_D_channel_geometry.py
==========================
3-panel channel-geometry figure from the Scenario-D sweep.

Constructs a 1-parameter family of modified exit-surfaces by adding a 2D
Gaussian perturbation G(n, s) centred on the saddle peak (n=2.0, s=0.05):

    f_A(n, s) = f_baseline(n, s) + A * G(n, s)

    A = +80  ->  Shallow channel  (saddle raised, broader/flatter)
    A =   0  ->  Baseline         (unmodified Scenario-D exit surface)
    A = -80  ->  Deepened channel (saddle suppressed, sharper)

Each panel shows a filled exit-surface patch zoomed on the saddle region,
with sparse gradient arrows and a det(H)=0 boundary to indicate curvature.

Output
------
    results/phase2D/D_channel_geometry.png
"""

from __future__ import annotations

import csv
import importlib
from pathlib import Path

import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.colors as mcolors
import matplotlib.ticker as ticker

_have_scipy = importlib.util.find_spec("scipy") is not None
if _have_scipy:
    from scipy.interpolate import RegularGridInterpolator
    from scipy.ndimage import gaussian_filter

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR  = Path(__file__).parent
SUMMARY_CSV = SCRIPT_DIR / "results" / "phase2D" / "summary.csv"
OUT_PNG     = SCRIPT_DIR / "results" / "phase2D" / "D_channel_geometry.png"

# ---------------------------------------------------------------------------
# Load sweep data
# ---------------------------------------------------------------------------

rows: list[dict] = []
with SUMMARY_CSV.open(encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rows.append({
            "n":    float(row["mobility_exp"]),
            "s":    float(row["noise_amp"]),
            "exit": None if row["phase_exit_step"] == "None"
                         else float(row["phase_exit_step"]),
        })

exponents = sorted({r["n"] for r in rows})
sigmas    = sorted({r["s"] for r in rows})

exit_grid    = np.full((len(sigmas), len(exponents)), np.nan)
no_exit_mask = np.zeros((len(sigmas), len(exponents)), dtype=bool)
for r in rows:
    i = sigmas.index(r["s"])
    j = exponents.index(r["n"])
    if r["exit"] is not None:
        exit_grid[i, j] = r["exit"]
    else:
        no_exit_mask[i, j] = True

exit_fill = np.where(no_exit_mask, 0.0, exit_grid)
log_n     = np.log10(np.array(exponents))
log_sig   = np.log10(np.array(sigmas))

# ---------------------------------------------------------------------------
# Fine interpolation: 200x200 in log-log space
# ---------------------------------------------------------------------------

N_FINE    = 200
ln_n_fine = np.linspace(log_n.min(),   log_n.max(),   N_FINE)
ln_s_fine = np.linspace(log_sig.min(), log_sig.max(), N_FINE)
LN, LS    = np.meshgrid(ln_n_fine, ln_s_fine)   # rows=s axis, cols=n axis

if _have_scipy:
    rgi_exit = RegularGridInterpolator(
        (log_sig, log_n), exit_fill,
        method="linear", bounds_error=False, fill_value=0.0,
    )
    exit_base = rgi_exit(np.column_stack([LS.ravel(), LN.ravel()])).reshape(N_FINE, N_FINE)

    rgi_noex = RegularGridInterpolator(
        (log_sig, log_n), no_exit_mask.astype(float),
        method="linear", bounds_error=False, fill_value=1.0,
    )
    no_exit_fine = rgi_noex(
        np.column_stack([LS.ravel(), LN.ravel()])
    ).reshape(N_FINE, N_FINE) > 0.45
else:
    exit_base    = np.zeros((N_FINE, N_FINE))
    no_exit_fine = np.zeros((N_FINE, N_FINE), dtype=bool)
    for ii, ls in enumerate(ln_s_fine):
        for jj, ln_v in enumerate(ln_n_fine):
            j0 = max(0, min(len(log_n)-2, int(np.searchsorted(log_n, ln_v))-1))
            i0 = max(0, min(len(log_sig)-2, int(np.searchsorted(log_sig, ls))-1))
            tn = (ln_v - log_n[j0])   / (log_n[j0+1]   - log_n[j0])
            ts = (ls   - log_sig[i0]) / (log_sig[i0+1] - log_sig[i0])
            def _bl(g):
                return (g[i0,j0]*(1-tn)*(1-ts) + g[i0,j0+1]*tn*(1-ts) +
                        g[i0+1,j0]*(1-tn)*ts   + g[i0+1,j0+1]*tn*ts)
            exit_base[ii, jj]    = _bl(exit_fill)
            no_exit_fine[ii, jj] = _bl(no_exit_mask.astype(float)) > 0.45

# ---------------------------------------------------------------------------
# Saddle centre + Gaussian perturbation kernel
# ---------------------------------------------------------------------------

x0 = np.log10(2.0)    # saddle n centre
y0 = np.log10(0.05)   # saddle s centre
SADDLE_STEP = 416

W_N = 0.52   # Gaussian half-width in log10(n) space
W_S = 0.52   # Gaussian half-width in log10(s) space

GAUSS_FULL = np.exp(-((LN - x0)**2 / (2 * W_N**2)
                     + (LS - y0)**2 / (2 * W_S**2)))

# ---------------------------------------------------------------------------
# Zoom window around saddle
# ---------------------------------------------------------------------------

ZOOM_N = (0.42, 5.0)
ZOOM_S = (0.008, 0.13)

col_sel = (ln_n_fine >= np.log10(ZOOM_N[0])) & (ln_n_fine <= np.log10(ZOOM_N[1]))
row_sel = (ln_s_fine >= np.log10(ZOOM_S[0])) & (ln_s_fine <= np.log10(ZOOM_S[1]))
c0, c1  = np.where(col_sel)[0][[0, -1]]
r0, r1  = np.where(row_sel)[0][[0, -1]]

def _z(a):
    return a[r0:r1+1, c0:c1+1]

LN_z   = _z(LN)
LS_z   = _z(LS)
BASE_z = _z(exit_base)
NEX_z  = _z(no_exit_fine)
GS_z   = _z(GAUSS_FULL)

EXTENT = [LN_z[0, 0], LN_z[0, -1], LS_z[0, 0], LS_z[-1, 0]]

dn = float(np.diff(LN_z[0, :]).mean())
ds = float(np.diff(LS_z[:, 0]).mean())

# ---------------------------------------------------------------------------
# 3-panel parameterisation
# ---------------------------------------------------------------------------

AMPLITUDES   = [+80,                0,           -80]
PANEL_LABELS = ["Shallow  (A = +80)",
                "Baseline  (A = 0)",
                "Deepened  (A = \u221280)"]
ACCENT_COLS  = ["#60a5fa",   "#fde047",   "#f87171"]   # blue / yellow / red

# Hessian smoothing for curvature extraction
H_SMOOTH = 6

panels: list[dict] = []
for amp in AMPLITUDES:
    f_raw  = np.clip(BASE_z + amp * GS_z, 0.0, None)
    f_disp = np.where(NEX_z, np.nan, f_raw)

    # Working copy with no-exit filled for differentiation
    f_work = np.where(NEX_z, 0.0, f_raw)

    # Gradient (lightly smoothed)
    if _have_scipy:
        fg = gaussian_filter(f_work, sigma=2)
    else:
        fg = f_work
    dF_ds_g, dF_dn_g = np.gradient(fg, ds, dn)

    # Hessian (more heavily smoothed)
    if _have_scipy:
        fh = gaussian_filter(f_work, sigma=H_SMOOTH)
    else:
        fh = f_work
    dFdn_h = np.gradient(fh, dn, axis=1)
    dFds_h = np.gradient(fh, ds, axis=0)
    H11 = np.gradient(dFdn_h, dn, axis=1)
    H22 = np.gradient(dFds_h, ds, axis=0)
    H12 = np.gradient(dFdn_h, ds, axis=0)
    det_H = H11 * H22 - H12**2

    panels.append(dict(f_disp=f_disp, dF_dn=dF_dn_g, dF_ds=dF_ds_g,
                       det_H=det_H, amp=amp))

# ---------------------------------------------------------------------------
# Shared colour scale
# ---------------------------------------------------------------------------

all_vals = np.concatenate(
    [p["f_disp"][~np.isnan(p["f_disp"])].ravel() for p in panels]
)
VMIN = max(0.0, float(all_vals.min()))
VMAX = float(all_vals.max())

CMAP_NAME = "plasma_r"
CMAP      = mpl.colormaps.get_cmap(CMAP_NAME).copy()
CMAP.set_bad(color="#2a2a2a")

# ---------------------------------------------------------------------------
# Figure: 1 x 3 panels  +  colorbar
# ---------------------------------------------------------------------------

FIG_BG   = "#1a1a1a"
PANEL_BG = "#0d0d0d"

fig = plt.figure(figsize=(13.5, 5.2))
fig.patch.set_facecolor(FIG_BG)

gs = gridspec.GridSpec(
    1, 4,
    figure       = fig,
    width_ratios = [1, 1, 1, 0.055],
    wspace       = 0.10,
    left         = 0.06,
    right        = 0.96,
    top          = 0.87,
    bottom       = 0.12,
)
axs = [fig.add_subplot(gs[0, k]) for k in range(3)]
cax = fig.add_subplot(gs[0, 3])

STRIDE = max(1, LN_z.shape[1] // 12)

for ax, panel, label, accent in zip(axs, panels, PANEL_LABELS, ACCENT_COLS):
    f      = panel["f_disp"]
    dF_dn  = panel["dF_dn"]
    dF_ds  = panel["dF_ds"]
    det_H  = panel["det_H"]

    ax.set_facecolor(PANEL_BG)

    # ── 1. Exit-surface heatmap ────────────────────────────────────────
    ax.imshow(
        f,
        extent        = EXTENT,
        origin        = "lower",
        cmap          = CMAP,
        vmin          = VMIN,
        vmax          = VMAX,
        aspect        = "auto",
        interpolation = "bilinear",
        zorder        = 2,
    )

    # ── 2. det(H) < 0 saddle zone ─────────────────────────────────────
    det_plot = np.where(NEX_z, 0.0, det_H)

    ax.contourf(
        LN_z, LS_z, det_plot,
        levels = [-1e15, 0.0],
        colors = ["#00cccc"],
        alpha  = 0.20,
        zorder = 3,
    )
    try:
        ax.contour(
            LN_z, LS_z, det_plot,
            levels     = [0.0],
            colors     = ["#00cccc"],
            linewidths = [1.2],
            linestyles = ["--"],
            zorder     = 4,
        )
    except Exception:
        pass

    # ── 3. Sparse gradient quiver ──────────────────────────────────────
    offs  = STRIDE // 2
    qr    = np.arange(offs, LN_z.shape[0], STRIDE)
    qc    = np.arange(offs, LN_z.shape[1], STRIDE)
    QN    = LN_z[np.ix_(qr, qc)]
    QS    = LS_z[np.ix_(qr, qc)]
    U     = dF_dn[np.ix_(qr, qc)]
    V     = dF_ds[np.ix_(qr, qc)]
    NEX_q = NEX_z[np.ix_(qr, qc)]

    U = np.where(NEX_q, 0.0, U)
    V = np.where(NEX_q, 0.0, V)

    mag_max = np.hypot(U[~NEX_q], V[~NEX_q]).max() if (~NEX_q).any() else 1.0
    if mag_max > 1e-10:
        U /= mag_max
        V /= mag_max

    ax.quiver(
        QN, QS, U, V,
        color          = "white",
        alpha          = 0.58,
        scale          = 1.0 / (STRIDE * dn * 0.42),
        scale_units    = "xy",
        pivot          = "mid",
        headwidth      = 3.0,
        headlength     = 3.8,
        headaxislength = 3.4,
        zorder         = 6,
    )

    # ── 4. Saddle-peak marker ──────────────────────────────────────────
    ax.scatter(
        [x0], [y0],
        marker     = "*",
        s          = 220,
        color      = "#fde047",
        edgecolors = "#1a1a1a",
        linewidths = 0.8,
        zorder     = 9,
    )

    # ── 5. Panel label ─────────────────────────────────────────────────
    ax.text(
        0.50, 0.965,
        label,
        transform  = ax.transAxes,
        fontsize   = 10.5,
        fontweight = "bold",
        color      = accent,
        ha         = "center",
        va         = "top",
        bbox       = dict(boxstyle="round,pad=0.25",
                          fc=PANEL_BG, ec=accent, alpha=0.88),
        zorder     = 10,
    )

    # ── 6. Axes ────────────────────────────────────────────────────────
    ax.set_xlim(EXTENT[0], EXTENT[1])
    ax.set_ylim(EXTENT[2], EXTENT[3])

    ax.set_xticks([np.log10(v) for v in exponents])
    ax.xaxis.set_major_formatter(
        ticker.FuncFormatter(lambda v, _: f"{10**v:g}")
    )
    ax.set_yticks([np.log10(v) for v in sigmas])
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda v, _: f"{10**v:g}")
    )
    ax.tick_params(axis="both", labelsize=9, colors="white")

    for spine in ax.spines.values():
        spine.set_edgecolor(accent)
        spine.set_linewidth(1.8)

    ax.set_xlabel("Mobility exponent  n", fontsize=9, color="white", labelpad=3)
    if ax is axs[0]:
        ax.set_ylabel("Noise amplitude  \u03c3", fontsize=9, color="white", labelpad=3)

# ---------------------------------------------------------------------------
# Shared colorbar
# ---------------------------------------------------------------------------

sm = mpl.cm.ScalarMappable(
    cmap = CMAP,
    norm = mcolors.Normalize(vmin=VMIN, vmax=VMAX),
)
sm.set_array([])
cb = fig.colorbar(sm, cax=cax)
cb.set_label("Exit step", color="white", fontsize=9, labelpad=8)
cb.ax.yaxis.set_tick_params(color="white", labelsize=8)
plt.setp(cb.ax.yaxis.get_ticklabels(), color="white")
cb.outline.set_edgecolor("#555555")

# ---------------------------------------------------------------------------
# Figure title
# ---------------------------------------------------------------------------

fig.text(
    0.47, 0.96,
    "Scenario D  \u2014  Saddle Channel Geometry",
    ha="center", va="bottom", fontsize=12, fontweight="bold", color="white",
)
fig.text(
    0.47, 0.935,
    "f\u2080 + A\u00b7G(n,\u03c3)   \u00b7   Arrows: \u2207f   "
    "\u00b7   Cyan dashed: det(H) = 0   \u00b7   \u2605: saddle peak (n=2, \u03c3=0.05)",
    ha="center", va="bottom", fontsize=8.0, color="#aaaaaa",
)

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------

OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"Saved: {OUT_PNG}")
plt.close(fig)
