"""Separating the two effects: is the xi drop about PHASE, or about SHAPE?

Gravity ledger #107 found that in the physical condition (C), both canonical
terms give a phase correlation length BELOW the no-phase control -- Grad
2.1 -> 0.8, canonical Coh 2.1 -> 0.7 -- reaching the paper's own "xi < 1, no
binding at all" failure.  But it flagged a confound it could not resolve.

The probe does two things at once:

  (1) picks which cell commits next        <- the SHAPE of the growing blob
  (2) lays down that cell's phase          <- the PHASE pattern

The phase term enters BOTH.  So a falling xi has two possible causes and the
single number cannot separate them:

  (a) the term genuinely makes phases disagree            -- a real problem
  (b) the term grows a different-shaped blob, and that     -- not about phase
      shape has different phase statistics                   at all

THE EXPERIMENT.  Freeze the shape.  Record the commit ORDER each arm produces,
then replay orders across arms, depositing phases the same way.  Anything left
over after the shape is held fixed is phase; anything that moves with the order
is shape.

Run: python p12_fixed_morphology_probe.py
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

L = 64
SEEDS = [11, 12, 13, 14, 15]
BWD, KBW, KRHO = 0.5, 0.5, 0.5          # condition (C), the physical case


def grow(seed, k_phase, mode):
    """Run the fill and return the COMMIT ORDER plus the graph/state it used."""
    rng = np.random.default_rng(seed)
    g, coords, nid = P.build_grid(L, BWD, rng)
    N = L * L
    state = StateVector({i: NodeState() for i in range(N)})
    coeffs = SigmaCoeffs()
    phase = np.full(N, np.nan)
    committed = np.zeros(N, dtype=bool)
    order = []

    def holo_acc(v):
        acc = 0j
        n = 0
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
        return a + 0.5 * (a * a - n)

    def deposit(v):
        acc, n = holo_acc(v)
        ang = rng.uniform(0, 2 * math.pi) if abs(acc) < 1e-12 else math.atan2(acc.imag, acc.real)
        phase[v] = ang % (2 * math.pi)
        committed[v] = True
        order.append(v)

    s = int(rng.choice(N))
    state[s].commit(coeffs.increment)
    state[s].active = True
    deposit(s)
    active = {s}

    commits = 0
    while active and commits < 6 * N and committed.sum() < N:
        for u in sorted(active):
            pass
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
            winner = apply_tiebreak(u, [v for v, sc in tot.items() if sc == tmax], g)
            first = not committed[winner]
            state[winner].commit(coeffs.increment)
            if first:
                deposit(winner)
            state[u].active = False
            state[winner].active = True
            active.add(winner)
            commits += 1
    return order, g, coords


def replay(order, g, coords, seed):
    """Deposit phases along a GIVEN commit order.  The deposit rule is the same
    in every arm of the original probe -- mean-field angle -- so this isolates
    everything the ORDER contributes."""
    rng = np.random.default_rng(seed + 5000)
    N = L * L
    phase = np.full(N, np.nan)
    committed = np.zeros(N, dtype=bool)
    rho = np.zeros(N)                       # rho at deposit time ~ commit index
    for idx, v in enumerate(order):
        acc = 0j
        for w in g.neighbors(v):
            if committed[w]:
                A = KBW * (g.bw(w, v) - 1.0) + KRHO * (rho[w] - rho[v])
                acc += cmath.exp(1j * (phase[w] + A))
        ang = rng.uniform(0, 2 * math.pi) if abs(acc) < 1e-12 else math.atan2(acc.imag, acc.real)
        phase[v] = ang % (2 * math.pi)
        committed[v] = True
        rho[v] = 1.0
    xi = P.xi_estimate(P.corr_vs_r(phase, committed, coords, np.random.default_rng(seed)))
    return P.global_order(phase, committed), xi


def morphology(order, g):
    """Shape statistic: mean number of already-committed neighbours at the moment
    each cell commits.  High = compact front, low = stringy/dendritic."""
    committed = set()
    ns = []
    for v in order:
        ns.append(sum(1 for w in g.neighbors(v) if w in committed))
        committed.add(v)
    return float(np.mean(ns[1:])) if len(ns) > 1 else 0.0


def main():
    print("Fixed-morphology decomposition. Condition (C), %dx%d, %d seeds." % (L, L, len(SEEDS)))
    print("Deposit rule is identical in every arm, so replaying an order isolates SHAPE.\n")

    arms = [(0.0, "coh", "control  k_phase=0"),
            (1.0, "grad", "Grad     k_phase=1"),
            (8.0, "grad", "Grad     k_phase=8"),
            (1.0, "coh", "Coh      k_phase=1"),
            (8.0, "coh", "Coh      k_phase=8"),
            (8.0, "coh_v3", "old-Coh  k_phase=8")]

    print("  %-22s %10s %10s %14s" % ("arm", "xi (replay)", "R", "front coord."))
    orders = {}
    for kp, mode, label in arms:
        xis, Rs, ms = [], [], []
        for s in SEEDS:
            order, g, coords = grow(s, kp, mode)
            R, xi = replay(order, g, coords, s)
            xis.append(xi)
            Rs.append(R)
            ms.append(morphology(order, g))
        orders[label] = (float(np.mean(xis)), float(np.mean(ms)))
        print("  %-22s %10.2f %10.3f %14.3f"
              % (label, np.mean(xis), np.mean(Rs), np.mean(ms)))

    print("""
CROSS-REPLAY -- the decisive test

  Deposit phases along the CONTROL's order, and along each arm's own order,
  with the same deposit rule.  If xi tracks the ORDER, the drop is shape.
""")
    for s in SEEDS[:3]:
        ctrl_order, gc, coc = grow(s, 0.0, "coh")
        _, xi_ctrl = replay(ctrl_order, gc, coc, s)
        coh_order, gh, coh_co = grow(s, 8.0, "coh")
        _, xi_coh = replay(coh_order, gh, coh_co, s)
        print("  seed %d:  control order -> xi = %.2f   |   Coh(k=8) order -> xi = %.2f"
              % (s, xi_ctrl, xi_coh))

    print("""
  The deposit rule does not depend on the arm -- every arm lays down the
  mean-field angle.  So if the two columns above differ, the ENTIRE difference
  is which cells committed in which order, i.e. SHAPE, and the canonical terms
  are not making phases disagree; they are growing a front whose phase reach is
  shorter.

  That is a different claim from "the term de-correlates", and it changes what
  the binding problem is -- not whether it exists.
""")


if __name__ == "__main__":
    main()
