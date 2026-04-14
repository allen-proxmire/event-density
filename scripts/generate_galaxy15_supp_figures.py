"""
Supplementary figure generation for ED-Data-Galaxy-15
======================================================
Generates four supplementary figures:
  S1. El Gordo coordinate cross-match
  S2. Wake profile from diffusion equation
  S3. Deceleration correction schematic
  S4. Finner sample TSP distribution
"""

import os
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Circle

OUTDIR = r"C:\Users\allen\GitHub\Event Density\docs\research\ED PAPERS\figures\galaxy15"
os.makedirs(OUTDIR, exist_ok=True)

# Constants
D_T = 2.1e27
kpc = 3.086e19
Gyr = 3.156e16
t_H = 4.35e17

plt.rcParams.update({
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "figure.dpi": 110,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "axes.grid": True,
    "grid.alpha": 0.3,
})


# =========================================================================
# Supplementary Figure S1: El Gordo coordinate cross-match
# =========================================================================
def figS1_el_gordo_crossmatch():
    """
    Show on a sky-plane view:
      - SE BCG (Caminha+2023)
      - SE WL centroid (Jee+2021)
      - Merger axis at PA = 136 deg
      - Decomposition into along-axis (28.7 kpc) and perpendicular (60.5 kpc)
    """
    fig, ax = plt.subplots(figsize=(8, 8))

    # SE BCG position (Caminha+2023)
    ra_bcg = 15.7406934
    dec_bcg = -49.2719924

    # SE WL centroid (Jee+2021)
    ra_wl = 15.73729
    dec_wl = -49.27274

    # Convert to arcsec offsets relative to BCG, with cos(dec)
    cos_dec = math.cos(math.radians(dec_bcg))
    dra = (ra_wl - ra_bcg) * 3600 * cos_dec  # arcsec, +east
    ddec = (dec_wl - dec_bcg) * 3600  # arcsec, +north

    # In sky convention: x-axis = east (positive RA), y-axis = north (positive Dec)
    # Plot
    ax.set_aspect("equal")
    # BCG
    ax.plot(0, 0, marker="*", color="gold", ms=24, mec="black",
            mew=1, zorder=5, label="SE BCG (Caminha+2023)")
    # WL centroid
    ax.plot(dra, ddec, marker="o", color="dodgerblue", ms=14, mec="black",
            mew=0.8, zorder=5, label="SE WL centroid (Jee+2021)")

    # WL uncertainty circle (~5 arcsec)
    wl_circle = Circle((dra, ddec), 5, fill=False, edgecolor="dodgerblue",
                       lw=1, ls="--", alpha=0.7,
                       label="WL 1σ (~5″ ≈ 40 kpc)")
    ax.add_patch(wl_circle)

    # Merger axis: PA = 136 deg (NW-SE line)
    PA = 136
    L = 18
    dx_axis = L * math.sin(math.radians(PA))
    dy_axis = L * math.cos(math.radians(PA))
    ax.plot([-dx_axis, dx_axis], [-dy_axis, dy_axis], "k-",
            lw=1.5, alpha=0.6, label=f"Merger axis (PA = {PA}°)")

    # Annotate NW and SE ends
    ax.text(-dx_axis * 1.05, -dy_axis * 1.05, "NW",
            ha="center", va="center", fontsize=11, weight="bold")
    ax.text(dx_axis * 1.05, dy_axis * 1.05, "SE",
            ha="center", va="center", fontsize=11, weight="bold")

    # Decompose offset
    # Total offset
    ax.annotate("", xy=(dra, ddec), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="firebrick", lw=2))
    ax.text(dra * 0.55 - 1, ddec * 0.55 - 1.5, "Total\n8.44″ = 66.9 kpc",
            color="firebrick", fontsize=9, ha="right")

    # Along-axis component projection
    nw_dir = np.array([math.sin(math.radians(PA + 180)),
                        math.cos(math.radians(PA + 180))])  # NW unit vector
    offset_vec = np.array([dra, ddec])
    along_axis = np.dot(offset_vec, nw_dir)  # positive = NW
    along_pt = nw_dir * along_axis

    # Draw along-axis vector (from origin)
    ax.annotate("", xy=(along_pt[0], along_pt[1]), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="darkgreen", lw=2.5))
    ax.text(along_pt[0] * 0.6 + 0.5, along_pt[1] * 0.6 + 0.5,
            f"Along axis (NW)\n3.62″ = 28.7 kpc",
            color="darkgreen", fontsize=10, ha="left", weight="bold")

    # Perpendicular component
    perp_pt = offset_vec - along_pt
    ax.annotate("", xy=(dra, ddec), xytext=(along_pt[0], along_pt[1]),
                arrowprops=dict(arrowstyle="-|>", color="purple", lw=1.5,
                                ls="dashed"))
    midp = (np.array([dra, ddec]) + along_pt) / 2
    ax.text(midp[0] + 0.5, midp[1], "Perpendicular\n7.62″ = 60.5 kpc",
            color="purple", fontsize=9, ha="left")

    # ED prediction circle around BCG (along-axis, NW direction)
    ed_pred_kpc = 27.2
    ed_arcsec = ed_pred_kpc / 7.933
    ed_pt = nw_dir * ed_arcsec
    ax.plot(ed_pt[0], ed_pt[1], "x", color="darkgreen", ms=14, mew=2.5,
            label=f"ED prediction: 27.2 kpc NW")

    # Compass (north up, east left for astronomical convention -- but we plot east right here)
    ax.text(0.95, 0.05, "N ↑\nE →", transform=ax.transAxes, ha="right",
            va="bottom", fontsize=10,
            bbox=dict(facecolor="white", alpha=0.8, edgecolor="black"))

    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.invert_xaxis()  # standard astronomy: east left, but offsets visible right
    # (actually for "east right" we don't invert; let's keep east-right)
    ax.invert_xaxis()  # double-invert == not inverted; keep east right

    ax.set_xlabel("Δ RA × cos(δ) [arcsec, +east]")
    ax.set_ylabel("Δ Dec [arcsec, +north]")
    ax.set_title("El Gordo SE: WL-BCG offset decomposition\n"
                 "(Jee+2021 WL vs Caminha+2023 BCG)")
    ax.legend(loc="upper left", fontsize=8.5, framealpha=0.92)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, "figS1_el_gordo_crossmatch.png"))
    plt.savefig(os.path.join(OUTDIR, "figS1_el_gordo_crossmatch.pdf"))
    plt.close()
    print("Supp Fig S1 saved.")


