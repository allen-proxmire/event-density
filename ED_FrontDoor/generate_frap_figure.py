"""
Generate a publication-ready schematic comparing FRAP front propagation
under Fickian diffusion vs degenerate-mobility (PME) diffusion.

Output: outputs/figures/frap_predicted_vs_fickian.png
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def main():
    # ── Parameters ─────────────────────────────────────────────────
    alpha_fick = 0.50
    alpha_deg = 0.16  # BSA at beta = 2.12, d = 2
    t = np.logspace(np.log10(0.1), np.log10(100), 500)

    # Anchor both curves at the bleach radius R0 at t0
    R0 = 3.0   # um, bleach radius
    t0 = 0.1   # s, start of recovery

    R_fick = R0 * (t / t0) ** alpha_fick
    R_deg  = R0 * (t / t0) ** alpha_deg

    # Highlight point
    t_hi = 10.0
    R_fick_hi = R0 * (t_hi / t0) ** alpha_fick
    R_deg_hi  = R0 * (t_hi / t0) ** alpha_deg

    # ── Figure ─────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(8, 5.5))

    # Curves
    ax.loglog(t, R_fick, "-", color="#2563EB", linewidth=2.5,
              label=f"Fickian  ($\\alpha = {alpha_fick:.2f}$)", zorder=3)
    ax.loglog(t, R_deg, "-", color="#DC2626", linewidth=2.5,
              label=f"Degenerate mobility  ($\\alpha = {alpha_deg:.2f}$,"
                    f"  $\\beta = 2.12$)", zorder=3)

    # Shaded region between curves at t = 10
    t_band = t[(t >= 0.5) & (t <= 60)]
    R_fick_band = R0 * (t_band / t0) ** alpha_fick
    R_deg_band  = R0 * (t_band / t0) ** alpha_deg
    ax.fill_between(t_band, R_deg_band, R_fick_band,
                    color="#7C3AED", alpha=0.08, zorder=1)

    # Vertical span at t = 10
    ax.vlines(t_hi, R_deg_hi, R_fick_hi, colors="#7C3AED",
              linewidth=1.5, linestyles=":", zorder=2)
    ax.plot(t_hi, R_fick_hi, "s", color="#2563EB", markersize=7, zorder=4)
    ax.plot(t_hi, R_deg_hi, "s", color="#DC2626", markersize=7, zorder=4)

    # Annotation: factor of ~3
    mid_y = np.sqrt(R_fick_hi * R_deg_hi)
    ax.annotate(
        f"  {R_fick_hi / R_deg_hi:.1f}x difference\n"
        f"  at $t = {t_hi:.0f}$ s",
        xy=(t_hi, mid_y), fontsize=9.5, color="#7C3AED",
        fontweight="bold", va="center",
        xytext=(28, 0), textcoords="offset points",
    )

    # Labels
    ax.set_xlabel("Time  $t$  (s)", fontsize=12)
    ax.set_ylabel("Recovery front radius  $R(t)$  ($\\mu$m)", fontsize=12)
    ax.set_title(
        "FRAP front propagation:  Fickian vs degenerate mobility",
        fontsize=13, fontweight="bold", pad=12,
    )

    ax.legend(fontsize=10, loc="upper left", framealpha=0.95,
              edgecolor="#D1D5DB")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=10)
    ax.set_xlim(0.08, 120)
    ax.set_ylim(2, 120)

    # ── Inset: bleach-boundary shape ───────────────────────────────
    inset = fig.add_axes([0.55, 0.15, 0.38, 0.32])  # [left, bottom, w, h]

    x = np.linspace(-3, 3, 600)
    R_bleach = 1.0  # normalised bleach radius

    # Fickian profile: Gaussian recovery (1 - exp(-r^2/2sigma^2))
    # i.e. concentration is LOW inside bleach, HIGH outside
    # Show the fluorescence intensity profile at a mid-recovery time
    sigma = 1.3  # broadened bleach
    fick_profile = 1.0 - 0.7 * np.exp(-x ** 2 / (2 * sigma ** 2))

    # Degenerate mobility: compact-support recovery
    # Sharp boundary at |x| = R_bleach
    deg_profile = np.where(
        np.abs(x) < R_bleach,
        0.3 + 0.0 * x,   # still bleached inside
        1.0 + 0.0 * x,   # fully recovered outside
    )
    # Smooth the transition very slightly for visual clarity (real front
    # is sharp but continuous)
    from scipy.ndimage import uniform_filter1d
    deg_profile = uniform_filter1d(deg_profile.astype(float), size=8)

    inset.fill_between(x, fick_profile, 0, alpha=0.15, color="#2563EB")
    inset.plot(x, fick_profile, "-", color="#2563EB", linewidth=1.8,
               label="Fickian")
    inset.fill_between(x, deg_profile, 0, alpha=0.15, color="#DC2626")
    inset.plot(x, deg_profile, "-", color="#DC2626", linewidth=1.8,
               label="PME")

    inset.set_xlim(-2.8, 2.8)
    inset.set_ylim(0, 1.25)
    inset.set_xlabel("Position", fontsize=8, labelpad=2)
    inset.set_ylabel("Fluorescence", fontsize=8, labelpad=2)
    inset.set_title("Bleach boundary shape", fontsize=8.5,
                    fontweight="bold", pad=4)
    inset.tick_params(labelsize=7)
    inset.legend(fontsize=7, loc="upper left", framealpha=0.9,
                 handlelength=1.2)
    inset.spines["top"].set_visible(False)
    inset.spines["right"].set_visible(False)

    # Annotations inside inset
    inset.annotate("Gaussian\ntail", xy=(1.8, 0.72), fontsize=6.5,
                   color="#2563EB", ha="center", fontstyle="italic")
    inset.annotate("Sharp\nfront", xy=(-1.6, 0.72), fontsize=6.5,
                   color="#DC2626", ha="center", fontstyle="italic")

    # ── Save ───────────────────────────────────────────────────────
    script_dir = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.join(script_dir, "..", "outputs", "figures")
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "frap_predicted_vs_fickian.png")
    fig.savefig(outpath, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close()

    print(f"Saved: {outpath}")
    print(f"Size:  {os.path.getsize(outpath) / 1024:.0f} KB")
    print(f"\nAt t = {t_hi:.0f} s:")
    print(f"  Fickian R = {R_fick_hi:.1f} um")
    print(f"  PME     R = {R_deg_hi:.1f} um")
    print(f"  Ratio     = {R_fick_hi / R_deg_hi:.1f}x")


if __name__ == "__main__":
    main()
