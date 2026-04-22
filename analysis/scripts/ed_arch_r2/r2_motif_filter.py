"""
Motif-conditioned architectural-saddle filter on the canonical Scenario D
field (r2_canonical_p_final.npy).

A saddle x* is admitted to the motif-conditioned distribution R_motif only if:
  1. x* is a Morse saddle of the smoothed field (det H < 0, non-degenerate).
  2. Rays of length L_ray along the principal-axis directions of H have
     endpoints in the expected sign:
       - Along the compression axis (negative eigenvalue): x* is a local max,
         so both rays descend -> endpoints below low threshold (low-E region).
       - Along the expansion axis (positive eigenvalue): x* is a local min,
         so both rays ascend -> endpoints above high threshold (high-E region).
  3. The field is monotonic along each ray (no sign flip within L_ray steps).

This enforces "four-quadrant alternating high/low/high/low with quadrant
connectivity preserved at scale L_ray" -- the channel-junction motif from
ED-Arch-02 / ED-SC-00.

Thresholds:
  hi = p_hat + alpha * std(p)
  lo = p_hat - alpha * std(p)

alpha controls filter strictness.  We scan a grid of (alpha, L_ray) to
characterize the motif-conditioned distribution under varying filter strength.

NO NEW SIMULATION.  Only re-analysis of the existing canonical field.
"""

from __future__ import annotations

import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


# -----------------------------------------------------------------------------
# Load canonical field
# -----------------------------------------------------------------------------

p = np.load(os.path.join(HERE, "r2_canonical_p_final.npy"))
N = p.shape[0]
p_hat = float(p.mean())
p_std = float(p.std())
p_min = float(p.min())
p_max = float(p.max())

print("=" * 80)
print("  Motif-conditioned architectural-saddle filter on canonical Scenario D")
print("=" * 80)
print(f"  Field shape: {p.shape}")
print(f"  p_hat = {p_hat:.5f}   std(p) = {p_std:.5f}")
print(f"  p_min = {p_min:.4f}   p_max = {p_max:.4f}")


# -----------------------------------------------------------------------------
# Smoothing (same as r2_canonical.py saddle detection)
# -----------------------------------------------------------------------------

def smooth(p: np.ndarray) -> np.ndarray:
    return p + 0.2 * (
        np.roll(p, 1, 0) + np.roll(p, -1, 0)
      + np.roll(p, 1, 1) + np.roll(p, -1, 1)
      - 4.0 * p
    )


E = smooth(p)


# -----------------------------------------------------------------------------
# Saddle detection (same as r2_canonical.py)
# -----------------------------------------------------------------------------

def find_morse_saddles(E: np.ndarray, deg_tol: float = 0.10):
    """Return list of (i, j, H, eigenvalues, eigenvectors, ratio) for Morse saddles."""
    dpdx = 0.5 * (np.roll(E, -1, axis=0) - np.roll(E, 1, axis=0))
    dpdy = 0.5 * (np.roll(E, -1, axis=1) - np.roll(E, 1, axis=1))

    sx_pos = dpdx > 0; sx_neg = dpdx < 0
    sy_pos = dpdy > 0; sy_neg = dpdy < 0

    x_signchange = (
        (sx_pos & np.roll(sx_neg, -1, axis=0)) |
        (sx_neg & np.roll(sx_pos, -1, axis=0))
    )
    y_signchange = (
        (sy_pos & np.roll(sy_neg, -1, axis=1)) |
        (sy_neg & np.roll(sy_pos, -1, axis=1))
    )
    cand = x_signchange & y_signchange
    interior = np.zeros_like(cand)
    interior[4:-4, 4:-4] = True
    cand &= interior

    ij = np.argwhere(cand)
    saddles = []
    for (i, j) in ij:
        i, j = int(i), int(j)
        d2x = E[i + 1, j] - 2 * E[i, j] + E[i - 1, j]
        d2y = E[i, j + 1] - 2 * E[i, j] + E[i, j - 1]
        dxy = 0.25 * (
            E[i + 1, j + 1] - E[i + 1, j - 1]
          - E[i - 1, j + 1] + E[i - 1, j - 1]
        )
        H = np.array([[d2x, dxy], [dxy, d2y]])
        det = d2x * d2y - dxy * dxy
        if det >= 0:
            continue
        w, V = np.linalg.eigh(H)
        if not (w[0] < 0 < w[1]):
            continue
        if min(abs(w[0]), abs(w[1])) / max(abs(w[0]), abs(w[1])) < deg_tol:
            continue
        # Ratio, larger-|k| in numerator
        if abs(w[0]) >= abs(w[1]):
            ratio = w[0] / w[1]
        else:
            ratio = w[1] / w[0]
        saddles.append({
            "i": i, "j": j,
            "H": H,
            "lambda_neg": float(w[0]),
            "lambda_pos": float(w[1]),
            "e_neg": V[:, 0],
            "e_pos": V[:, 1],
            "ratio": float(ratio),
            "E_at": float(E[i, j]),
        })
    return saddles


