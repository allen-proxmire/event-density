"""
ED-Arch R2 field-space Hessian test.

Purpose
-------
Runs Scenario D (ED-Arch-01) at the reported saddle-peak parameters
(n = 2.7, sigma = 0.0556) on a 512x512 periodic lattice, then evaluates
the FIELD-SPACE Hessian H_field = [[d2p/dx2, d2p/dxdy],
                                   [d2p/dxdy, d2p/dy2]]
at every interior spatial stationary point of p(x, y) at the final step.

This is the direct R2 check. It answers: does the Scenario D field p(x, y)
itself carry the reported kappa_para/kappa_perp = -1.3, or is -1.3 a property
only of the (n, sigma) parameter-space Hessian H_param?

Under the R2 prediction (isotropy argument), the expected field-space
ratio is -1 +/- fluctuations because the update rule has no preferred
spatial direction:

  p_{t+1}(i,j) = p(i,j) + dt * [ n * Lap(p) - alpha * p^gamma + sigma * eta ]

If the measured distribution clusters near -1, R2 is inconsistent with
ED-Arch-01's published -1.3 as a field-space invariant: the -1.3 is then
only a property of the parameter-space observable surface, not of the
event-density field itself.

Parameters
----------
The Scenario D update rule parameters alpha, gamma, dt, and IC scale are
not all stated in the ED-Arch-01 excerpts I have. I use defaults that
match the ED-SC-05.5 / ED-12.5 cubic gradient-flow form (gamma = 3) and
standard soft-bounding (alpha = 1.0, clamp at +/- 1). dt = 1 as stated.
IC is a small-amplitude Gaussian random field.

Outputs
-------
- Prints summary statistics of field-space Hessian eigenvalue ratio.
- Saves:
    r2_field_hessian_summary.txt   (human-readable summary)
    r2_field_hessian_ratios.npy    (per-saddle ratios)
    r2_p_final.npy                 (final p field)
    r2_saddle_map.png              (optional visualization if matplotlib)
"""

from __future__ import annotations

import os
import sys
import time
import numpy as np

# -----------------------------------------------------------------------------
# Parameters
# -----------------------------------------------------------------------------

N           = 512          # lattice size
# Stable explicit-Euler integration: CFL for 5-point Laplacian requires
# dt * n * 4 / h^2 < 2.  With h = 1 and n = 2.7, dt must be < 0.185.
# We use dt = 0.1 internally and rescale T to match 457 iterations of the
# paper's dt = 1 update (i.e. physical time t_phys = 457).
dt          = 0.1
T_phys      = 457.0        # physical time from ED-Arch-01 (step 457 at dt=1)
T           = int(T_phys / dt)   # = 4570 stable sub-steps
n_mob       = 2.7
sigma       = 0.0556
alpha       = 1.0
gamma       = 3
p_min, p_max = -1.0, 1.0
ic_scale    = 0.05
seed        = 20260417
# Numerical filter: discard saddles with |lambda_min|/|lambda_max| < deg_tol
# (these are near-degenerate Hessians where one eigenvalue is noise-level).
deg_tol     = 0.10

RNG = np.random.default_rng(seed)

OUTDIR = os.path.dirname(os.path.abspath(__file__))


# -----------------------------------------------------------------------------
# Laplacian (5-point, periodic BC)
# -----------------------------------------------------------------------------

def laplacian(p: np.ndarray) -> np.ndarray:
    """5-point periodic Laplacian with unit grid spacing."""
    return (
        np.roll(p,  1, axis=0) + np.roll(p, -1, axis=0)
      + np.roll(p,  1, axis=1) + np.roll(p, -1, axis=1)
      - 4.0 * p
    )


# -----------------------------------------------------------------------------
# Scenario D integrator
# -----------------------------------------------------------------------------

def run_scenario_d(
    N: int, T: int, n_mob: float, sigma: float,
    alpha: float, gamma: int, dt: float,
    p_min: float, p_max: float, ic_scale: float,
    rng: np.random.Generator,
) -> np.ndarray:
    """
    Run Scenario D update on an NxN periodic lattice for T steps at step dt.
    Langevin noise is scaled by sqrt(dt) to preserve the per-unit-time
    noise strength of the paper's dt=1 convention.
    """
    p = ic_scale * rng.standard_normal((N, N))
    sqrt_dt = np.sqrt(dt)
    for _ in range(T):
        lap   = laplacian(p)
        noise = rng.standard_normal((N, N))
        p = p + dt * (n_mob * lap - alpha * (p ** gamma)) + sigma * sqrt_dt * noise
        np.clip(p, p_min, p_max, out=p)
    return p


