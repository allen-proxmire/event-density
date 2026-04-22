"""
Generate the combined solver-independence figure and the summary table.

Loads the 12 .npz files (2 solvers x 3 H x 2 regimes), extracts peak omega_v,
and produces:

 1. omega_vs_H.png  -- main figure: omega(H) with linear theory curve,
    FPv2 54% curve, and measured points for both solvers in both regimes
 2. time_series_comparison.png  -- v(t) overlaid for a single H value,
    showing both solvers produce essentially the same trajectory
 3. summary_table.txt  -- the quantitative results
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch, detrend as sp_detrend


def load_npz(path):
    d = np.load(path, allow_pickle=True)
    out = {k: d[k] for k in d.files}
    out["meta"] = eval(str(out["meta_json"]))
    return out


def compute_psd(t, y, detrend="linear"):
    y = np.asarray(y, dtype=np.float64)
    if detrend == "linear":
        y = sp_detrend(y, type="linear")
    dt = float(t[1] - t[0])
    fs = 1.0 / dt
    nperseg = min(len(y), 2048)
    f, P = welch(y, fs=fs, nperseg=nperseg, window="hann")
    return f, P


def peak_omega(t, v, band_hz=(0.01, 0.3)):
    keep = t > 5.0
    if keep.sum() < 100:
        return np.nan, np.nan
    f, P = compute_psd(t[keep], v[keep])
    mask = (f >= band_hz[0]) & (f <= band_hz[1])
    if mask.sum() == 0:
        return np.nan, np.nan
    idx = np.argmax(P[mask])
    f_peak = f[mask][idx]
    return 2 * np.pi * f_peak, P[mask][idx]


def analyze_run(path):
    d = load_npz(path)
    ep = d["meta"]["ed_params"]
    H = ep["H"]
    linpred = d["meta"]["linpred"]
    t = d["t_hist"]
    v = d["v_hist"]

    # Check for runaway
    v_absmax = np.abs(v).max()
    v_final = v[-1]
    runaway = v_absmax > 1.0   # physical runaway if |v| exceeds O(1)

    omega, power = peak_omega(t, v)
    return dict(H=H, solver=d["meta"]["solver"],
                linpred=linpred,
                omega_linear=linpred["omega"],
                omega_measured=omega,
                v_absmax=v_absmax,
                v_final=v_final,
                runaway=runaway,
                t=t, v=v)


def main():
    here = Path(__file__).parent
    regimes = ["linear", "nonlinear"]
    solvers = [("spec", "spectral_ETDRK2"), ("bdf", "MOL_BDF")]
    H_values = [10, 20, 50]

    results = {}
    for reg in regimes:
        for tag, sname in solvers:
            for H in H_values:
                path = here / f"{tag}_H{H:02d}_{reg}.npz"
                key = (reg, sname, H)
                results[key] = analyze_run(path)

    # Print summary table
    fp_nonlinear = {10: 0.1662, 20: 0.2400, 50: 0.3842}
    lines = []
    lines.append("=" * 110)
    lines.append(f"{'Regime':<12}{'Solver':<22}{'H':>6}{'omega_linear':>14}"
                 f"{'omega_meas':>14}{'meas/lin':>12}{'|v|_max':>12}{'runaway?':>12}")
    lines.append("-" * 110)
    for reg in regimes:
        for tag, sname in solvers:
            for H in H_values:
                r = results[(reg, sname, H)]
                rstr = "YES" if r["runaway"] else "no"
                ratio = (r["omega_measured"] / r["omega_linear"]
                         if not np.isnan(r["omega_measured"]) else float("nan"))
                lines.append(f"{reg:<12}{sname:<22}{H:>6d}{r['omega_linear']:>14.4f}"
                             f"{r['omega_measured']:>14.4f}{ratio:>12.3f}"
                             f"{r['v_absmax']:>12.2e}{rstr:>12}")
        lines.append("-" * 110)
    lines.append(f"Reference: FPv2 §8.4 nonlinear measurements")
    for H in H_values:
        om_lin = results[("linear", "spectral_ETDRK2", H)]["omega_linear"]
        lines.append(f"    H={H}: ω_FPv2 = {fp_nonlinear[H]:.4f}  "
                     f"ratio to linear = {fp_nonlinear[H]/om_lin:.3f}")
    lines.append("=" * 110)
    summary_text = "\n".join(lines)
    print(summary_text)
    (here / "summary_table.txt").write_text(summary_text, encoding="utf-8")

    # ----- Figure 1: omega vs H for both regimes, both solvers -----
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

    # Dense H-range for theory curves
    ep0 = results[("linear", "spectral_ETDRK2", 10)]
    D, P0, zeta, tau = 0.3, 0.01, 0.1, 1.0
    gamma = (D * P0 + zeta / tau) / 2
    H_dense = np.logspace(0, 2, 200)
    omega_lin_dense = np.sqrt((D * P0 * zeta + H_dense * P0) / tau - gamma ** 2)

    for ax, reg in zip(axes, regimes):
        ax.plot(H_dense, omega_lin_dense, "k-", lw=1.5, alpha=0.8,
                 label="Linear theory ω = √((DP₀ζ + HP₀)/τ − γ²)")
        ax.plot(H_dense, 0.54 * omega_lin_dense, "k--", lw=1.2, alpha=0.6,
                 label="FPv2 §8.4 reference: 0.54 × linear")
        # FPv2 points
        H_vals = np.array(H_values)
        omega_fp = np.array([fp_nonlinear[h] for h in H_vals])
        ax.plot(H_vals, omega_fp, "ks", markersize=9, markerfacecolor="grey",
                 label="FPv2 §8.4 reported values")

        # Solver 1: spectral
        om_spec = np.array([results[(reg, "spectral_ETDRK2", h)]["omega_measured"]
                             for h in H_values])
        ra_spec = np.array([results[(reg, "spectral_ETDRK2", h)]["runaway"]
                             for h in H_values])
        # Solver 2: BDF
        om_bdf = np.array([results[(reg, "MOL_BDF", h)]["omega_measured"]
                            for h in H_values])
        ra_bdf = np.array([results[(reg, "MOL_BDF", h)]["runaway"]
                            for h in H_values])

        valid_spec = ~np.isnan(om_spec) & ~ra_spec
        ax.plot(H_vals[valid_spec], om_spec[valid_spec], "o",
                 color="C0", markersize=14,
                 label="Spectral ETDRK2 (valid)")
        if ra_spec.any():
            ax.plot(H_vals[ra_spec], np.nan_to_num(om_spec[ra_spec]), "x",
                     color="C0", markersize=14, mew=2,
                     label="Spectral ETDRK2 (runaway — unreliable)")

        valid_bdf = ~np.isnan(om_bdf) & ~ra_bdf
        ax.plot(H_vals[valid_bdf], om_bdf[valid_bdf], "^",
                 color="C3", markersize=12,
                 label="MOL-BDF (valid)")
        if ra_bdf.any():
            ax.plot(H_vals[ra_bdf], np.nan_to_num(om_bdf[ra_bdf]), "x",
                     color="C3", markersize=14, mew=2,
                     label="MOL-BDF (runaway — unreliable)")

        ax.set_xscale("log")
        ax.set_xlabel("H  (participation coupling strength)")
        if reg == "linear":
            ax.set_ylabel("ω  (oscillation frequency)")
        ax.set_title(f"{reg.capitalize()} regime  (amp = "
                      f"{'0.2' if reg == 'linear' else '0.45'}, "
                      f"σ = {'0.15' if reg == 'linear' else '0.30'})")
        ax.legend(fontsize=8, loc="upper left")
        ax.grid(True, alpha=0.3, which="both")
        ax.set_ylim(0.0, 1.0)
        ax.set_xlim(8, 70)

    fig.suptitle("Solver-Independence Test — ω(H) measured by two independent solvers "
                  "vs linear theory vs FPv2 §8.4", fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    figpath = here / "omega_vs_H.png"
    fig.savefig(figpath, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"\nWrote {figpath}")

    # ----- Figure 2: time-series overlay for a single H (linear regime) -----
    fig, axes = plt.subplots(3, 1, figsize=(12, 9), sharex=True)
    for ax, H in zip(axes, H_values):
        r_sp = results[("linear", "spectral_ETDRK2", H)]
        r_bdf = results[("linear", "MOL_BDF", H)]
        ax.plot(r_sp["t"], r_sp["v"], "C0", lw=0.8,
                 label=f"Spectral ETDRK2  ω={r_sp['omega_measured']:.4f}")
        ax.plot(r_bdf["t"], r_bdf["v"], "C3", lw=0.8, alpha=0.75,
                 label=f"MOL-BDF          ω={r_bdf['omega_measured']:.4f}")
        ax.axhline(0, color="k", lw=0.3, alpha=0.4)
        ax.set_ylabel(f"v(t),  H={H}")
        ax.set_title(f"H = {H}   (linear prediction ω = {r_sp['omega_linear']:.4f})",
                      fontsize=10)
        ax.legend(loc="upper right", fontsize=9)
        ax.grid(True, alpha=0.3)
    axes[-1].set_xlabel("time")
    fig.suptitle("Solver-Independence Test — v(t) time series, linear regime, both solvers",
                  fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    figpath2 = here / "time_series_comparison.png"
    fig.savefig(figpath2, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {figpath2}")

    return results


if __name__ == "__main__":
    main()
