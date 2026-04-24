"""Implement the three GRF falsifier tests for r* = -1.304 on the R2
simulator.

Tests
-----
1. Scale invariance under (alpha, sigma) rescaling, p_hat held fixed.
   GRF prediction: r* unchanged within +/- 0.05.

2. Ray-length L_ray = 2 -> 4.
   GRF prediction: r* shifts toward -1.55 to -1.7 (more anisotropic).

3. Ray-count N_req = 2 -> 4 (out of 4 principal-axis rays).
   GRF prediction: r* shifts toward -1.15 to -1.2 (more isotropic).

Protocol
--------
* 10 realisations (seeds 77, 101, 123, ..., 2021), 500 steps each, 64x64 grid.
* Motif filter: ray-endpoint sign test on the 4 principal-axis rays of the
  smoothed Hessian.
* Baseline filter: alpha_filt = 0.5, L_ray = 2, N_req = 2 (out of 4).
* Report median ratio and bootstrap-95% CI across motifs pooled over seeds.
"""

from __future__ import annotations

import json
import os
import sys
import time
import numpy as np

ED_SIM_CODE = r"C:\Users\allen\GitHub\Emergence Universe\ED-SIM-Code"
if ED_SIM_CODE not in sys.path:
    sys.path.insert(0, ED_SIM_CODE)

from ED_Update_Rule import ed_step_mobility

HERE = os.path.dirname(os.path.abspath(__file__))


# -----------------------------------------------------------------------------
# Canonical R2 parameters
# -----------------------------------------------------------------------------

SIZE         = 64
STEPS        = 500
ALPHA0       = 0.03
GAMMA        = 0.5
DT           = 0.05
P_MIN, P_MAX = 0.01, 1.0
BOUNDARY     = "periodic"
MOBILITY_EXP = 2.7
NOISE0       = 0.0556
DEG_TOL      = 0.10

SEEDS = [77, 101, 123, 234, 456, 789, 1011, 1213, 1415, 2021]


# -----------------------------------------------------------------------------
# Simulator
# -----------------------------------------------------------------------------

def run_scenario_d(alpha: float, noise_amp: float, seed: int,
                   steps: int = STEPS, size: int = SIZE) -> np.ndarray:
    rng = np.random.default_rng(seed)
    p = rng.uniform(0.3, 0.7, size=(size, size))
    for _ in range(steps):
        p = ed_step_mobility(
            p, alpha=alpha, gamma=GAMMA, dt=DT,
            p_min=P_MIN, p_max=P_MAX, boundary=BOUNDARY,
            mobility_exp=MOBILITY_EXP, noise_scale=noise_amp, rng=rng,
        )
    return p


# -----------------------------------------------------------------------------
# Saddle detection + motif filter
# -----------------------------------------------------------------------------

def smooth_field(p: np.ndarray) -> np.ndarray:
    return p + 0.2 * (
        np.roll(p, 1, 0) + np.roll(p, -1, 0)
      + np.roll(p, 1, 1) + np.roll(p, -1, 1)
      - 4.0 * p
    )


