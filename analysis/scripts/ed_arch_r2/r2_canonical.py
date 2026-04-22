"""
ED-Arch R2 field-space Hessian test — CANONICAL reproduction.

Uses the actual Scenario D update rule from the Emergence Universe repo
(ED_Update_Rule.py: ed_step_mobility), with the canonical parameters
discovered in Run_Simulation.py:

    alpha        = 0.03       (NOT 1.0)
    beta         = 0.20       (gradient smoothing; this is the Laplacian coefficient)
    gamma        = 0.5        (CONCAVE; NOT 3.0)
    dt           = 0.05       (NOT 1.0)
    mobility_exp = 2.7        (saddle peak; this is the "n" in ED-Arch-01)
    noise_amp    = 0.0556     (saddle peak)
    size         = 64         (NOT 512)
    steps        = 500
    IC           = uniform[0.3, 0.7]
    p_min, p_max = 0.01, 1.0
    boundary     = periodic
    mode         = mobility-weighted (ed_step_mobility)
    seed         = 77         (canonical run seed from Run_Simulation.py)

The mobility-weighted update is:
    M(p)    = ((p_max - p) / p_max) ** mobility_exp
    J_k     = M((p + p_k)/2) * (p_k - p)           for each neighbour k
    delta_p = sum_k J_k  -  alpha * p^gamma  +  N(0, noise_amp)
    p_new   = clip(p + dt * delta_p, p_min, p_max)

R2 test: compute field-space Hessian H_field = d2p/dx_i dx_j at spatial
stationary points of the final p(x, y), report eigenvalue ratio distribution.
Previous R2 attempts used the wrong update rule (they had n as the Laplacian
coefficient and gamma=3).  This is the corrected test.
"""

from __future__ import annotations

import os
import sys
import time
import numpy as np

# Import the canonical update rule.
ED_SIM_CODE = r"C:\Users\allen\GitHub\Emergence Universe\ED-SIM-Code"
if ED_SIM_CODE not in sys.path:
    sys.path.insert(0, ED_SIM_CODE)

from ED_Update_Rule import ed_step_mobility, gradient_magnitude, coarse_grained_stats


# -----------------------------------------------------------------------------
# Canonical parameters (from Run_Simulation.py Scenario D)
# -----------------------------------------------------------------------------

SIZE         = 64
STEPS        = 500
ALPHA        = 0.03
GAMMA        = 0.5
DT           = 0.05
P_MIN, P_MAX = 0.01, 1.0
BOUNDARY     = "periodic"
SEED         = 77                  # canonical seed from EDLattice(seed=77)

# Saddle peak from ED-Arch-01:
MOBILITY_EXP = 2.7
NOISE_AMP    = 0.0556

# Numerical filter: discard saddles with |lambda_min|/|lambda_max| < deg_tol
DEG_TOL      = 0.10

OUTDIR       = os.path.dirname(os.path.abspath(__file__))


# -----------------------------------------------------------------------------
# Initial condition (matches EDLattice.init_random_noise(lo=0.3, hi=0.7))
# -----------------------------------------------------------------------------

def init_random_noise(rng: np.random.Generator, size: int,
                      lo: float = 0.3, hi: float = 0.7) -> np.ndarray:
    return rng.uniform(lo, hi, size=(size, size))


# -----------------------------------------------------------------------------
# Scenario D runner (canonical)
# -----------------------------------------------------------------------------

def run_scenario_d_canonical(
    mobility_exp: float, noise_amp: float,
    size: int = SIZE, steps: int = STEPS, seed: int = SEED,
) -> tuple[np.ndarray, dict]:
    rng = np.random.default_rng(seed)
    p = init_random_noise(rng, size)
    t0 = time.time()
    for t in range(steps):
        p = ed_step_mobility(
            p,
            alpha=ALPHA,
            gamma=GAMMA,
            dt=DT,
            p_min=P_MIN,
            p_max=P_MAX,
            boundary=BOUNDARY,
            mobility_exp=mobility_exp,
            noise_scale=noise_amp,
            rng=rng,
        )
    t_run = time.time() - t0
    stats = coarse_grained_stats(p, boundary=BOUNDARY)
    stats["t_run"] = t_run
    stats["t_phys"] = DT * steps
    return p, stats


# -----------------------------------------------------------------------------
# Saddle detection and Hessian evaluation (reused from r2_field_hessian_test.py)
# -----------------------------------------------------------------------------

