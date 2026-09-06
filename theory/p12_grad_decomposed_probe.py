"""Is Grad's shrinking xi a PHASE effect, or a coordination-number artifact?

Note_PhaseInGrad_Probe_2026-09-05.md found the only surviving discriminator
between assigning the measured phase-alignment to Coh or to Grad:

    Coh  (intensive, |acc|/n) : xi flat at ~3.7-4.2 across a 16x sweep in k_phase
    Grad (extensive, |acc|)   : xi falls monotonically, 2.2 -> 0.8

and then flagged its own honest limit, verbatim:

    "The extensive form conflates two effects: alignment quality and
     coordination number.  A cleaner probe would decompose
     |acc| = n x (|acc|/n) and sweep [them separately]."

This is that probe.  Since |acc| = n * (|acc|/n) exactly, the two readings
differ by ONE factor of the coordination number n.  So generalise:

    bonus(v) = n**alpha * (|acc| / n)          alpha = 0 -> Coh
                                               alpha = 1 -> Grad

and add the decisive control:

    bonus(v) = n                                PHASE-BLIND coordination reward

THE TEST.  If rewarding coordination number with NO phase information at all
reproduces the shrinking xi, then Grad's discriminator is an artifact of
extensivity and not a statement about phase -- and the discriminator dies.

Run: python p12_grad_decomposed_probe.py
"""
import cmath
import math
import sys

import numpy as np

SIM = r"C:/Users/allen/GitHub/event-density/evaluation/Bits"
THEORY = r"C:/Users/allen/GitHub/event-density/theory"
sys.path.insert(0, SIM)
sys.path.insert(0, THEORY)

from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,
                       compute_sigma, compute_candidates, apply_tiebreak)
import p12_phase_in_grad_probe as P


def run_fill(L, bw_disorder, kappa_bw, kappa_rho, k_phase, rng,
             alpha=0.0, phase_blind=False, n_seeds=1, max_commits_factor=6):
    """bonus = n**alpha * (|acc|/n); phase_blind replaces |acc|/n by 1.0."""
    g, coords, nid = P.build_grid(L, bw_disorder, rng)
    N = L * L
    state = StateVector({i: NodeState() for i in range(N)})
    coeffs = SigmaCoeffs()
    phase = np.full(N, np.nan)
    committed = np.zeros(N, dtype=bool)

    def holo_acc(v):
        acc = 0j
        n = 0
        for w in g.neighbors(v):
            if committed[w]:
                A = kappa_bw * (g.bw(w, v) - 1.0) + kappa_rho * (state[w].rho - state[v].rho)
                acc += cmath.exp(1j * (phase[w] + A))
                n += 1
        return acc, n

    def phase_bonus(v):
        acc, n = holo_acc(v)
        if not n:
            return 0.0
        quality = 1.0 if phase_blind else abs(acc) / n
        return (n ** alpha) * quality

    def deposit(v):
        acc, n = holo_acc(v)
        ang = rng.uniform(0, 2 * math.pi) if abs(acc) < 1e-12 else math.atan2(acc.imag, acc.real)
        phase[v] = ang % (2 * math.pi)
        committed[v] = True

    seeds = rng.choice(N, size=n_seeds, replace=False)
    active = set()
    for s in seeds:
        state[int(s)].commit(coeffs.increment)
        state[int(s)].active = True
        deposit(int(s))
        active.add(int(s))

    max_commits = max_commits_factor * N
    commits = 0
    while active and commits < max_commits and committed.sum() < N:
        order = sorted(active)
        active = set()
        for u in order:
            if not state[u].active:
                continue
            cands = compute_candidates(u, state, g)
            if not cands:
                state[u].active = False
                continue
            base = {v: compute_sigma(u, v, state, g, coeffs) for v in cands}
            if k_phase:
                tot = {v: base[v] + k_phase * phase_bonus(v) for v in cands}
            else:
                tot = base
            tmax = max(tot.values())
            winner = apply_tiebreak(u, [v for v, s in tot.items() if s == tmax], g)
            first = not committed[winner]
            state[winner].commit(coeffs.increment)
            if first:
                deposit(winner)
            state[u].active = False
            state[winner].active = True
            active.add(winner)
            commits += 1
    return phase, committed, coords


def measure(L, bwd, kbw, krho, kp, seed, alpha, phase_blind=False):
    fresh = lambda: np.random.default_rng(seed)
    p, c, co = run_fill(L, bwd, kbw, krho, kp, fresh(), alpha=alpha, phase_blind=phase_blind)
    R = P.global_order(p, c)
    C = P.corr_vs_r(p, c, co, fresh())
    return R, P.xi_estimate(C)


def main():
    L, seed = 64, 11
    BWD, KBW, KRHO = 0.5, 0.5, 0.5            # condition (C), the physical case
    KPS = [0.5, 1.0, 2.0, 4.0, 8.0]

    print("Grad's shrinking xi: phase effect, or coordination-number artifact?")
    print("=" * 78)
    print("Condition (C), the physical case: quenched bandwidth + rho holonomy.")
    print("Grid %dx%d, single seed, no thermal noise, matched RNG stream.\n" % (L, L))
    print("bonus = n**alpha * (|acc|/n)      alpha=0 -> Coh,  alpha=1 -> Grad\n")

    print("  %-40s %s" % ("", "  ".join("kp=%.1f" % k for k in KPS)))
    rows = {}
    for label, alpha, blind in [
        ("alpha=0.0  (Coh, intensive)", 0.0, False),
        ("alpha=0.5  (interpolated)", 0.5, False),
        ("alpha=1.0  (Grad, extensive)", 1.0, False),
        ("PHASE-BLIND n only  (the control)", 1.0, True),
    ]:
        xis = []
        for kp in KPS:
            R, xi = measure(L, BWD, KBW, KRHO, kp, seed, alpha, phase_blind=blind)
            xis.append(xi)
        rows[label] = xis
        print("  %-40s %s" % (label, "  ".join("%6.1f" % x for x in xis)))

    print("""
READING

  The Coh and Grad rows should reproduce the earlier run (flat ~4 vs falling
  2.2 -> 0.8).  The row that decides the question is the last one.

  THE PHASE-BLIND CONTROL rewards coordination number and NOTHING ELSE -- it
  cannot see phase at all, since |acc|/n is replaced by the constant 1.  If it
  still shows xi shrinking as k_phase rises, then the shrinkage is a property
  of extensivity, not of the phase term, and the discriminator proposed in
  Note_PhaseInGrad_Probe cannot distinguish the Coh and Grad readings.
""")
    blind = rows["PHASE-BLIND n only  (the control)"]
    grad = rows["alpha=1.0  (Grad, extensive)"]
    print("  phase-blind xi trend : %6.1f -> %6.1f   (%s)"
          % (blind[0], blind[-1], "SHRINKS" if blind[-1] < blind[0] else "does not shrink"))
    print("  Grad        xi trend : %6.1f -> %6.1f   (%s)"
          % (grad[0], grad[-1], "SHRINKS" if grad[-1] < grad[0] else "does not shrink"))
    if blind[-1] < blind[0]:
        print("""
  VERDICT: the shrinkage survives with the phase information removed.
  Grad's xi-trend is a COORDINATION-NUMBER ARTIFACT.  The discriminator is
  dead, and the Coh-versus-Grad question returns to the draw it was in
  before that trend was proposed.""")
    else:
        print("""
  VERDICT: the shrinkage does NOT survive removing the phase information, so
  the trend is a genuine phase effect and the discriminator stands.""")


if __name__ == "__main__":
    main()
