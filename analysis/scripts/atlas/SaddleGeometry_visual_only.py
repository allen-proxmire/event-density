"""
Saddle Geometry — visual-only illustration.

A Pringle-chip schematic of the canonical ED saddle:
  - one axis compresses (negative-curvature, navy / violet descent)
  - one axis expands (positive-curvature, amber / coral ascent)
  - det(H) < 0 at the saddle point
  - eigenvalue ratio  r = lambda_parallel / lambda_perp ~= -1.30
    (the ED-SC 2.0 reference value)

Composition:
  MAIN      : 3D saddle surface z = x^2 - y^2 shaded by height (cyan
              down, amber up); two principal-axis curves traced ON
              the surface -- amber ridge along the expansion axis,
              cyan valley along the compression axis.
  CENTER    : golden saddle-point marker with small halo.
  CORNERS   : tiny structural tags for kappa_perp > 0, kappa_parallel < 0,
              det(H) < 0, and the ED-SC 2.0 ratio r* ~= -1.304.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from mpl_toolkits.mplot3d.art3d import Line3DCollection

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\SaddleGeometry.png"


def build():
    fig = plt.figure(figsize=(13, 9), dpi=220)
    fig.patch.set_facecolor("#f7fbfe")

    # ---- backdrop (2D axes under the 3D) -------------------------------
    bg = fig.add_axes([0, 0, 1, 1], zorder=0)
    bg.set_xlim(0, 14)
    bg.set_ylim(0, 10)
    bg.axis("off")
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    bg.imshow(grad, extent=[0, 14, 0, 10], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    bg.add_patch(Rectangle((0, 0), 14, 1.5,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # ---- main 3D axes --------------------------------------------------
    ax = fig.add_axes([0.05, 0.05, 0.90, 0.92], projection="3d", zorder=2)
    ax.set_facecolor((1, 1, 1, 0))  # transparent

    # Saddle surface  z = x^2 - y^2
    n = 90
    X, Y = np.meshgrid(np.linspace(-1.5, 1.5, n),
                       np.linspace(-1.5, 1.5, n))
    Z = X ** 2 - Y ** 2

    # Custom two-tone cmap: cyan (low) -> pale -> amber (high)
    from matplotlib.colors import LinearSegmentedColormap
    sad_cmap = LinearSegmentedColormap.from_list(
        "saddle",
        [
            (0.00, "#0f5e85"),   # deep cyan
            (0.25, "#57c6e6"),
            (0.48, "#e8f1f5"),   # pale hinge
            (0.52, "#fff1d8"),
            (0.75, "#ffc470"),
            (1.00, "#c97a10"),   # deep amber
        ],
    )

    ax.plot_surface(
        X, Y, Z, cmap=sad_cmap,
        rstride=2, cstride=2,
        linewidth=0, antialiased=True,
        edgecolor="none", alpha=0.96, zorder=3,
    )

    # Wireframe overlay for Pringle-chip feel (faint)
    ax.plot_wireframe(X, Y, Z, rstride=8, cstride=8,
                      color="#1f3b57", linewidth=0.5,
                      alpha=0.30, zorder=4)

    # ---- principal-axis curves traced ON the surface -------------------
    t = np.linspace(-1.45, 1.45, 120)

    # Expansion axis (along x, y = 0):  z = x^2  -- positive curvature
    x_exp, y_exp, z_exp = t, np.zeros_like(t), t ** 2
    # glow underlay
    for lw, a in [(8, 0.10), (5, 0.22)]:
        ax.plot(x_exp, y_exp, z_exp + 0.005,
                color="#ffd98a", lw=lw, alpha=a, zorder=6,
                solid_capstyle="round")
    ax.plot(x_exp, y_exp, z_exp + 0.005,
            color="#c97a10", lw=3.2, zorder=7,
            solid_capstyle="round")

    # Compression axis (along y, x = 0):  z = -y^2 -- negative curvature
    x_comp, y_comp, z_comp = np.zeros_like(t), t, -t ** 2
    for lw, a in [(8, 0.10), (5, 0.22)]:
        ax.plot(x_comp, y_comp, z_comp - 0.005,
                color="#9fe6f3", lw=lw, alpha=a, zorder=6,
                solid_capstyle="round")
    ax.plot(x_comp, y_comp, z_comp - 0.005,
            color="#0f5e85", lw=3.2, zorder=7,
            solid_capstyle="round")

    # Arrow caps at each end of each principal axis (simulated with
    # short Line3DCollection segments + small terminal markers)
    def end_marker(x, y, z, col, edge):
        ax.scatter([x], [y], [z], s=90,
                   facecolor=col, edgecolor=edge,
                   linewidth=1.4, zorder=10)

    end_marker(x_exp[-1], y_exp[-1], z_exp[-1], "#ff9f1a", "#7a4a0a")
    end_marker(x_exp[0],  y_exp[0],  z_exp[0],  "#ff9f1a", "#7a4a0a")
    end_marker(x_comp[-1], y_comp[-1], z_comp[-1], "#57c6e6", "#0b4a68")
    end_marker(x_comp[0],  y_comp[0],  z_comp[0],  "#57c6e6", "#0b4a68")

    # ---- saddle point (center) -----------------------------------------
    # halo layers
    for r_, a in [(0.22, 0.14), (0.14, 0.28)]:
        th = np.linspace(0, 2 * np.pi, 40)
        xh = r_ * np.cos(th)
        yh = r_ * np.sin(th)
        zh = np.zeros_like(th) + 0.01
        ax.plot(xh, yh, zh, color="#ffd24a", alpha=a, lw=2, zorder=9)
    ax.scatter([0], [0], [0.01], s=220,
               facecolor="#ffd24a", edgecolor="#7a4a0a",
               linewidth=1.8, zorder=11)

    # Small five-point star inside the saddle marker (approximate by
    # scattering another small gold dot on top)
    ax.scatter([0], [0], [0.02], s=60,
               facecolor="#fff1b0", edgecolor="#c97a10",
               linewidth=0.9, zorder=12)

    # ---- view + framing -----------------------------------------------
    ax.view_init(elev=26, azim=-58)
    ax.set_box_aspect([1, 1, 0.55])
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_zlim(-2.2, 2.2)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
    ax.set_xlabel(""); ax.set_ylabel(""); ax.set_zlabel("")
    # hide panes + axes lines
    for pane in (ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane):
        pane.set_visible(False)
    ax.grid(False)

    # ---- structural-label tags on the 2D backdrop ----------------------
    def pill(bg_ax, cx, cy, w, h, text, face, edge, txtcol):
        bg_ax.add_patch(FancyBboxPatch(
            (cx - w / 2, cy - h / 2), w, h,
            boxstyle="round,pad=0.02,rounding_size=0.10",
            facecolor=face, edgecolor=edge, lw=1.4, zorder=5,
        ))
        bg_ax.text(cx, cy, text, ha="center", va="center",
                   fontsize=10.5, color=txtcol,
                   fontweight="bold")

    # expansion-axis tag (upper right)
    pill(bg, 11.6, 8.4, 3.6, 0.6,
         r"$\kappa_\perp > 0$   expansion",
         "#fff1d8", "#c97a10", "#7a4a0a")
    # compression-axis tag (lower left)
    pill(bg, 2.5, 1.9, 3.6, 0.6,
         r"$\kappa_\parallel < 0$   compression",
         "#e6f4fa", "#0b4a68", "#0f5e85")

    # det(H) < 0 tag (upper left)
    pill(bg, 2.35, 8.4, 3.1, 0.6,
         r"det$(H) < 0$     saddle",
         "#f5e1e6", "#6b2e45", "#6b2e45")

    # ED-SC 2.0 r* tag (lower right)
    pill(bg, 11.4, 1.9, 3.8, 0.6,
         r"$r^{*} = \lambda_\parallel / \lambda_\perp \approx -1.304$",
         "#ece3f4", "#6d5aa1", "#4a3f80")

    # Center title-y tag (top center)
    bg.text(7.0, 9.3, "Saddle Geometry",
            ha="center", va="center",
            fontsize=16, fontweight="bold", color="#1f3b57")
    bg.text(7.0, 8.85,
            "one axis compresses  |  one axis expands  |  det$(H) < 0$",
            ha="center", va="center",
            fontsize=10.5, style="italic", color="#4a5568")

    # small legend swatches under the title
    bg.add_patch(Circle((5.2, 0.65), 0.14, facecolor="#c97a10",
                        edgecolor="#7a4a0a", lw=1.2, zorder=6))
    bg.text(5.45, 0.65, "expansion axis",
            ha="left", va="center", fontsize=9.5, color="#7a4a0a")
    bg.add_patch(Circle((8.0, 0.65), 0.14, facecolor="#0f5e85",
                        edgecolor="#0b4a68", lw=1.2, zorder=6))
    bg.text(8.25, 0.65, "compression axis",
            ha="left", va="center", fontsize=9.5, color="#0f5e85")
    bg.add_patch(Circle((10.9, 0.65), 0.14, facecolor="#ffd24a",
                        edgecolor="#7a4a0a", lw=1.2, zorder=6))
    bg.text(11.15, 0.65, "saddle point",
            ha="left", va="center", fontsize=9.5, color="#7a4a0a")

    # ---- save ----------------------------------------------------------
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    plt.savefig(OUT, dpi=220, bbox_inches="tight",
                facecolor="#f7fbfe", edgecolor="none")
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    build()
