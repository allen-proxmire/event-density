"""RC channel test: does the substrate relax a density perturbation EXPONENTIALLY toward
equilibrium rho* (the penalty channel = RC/Debye decay)?

UDM-PDE penalty channel: d_t delta = -D P0 delta, delta = rho - rho*, exponential decay to
rho* from EITHER side (symmetric). The certified rule has a coherence term that FAVORS
rho near rho* (sigma.py: coh = -(rho_v - rho*)^2), so it should pull toward rho*. But the
substrate only ADDS rho (deposits) -- it has no rho-removal -- so the honest prior is it
relaxes UP toward rho* from below and CANNOT relax DOWN from above (asymmetric = not RC).

Test: dense fronts on a uniform field initialized above and below rho*=0.5, with and
without the extinction switch; track <rho>(t) and ask whether it decays to rho*
exponentially and SYMMETRICALLY (RC) or only upward (generative-only, RC needs dissipation).
Certified Sigma-rule.
"""
from __future__ import annotations
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from coarsegrain_test import grid  # noqa: E402
BITS = os.path.join(os.path.dirname(HERE), "Bits")
sys.path.insert(0, BITS)
from simulator import NodeState, StateVector, assign_stratum_ids, step  # noqa: E402
from simulator.sigma import SigmaCoeffs  # noqa: E402

RHO_STAR = 0.5


def run_field(S, rho0, T, seed, ext, seed_frac=0.25):
    rng = np.random.default_rng(seed)
    coeffs = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=RHO_STAR, extinction_threshold=ext)
    sv = StateVector()
    for y in range(S):
        for x in range(S):
            sv[y * S + x] = NodeState(rho=float(np.clip(rho0 + rng.uniform(-0.05, 0.05), 0, 0.99)),
                                      orientation=rng.normal(size=2))
    g = grid(S)
    ids = [y * S + x for y in range(S) for x in range(S)]
    for nid in rng.choice(ids, size=int(len(ids) * seed_frac), replace=False):
        sv[nid].active = True
    st = assign_stratum_ids(sv, g)
    alln = list(sv)
    mt = [float(np.mean([sv[n].rho for n in alln]))]
    for _ in range(T):
        if step(sv, g, coeffs, strata=st) == 0:
            break
        mt.append(float(np.mean([sv[n].rho for n in alln])))
    return np.array(mt)


def relax_rate(mt):
    """fit delta(t) = <rho>-rho* ~ delta0 e^{-k t}; return k (>0 = decays to rho*)."""
    d = mt - RHO_STAR
    if np.any(np.sign(d) != np.sign(d[0])) or np.abs(d[0]) < 1e-3:
        return float("nan")
    t = np.arange(len(d))
    k, _ = np.polyfit(t, np.log(np.abs(d) + 1e-9), 1)
    return -float(k)


def main():
    S, T = 81, 55
    print("=" * 78)
    print(f"RC RELAXATION TEST — does <rho> decay exponentially & symmetrically to rho*={RHO_STAR}?")
    print("=" * 78)
    for label, ext in (("no-extinction (bare generative rule)", None),
                       ("extinction ON (dissipative switch)", -1.2)):
        print(f"\n  {label}")
        print(f"    {'rho0':>5} {'<rho>: start->end':>20} {'toward rho*?':>13} {'decay rate k':>13}")
        for rho0 in (0.20, 0.35, 0.65, 0.80):
            mt = run_field(S, rho0, T, 3, ext)
            moved = mt[-1] - mt[0]
            toward = (rho0 < RHO_STAR and moved > 0.01) or (rho0 > RHO_STAR and moved < -0.01)
            k = relax_rate(mt)
            tag = "yes" if toward else ("froze" if abs(moved) < 0.01 else "AWAY")
            print(f"    {rho0:>5.2f} {mt[0]:>9.2f} -> {mt[-1]:<8.2f} {tag:>13} {k:>13.3f}")
    print("\n" + "-" * 78)
    print("READ: <rho> decaying to rho* from BOTH sides, exponentially, amplitude-independent")
    print("  rate = RC channel reproduced. Relaxes UP from below but NOT down from above")
    print("  = generative-only; RC needs a rho-decay (dissipation) the deposit rule lacks.")
    print("-" * 78)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
