"""The two-line fix: run the ORIGINAL probe with a Coh arm that is actually Coh.

Gravity ledger #104 found that p12_phase_in_grad_probe.py's "Coh reading",
bonus = |acc|/n, is not canonical Coh at all -- it is the simulator's
v3_active per-locus-average convention, i.e. Grad divided by the coordination
number.  So that probe compared Grad against Grad/n and never asked the
question.

Canonical Coh at a candidate v, with b ~ 1 and v's own contribution included:

    Coh(v) = |e^{i phi_v} + acc|^2 - (1 + n)
           = |acc|^2 - n + 2|acc| cos(phi_v - arg acc)

maximised over v's free phase:

    Coh_max = 2|acc| + (|acc|^2 - n)
    Grad_max = 2|acc|                       (the Dirichlet form, as before)

    ==>  Coh - Grad = |acc|^2 - n = 2 * sum_{w<w'} cos(dpi_ww')
                    = exactly the NEIGHBOUR-NEIGHBOUR cross term.

Everything else in the original probe is untouched, so the 'grad' arm here
reproduces the validated baseline and the comparison is like-for-like.

Three arms:
    grad     |acc|                          the Dirichlet form (baseline)
    coh_v3   |acc| / n                      the OLD arm -- kept to show it move
    coh      |acc| + (|acc|^2 - n)/2        CANONICAL Coh, same normalisation
                                            as grad, differing by exactly NN

Run: python p12_coh_canonical_probe.py
"""
import cmath
import math
import sys

import numpy as np

SIM = r"C:/Users/allen/GitHub/event-density/evaluation/Bits"
THEORY = r"C:/Users/allen/GitHub/event-density/theory"
sys.path.insert(0, SIM)
sys.path.insert(0, THEORY)

from simulator import (NodeState, StateVector, SigmaCoeffs,
                       compute_sigma, compute_candidates, apply_tiebreak)
import p12_phase_in_grad_probe as P


def run_fill(L, bw_disorder, kappa_bw, kappa_rho, k_phase, rng,
             mode="coh", n_seeds=1, max_commits_factor=6):
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

    # ---- the only thing that differs between arms ----------------------
    def phase_bonus(v):
        acc, n = holo_acc(v)
        if not n:
            return 0.0
        a = abs(acc)
        if mode == "grad":
            return a
        if mode == "coh_v3":
            return a / n
        return a + 0.5 * (a * a - n)          # canonical Coh
    # --------------------------------------------------------------------

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


def measure(L, bwd, kbw, krho, kp, seed, mode):
    fresh = lambda: np.random.default_rng(seed)
    p, c, co = run_fill(L, bwd, kbw, krho, kp, fresh(), mode=mode)
    R = P.global_order(p, c)
    xi = P.xi_estimate(P.corr_vs_r(p, c, co, fresh()))
    return R, xi


def verdict(R, xi):
    return "CRYSTAL" if (R > 0.8 and xi > 15) else "finite"


def main():
    L, seed = 64, 11
    print("Canonical-Coh probe. %dx%d, single seed, no thermal noise." % (L, L))
    print("Coh - Grad = |acc|^2 - n = the neighbour-neighbour cross term.\n")

    arms = [("grad", "Grad  |acc|            "),
            ("coh_v3", "old 'Coh'  |acc|/n     "),
            ("coh", "CANONICAL Coh          ")]
    conds = [("CONTROL homogeneous (kappa=0)", 0.0, 0.0, 0.0),
             ("(A) bandwidth holonomy kbw=0.5", 0.5, 0.5, 0.0),
             ("(C) physical: bw + rho holonomy", 0.5, 0.5, 0.5)]

    for name, bwd, kbw, krho in conds:
        print("#" * 78)
        print("### " + name)
        for mode, label in arms:
            out = []
            for kp in [0.5, 1.0, 2.0, 4.0, 8.0]:
                R, xi = measure(L, bwd, kbw, krho, kp, seed, mode)
                out.append((kp, R, xi))
            vs = {verdict(R, xi) for _, R, xi in out}
            tag = vs.pop() if len(vs) == 1 else "MIXED"
            print("  %s %s   %s" % (label,
                                    "  ".join("R=%.2f xi=%4.1f" % (R, xi) for _, R, xi in out),
                                    tag))
        print()

    print("""READING

  The 'grad' arm reproduces the validated baseline, so any difference in the
  canonical-Coh arm is attributable to the neighbour-neighbour term and to
  nothing else -- same grid, same seed, same deposit rule, same normalisation.

  What to look for:
    * (A) is the condition where the old arms split -- Grad crystallised,
      old-'Coh' stayed finite.  Since old-'Coh' was Grad/n, that split was the
      coordination number.  Where does CANONICAL Coh fall?
    * (C) is the physical case.  If canonical Coh tracks Grad there, the two
      terms are behaviourally the same where it matters, and which one owns
      the July measurement stops being a live distinction.
""")


if __name__ == "__main__":
    main()
