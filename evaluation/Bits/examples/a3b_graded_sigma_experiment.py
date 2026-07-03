"""A3b -- the follow-on the A3 sweep named: does severance become GRADED once bandwidth is
actually wired into the dynamics, or does it stay a hard threshold even then?

A3 found that the certified rule's bandwidth field is dynamically inert: compute_sigma never
reads it, and admissible_neighbors only checks the binary decoupled flag. Bandwidth only enters
at apply_tiebreak, and only as a tie-break key for EXACTLY-tied Sigma values -- a narrow edge
case, not a graded weighting.

This is an EXPERIMENTAL, NOT-CERTIFIED extension -- it does not touch or replace the certified
simulator (graph.py / sigma.py / update.py are untouched and remain the source of truth for
every other result in this project). It defines a parallel graded-Sigma variant:

    Sigma_graded(u, v) = bandwidth(u, v) * Sigma_certified(u, v)

the most natural, minimal way to make bandwidth a genuine multiplicative gain on the
coherence-driving signal for a channel: a low-bandwidth channel is proportionally LESS
attractive to commit across, not structurally forbidden, so as bandwidth -> 0 the channel should
be chosen less and less often (unless it's the only admissible candidate), giving a real,
continuous route to severance instead of the certified rule's all-or-nothing decoupled flag.

Reruns the exact same chain-topology reach-grading test A3 ran, swapping only the Sigma function,
to see whether M2 (across-boundary information) now trends toward the shuffle floor continuously
as bridge bandwidth drops, or whether it still snaps sharply rather than fading in.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from simulator import ParticipationGraph, NodeState, StateVector, SigmaCoeffs, assign_stratum_ids  # noqa: E402
from simulator.sigma import compute_sigma, compute_candidates  # noqa: E402
from analysis.delta import compute_all  # noqa: E402

S = 32
N_ENSEMBLE = 150
BW = 0.5
COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5, extinction_threshold=-2.0)


# ---------- experimental graded-Sigma update loop (parallel to update.py, NOT certified) ----------

def compute_sigma_graded(u, v, state, graph, coeffs):
    """Sigma_graded = bandwidth * Sigma_certified -- bandwidth as a genuine multiplicative gain,
    not a tie-break-only field. The certified compute_sigma is reused UNCHANGED underneath."""
    return graph.bw(u, v) * compute_sigma(u, v, state, graph, coeffs)


def apply_tiebreak_graded(u, candidates, graph):
    return max(candidates, key=lambda v: (graph.bw(u, v), v))


def apply_update_graded(u, state, graph, coeffs):
    cands = compute_candidates(u, state, graph)
    if not cands:
        state[u].active = False
        return None
    sig = {v: compute_sigma_graded(u, v, state, graph, coeffs) for v in cands}
    smax = max(sig.values())
    if coeffs.extinction_threshold is not None and smax <= coeffs.extinction_threshold:
        state[u].active = False
        return None
    maximal = [v for v, s in sig.items() if s == smax]
    winner = apply_tiebreak_graded(u, maximal, graph)
    transverse = state[u].orientation[1:].copy()
    state[winner].commit(coeffs.increment, longitudinal=float(winner), transverse=transverse)
    state[u].active = False
    state[winner].active = True
    return winner


def step_graded(state, graph, coeffs, strata=None):
    def sid(u):
        return strata.get(u, state.stratum_id(u)) if strata is not None else state.stratum_id(u)
    order = sorted(state.active_nodes(), key=lambda u: (sid(u), u))
    newly_active = set()
    commits = 0
    for u in order:
        if u in newly_active or not state.is_active(u):
            continue
        v = apply_update_graded(u, state, graph, coeffs)
        if v is not None:
            commits += 1
            newly_active.add(v)
    return commits


# ---------- same chain-plus-graded-bridge construction as A3 ----------

def build_chain_graded_bridge(S, bridge_bw, bw=BW):
    g = ParticipationGraph()
    A = list(range(S))
    B = list(range(S, 2 * S))
    for chain in (A, B):
        for i in range(len(chain) - 1):
            g.add_edge(chain[i], chain[i + 1], bandwidth=bw)
    g.add_edge(A[-1], B[0], bandwidth=bridge_bw, decoupled=False)
    half = S // 2
    return g, A, B, A[:half], A[half:]


def run_one(graph, seed_a, seed_b, coeffs, max_steps, seed_nodes):
    sv = StateVector()
    rng_a = np.random.default_rng(seed_a)
    rng_b = np.random.default_rng(seed_b)
    nodes = list(graph.nodes())
    half = len(nodes) // 2
    for n in nodes[:half]:
        sv[n] = NodeState(rho=float(rng_a.uniform(0.0, 0.5)), orientation=rng_a.normal(size=2))
    for n in nodes[half:]:
        sv[n] = NodeState(rho=float(rng_b.uniform(0.0, 0.5)), orientation=rng_b.normal(size=2))
    for n in seed_nodes:
        sv[n].active = True
    strata = assign_stratum_ids(sv, graph)
    steps = 0
    for t in range(1, max_steps + 1):
        c = step_graded(sv, graph, coeffs, strata=strata)
        steps = t
        if c == 0:
            break
    return sv, steps, (steps < max_steps)


def measure(bridge_bw, N=N_ENSEMBLE, max_steps=1200):
    g, A, B, A_left, A_right = build_chain_graded_bridge(S, bridge_bw)
    seed_nodes = [A[0], B[0]]
    A_s, B_s, AL_s, AR_s = [], [], [], []
    natural = 0
    for k in range(N):
        sv, steps, term = run_one(g, 1000 + k, 5000 + k, COEFFS, max_steps, seed_nodes)
        natural += int(term)
        A_s.append(sum(sv[n].rho for n in A))
        B_s.append(sum(sv[n].rho for n in B))
        AL_s.append(sum(sv[n].rho for n in A_left))
        AR_s.append(sum(sv[n].rho for n in A_right))
    ds = {"A": np.array(A_s), "B": np.array(B_s),
          "A_left": np.array(AL_s), "A_right": np.array(AR_s)}
    d = compute_all(ds)
    d["natural_fraction"] = natural / N
    return d


def main():
    print("=" * 88)
    print("A3b — GRADED-SIGMA experiment: does wiring bandwidth into Sigma make severance continuous?")
    print("  (experimental, NOT the certified rule -- Sigma_graded = bandwidth * Sigma_certified)")
    print("=" * 88)

    bws = [0.5, 0.25, 0.10, 0.05, 0.01, 0.005, 0.001, 0.0001]
    rows = []
    print(f"\n  {'bridge_bw':>10} {'M1':>10} {'M2':>10} {'M3':>10} {'Delta':>10} {'nat%':>6}")
    print("  " + "-" * 60)
    for bw in bws:
        d = measure(bw)
        rows.append((bw, d))
        print(f"  {bw:>10.4f} {d['M1_bits']:>+10.4f} {d['M2_bits']:>+10.4f} "
              f"{d['M3_bits']:>+10.4f} {d['delta_bits']:>+10.4f} {d['natural_fraction']*100:>5.0f}%")

    m2s = [d["M2_bits"] for _, d in rows]
    print("\n  READ: does M2 trend DOWN toward the shuffle floor (M3, ~0) as bridge_bw shrinks")
    print("  (a real, graded route to severance), or does it stay flat/erratic (severance still")
    print("  effectively hard even with bandwidth wired in as a Sigma-scaling gain)?")
    trend = "TRENDS TOWARD SEVERANCE" if m2s[-1] < m2s[0] - 0.05 else "FLAT / NO CLEAR TREND"
    print(f"\n  M2 at bw={bws[0]}: {m2s[0]:+.4f}   M2 at bw={bws[-1]}: {m2s[-1]:+.4f}   -> {trend}")

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sweep_output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "a3b_graded_sigma.json"), "w", encoding="utf-8") as fh:
        json.dump({"bws": bws, "M2": m2s, "trend": trend}, fh, indent=2)
    print("=" * 88)


if __name__ == "__main__":
    main()
