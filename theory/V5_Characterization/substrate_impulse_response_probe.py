"""Does the certified substrate's OWN natural response to a localized
perturbation actually decay exponentially with distance -- the direct,
decisive test of the V5_Envelope_Shape_From_P11_Scoping.md hypothesis --
rather than the murkier, indirect question of whether P11 commitment events
form a "clean rate" (which turns out not to map cleanly onto the certified
code: every single step involves a commitment, so there is no meaningful
sense of "sometimes it commits, sometimes it doesn't" to extract a rate
from directly).

METHOD (paired, single-variable, same certified base dynamics -- no
self-loop, no field bonus, no dwell mechanism at all; this tests the BASE
substrate's own impulse response). Two runs from an IDENTICAL initial
condition, differing by exactly one tiny perturbation (a small rho bump) at
a single locus. Let both evolve under the certified, unmodified update rule
for many steps. Measure the DIFFERENCE between the two runs' resulting rho
fields as a function of distance from the perturbed locus. If the substrate's
natural response is a screened/gapped process (as the P11-envelope-shape
hypothesis predicts), this difference should decay exponentially with
distance from the perturbation. If it decays as a power law, stays flat, or
shows no clean decay at all, the hypothesis does not survive this direct
check.
"""
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,  # noqa: E402
                       assign_stratum_ids, step)

CHAIN_LEN = 300
EDGE_BW = 0.5
RHO_STAR = 0.5
JITTER_SD = 1e-3
PERTURB_POS = 150
PERTURB_AMOUNT = 0.3
N_FRONTS = 40          # many independent active fronts spread across the chain,
                       # so the perturbation's influence can be picked up by
                       # whichever ones pass near it -- not just one lone front
MAX_STEPS = 250
COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=RHO_STAR, increment=1.0,
                     extinction_threshold=None)


def build_chain(n):
    g = ParticipationGraph()
    for i in range(n - 1):
        g.add_edge(i, i + 1, bandwidth=EDGE_BW)
    return g


def make_state(n, seed, perturb=False):
    rng = np.random.default_rng(seed)
    sv = StateVector()
    for i in range(n):
        rho = RHO_STAR + rng.normal(0, JITTER_SD)
        if perturb and i == PERTURB_POS:
            rho += PERTURB_AMOUNT
        sv[i] = NodeState(rho=float(max(0.0, rho)))
    # Spread many independent fronts evenly, so the perturbation's influence
    # can be sampled at every distance simultaneously in one run.
    starts = np.linspace(5, n - 6, N_FRONTS).astype(int)
    for s in starts:
        sv[int(s)].active = True
    return sv


def run(seed, perturb):
    g = build_chain(CHAIN_LEN)
    sv = make_state(CHAIN_LEN, seed, perturb=perturb)
    strata = assign_stratum_ids(sv, g)
    for t in range(1, MAX_STEPS + 1):
        n = step(sv, g, COEFFS, strata=strata, t=t)
        if n == 0:
            break
    return np.array([sv[i].rho for i in range(CHAIN_LEN)])


def main():
    print("=" * 92)
    print("SUBSTRATE IMPULSE-RESPONSE PROBE -- does a localized rho perturbation's")
    print("influence on the resulting field decay exponentially with distance?")
    print(f"chain={CHAIN_LEN}, perturbation@{PERTURB_POS} (amount={PERTURB_AMOUNT}), "
          f"{N_FRONTS} independent fronts, {MAX_STEPS} steps")
    print("=" * 92)

    seeds = list(range(15))
    diffs = []
    for s in seeds:
        rho_base = run(s, perturb=False)
        rho_pert = run(s, perturb=True)
        diffs.append(np.abs(rho_pert - rho_base))
    mean_diff = np.mean(diffs, axis=0)

    bins = list(range(-100, 101, 10))
    print(f"\n{'dist_to_perturb':>16}{'mean_abs_diff':>16}")
    profile = []
    for b in bins:
        lo, hi = PERTURB_POS + b, PERTURB_POS + b + 10
        lo, hi = max(0, lo), min(CHAIN_LEN, hi)
        if lo < hi:
            val = mean_diff[lo:hi].mean()
            profile.append((b + 5, val))
            print(f"{b:>16}{val:>16.6f}")

    # Fit log(diff) vs distance -- linear fit slope = -1/decay_length if
    # exponential; check the fit quality (R^2) as the real discriminant.
    dist = np.array([abs(d) for d, v in profile if v > 1e-8])
    logval = np.array([np.log(v) for d, v in profile if v > 1e-8])
    if len(dist) >= 3:
        A = np.vstack([dist, np.ones_like(dist)]).T
        slope, intercept = np.linalg.lstsq(A, logval, rcond=None)[0]
        pred = A @ [slope, intercept]
        ss_res = np.sum((logval - pred) ** 2)
        ss_tot = np.sum((logval - logval.mean()) ** 2)
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else float("nan")
        print(f"\nLinear fit of log(|diff|) vs distance: slope={slope:.4f} "
              f"(decay length = {-1/slope if slope != 0 else float('inf'):.2f} hops), R^2={r2:.4f}")
        print("High R^2 (>0.9ish) for THIS linear-in-log fit would support exponential decay.")
        print("Also fit log(diff) vs log(distance) to check the power-law alternative directly.")
        logdist = np.array([np.log(d) for d in dist if d > 0])
        logval2 = np.array([v for d, v in zip(dist, logval) if d > 0])
        if len(logdist) >= 3:
            A2 = np.vstack([logdist, np.ones_like(logdist)]).T
            slope2, intercept2 = np.linalg.lstsq(A2, logval2, rcond=None)[0]
            pred2 = A2 @ [slope2, intercept2]
            ss_res2 = np.sum((logval2 - pred2) ** 2)
            ss_tot2 = np.sum((logval2 - logval2.mean()) ** 2)
            r2_power = 1 - ss_res2 / ss_tot2 if ss_tot2 > 0 else float("nan")
            print(f"Power-law fit (log-log): exponent={slope2:.4f}, R^2={r2_power:.4f}")
            print(f"\nCOMPARISON: exponential-fit R^2={r2:.4f} vs power-law-fit R^2={r2_power:.4f}")
    else:
        print("\nNot enough non-trivial distance bins to fit -- perturbation influence "
              "may not be detectable at all with this setup.")

    print("\n" + "=" * 92)
    print("READINGS:")
    print("  Exponential fit clearly better (higher R^2) than power-law fit -- supports")
    print("  the P11-as-gap hypothesis directly, on the REAL substrate, not an analogy.")
    print("  Power-law fit better, or neither fits well -- the hypothesis does not survive")
    print("  this direct check; the envelope-shape argument needs rethinking, same honesty")
    print("  standard as every other check tonight.")
    print("=" * 92)


if __name__ == "__main__":
    main()
