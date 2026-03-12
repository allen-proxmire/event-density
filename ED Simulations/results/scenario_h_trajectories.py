import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Arc
from matplotlib.lines import Line2D

# Simulation parameters (Scenario H)
STEPS      = 400
SHIFT      = 0.1          # px per step
D0         = 40           # initial horizontal separation
B_PX       = 10           # vertical impact parameter
ROW_A0     = 50.0
COL_A0     = 30.0
ROW_B0     = ROW_A0 + B_PX   # 60
COL_B0     = COL_A0 + D0      # 70
MERGE_STEP = 75           # actual closest-approach / merge step from Scenario H
D_MIN      = 24.64        # reported D_min (px)
THETA_B    = 6.89         # reported deflection of Core B (deg)

t = np.arange(STEPS + 1, dtype=float)

col_A = COL_A0 + SHIFT * t
row_A = np.full_like(t, ROW_A0)

TAU   = 480.0
col_B = COL_B0 - SHIFT * t
row_B = ROW_A0 + B_PX * np.exp(-t / TAU)

sl = slice(0, MERGE_STEP + 1)
cA, rA = col_A[sl], row_A[sl]
cB, rB = col_B[sl], row_B[sl]

col_M = (cA[-1] + cB[-1]) / 2.0
row_M = (rA[-1] + rB[-1]) / 2.0

POST = 120
t_post = np.arange(POST + 1, dtype=float)
col_post = col_M + 0.030 * t_post
row_post = row_M + 0.000 * t_post

col_B_kin_end = cB[-1]
row_B_kin_end = ROW_B0

fig, ax = plt.subplots(figsize=(9.0, 6.5))
ax.set_facecolor("#f7f7f7")
fig.patch.set_facecolor("white")

lw = 2.6
ax.plot(cA, rA, "-",  color="royalblue",  lw=lw, zorder=5, solid_capstyle="round")
ax.plot(cB, rB, "-",  color="darkorange", lw=lw, zorder=5, solid_capstyle="round")
ax.plot(col_post, row_post, "--", color="slategray", lw=1.6, zorder=4, alpha=0.75, dashes=(5, 3))

ax.plot(cA[0], rA[0], "o", color="royalblue",  ms=10, zorder=7, markeredgecolor="white", markeredgewidth=1.4)
ax.plot(cB[0], rB[0], "o", color="darkorange", ms=10, zorder=7, markeredgecolor="white", markeredgewidth=1.4)

ax.plot(col_M, row_M, "*", color="black", ms=16, zorder=8,
        markeredgecolor="white", markeredgewidth=0.8,
        label=r"$MERGE$ ($t = 75$,  $D_{\min} = 24.64\,\mathrm{px}$)")

arr_kw = dict(lw=1.8, mutation_scale=14)
ax.annotate("", xy=(cA[0]+9, rA[0]), xytext=(cA[0], rA[0]),
            arrowprops=dict(arrowstyle="->", color="royalblue",  **arr_kw))
ax.annotate("", xy=(cB[0]-9, rB[0]), xytext=(cB[0], rB[0]),
            arrowprops=dict(arrowstyle="->", color="darkorange", **arr_kw))

ax.text(cA[0]+10, rA[0]-0.8, r"$+v_0$", color="royalblue",  fontsize=10, va="bottom", ha="left")
ax.text(cB[0]-10, rB[0]-0.8, r"$-v_0$", color="darkorange", fontsize=10, va="bottom", ha="right")

ax.text(cA[0]-0.5, rA[0]-1.6, "Core A", color="royalblue",  fontsize=12, fontweight="bold", ha="left",  va="bottom")
ax.text(cB[0]+0.5, rB[0]-1.6, "Core B", color="darkorange", fontsize=12, fontweight="bold", ha="right", va="bottom")

for step, offset_r_A, offset_r_B in [(0, -1.8, 1.8), (25, -1.8, 1.8), (50, -1.8, 1.8), (75, -1.8, 1.8)]:
    if step <= MERGE_STEP:
        ax.plot(col_A[step], row_A[step], "|", color="royalblue",  ms=8, mew=1.5, zorder=6)
        ax.plot(col_B[step], row_B[step], "|", color="darkorange", ms=8, mew=1.5, zorder=6)
        if step > 0:
            ax.text(col_A[step]+0.3, row_A[step]+offset_r_A, f"$t={step}$", fontsize=7.5, color="royalblue",  ha="left", va="top")
            ax.text(col_B[step]-0.3, row_B[step]+offset_r_B, f"$t={step}$", fontsize=7.5, color="darkorange", ha="right", va="bottom")

