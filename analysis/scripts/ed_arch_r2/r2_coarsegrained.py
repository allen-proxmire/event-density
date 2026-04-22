"""
Coarse-grained Hessian check.
The grid-resolution Hessian of Scenario-D's clamped field picks up
saddles at pixel-scale wall-intersections where square-grid symmetry
forces kappa_para/kappa_perp = -1 exactly. That grid-symmetry can mask
any genuine architectural anisotropy.

This script:
  1. Runs Scenario D to T=457 at (n*, sigma*) on 512x512.
  2. Downsamples the field 8x (to 64x64) by block-averaging.
  3. Finds Morse saddles of the downsampled field.
  4. Computes Hessian eigenvalue ratios at those architectural-scale saddles.

If the architectural-scale distribution still clusters at -1 (not -1.3),
the R2 conclusion holds regardless of coarsening scale.
"""
from __future__ import annotations

import os
import numpy as np

import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from r2_field_hessian_test import (
    run_scenario_d, find_saddles, hessian_at,
)


def block_average(p: np.ndarray, block: int) -> np.ndarray:
    N = p.shape[0]
    assert N % block == 0
    m = N // block
    return p.reshape(m, block, m, block).mean(axis=(1, 3))


def extract_ratios(p: np.ndarray, deg_tol: float = 0.10) -> np.ndarray:
    ij, smooth = find_saddles(p)
    ratios: list[float] = []
    for (i, j) in ij:
        H = hessian_at(smooth, int(i), int(j))
        det = H[0, 0] * H[1, 1] - H[0, 1] * H[1, 0]
        if det >= 0:
            continue
        w, _ = np.linalg.eigh(H)
        if not (w[0] < 0 < w[1]):
            continue
        kneg, kpos = float(w[0]), float(w[1])
        if min(abs(kneg), abs(kpos)) / max(abs(kneg), abs(kpos)) < deg_tol:
            continue
        if abs(kneg) >= abs(kpos):
            ratios.append(kneg / kpos)
        else:
            ratios.append(kpos / kneg)
    return np.array(ratios)


def main() -> None:
    N        = 512
    T        = 457
    n_mob    = 2.7
    sigma    = 0.0556
    alpha    = 1.0
    gamma    = 3
    dt       = 1.0
    p_min    = -1.0
    p_max    = 1.0
    ic_scale = 0.05
    seed     = 20260417

    rng = np.random.default_rng(seed)
    p = run_scenario_d(
        N=N, T=T, n_mob=n_mob, sigma=sigma,
        alpha=alpha, gamma=gamma, dt=dt,
        p_min=p_min, p_max=p_max, ic_scale=ic_scale, rng=rng,
    )

    print(f"{'scale':>8} {'grid':>6} {'N_sad':>7} {'median':>9} {'mean':>9} "
          f"{'std':>8} {'frac_in_arch':>14} {'frac_near_-1':>14}")
    print("-" * 90)

    for block in [1, 2, 4, 8, 16]:
        if block == 1:
            pb = p
        else:
            pb = block_average(p, block)
        r = extract_ratios(pb)
        if len(r) == 0:
            print(f"{block:>8d} {pb.shape[0]:>6d}   (no Morse saddles detected)")
            continue
        median = float(np.median(r))
        mean   = float(r.mean())
        std    = float(r.std())
        in_arch = float(((r >= -1.5) & (r <= -1.1)).mean())
        near_1  = float(((r >= -1.17) & (r <= -0.83)).mean())
        print(f"{block:>8d} {pb.shape[0]:>6d} {len(r):>7d} "
              f"{median:>+9.4f} {mean:>+9.4f} {std:>8.4f} "
              f"{in_arch*100:>13.1f}% {near_1*100:>13.1f}%")

    print("-" * 90)
    print("scale = block size for block-average coarsening")
    print("grid  = side of coarsened lattice")
    print("frac_in_arch = fraction of saddles in ED-Arch-01 window [-1.5, -1.1]")
    print("frac_near_-1 = fraction with |ratio+1| <= 0.17")


if __name__ == "__main__":
    main()