def central_diff(p: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    dpdx = 0.5 * (np.roll(p, -1, axis=0) - np.roll(p, 1, axis=0))
    dpdy = 0.5 * (np.roll(p, -1, axis=1) - np.roll(p, 1, axis=1))
    return dpdx, dpdy


def find_saddles(p: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    smooth = (
        p
        + 0.2 * (np.roll(p,  1, 0) + np.roll(p, -1, 0)
               + np.roll(p,  1, 1) + np.roll(p, -1, 1)
               - 4.0 * p)
    )
    dpdx, dpdy = central_diff(smooth)
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
    interior = np.zeros_like(candidates)
    interior[4:-4, 4:-4] = True
    candidates &= interior
    ij = np.argwhere(candidates)
    return ij, smooth


def hessian_at(p: np.ndarray, i: int, j: int) -> np.ndarray:
    d2x = p[i + 1, j] - 2.0 * p[i, j] + p[i - 1, j]
    d2y = p[i, j + 1] - 2.0 * p[i, j] + p[i, j - 1]
    dxy = 0.25 * (
        p[i + 1, j + 1] - p[i + 1, j - 1]
      - p[i - 1, j + 1] + p[i - 1, j - 1]
    )
    return np.array([[d2x, dxy], [dxy, d2y]])


def extract_ratios(p: np.ndarray, deg_tol: float = DEG_TOL) -> tuple[np.ndarray, int, int]:
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
    return np.array(ratios), len(ij), n_deg


# -----------------------------------------------------------------------------
# Main — saddle-peak R2 test
# -----------------------------------------------------------------------------

def summarize(label: str, r: np.ndarray) -> dict:
    if len(r) == 0:
        print(f"  {label}: NO saddles detected")
        return {"label": label, "n": 0}
    p5, p25, p50, p75, p95 = np.percentile(r, [5, 25, 50, 75, 95])
    in_arch = float(((r >= -1.5) & (r <= -1.1)).mean())
    near_1  = float(((r >= -1.17) & (r <= -0.83)).mean())
    print(f"  {label:40s}  N={len(r):4d}  "
          f"med={p50:+.3f}  mean={r.mean():+.3f}  std={r.std():.3f}  "
          f"IQR=[{p25:+.3f},{p75:+.3f}]  in_arch={in_arch*100:.1f}%  "
          f"near_-1={near_1*100:.1f}%")
    return {
        "label": label, "n": len(r),
        "median": p50, "mean": float(r.mean()), "std": float(r.std()),
        "p5": p5, "p95": p95, "p25": p25, "p75": p75,
        "frac_in_arch": in_arch, "frac_near_-1": near_1,
    }


def main() -> None:
    print("="*100)
    print("  ED-Arch R2 CANONICAL field-space Hessian test")
    print(f"  alpha={ALPHA}  beta=(not used, replaced by mobility-weighted diffusion)  "
          f"gamma={GAMMA}  dt={DT}  size={SIZE}  steps={STEPS}  seed={SEED}")
    print(f"  mobility_exp (n*) = {MOBILITY_EXP}   noise_amp (sigma*) = {NOISE_AMP}")
    print("="*100)

    # --- Saddle peak run ---
    p, stats = run_scenario_d_canonical(MOBILITY_EXP, NOISE_AMP)
    print(f"  run done in {stats['t_run']:.1f}s, t_phys={stats['t_phys']}")
    print(f"  p_hat={stats['p_hat']:.5f}  G={stats['G']:.5f}  "
          f"L={stats['L']:.1f}  p_min={p.min():.4f}  p_max={p.max():.4f}  "
          f"std(p)={p.std():.5f}")
    r, n_cand, n_deg = extract_ratios(p)
    print(f"  saddle candidates: {n_cand}, degenerate discarded: {n_deg}")
    print("")
    summary_peak = summarize("saddle peak (n=2.7, sigma=0.0556)", r)

    # --- Parameter-grid scan: exactly the 4x4 ED-Arch-01 sweep ---
    print("\n  4x4 sweep over (mobility_exp, noise_amp):")
    print("  " + "-"*98)
    EXPONENTS    = [0.5, 1.0, 2.0, 4.0]
    NOISE_LEVELS = [0.01, 0.02, 0.05, 0.10]
    rows = []
    for n_mob in EXPONENTS:
        for noise in NOISE_LEVELS:
            p, stats = run_scenario_d_canonical(n_mob, noise)
            r, _, _ = extract_ratios(p)
            if len(r) == 0:
                print(f"  n={n_mob:>5} noise={noise:>6}  N=0 (no saddles)")
                rows.append((n_mob, noise, 0, None, None, None, None))
                continue
            med = float(np.median(r))
            mn  = float(r.mean())
            in_arch = float(((r >= -1.5) & (r <= -1.1)).mean())
            near_1  = float(((r >= -1.17) & (r <= -0.83)).mean())
            print(f"  n={n_mob:>5} noise={noise:>6}  N={len(r):>4}  "
                  f"med={med:+.3f}  mean={mn:+.3f}  "
                  f"in_arch={in_arch*100:5.1f}%  near_-1={near_1*100:5.1f}%  "
                  f"p_hat={stats['p_hat']:.4f}  L={stats['L']:.1f}")
            rows.append((n_mob, noise, len(r), med, mn, in_arch, near_1))

    # --- Save ---
    np.save(os.path.join(OUTDIR, "r2_canonical_p_final.npy"), p)
    np.save(os.path.join(OUTDIR, "r2_canonical_ratios.npy"), r)
    with open(os.path.join(OUTDIR, "r2_canonical_summary.txt"), "w") as fh:
        fh.write("ED-Arch R2 CANONICAL field-space Hessian test\n")
        fh.write(f"Params: alpha={ALPHA}, gamma={GAMMA}, dt={DT}, size={SIZE}, "
                 f"steps={STEPS}, seed={SEED}, p_min={P_MIN}, p_max={P_MAX}\n\n")
        fh.write("Saddle peak (n=2.7, sigma=0.0556):\n")
        for k, v in summary_peak.items():
            fh.write(f"  {k}: {v}\n")
        fh.write("\n4x4 sweep:\n")
        fh.write(f"{'n':>6} {'noise':>7} {'N':>5} {'med':>7} {'mean':>7} "
                 f"{'in_arch':>8} {'near_-1':>8}\n")
        for row in rows:
            (n_mob, noise, N, med, mn, ia, n1) = row
            if N == 0:
                fh.write(f"{n_mob:>6} {noise:>7} {N:>5} (no saddles)\n")
            else:
                fh.write(f"{n_mob:>6} {noise:>7} {N:>5} {med:>+7.3f} {mn:>+7.3f} "
                         f"{ia*100:>7.1f}% {n1*100:>7.1f}%\n")
    print("\n  outputs saved")


if __name__ == "__main__":
    main()
