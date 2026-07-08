"""P12 phase-coherence probe v3 — WINNER-SELECTION-ACTIVE variant (Step 1).

v2 (intrinsic disorder) result: with a P05 holonomy tied to substrate disorder,
a phase-rewarding Coh deposits FINITE-REACH order (no crystal). BUT there the
phase was PASSIVE: it was painted on AFTER the certified rho-rule chose the
winner. The phase never decided who commits. So v2 shows the sign is *permitted*,
not that the substrate *acts on* it.

Step 1 makes the phase CAUSAL. The coherence content of the participation
superposition at a candidate site v is its phase-resultant magnitude,
    C(v) = | sum_{w committed nbr} exp( i( phase[w] + A(w->v) ) ) | / n_committed ,
maximal (=1) when the incoming phase votes agree, ~0 when they conflict. We add
this to the sigma used for winner selection:
    sigma_total(u,v) = compute_sigma(u,v)      [certified rho-rule, verbatim]
                     + k_phase * C(v)           [phase now decides the winner]
so the front dynamically PREFERS to grow into coherent sites. k_phase=0 recovers
v2 exactly (passive). Matched pairs (same seed/grid/kappa, k_phase 0 vs >0)
isolate the effect of making phase causal.

Two questions:
  (a) Does active selection actually change growth / strengthen alignment vs
      passive? (diagnostic: flip_frac = fraction of commits where the phase term
      changes the winner vs the certified-only choice.)
  (b) Does finite-reach SURVIVE when phase is causally self-reinforcing, or does
      active selection tip intrinsic-disorder order into a CRYSTAL (a real
      limitation: Knots-safe only while phase is passive)? Sweep k_phase; look
      for an order/disorder threshold.

HONEST SCOPE: this is a MORE-extended rule than v2 (phase enters selection, not
just deposition). The certified rho-sigma is still computed verbatim and enters
additively; the phase term is a named, weighted extension, NOT the certified
rule. No certified result is altered; this asks what the extension does.

Single seed, NO thermal noise. rho via certified commit. Home of the arc:
theory/P12_Coherence_PhaseAlignment_Scoping.md .
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


def run_fill(L, bw_disorder, kappa_bw, kappa_rho, k_phase, rng,
             n_seeds=1, max_commits_factor=6):
    g, coords, nid = build_grid(L, bw_disorder, rng)
    N = L * L
    state = StateVector({i: NodeState() for i in range(N)})
    coeffs = SigmaCoeffs()
    phase = np.full(N, np.nan)
    committed = np.zeros(N, dtype=bool)

    def holo_acc(v):
        """resultant of committed edge-neighbors' phases, holonomy-transported."""
        acc = 0j; n = 0
        for w in g.neighbors(v):
            if committed[w]:
                A = kappa_bw * (g.bw(w, v) - 1.0) + kappa_rho * (state[w].rho - state[v].rho)
                acc += cmath.exp(1j * (phase[w] + A)); n += 1
        return acc, n

    def coherence_bonus(v):
        acc, n = holo_acc(v)
        return abs(acc) / n if n else 0.0        # resultant magnitude in [0,1]

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
            # certified-only winner (what v2 would pick) — for the flip diagnostic
            bmax = max(base.values())
            cert_winner = apply_tiebreak(u, [v for v, s in base.items() if s == bmax], g)
            # phase-augmented winner (active rule)
            if k_phase:
                tot = {v: base[v] + k_phase * coherence_bonus(v) for v in cands}
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


def xi_estimate(C):
    """crude corr length: first r where C(r) drops below 1/e, linear-interp."""
    rs = sorted(C); thr = 1/math.e
    prev_r, prev_c = 0, 1.0
    for r in rs:
        c = C[r]
        if c < thr:
            if prev_c == c: return float(r)
            return prev_r + (prev_c - thr) / (prev_c - c) * (r - prev_r)
        prev_r, prev_c = r, c
    return float(max(rs)) if rs else float('nan')


def summarize(tag, phase, committed, coords, flip_frac, rng):
    R = global_order(phase, committed); C = corr_vs_r(phase, committed, coords, rng)
    xi = xi_estimate(C)
    print(f"\n=== {tag} ===  committed={committed.sum()}  R_global={R:.3f}  xi~{xi:.1f}  flip_frac={flip_frac:.3f}")
    print("  r:   " + "  ".join(f"{r}={C.get(r, float('nan')):+.2f}" for r in [1,2,3,5,8,12,18,25]))
    return R, C, xi


def main():
    L = 64; seed = 11
    print(f"Grid {L}x{L}. SINGLE seed, NO thermal noise. Certified rho-sigma + k_phase*coherence.")
    print("STEP 1: phase now DECIDES the winner. Does active selection preserve finite-reach,")
    print("or does self-reinforcement crystallize? k_phase=0 == v2 (passive) baseline.\n")

    def fresh(): return np.random.default_rng(seed)  # same stream per condition -> matched pairs

    print("################ CONTROL: no intrinsic disorder (homogeneous, pure copy) ################")
    for kp in [0.0, 1.0, 4.0]:
        p,c,co,ff = run_fill(L, 0.0, 0.0, 0.0, kp, fresh())
        summarize(f"homogeneous kappa=0  k_phase={kp}", p,c,co,ff, fresh())

    print("\n################ (A) BANDWIDTH holonomy, bw_disorder=0.5, kappa_bw=0.5 ################")
    print("################     passive baseline vs active selection, sweep k_phase        ################")
    for kp in [0.0, 0.5, 1.0, 2.0, 4.0, 8.0]:
        p,c,co,ff = run_fill(L, 0.5, 0.5, 0.0, kp, fresh())
        summarize(f"bw-holonomy kappa_bw=0.5  k_phase={kp}", p,c,co,ff, fresh())

    print("\n################ (B) RHO holonomy (homogeneous grid), kappa_rho=0.5 ################")
    for kp in [0.0, 1.0, 2.0, 4.0]:
        p,c,co,ff = run_fill(L, 0.0, 0.0, 0.5, kp, fresh())
        summarize(f"rho-holonomy kappa_rho=0.5  k_phase={kp}", p,c,co,ff, fresh())


if __name__ == "__main__":
    main()
