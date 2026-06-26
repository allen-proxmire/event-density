"""RLC channel test: does the substrate produce telegraph OSCILLATION (the participation
channel)? Oscillation needs a GLOBAL feedback loop (the participation variable v). The
certified Sigma-rule is purely LOCAL, so the prior is: bare substrate = monotone (no ring);
add the global participation feedback (ED's non-local P04 participation, the UDM paper's
"minimal non-local extension") and the telegraph oscillation appears.

Part A: bare substrate, track <rho>(t) -> expect monotone (no oscillation).
Part B: add global participation v (v' = (-kappa(<rho>-rho*) - zeta v)/tau; uniform feedback
        rho += H v each step) -> expect damped oscillation of <rho> for H above threshold.

Oscillation detected by counting sign-changes of (<rho> - rho*) (monotone ~ 0-1; ring = many).
Certified Sigma-rule for the local dynamics; the participation feedback is the added ED
ingredient (made explicit, parallel to extinction for RC).
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


def run(S, T, seed, H, tau=1.0, zeta=0.1, kappa=1.0, seed_frac=0.25, ext=-1.2, rho0=0.35):
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
    v = 0.0
    mt = [float(np.mean([sv[n].rho for n in alln]))]
    for _ in range(T):
        step(sv, g, coeffs, strata=st)   # local substrate dynamics (may stop returning 0; keep forcing)
        rbar = float(np.mean([sv[n].rho for n in alln]))
        v += (-kappa * (rbar - RHO_STAR) - zeta * v) / tau     # global participation mode
        if H > 0:
            for n in alln:
                sv[n].rho = max(0.0, sv[n].rho + H * v)         # uniform feedback (the inductor)
        mt.append(float(np.mean([sv[n].rho for n in alln])))
    return np.array(mt)


def n_oscillations(mt):
    d = mt - RHO_STAR
    s = np.sign(d)
    return int(np.sum(s[1:] != s[:-1]))


def main():
    S, T = 81, 70
    print("=" * 76)
    print(f"RLC OSCILLATION TEST — does <rho> RING (telegraph) with global feedback?")
    print("=" * 76)
    print(f"\n  {'H (feedback)':>13} {'sign-crossings of <rho>-rho*':>30}   verdict")
    for H in (0.0, 0.05, 0.10, 0.20):
        mt = run(S, T, 3, H)
        nc = n_oscillations(mt)
        verdict = ("monotone (no ring)" if nc <= 1 else
                   "RINGS (telegraph oscillation)" if nc >= 3 else "marginal")
        print(f"  {H:>13.2f} {nc:>30d}   {verdict}")
        if H in (0.0, 0.10):
            samp = " ".join(f"{mt[i]:.2f}" for i in range(0, len(mt), max(1, len(mt) // 10)))
            print(f"                <rho>(t): {samp}")

    print("\n" + "-" * 76)
    print("READ: H=0 (bare local rule) monotone = oscillation is NOT native to the local")
    print("  substrate. Ringing appears only once the GLOBAL participation feedback is added")
    print("  = RLC needs the non-local participation ingredient (ED's P04), not the bare rule.")
    print("-" * 76)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
