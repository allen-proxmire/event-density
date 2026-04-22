"""
Generate publication-quality figures for the telegraph-modulated PME
(Foundational Paper v2 Analogue 5) from the saved simulation output.

Produces:
  1. field_snapshots.png — delta(x,y,t) at 6 times showing PME spreading
  2. time_series.png      — v(t), rho_center(t), rho_mean(t) on one axis set
  3. psd.png              — PSD of v(t) and rho_center(t) with peak annotations
  4. harmonic.png         — zoom on fundamental vs 3x harmonic
  5. summary.png          — 4-panel composite for the memo
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors, cm
from pathlib import Path


def load(npz_path):
    d = np.load(npz_path, allow_pickle=True)
    out = {k: d[k] for k in d.files}
    # meta_json was stored as a str representation of a dict; eval it
    out["meta"] = eval(str(out["meta_json"]))
    return out


def fig_field_snapshots(data, outpath):
    """Six snapshots of delta = rho_max - rho across simulation time."""
    meta = data["meta"]
    rho_max = meta["ed_params"]["rho_max"]
    rho_star = meta["ed_params"]["rho_star"]
    t_snap = data["t_snap"]
    rho_snap = data["rho_snap"]

    # Pick 6 snapshots evenly spaced in time
    n = len(t_snap)
    idxs = np.linspace(0, n - 1, 6).astype(int)

    # delta = rho_max - rho (positive = depression; initial bump was depression)
    # But we'll plot rho itself relative to rho_star to show bump structure
    # More intuitive: plot rho_star - rho (positive = depression)
    delta_disp = np.stack([(rho_star - rho_snap[i]) for i in idxs])

    # Common color scale
    vmin, vmax = delta_disp.min(), delta_disp.max()
    if abs(vmin) < 1e-6 and abs(vmax) < 1e-6:
        vmin, vmax = -0.01, 0.01
    vmax_abs = max(abs(vmin), abs(vmax))

    fig, axes = plt.subplots(2, 3, figsize=(11, 7))
    axes = axes.flatten()
    for i, (ax, snap_idx) in enumerate(zip(axes, idxs)):
        im = ax.imshow(rho_star - rho_snap[snap_idx].T, origin="lower",
                        extent=[data["x"].min(), data["x"].max(),
                                data["y"].min(), data["y"].max()],
                        cmap="RdBu_r", vmin=-vmax_abs, vmax=vmax_abs)
        ax.set_title(f"t = {t_snap[snap_idx]:.1f}", fontsize=11)
        ax.set_xlabel("x")
        if i % 3 == 0:
            ax.set_ylabel("y")
    fig.colorbar(im, ax=axes, label=r"$\rho^* - \rho$  (depression)",
                  fraction=0.02, pad=0.02)
    fig.suptitle("Telegraph-modulated PME: field evolution", fontsize=13)
    fig.savefig(outpath, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {outpath}")


def fig_time_series(data, outpath):
    """v(t), rho_center(t), rho_mean(t), Fbar(t) stacked."""
    meta = data["meta"]
    rho_star = meta["ed_params"]["rho_star"]
    t = data["t_hist"]

    fig, axes = plt.subplots(4, 1, figsize=(10, 9), sharex=True)

    axes[0].plot(t, data["v_hist"], "C0", lw=0.8)
    axes[0].axhline(0, color="k", lw=0.4, alpha=0.4)
    axes[0].set_ylabel(r"$v(t)$", fontsize=11)
    axes[0].set_title("Participation variable", fontsize=10)

    axes[1].plot(t, data["rho_center_hist"] - rho_star, "C1", lw=0.8)
    axes[1].axhline(0, color="k", lw=0.4, alpha=0.4)
    axes[1].set_ylabel(r"$\rho_{\rm center}(t) - \rho^*$", fontsize=11)
    axes[1].set_title("Central density (depression → relaxation + oscillation)",
                      fontsize=10)

    axes[2].plot(t, data["rho_mean_hist"] - rho_star, "C2", lw=0.8)
    axes[2].axhline(0, color="k", lw=0.4, alpha=0.4)
    axes[2].set_ylabel(r"$\bar\rho(t) - \rho^*$", fontsize=11)
    axes[2].set_title("Domain-averaged density (uniform mode)", fontsize=10)

    axes[3].plot(t, data["Fbar_hist"], "C3", lw=0.8)
    axes[3].axhline(0, color="k", lw=0.4, alpha=0.4)
    axes[3].set_ylabel(r"$\bar F[\rho](t)$", fontsize=11)
    axes[3].set_title("Domain-averaged operator (drives v)", fontsize=10)

    axes[-1].set_xlabel("time")
    fig.suptitle("Telegraph-modulated PME: time series (H={:.0f})".format(
        meta["ed_params"]["H"]), fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(outpath, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {outpath}")


def compute_psd(t, y, detrend="linear"):
    """Welch-style PSD via scipy if available, else periodogram."""
    from scipy.signal import welch, detrend as sp_detrend
    dt = float(t[1] - t[0])
    fs = 1.0 / dt
    y = np.asarray(y, dtype=np.float64)
    if detrend == "linear":
        y = sp_detrend(y, type="linear")
    elif detrend == "mean":
        y = y - y.mean()
    nperseg = min(len(y), 2048)
    f, P = welch(y, fs=fs, nperseg=nperseg, window="hann")
    return f, P


def fig_psd(data, outpath):
    """PSD of v(t) and rho_center(t) showing matched omega_v."""
    meta = data["meta"]
    linpred = meta["linpred"]
    t = data["t_hist"]
    rho_star = meta["ed_params"]["rho_star"]

    # Drop the early transient (first ~5 time units) so the PME-spreading transient
    # doesn't dominate the spectrum. Keep the relaxation + oscillation tail.
    keep = t > 5.0
    t_k = t[keep]
    v_k = data["v_hist"][keep]
    rc_k = data["rho_center_hist"][keep] - rho_star

    fv, Pv = compute_psd(t_k, v_k, detrend="linear")
    fc, Pc = compute_psd(t_k, rc_k, detrend="linear")

    # Find peak in 0.01 - 0.3 Hz range (period 3 - 100)
    def peak_in_band(f, P, band):
        mask = (f >= band[0]) & (f <= band[1])
        idx = np.argmax(P[mask])
        return f[mask][idx], P[mask][idx]

    band = (0.01, 0.3)
    fpeak_v, Ppeak_v = peak_in_band(fv, Pv, band)
    fpeak_c, Ppeak_c = peak_in_band(fc, Pc, band)

    omega_v = 2 * np.pi * fpeak_v
    omega_c = 2 * np.pi * fpeak_c

    match_pct = 100 * abs(fpeak_v - fpeak_c) / max(fpeak_v, fpeak_c)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(fv, Pv, "C0", lw=1.2, label=f"$v(t)$   peak at f={fpeak_v:.4f} Hz  ω={omega_v:.4f}")
    ax.loglog(fc, Pc, "C1", lw=1.2, label=f"$\\rho_c(t)-\\rho^*$   peak at f={fpeak_c:.4f} Hz  ω={omega_c:.4f}")

    # Mark linearized prediction
    f_linear = linpred["omega"] / (2 * np.pi)
    ax.axvline(f_linear, color="k", ls="--", lw=1, alpha=0.7,
                label=f"linearized prediction  ω={linpred['omega']:.4f}  f={f_linear:.4f}")

    ax.axvline(fpeak_v, color="C0", ls=":", lw=0.8, alpha=0.7)
    ax.axvline(fpeak_c, color="C1", ls=":", lw=0.8, alpha=0.7)

    ax.set_xlabel("frequency (1/time)")
    ax.set_ylabel("power spectral density")
    ax.set_title(f"PSD: v(t) and ρ_center(t) — v-δ frequency match {match_pct:.2f}%  "
                  f"(H={meta['ed_params']['H']:.0f})")
    ax.legend(loc="lower left", fontsize=9)
    ax.grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(outpath, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {outpath}  (match = {match_pct:.3f}%)")
    return dict(fpeak_v=fpeak_v, fpeak_c=fpeak_c,
                omega_v=omega_v, omega_c=omega_c,
                omega_linear=linpred["omega"], match_pct=match_pct)


def fig_harmonic(data, outpath, fpeak_v):
    """Zoom on fundamental + 3x harmonic."""
    meta = data["meta"]
    t = data["t_hist"]
    rho_star = meta["ed_params"]["rho_star"]
    keep = t > 5.0
    t_k = t[keep]
    v_k = data["v_hist"][keep]

    fv, Pv = compute_psd(t_k, v_k, detrend="linear")

    # Estimate amplitude of fundamental vs 3rd harmonic via band integration
    def band_power(f, P, fc, bw_frac=0.2):
        lo = fc * (1 - bw_frac)
        hi = fc * (1 + bw_frac)
        mask = (f >= lo) & (f <= hi)
        return np.trapezoid(P[mask], f[mask])

    P_fund = band_power(fv, Pv, fpeak_v)
    P_h3 = band_power(fv, Pv, 3 * fpeak_v)
    ratio = np.sqrt(P_h3 / P_fund) if P_fund > 0 else 0.0

    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.loglog(fv, Pv, "C0", lw=1.2, label="$v(t)$ PSD")
    ax.axvline(fpeak_v, color="k", ls="--", lw=0.8, alpha=0.7,
                label=f"fundamental f={fpeak_v:.4f}")
    ax.axvline(3 * fpeak_v, color="r", ls="--", lw=0.8, alpha=0.7,
                label=f"3rd harmonic f={3*fpeak_v:.4f}")
    # ED prediction band for 3rd harmonic amplitude: 3-6% of fundamental
    ax.annotate(f"3rd-harmonic amplitude ratio: {100*ratio:.2f}%\n"
                f"ED-predicted band: 3–6%",
                xy=(3 * fpeak_v, P_h3), xytext=(0.02, 0.02),
                textcoords="axes fraction",
                fontsize=10,
                bbox=dict(boxstyle="round,pad=0.4", fc="wheat", ec="gray", alpha=0.85))
    ax.set_xlabel("frequency (1/time)")
    ax.set_ylabel("PSD")
    ax.set_title("Telegraph-modulated PME: v(t) fundamental + 3rd-harmonic check")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(outpath, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {outpath}  (3rd-harmonic amp ratio = {100*ratio:.3f}%)")
    return ratio


def fig_summary(data, outpath, psd_info, harmonic_ratio):
    """Composite 4-panel summary for the memo."""
    meta = data["meta"]
    ep = meta["ed_params"]
    rho_star = ep["rho_star"]
    t_snap = data["t_snap"]
    rho_snap = data["rho_snap"]
    t = data["t_hist"]

    fig = plt.figure(figsize=(13, 9))
    gs = fig.add_gridspec(3, 3, hspace=0.45, wspace=0.32)

    # Top-left + top-middle: field snapshots at t=0, t=mid, t=late
    mid_idx = len(t_snap) // 2
    late_idx = len(t_snap) - 1
    vmin, vmax = -0.2, 0.2
    for col, idx, tlabel in zip(range(3), [0, mid_idx, late_idx],
                                  ["initial", "mid-run", "late"]):
        ax = fig.add_subplot(gs[0, col])
        im = ax.imshow(rho_star - rho_snap[idx].T, origin="lower",
                        extent=[data["x"].min(), data["x"].max(),
                                data["y"].min(), data["y"].max()],
                        cmap="RdBu_r", vmin=vmin, vmax=vmax)
        ax.set_title(f"{tlabel}  (t = {t_snap[idx]:.1f})", fontsize=10)
        if col == 0:
            ax.set_ylabel("y")
        ax.set_xlabel("x")
    cax = fig.add_axes([0.92, 0.71, 0.015, 0.17])
    fig.colorbar(im, cax=cax, label=r"$\rho^* - \rho$")

    # Middle row: time series of v(t) and rho_mean(t)
    ax_v = fig.add_subplot(gs[1, :])
    ax_v.plot(t, data["v_hist"], "C0", lw=0.9, label="$v(t)$")
    ax_v2 = ax_v.twinx()
    ax_v2.plot(t, data["rho_mean_hist"] - rho_star, "C1", lw=0.9, alpha=0.85,
               label=r"$\bar\rho(t) - \rho^*$")
    ax_v.axhline(0, color="k", lw=0.4, alpha=0.4)
    ax_v.set_xlabel("time")
    ax_v.set_ylabel("v(t)", color="C0")
    ax_v2.set_ylabel(r"$\bar\rho - \rho^*$", color="C1")
    ax_v.tick_params(axis="y", labelcolor="C0")
    ax_v2.tick_params(axis="y", labelcolor="C1")
    ax_v.set_title("Participation oscillation coupled with uniform-mode density deviation",
                    fontsize=10)

    # Bottom row: PSD comparison + text box of headline numbers
    ax_psd = fig.add_subplot(gs[2, :2])
    keep = t > 5.0
    fv, Pv = compute_psd(t[keep], data["v_hist"][keep], detrend="linear")
    fc, Pc = compute_psd(t[keep], data["rho_center_hist"][keep] - rho_star,
                          detrend="linear")
    ax_psd.loglog(fv, Pv, "C0", lw=1.2, label="$v(t)$")
    ax_psd.loglog(fc, Pc, "C1", lw=1.2, label=r"$\rho_{\rm center}(t)$")
    ax_psd.axvline(psd_info["fpeak_v"], color="C0", ls=":", lw=0.8, alpha=0.7)
    ax_psd.axvline(psd_info["fpeak_c"], color="C1", ls=":", lw=0.8, alpha=0.7)
    ax_psd.axvline(psd_info["omega_linear"] / (2 * np.pi), color="k",
                    ls="--", lw=1, alpha=0.6, label="linear prediction")
    ax_psd.set_xlabel("frequency")
    ax_psd.set_ylabel("PSD")
    ax_psd.set_title("v–δ frequency match", fontsize=10)
    ax_psd.legend(loc="lower left", fontsize=9)
    ax_psd.grid(True, alpha=0.3, which="both")

    # Text box
    ax_text = fig.add_subplot(gs[2, 2])
    ax_text.axis("off")
    textstr = (
        f"Parameters:\n"
        f"  D={ep['D']}, P₀={ep['P0']}, H={ep['H']}\n"
        f"  ζ={ep['zeta']}, τ={ep['tau']}, β={ep['beta']}\n\n"
        f"Linear prediction:\n"
        f"  ω = {psd_info['omega_linear']:.4f}\n"
        f"  T = {2*np.pi/psd_info['omega_linear']:.2f}\n\n"
        f"Measured:\n"
        f"  ω_v    = {psd_info['omega_v']:.4f}\n"
        f"  ω_δ    = {psd_info['omega_c']:.4f}\n"
        f"  match  = {psd_info['match_pct']:.3f}%\n\n"
        f"3rd harmonic:\n"
        f"  amp ratio = {100*harmonic_ratio:.2f}%\n"
        f"  ED band   = 3–6%\n"
    )
    ax_text.text(0.0, 0.98, textstr, transform=ax_text.transAxes,
                  fontsize=10, verticalalignment="top", family="monospace",
                  bbox=dict(boxstyle="round,pad=0.5", fc="aliceblue", ec="gray"))

    fig.suptitle("Telegraph-modulated PME — Foundational Paper v2 Analogue 5",
                  fontsize=13, y=0.995)
    fig.savefig(outpath, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {outpath}")


if __name__ == "__main__":
    here = Path(__file__).parent
    data = load(here / "analogue5_H50.npz")
    fig_field_snapshots(data, here / "field_snapshots.png")
    fig_time_series(data, here / "time_series.png")
    psd_info = fig_psd(data, here / "psd.png")
    harmonic_ratio = fig_harmonic(data, here / "harmonic.png",
                                    fpeak_v=psd_info["fpeak_v"])
    fig_summary(data, here / "summary.png", psd_info, harmonic_ratio)
    print("\nAll figures generated.")
