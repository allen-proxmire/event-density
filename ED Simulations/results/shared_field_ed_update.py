import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

try:
    from scipy.ndimage import gaussian_filter
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

GR, GC   = 80, 100
R_CORE   = 7.0
AMP      = 0.88
BG       = 0.08
SHIFT    = 5

ROW_A, COL_A0 = 36, 26
ROW_B, COL_B0 = 50, 74

ri, ci = np.ogrid[0:GR, 0:GC]
EXT    = [0, GC, GR, 0]
CMAP   = "gray_r"
VM, VX = 0.05, 1.0
LVL    = [0.25, 0.50, 0.75]

def g(r0, c0, amp=AMP, R=R_CORE):
    return amp * np.exp(-((ri-r0)**2 + (ci-c0)**2) / (2*R**2))

pA_sep  = np.clip(BG*0.5 + g(ROW_A, COL_A0), 0, 1)
pB_sep  = np.clip(BG*0.5 + g(ROW_B, COL_B0), 0, 1)
p1      = np.clip(BG + g(ROW_A, COL_A0) + g(ROW_B, COL_B0), 0, 1)
p2      = p1.copy()

p3 = np.clip(BG*1.05 + g(ROW_A, COL_A0, amp=AMP*0.91)
                      + g(ROW_B, COL_B0, amp=AMP*0.91), 0, 1)
if HAS_SCIPY:
    p3 = np.clip(gaussian_filter(p3, sigma=0.55), 0, 1)

CA_adv = COL_A0 + SHIFT
CB_adv = COL_B0 - SHIFT
p4 = np.clip(BG*1.05 + g(ROW_A, CA_adv, amp=AMP*0.91)
                      + g(ROW_B, CB_adv, amp=AMP*0.91), 0, 1)

pA5 = np.clip(BG*0.5 + g(ROW_A, CA_adv, amp=AMP*0.91), 0, 1)
pB5 = np.clip(BG*0.5 + g(ROW_B, CB_adv, amp=AMP*0.91), 0, 1)

W = [10, 2, 10, 2, 10, 2, 10, 2, 10]
fig = plt.figure(figsize=(19.5, 4.8))
gs  = gridspec.GridSpec(1, 9, figure=fig, width_ratios=W,
                        wspace=0.0, left=0.02, right=0.965,
                        top=0.80, bottom=0.10)

P_IDX = [0, 2, 4, 6, 8]
A_IDX = [1, 3, 5, 7]

axP = [fig.add_subplot(gs[0, i]) for i in P_IDX]
axA = [fig.add_subplot(gs[0, i]) for i in A_IDX]

TITLES = [
    r"$p_A$  and  $p_B$" + "\n" + r"(two separate fields)",
    r"$p_{\mathrm{total}} = p_A + p_B$" + "\n" + r"(combined)",
    r"After ED Update" + "\n" + r"$\mathcal{F}[p_{\mathrm{total}}]$",
    r"After Advection" + "\n" + r"$p \leftarrow \mathrm{shift}(p,\,v)$",
    r"Recovered  $p_A'$,  $p_B'$" + "\n" + r"(soft $\sigma$-partition)",
]
FIELDS = [p1, p2, p3, p4, p4]

last_im = None
for idx, (ax, fld, ttl) in enumerate(zip(axP, FIELDS, TITLES)):
    im = ax.imshow(fld, cmap=CMAP, vmin=VM, vmax=VX,
                   origin="upper", extent=EXT, aspect="equal")
    last_im = im
    if idx not in (0, 4):
        ax.contour(np.arange(GC), np.arange(GR), fld,
                   levels=LVL, colors="black", linewidths=0.9, alpha=0.70)
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_linewidth(1.2); sp.set_color("black")
    ax.set_title(ttl, fontsize=9.5, fontweight="bold", pad=6, linespacing=1.4)
ax1 = axP[0]
ax1.contour(np.arange(GC), np.arange(GR), pA_sep,
            levels=[0.25,0.50,0.75], colors="black", linewidths=0.9,
            linestyles="solid", alpha=0.75)
ax1.contour(np.arange(GC), np.arange(GR), pB_sep,
            levels=[0.25,0.50,0.75], colors="black", linewidths=0.9,
            linestyles="dashed", alpha=0.75)
ax1.axvline(x=50, color="dimgray", linestyle=":", linewidth=1.2, alpha=0.85)
ax1.text(26, 8,  r"$p_A$", ha="center", va="top", fontsize=13,
         fontweight="bold", color="black")
ax1.text(74, 8,  r"$p_B$", ha="center", va="top", fontsize=13,
         fontweight="bold", color="black", style="italic")
ax1.plot(COL_A0, ROW_A, "o", color="white", ms=5.5, mec="black", mew=1.3, zorder=6)
ax1.plot(COL_B0, ROW_B, "o", color="white", ms=5.5, mec="black", mew=1.3, zorder=6)

ax2 = axP[1]
ax2.plot(COL_A0, ROW_A, "o", color="white", ms=5.5, mec="black", mew=1.3, zorder=6)
ax2.plot(COL_B0, ROW_B, "o", color="white", ms=5.5, mec="black", mew=1.3, zorder=6)

