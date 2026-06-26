"""#5c re-check (AP's 'new CGing'): is the coarse field GAUSSIAN + sparse committal
spikes (entropy), or pervasively non-Gaussian?

#2 flipped because it had a SOURCE: a clean Coulomb signal to separate from the
disorder (the coherent/incoherent split). Gaussianity has no source -- it's a
homogeneous fluctuating field -- so the parallel question is:

  is the non-Gaussianity carried by a SPARSE, separable set of extreme cells
  (the committal spikes = entropy) sitting on a Gaussian field, or is it pervasive?

Test: measure skew/excess-kurtosis of the coarse fluctuation field, then sweep
REMOVING the top-k% by |fluctuation| (the candidate spikes) and recompute.
  - cumulants -> 0 after removing a SMALL k% : Gaussian field + sparse spikes
    (the spikes are the entropy) -> the window (flips like #2).
  - need to remove a LARGE fraction : pervasively non-Gaussian -> stays a wall
    (the non-Gaussianity is spatially correlated, not isolated spikes).

Honest prior: #5c found kurtosis GROWS under coarse-graining (anti-CLT), which
smells correlated/pervasive (filaments span cells), so this could come back NO.
Certified Sigma-substrate (same as grf_cumulant_test). Could-say-no.
"""
from __future__ import annotations
import os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coarsegrain_test import ensemble_run, coarse


def cumulants(x):
    x = np.asarray(x, float)
    s = x.std()
    if s < 1e-12:
        return 0.0, 0.0
    return float(np.mean(x ** 3) / s ** 3), float(np.mean(x ** 4) / s ** 4 - 3.0)


def main():
    S, T = 121, 45
    seeds = list(range(2, 12))
    LATE = 0.4
    blocks = [1, 4]                       # fine + a coarse scale
    ks = [0.0, 0.005, 0.01, 0.02, 0.05, 0.10, 0.20]   # fraction of extreme cells removed

    print("=" * 84)
    print(f"#5c re-check — Gaussian + sparse spikes, or pervasive?  (S={S}, {len(seeds)} seeds)")
    print("=" * 84)

    SEED_FRAC = 0.01     # SPARSE seeding: strong non-Gaussianity from ISOLATED filaments
    print(f"  (seed fraction = {SEED_FRAC}: sparse -> isolated filaments = the candidate 'spikes')")
    fields = []
    for sd in seeds:
        fr = ensemble_run(S, "uniform", T, n_seed_frac=SEED_FRAC, seed=sd)
        n = len(fr)
        fields.append(fr[int(n * (1 - LATE)):])

    for b in blocks:
        # pool per-frame-demeaned coarse fluctuations
        pooled = []
        for late in fields:
            cg = coarse(late, b)
            for f in cg:
                pooled.append((f - f.mean()).ravel())
        x = np.concatenate(pooled)
        ax = np.abs(x - x.mean())
        print(f"\n  R_cg = {b}   (pooled N = {x.size})")
        print(f"   {'remove top':>11} {'skew':>9} {'exkurt':>9}   reading")
        for k in ks:
            if k == 0:
                keep = x
            else:
                thr = np.quantile(ax, 1 - k)
                keep = x[ax <= thr]            # drop the top-k% most extreme cells
            sk, ek = cumulants(keep)
            near = abs(sk) < 0.1 and abs(ek) < 0.15
            print(f"   {k*100:>9.1f}% {sk:>9.3f} {ek:>9.3f}   {'~Gaussian' if near else 'non-Gaussian'}")

    print("\n" + "-" * 84)
    print("READ:")
    print("  - cumulants -> ~0 after removing a SMALL k% (<~2%): Gaussian field + sparse")
    print("    committal spikes (entropy) -> #5c FLIPS like #2 (a window).")
    print("  - need to remove a LARGE fraction: pervasively non-Gaussian (correlated, not")
    print("    isolated spikes) -> #5c STAYS a wall; the three walls are not all the same.")
    print("-" * 84)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