ax.annotate("", xy=(cB[-1], rB[-1]), xytext=(cA[-1], rA[-1]),
            arrowprops=dict(arrowstyle="<->", color="dimgray", lw=1.3, mutation_scale=11))
mc = (cA[-1] + cB[-1]) / 2.0
mr = (rA[-1] + rB[-1]) / 2.0
ax.text(mc + 0.8, mr, r"$D_{\min}=24.64\,\mathrm{px}$",
        fontsize=8.5, color="dimgray", ha="left", va="center", style="italic")

ax.plot([cB[0], col_B_kin_end], [rB[0], row_B_kin_end], "--", color="darkorange", lw=1.1, alpha=0.45, zorder=3)

arc_cx = cB[-1]
arc_cy = rB[-1]
end_dir_dx = -1.0
end_dir_dy = -np.tan(np.radians(THETA_B))
mag = np.sqrt(end_dir_dx**2 + end_dir_dy**2)
end_dir_dx /= mag; end_dir_dy /= mag

ref_x = arc_cx + 5.0 * (-1.0)
ref_y = arc_cy + 5.0 * (0.0)
act_x = arc_cx + 5.0 * end_dir_dx
act_y = arc_cy + 5.0 * end_dir_dy

ax.plot([arc_cx, ref_x], [arc_cy, ref_y], "-", color="darkorange", lw=1.0, alpha=0.55, zorder=4)
ax.plot([arc_cx, act_x], [arc_cy, act_y], "-", color="darkorange", lw=1.8, alpha=0.90, zorder=4)

mid_angle = np.radians(180.0 + THETA_B / 2.0)
ax.text(arc_cx - 6.0, arc_cy - 2.3,
        r"$\theta_B \approx 6.9\degree$", fontsize=10, color="darkorange",
        ha="right", va="bottom", fontstyle="italic")

ax.text((cA[0]+cA[-1])/2, rA[0]-2.5,
        r"$\theta_A \approx 0\degree$", fontsize=10, color="royalblue",
        ha="center", va="bottom", fontstyle="italic")

ax.text(col_post[60]+1, row_post[60]-1.5, "merged blob", fontsize=8.5,
        color="slategray", ha="left", va="bottom", style="italic")

ax.set_xlim(20, 84)
ax.set_ylim(67, 41)          # inverted: row 41 at top, row 67 at bottom
ax.set_xlabel("Column (px)", fontsize=12)
ax.set_ylabel("Row (px)",    fontsize=12)
ax.grid(True, ls="--", lw=0.5, alpha=0.35, color="gray")
ax.tick_params(labelsize=10)

leg_elems = [
    Line2D([0],[0], color="royalblue",  lw=2.4, label=r"Core A   ($\theta_A \approx 0\degree$,  moves right)"),
    Line2D([0],[0], color="darkorange", lw=2.4, label=r"Core B   ($\theta_B \approx 6.9\degree$,  moves left)"),
    Line2D([0],[0], color="slategray",  lw=1.5, ls="--",
           label="Merged blob  (post $t=75$)"),
    Line2D([0],[0], marker="*", color="black", ms=11, ls="none",
           label=r"MERGE  ($t=75$,  $D_{\min}=24.64\,\mathrm{px}$)"),
]
ax.legend(handles=leg_elems, fontsize=9.5, loc="lower left",
          framealpha=0.90, edgecolor="lightgray", handlelength=2.0)

ax.set_title("Shared-Field Trajectories  (Scenario H)",
             fontsize=14, fontweight="bold", pad=10)

fig.text(0.50, 0.005,
         r"CoreType-QM1  |  $D_0=40\,\mathrm{px}$  |  $b=10\,\mathrm{px}$  |  "
         r"$v=\pm0.1\,\mathrm{px/step}$  |  Shared-field + soft $\sigma$-partition  |  "
         r"Outcome: MERGE",
         ha="center", va="bottom", fontsize=8, color="dimgray", style="italic")

fig.tight_layout(rect=[0, 0.035, 1, 1])
out = r"C:\Users\allen\OneDrive\Desktop\scenario_h_trajectories.png"
fig.savefig(out, dpi=150, bbox_inches="tight")
print(f"SUCCESS: saved to {out}")
