"""ED #5c firming — pressure-test the "approximately Gaussian" surprise.

The base test (grf_cumulant_test.py) found the coarse field only weakly non-Gaussian.
Flag: uniform-IC field is sparse-deposit-on-smooth-background, so the static background
may dilute the committal worldline structure (the trapping the prior was about). Two
sharper probes here:

  (1) sweep the DEPOSIT DENSITY (seed fraction): sparse -> isolated filaments (should be
      most non-Gaussian if trapping structure is real); dense -> overlapping deposits (CLT).
  (2) the DEPOSITED-INCREMENT field (late - initial): isolates what the committal dynamics
      added, removing the static background entirely. If the deposits are filamentary/
      heavy-tailed, the increment is strongly non-Gaussian even where the total looks mild.

Could-say-no: if non-Gaussianity stays weak even in the increment and at sparse seeding,
the "approximately Gaussian" surprise is robust. If it spikes, the base test was diluted
and ED's committal structure is genuinely non-Gaussian (prior vindicated).
"""
from __future__ import annotations
import os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coarsegrain_test import ensemble_run, coarse


def cumulants(stack):
    """skew, excess kurtosis on per-frame-demeaned values pooled over a (n,S,S) stack."""
    vals = []
    for fr in stack:
        ff = fr - fr.mean()
        vals.append(ff.ravel())
    x = np.concatenate(vals)
    s = x.std()
    if s < 1e-12:
        return 0.0, 0.0
    return float(np.mean(x ** 3) / s ** 3), float(np.mean(x ** 4) / s ** 4 - 3.0)


def main():
    S, T = 121, 45
    seeds = list(range(2, 7))                 # 5 realizations
    fracs = [0.01, 0.04, 0.10, 0.25]          # deposit-density sweep
    LATE = 0.4
    Rs = [1, 4]                                # fine + coarse

    print("=" * 84)
    print(f"#5c firming — deposit-density sweep + increment field (S={S}, T={T}, {len(seeds)} seeds)")
    print("  TOTAL = full late field ; INCREMENT = (late - initial), isolates committal deposits")
    print("  (skew, excess-kurtosis; both 0 for Gaussian)")
    print("=" * 84)
    hdr = f"  {'seedfrac':>8}"
    for R in Rs:
        hdr += f" | tot R{R}: skew  exk"
    for R in Rs:
        hdr += f" | inc R{R}: skew  exk"
    print(hdr)

    for sf in fracs:
        tot = {R: [] for R in Rs}
        inc = {R: [] for R in Rs}
        for sd in seeds:
            frames = ensemble_run(S, "uniform", T, n_seed_frac=sf, seed=sd)
            n = len(frames)
            late = frames[int(n * (1 - LATE)):]
            increment = late - frames[0]          # what the dynamics deposited
            for R in Rs:
                tot[R].append(coarse(late, R))
                inc[R].append(coarse(increment, R))
        line = f"  {sf:>8.2f}"
        for R in Rs:
            sk, ek = cumulants(np.concatenate(tot[R]))
            line += f" | {sk:>6.2f} {ek:>6.2f}"
        for R in Rs:
            sk, ek = cumulants(np.concatenate(inc[R]))
            line += f" | {sk:>6.2f} {ek:>6.2f}"
        print(line)

    print("\n" + "-" * 84)
    print("READ:")
    print("  - TOTAL columns staying near 0 across seedfrac = base 'approximately Gaussian' robust.")
    print("  - INCREMENT spiking (esp. high kurtosis at sparse seedfrac) = committal deposit")
    print("    structure IS non-Gaussian (heavy-tailed/zero-inflated); the total is background-diluted.")
    print("  - Both staying mild = the surprise is real; ED's coarse field is genuinely near-Gaussian.")
    print("-" * 84)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