def find_morse_saddles(E: np.ndarray, deg_tol: float = DEG_TOL):
    dpdx = 0.5 * (np.roll(E, -1, 0) - np.roll(E, 1, 0))
    dpdy = 0.5 * (np.roll(E, -1, 1) - np.roll(E, 1, 1))
    sx_pos, sx_neg = dpdx > 0, dpdx < 0
    sy_pos, sy_neg = dpdy > 0, dpdy < 0
    xsc = (sx_pos & np.roll(sx_neg, -1, 0)) | (sx_neg & np.roll(sx_pos, -1, 0))
    ysc = (sy_pos & np.roll(sy_neg, -1, 1)) | (sy_neg & np.roll(sy_pos, -1, 1))
    cand = xsc & ysc
    interior = np.zeros_like(cand)
    interior[4:-4, 4:-4] = True
    cand &= interior
    out = []
    for (i, j) in np.argwhere(cand):
        i, j = int(i), int(j)
        d2x = E[i+1, j] - 2*E[i, j] + E[i-1, j]
        d2y = E[i, j+1] - 2*E[i, j] + E[i, j-1]
        dxy = 0.25 * (E[i+1, j+1] - E[i+1, j-1] - E[i-1, j+1] + E[i-1, j-1])
        H = np.array([[d2x, dxy], [dxy, d2y]])
        det = d2x * d2y - dxy * dxy
        if det >= 0:
            continue
        w, V = np.linalg.eigh(H)
        if not (w[0] < 0 < w[1]):
            continue
        if min(abs(w[0]), abs(w[1])) / max(abs(w[0]), abs(w[1])) < deg_tol:
            continue
        if abs(w[0]) >= abs(w[1]):
            ratio = w[0] / w[1]
        else:
            ratio = w[1] / w[0]
        out.append({
            "i": i, "j": j, "E_at": float(E[i, j]),
            "lam_neg": float(w[0]), "lam_pos": float(w[1]),
            "e_neg": V[:, 0], "e_pos": V[:, 1],
            "ratio": float(ratio),
        })
    return out


def trace_endpoint(E, i, j, direction, sign, L_ray):
    Ny, Nx = E.shape
    di = sign * direction[0] * L_ray
    dj = sign * direction[1] * L_ray
    ii = int(round(i + di)) % Ny
    jj = int(round(j + dj)) % Nx
    return float(E[ii, jj])


def motif_pass(saddle, E, p_hat, p_std, alpha_filt, L_ray, N_req):
    """Return True if saddle passes ray-endpoint filter.
    Four principal-axis rays; count how many pass sign test; compare to N_req.
    """
    hi = p_hat + alpha_filt * p_std
    lo = p_hat - alpha_filt * p_std
    e_neg, e_pos = saddle["e_neg"], saddle["e_pos"]
    i, j = saddle["i"], saddle["j"]

    # Negative-eigenvalue axis: endpoint should be < lo (saddle is max along this axis).
    # Positive-eigenvalue axis: endpoint should be > hi (saddle is min along this axis).
    checks = [
        trace_endpoint(E, i, j, e_neg, +1, L_ray) < lo,
        trace_endpoint(E, i, j, e_neg, -1, L_ray) < lo,
        trace_endpoint(E, i, j, e_pos, +1, L_ray) > hi,
        trace_endpoint(E, i, j, e_pos, -1, L_ray) > hi,
    ]
    return sum(checks) >= N_req


# -----------------------------------------------------------------------------
# Test driver
# -----------------------------------------------------------------------------

def run_config(label, alpha, noise_amp, alpha_filt, L_ray, N_req):
    t0 = time.time()
    pooled = []
    per_seed = []
    p_hats = []
    p_stds = []
    for seed in SEEDS:
        p = run_scenario_d(alpha, noise_amp, seed)
        E = smooth_field(p)
        p_hat = float(p.mean()); p_std = float(p.std())
        p_hats.append(p_hat); p_stds.append(p_std)
        sads = find_morse_saddles(E)
        admitted = [s for s in sads
                    if motif_pass(s, E, p_hat, p_std, alpha_filt, L_ray, N_req)]
        r = [s["ratio"] for s in admitted]
        pooled.extend(r)
        per_seed.append({
            "seed": seed, "n_cand": len(sads), "n_motif": len(r),
            "median": float(np.median(r)) if r else None,
            "p_hat": p_hat, "p_std": p_std,
        })
    t_run = time.time() - t0
    result = {
        "label": label,
        "params": {"alpha": alpha, "noise": noise_amp,
                   "alpha_filt": alpha_filt, "L_ray": L_ray, "N_req": N_req},
        "n_total": len(pooled),
        "t_run": t_run,
        "p_hat_mean": float(np.mean(p_hats)),
        "p_std_mean": float(np.mean(p_stds)),
        "per_seed": per_seed,
    }
    if pooled:
        pooled = np.array(pooled)
        q25, q50, q75 = np.percentile(pooled, [25, 50, 75])
        # Bootstrap-95 CI for the median
        rng = np.random.default_rng(12345)
        B = 4000
        boot = [np.median(rng.choice(pooled, size=len(pooled), replace=True))
                for _ in range(B)]
        ci_lo, ci_hi = np.percentile(boot, [2.5, 97.5])
        result.update({
            "median": float(q50), "q25": float(q25), "q75": float(q75),
            "ci95_lo": float(ci_lo), "ci95_hi": float(ci_hi),
            "mean": float(pooled.mean()), "std": float(pooled.std()),
        })
    else:
        result.update({"median": None})
    return result


