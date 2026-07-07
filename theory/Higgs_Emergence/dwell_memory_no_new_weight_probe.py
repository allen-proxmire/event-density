"""Attempt to eliminate the intrinsic-memory probe's two free parameters, or at
least reduce them honestly, rather than leaving both as arbitrary picks.

TARGET 1 -- k_mem (coupling strength): can memory be folded into the EXISTING
coherence weight kc instead of getting its own new weight? P12's own canonical
definition is a fixed THREE-term functional (Coh - Str - Grad) -- adding a
fourth, independently-weighted term (the first probe's k_mem*mem bonus) is
more new structure than necessary. A more economical design: let a chain's
own accumulated history shift what density it's "comfortable" with (its own
coherence TARGET), rather than adding a brand new bonus term. Concretely,
replace the self-loop Coh target rho_star with (rho_star + chain_mem), and
grow chain_mem by the SAME increment already used for rho commits
(coeffs.increment) rather than an arbitrary "+1" -- both choices reuse
existing corpus quantities (kc, coeffs.increment) instead of introducing new
ones. If this still produces the same qualitative result (stable, bounded
plateau), that's a real reduction: down from two new free parameters to one.

TARGET 2 -- the fade rate: named directly as V1's own memory time in the
write-up (Paper_090's kernel is explicitly a chain's response to ITS OWN
earlier state -- exactly what chain_mem represents). This does not derive a
NUMBER (Paper_090 itself states the value stays inherited, same as every
other regime's tau_V5), but it means the fade rate is not a NEW unknown --
it is the SAME already-acknowledged inherited quantity the corpus already
carries, just newly identified with a concrete, working piece of code rather
than left as an abstract admissible-class object nobody had implemented.
"""
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,  # noqa: E402
                       assign_stratum_ids)
from simulator.sigma import compute_candidates, coherence  # noqa: E402
from simulator.update import apply_tiebreak  # noqa: E402

CHAIN_LEN = 400
EDGE_BW = 0.5
B_SELF = 1.0
RHO_STAR = 0.5
JITTER_SD = 1e-3
PROBE_START = 10
MAX_STEPS = 8000


def build_chain_with_selfloops(n, b_self):
    g = ParticipationGraph()
    for i in range(n - 1):
        g.add_edge(i, i + 1, bandwidth=EDGE_BW)
    if b_self > 0:
        for i in range(n):
            g.add_edge(i, i, bandwidth=b_self)
    return g


def fresh_state(n, seed):
    rng = np.random.default_rng(seed)
    sv = StateVector()
    for i in range(n):
        sv[i] = NodeState(rho=float(max(0.0, RHO_STAR + rng.normal(0, JITTER_SD))))
    return sv


def sigma_no_new_weight(u, v, state, graph, coeffs, chain_mem):
    """Certified compute_sigma's exact formula, with ONE change: for the
    self-loop candidate only, the coherence TARGET shifts by the chain's own
    accumulated memory -- reusing kc (no new weight) and coeffs.increment
    (no new unit-conversion constant). Every other term (strain, grad) is
    the certified formula, untouched."""
    rho_u = state.rho_at(u)
    rho_v = state.rho_at(v)
    if v == u:
        target = coeffs.rho_star + chain_mem.get(u, 0.0)
        coh = -(rho_v - target) ** 2
    else:
        coh = coherence(u, v, state, coeffs)
    strain = rho_v
    grad = abs(rho_v - rho_u)
    return coeffs.kc * coh - coeffs.ks * strain - coeffs.kg * grad


