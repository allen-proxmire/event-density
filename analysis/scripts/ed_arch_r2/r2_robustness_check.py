"""
Robustness check for the R2 result.
Runs Scenario D at the saddle-peak (n*, sigma*) under multiple
(alpha, gamma, seed) choices and reports the median/mean/IQR of
field-space Hessian eigenvalue ratios at Morse saddles.

If the ratio distribution peaks at -1 across all (alpha, gamma, seed)
triples, R2's isotropy prediction is confirmed regardless of the
penalty-parameter choice and the conclusion is robust.
"""

from __future__ import annotations

import os
import time
import numpy as np

# Import the main test machinery
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from r2_field_hessian_test import (
    run_scenario_d, find_saddles, hessian_at,
)


def one_test(
    N: int, T: int, n_mob: float, sigma: float,
    alpha: float, gamma: int, dt: float,
    p_min: float, p_max: float, ic_scale: float,
    seed: int, deg_tol: float = 0.10,
) -> tuple[float, float, float, int, int]:
    """Return (median, mean, std, n_saddles_kept, n_discarded_deg)."""
    rng = np.random.default_rng(seed)
    p = run_scenario_d(
        N=N, T=T, n_mob=n_mob, sigma=sigma,
        alpha=alpha, gamma=gamma, dt=dt,
        p_min=p_min, p_max=p_max, ic_scale=ic_scale, rng=rng,
    )
    ij, smooth = find_saddles(p)
    ratios: list[float] = []
    n_deg = 0
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
            n_deg += 1
            continue
        if abs(kneg) >= abs(kpos):
            ratios.append(kneg / kpos)
        else:
            ratios.append(kpos / kneg)
    if not ratios:
        return (float("nan"), float("nan"), float("nan"), 0, n_deg)
    r = np.array(ratios)
    return (float(np.median(r)), float(r.mean()), float(r.std()), len(r), n_deg)


def main() -> None:
    # Fixed: (n*, sigma*) = ED-Arch-01 saddle peak
    N        = 512
    T        = 457
    n_mob    = 2.7
    sigma    = 0.0556
    dt       = 1.0
    p_min    = -1.0
    p_max    = 1.0
    ic_scale = 0.05

    # Scan (alpha, gamma, seed)
    configs = [
        # alpha,   gamma, seed
        ( 1.0,     3,     20260417),  # nominal
        ( 1.0,     3,     1),         # seed robustness
        ( 1.0,     3,     7),
        ( 0.1,     3,     20260417),  # weaker penalty
        ( 0.01,    3,     20260417),  # much weaker penalty
        (10.0,     3,     20260417),  # stronger penalty
        ( 1.0,     5,     20260417),  # quintic penalty
        ( 1.0,     2,     20260417),  # quadratic (non-GL) penalty (odd; keep sign-fix)
    ]

    print(f"{'alpha':>8} {'gamma':>6} {'seed':>10} {'N_sad':>7} {'N_deg':>7} "
          f"{'median':>9} {'mean':>9} {'std':>8}")
    print("-" * 80)
    summary_rows = []
    t0 = time.time()
    for (alpha, gamma, seed) in configs:
        if gamma % 2 == 0:
            # Fix: even gamma makes penalty sign wrong; use -|p|^gamma * sign(p) form
            # Skip for now; only odd gamma matches ED-SC-05.5 cubic-like form.
            continue
        med, mean, std, n_sad, n_deg = one_test(
            N=N, T=T, n_mob=n_mob, sigma=sigma,
            alpha=alpha, gamma=gamma, dt=dt,
            p_min=p_min, p_max=p_max, ic_scale=ic_scale,
            seed=seed,
        )
        print(f"{alpha:>8.3f} {gamma:>6d} {seed:>10d} {n_sad:>7d} {n_deg:>7d} "
              f"{med:>+9.4f} {mean:>+9.4f} {std:>8.4f}")
        summary_rows.append((alpha, gamma, seed, n_sad, n_deg, med, mean, std))
    dt_total = time.time() - t0
    print("-" * 80)
    print(f"total runtime: {dt_total:.1f}s")

    # Save
    with open(os.path.join(HERE, "r2_robustness_summary.txt"), "w") as fh:
        fh.write("ED-Arch-01 R2 robustness scan\n")
        fh.write(f"N={N}, T={T}, n={n_mob}, sigma={sigma}, dt={dt}\n")
        fh.write(f"{'alpha':>8} {'gamma':>6} {'seed':>10} {'N_sad':>7} "
                 f"{'N_deg':>7} {'median':>9} {'mean':>9} {'std':>8}\n")
        for row in summary_rows:
            fh.write(
                f"{row[0]:>8.3f} {row[1]:>6d} {row[2]:>10d} "
                f"{row[3]:>7d} {row[4]:>7d} "
                f"{row[5]:>+9.4f} {row[6]:>+9.4f} {row[7]:>8.4f}\n"
            )


if __name__ == "__main__":
    main()
