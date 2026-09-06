"""Does #111's Coh-vs-Grad ordering survive a change in rho_star?

Ledger #119 found rho_star is undocumented and dominates phase reach: xi runs
5.23 / 2.13 / 1.19 / 0.76 / 0.63 across rho_star = 0.0 / 0.5 / 1.0 / 1.5 / 2.0,
a factor of eight.  Every result in #103-#118 was measured at rho_star = 0.5.

#111's conclusion was a 2x2: binding requires INTENSIVE scoring AND NO
neighbour-neighbour term, so only |acc|/n (which is intensive Grad) binds.
That was established at one rho_star.

THE TEST.  "Binds" means: reach exceeds the NO-PHASE CONTROL AT THE SAME
rho_star.  The control has to move with rho_star or the comparison is
meaningless -- which is exactly the error #119 warns about.  So for each
rho_star, run the control and every arm, and ask which arms clear their own
control.

If the same arms bind at every rho_star, #111 is general.  If the set changes,
#111 is a statement about rho_star = 0.5.

Run: python p12_rhostar_ordering_probe.py
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
RHOSTARS = [0.0, 0.5, 1.0]
KP = 8.0


def run(seed, rho_star, k_phase, mode):
    rng = np.random.default_rng(seed)
    g, coords, nid = P.build_grid(L, BWD, rng)
    N = L * L
    state = StateVector({i: NodeState() for i in range(N)})
    coeffs = SigmaCoeffs(rho_star=rho_star)
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
    return xi


def mean_xi(rho_star, k_phase, mode):
    return float(np.mean([run(s, rho_star, k_phase, mode) for s in SEEDS]))


def main():
    print("Does #111's ordering survive rho_star? %dx%d, %d seeds, k_phase = %.0f."
          % (L, L, len(SEEDS), KP))
    print("'Binds' = reach exceeds the NO-PHASE CONTROL AT THE SAME rho_star.\n")

    arms = [("grad", "Grad  |acc|            (extensive, no NN)"),
            ("coh", "canonical Coh          (extensive, NN)"),
            ("coh_int", "intensive Coh          (intensive, NN)"),
            ("coh_v3", "|acc|/n = intensive Grad (intensive, no NN)")]

    verdicts = {}
    for rs in RHOSTARS:
        ctrl = mean_xi(rs, 0.0, "coh")
        print("rho_star = %.1f   control xi = %.2f" % (rs, ctrl))
        binds = []
        for mode, label in arms:
            xi = mean_xi(rs, KP, mode)
            ok = xi > ctrl
            if ok:
                binds.append(mode)
            print("   %-44s xi = %5.2f   %s"
                  % (label, xi, "BINDS" if ok else "does not bind"))
        verdicts[rs] = tuple(binds)
        print()

    print("=" * 78)
    print("ORDERING ACROSS rho_star\n")
    for rs in RHOSTARS:
        print("  rho_star = %.1f  ->  binds: %s" % (rs, verdicts[rs] or "(none)"))
    same = len(set(verdicts.values())) == 1
    print("""
  %s

  If the SAME arms bind at every rho_star, #111's 2x2 is general: binding needs
  intensive scoring and no neighbour-neighbour term, whatever the coherence
  target.  If the set changes, #111 is a statement about rho_star = 0.5 and
  should be relabelled.
""" % ("SAME SET AT EVERY rho_star -- the ordering is stable."
       if same else "THE SET CHANGES -- #111 is rho_star-dependent."))


if __name__ == "__main__":
    main()