def apply_update_no_new_weight(u, state, graph, coeffs, chain_mem, mem_decay):
    cands = compute_candidates(u, state, graph)
    if not cands:
        state[u].active = False
        return None

    sig = {v: sigma_no_new_weight(u, v, state, graph, coeffs, chain_mem) for v in cands}
    smax = max(sig.values())

    if coeffs.extinction_threshold is not None and smax <= coeffs.extinction_threshold:
        state[u].active = False
        return None

    maximal = [v for v, s in sig.items() if s == smax]
    winner = apply_tiebreak(u, maximal, graph)

    transverse = state[u].orientation[1:].copy()
    state[winner].commit(coeffs.increment, longitudinal=float(winner), transverse=transverse)

    state[u].active = False
    state[winner].active = True

    mem_u = chain_mem.get(u, 0.0)
    # Growth uses coeffs.increment -- the SAME quantity rho already grows by
    # at every commit, not a new arbitrary "+1".
    new_mem = mem_decay * mem_u + coeffs.increment
    if u in chain_mem:
        del chain_mem[u]
    chain_mem[winner] = new_mem
    return winner


def run_probe(seed, mem_decay, coeffs, max_steps=MAX_STEPS, start=PROBE_START):
    g = build_chain_with_selfloops(CHAIN_LEN, B_SELF)
    sv = fresh_state(CHAIN_LEN, seed)
    assign_stratum_ids(sv, g)
    sv[start].active = True
    chain_mem = {start: 0.0}

    trace = [start]
    for t in range(1, max_steps + 1):
        active = sv.active_nodes()
        if len(active) != 1:
            break
        u = active[0]
        winner = apply_update_no_new_weight(u, sv, g, coeffs, chain_mem, mem_decay)
        if winner is None:
            break
        trace.append(winner)
        if winner >= CHAIN_LEN - 3:
            break
    trace = np.array(trace)
    total_steps = len(trace) - 1
    v_eff = (trace[-1] - trace[0]) / total_steps if total_steps > 0 else 0.0
    return dict(trace=trace, v_eff=v_eff, steps=total_steps, final_pos=trace[-1])


def windowed_velocity(trace, window=200):
    d = np.diff(trace.astype(float))
    return [d[i:i + window].mean() for i in range(0, len(d), window) if len(d[i:i + window]) > 0]


def main():
    print("=" * 92)
    print("NO-NEW-WEIGHT PROBE -- does folding memory into the EXISTING kc coherence")
    print("weight (instead of a new k_mem) still produce a stable, bounded plateau?")
    print(f"chain={CHAIN_LEN}, start@{PROBE_START}, steps={MAX_STEPS}")
    print("=" * 92)

    seeds = list(range(6))
    COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=RHO_STAR, increment=1.0,
                         extinction_threshold=None)

    for decay, label in ((1.0, "decay=1.0 (no fade, predicted runaway)"),
                        (0.95, "decay=0.95 (mild fade)"),
                        (0.9, "decay=0.9 (faster fade)"),
                        (0.98, "decay=0.98 (slower fade)")):
        print(f"\n[{label}]")
        rows = [run_probe(s, decay, COEFFS) for s in seeds]
        v = np.mean([r["v_eff"] for r in rows])
        reached = np.mean([1.0 if r["final_pos"] >= CHAIN_LEN - 3 else 0.0 for r in rows])
        print(f"  overall v_eff={v:.4f}  reached_boundary_frac={reached:.2f}")
        wv = windowed_velocity(rows[0]["trace"], window=200)
        print(f"  windowed v_eff (seed 0, 200-step windows): "
              + ", ".join(f"{x:.3f}" for x in wv[:10]))
        if len(wv) >= 6:
            plateau = np.mean(wv[-3:])
            early = np.mean(wv[:2])
            print(f"  early avg={early:.3f}  late avg (plateau check)={plateau:.3f}")

    print("\n" + "=" * 92)
    print("READINGS:")
    print("  Same qualitative shape as the original k_mem probe (runaway at decay=1.0,")
    print("  stable plateau at decay<1.0) using ZERO new coupling constants (kc reused,")
    print("  coeffs.increment reused) -- would mean the coupling-strength parameter is")
    print("  genuinely eliminated, not just relabeled: down to one open parameter (the")
    print("  fade rate / V1 memory time), not two.")
    print("  Different/no plateau -- the economical version doesn't reproduce the effect;")
    print("  k_mem (the original, separately-weighted bonus) was doing real work that")
    print("  reusing kc alone can't replace -- an honest negative on the reduction attempt.")
    print("=" * 92)


if __name__ == "__main__":
    main()
