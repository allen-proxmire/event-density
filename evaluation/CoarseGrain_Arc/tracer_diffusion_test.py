"""The tracer test (AP's route to diffusion): does a TRACER diffuse IN the ED medium,
even though the medium's worldlines are ballistic?

Einstein's Brownian setup: a test particle kicked by a fluctuating medium random-walks
(diffuses) even if the medium underneath is doing something else. The ED-faithful tracer
is a single worldline (one active front) propagating through a DISORDERED rho-landscape
(uniform-random IC) under the certified Sigma-rule. As it scatters off the rho-disorder,
does its direction DECORRELATE (-> diffusion) or persist (-> ballistic)?

Two diagnostics:
  - MSD(t) = <|x(t)-x(0)|^2> ~ t^alpha:  alpha=2 ballistic, alpha=1 diffusive, alpha<1
    sub-diffusive (trapped). A ballistic->diffusive crossover (alpha 2 then 1) is exactly
    how real Brownian motion arises (ballistic below the mean free time, diffusive above).
  - velocity autocorrelation C(tau)=<v(t).v(t+tau)>:  decays to 0 -> direction forgets
    itself -> diffusion route OPEN; stays positive -> persistent -> ballistic, no diffusion.

Honest prior: ED traps (committal), so I expect alpha<2 but likely sub-diffusive, VACF
staying positive (the filaments = persistent flow). But this is the right test and the one
route to diffusion we haven't closed -- a long-time crossover would be a real surprise.
Certified single-chain worldline; no new rules.
"""
from __future__ import annotations
import os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coarsegrain_test import single_chain_trajectory


def main():
    S, T = 201, 110
    seeds = list(range(1, 49))          # 48 tracers / disorder realizations
    margin = 6
    print("=" * 78)
    print(f"TRACER TEST — does a worldline diffuse in the disordered ED medium?  (S={S})")
    print("=" * 78)

    paths = []
    for sd in seeds:
        p = single_chain_trajectory(S, "uniform", T, seed=sd).astype(float)
        paths.append(p)
    lens = [len(p) - 1 for p in paths]
    print(f"\n  tracer path length (steps): min {min(lens)}, median {int(np.median(lens))}, max {max(lens)}")

    # MSD(t) over tracers alive & interior at t
    ts, ms = [], []
    for t in range(1, T + 1):
        d = []
        for p in paths:
            if len(p) > t:
                x, y = p[t]
                if margin <= x < S - margin and margin <= y < S - margin:
                    d.append((p[t, 0] - p[0, 0]) ** 2 + (p[t, 1] - p[0, 1]) ** 2)
        if len(d) >= 8:
            ts.append(t); ms.append(np.mean(d))
    ts, ms = np.array(ts), np.array(ms)
    print("\n  MSD(t) at t = " + " ".join(f"{int(t)}:{m:.0f}" for t, m in zip(ts, ms) if int(t) % 15 == 0))
    sel = (ts >= 5) & (ts <= ts.max() * 0.8) & (ms > 0)
    alpha, logc = np.polyfit(np.log(ts[sel]), np.log(ms[sel]), 1)
    label = ("ballistic (no diffusion)" if alpha > 1.7 else
             "DIFFUSIVE" if abs(alpha - 1) < 0.25 else
             "sub-diffusive (trapped)" if alpha < 0.8 else
             "intermediate")
    print(f"\n  MSD ~ t^alpha :  alpha = {alpha:.2f}   -> {label}")

    # velocity autocorrelation
    maxtau = 30
    vacf = np.zeros(maxtau); cnt = np.zeros(maxtau)
    for p in paths:
        v = np.diff(p, axis=0)
        n = len(v)
        for tau in range(maxtau):
            for t in range(n - tau):
                vacf[tau] += float(v[t] @ v[t + tau]); cnt[tau] += 1
    vacf /= np.maximum(cnt, 1)
    vn = vacf / (vacf[0] + 1e-12)
    print("\n  VACF(tau)/VACF(0): " + " ".join(f"{vn[k]:.2f}" for k in range(0, maxtau, 3)))
    tail = np.mean(vn[15:25])
    print(f"  -> VACF tail (tau 15-25) = {tail:.2f}   "
          f"{'decays to ~0: direction DECORRELATES (diffusion route open)' if tail < 0.2 else 'stays positive: PERSISTENT (ballistic, no decorrelation)'}")

    print("\n" + "-" * 78)
    print("READ: alpha~1 AND VACF->0  => the tracer DIFFUSES in the medium (diffusion a floor")
    print("  up, via Brownian tracer) -- a real route. alpha~2 / VACF persistent => ballistic;")
    print("  alpha<1 => trapped. Either non-diffusive answer confirms ED won't diffuse even via")
    print("  a tracer -- the same committal wall, now closed from the Brownian side.")
    print("-" * 78)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