# -----------------------------------------------------------------------------
# Stationary-point detection and field-space Hessian
# -----------------------------------------------------------------------------

def central_diff(p: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Central-difference gradients on periodic lattice, unit spacing."""
    dpdx = 0.5 * (np.roll(p, -1, axis=0) - np.roll(p, 1, axis=0))
    dpdy = 0.5 * (np.roll(p, -1, axis=1) - np.roll(p, 1, axis=1))
    return dpdx, dpdy


def find_saddles(p: np.ndarray) -> np.ndarray:
    """
    Return (i, j) coordinates of grid points that are saddle stationary
    points of the SMOOTHED field, detected via:
      - both gradient components change sign across the 4 neighbors
      - Hessian has det < 0 at the point
    We first smooth p lightly to suppress noise-scale fluctuations so the
    stationary points are architectural, not noise-level.
    """
    # Mild smoothing: one iteration of (1+4+1 box)-type filter
    # to suppress single-pixel noise fluctuations before detecting saddles.
    smooth = (
        p
        + 0.2 * (np.roll(p,  1, 0) + np.roll(p, -1, 0)
               + np.roll(p,  1, 1) + np.roll(p, -1, 1)
               - 4.0 * p)
    )

    dpdx, dpdy = central_diff(smooth)

    # Sign-change detection: both gradient components change sign locally
    sx_pos = dpdx > 0
    sx_neg = dpdx < 0
    sy_pos = dpdy > 0
    sy_neg = dpdy < 0

    x_signchange = (
        (sx_pos & np.roll(sx_neg, -1, axis=0)) |
        (sx_neg & np.roll(sx_pos, -1, axis=0))
    )
    y_signchange = (
        (sy_pos & np.roll(sy_neg, -1, axis=1)) |
        (sy_neg & np.roll(sy_pos, -1, axis=1))
    )
    candidates = x_signchange & y_signchange

    # Restrict to interior to avoid edge artifacts (even with periodic BC,
    # we exclude the outer 4 rows/cols to be safe with finite-difference stencils).
    interior = np.zeros_like(candidates)
    interior[4:-4, 4:-4] = True
    candidates &= interior

    ij = np.argwhere(candidates)
    return ij, smooth


def hessian_at(p: np.ndarray, i: int, j: int) -> np.ndarray:
    """
    Central-difference Hessian of p at (i, j) with unit grid spacing.
    Returns 2x2 numpy array.
    """
    d2x = p[i + 1, j] - 2.0 * p[i, j] + p[i - 1, j]
    d2y = p[i, j + 1] - 2.0 * p[i, j] + p[i, j - 1]
    dxy = 0.25 * (
        p[i + 1, j + 1] - p[i + 1, j - 1]
      - p[i - 1, j + 1] + p[i - 1, j - 1]
    )
    return np.array([[d2x, dxy], [dxy, d2y]])


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main() -> None:
    t0 = time.time()
    print(f"[r2] running Scenario D: N={N}, T={T}, n={n_mob}, sigma={sigma}, "
          f"alpha={alpha}, gamma={gamma}, dt={dt}, seed={seed}")
    p = run_scenario_d(
        N=N, T=T, n_mob=n_mob, sigma=sigma,
        alpha=alpha, gamma=gamma, dt=dt,
        p_min=p_min, p_max=p_max, ic_scale=ic_scale,
        rng=RNG,
    )
    t_sim = time.time() - t0
    print(f"[r2] sim done in {t_sim:.1f}s. "
          f"Final field stats: min={p.min():.4f}, max={p.max():.4f}, "
          f"mean={p.mean():.4f}, std={p.std():.4f}")

    ij, smooth = find_saddles(p)
    print(f"[r2] found {len(ij)} saddle candidates (after det(H)<0 filter below)")

    ratios_ideal: list[float] = []   # larger-|k| over smaller-|k| (signed); |ratio| >= 1
    kappa_pairs: list[tuple[float, float]] = []
    deg_discarded = 0

    for (i, j) in ij:
        H = hessian_at(smooth, int(i), int(j))
        det = H[0, 0] * H[1, 1] - H[0, 1] * H[1, 0]
        if det >= 0:
            continue  # not a saddle
        w, _ = np.linalg.eigh(H)
        # w is sorted ascending. For a saddle, w[0] < 0 < w[1].
        if not (w[0] < 0 < w[1]):
            continue
        kneg, kpos = float(w[0]), float(w[1])
        # Discard near-degenerate Hessians (one eigenvalue near zero = noise).
        if min(abs(kneg), abs(kpos)) / max(abs(kneg), abs(kpos)) < deg_tol:
            deg_discarded += 1
            continue
        kappa_pairs.append((kneg, kpos))
        # "parallel" convention: the larger-magnitude direction.
        if abs(kneg) >= abs(kpos):
            ratio = kneg / kpos         # negative, |ratio| >= 1
        else:
            ratio = kpos / kneg         # negative, |ratio| >= 1 after flip
        ratios_ideal.append(ratio)

    ratios_ideal = np.array(ratios_ideal)
    print(f"[r2] discarded {deg_discarded} near-degenerate Hessians (|k_min|/|k_max| < {deg_tol})")

    if len(ratios_ideal) == 0:
        print("[r2] NO Morse saddle stationary points detected. "
              "Field may be too noisy or too smooth; investigate IC/T.")
        return

    print(f"[r2] {len(ratios_ideal)} Morse saddles kept after det(H)<0 filter")

    # Summary
    r = ratios_ideal  # larger-magnitude-in-numerator convention (matches ED-Arch usage)
    p5, p25, p50, p75, p95 = np.percentile(r, [5, 25, 50, 75, 95])
    mean, std = r.mean(), r.std()
    print("")
    print("=============================================================")
    print("  ED-Arch-01 R2 field-space Hessian test — results")
    print("=============================================================")
    print(f"  n = {n_mob}, sigma = {sigma}, N = {N}, T = {T}")
    print(f"  Saddle count: {len(r)}")
    print(f"  kappa_para / kappa_perp  (larger-|k| over smaller-|k|, signed)")
    print(f"    mean   = {mean:+.4f}")
    print(f"    std    = {std:.4f}")
    print(f"    median = {p50:+.4f}")
    print(f"    5–95%  = [{p5:+.4f}, {p95:+.4f}]")
    print(f"    25–75% = [{p25:+.4f}, {p75:+.4f}]")
    print(f"  ED-Arch-01 window (-1.3 +/- 0.2): [-1.5, -1.1]")
    print(f"  R2 isotropy prediction:            -1.0 +/- noise")
    in_window = ((r >= -1.5) & (r <= -1.1)).mean()
    near_one  = ((r >= -1.2) & (r <= -0.83)).mean()  # |r-(-1)| <= 0.17 symmetrically
    print(f"  Fraction in ED-Arch-01 window: {in_window*100:.1f}%")
    print(f"  Fraction near -1 (|r+1|<=0.17 symmetrically): {near_one*100:.1f}%")
    print("=============================================================")

    # Save
    np.save(os.path.join(OUTDIR, "r2_field_hessian_ratios.npy"), r)
    np.save(os.path.join(OUTDIR, "r2_p_final.npy"), p)
    with open(os.path.join(OUTDIR, "r2_field_hessian_summary.txt"), "w") as fh:
        fh.write("ED-Arch-01 R2 field-space Hessian test\n")
        fh.write(f"N={N}, T={T}, n={n_mob}, sigma={sigma}, "
                 f"alpha={alpha}, gamma={gamma}, dt={dt}, seed={seed}\n")
        fh.write(f"Saddle count: {len(r)}\n")
        fh.write(f"mean ratio: {mean:+.4f}\n")
        fh.write(f"std ratio:  {std:.4f}\n")
        fh.write(f"median:     {p50:+.4f}\n")
        fh.write(f"5-95 pct:   [{p5:+.4f}, {p95:+.4f}]\n")
        fh.write(f"25-75 pct:  [{p25:+.4f}, {p75:+.4f}]\n")
        fh.write(f"Fraction in [-1.5, -1.1]: {in_window*100:.1f}%\n")
        fh.write(f"Fraction near -1 (symmetric): {near_one*100:.1f}%\n")

    print(f"[r2] outputs saved to {OUTDIR}")
    t_total = time.time() - t0
    print(f"[r2] total runtime: {t_total:.1f}s")


if __name__ == "__main__":
    main()
