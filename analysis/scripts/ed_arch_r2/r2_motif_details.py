"""Extract the individual motif-admitted saddles at the best filter setting."""
from __future__ import annotations
import os
import numpy as np
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from r2_motif_filter import (
    smooth, find_morse_saddles, motif_admit, p, p_hat, p_std, E
)

saddles = find_morse_saddles(E)

print("=" * 80)
print("  Motif-admitted saddles at multiple filter settings")
print("=" * 80)
print(f"  p_hat = {p_hat:.5f}   std = {p_std:.5f}")
print(f"  baseline (all Morse saddles): N={len(saddles)}")
print("")

for (alpha, L_ray, mono, label) in [
    (0.25, 2, False, "loose (best N with median-match)"),
    (0.25, 2, True,  "stricter (monotone)"),
    (0.25, 3, False, "L_ray=3"),
    (0.25, 4, False, "L_ray=4"),
    (0.50, 2, False, "alpha=0.5"),
]:
    admitted = [s for s in saddles if motif_admit(s, E, alpha, L_ray, mono)]
    ratios = sorted([s["ratio"] for s in admitted])  # ascending (most negative first)
    print(f"  --- alpha={alpha}, L_ray={L_ray}, mono={mono} [{label}] ---")
    print(f"  N_motif = {len(admitted)}")
    if len(admitted) == 0:
        print("  (empty)")
        print("")
        continue
    print(f"  ratios (sorted, most-negative first):")
    for r in ratios:
        marker = "  <-- IN [-1.5, -1.1]" if -1.5 <= r <= -1.1 else ""
        print(f"    {r:+.4f}{marker}")
    if len(ratios) >= 1:
        arr = np.array(ratios)
        print(f"  mean  = {arr.mean():+.4f}")
        print(f"  std   = {arr.std():.4f}")
        if len(ratios) >= 2:
            print(f"  median = {np.median(arr):+.4f}")
            p25, p75 = np.percentile(arr, [25, 75])
            print(f"  IQR   = [{p25:+.4f}, {p75:+.4f}]  width={p75-p25:.4f}")
        in_arch = ((arr >= -1.5) & (arr <= -1.1)).mean()
        print(f"  fraction in [-1.5, -1.1]: {in_arch*100:.1f}%")

    # Location of saddles
    print(f"  locations (i, j) and field value:")
    for s in admitted:
        print(f"    ({s['i']:2d}, {s['j']:2d})  E={s['E_at']:.5f}  ratio={s['ratio']:+.4f}  "
              f"lam_neg={s['lambda_neg']:+.2e}  lam_pos={s['lambda_pos']:+.2e}")
    print("")

# Text histogram of the baseline vs loose-motif distribution
print("=" * 80)
print("  Text histogram: ALL Morse saddles vs motif-conditioned (loose)")
print("=" * 80)
all_r = np.array([s["ratio"] for s in saddles])
admitted_loose = [s for s in saddles if motif_admit(s, E, 0.25, 2, False)]
motif_r = np.array([s["ratio"] for s in admitted_loose])

bins = np.arange(-6.0, -0.99, 0.25)
bins = np.concatenate([bins, [-0.99]])  # catch the near-(-1) edge cleanly
labels = [f"[{bins[k]:+.2f}, {bins[k+1]:+.2f})" for k in range(len(bins) - 1)]
hist_all, _   = np.histogram(all_r,   bins=bins)
hist_motif, _ = np.histogram(motif_r, bins=bins)

print(f"  {'bin':>18}  {'ALL':>10}  {'MOTIF':>10}")
for lab, a, m in zip(labels, hist_all, hist_motif):
    # mark ED-Arch window
    lo, hi = map(float, lab.strip("[)").split(", "))
    mark = " <-- ED-Arch window" if (-1.5 <= lo and hi <= -1.0) else ""
    bar_all   = "#" * min(a, 40)
    bar_motif = "*" * min(m * 5, 40)
    print(f"  {lab:>18}  {a:>10}  {m:>10}  {bar_all:<40}  {bar_motif:<10}{mark}")

print("")
print("  (ALL bars scaled 1:1, MOTIF bars scaled 5:1 for visibility)")
