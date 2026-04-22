"""
v1.2 H-sweep combined figure.

Loads the three simulation .npz files (H=10, 20, 50), extracts peak omega_v,
and produces a two-panel composite:

  (A) v(t) time series overlaid for the three H values
  (B) PSD of v(t) for the three H values, with measured peaks,
      linear-prediction bands, and Foundational Paper v2 reported values

Also produces a table-style PNG summarizing the numbers.
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from make_figures import load, compute_psd


def peak_in_band(f, P, band=(0.01, 0.3)):
    mask = (f >= band[0]) & (f <= band[1])
    idx = np.argmax(P[mask])
    return f[mask][idx], P[mask][idx]


def analyze_run(npz_path):
    data = load(npz_path)
    t = data["t_hist"]
    rho_star = data["meta"]["ed_params"]["rho_star"]
    H = data["meta"]["ed_params"]["H"]
    linpred = data["meta"]["linpred"]

    keep = t > 5.0
    fv, Pv = compute_psd(t[keep], data["v_hist"][keep], detrend="linear")
    fc, Pc = compute_psd(t[keep], data["rho_center_hist"][keep] - rho_star,
                          detrend="linear")

    fpeak_v, Ppeak_v = peak_in_band(fv, Pv)
    fpeak_c, Ppeak_c = peak_in_band(fc, Pc)

    return dict(H=H, data=data,
                fv=fv, Pv=Pv, fc=fc, Pc=Pc,
                fpeak_v=fpeak_v, omega_v=2 * np.pi * fpeak_v,
                fpeak_c=fpeak_c, omega_c=2 * np.pi * fpeak_c,
                linpred=linpred,
                t=t[keep], v=data["v_hist"][keep])


def main():
    here = Path(__file__).parent
    outdir = here / "v1.2_H_sweep"
    runs = []
    for H in [10, 20, 50]:
        runs.append(analyze_run(outdir / f"analogue5_H{H:02d}.npz"))

    # Foundational Paper v2 §8.4 reported nonlinear measurements
    fp_nonlinear = {10: 0.1662, 20: 0.2400, 50: 0.3842}

    # Main composite figure
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # (A) v(t) overlay
    ax = axes[0]
    colors = ["C0", "C1", "C2"]
    for r, c in zip(runs, colors):
        # Normalize to max absolute amplitude so we can compare frequencies at a glance
        t, v = r["t"], r["v"]
        vnorm = v / max(abs(v).max(), 1e-12)
        ax.plot(t, vnorm, c, lw=0.8,
                label=f"H = {r['H']:.0f}  (ω_lin = {r['linpred']['omega']:.3f}, "
                      f"measured ω = {r['omega_v']:.3f})")
    ax.axhline(0, color="k", lw=0.3, alpha=0.4)
    ax.set_xlabel("time")
    ax.set_ylabel("v(t) / |v|_max  (normalized)")
    ax.set_title("Participation oscillation at three H values (linear regime)")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 100)  # zoom to show oscillations clearly

    # (B) PSD comparison
    ax = axes[1]
    for r, c in zip(runs, colors):
        ax.loglog(r["fv"], r["Pv"], c, lw=1.1,
                   label=f"H={r['H']:.0f}  peak at f={r['fpeak_v']:.4f}  ω={r['omega_v']:.4f}")
        # mark linear prediction
        f_lin = r["linpred"]["omega"] / (2 * np.pi)
        ax.axvline(f_lin, color=c, ls="--", lw=0.9, alpha=0.6)
        # mark Foundational Paper reported nonlinear value
        if r["H"] in fp_nonlinear:
            f_fp = fp_nonlinear[r["H"]] / (2 * np.pi)
            ax.axvline(f_fp, color=c, ls=":", lw=0.9, alpha=0.8)

    ax.set_xlabel("frequency (1/time)")
    ax.set_ylabel("PSD of v(t)")
    ax.set_title("PSD: measured ω vs linear prediction (dashed) vs FPv2 §8 reported (dotted)")
    ax.set_xlim(0.01, 1.0)
    ax.legend(loc="lower left", fontsize=8)
    ax.grid(True, alpha=0.3, which="both")

    # Annotation box
    ann_text = ("Dashed: linearized eigenmode prediction.\n"
                "Dotted: Foundational Paper v2 §8.4 nonlinear measurement.\n\n"
                "Measured peaks match the DASHED (linear) prediction at all three H.\n"
                "The DOTTED (nonlinear) values are NOT reproduced in these sims\n"
                "— consistent with the v1.1 analysis: our explicit-Euler +\n"
                "Gaussian-IC protocol stays in the linear regime.")
    fig.text(0.52, -0.02, ann_text, fontsize=9,
             bbox=dict(boxstyle="round,pad=0.5", fc="lemonchiffon", ec="gray"))

    fig.suptitle("Telegraph-Modulated PME: H-sweep (v1.2, linear regime)", fontsize=13)
    fig.tight_layout(rect=[0, 0.07, 1, 0.96])
    figpath = outdir / "H_sweep_summary.png"
    fig.savefig(figpath, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {figpath}")

    # Scaling plot: omega_measured vs sqrt(H) compared to theory
    fig, ax = plt.subplots(figsize=(8, 6))
    H_vals = np.array([r["H"] for r in runs])
    omega_meas = np.array([r["omega_v"] for r in runs])
    omega_lin = np.array([r["linpred"]["omega"] for r in runs])
    omega_fp = np.array([fp_nonlinear[int(h)] for h in H_vals])

    # Dense H range for theory
    H_dense = np.linspace(1, 100, 200)
    ep_params = runs[0]["data"]["meta"]["ed_params"]
    D, P0, zeta, tau = (ep_params["D"], ep_params["P0"],
                         ep_params["zeta"], ep_params["tau"])
    gamma = (D * P0 + zeta / tau) / 2
    omega_lin_dense = np.sqrt((D * P0 * zeta + H_dense * P0) / tau - gamma ** 2)
    # FP reports roughly omega_fp = 0.54 * omega_lin -> dashed line
    omega_fp_dense = 0.54 * omega_lin_dense

    ax.plot(H_dense, omega_lin_dense, "k-", lw=1.5, alpha=0.7,
             label="Linearized theory: ω = √((DP₀ζ + HP₀)/τ − γ²)")
    ax.plot(H_dense, omega_fp_dense, "k:", lw=1.2, alpha=0.6,
             label="FPv2 §8.4 reported nonlinear (54% of linear)")
    ax.plot(H_vals, omega_meas, "o", color="C0", markersize=12,
             label=f"Measured ω_v (N={len(H_vals)} runs)", zorder=5)
    ax.plot(H_vals, omega_fp, "s", color="C3", markersize=10, alpha=0.6,
             label="FPv2 §8.4 reported values", zorder=4)

    ax.set_xscale("log")
    ax.set_xlabel("H (participation coupling strength)")
    ax.set_ylabel("ω  (oscillation frequency)")
    ax.set_title("Telegraph-modulated PME: ω(H) scaling — measured vs linear vs FPv2")
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(True, alpha=0.3, which="both")

    scaling_path = outdir / "omega_vs_H.png"
    fig.tight_layout()
    fig.savefig(scaling_path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {scaling_path}")

    # Print the measurements table
    print("\n" + "=" * 78)
    print(f"{'H':>6} | {'omega_lin':>12} | {'omega_meas':>12} | "
          f"{'omega_FPv2':>12} | {'meas/lin':>10} | {'FPv2/lin':>10}")
    print("-" * 78)
    for r in runs:
        H = r["H"]
        om_lin = r["linpred"]["omega"]
        om_meas = r["omega_v"]
        om_fp = fp_nonlinear[int(H)]
        print(f"{H:>6.0f} | {om_lin:>12.4f} | {om_meas:>12.4f} | "
              f"{om_fp:>12.4f} | {om_meas/om_lin:>10.3f} | {om_fp/om_lin:>10.3f}")
    print("=" * 78)

    return runs


if __name__ == "__main__":
    main()
