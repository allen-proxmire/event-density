"""P12 phase-coherence probe on the CERTIFIED Sigma-rule substrate.

Tests whether a finite-reach P09-phase coherence term added to Sigma:
  (a) rewards phase alignment (order emerges from the deposition), and
  (b) stays FINITE-REACH (C(r) decays -> Knots-safe) vs producing long-range
      order (C(r) -> const -> a forbidden crystal).

Faithful to the certified rule: the rho-dynamics use the certified decision
functions verbatim (compute_sigma / compute_candidates / apply_tiebreak /
NodeState.commit). We ADD a phase channel pi in [0,2pi) and, at each node's
FIRST commit, deposit the phase that MAXIMIZES the finite-reach coherence term
  Coh_phase(v) = sum_{w committed, |v-w|<=reach} k(|v-w|) cos(pi_v - pi_w)
whose maximizer over pi_v is the mean-field angle. That IS Sigma-maximization
of the phase term (a polarity-extended rule, per tension_polarity.md:154).
rho is never touched by the phase channel, so the certified rho-dynamics are
unchanged (test (c) holds by construction).
"""
import sys, math, cmath
import numpy as np

SIM = r"C:/Users/allen/GitHub/event-density/evaluation/Bits"
sys.path.insert(0, SIM)
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,
                       compute_sigma, compute_candidates, apply_tiebreak)


def build_grid(L):
    g = ParticipationGraph()
    nid = lambda r, c: r * L + c
    for r in range(L):
        for c in range(L):
            g.add_node(nid(r, c))
    for r in range(L):
        for c in range(L):
            if c + 1 < L: g.add_edge(nid(r, c), nid(r, c + 1), 1.0)
            if r + 1 < L: g.add_edge(nid(r, c), nid(r + 1, c), 1.0)
    coords = np.array([(i // L, i % L) for i in range(L * L)], dtype=float)
    return g, coords, nid


def run_fill(L, n_seeds, reach, sigma_noise, rng, max_commits_factor=6):
    """Run certified front dynamics from n_seeds; deposit coherence-max phase at
    each node's first commit. Returns phase (NaN=uncommitted), committed mask."""
    g, coords, nid = build_grid(L)
    N = L * L
    state = StateVector({i: NodeState() for i in range(N)})
    coeffs = SigmaCoeffs()  # certified defaults
    phase = np.full(N, np.nan)
    committed = np.zeros(N, dtype=bool)
    # committed-node bookkeeping for fast reach lookup
    comm_coords = []   # list of (r,c)
    comm_phase = []    # parallel phases

    def deposit_phase(v):
        r0, c0 = coords[v]
        acc = 0j
        rr = int(math.ceil(reach))
        for w_i, (rw, cw) in enumerate(comm_coords):
            if abs(rw - r0) > rr or abs(cw - c0) > rr:
                continue
            d = math.hypot(rw - r0, cw - c0)
            if d <= reach and d > 0:
                acc += math.exp(-d / max(reach, 1e-9)) * cmath.exp(1j * comm_phase[w_i])
        if abs(acc) < 1e-12:
            ang = rng.uniform(0, 2 * math.pi)          # nucleation: no neighbors
        else:
            ang = math.atan2(acc.imag, acc.real)
        if sigma_noise > 0:
            ang += rng.normal(0, sigma_noise)
        ang %= (2 * math.pi)
        phase[v] = ang
        committed[v] = True
        comm_coords.append((r0, c0)); comm_phase.append(ang)

    # seed
    seeds = rng.choice(N, size=n_seeds, replace=False)
    active = set()
    for s in seeds:
        state[int(s)].commit(coeffs.increment)
        state[int(s)].active = True
        deposit_phase(int(s))
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
            sig = {v: compute_sigma(u, v, state, g, coeffs) for v in cands}
            smax = max(sig.values())
            winner = apply_tiebreak(u, [v for v, s in sig.items() if s == smax], g)
            first = not committed[winner]
            state[winner].commit(coeffs.increment)          # certified rho writer
            if first:
                deposit_phase(winner)
            state[u].active = False
            state[winner].active = True
            active.add(winner)
            commits += 1
    return phase, committed, coords


def global_order(phase, committed):
    p = phase[committed]
    return abs(np.mean(np.exp(1j * p)))          # ~1 aligned, ~1/sqrt(N) random


def corr_vs_r(phase, committed, coords, rng, n_pairs=300000, rmax=None):
    idx = np.where(committed)[0]
    if rmax is None: rmax = 30
    a = rng.choice(idx, size=n_pairs); b = rng.choice(idx, size=n_pairs)
    d = np.hypot(coords[a, 0] - coords[b, 0], coords[a, 1] - coords[b, 1])
    dc = np.cos(phase[a] - phase[b])
    rbin = np.round(d).astype(int)
    out = {}
    for r in range(1, rmax + 1):
        m = rbin == r
        if m.sum() > 50:
            out[r] = float(np.mean(dc[m]))
    return out


def summarize(tag, phase, committed, coords, rng):
    R = global_order(phase, committed)
    C = corr_vs_r(phase, committed, coords, rng)
    # surrogate null: shuffle phases among committed
    ps = phase.copy()
    idx = np.where(committed)[0]
    ps[idx] = rng.permutation(ps[idx])
    Cs = corr_vs_r(ps, committed, coords, rng)
    print(f"\n=== {tag} ===  committed={committed.sum()}  R_global={R:.3f}")
    rs = [1, 2, 3, 5, 8, 12, 18, 25]
    print("  r      C(r)     surrogate")
    for r in rs:
        if r in C:
            print(f"  {r:<5} {C[r]:+.3f}    {Cs.get(r, float('nan')):+.3f}")
    return R, C


def main():
    L = 60
    rng = np.random.default_rng(7)
    print(f"Grid {L}x{L} = {L*L} nodes. Certified rho-dynamics; phase channel added.")

    # (1) SINGLE seed, pure coherence-max deposit, reach sweep -> intrinsic reach test
    for reach in (1.0, 3.0):
        phase, committed, coords = run_fill(L, n_seeds=1, reach=reach, sigma_noise=0.0, rng=rng)
        summarize(f"single-seed  reach={reach}  noise=0", phase, committed, coords, rng)

    # (2) MANY seeds (domains), reach sweep
    for reach in (1.0, 3.0):
        phase, committed, coords = run_fill(L, n_seeds=40, reach=reach, sigma_noise=0.0, rng=rng)
        summarize(f"multi-seed40 reach={reach}  noise=0", phase, committed, coords, rng)

    # (3) single seed WITH deposition noise (order-disorder knob)
    for nz in (0.3, 0.8):
        phase, committed, coords = run_fill(L, n_seeds=1, reach=3.0, sigma_noise=nz, rng=rng)
        summarize(f"single-seed  reach=3  noise={nz}", phase, committed, coords, rng)

    # (4) CONTROL: no coherence (random phases, not deposited by alignment)
    phase, committed, coords = run_fill(L, n_seeds=1, reach=3.0, sigma_noise=1e9, rng=rng)
    summarize("CONTROL random-phase (coherence off)", phase, committed, coords, rng)


if __name__ == "__main__":
    main()
