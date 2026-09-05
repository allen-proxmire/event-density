"""P12 phase-in-GRAD probe — does the finite-reach result survive when the phase
term is assigned to Grad rather than to Coh?  (2026-09-05)

WHY THIS EXISTS
---------------
The 2026-09-05 sign check (foundations/Note_SigmaC_SignCheck_2026-09-05.md)
settled the P12 split from Paper_030's established a = a_N + sqrt(a_N a_0):

    Str_K = sum_a b_K^(a)                            the diagonal   (intra-locus)
    Coh_K = 2 sum_{a<b} sqrt(b_a b_b) cos Theta_ab   the off-diagonal (intra-locus)

That leaves Grad as the only INTER-locus term, and the proposal
(foundations/Note_Grad_Proposal_2026-09-05.md) is the discrete Dirichlet form

    Grad = sum_K sum_<u,v> |P_K(v) - P_K(u)|^2
         = sum [ b(v) + b(u) - 2 sqrt(b(v) b(u)) cos(dphi) ]

Sigma_C carries -Grad, so its phase part enters Sigma_C as
    + 2 sum_w sqrt(b_v b_w) cos(phi_v - phi_w - A_w)
i.e. alignment ACROSS AN EDGE is rewarded.

But that is what v3_active's probe already measures: it deposits phase from
COMMITTED NEIGHBOURS through the P05 connection.  So the measured finite-reach
result may belong to Grad, not Coh.  This probe asks whether it survives the
reassignment.

THE ONE SUBSTANTIVE DIFFERENCE
------------------------------
Write acc(v) = sum_{w committed nbr} exp(i(phi_w + A(w->v))).

  v3_active (Coh reading, INTENSIVE):   bonus = |acc| / n     in [0,1]
      a per-locus average: "do the incoming votes agree with each other?"

  this probe (Grad reading, EXTENSIVE): bonus = |acc|         in [0,n]
      an edge sum: every edge contributes, so agreement AND neighbour count
      both raise it.

Maximising over the candidate's own (not-yet-assigned) phase gives exactly
2|acc| for the Dirichlet form with b ~ 1; the 2 is absorbable into k_phase, so
the substantive difference is precisely the /n normalisation -- which is what
distinguishes an edge sum from a per-locus average.  The deposit rule is
unchanged: setting phi_v to the resultant angle is already the Dirichlet-optimal
choice, so only SELECTION differs.

HONEST SCOPE: same as v3_active.  The certified rho-sigma is computed verbatim
and enters additively; the phase term is a named, weighted extension, not the
certified rule.  Single seed, no thermal noise.  Matched seeds across conditions.

Run: python theory/p12_phase_in_grad_probe.py
Home of the arc: theory/P12_Coherence_PhaseAlignment_Scoping.md
"""
import sys, math, cmath
import numpy as np

SIM = r"C:/Users/allen/GitHub/event-density/evaluation/Bits"
sys.path.insert(0, SIM)
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,
                       compute_sigma, compute_candidates, apply_tiebreak)


