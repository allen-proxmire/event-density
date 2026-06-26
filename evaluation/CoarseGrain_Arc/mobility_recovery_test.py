"""Does the substrate reproduce the UDM degenerate mobility M(rho) = M0 (rho_max - rho)^beta?

The tracer test showed a worldline DIFFUSES in a dilute disordered medium (alpha~1.18,
velocity decorrelates). ShadowEmergence showed it TRAPS at high density. The UDM mobility
M(rho) = M0 (rho_max - rho)^beta is exactly a diffusivity that dies as density -> capacity.

Test: run tracers (single worldlines) through media at a RANGE of base densities rho0,
measure each regime's effective diffusivity D_eff (MSD slope) and exponent alpha. If
D_eff(rho) DECREASES toward 0 as rho0 -> rho_max, and fits (rho_max - rho0)^beta, the
substrate reproduces the UDM mobility -- the degenerate-mobility PDE read straight off the
worldlines (AP's path was ED philosophy -> UDM -> physics; this comes back the other way).

Reports D_eff(rho0), alpha(rho0), front survival, and the fitted beta. Certified Sigma-rule.
"""
from __future__ import annotations
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from coarsegrain_test import grid, COEFFS  # noqa: E402
BITS = os.path.join(os.path.dirname(HERE), "Bits")
sys.path.insert(0, BITS)
from simulator import NodeState, StateVector, assign_stratum_ids, step  # noqa: E402


def tracer_path(S, rho0, T, seed):
    rng = np.random.default_rng(seed)
    sv = StateVector()
    for y in range(S):
        for x in range(S):
            sv[y * S + x] = NodeState(rho=float(np.clip(rho0 + rng.uniform(-0.1, 0.1), 0.0, 0.99)),
                                      orientation=rng.normal(size=2))
    g = grid(S)
    c = (S // 2) * S + (S // 2)
    sv[c].active = True
    st = assign_stratum_ids(sv, g)
    path = [(S // 2, S // 2)]
    for _ in range(T):
        if step(sv, g, COEFFS, strata=st) == 0:
            break
        act = [n for n in sv if sv[n].active]
        if not act:
            break
        n = act[0]
        path.append((n % S, n // S))
    return np.array(path, float)


def msd_alpha_D(paths, S, T, margin=5):
    ts, ms = [], []
    for t in range(1, T + 1):
        d = []
        for p in paths:
            if len(p) > t:
                x, y = p[t]
                if margin <= x < S - margin and margin <= y < S - margin:
                    d.append((p[t, 0] - p[0, 0]) ** 2 + (p[t, 1] - p[0, 1]) ** 2)
        if len(d) >= 6:
            ts.append(t); ms.append(np.mean(d))
    ts, ms = np.array(ts), np.array(ms)
    if len(ts) < 5:
        return 0.0, 0.0
    sel = (ts >= 4) & (ts <= ts.max() * 0.8) & (ms > 0)
    if sel.sum() < 4:
        return 0.0, float(ms[-1] / (4 * ts[-1]))
    alpha, _ = np.polyfit(np.log(ts[sel]), np.log(ms[sel]), 1)
    # diffusivity proxy: MSD/(4t) at the largest reliable t (2D)
    D = float(ms[sel][-1] / (4 * ts[sel][-1]))
    return float(alpha), D


def main():
    S, T = 141, 80
    seeds = list(range(1, 21))
    rho_levels = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80]
    rho_max = 1.0
    print("=" * 78)
    print(f"MOBILITY RECOVERY — does D_eff(rho) trace the UDM (rho_max-rho)^beta?  (S={S})")
    print("=" * 78)
    print(f"\n  {'rho0':>5} {'survival':>9} {'alpha':>7} {'D_eff':>9}   regime")
    rec = []
    for rho0 in rho_levels:
        paths = [tracer_path(S, rho0, T, sd) for sd in seeds]
        lens = [len(p) - 1 for p in paths]
        surv = float(np.median(lens)) / T
        alpha, D = msd_alpha_D(paths, S, T)
        reg = ("DIFFUSIVE" if abs(alpha - 1) < 0.3 else
               "ballistic" if alpha > 1.5 else
               "sub-diff/trapped" if 0 < alpha < 0.7 else "weak/frozen")
        print(f"  {rho0:>5.2f} {surv:>8.2f} {alpha:>7.2f} {D:>9.3f}   {reg}")
        rec.append((rho0, D, alpha, surv))

    # fit D_eff(rho0) = D0 (rho_max - rho0)^beta  (use levels with real motion)
    arr = np.array([(r, D) for r, D, a, s in rec if D > 1e-3 and (rho_max - r) > 0.05])
    print("\n" + "-" * 78)
    if len(arr) >= 3:
        x = np.log(rho_max - arr[:, 0])
        y = np.log(arr[:, 1])
        beta, logD0 = np.polyfit(x, y, 1)
        pred = np.exp(logD0) * (rho_max - arr[:, 0]) ** beta
        r2 = 1 - np.sum((arr[:, 1] - pred) ** 2) / (np.sum((arr[:, 1] - arr[:, 1].mean()) ** 2) + 1e-12)
        print(f"  FIT  D_eff(rho) = D0 (rho_max - rho)^beta   (rho_max={rho_max})")
        print(f"       beta = {beta:.2f}   R^2 = {r2:.3f}   "
              f"(UDM canonical beta=2; soft-matter beta~1.72)")
        print(f"  -> {'DEGENERATE mobility recovered (D_eff dies toward capacity) = the UDM form' if beta > 0.5 and r2 > 0.6 else 'no clean degenerate power law (see table)'}")
    else:
        print("  too few mobile density levels to fit (front freezes early at high rho)")
    print("\n  READ: D_eff decreasing toward 0 as rho0 -> rho_max, fitting (rho_max-rho)^beta,")
    print("  IS the UDM degenerate mobility read off the substrate. A diffusive->trapped")
    print("  crossover in alpha is the dilute-diffusion / dense-caging picture.")
    print("-" * 78)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
