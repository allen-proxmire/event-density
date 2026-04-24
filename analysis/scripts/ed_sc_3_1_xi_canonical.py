"""Measure canonical xi on the ED-SIM mobility engine for ED-SC 3.1.

Simulator of record: r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility.
Read-only use: reads the module's canonical constants, never assigns to
them. Does NOT run the motif filter, saddle detection, or smoothing.

Computes xi as the radial half-decay length of the 2D autocorrelation
C(r) of the density deviation (p - <p>) at each snapshot, averaged over
snapshots within a seed, then averaged over seeds.
"""
import json
import os
import sys
import time
import numpy as np
from numpy.fft import fft2, ifft2, fftshift

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "ed_arch_r2"))
import r2_grf_falsifier_tests as fr  # simulator of record

from ED_Update_Rule import ed_step_mobility


def xi_halfdecay(field, dx=1.0):
    """Radial half-decay of 2D autocorrelation, GR-SC 1.7 prescription."""
    N = field.shape[0]
    f = field - np.mean(field)
    F = fft2(f)
    C = fftshift(np.real(ifft2(F * np.conj(F)))) / (N * N)
    c0 = C[N // 2, N // 2]
    if c0 <= 0:
        return float('nan')
    y, x = np.indices(C.shape)
    r = np.sqrt((x - N // 2) ** 2 + (y - N // 2) ** 2).astype(int)
    rmax = N // 2
    prof = np.empty(rmax)
    for k in range(rmax):
        mask = (r == k)
        prof[k] = C[mask].mean() if mask.any() else 0.0
    prof /= c0
    for k in range(1, rmax):
        if prof[k] <= 0.5:
            if prof[k - 1] == prof[k]:
                return float(k) * dx
            return float(k - 1 + (prof[k - 1] - 0.5)
                         / (prof[k - 1] - prof[k])) * dx
    return float(rmax) * dx


def run_seed_and_snapshot_xi(seed, alpha, noise_amp, steps, size,
                             snap_every=10, burn_in=100):
    """Evolve the canonical ED-SIM mobility engine and sample xi per snapshot.

    Snapshots xi on the raw density p (primary) and on the smoothed field
    E = smooth_field(p) (secondary, for audit).
    """
    rng = np.random.default_rng(seed)
    p = rng.uniform(0.3, 0.7, size=(size, size))
    xis_p = []
    xis_E = []
    for step in range(steps):
        p = ed_step_mobility(
            p, alpha=alpha, gamma=fr.GAMMA, dt=fr.DT,
            p_min=fr.P_MIN, p_max=fr.P_MAX, boundary=fr.BOUNDARY,
            mobility_exp=fr.MOBILITY_EXP, noise_scale=noise_amp, rng=rng,
        )
        if step >= burn_in and (step - burn_in) % snap_every == 0:
            xis_p.append(xi_halfdecay(p))
            xis_E.append(xi_halfdecay(fr.smooth_field(p)))
    return xis_p, xis_E


def main():
    seeds = fr.SEEDS  # simulator-of-record canonical list
    alpha = fr.ALPHA0
    noise_amp = fr.NOISE0
    steps = fr.STEPS
    size = fr.SIZE

    per_seed_p = {}
    per_seed_E = {}
    errors = {}
    all_xi_p = []
    all_xi_E = []
    t0 = time.time()
    for s in seeds:
        try:
            xip, xiE = run_seed_and_snapshot_xi(
                seed=s, alpha=alpha, noise_amp=noise_amp,
                steps=steps, size=size, snap_every=10, burn_in=100)
            if len(xip) == 0:
                per_seed_p[str(s)] = None
                per_seed_E[str(s)] = None
                errors[str(s)] = "no snapshots produced"
                continue
            xip_arr = np.array([x for x in xip if np.isfinite(x)])
            xiE_arr = np.array([x for x in xiE if np.isfinite(x)])
            per_seed_p[str(s)] = float(xip_arr.mean()) if len(xip_arr) else None
            per_seed_E[str(s)] = float(xiE_arr.mean()) if len(xiE_arr) else None
            all_xi_p.extend(xip_arr.tolist())
            all_xi_E.extend(xiE_arr.tolist())
            print(f"  seed={s}  xi_p={per_seed_p[str(s)]:.4f}  "
                  f"xi_E={per_seed_E[str(s)]:.4f}  "
                  f"(snaps={len(xip_arr)})", file=sys.stderr)
        except Exception as e:
            per_seed_p[str(s)] = None
            per_seed_E[str(s)] = None
            errors[str(s)] = repr(e)
            print(f"  seed={s}  FAILED: {e}", file=sys.stderr)

    out = {
        "method": "GR-SC 1.7 half-decay of 2D autocorrelation",
        "simulator": ("r2_grf_falsifier_tests.py + "
                      "ED_Update_Rule.ed_step_mobility"),
        "canonical_parameters": {
            "alpha": alpha, "gamma": fr.GAMMA, "noise_sigma": noise_amp,
            "mobility_exp": fr.MOBILITY_EXP,
            "steps": steps, "size": size, "dt": fr.DT,
            "p_min": fr.P_MIN, "p_max": fr.P_MAX,
            "boundary": fr.BOUNDARY,
        },
        "seeds": seeds,
        "snapshots_per_seed_max": (steps - 100) // 10,
        "xi_per_seed": per_seed_p,                 # primary channel: density p
        "xi_per_seed_smoothed": per_seed_E,        # audit channel: smoothed E
        "xi_mean": float(np.mean(all_xi_p)) if all_xi_p else None,
        "xi_std": float(np.std(all_xi_p)) if all_xi_p else None,
        "xi_mean_smoothed": float(np.mean(all_xi_E)) if all_xi_E else None,
        "xi_std_smoothed": float(np.std(all_xi_E)) if all_xi_E else None,
        "n_snapshots_total": len(all_xi_p),
        "wall_seconds": time.time() - t0,
        "errors": errors,
    }
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