# =========================================================================
# Supplementary Figure S2: Wake profile from diffusion equation
# =========================================================================
def figS2_wake_profile():
    """
    Plot the steady-state T(x') profile for several velocities.
    Show the asymmetry between forward (D_T/v) and trailing (v/lambda) decays.
    """
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    # Co-moving coordinate x' (kpc)
    x = np.linspace(-1500, 200, 4000)  # kpc
    x_m = x * kpc

    velocities = [
        (4500, "Bullet (v=4500 km/s)", "#1f77b4"),
        (2500, "El Gordo (v=2500 km/s)", "#2ca02c"),
        (1500, "Musket Ball (v=1500 km/s)", "#d62728"),
        (500, "Decelerated (v=500 km/s)", "#9467bd"),
    ]

    # ---- Left panel: T-field profile ----
    ax = axes[0]
    lam = 1.0 / t_H
    for v_kms, label, c in velocities:
        v = v_kms * 1e3  # m/s
        # Forward decay length: ell_+ = D_T / v
        ell_plus = D_T / v
        # Trailing decay length: ell_- = v / lambda (in v^2 >> 4 D_T lambda limit)
        ell_minus = v / lam

        # T-field (arbitrary normalization)
        T = np.where(x_m > 0,
                     np.exp(-x_m / ell_plus),
                     np.exp(x_m / ell_minus))

        ax.plot(x, T, color=c, lw=2, label=label)

        # Annotate forward and trailing scales (only for Bullet)
        if v_kms == 4500:
            ax.annotate(f"ℓ_+ = D_T/v = {ell_plus/kpc:.1f} kpc",
                        xy=(ell_plus/kpc, np.exp(-1)),
                        xytext=(80, 0.5),
                        arrowprops=dict(arrowstyle="->", color=c),
                        fontsize=9, color=c)

    # Source position
    ax.axvline(0, color="black", ls="-", lw=1, alpha=0.5)
    ax.text(0, 1.05, "Source\n(BCG)", ha="center", fontsize=9)

    # Direction of motion
    ax.annotate("", xy=(180, 0.85), xytext=(80, 0.85),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=2))
    ax.text(130, 0.92, "v", fontsize=12, ha="center", weight="bold")

    # Trailing wake region
    ax.axvspan(-1500, 0, alpha=0.05, color="green")
    ax.text(-1000, 0.6, "Wake (trailing)", color="darkgreen", fontsize=10,
            ha="center", style="italic")

    ax.set_xlim(-1500, 200)
    ax.set_ylim(0, 1.1)
    ax.set_xlabel("x' = x − x_source [kpc] (negative = behind source)")
    ax.set_ylabel("T(x') / T(0)  (normalized)")
    ax.set_title("(a) Steady-state wake profile — full extent")
    ax.legend(loc="upper left", fontsize=9)

    # ---- Right panel: zoomed-in view of the asymmetric region ----
    ax = axes[1]
    x_zoom = np.linspace(-200, 200, 2000)
    x_m_zoom = x_zoom * kpc

    for v_kms, label, c in velocities:
        v = v_kms * 1e3
        ell_plus = D_T / v
        ell_minus = v / lam

        T = np.where(x_m_zoom > 0,
                     np.exp(-x_m_zoom / ell_plus),
                     np.exp(x_m_zoom / ell_minus))
        ax.plot(x_zoom, T, color=c, lw=2, label=label)

        # Mark the forward-decay length
        ax.axvline(D_T / v / kpc, color=c, ls=":", lw=1, alpha=0.6)

    ax.axvline(0, color="black", ls="-", lw=1, alpha=0.5)
    ax.text(0, 1.05, "Source", ha="center", fontsize=9)

    # Direction
    ax.annotate("", xy=(150, 0.85), xytext=(70, 0.85),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=2))
    ax.text(110, 0.92, "v", fontsize=12, ha="center", weight="bold")

    ax.set_xlim(-200, 200)
    ax.set_ylim(0, 1.1)
    ax.set_xlabel("x' [kpc]")
    ax.set_ylabel("T(x') / T(0)")
    ax.set_title("(b) Inner ±200 kpc — asymmetry sets observable offset")
    ax.legend(loc="upper left", fontsize=9)

    fig.suptitle("ED temporal-tension wake T(x') from the diffusion equation\n"
                 "$\\partial_t T = D_T \\nabla^2 T + S - \\lambda T$ "
                 "(steady state, $v^2 \\gg 4 D_T \\lambda$)",
                 fontsize=12, y=1.02)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, "figS2_wake_profile.png"))
    plt.savefig(os.path.join(OUTDIR, "figS2_wake_profile.pdf"))
    plt.close()
    print("Supp Fig S2 saved.")


