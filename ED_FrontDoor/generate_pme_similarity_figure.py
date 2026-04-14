"""
Generate a publication-ready figure of the Barenblatt-Pattle similarity
solution for the porous-medium equation with m = beta + 1, beta = 1.69.

The exact 1-D Barenblatt solution is:

    u(x,t) = t^{alpha_rho} * [ C - k * (x / t^{alpha_R})^2 ]_+^{1/(m-1)}

where
    alpha_R   = 1 / (d*(m-1) + 2)      (front-radius exponent)
    alpha_rho = -d * alpha_R            (peak-density exponent, d=1)
    k         = alpha_R * (m-1) / (2*d*m)
    C         is set by the conserved mass M = int u dx

Output: outputs/figures/pme_similarity_solution.png
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def barenblatt_1d(x, t, m, M=1.0):
    """Exact Barenblatt-Pattle solution in 1-D.

    Parameters
    ----------
    x : array  — spatial coordinate
    t : float  — time (must be > 0)
    m : float  — PME exponent (> 1)
    M : float  — conserved mass

    Returns
    -------
    u : array  — density profile
    R : float  — front position (compact-support radius)
    """
    d = 1
    alpha_R = 1.0 / (d * (m - 1) + 2)
    alpha_rho = -d * alpha_R  # negative: peak decays

    k = alpha_R * (m - 1) / (2 * d * m)

    # Determine C from mass conservation.
    # M = int_{-R}^{R} u dx  where R = sqrt(C/k) * t^{alpha_R}
    # Using the substitution xi = x / t^{alpha_R}:
    #   M = t^{alpha_rho + alpha_R} * int_{-R0}^{R0} [C - k*xi^2]^{1/(m-1)} dxi
    # The time prefactor t^{alpha_rho + alpha_R} = t^0 = 1 (mass is conserved).
    # The spatial integral evaluates to:
    #   I = 2 * (C/k)^{1/2} * C^{1/(m-1)} * B(1/2, 1/(m-1) + 1)  (Beta function)
    # where B is the Euler beta function.
    from scipy.special import beta as euler_beta
    p = 1.0 / (m - 1)
    # int_{-R0}^{R0} [C - k*xi^2]_+^p dxi
    #   let xi = sqrt(C/k) * sin(theta)  =>
    #   = 2*sqrt(C/k) * C^p * int_0^{pi/2} cos^{2p+1}(theta) dtheta
    #   = 2*sqrt(C/k) * C^p * (1/2) * B(1, p + 1/2)
    #   = sqrt(C/k) * C^p * B(1, p + 1/2)
    #
    # Simpler: use the known formula
    #   I = 2*sqrt(C/k) * C^p * B(1/2, p+1) / 1
    # where B(a,b) = Gamma(a)*Gamma(b)/Gamma(a+b)
    B_val = euler_beta(0.5, p + 1)
    # M = 2 * sqrt(C/k) * C^p * (1/2) * B_val  ... let me just use the
    # standard textbook formula directly.
    #
    # From Vazquez (2007), the Barenblatt solution in d=1 with mass M is:
    #   u(x,t) = t^{-alpha} * [ C - k * eta^2 ]_+^{1/(m-1)}
    #   alpha = 1/(m+1)  [for d=1: alpha = alpha_R]
    #   eta = x / t^alpha
    #   k = alpha*(m-1) / (2*m)
    #   C = [ M * k^{1/2} * Gamma(1/(m-1) + 3/2) /
    #          (Gamma(1/(m-1) + 1) * Gamma(1/2)) ]^{2(m-1)/(m+1)}
    #
    # Let me just solve for C numerically from the mass integral.

    # For a given C, compute the mass:
    def mass_from_C(C_try):
        R0 = np.sqrt(C_try / k)
        xi = np.linspace(-R0, R0, 10000)
        inner = np.maximum(C_try - k * xi ** 2, 0.0)
        u_xi = inner ** p
        return np.trapezoid(u_xi, xi)

    # Bracket C
    from scipy.optimize import brentq
    C_sol = brentq(lambda c: mass_from_C(c) - M, 1e-10, 100.0)

    R0 = np.sqrt(C_sol / k)          # support radius in similarity variable
    R_t = R0 * t ** alpha_R           # support radius at time t

    eta = x / t ** alpha_R
    inner = C_sol - k * eta ** 2
    u = t ** alpha_rho * np.maximum(inner, 0.0) ** p

    return u, R_t, alpha_R, alpha_rho, C_sol, k


def main():
    beta = 1.69
    m = beta + 1  # 2.69
    M = 1.0       # unit mass

    times = [0.1, 1.0, 10.0]
    colors = ["#DC2626", "#2563EB", "#059669"]
    labels = [f"$t = {t}$" for t in times]

    # Compute profiles
    x_full = np.linspace(-6, 6, 4000)
    profiles = []
    fronts = []
    for t_val in times:
        u, R_t, alpha_R, alpha_rho, C, k = barenblatt_1d(x_full, t_val, m, M)
        profiles.append(u)
        fronts.append(R_t)

    # ── Figure ─────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(9, 5))

    for i, (t_val, u, R_t, col, lab) in enumerate(
        zip(times, profiles, fronts, colors, labels)
    ):
        # Plot the profile
        ax.plot(x_full, u, "-", color=col, linewidth=2.2, label=lab, zorder=3)

        # Fill underneath
        ax.fill_between(x_full, u, 0, color=col, alpha=0.08, zorder=1)

        # Mark front positions with thin vertical ticks
        for sign in [1, -1]:
            ax.plot([sign * R_t, sign * R_t], [0, 0.015 * max(profiles[0])],
                    "-", color=col, linewidth=1.2, zorder=4)
            # Small triangle marker at base
            ax.plot(sign * R_t, 0, "v", color=col, markersize=5, zorder=5,
                    clip_on=False)

    # Annotate front positions
    for i, (t_val, R_t, col) in enumerate(zip(times, fronts, colors)):
        y_annot = -0.035 * max(profiles[0])
        ax.text(R_t, y_annot, f"$R = {R_t:.2f}$",
                fontsize=7.5, color=col, ha="center", va="top",
                fontweight="bold")

    # Exponent annotation box
    ax.text(0.97, 0.97,
            f"$\\beta = {beta}$\n"
            f"$m = \\beta + 1 = {m:.2f}$\n"
            f"$\\alpha_R = 1/(\\beta+2) = {alpha_R:.4f}$\n"
            f"$\\alpha_\\rho = {alpha_rho:.4f}$\n\n"
            f"$R(t) \\propto t^{{{alpha_R:.3f}}}$\n"
            f"$u_{{\\max}}(t) \\propto t^{{{alpha_rho:.3f}}}$",
            transform=ax.transAxes, fontsize=9.5,
            verticalalignment="top", horizontalalignment="right",
            fontfamily="monospace",
            bbox=dict(boxstyle="round,pad=0.5", facecolor="white",
                      edgecolor="#D1D5DB", alpha=0.95))

    # Compact support annotation
    ax.annotate(
        "Compact support:\n$u = 0$ outside $|x| < R(t)$",
        xy=(fronts[1] + 0.15, 0.003 * max(profiles[0])),
        xytext=(fronts[1] + 1.2, 0.25 * max(profiles[0])),
        fontsize=8.5, color="#6B7280", fontstyle="italic",
        arrowprops=dict(arrowstyle="->", color="#9CA3AF", linewidth=1.2),
        va="center",
    )

    # Labels and style
    ax.set_xlabel("Position  $x$", fontsize=12)
    ax.set_ylabel("Density  $u(x, t)$", fontsize=12)
    ax.set_title(
        "Barenblatt-Pattle similarity solution of the porous-medium equation",
        fontsize=13, fontweight="bold", pad=12,
    )

    ax.set_xlim(-5.5, 5.5)
    y_max = 1.08 * max(profiles[0])
    ax.set_ylim(-0.06 * y_max, y_max)
    ax.axhline(0, color="black", linewidth=0.6, zorder=0)

    ax.legend(fontsize=10, loc="upper left", framealpha=0.95,
              edgecolor="#D1D5DB")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=10)

    # ── Save ───────────────────────────────────────────────────────
    script_dir = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.join(script_dir, "..", "outputs", "figures")
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "pme_similarity_solution.png")
    fig.savefig(outpath, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close()

    print(f"Saved: {outpath}")
    print(f"Size:  {os.path.getsize(outpath) / 1024:.0f} KB")
    print(f"\nbeta = {beta},  m = {m:.2f}")
    print(f"alpha_R   = {alpha_R:.6f}")
    print(f"alpha_rho = {alpha_rho:.6f}")
    for t_val, R_t in zip(times, fronts):
        print(f"  t = {t_val:5.1f}  =>  R = {R_t:.4f}")


if __name__ == "__main__":
    main()
