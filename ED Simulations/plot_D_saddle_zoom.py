"""
plot_D_saddle_zoom.py
======================
Zoom-in on the saddle-peak region of the Scenario-D phase-exit surface
near (n≈2.0, σ≈0.05).

Layers
------
  1. Filled exit-step surface  (plasma_r, full colour)
  2. Exit-step iso-lines        (thin, semi-transparent)
  3. Gradient arrows            (quiver; white → red by magnitude)
  4. det(H)=0 iso-line          (cyan dashed) – boundary between
                                  saddle  (det H < 0)  and
                                  max/min (det H > 0)  curvature regimes
  5. det(H) < 0 tint            (light cyan fill) – saddle zone
  6. Saddle-peak marker ★       with (n, σ, step) annotation
  7. No-exit boundary           (white dashed)

Saddle detection
----------------
The gradient and Hessian are computed from a lightly Gaussian-smoothed
version of the bilinear-interpolated surface so that second derivatives
are finite and spatially meaningful.  The sign of det(H) = H₁₁·H₂₂ − H₁₂²
distinguishes saddle geometry (det<0) from extremal geometry (det>0).

Output
------
    results/phase2D/D_saddle_zoom.png
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
    from scipy.ndimage import gaussian_filter as _gf
else:
    _RGI = None
    def _gf(arr, sigma): return arr        # no-op fallback

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR  = Path(__file__).parent
SUMMARY_CSV = SCRIPT_DIR / "results" / "phase2D" / "summary.csv"
OUT_PNG     = SCRIPT_DIR / "results" / "phase2D" / "D_saddle_zoom.png"

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------

rows: list[dict] = []
with SUMMARY_CSV.open(encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rows.append({
            "n":    float(row["mobility_exp"]),
            "sig":  float(row["noise_amp"]),
            "exit": None if row["phase_exit_step"] == "None"
                        else int(row["phase_exit_step"]),
        })

exponents = sorted({r["n"]   for r in rows})
sigmas    = sorted({r["sig"] for r in rows})
nn, ns    = len(exponents), len(sigmas)

exit_grid    = np.full((ns, nn), np.nan)
no_exit_grid = np.zeros((ns, nn))
for r in rows:
    ci = exponents.index(r["n"])
    ri = sigmas.index(r["sig"])
    if r["exit"] is not None:
        exit_grid[ri, ci] = float(r["exit"])
    else:
        no_exit_grid[ri, ci] = 1.0

EXIT_FILL = np.where(np.isnan(exit_grid), 500.0, exit_grid)

# ---------------------------------------------------------------------------
# High-resolution interpolation over the full grid (log-log, 240×240)
# ---------------------------------------------------------------------------

log_n   = np.log10(np.array(exponents, dtype=float))
log_sig = np.log10(np.array(sigmas,    dtype=float))

NFULL = 240
n_fine   = np.linspace(log_n.min(),   log_n.max(),   NFULL)
sig_fine = np.linspace(log_sig.min(), log_sig.max(), NFULL)
NF, SF   = np.meshgrid(n_fine, sig_fine)      # (NFULL, NFULL)


def _interp_full(data: np.ndarray) -> np.ndarray:
    if _have_scipy:
        rgi = _RGI((log_sig, log_n), data,
                   method="linear", bounds_error=False, fill_value=None)
        return rgi(np.stack([SF.ravel(), NF.ravel()], axis=-1)).reshape(SF.shape)
    out = np.empty(SF.shape)
    for i, ls in enumerate(sig_fine):
        for j, ln in enumerate(n_fine):
            ri0 = max(0, np.searchsorted(log_sig, ls) - 1); ri1 = min(ns-1, ri0+1)
            ci0 = max(0, np.searchsorted(log_n,   ln) - 1); ci1 = min(nn-1, ci0+1)
            if ri0==ri1 or ci0==ci1:
                out[i,j] = data[ri0, ci0]
            else:
                fr = (ls-log_sig[ri0])/(log_sig[ri1]-log_sig[ri0])
                fc = (ln-log_n[ci0])/(log_n[ci1]-log_n[ci0])
                out[i,j] = ((1-fr)*(1-fc)*data[ri0,ci0]+(1-fr)*fc*data[ri0,ci1]
                           +fr*(1-fc)*data[ri1,ci0]+fr*fc*data[ri1,ci1])
    return out


exit_full = _interp_full(EXIT_FILL)
mask_full = _interp_full(no_exit_grid)

no_exit_full = mask_full >= 0.50

# Mask exit in no-exit zone
exit_masked = np.where(no_exit_full, np.nan, exit_full)

# ---------------------------------------------------------------------------
# Zoom: restrict to the saddle neighbourhood
# Only keep rows/cols inside n∈[0.9,4.5], σ∈[0.016,0.12]
# ---------------------------------------------------------------------------

N_LO,  N_HI  = np.log10(0.9),  np.log10(4.5)
S_LO,  S_HI  = np.log10(0.016), np.log10(0.12)

jlo = np.searchsorted(n_fine,   N_LO)
jhi = np.searchsorted(n_fine,   N_HI)
ilo = np.searchsorted(sig_fine, S_LO)
ihi = np.searchsorted(sig_fine, S_HI)

# zoom slices
NZ   = NF[ilo:ihi, jlo:jhi]
SZ   = SF[ilo:ihi, jlo:jhi]
X_Z  = 10**NZ          # n
Y_Z  = 10**SZ          # σ

exit_z     = exit_masked[ilo:ihi, jlo:jhi]
no_exit_z  = no_exit_full[ilo:ihi, jlo:jhi]
mask_z     = mask_full[ilo:ihi, jlo:jhi]
n_z        = n_fine[jlo:jhi]
s_z        = sig_fine[ilo:ihi]

# ---------------------------------------------------------------------------
# Gaussian-smooth exit for Hessian (finite differences need smoothness)
# σ_smooth chosen so each "pixel" covers ~1/8 of the zoom range
# ---------------------------------------------------------------------------

SMOOTH = 6.0   # pixels in the zoom array
exit_smooth = _gf(np.where(no_exit_z, 0.0, exit_z.filled(0.0)
                            if hasattr(exit_z, 'filled') else
                            np.where(np.isnan(exit_z), 0.0, exit_z)),
                  sigma=SMOOTH)
# zero out no-exit zone in smooth surface so derivatives don't bleed
exit_smooth = np.where(no_exit_z, np.nan, exit_smooth)

# grid spacing in log units (uniform)
dn  = n_z[1]   - n_z[0]
ds  = s_z[1]   - s_z[0]

# first derivatives (in log-log space)
dF_dn  = np.gradient(exit_smooth, dn,  axis=1)   # ∂f/∂(log n)
dF_ds  = np.gradient(exit_smooth, ds,  axis=0)   # ∂f/∂(log σ)

# second derivatives  → Hessian components
H11 = np.gradient(dF_dn, dn, axis=1)    # ∂²f/∂(log n)²
H22 = np.gradient(dF_ds, ds, axis=0)    # ∂²f/∂(log σ)²
H12 = np.gradient(dF_dn, ds, axis=0)    # ∂²f/∂(log n)∂(log σ)

det_H = H11 * H22 - H12**2
det_H = np.where(no_exit_z, np.nan, det_H)

# Gradient magnitude (in log space)
grad_mag = np.sqrt(dF_dn**2 + dF_ds**2)
grad_mag = np.where(no_exit_z, np.nan, grad_mag)

# ---------------------------------------------------------------------------
# Locate saddle peak = highest exit step in exited zone
# ---------------------------------------------------------------------------

exit_for_peak = np.where(no_exit_z, -np.inf,
                          np.nan_to_num(exit_z, nan=-np.inf))
pi, pj = np.unravel_index(np.argmax(exit_for_peak), exit_for_peak.shape)
peak_n   = X_Z[pi, pj]
peak_sig = Y_Z[pi, pj]
peak_val = int(np.nanmax(exit_z))

# ---------------------------------------------------------------------------
# Quiver subsampling  (skip every K points in the zoom window)
# ---------------------------------------------------------------------------

K   = max(1, len(n_z) // 16)
qi  = np.arange(K//2, len(s_z), K)
qj  = np.arange(K//2, len(n_z), K)
QI, QJ = np.meshgrid(qj, qi, indexing="xy")   # note: i=row=σ, j=col=n

q_x  = X_Z[qi[:, None], qj[None, :]]   # n-coords
q_y  = Y_Z[qi[:, None], qj[None, :]]   # σ-coords
q_u  = dF_dn[qi[:, None], qj[None, :]] # ∂f/∂log(n)
q_v  = dF_ds[qi[:, None], qj[None, :]] # ∂f/∂log(σ)
q_mag = grad_mag[qi[:, None], qj[None, :]]

# mask arrows in no-exit zone
valid = ~no_exit_z[qi[:, None], qj[None, :]]
q_u = np.where(valid, q_u, np.nan)
q_v = np.where(valid, q_v, np.nan)

# Normalise arrows to uniform visual length; colour by magnitude
arrow_scale = np.nanmax(q_mag) + 1e-9
q_u_n = q_u / arrow_scale
q_v_n = q_v / arrow_scale

# In log-log axes, arrows need to be in data units: convert Δlog→Δdata
# Δlog(n)  →  n * Δlog(n) * ln(10)  ≈  n * Δlog(n) * 2.303  (small angle)
# But for quiver on log axes we just scale by the data coordinate so the
# visual length is uniform.  matplotlib quiver handles log axes poorly,
# so we plot in log space and set ax.set_xscale/yscale after.
# Simplest: plot on linear axes using log(n), log(σ) as coordinates.

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(8.6, 6.4))
fig.patch.set_facecolor("#1a1a1a")
ax.set_facecolor("#1a1a1a")

CMAP_S = mpl.colormaps["plasma_r"].copy()
CMAP_S.set_bad("#1a1a1a")
NORM_S = mcolors.Normalize(vmin=84, vmax=416)

# ── 1. Exit-step surface ───────────────────────────────────────────────────
pcm = ax.pcolormesh(
    X_Z, Y_Z, exit_z,
    cmap=CMAP_S, norm=NORM_S,
    shading="gouraud",
    zorder=2,
)

# ── 2. Exit iso-step contour lines ────────────────────────────────────────
ciso = ax.contour(
    X_Z, Y_Z, exit_z,
    levels=[167, 250, 333, 380, 416],
    colors=["white"],
    linewidths=0.7,
    alpha=0.35,
    zorder=3,
)
ax.clabel(ciso, fmt=lambda v: f"{int(v)}", fontsize=7,
          inline=True, use_clabeltext=True)

# ── 3. det(H) < 0 saddle zone tint ────────────────────────────────────────
saddle_zone = np.where(det_H < 0, 1.0, 0.0)
saddle_zone = np.where(no_exit_z, np.nan, saddle_zone)
ax.contourf(
    X_Z, Y_Z, saddle_zone,
    levels=[0.5, 1.5],
    colors=["#00ccff"],
    alpha=0.12,
    zorder=4,
)

# det(H)=0 boundary line (saddle ↔ extremal transition)
ax.contour(
    X_Z, Y_Z,
    np.where(np.isnan(det_H), 0.0, det_H),
    levels=[0.0],
    colors=["#00eeff"],
    linewidths=[1.6],
    linestyles=["-."],
    zorder=5,
)

# ── 4. Gradient quiver ────────────────────────────────────────────────────
# Plot in log space to get uniform-length arrows on log axes
q_x_log = np.log10(q_x)
q_y_log = np.log10(q_y)

# arrow colours by magnitude
cmap_q   = plt.get_cmap("hot_r")
q_col    = np.where(valid, q_mag / arrow_scale, np.nan).ravel()
q_col_c  = cmap_q(np.nan_to_num(q_col, nan=0.0))

# use a secondary axes in log-space (twin) approach:
# simplest: just set xscale/yscale to log and plot normally.
# For quiver, we plot in actual data (n,σ) coords — matplotlib handles it.
qv = ax.quiver(
    q_x, q_y,
    q_u_n * q_x * np.log(10),     # convert Δlog(n) → Δn  (tangent approx)
    q_v_n * q_y * np.log(10),     # convert Δlog(σ) → Δσ
    np.where(valid, q_mag, np.nan),
    cmap="hot_r",
    norm=mcolors.Normalize(vmin=0, vmax=np.nanpercentile(q_mag, 95)),
    scale=None,
    scale_units="xy",
    angles="xy",
    width=0.003,
    headwidth=4,
    headlength=5,
    alpha=0.85,
    zorder=9,
)

# ── 5. No-exit boundary ───────────────────────────────────────────────────
ax.contour(
    X_Z, Y_Z, mask_z,
    levels=[0.499],
    colors=["white"],
    linewidths=[2.0],
    linestyles=["--"],
    zorder=10,
)
ax.contourf(
    X_Z, Y_Z, mask_z,
    levels=[0.499, 1.5],
    colors=["#1a1a1a"],
    zorder=6,
)

# ── 6. Data points ────────────────────────────────────────────────────────
for r in rows:
    if N_LO <= np.log10(r["n"]) <= N_HI and S_LO <= np.log10(r["sig"]) <= S_HI:
        fc = "#888888" if r["exit"] is None else "#eeeeee"
        ax.scatter(r["n"], r["sig"], s=55, color=fc,
                   edgecolors="#111111", linewidths=0.8, zorder=12)

# ── 7. Saddle peak marker ★ ────────────────────────────────────────────────
ax.scatter([peak_n], [peak_sig],
           s=220, marker="*", color="#ffee00",
           edgecolors="#333300", linewidths=0.8,
           zorder=14,
           label=f"Saddle peak  (step {peak_val})")

ann_off_n   = peak_n   * 0.70
ann_off_sig = peak_sig * 1.60
ax.annotate(
    f"  saddle peak\n  n = {peak_n:.2g}\n  σ = {peak_sig:.3g}\n  step = {peak_val}",
    xy=(peak_n, peak_sig),
    xytext=(ann_off_n, ann_off_sig),
    fontsize=8.5, color="#ffee00", fontweight="bold",
    arrowprops=dict(
        arrowstyle="->", color="#ffee00", lw=1.4,
        connectionstyle="arc3,rad=0.20",
    ),
    bbox=dict(boxstyle="round,pad=0.4", fc="#222200", ec="#ffee00", alpha=0.88),
    zorder=15,
)

# ── 8. Axes ────────────────────────────────────────────────────────────────
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(10**N_LO, 10**N_HI)
ax.set_ylim(10**S_LO, 10**S_HI)

# ticks at the grid values that fall inside the zoom
xt = [v for v in exponents   if 10**N_LO <= v <= 10**N_HI]
yt = [v for v in sigmas      if 10**S_LO <= v <= 10**S_HI]
ax.set_xticks(xt); ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda v,_: f"{v:g}"))
ax.set_yticks(yt); ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v,_: f"{v:g}"))
ax.tick_params(axis="both", labelsize=11, colors="white")
for spine in ax.spines.values():
    spine.set_edgecolor("#555555")

ax.set_xlabel("Mobility exponent  n", fontsize=12, labelpad=8, color="white")
ax.set_ylabel("Noise amplitude  σ",   fontsize=12, labelpad=8, color="white")
ax.set_title(
    "Scenario D  —  Saddle-peak zoom  (exit-step surface + gradient field)\n"
    "cyan tint = det(H) < 0  (saddle curvature)  |  arrows = ∇(exit step)",
    fontsize=11, fontweight="bold", color="white", pad=12,
)

# ── 9. Colourbar (exit step) ───────────────────────────────────────────────
cbar = fig.colorbar(pcm, ax=ax, pad=0.025, fraction=0.046,
                    ticks=[167, 250, 333, 380, 416])
cbar.set_label("Phase-exit step", fontsize=9, color="white")
cbar.ax.tick_params(labelsize=9, colors="white")
cbar.outline.set_edgecolor("#555555")

# ── 10. Legend ─────────────────────────────────────────────────────────────
import matplotlib.lines  as mlines
import matplotlib.patches as mpatches

handles = [
    mlines.Line2D([],[],color="#00eeff",lw=1.6,ls="-.",
                  label="det(H) = 0  (saddle boundary)"),
    mpatches.Patch(facecolor="#00ccff",alpha=0.3,edgecolor="none",
                   label="det(H) < 0  (saddle zone)"),
    mlines.Line2D([],[],color="white",lw=2.0,ls="--",
                  label="No-exit boundary"),
    mlines.Line2D([],[],marker="*",color="w",markersize=10,
                  markerfacecolor="#ffee00",markeredgecolor="#333300",
                  lw=0,label=f"Saddle peak  (step {peak_val})"),
]
leg = ax.legend(handles=handles, loc="lower left",
                fontsize=8, framealpha=0.75,
                edgecolor="#555555", labelcolor="white",
                facecolor="#222222")

# ── 11. Save ──────────────────────────────────────────────────────────────
fig.tight_layout()
OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"Saved: {OUT_PNG}")
plt.close(fig)