# =========================================================================
# Supplementary Figure S3: Deceleration correction schematic
# =========================================================================
def figS3_deceleration_schematic():
    """
    Schematic showing how v_current(t) drops after pericenter,
    and how the corresponding wake length grows.
    """
    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    t = np.linspace(0, 1.2, 500)  # Gyr
    T_apo = 1.0  # Gyr

    # Velocity curves for different v_peri
    velocities = [
        (4500, "Bullet (v_peri = 4500)", "#1f77b4"),
        (2500, "El Gordo (v_peri = 2500)", "#2ca02c"),
        (1500, "Musket Ball (v_peri = 1500)", "#d62728"),
    ]

    # ---- Top panel: v_current(t) ----
    ax = axes[0]
    for vp, label, c in velocities:
        # Keplerian-like deceleration
        ratio = np.minimum(t / T_apo, 1.0)
        vc = vp * np.sqrt(np.maximum(0, 1 - ratio ** 2))
        ax.plot(t, vc, color=c, lw=2.5, label=label)

    # Mark TSP locations of clusters
    cluster_marks = [
        ("Bullet", 0.15, 4500),
        ("El Gordo", 0.75, 2500),
        ("Musket Ball", 0.96, 1500),
    ]
    for name, tsp, vp in cluster_marks:
        ratio = min(tsp / T_apo, 1.0)
        vc = vp * math.sqrt(max(0, 1 - ratio ** 2))
        ax.plot(tsp, vc, "ko", ms=10, mec="white", mew=1, zorder=5)
        ax.annotate(name, xy=(tsp, vc), xytext=(tsp + 0.03, vc + 200),
                    fontsize=9)

    ax.set_ylabel(r"$v_{\rm current}(t)$ [km/s]")
    ax.set_title("(a) Subcluster current velocity vs time since pericenter")
    ax.legend(loc="upper right", fontsize=10)
    ax.set_ylim(0, 5000)

    # Annotate
    ax.text(0.05, 4500, r"$v_{\rm current}(t) = v_{\rm peri} \sqrt{1 - (t/T_{\rm apo})^2}$",
            fontsize=11, bbox=dict(facecolor="white", alpha=0.85))

    # ---- Bottom panel: ℓ(t) = D_T / v_current ----
    ax = axes[1]
    for vp, label, c in velocities:
        ratio = np.minimum(t / T_apo, 1.0)
        vc_safe = np.maximum(vp * np.sqrt(np.maximum(0, 1 - ratio ** 2)),
                             50)  # floor at 50 km/s to avoid divergence
        ell = D_T / (vc_safe * 1e3) / kpc
        ax.plot(t, ell, color=c, lw=2.5, label=label)

    # Mark cluster locations
    for name, tsp, vp in cluster_marks:
        ratio = min(tsp / T_apo, 1.0)
        vc = max(vp * math.sqrt(max(0, 1 - ratio ** 2)), 50)
        ell = D_T / (vc * 1e3) / kpc
        ax.plot(tsp, ell, "ko", ms=10, mec="white", mew=1, zorder=5)

    # ED predicted ℓ at v_peri (Galaxy-13 prediction): horizontal lines
    for vp, _, c in velocities:
        ell_peri = D_T / (vp * 1e3) / kpc
        ax.axhline(ell_peri, color=c, ls=":", lw=1.5, alpha=0.6)

    ax.set_xlabel("Time since pericenter (TSP) [Gyr]")
    ax.set_ylabel(r"$\ell = D_T / v_{\rm current}$ [kpc]")
    ax.set_title("(b) Wake length grows as subcluster decelerates")
    ax.set_yscale("log")
    ax.set_ylim(5, 1000)
    ax.legend(loc="upper left", fontsize=10)

    ax.text(0.02, 7,
            "Dotted lines: Galaxy-13 prediction at $v_{\\rm peri}$\n"
            "Solid curves: corrected ED prediction $\\ell = D_T / v_{\\rm current}$",
            fontsize=9, bbox=dict(facecolor="lightyellow", alpha=0.85))

    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, "figS3_deceleration_schematic.png"))
    plt.savefig(os.path.join(OUTDIR, "figS3_deceleration_schematic.pdf"))
    plt.close()
    print("Supp Fig S3 saved.")