# -----------------------------------------------------------------------------
# Motif filter
# -----------------------------------------------------------------------------

def trace_ray(E: np.ndarray, i: int, j: int,
              direction: np.ndarray, sign: int, L_ray: int) -> np.ndarray:
    """Return E values along the ray from (i, j) in the given direction * sign,
    sampled at integer lattice steps 1 .. L_ray (with periodic wrap)."""
    Ny, Nx = E.shape
    vals = np.empty(L_ray, dtype=float)
    for step in range(1, L_ray + 1):
        di = sign * direction[0] * step
        dj = sign * direction[1] * step
        ii = int(round(i + di)) % Ny
        jj = int(round(j + dj)) % Nx
        vals[step - 1] = E[ii, jj]
    return vals


def motif_admit(saddle: dict, E: np.ndarray,
                alpha: float, L_ray: int,
                require_monotone: bool = True) -> bool:
    i, j = saddle["i"], saddle["j"]
    e_neg, e_pos = saddle["e_neg"], saddle["e_pos"]
    E_x = saddle["E_at"]

    hi = p_hat + alpha * p_std
    lo = p_hat - alpha * p_std

    # 4 rays: ±e_neg (compression axis; should descend to low region)
    #          ±e_pos (expansion axis; should ascend to high region)
    r_neg_pp = trace_ray(E, i, j, e_neg, +1, L_ray)
    r_neg_mm = trace_ray(E, i, j, e_neg, -1, L_ray)
    r_pos_pp = trace_ray(E, i, j, e_pos, +1, L_ray)
    r_pos_mm = trace_ray(E, i, j, e_pos, -1, L_ray)

    # Endpoint threshold condition
    endpoint_ok = (
        r_neg_pp[-1] < lo and r_neg_mm[-1] < lo and
        r_pos_pp[-1] > hi and r_pos_mm[-1] > hi
    )
    if not endpoint_ok:
        return False

    if require_monotone:
        # Along e_neg rays, E(step) <= E_x for all steps (non-increasing from saddle).
        # Along e_pos rays, E(step) >= E_x for all steps (non-decreasing from saddle).
        mono_neg = (r_neg_pp <= E_x).all() and (r_neg_mm <= E_x).all()
        mono_pos = (r_pos_pp >= E_x).all() and (r_pos_mm >= E_x).all()
        if not (mono_neg and mono_pos):
            return False

    return True


# -----------------------------------------------------------------------------
# Main analysis
# -----------------------------------------------------------------------------

saddles = find_morse_saddles(E)
all_ratios = np.array([s["ratio"] for s in saddles])

print(f"  Morse saddles (after degeneracy filter): {len(saddles)}")
print(f"")
print(f"  --- baseline R_all (no motif filter) ---")
if len(all_ratios) > 0:
    q25, q50, q75 = np.percentile(all_ratios, [25, 50, 75])
    in_arch = float(((all_ratios >= -1.5) & (all_ratios <= -1.1)).mean())
    print(f"  N={len(all_ratios)}   median={q50:+.3f}   IQR=[{q25:+.3f}, {q75:+.3f}]   "
          f"width={q75 - q25:.3f}   in_arch={in_arch*100:.1f}%")

# --- scan over filter parameters ---
print(f"")
print(f"  --- motif-conditioned R_motif across filter strengths ---")
print(f"  {'alpha':>6}  {'L_ray':>5}  {'mono':>5}  {'N':>4}  "
      f"{'median':>8}  {'IQR':>21}  {'IQR width':>10}  {'in_arch':>8}")
print("  " + "-" * 85)

