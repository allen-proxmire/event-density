"""P12 phase-coherence probe v2 — INTRINSIC-DISORDER variant.

Step-2 found: a pure mean-field phase deposit CRYSTALLIZES from a single seed
(long-range order, forbidden). Step-3 question: does the substrate's OWN
disorder break the crystal WITHOUT imposed thermal noise or imposed
multi-seeding?

Mechanism (ED-native): P05 transports phase across an edge with a CONNECTION
(holonomy). Tie that connection to the substrate's intrinsic heterogeneity:
  A(w->v) = kappa * (bw(w,v) - 1)          [quenched bandwidth disorder], or
  A(w->v) = kappa_rho * (rho_w - rho_v)    [the substrate's own rho-field].
Deposit at v's first commit = mean-field angle of {phase[w] + A(w->v)} over
committed edge-neighbors w. Quenched-disordered A => phase random-walks along
paths => finite correlation length, from intrinsic substrate disorder alone.
NO thermal noise, single seed. kappa=0 recovers the pure-copy crystal.

rho-dynamics are the certified rule verbatim (winner-selection unchanged).
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
        return 1.0 + bw_disorder * (2 * rng.random() - 1.0)  # U[1-d, 1+d]
    for r in range(L):
        for c in range(L):
            if c + 1 < L: g.add_edge(nid(r, c), nid(r, c + 1), bw())
            if r + 1 < L: g.add_edge(nid(r, c), nid(r + 1, c), bw())
    coords = np.array([(i // L, i % L) for i in range(L * L)], dtype=float)
    return g, coords, nid


def run_fill(L, bw_disorder, kappa_bw, kappa_rho, rng, n_seeds=1, max_commits_factor=6):
    g, coords, nid = build_grid(L, bw_disorder, rng)
    N = L * L
    state = StateVector({i: NodeState() for i in range(N)})
    coeffs = SigmaCoeffs()
    phase = np.full(N, np.nan)
    committed = np.zeros(N, dtype=bool)

    def deposit(v):
        acc = 0j
        for w in g.neighbors(v):                       # edge-adjacent only (reach=1)
            if committed[w]:
                A = kappa_bw * (g.bw(w, v) - 1.0) + kappa_rho * (state[w].rho - state[v].rho)
                acc += cmath.exp(1j * (phase[w] + A))
        ang = rng.uniform(0, 2*math.pi) if abs(acc) < 1e-12 else math.atan2(acc.imag, acc.real)
        phase[v] = ang % (2*math.pi)
        committed[v] = True

    seeds = rng.choice(N, size=n_seeds, replace=False)
    active = set()
    for s in seeds:
        state[int(s)].commit(coeffs.increment); state[int(s)].active = True
        deposit(int(s)); active.add(int(s))

    max_commits = max_commits_factor * N; commits = 0
    while active and commits < max_commits and committed.sum() < N:
        order = sorted(active); active = set()
        for u in order:
            if not state[u].active: continue
            cands = compute_candidates(u, state, g)
            if not cands:
                state[u].active = False; continue
            sig = {v: compute_sigma(u, v, state, g, coeffs) for v in cands}
            smax = max(sig.values())
            winner = apply_tiebreak(u, [v for v, s in sig.items() if s == smax], g)
            first = not committed[winner]
            state[winner].commit(coeffs.increment)
            if first: deposit(winner)
            state[u].active = False; state[winner].active = True; active.add(winner)
            commits += 1
    return phase, committed, coords


def global_order(phase, committed):
    return abs(np.mean(np.exp(1j * phase[committed])))


def corr_vs_r(phase, committed, coords, rng, n_pairs=300000, rmax=30):
    idx = np.where(committed)[0]
    a = rng.choice(idx, n_pairs); b = rng.choice(idx, n_pairs)
    d = np.hypot(coords[a,0]-coords[b,0], coords[a,1]-coords[b,1])
    dc = np.cos(phase[a]-phase[b]); rb = np.round(d).astype(int)
    out = {}
    for r in range(1, rmax+1):
        m = rb == r
        if m.sum() > 50: out[r] = float(np.mean(dc[m]))
    return out


def summarize(tag, phase, committed, coords, rng):
    R = global_order(phase, committed); C = corr_vs_r(phase, committed, coords, rng)
    print(f"\n=== {tag} ===  committed={committed.sum()}  R_global={R:.3f}")
    print("  r:   " + "  ".join(f"{r}={C.get(r, float('nan')):+.2f}" for r in [1,2,3,5,8,12,18,25]))
    return R, C


def main():
    L = 60; rng = np.random.default_rng(11)
    print(f"Grid {L}x{L}. SINGLE seed, NO thermal noise. Certified rho-dynamics.")
    print("Testing: does intrinsic substrate disorder (bandwidth heterogeneity /")
    print("rho-field) via a P05 connection break the single-seed crystal?\n")

    # baseline: pure copy, homogeneous -> crystal
    p,c,co = run_fill(L, bw_disorder=0.0, kappa_bw=0.0, kappa_rho=0.0, rng=rng)
    summarize("BASELINE homogeneous, kappa=0 (pure copy)", p,c,co, rng)

    # (A) quenched BANDWIDTH disorder via P05 connection, sweep kappa
    for bd, kb in [(0.5, 0.5), (0.5, 1.0), (0.5, 2.0), (0.9, 1.0)]:
        p,c,co = run_fill(L, bw_disorder=bd, kappa_bw=kb, kappa_rho=0.0, rng=rng)
        summarize(f"bandwidth-holonomy  bw_disorder={bd}  kappa_bw={kb}", p,c,co, rng)

    # (B) purest intrinsic: homogeneous grid, rho-field holonomy only
    for kr in [0.5, 1.0, 2.0]:
        p,c,co = run_fill(L, bw_disorder=0.0, kappa_bw=0.0, kappa_rho=kr, rng=rng)
        summarize(f"rho-holonomy (homogeneous grid)  kappa_rho={kr}", p,c,co, rng)


if __name__ == "__main__":
    main()
