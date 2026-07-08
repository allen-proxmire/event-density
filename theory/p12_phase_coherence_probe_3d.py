"""P12 phase-coherence probe — 3D HARDENING check.

2D found: intrinsic substrate disorder (P05 connection tied to bandwidth / rho)
breaks the single-seed crystal -> finite-reach. But true long-range order is
EASIER in 3D (XY: quasi-order in 2D, genuine LRO in 3D). So the load-bearing
test: does intrinsic disorder STILL hold the phase-order finite-reach in 3D
(space is 3+1, P06), or does 3D crystallize despite the disorder?

Same certified rho-engine + P09 phase + P05-connection holonomy. 3D lattice,
6-neighbor. Single seed, NO imposed thermal noise.
"""
import sys, math, cmath
import numpy as np

SIM = r"C:/Users/allen/GitHub/event-density/evaluation/Bits"
sys.path.insert(0, SIM)
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,
                       compute_sigma, compute_candidates, apply_tiebreak)


def build_grid3d(L, bw_disorder, rng):
    g = ParticipationGraph()
    nid = lambda i, j, k: (i * L + j) * L + k
    N = L ** 3
    for n in range(N):
        g.add_node(n)
    def bw():
        return 1.0 + bw_disorder * (2 * rng.random() - 1.0)
    for i in range(L):
        for j in range(L):
            for k in range(L):
                if i + 1 < L: g.add_edge(nid(i, j, k), nid(i + 1, j, k), bw())
                if j + 1 < L: g.add_edge(nid(i, j, k), nid(i, j + 1, k), bw())
                if k + 1 < L: g.add_edge(nid(i, j, k), nid(i, j, k + 1), bw())
    coords = np.array([((n // L) // L, (n // L) % L, n % L) for n in range(N)], dtype=float)
    return g, coords


def run_fill(L, bw_disorder, kappa_bw, kappa_rho, rng, n_seeds=1, mcf=8):
    g, coords = build_grid3d(L, bw_disorder, rng)
    N = L ** 3
    state = StateVector({i: NodeState() for i in range(N)})
    coeffs = SigmaCoeffs()
    phase = np.full(N, np.nan); committed = np.zeros(N, dtype=bool)

    def deposit(v):
        acc = 0j
        for w in g.neighbors(v):
            if committed[w]:
                A = kappa_bw * (g.bw(w, v) - 1.0) + kappa_rho * (state[w].rho - state[v].rho)
                acc += cmath.exp(1j * (phase[w] + A))
        ang = rng.uniform(0, 2*math.pi) if abs(acc) < 1e-12 else math.atan2(acc.imag, acc.real)
        phase[v] = ang % (2*math.pi); committed[v] = True

    for s in rng.choice(N, size=n_seeds, replace=False):
        state[int(s)].commit(coeffs.increment); state[int(s)].active = True; deposit(int(s))
    active = set(int(s) for s in np.where(committed)[0])
    max_commits = mcf * N; commits = 0
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


def summarize(tag, phase, committed, coords, rng, rmax=20):
    R = abs(np.mean(np.exp(1j * phase[committed])))
    idx = np.where(committed)[0]
    a = rng.choice(idx, 300000); b = rng.choice(idx, 300000)
    d = np.linalg.norm(coords[a] - coords[b], axis=1)
    dc = np.cos(phase[a] - phase[b]); rb = np.round(d).astype(int)
    C = {r: float(np.mean(dc[rb == r])) for r in range(1, rmax+1) if (rb == r).sum() > 50}
    print(f"\n=== {tag} ===  committed={committed.sum()}/{len(committed)}  R={R:.3f}")
    print("  r:  " + "  ".join(f"{r}={C.get(r, float('nan')):+.2f}" for r in [1,2,3,4,6,9,13,18]))
    return R, C


def main():
    L = 28; rng = np.random.default_rng(23)
    print(f"3D grid {L}^3 = {L**3} nodes. SINGLE seed, NO thermal noise. Certified rho.")
    print("KEY: does 3D crystallize despite intrinsic disorder, or stay finite-reach?\n")

    p,c,co = run_fill(L, 0.0, 0.0, 0.0, rng);  summarize("3D BASELINE kappa=0 (pure copy)", p,c,co, rng)
    for kb in [0.5, 1.0, 2.0, 4.0]:
        p,c,co = run_fill(L, 0.5, kb, 0.0, rng); summarize(f"3D bandwidth-holonomy bw_dis=0.5 kappa_bw={kb}", p,c,co, rng)
    for kr in [0.5, 1.0, 2.0]:
        p,c,co = run_fill(L, 0.0, 0.0, kr, rng); summarize(f"3D rho-holonomy (homog) kappa_rho={kr}", p,c,co, rng)


if __name__ == "__main__":
    main()
