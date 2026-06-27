"""Layer-2 test #2 — DIFFUSION: does ED-transport + the substrate's intrinsic scattering
coarse-grain (a second time) to real diffusion, with consistent coefficients?

The two-layer program: ED's direct CG = layer 1 = transport (ballistic worldlines).
Diffusion is layer 2 = the second CG, which needs decorrelation. The ingredient is NOT
added by hand: ED worldlines already scatter off the substrate's own rho-disorder
(tracer test). This measures whether that intrinsic scattering produces NORMAL diffusion,
checked by COEFFICIENTS, not form:

  - Green-Kubo D_GK = (1/(2d)) * sum_tau <v(0).v(tau)>   (parameter-free, from the VACF)
  - MSD D_MSD = MSD/(2 d t) at long t                    (from the spreading)
  If the worldlines truly diffuse, D_GK == D_MSD. Disagreement => not diffusion.

  - asymptotic exponent alpha (MSD ~ t^alpha): ->1 diffusion, >1 super, <1 trapped.
  - displacement distribution Gaussian? (diffusion's profile; touches layer-2 #1 too.)

Outcomes: clean diffusion (alpha->1, D_GK~=D_MSD, Gaussian) = layer-2 recovered;
super-diffusion (alpha>1, VACF integral diverges) = an edge; trapped (alpha<1) = caging.
Certified single-chain worldlines; the scattering is intrinsic (uniform rho-disorder), no
tuned knob. Could-say-no by coefficient mismatch.
"""
from __future__ import annotations
import os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coarsegrain_test import single_chain_trajectory

D_DIM = 2


def main():
    S, T = 251, 150
    seeds = list(range(1, 61))
    margin = 6
    print("=" * 80)
    print(f"DIFFUSION layer-2 test — does ED's intrinsic scattering give NORMAL diffusion?")
    print(f"  (S={S}, T={T}, {len(seeds)} worldlines in uniform rho-disorder)")
    print("=" * 80)

    paths = [single_chain_trajectory(S, "uniform", T, seed=sd).astype(float) for sd in seeds]
    lens = [len(p) - 1 for p in paths]
    print(f"\n  path length: min {min(lens)}, median {int(np.median(lens))}, max {max(lens)}")

    # MSD(t) over interior tracers
    ts, ms, ns = [], [], []
    for t in range(1, T + 1):
        d = [(p[t, 0] - p[0, 0]) ** 2 + (p[t, 1] - p[0, 1]) ** 2
             for p in paths if len(p) > t and margin <= p[t, 0] < S - margin and margin <= p[t, 1] < S - margin]
        if len(d) >= 8:
            ts.append(t); ms.append(np.mean(d)); ns.append(len(d))
    ts, ms = np.array(ts), np.array(ms)

    def alpha(lo, hi):
        m = (ts >= lo) & (ts <= hi) & (ms > 0)
        if m.sum() < 4:
            return float("nan")
        a, _ = np.polyfit(np.log(ts[m]), np.log(ms[m]), 1)
        return float(a)

    a_early = alpha(4, 20)
    a_late = alpha(40, ts.max() * 0.9)
    print(f"\n  MSD exponent alpha:  early (t 4-20) = {a_early:.2f}   late (t 40-{int(ts.max()*0.9)}) = {a_late:.2f}")
    print("    MSD(t): " + " ".join(f"{int(t)}:{m:.0f}" for t, m in zip(ts, ms) if int(t) % 25 == 0))

    # D from MSD slope at long time:  MSD = 2 d D t  ->  D = MSD/(2 d t)
    late = ts >= ts.max() * 0.5
    D_msd = float(np.mean(ms[late] / (2 * D_DIM * ts[late])))

    # VACF and Green-Kubo D_GK = (1/(2d)) [C(0) + 2 sum_{tau>=1} C(tau)]
    maxtau = 40
    vacf = np.zeros(maxtau); cnt = np.zeros(maxtau)
    for p in paths:
        v = np.diff(p, axis=0)
        n = len(v)
        for tau in range(maxtau):
            for t in range(n - tau):
                vacf[tau] += float(v[t] @ v[t + tau]); cnt[tau] += 1
    vacf /= np.maximum(cnt, 1)
    D_gk = (vacf[0] + 2 * vacf[1:].sum()) / (2 * D_DIM)
    vn = vacf / (vacf[0] + 1e-12)
    print(f"\n  VACF/VACF(0): " + " ".join(f"{vn[k]:.2f}" for k in range(0, maxtau, 4)))
    tail = float(np.mean(np.abs(vn[20:35])))
    print(f"    VACF tail |tau 20-35| = {tail:.3f}  ({'decays -> finite integral (normal-diffusion compatible)' if tail < 0.1 else 'persistent tail -> integral suspect (super-diffusion)'})")

    print(f"\n  D_MSD (spread)    = {D_msd:.3f}")
    print(f"  D_GK  (Green-Kubo) = {D_gk:.3f}")
    ratio = D_msd / D_gk if abs(D_gk) > 1e-9 else float("inf")
    print(f"  D_MSD / D_GK       = {ratio:.2f}   (==1 if the two coefficients agree)")

    # displacement Gaussianity at a late time
    tg = int(ts.max() * 0.8)
    dx = np.array([p[tg, 0] - p[0, 0] for p in paths if len(p) > tg and margin <= p[tg, 0] < S - margin]
                  + [p[tg, 1] - p[0, 1] for p in paths if len(p) > tg and margin <= p[tg, 1] < S - margin])
    dx = dx - dx.mean(); sd = dx.std()
    sk = float(np.mean(dx ** 3) / sd ** 3) if sd > 0 else 0.0
    ek = float(np.mean(dx ** 4) / sd ** 4 - 3) if sd > 0 else 0.0
    print(f"\n  displacement distribution at t={tg}: skew {sk:.2f}, excess-kurt {ek:.2f}  "
          f"({'~Gaussian (diffusion profile)' if abs(sk) < 0.2 and abs(ek) < 0.3 else 'non-Gaussian'})")

    # verdict
    print("\n" + "-" * 80)
    diff = abs(a_late - 1) < 0.2 and 0.6 < ratio < 1.6
    if diff:
        v = "CLEAN DIFFUSION — layer-2 recovered (alpha~1, D_GK~=D_MSD)"
    elif a_late > 1.2:
        v = "SUPER-DIFFUSION — an edge (persistence won't decorrelate to normal diffusion)"
    elif a_late < 0.8:
        v = "SUB-DIFFUSIVE / TRAPPED — an edge (caging)"
    else:
        v = "INTERMEDIATE / coefficient mismatch — not clean diffusion"
    print(f"  VERDICT: {v}")
    print("-" * 80)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
