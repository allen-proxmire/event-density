"""What is rho_star doing in the certified rule, and does its value matter?

Ledger #118 found that dwell is suppressed not by the update rule but by the
PARAMETERS: with rho_star = 0.5 and increment = 1, a locus jumps from 0 straight
past the coherence target.  A corpus search finds NO justification anywhere for
rho_star = 0.5 or for increment = 1; SigmaCoeffs' own docstring says only that
"qualitative roles are fixed ...; magnitudes are tunable".

But rho_star is not a magnitude.  It is a TARGET, and where it sits relative to
the increment is qualitative:

    rho takes values 0, 1, 2, 3, ...          (increment = 1)
    Coh(v) = -(rho_v - rho_star)^2

    rho_star = 0.5  ->  Coh = -0.25, -0.25, -2.25, -6.25, ...
                                ^^^^^^^^^^^^  IDENTICAL at rho = 0 and 1

So at the two commonest candidate densities -- a fresh locus (rho = 0) and a
once-committed one (rho = 1) -- the coherence term takes the SAME VALUE and
cannot distinguish them.  The choice is made entirely by Str and Grad.

And 0.5 is the value that maximises the minimum distance from the target to the
reachable set {0, 1, 2, ...}: it is the MOST unreachable choice available.

Two questions, both measured here:
  (1) How often does Coh actually differentiate between candidates?
  (2) Does the value of rho_star change any measured outcome?

If Coh rarely differentiates and outcomes are flat in rho_star, then rho_star is
inert in the certified regime and the corpus should say so.  If moving it to a
REACHABLE value (1.0) changes things, then 0.5 is a substantive undocumented
choice.

Run: python p12_rhostar_probe.py
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
BWD, KBW, KRHO = 0.5, 0.5, 0.5           # condition (C)


def run(seed, rho_star):
    import cmath, math
    rng = np.random.default_rng(seed)
    g, coords, nid = P.build_grid(L, BWD, rng)
    N = L * L
    state = StateVector({i: NodeState() for i in range(N)})
    coeffs = SigmaCoeffs(rho_star=rho_star)
    phase = np.full(N, np.nan)
    committed = np.zeros(N, dtype=bool)

    def deposit(v):
        acc = 0j
        for w in g.neighbors(v):
            if committed[w]:
                A = KBW * (g.bw(w, v) - 1.0) + KRHO * (state[w].rho - state[v].rho)
                acc += cmath.exp(1j * (phase[w] + A))
        ang = rng.uniform(0, 2 * math.pi) if abs(acc) < 1e-12 else math.atan2(acc.imag, acc.real)
        phase[v] = ang % (2 * math.pi)
        committed[v] = True

    s = int(rng.choice(N))
    state[s].commit(coeffs.increment)
    state[s].active = True
    deposit(s)
    active = {s}

    commits = 0
    decisions = 0
    coh_differentiates = 0
    coh_decides = 0            # Coh differs AND flipping it would change the winner
    while active and commits < 6 * N and committed.sum() < N:
        for u in sorted(active) or []:
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
            decisions += 1
            cohs = [-(state.rho_at(v) - rho_star) ** 2 for v in cands]
            if max(cohs) - min(cohs) > 1e-12:
                coh_differentiates += 1
            full = {v: compute_sigma(u, v, state, g, coeffs) for v in cands}
            # counterfactual: same Sigma with the Coh channel switched off
            nocoh = {v: full[v] - coeffs.kc * (-(state.rho_at(v) - rho_star) ** 2)
                     for v in cands}
            wf = apply_tiebreak(u, [v for v, x in full.items() if x == max(full.values())], g)
            wn = apply_tiebreak(u, [v for v, x in nocoh.items() if x == max(nocoh.values())], g)
            if wf != wn:
                coh_decides += 1
            winner = wf
            first = not committed[winner]
            state[winner].commit(coeffs.increment)
            if first:
                deposit(winner)
            state[u].active = False
            state[winner].active = True
            active.add(winner)
            commits += 1
    R = P.global_order(phase, committed)
    xi = P.xi_estimate(P.corr_vs_r(phase, committed, coords, np.random.default_rng(seed)))
    return (R, xi, committed.sum(),
            coh_differentiates / decisions if decisions else 0.0,
            coh_decides / decisions if decisions else 0.0)


def main():
    print("What is rho_star doing? Condition (C), %dx%d, %d seeds." % (L, L, len(SEEDS)))
    print("increment = 1, so rho is reachable only at 0, 1, 2, ...\n")
    print("  %-12s %8s %8s %10s %14s %12s"
          % ("rho_star", "R", "xi", "committed", "Coh differs", "Coh decides"))
    for rs in (0.0, 0.5, 1.0, 1.5, 2.0):
        res = [run(s, rs) for s in SEEDS]
        R = np.mean([r[0] for r in res]); xi = np.mean([r[1] for r in res])
        nc = np.mean([r[2] for r in res]); cd = np.mean([r[3] for r in res])
        dec = np.mean([r[4] for r in res])
        tag = "   <== certified" if rs == 0.5 else ("   <== reachable" if rs == 1.0 else "")
        print("  %-12.1f %8.3f %8.2f %10.0f %14.3f %12.3f%s"
              % (rs, R, xi, nc, cd, dec, tag))

    print("""
READING

  "Coh differs" is the fraction of decisions where the coherence term takes
  different values across the candidates -- i.e. where it COULD matter.
  "Coh decides" is the fraction where switching the Coh channel off actually
  changes the winner -- i.e. where it DOES matter.

  If "Coh decides" is near zero at the certified rho_star = 0.5, then the
  coherence channel is inert in the certified regime: Str and Grad make every
  choice, and rho_star's value is undocumented because nothing depends on it.

  If the measured quantities move when rho_star reaches a REACHABLE value
  (1.0), then 0.5 is a substantive, undocumented choice -- it puts the target
  exactly halfway between the two commonest densities, which is the most
  unreachable place it could sit.
""")


if __name__ == "__main__":
    main()