def build_grid(L, bw_disorder, rng):
    g = ParticipationGraph()
    nid = lambda r, c: r * L + c
    for i in range(L * L):
        g.add_node(i)
    def bw():
        return 1.0 + bw_disorder * (2 * rng.random() - 1.0)
    for r in range(L):
        for c in range(L):
            if c + 1 < L: g.add_edge(nid(r, c), nid(r, c + 1), bw())
            if r + 1 < L: g.add_edge(nid(r, c), nid(r + 1, c), bw())
    coords = np.array([(i // L, i % L) for i in range(L * L)], dtype=float)
    return g, coords, nid


def run_fill(L, bw_disorder, kappa_bw, kappa_rho, k_phase, rng,
             mode="grad", n_seeds=1, max_commits_factor=6):
    """mode='coh'  -> |acc|/n   (v3_active, intensive, per-locus average)
       mode='grad' -> |acc|     (Dirichlet, extensive, edge sum)"""
    g, coords, nid = build_grid(L, bw_disorder, rng)
    N = L * L
    state = StateVector({i: NodeState() for i in range(N)})
    coeffs = SigmaCoeffs()
    phase = np.full(N, np.nan)
    committed = np.zeros(N, dtype=bool)

    def holo_acc(v):
        acc = 0j; n = 0
        for w in g.neighbors(v):
            if committed[w]:
                A = kappa_bw * (g.bw(w, v) - 1.0) + kappa_rho * (state[w].rho - state[v].rho)
                acc += cmath.exp(1j * (phase[w] + A)); n += 1
        return acc, n

    def phase_bonus(v):
        acc, n = holo_acc(v)
        if not n:
            return 0.0
        return abs(acc) if mode == "grad" else abs(acc) / n

    def deposit(v):
        acc, n = holo_acc(v)
        ang = rng.uniform(0, 2*math.pi) if abs(acc) < 1e-12 else math.atan2(acc.imag, acc.real)
        phase[v] = ang % (2*math.pi)
        committed[v] = True

    seeds = rng.choice(N, size=n_seeds, replace=False)
    active = set()
    for s in seeds:
        state[int(s)].commit(coeffs.increment); state[int(s)].active = True
        deposit(int(s)); active.add(int(s))

    max_commits = max_commits_factor * N; commits = 0; flips = 0; decisions = 0
    while active and commits < max_commits and committed.sum() < N:
        order = sorted(active); active = set()
        for u in order:
            if not state[u].active: continue
            cands = compute_candidates(u, state, g)
            if not cands:
                state[u].active = False; continue
            base = {v: compute_sigma(u, v, state, g, coeffs) for v in cands}
            bmax = max(base.values())
            cert_winner = apply_tiebreak(u, [v for v, s in base.items() if s == bmax], g)
            if k_phase:
                tot = {v: base[v] + k_phase * phase_bonus(v) for v in cands}
            else:
                tot = base
            tmax = max(tot.values())
            winner = apply_tiebreak(u, [v for v, s in tot.items() if s == tmax], g)
            decisions += 1
            if winner != cert_winner: flips += 1
            first = not committed[winner]
            state[winner].commit(coeffs.increment)
            if first: deposit(winner)
            state[u].active = False; state[winner].active = True; active.add(winner)
            commits += 1
    flip_frac = flips / decisions if decisions else 0.0
    return phase, committed, coords, flip_frac


def global_order(phase, committed):
    return abs(np.mean(np.exp(1j * phase[committed])))


def corr_vs_r(phase, committed, coords, rng, n_pairs=200000, rmax=30):
    idx = np.where(committed)[0]
    a = rng.choice(idx, n_pairs); b = rng.choice(idx, n_pairs)
    d = np.hypot(coords[a,0]-coords[b,0], coords[a,1]-coords[b,1])
    dc = np.cos(phase[a]-phase[b]); rb = np.round(d).astype(int)
    out = {}
    for r in range(1, rmax+1):
        m = rb == r
        if m.sum() > 50: out[r] = float(np.mean(dc[m]))
    return out


def xi_estimate(C):
    rs = sorted(C); thr = 1/math.e
    prev_r, prev_c = 0, 1.0
    for r in rs:
        c = C[r]
        if c < thr:
            if prev_c == c: return float(r)
            return prev_r + (prev_c - thr) / (prev_c - c) * (r - prev_r)
        prev_r, prev_c = r, c
    return float(max(rs)) if rs else float('nan')


def row(tag, phase, committed, coords, flip_frac, rng):
    R = global_order(phase, committed); C = corr_vs_r(phase, committed, coords, rng)
    xi = xi_estimate(C)
    verdict = "CRYSTAL" if (R > 0.8 and xi > 15) else "finite-reach"
    print("  %-34s R=%.3f  xi=%5.1f  flip=%.3f   %s"
          % (tag, R, xi, flip_frac, verdict))
    return R, xi


def main():
    L, seed = 64, 11
    fresh = lambda: np.random.default_rng(seed)   # matched stream per condition
    print("P12 phase-in-Grad probe. Grid %dx%d, single seed, no thermal noise." % (L, L))
    print("Question: does finite-reach survive when the phase term is assigned to")
    print("Grad (extensive edge sum, |acc|) rather than Coh (intensive, |acc|/n)?\n")

    conds = [
        ("CONTROL homogeneous (kappa=0)", 0.0, 0.0, 0.0),
        ("(A) bandwidth holonomy kbw=0.5", 0.5, 0.5, 0.0),
        ("(C) physical: bw + rho holonomy", 0.5, 0.5, 0.5),
    ]
    for name, bwd, kbw, krho in conds:
        print("#" * 78)
        print("### " + name)
        for mode in ("coh", "grad"):
            label = "Coh  |acc|/n " if mode == "coh" else "Grad |acc|   "
            print("  --- %s ---" % label)
            for kp in [0.0, 0.5, 1.0, 2.0, 4.0, 8.0]:
                p, c, co, ff = run_fill(L, bwd, kbw, krho, kp, fresh(), mode=mode)
                row("k_phase=%.1f" % kp, p, c, co, ff, fresh())
        print()


if __name__ == "__main__":
    main()
