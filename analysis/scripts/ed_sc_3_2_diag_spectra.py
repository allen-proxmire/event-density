"""Diagnostic: measure spectral triad (sigma0, sigma1, sigma2) and xi
(GR-SC 1.7 half-decay) on snapshots from the canonical R2 SPDE.

READ-ONLY with respect to r_star_montecarlo: imports the module but
never assigns to any module global. Uses mc.imex_step only, does not
call process_snapshot or motif_filter_check, so no filter parameter
is exercised.
"""
import json, os, sys, time
import numpy as np
from numpy.fft import fft2, ifft2, fftshift
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r_star_montecarlo as mc


def spectral_triad(d, dx=1.0):
    gx = (np.roll(d, -1, 0) - np.roll(d, 1, 0)) / (2 * dx)
    gy = (np.roll(d, -1, 1) - np.roll(d, 1, 1)) / (2 * dx)
    lap = (np.roll(d, -1, 0) + np.roll(d, 1, 0)
           + np.roll(d, -1, 1) + np.roll(d, 1, 1) - 4 * d) / (dx * dx)
    return (float(np.std(d)),
            float(np.sqrt(np.mean(gx * gx + gy * gy))),
            float(np.sqrt(np.mean(lap * lap))))


def xi_halfdecay(d, dx=1.0):
    N = d.shape[0]
    f = d - np.mean(d)
    F = fft2(f)
    C = fftshift(np.real(ifft2(F * np.conj(F)))) / (N * N)
    c0 = C[N // 2, N // 2]
    if c0 <= 0:
        return float('nan')
    y, x = np.indices(C.shape)
    r = np.sqrt((x - N // 2) ** 2 + (y - N // 2) ** 2).astype(int)
    prof = np.array([C[r == k].mean() if np.any(r == k) else 0.0
                     for k in range(N // 2)]) / c0
    for k in range(1, N // 2):
        if prof[k] <= 0.5:
            if prof[k - 1] == prof[k]:
                return float(k) * dx
            return float(k - 1 + (prof[k - 1] - 0.5) / (prof[k - 1] - prof[k])) * dx
    return float(N // 2) * dx


def main():
    seeds = [77, 123, 456, 789, 1011, 1213, 1415, 1617, 1819, 2021]
    triads = []
    xis = []
    t0 = time.time()
    for s in seeds:
        rng = np.random.default_rng(s)
        delta = 0.3 + 0.4 * rng.random((mc.L, mc.L))
        lap_sym = mc.fft_laplacian_symbol(mc.L, mc.DX)
        for step in range(mc.N_STEPS):
            delta = mc.imex_step(delta, mc.DT, lap_sym, rng)
            if step >= mc.BURN_IN and (step - mc.BURN_IN) % mc.SNAPSHOT_EVERY == 0:
                s0, s1, s2 = spectral_triad(delta, mc.DX)
                triads.append((s0, s1, s2))
                xis.append(xi_halfdecay(delta, mc.DX))
        print(f"  seed={s} done (cum snaps={len(triads)})", file=sys.stderr)
    tri = np.array(triads)
    out = {
        "seeds": seeds,
        "n_snapshots": len(triads),
        "sigma0_mean": float(tri[:, 0].mean()),
        "sigma1_mean": float(tri[:, 1].mean()),
        "sigma2_mean": float(tri[:, 2].mean()),
        "sigma0_std": float(tri[:, 0].std()),
        "sigma1_std": float(tri[:, 1].std()),
        "sigma2_std": float(tri[:, 2].std()),
        "xi_mean": float(np.nanmean(xis)),
        "xi_std": float(np.nanstd(xis)),
        "isoperimetric_s0s2_over_s1sq":
            float(tri[:, 0].mean() * tri[:, 2].mean() / (tri[:, 1].mean() ** 2)),
        "wall_seconds": time.time() - t0,
    }
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