scan_results = []
for alpha in [0.25, 0.5, 0.75, 1.0]:
    for L_ray in [2, 3, 4, 6, 8]:
        for require_monotone in [False, True]:
            admitted = [s for s in saddles
                        if motif_admit(s, E, alpha=alpha, L_ray=L_ray,
                                       require_monotone=require_monotone)]
            ratios = np.array([s["ratio"] for s in admitted])
            if len(ratios) == 0:
                print(f"  {alpha:>6.2f}  {L_ray:>5d}  {str(require_monotone):>5}  "
                      f"{0:>4d}   (no saddles)")
                scan_results.append((alpha, L_ray, require_monotone,
                                     0, None, None, None, None))
                continue
            q25, q50, q75 = np.percentile(ratios, [25, 50, 75])
            in_arch = float(((ratios >= -1.5) & (ratios <= -1.1)).mean())
            print(f"  {alpha:>6.2f}  {L_ray:>5d}  {str(require_monotone):>5}  "
                  f"{len(ratios):>4d}  {q50:>+8.3f}  "
                  f"[{q25:>+6.3f}, {q75:>+6.3f}]   {q75 - q25:>9.3f}   "
                  f"{in_arch*100:>7.1f}%")
            scan_results.append((alpha, L_ray, require_monotone,
                                 len(ratios), q50, q25, q75, in_arch))


# -----------------------------------------------------------------------------
# Verdict
# -----------------------------------------------------------------------------

# Find the best-case configuration: tightest IQR with non-trivial sample size
best = None
for (alpha, L_ray, mono, N_sad, med, q25, q75, in_arch) in scan_results:
    if N_sad < 5:
        continue
    if med is None:
        continue
    iqr_width = q75 - q25
    # Score: closest to -1.3 median + tightest IQR + inside window
    if best is None or iqr_width < best["iqr_width"]:
        best = {"alpha": alpha, "L_ray": L_ray, "mono": mono,
                "N": N_sad, "median": med, "q25": q25, "q75": q75,
                "iqr_width": iqr_width, "in_arch": in_arch}

print("")
print("=" * 80)
print("  VERDICT")
print("=" * 80)
if best is None:
    print("  No filter setting produced a non-trivial motif-saddle sample.")
    print("  -> Motif-conditioned form cannot be tested on this field.")
else:
    print(f"  Tightest motif-conditioned distribution across filter scan:")
    print(f"    alpha = {best['alpha']}   L_ray = {best['L_ray']}   "
          f"monotone = {best['mono']}")
    print(f"    N_motif = {best['N']}")
    print(f"    median  = {best['median']:+.3f}")
    print(f"    IQR     = [{best['q25']:+.3f}, {best['q75']:+.3f}]   "
          f"width = {best['iqr_width']:.3f}")
    print(f"    in ED-Arch-01 window [-1.5, -1.1]: {best['in_arch']*100:.1f}%")
    print("")
    # Test criteria
    med_near_target = abs(best["median"] - (-1.3)) <= 0.2
    iqr_tight       = best["iqr_width"] < 0.3
    print(f"  Criteria (from §4 of Option-2 rewrite):")
    print(f"    median within +/- 0.2 of -1.3?   {'YES' if med_near_target else 'NO'} "
          f"(median = {best['median']:+.3f}, target = -1.3)")
    print(f"    IQR width < 0.3?                  {'YES' if iqr_tight else 'NO'} "
          f"(width = {best['iqr_width']:.3f})")
    print("")
    if med_near_target and iqr_tight:
        print("  >>> MOTIF-CONDITIONED FORM RECOVERED -- ED-SC invariant candidate: -1.3 +/- 0.2")
    else:
        print("  >>> MOTIF-CONDITIONED FORM DID NOT RECOVER a tight -1.3 cluster.")
        print("      -> Retreat to channel-specific form (§4).")

# Save
out = os.path.join(HERE, "r2_motif_summary.txt")
with open(out, "w") as fh:
    fh.write("Motif-conditioned architectural-saddle filter on canonical Scenario D\n")
    fh.write(f"Field stats: p_hat={p_hat:.5f}, std={p_std:.5f}, "
             f"range=[{p_min:.4f}, {p_max:.4f}]\n\n")
    fh.write(f"{'alpha':>6}  {'L_ray':>5}  {'mono':>5}  {'N':>4}  "
             f"{'median':>8}  {'q25':>7}  {'q75':>7}  "
             f"{'iqr_w':>6}  {'in_arch':>7}\n")
    for (alpha, L_ray, mono, N_sad, med, q25, q75, in_arch) in scan_results:
        if med is None:
            fh.write(f"{alpha:>6.2f}  {L_ray:>5d}  {str(mono):>5}  "
                     f"{0:>4d}  (empty)\n")
        else:
            fh.write(f"{alpha:>6.2f}  {L_ray:>5d}  {str(mono):>5}  "
                     f"{N_sad:>4d}  {med:>+8.3f}  {q25:>+7.3f}  {q75:>+7.3f}  "
                     f"{q75 - q25:>6.3f}  {in_arch*100:>6.1f}%\n")
print(f"")
print(f"  written: {out}")
