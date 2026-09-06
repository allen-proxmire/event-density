"""Faithful replay: validate the shape claim, and measure WHY the front matters.

Ledger #108 established, by reading the source, that deposit(v) takes the
mean-field angle of committed neighbours and does NOT depend on which arm is
running.  So the whole arm-to-arm xi difference is the commit ORDER.  The
replay written for #108 confirmed the mechanism but flattened rho, so its
numbers were flagged and discarded.

This one is faithful.  During the live run it records, for every deposit, the
exact (neighbour, A) pairs that entered holo_acc -- where

    A = kappa_bw * (bw(w,v) - 1) + kappa_rho * (rho_w - rho_v)

and rho ACCUMULATES with every commit.  A replay driven by that recording is
bit-faithful to the live deposit given the same order, so:

  (1) VALIDATION -- replaying an arm's own recording must reproduce its live
      xi.  If it does, the deposit really is fully determined by (order, A),
      which is #108's claim tested rather than asserted.

  (2) MECHANISM -- with the recording in hand we can ask WHY one front has
      shorter phase reach than another.  The candidate is the spread of A.
      A is the connection the phases are transported through; a front that
      grows so as to put large rho-differences between neighbours spreads A,
      and a spread connection destroys coherence.  That is measurable.

Run: python p12_faithful_replay_probe.py
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


def live(seed, k_phase, mode):
    """Run the fill; return (phase, committed, coords, recording, front_coord).

    recording = list of (v, [(w, A), ...]) in deposit order -- everything
    holo_acc saw, so a replay can reproduce the deposit exactly."""
    rng = np.random.default_rng(seed)
    g, coords, nid = P.build_grid(L, BWD, rng)
    N = L * L
    state = StateVector({i: NodeState() for i in range(N)})
    coeffs = SigmaCoeffs()
    phase = np.full(N, np.nan)
    committed = np.zeros(N, dtype=bool)
    rec = []
    coordn = []

    def holo_pairs(v):
        out = []
        for w in g.neighbors(v):
            if committed[w]:
                A = KBW * (g.bw(w, v) - 1.0) + KRHO * (state[w].rho - state[v].rho)
                out.append((w, A))
        return out

    def phase_bonus(v):
        pairs = holo_pairs(v)
        n = len(pairs)
        if not n:
            return 0.0
        acc = sum(cmath.exp(1j * (phase[w] + A)) for w, A in pairs)
        a = abs(acc)
        if mode == "grad":
            return a
        if mode == "coh_v3":
            return a / n
        return a + 0.5 * (a * a - n)

    def deposit(v):
        pairs = holo_pairs(v)
        acc = sum(cmath.exp(1j * (phase[w] + A)) for w, A in pairs)
        ang = rng.uniform(0, 2 * math.pi) if abs(acc) < 1e-12 else math.atan2(acc.imag, acc.real)
        phase[v] = ang % (2 * math.pi)
        committed[v] = True
        rec.append((v, pairs))
        coordn.append(len(pairs))

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
            winner = apply_tiebreak(u, [v for v, sc in tot.items() if sc == tmax], g)
            first = not committed[winner]
            state[winner].commit(coeffs.increment)
            if first:
                deposit(winner)
            state[u].active = False
            state[winner].active = True
            active.add(winner)
            commits += 1
    return phase, committed, coords, rec, float(np.mean(coordn[1:]))


def replay(rec, seed):
    """Deposit phases from the recording alone.  Bit-faithful given the order."""
    rng = np.random.default_rng(seed)          # same stream position is not
    N = L * L                                   # guaranteed; see the note below
    phase = np.full(N, np.nan)
    committed = np.zeros(N, dtype=bool)
    for v, pairs in rec:
        acc = sum(cmath.exp(1j * (phase[w] + A)) for w, A in pairs if committed[w])
        ang = rng.uniform(0, 2 * math.pi) if abs(acc) < 1e-12 else math.atan2(acc.imag, acc.real)
        phase[v] = ang % (2 * math.pi)
        committed[v] = True
    return phase, committed


def a_spread(rec):
    """Spread of the transport connection actually encountered."""
    allA = [A for _, pairs in rec for _, A in pairs]
    return float(np.std(allA)), float(np.mean(np.abs(allA)))


def main():
    print("Faithful replay. Condition (C), %dx%d, %d seeds." % (L, L, len(SEEDS)))
    print("Recording every (neighbour, A) pair that entered each deposit.\n")

    arms = [(0.0, "coh", "control   k=0"),
            (8.0, "grad", "Grad      k=8"),
            (8.0, "coh", "CANON Coh k=8"),
            (8.0, "coh_v3", "old-Coh   k=8")]

    print("  %-16s %9s %9s %10s %10s %8s"
          % ("arm", "xi live", "xi replay", "std(A)", "mean|A|", "front n"))
    rows = []
    for kp, mode, label in arms:
        lv, rp, sa, ma, fc = [], [], [], [], []
        for s in SEEDS:
            ph, c, co, rec, coordn = live(s, kp, mode)
            xi_live = P.xi_estimate(P.corr_vs_r(ph, c, co, np.random.default_rng(s)))
            ph2, c2 = replay(rec, s)
            xi_rep = P.xi_estimate(P.corr_vs_r(ph2, c2, co, np.random.default_rng(s)))
            sd, mn = a_spread(rec)
            lv.append(xi_live); rp.append(xi_rep); sa.append(sd); ma.append(mn); fc.append(coordn)
        rows.append((label, np.mean(lv), np.mean(rp), np.mean(sa), np.mean(ma), np.mean(fc)))
        print("  %-16s %9.2f %9.2f %10.3f %10.3f %8.3f"
              % (label, np.mean(lv), np.mean(rp), np.mean(sa), np.mean(ma), np.mean(fc)))

    print("""
READING

  VALIDATION -- 'xi replay' should equal 'xi live'.  The recording carries
  every input the deposit had, so if these match, #108's claim is confirmed by
  test and not only by reading: the phase field is fully determined by the
  commit order plus the connection values, with no dependence on which arm's
  bonus produced that order.

  MECHANISM -- std(A) is the spread of the transport connection each front
  actually encountered.  A is what phases are carried through; a wide spread
  scrambles them.  If the arms with short xi are the arms with large std(A),
  the story is complete: the phase bonus steers growth into fronts with big
  rho-differences between neighbours, which widens the connection, which
  shortens the reach.  Nothing about the phase FORMULA is involved.
""")
    xs = np.array([r[3] for r in rows])
    ys = np.array([r[1] for r in rows])
    if len(xs) > 2 and xs.std() > 0:
        print("  correlation across arms, std(A) vs xi_live : r = %.3f"
              % float(np.corrcoef(xs, ys)[0, 1]))


if __name__ == "__main__":
    main()
