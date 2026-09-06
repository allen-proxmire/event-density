"""Does a DWELL-CAPABLE update rule change any certified result?

P-Commitment-Advancement was adopted 2026-09-06 (gravity ledger #117): a
commitment selecting a propagation-carrying (Adjacency-class) channel advances
the chain's locus; one selecting a non-propagating channel does not.  The
certified rule is the special case where every commitment advances -- its
candidate set is admissible_neighbors(u), with u excluded.

This makes the rule dwell-capable in the minimal way: ADD u TO ITS OWN
CANDIDATE SET, scored by the certified Sigma exactly as any other candidate.
Nothing else changes -- same Sigma, same tiebreak, same commit chokepoint.

THE ALGEBRA FIRST, because it predicts the answer.  The certified Sigma is

    Coh  = -(rho_v - rho_star)^2      rho_star = 0.5
    Str  = rho_v
    Grad = |rho_v - rho_u|
    Sigma(u->v) = Coh - Str - Grad

For a SELF-transition, Grad = 0 -- there is no gradient to fight -- so

    Sigma(u->u)      = -(rho_u - 0.5)^2 - rho_u
    Sigma(u->v_new)  = -0.25 - rho_u          (fresh neighbour, rho_v = 0)

    rho_u = 1 :  -1.25  vs  -1.25   EXACT TIE
    rho_u = 2 :  -4.25  vs  -2.25   neighbour wins
    rho_u = 3 :  -9.25  vs  -3.25   neighbour wins, by more

So with the certified parameters (rho_star = 0.5, increment = 1) a locus jumps
from 0 straight to 1, PAST the coherence target, and dwell is never favoured
after that -- it is only ever tied, at rho_u = 1, and then decided by the
tiebreak on node ids.

PREDICTION: the certified results are robust to allowing dwell, not because the
rule forbids it but because the PARAMETERS make it non-competitive.  This run
tests that, and measures how often dwell actually wins.

Run: python p12_dwell_capable_probe.py
"""
import sys

import numpy as np

SIM = r"C:/Users/allen/GitHub/event-density/evaluation/Bits"
THEORY = r"C:/Users/allen/GitHub/event-density/theory"
sys.path.insert(0, SIM)
sys.path.insert(0, THEORY)

from simulator import (NodeState, StateVector, SigmaCoeffs,
                       compute_sigma, compute_candidates, apply_tiebreak)
import p12_phase_in_grad_probe as P

L = 64
SEEDS = [11, 12, 13, 14, 15]
BWD, KBW, KRHO = 0.5, 0.5, 0.5           # condition (C), the physical case


def run(seed, dwell_capable, k_phase=0.0):
    rng = np.random.default_rng(seed)
    g, coords, nid = P.build_grid(L, BWD, rng)
    N = L * L
    state = StateVector({i: NodeState() for i in range(N)})
    coeffs = SigmaCoeffs()
    phase = np.full(N, np.nan)
    committed = np.zeros(N, dtype=bool)

    import cmath, math

    def holo_acc(v):
        acc, n = 0j, 0
        for w in g.neighbors(v):
            if committed[w]:
                A = KBW * (g.bw(w, v) - 1.0) + KRHO * (state[w].rho - state[v].rho)
                acc += cmath.exp(1j * (phase[w] + A))
                n += 1
        return acc, n

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

    commits = dwells = decisions = 0
    while active and commits < 6 * N and committed.sum() < N:
        cur = sorted(active)
        active = set()
        for u in cur:
            if not state[u].active:
                continue
            cands = compute_candidates(u, state, g)
            if dwell_capable:
                cands = cands + [u]          # the ONLY change
            if not cands:
                state[u].active = False
                continue
            sc = {v: compute_sigma(u, v, state, g, coeffs) for v in cands}
            smax = max(sc.values())
            maximal = [v for v, x in sc.items() if x == smax]
            # The certified tiebreak keys on graph.bw(u, v) -- the EDGE
            # bandwidth -- so a self-transition has no key at all.  That is a
            # SECOND place the certified rule assumes the winner is a
            # neighbour.  One modelling choice is unavoidable here: give the
            # self-move the disorder MEAN, bw = 1.0, so it competes on the same
            # footing as an average edge rather than being handed a win or a
            # loss by construction.
            winner = max(maximal, key=lambda v: (1.0 if v == u else g.bw(u, v), v))
            decisions += 1
            if winner == u:
                dwells += 1
            first = not committed[winner]
            state[winner].commit(coeffs.increment)
            if first:
                deposit(winner)
            state[u].active = False
            state[winner].active = True
            active.add(winner)
            commits += 1
    return phase, committed, coords, (dwells / decisions if decisions else 0.0), committed.sum()


def measure(seed, dwell_capable):
    ph, c, co, dfrac, ncom = run(seed, dwell_capable)
    R = P.global_order(ph, c)
    xi = P.xi_estimate(P.corr_vs_r(ph, c, co, np.random.default_rng(seed)))
    return R, xi, dfrac, ncom


def main():
    print("Dwell-capable rule vs the certified rule. Condition (C), %dx%d, %d seeds."
          % (L, L, len(SEEDS)))
    print("Only change: u is added to its own candidate set, scored by the same Sigma.\n")
    print("  %-22s %8s %8s %12s %10s" % ("rule", "R", "xi", "dwell frac", "committed"))
    out = {}
    for dc, label in ((False, "certified (no dwell)"), (True, "DWELL-CAPABLE")):
        res = [measure(s, dc) for s in SEEDS]
        Rs = np.mean([r[0] for r in res]); xis = np.mean([r[1] for r in res])
        df = np.mean([r[2] for r in res]); nc = np.mean([r[3] for r in res])
        out[label] = (Rs, xis, df, nc)
        print("  %-22s %8.3f %8.2f %12.4f %10.0f" % (label, Rs, xis, df, nc))

    a = out["certified (no dwell)"]
    b = out["DWELL-CAPABLE"]
    print("""
READING
""")
    print("  dwell fraction under the dwell-capable rule : %.4f" % b[2])
    print("  R    certified %.3f  ->  dwell-capable %.3f   (delta %+.3f)" % (a[0], b[0], b[0] - a[0]))
    print("  xi   certified %.2f  ->  dwell-capable %.2f   (delta %+.2f)" % (a[1], b[1], b[1] - a[1]))
    print("  nodes committed  %.0f -> %.0f" % (a[3], b[3]))
    print("""
  The algebra predicts dwell is only ever TIED (at rho_u = 1) and disfavoured
  after, because with rho_star = 0.5 and increment = 1 a locus jumps from 0
  straight past the coherence target.  If the dwell fraction is ~0 and the
  measured quantities are unchanged, the certified results are robust to
  allowing dwell -- and the reason is the PARAMETERS, not the rule.

  That would also say something about the dwell route: adopting
  P-Commitment-Advancement licenses a dwell, but the certified parameters make
  it unreachable.  A dwell-bearing substrate needs rho_star or the increment
  changed, which is a separate and much larger commitment.
""")


if __name__ == "__main__":
    main()
