"""The last undocumented parameter: does `increment` change anything?

Ledger #119 flagged rho_star = 0.5 and increment = 1 as equally undocumented,
and #120 tested rho_star: the ARM RANKING is invariant, the BINDING threshold
is not.  This does the same for `increment`, which is the other half -- it sets
the reachable lattice that rho_star is measured against.

    rho reachable at 0, inc, 2*inc, ...      Coh = -(rho_v - 0.5)^2

    inc = 1.0  (certified) : reachable {0, 1, 2}     target 0.5 is UNREACHABLE,
                                                     equidistant from 0 and 1
    inc = 0.5              : reachable {0, .5, 1}    target is EXACTLY REACHABLE
    inc = 2.0              : reachable {0, 2, 4}     target badly overshot

The inc = 0.5 case is the interesting one, and the algebra predicts something
sharp.  At rho_u = 0.5 a locus sits exactly ON the coherence optimum:

    Sigma(u->u)     = -(0.5-0.5)^2 - 0.5 - 0     = -0.50
    Sigma(u->v_new) = -(0-0.5)^2   - 0   - 0.5   = -0.75

So with inc = 0.5 the SELF-transition strictly beats a fresh neighbour -- the
rule becomes dwell-PREFERRING.  The certified rule forbids self-transitions, so
the front is forced onto a strictly worse-scoring candidate every step.  That is
a qualitatively different regime from the certified one, produced by changing a
constant nothing documents.

Measured here: the arm ranking and the binding verdict, exactly as #120, with
each arm against the no-phase control at its OWN increment.

Run: python p12_increment_probe.py
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

L = 48
SEEDS = [11, 12, 13]
BWD, KBW, KRHO = 0.5, 0.5, 0.5
INCREMENTS = [0.5, 1.0, 2.0]
KP = 8.0


def run(seed, increment, k_phase, mode):
    rng = np.random.default_rng(seed)
    g, coords, nid = P.build_grid(L, BWD, rng)
    N = L * L
    state = StateVector({i: NodeState() for i in range(N)})
    coeffs = SigmaCoeffs(increment=increment)          # rho_star stays 0.5
    phase = np.full(N, np.nan)
    committed = np.zeros(N, dtype=bool)

    def holo_acc(v):
        acc, n = 0j, 0
        for w in g.neighbors(v):
            if committed[w]:
                A = KBW * (g.bw(w, v) - 1.0) + KRHO * (state[w].rho - state[v].rho)
                acc += cmath.exp(1j * (phase[w] + A))
                n += 1
        return acc, n

    def phase_bonus(v):
        acc, n = holo_acc(v)
        if not n:
            return 0.0
        a = abs(acc)
        if mode == "grad":
            return a
        if mode == "coh_v3":
            return a / n
        if mode == "coh_int":
            return a / n + 0.5 * (a * a - n) / (n * n)
        return a + 0.5 * (a * a - n)

    def deposit(v):
        acc, n = holo_acc(v)
        ang = rng.uniform(0, 2 * math.pi) if abs(acc) < 1e-12 else math.atan2(acc.imag, acc.real)
        phase[v] = ang % (2 * math.pi)
        committed[v] = True

    s = int(rng.choice(N))
    state[s].commit(coeffs.increment)
    state[s].active = True
    deposit(s)
    active = {s}
    commits = 0
    while active and commits < 6 * N and committed.sum() < N:
        cur = sorted(active)
        active = set()
        for u in cur:
            if not state[u].active:
                continue
            cands = compute_candidates(u, state, g)
            if not cands:
                state[u].active = False
                continue
            base = {v: compute_sigma(u, v, state, g, coeffs) for v in cands}
            tot = ({v: base[v] + k_phase * phase_bonus(v) for v in cands}
                   if k_phase else base)
            tmax = max(tot.values())
            winner = apply_tiebreak(u, [v for v, x in tot.items() if x == tmax], g)
            first = not committed[winner]
            state[winner].commit(coeffs.increment)
            if first:
                deposit(winner)
            state[u].active = False
            state[winner].active = True
            active.add(winner)
            commits += 1
    xi = P.xi_estimate(P.corr_vs_r(phase, committed, coords, np.random.default_rng(seed)))
    return xi, int(committed.sum())


def mean_of(increment, k_phase, mode):
    res = [run(s, increment, k_phase, mode) for s in SEEDS]
    return float(np.mean([r[0] for r in res])), float(np.mean([r[1] for r in res]))


def main():
    print("The `increment` sweep. %dx%d, %d seeds, k_phase = %.0f, rho_star = 0.5 fixed."
          % (L, L, len(SEEDS), KP))
    print("Each arm against the no-phase control at its OWN increment.\n")

    arms = [("grad", "Grad  |acc|              (ext, no NN)"),
            ("coh", "canonical Coh            (ext, NN)"),
            ("coh_int", "intensive Coh            (int, NN)"),
            ("coh_v3", "|acc|/n = intensive Grad (int, no NN)")]

    rankings, binders = {}, {}
    for inc in INCREMENTS:
        c_xi, c_n = mean_of(inc, 0.0, "coh")
        tag = "  <== certified" if inc == 1.0 else ("  <== target reachable" if inc == 0.5 else "")
        print("increment = %.1f   control xi = %.2f   (filled %.0f/%d)%s"
              % (inc, c_xi, c_n, L * L, tag))
        rows = []
        for mode, label in arms:
            xi, nn = mean_of(inc, KP, mode)
            rows.append((mode, xi))
            print("   %-40s xi = %5.2f  %s   (filled %.0f)"
                  % (label, xi, "BINDS" if xi > c_xi else "     ", nn))
        rankings[inc] = tuple(m for m, _ in sorted(rows, key=lambda r: -r[1]))
        binders[inc] = tuple(m for m, x in rows if x > c_xi)
        print()

    print("=" * 78)
    print("ACROSS `increment`\n")
    for inc in INCREMENTS:
        print("  inc = %.1f   ranking %s   binds %s"
              % (inc, " > ".join(rankings[inc]), binders[inc] or "(none)"))
    print("""
  Ranking stable?  %s
  Binder set stable? %s

  #120 found the ranking invariant across rho_star and the binding threshold
  not.  If the same split appears here, the pattern is a property of the
  comparison and not of either parameter -- WHICH functional is best is robust,
  WHETHER a phase term helps is a regime statement.
""" % ("YES" if len(set(rankings.values())) == 1 else "NO",
       "YES" if len(set(binders.values())) == 1 else "NO"))


if __name__ == "__main__":
    main()
