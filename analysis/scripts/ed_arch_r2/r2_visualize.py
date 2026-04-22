"""Quick visualization of the Scenario D final field and ratio histogram."""
from __future__ import annotations

import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False

if not HAS_MPL:
    print("matplotlib not installed; skipping visualization")
    import sys; sys.exit(0)

p = np.load(os.path.join(HERE, "r2_p_final.npy"))
r = np.load(os.path.join(HERE, "r2_field_hessian_ratios.npy"))

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Field (center 128x128 crop for visibility)
c = 128
cx, cy = p.shape[0] // 2, p.shape[1] // 2
crop = p[cx - c:cx + c, cy - c:cy + c]
im = axes[0].imshow(crop, cmap="RdBu", vmin=-1, vmax=1, origin="lower")
axes[0].set_title(f"Scenario D final p(x, y), center {2*c}x{2*c} crop\n"
                  f"(n=2.7, sigma=0.0556, T=457)")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
plt.colorbar(im, ax=axes[0], fraction=0.046)

# Ratio histogram
r_clip = r[(r > -10) & (r < 10)]
axes[1].hist(r_clip, bins=80, color="steelblue", edgecolor="black", alpha=0.8)
axes[1].axvspan(-1.5, -1.1, alpha=0.3, color="green", label="ED-Arch-01 window [-1.5, -1.1]")
axes[1].axvline(-1.3, color="darkgreen", linestyle="--", label="ED-Arch-01 value -1.3")
axes[1].axvline(-1.0, color="red", linestyle="--", label="R2 isotropy prediction -1")
axes[1].axvline(float(np.median(r)), color="purple", linestyle=":", label=f"observed median = {float(np.median(r)):.2f}")
axes[1].set_xlabel("kappa_par / kappa_perp")
axes[1].set_ylabel("Morse saddle count")
axes[1].set_title(f"Field-space Hessian ratio distribution\n"
                  f"N_saddles = {len(r)} (clipped to [-10, 10] for display)")
axes[1].set_xlim(-10, 0)
axes[1].legend(loc="upper left")

# Log-scale wider view
axes[2].hist(r, bins=100, color="steelblue", edgecolor="black", alpha=0.8, log=True)
axes[2].axvspan(-1.5, -1.1, alpha=0.3, color="green")
axes[2].axvline(-1.3, color="darkgreen", linestyle="--")
axes[2].axvline(-1.0, color="red", linestyle="--")
axes[2].set_xlabel("kappa_par / kappa_perp")
axes[2].set_ylabel("count (log)")
axes[2].set_title("Full ratio distribution (log-y)")
axes[2].set_xlim(-50, 0)

plt.tight_layout()
out = os.path.join(HERE, "r2_visualization.png")
plt.savefig(out, dpi=120)
print(f"saved {out}")

# Also save field as separate plot at lower resolution
fig2, ax = plt.subplots(1, 1, figsize=(8, 8))
im = ax.imshow(p, cmap="RdBu", vmin=-1, vmax=1, origin="lower")
ax.set_title(f"Scenario D final field p(x, y) at (n=2.7, sigma=0.0556, T=457)\n"
             f"mean={p.mean():.4f}, std={p.std():.4f}")
plt.colorbar(im, ax=ax, fraction=0.046)
plt.tight_layout()
out2 = os.path.join(HERE, "r2_field_full.png")
plt.savefig(out2, dpi=100)
print(f"saved {out2}")