ax3 = axP[2]
ax3.plot(COL_A0, ROW_A, "o", color="white", ms=5.5, mec="black", mew=1.3, zorder=6)
ax3.plot(COL_B0, ROW_B, "o", color="white", ms=5.5, mec="black", mew=1.3, zorder=6)
ax3.text(50, GR-4, "drain + diffuse", ha="center", va="bottom",
         fontsize=7.5, color="dimgray", style="italic")

ax4 = axP[3]
ax4.plot(CA_adv, ROW_A, "o", color="white", ms=5.5, mec="black", mew=1.3, zorder=6)
ax4.plot(CB_adv, ROW_B, "o", color="white", ms=5.5, mec="black", mew=1.3, zorder=6)
kw = dict(arrowstyle="->", color="black", lw=1.6, mutation_scale=12)
ax4.annotate("", xy=(CA_adv+10, ROW_A), xytext=(CA_adv, ROW_A),
             arrowprops=kw)
ax4.text(CA_adv+11, ROW_A, r"$+v_0$", va="center", ha="left", fontsize=8,
         color="black")
ax4.annotate("", xy=(CB_adv-10, ROW_B), xytext=(CB_adv, ROW_B),
             arrowprops=kw)
ax4.text(CB_adv-11, ROW_B, r"$-v_0$", va="center", ha="right", fontsize=8,
         color="black")

ax5 = axP[4]
ax5.contour(np.arange(GC), np.arange(GR), pA5,
            levels=LVL, colors="black", linewidths=1.0,
            linestyles="solid", alpha=0.85)
ax5.contour(np.arange(GC), np.arange(GR), pB5,
            levels=LVL, colors="dimgray", linewidths=1.0,
            linestyles="dashed", alpha=0.85)
ax5.plot(CA_adv, ROW_A, "o", color="white", ms=5.5, mec="black", mew=1.3, zorder=6)
ax5.plot(CB_adv, ROW_B, "o", color="white", ms=5.5, mec="dimgray", mew=1.3, zorder=6)
ax5.text(CA_adv, ROW_A-11, r"$p_A'$", ha="center", va="bottom",
         fontsize=12, fontweight="bold", color="black")
ax5.text(CB_adv, ROW_B-11, r"$p_B'$", ha="center", va="bottom",
         fontsize=12, fontweight="bold", color="dimgray", style="italic")
ax5.text(50, GR-4, r"Gaussian $\sigma$-weights", ha="center", va="bottom",
         fontsize=7.5, color="dimgray", style="italic")

from matplotlib.lines import Line2D
leg_elems = [
    Line2D([0],[0], color="black",   lw=1.0, ls="solid",  label=r"$p_A'$ (solid)"),
    Line2D([0],[0], color="dimgray", lw=1.0, ls="dashed", label=r"$p_B'$ (dashed)"),
]
ax5.legend(handles=leg_elems, fontsize=7.5, loc="lower right",
           framealpha=0.8, edgecolor="gray", handlelength=1.8)

ARROW_LABELS = [
    "combine\n(sum)",
    r"ED update" + "\n" + r"$\mathcal{F}[\cdot]$",
    r"advect" + "\n" + r"$\leftarrow\!\cdot\!\rightarrow$",
    r"partition" + "\n" + r"$w_A,\,w_B$",
]
for ax_a, lbl in zip(axA, ARROW_LABELS):
    ax_a.set_xlim(0, 1); ax_a.set_ylim(0, 1)
    ax_a.axis("off")
    ax_a.annotate("", xy=(0.88, 0.50), xytext=(0.12, 0.50),
                  arrowprops=dict(arrowstyle="->", color="black",
                                  lw=2.2, mutation_scale=17),
                  xycoords="axes fraction", textcoords="axes fraction")
    ax_a.text(0.50, 0.64, lbl, ha="center", va="bottom", fontsize=8.5,
              fontweight="bold", color="black", transform=ax_a.transAxes,
              linespacing=1.35)

cax  = fig.add_axes([0.968, 0.13, 0.013, 0.65])
cbar = fig.colorbar(last_im, cax=cax)
cbar.set_label(r"$\rho$ (norm.)", fontsize=9)
cbar.ax.tick_params(labelsize=7.5)

fig.suptitle("Shared-Field ED Update", fontsize=15, fontweight="bold", y=0.96)

fig.text(0.485, 0.01,
         r"CoreType-QM1  |  $R_\mathrm{core}=7\,\mathrm{px}$  |  "
         r"$D_0=48\,\mathrm{px}$  |  $b=14\,\mathrm{px}$  |  "
         r"$v=\pm0.1\,\mathrm{px/step}$  |  Gaussian soft partition ($\sigma=1.5\,R$)",
         ha="center", va="bottom", fontsize=8, color="dimgray", style="italic")

out = r"C:\Users\allen\OneDrive\Desktop\shared_field_ed_update.png"
fig.savefig(out, dpi=150, bbox_inches="tight")
print(f"SUCCESS: saved to {out}")