def main():
    print("="*100)
    print("  R2 GRF Falsifier Tests")
    print("="*100)

    # Canonical R2 motif filter (reproducing ED-Arch-01 r*=-1.304):
    #   alpha_filt = 0.25, L_ray = 2, N_req = 4 (all four principal-axis rays).
    # This is the "baseline" for Tests 1 and 2.
    # Test 3 loosens N_req to 2 as the "looser baseline" and tightens to 4
    # (the canonical) as the stricter condition; GRF predicts the stricter
    # filter pushes r* toward less-anisotropic (closer to -1).
    ALPHA_F, L0, NREQ0 = 0.25, 2, 4

    # Scale-invariance rescaling: preserve the noise-driven mean-field balance.
    # In the linearised SPDE alpha_eff = alpha*gamma*p_hat^{gamma-1}; keeping
    # p_hat fixed requires alpha -> k*alpha, and sigma -> sigma*sqrt(k) preserves
    # the GRF variance ratio sigma^2 / alpha_eff at fixed p_hat.
    K_RESCALE = 2.0

    configs = [
        # Test 1: scale invariance (alpha, sigma) -> (k*alpha, sigma*sqrt(k)).
        ("T1a_baseline",    ALPHA0,             NOISE0,                       ALPHA_F, L0, NREQ0),
        ("T1b_rescaled",    K_RESCALE*ALPHA0,   NOISE0*np.sqrt(K_RESCALE),    ALPHA_F, L0, NREQ0),

        # Test 2: ray-length L_ray = 2 -> 4 (at canonical alpha_filt, N_req).
        ("T2a_Lray2",       ALPHA0, NOISE0, ALPHA_F, 2, NREQ0),
        ("T2b_Lray4",       ALPHA0, NOISE0, ALPHA_F, 4, NREQ0),

        # Test 3: ray-count N_req = 2 -> 4.
        ("T3a_Nreq2",       ALPHA0, NOISE0, ALPHA_F, L0, 2),
        ("T3b_Nreq4",       ALPHA0, NOISE0, ALPHA_F, L0, 4),
    ]

    results = []
    for cfg in configs:
        r = run_config(*cfg)
        results.append(r)
        if r.get("median") is None:
            print(f"  {cfg[0]:>18s}  N=0 motifs  t={r['t_run']:.1f}s")
        else:
            print(f"  {cfg[0]:>18s}  N={r['n_total']:>4d}  "
                  f"med={r['median']:+.3f}  "
                  f"CI95=[{r['ci95_lo']:+.3f},{r['ci95_hi']:+.3f}]  "
                  f"IQR=[{r['q25']:+.3f},{r['q75']:+.3f}]  "
                  f"p_hat={r['p_hat_mean']:.4f}  t={r['t_run']:.1f}s")

    with open(os.path.join(HERE, "r2_grf_falsifier_results.json"), "w") as fh:
        # strip np arrays -- we already cast
        json.dump(results, fh, indent=2)
    print("\n  saved: r2_grf_falsifier_results.json")


if __name__ == "__main__":
    main()
