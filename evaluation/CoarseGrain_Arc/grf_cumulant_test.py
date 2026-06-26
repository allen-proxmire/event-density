"""ED #5c — GRF Gaussianity cumulant test on the CERTIFIED dynamical substrate.

The S1-motif arc (Paper_EDSC_Motif / SC-4.7) rests on a GRF *regime hypothesis*:
the coarse-grained participation field is Gaussian. It is currently ASSUMED, not
measured. This is the cheap, could-say-no test the research map (#5c) calls for.

Target choice (honest): the literal r* GRF-linearization pipeline is not on disk
(its ED_Update_Rule / r2_grf_falsifier modules were never committed). But the
MEANINGFUL test is whether ED's *dynamical* field comes out Gaussian — and the
certified Sigma-rule substrate that the CoarseGrain arc used IS on disk. So we
measure the cumulants of the coarse-grained event-density field produced by that
certified simulator, swept across the coarse-graining scale R_cg.

Diagnostics (all 0 for a Gaussian field):
  - skewness            (3rd standardized moment)
  - excess kurtosis     (4th standardized moment - 3)  = normalized connected 4-pt at coincidence
  - Wick residual       does <f^2(x) f^2(x+r)> factor as <f^2>^2 + 2<f(x)f(x+r)>^2 ?

Three outcomes, all publishable:
  cumulants -> 0 as R_cg grows : Gaussian in the hydrodynamic window (assumed -> MEASURED)
  cumulants persist            : Gaussianity FALSE (regime hypothesis refuted)
  Gaussian only in a band      : maps the validity window

Prior (from the CoarseGrain/Shadow arc: ED dynamics are committal/trapping, ballistic
worldline deposits, sub-diffusive -- "locks configs, doesn't decorrelate"): expect
persistent non-Gaussianity or at best a narrow band, NOT clean Gaussianity. Could-say-no.
"""
from __future__ import annotations
import os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coarsegrain_test import ensemble_run, coarse  # certified-sim machinery


def cumulants_pooled(vals):
    """skewness, excess kurtosis on a pooled 1D sample of field fluctuations."""
    x = np.asarray(vals, float)
    x = x - x.mean()
    s = x.std()
    if s < 1e-12:
        return 0.0, 0.0
    return float(np.mean(x ** 3) / s ** 3), float(np.mean(x ** 4) / s ** 4 - 3.0)


def wick_residual(field2d, r=1):
    """relative residual of <f^2(x) f^2(x+r)> vs the Gaussian Wick value; 0 if Gaussian."""
    f = field2d - field2d.mean()
    a, b = f[:, :-r], f[:, r:]
    c2 = np.mean(a * b)                 # <f(x) f(x+r)>
    var = np.mean(f * f)               # <f^2>
    lhs = np.mean((a * a) * (b * b))   # <f^2(x) f^2(x+r)>
    rhs = var * var + 2.0 * c2 * c2    # Gaussian Wick factorization
    return float((lhs - rhs) / (rhs + 1e-12))


def main():
    S, T = 121, 45
    seeds = list(range(2, 12))          # 10 dynamical realizations
    blocks = [1, 2, 3, 4, 6, 8, 11]     # R_cg sweep (block-average size, lattice units)
    ic = "uniform"                      # generic homogeneous start; test the dynamical field
    LATE_FRAC = 0.4                     # use the last 40% of frames (developed field)

    print("=" * 78)
    print(f"ED #5c — Gaussianity cumulant test, certified dynamical substrate (S={S}, T={T})")
    print(f"  {len(seeds)} seeds, IC={ic}, late {int(LATE_FRAC*100)}% of frames, "
          f"fluctuation field per-frame demeaned")
    print("=" * 78)

    # gather late-time fields once per seed
    fields = []  # list of (n_late, S, S)
    for sd in seeds:
        frames = ensemble_run(S, ic, T, seed=sd)
        n = len(frames)
        late = frames[int(n * (1 - LATE_FRAC)):]
        fields.append(late)
    print(f"  collected fields: {[f.shape[0] for f in fields]} late frames/seed\n")

    print(f"  {'R_cg':>5} {'cells':>7} {'skew':>10} {'exkurt':>10} {'Wick_res':>10}   reading")
    rows = []
    for b in blocks:
        pooled = []          # demeaned coarse-field values, pooled across seeds+late-frames
        wicks = []
        ncells = (S // b) ** 2
        for late in fields:
            cg = coarse(late, b)               # (n_late, S/b, S/b)
            for fr in cg:
                ff = fr - fr.mean()
                pooled.append(ff.ravel())
                if fr.shape[1] > 1:
                    wicks.append(wick_residual(fr, r=1))
        pooled = np.concatenate(pooled)
        skew, exk = cumulants_pooled(pooled)
        wick = float(np.mean(wicks)) if wicks else float("nan")
        near0 = (abs(skew) < 0.1 and abs(exk) < 0.1)
        rows.append((b, ncells, skew, exk, wick))
        print(f"  {b:>5} {ncells:>7} {skew:>10.3f} {exk:>10.3f} {wick:>10.3f}   "
              f"{'~Gaussian' if near0 else 'NON-Gaussian'}")

    # verdict
    print("\n" + "-" * 78)
    sk = np.array([abs(r[2]) for r in rows])
    ek = np.array([abs(r[3]) for r in rows])
    trend_sk = sk[-1] - sk[0]
    trend_ek = ek[-1] - ek[0]
    gaussian_large = (sk[-1] < 0.15 and ek[-1] < 0.3)
    gaussian_any = np.any((sk < 0.15) & (ek < 0.3))
    print("VERDICT:")
    print(f"  |skew|:    fine={sk[0]:.2f} -> coarse={sk[-1]:.2f}  (trend {trend_sk:+.2f})")
    print(f"  |exkurt|:  fine={ek[0]:.2f} -> coarse={ek[-1]:.2f}  (trend {trend_ek:+.2f})")
    if gaussian_large and trend_ek < -0.1:
        print("  -> GAUSSIANIZES under coarse-graining (CLT route): GRF regime hypothesis"
              " MEASURED-supported in the hydrodynamic window.")
    elif gaussian_any and not gaussian_large:
        print("  -> Gaussian only in a BAND: regime hypothesis holds in a limited window;"
              " maps the validity range.")
    else:
        print("  -> NON-Gaussian and persistent: GRF regime hypothesis NOT supported"
              " (consistent with the committal/trapping CoarseGrain finding). Honest no.")
    print("-" * 78)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
