"""#3 re-check (the swing vote): does the ENSEMBLE-MEAN density obey the diffusion PDE,
with the ballistic worldlines as the disorder/entropy?

The CoarseGrain arc found a SINGLE realization's d_t rho ~ eikonal/ballistic (|grad rho|),
NOT diffusion (lap rho). #2's lesson: separate signal from disorder. For diffusion, the
signal is the SMOOTH MEAN density; the disorder is the per-realization ballistic noise.
In standard physics this is exactly how diffusion emerges -- individual walkers are
ballistic, the ensemble-MEAN density diffuses.

Test: average the density over many realizations -> <rho>(t); regress d_t<rho> on the
PDE library (diffusion lap rho, eikonal |grad rho|, PME). Does the MEAN diffuse?

  - <rho> regresses to DIFFUSION (high R^2 for lap rho, beating eikonal): #3 FLIPS --
    the mean density diffuses, the worldlines are the disorder. A window.
  - <rho> still eikonal/ballistic: #3 STAYS a wall -- even the mean spreads ballistically
    (straight worldlines, not random-walk), so the diffusion PDE isn't the coherent law.

Honest prior: ED's worldlines are STRAIGHT/ballistic (|v|~1), not random-walk steps. The
mean of straight walkers spreads BALLISTICALLY (|x| ~ t), which is eikonal/transport, not
diffusion (|x| ~ sqrt t). So the prior leans NO (mean stays eikonal). Could-say-no; test it.
"""
from __future__ import annotations
import os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coarsegrain_test import ensemble_run, coarse, regress_pde


def main():
    S, T = 121, 45
    seeds = list(range(2, 22))       # 20 realizations to average
    rho_max = 2.0
    print("=" * 80)
    print(f"#3 re-check — does the ENSEMBLE-MEAN density obey diffusion?  (S={S}, {len(seeds)} seeds)")
    print("=" * 80)

    for ic in ("gaussian", "step", "ring"):
        # single realization (the old result)
        single = ensemble_run(S, ic, T, seed=seeds[0])
        # ensemble mean over realizations
        stack = None
        nmin = 10**9
        runs = []
        for sd in seeds:
            fr = ensemble_run(S, ic, T, seed=sd)
            runs.append(fr)
            nmin = min(nmin, len(fr))
        mean = np.mean([r[:nmin] for r in runs], axis=0)

        cg_single = coarse(single[:nmin], 4)
        cg_mean = coarse(mean, 4)
        rs_single, n1 = regress_pde(cg_single, rho_max)
        rs_mean, n2 = regress_pde(cg_mean, rho_max)

        def best(rs):
            return max(("diffusion", "eikonal", "diff+eik", "PME(UDM)"), key=lambda k: rs[k][0])

        print(f"\n  IC = {ic}")
        print(f"    {'model':<12}{'single R^2':>12}{'MEAN R^2':>12}")
        for name in ("diffusion", "eikonal", "diff+eik", "PME(UDM)"):
            print(f"    {name:<12}{rs_single[name][0]:>12.3f}{rs_mean[name][0]:>12.3f}")
        print(f"    -> single best: {best(rs_single)} ({rs_single[best(rs_single)][0]:.3f}); "
              f"MEAN best: {best(rs_mean)} ({rs_mean[best(rs_mean)][0]:.3f})")
        # the decisive number: does the MEAN's diffusion R^2 beat its eikonal R^2?
        d, e = rs_mean["diffusion"][0], rs_mean["eikonal"][0]
        print(f"    MEAN: diffusion R^2 = {d:.3f}  vs  eikonal R^2 = {e:.3f}  -> "
              f"{'DIFFUSION wins (flip?)' if d > e + 0.05 else 'eikonal/ballistic wins (wall)'}")

    print("\n" + "-" * 80)
    print("READ: if the ENSEMBLE-MEAN regresses to diffusion (lap rho beating eikonal),")
    print("  #3 FLIPS -- the coherent/mean density diffuses, worldlines are the disorder.")
    print("  If the mean stays eikonal/ballistic, #3 STAYS a wall (straight worldlines, the")
    print("  mean spreads ballistically not diffusively).")
    print("-" * 80)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