# =========================================================================
# Supplementary Figure S4: TSP distribution of the Finner sample
# =========================================================================
def figS4_finner_TSP_distribution():
    """
    Histogram of TSP estimates for the Finner+25 / Golovich+19 radio-relic sample.
    Shows the TSP-narrow selection that justifies the flat v_peri scaling.
    """
    # TSP estimates for the Finner clusters (where available, mostly from Golovich)
    finner_TSP = [
        # Cluster, TSP (Gyr), source
        ("Toothbrush",     1.3, "Bruggen+12"),
        ("A115",           0.1, "Barrena+07 pre-peri"),
        ("A1240",          0.3, "Barrena+09"),
        ("A2034",          0.20, "Monteiro-Oliveira+18"),
        ("A2163",          0.5, "Bourdin+11"),
        ("A2255",          0.15, "Sakelliou+06"),
        ("A2744 (N-S)",    0.55, "Cerini+24"),
        ("A3365",          0.6, "Urdampilleta+21"),
        ("A3411",          1.0, "van Weeren+17"),
        ("CIZA J2242",     1.0, "Donnert+17"),
        ("MACS J1149",     1.16, "Golovich+16 MCMAC"),
        ("ZwCl 0008",      0.76, "Golovich+17 MCMAC"),
        ("ZwCl 2341",      0.5, "Benson+17"),
    ]
    tsp_vals = np.array([d[1] for d in finner_TSP])

    # Compare to high-precision sample
    hp_TSP = [
        ("Bullet", 0.15),
        ("MACS J0025", 0.50),
        ("El Gordo SE", 0.75),
        ("Musket Ball S", 0.96),
    ]
    hp_vals = np.array([d[1] for d in hp_TSP])

    fig, ax = plt.subplots(figsize=(10, 5.5))

    bins = np.linspace(0, 1.5, 16)
    ax.hist(tsp_vals, bins=bins, color="#1f77b4", alpha=0.65, edgecolor="black",
            label=f"Finner+25 sample (N={len(tsp_vals)})")
    ax.hist(hp_vals, bins=bins, color="#d62728", alpha=0.85, edgecolor="black",
            label=f"High-precision sample (N={len(hp_vals)})")

    # Mean and median lines
    ax.axvline(np.median(tsp_vals), color="#1f77b4", ls="--", lw=2,
               label=f"Finner median TSP = {np.median(tsp_vals):.2f} Gyr")
    ax.axvline(np.std(tsp_vals), color="#1f77b4", ls=":", lw=1, alpha=0)
    # Span of Finner sample
    ax.axvspan(np.percentile(tsp_vals, 25), np.percentile(tsp_vals, 75),
               color="#1f77b4", alpha=0.10,
               label=f"Finner IQR: {np.percentile(tsp_vals,25):.2f}–"
                     f"{np.percentile(tsp_vals,75):.2f} Gyr")

    ax.set_xlabel("Time since pericenter (TSP) [Gyr]")
    ax.set_ylabel("Number of clusters")
    ax.set_title("TSP distribution of cluster samples\n"
                 "Finner+25 sample is TSP-narrow (median ~0.6 Gyr) "
                 "→ v_current is more uniform than v_peri")
    ax.legend(loc="upper right", fontsize=9)

    # Annotation: explanation
    ax.text(0.02, 0.95,
            "ED interpretation:\n"
            "Radio-relic selection requires post-pericenter shocks,\n"
            "so the Finner sample is concentrated at TSP ~ 0.5–1.0 Gyr.\n"
            "Within this narrow window, v_current is approximately\n"
            "uniform (~500–1000 km/s) regardless of v_peri.\n"
            "Result: ℓ depends weakly on v_peri (n ≈ 0)\n"
            "but matches the ED prediction at typical v_current.",
            transform=ax.transAxes, fontsize=9, va="top",
            bbox=dict(facecolor="lightyellow", alpha=0.9))

    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, "figS4_finner_TSP_distribution.png"))
    plt.savefig(os.path.join(OUTDIR, "figS4_finner_TSP_distribution.pdf"))
    plt.close()
    print("Supp Fig S4 saved.")


# =========================================================================
# Main
# =========================================================================
if __name__ == "__main__":
    print(f"Output directory: {OUTDIR}")
    print()
    figS1_el_gordo_crossmatch()
    figS2_wake_profile()
    figS3_deceleration_schematic()
    figS4_finner_TSP_distribution()
    print()
    print("All supplementary figures saved.")
