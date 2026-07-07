"""The real-memory test (recommendation #1 from the 2026-07-06 next-steps list):
give a chain a genuine, chain-carried "history" value that the movement rule
actually reads -- not an externally hand-inserted bonus tied to a fixed
reference position (the field-decay probe), and not the trail a chain leaves
behind for OTHERS (Test 1, which found the wrong sign and doesn't touch this
chain's own memory anyway).

WHY THIS IS A DIFFERENT, MORE HONEST TEST. The fourth-pass finding
(V5_Envelope_Shape_From_P11_Scoping.md) established the certified substrate
has exactly two state channels: orientation (travels with a chain, but the
update rule is hard-invariant blind to it) and rho (read by the update rule,
but carries no chain identity, so it isn't really "memory" of any specific
chain). This probe adds a THIRD channel that has BOTH properties at once:
travels with a chain (carried forward at every commit, the same mechanism
orientation already uses) AND is read by the update rule (unlike orientation).
This is a real structural addition, named honestly as new state the
certified reference substrate does not have -- not something already
licensed "for free" by P02-P13.

WHAT IS BEING TESTED. Does a chain's own accumulated history -- literally
"how many times has this chain committed so far, with some fade" -- make it
progressively more inclined to dwell (self-commit) rather than advance? If
so, does this settle into a stable, bounded "heaviness" (real mass should be
a constant property, not something that grows without limit), or does it
blow up / do nothing? No external reference position anywhere in this
design -- if this works, the resulting "mass" is intrinsic to the chain,
which is the more honest reading of what mass actually is.
"""
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,  # noqa: E402
                       assign_stratum_ids)
from simulator.sigma import compute_sigma, compute_candidates  # noqa: E402
from simulator.update import apply_tiebreak  # noqa: E402

CHAIN_LEN = 400
EDGE_BW = 0.5
B_SELF = 1.0
RHO_STAR = 0.5
JITTER_SD = 1e-3
COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=RHO_STAR, increment=1.0,
                     extinction_threshold=None)
PROBE_START = 10
MAX_STEPS = 2000


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


def apply_update_with_intrinsic_memory(u, state, graph, coeffs, chain_mem, k_mem, mem_decay):
    """Certified apply_update, with two changes: (1) the self-loop candidate's
    Sigma gets a bonus proportional to THIS CHAIN'S OWN accumulated memory
    (chain_mem[u]) -- no external reference position anywhere; (2) memory is
    carried forward at every commit, exactly the way orientation already is,
    updated by a simple grow-then-decay rule."""
    cands = compute_candidates(u, state, graph)
    if not cands:
        state[u].active = False
        return None

    mem_u = chain_mem.get(u, 0.0)
    sig = {}
    for v in cands:
        s = compute_sigma(u, v, state, graph, coeffs)
        if v == u:
            s += k_mem * mem_u
        sig[v] = s
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

    # Carry memory forward -- every commit (dwell OR advance) ages the chain by
    # one unit, with a decay factor controlling how much history persists.
    new_mem = mem_decay * mem_u + 1.0
    if u in chain_mem:
        del chain_mem[u]
    chain_mem[winner] = new_mem
    return winner


def run_probe(seed, k_mem, mem_decay, max_steps=MAX_STEPS, start=PROBE_START):
    g = build_chain_with_selfloops(CHAIN_LEN, B_SELF)
    sv = fresh_state(CHAIN_LEN, seed)
    assign_stratum_ids(sv, g)
    sv[start].active = True
    chain_mem = {start: 0.0}

    trace = [start]
    mem_trace = [0.0]
    dwell_count = advance_count = 0
    for t in range(1, max_steps + 1):
        active = sv.active_nodes()
        if len(active) != 1:
            break
        u = active[0]
        winner = apply_update_with_intrinsic_memory(u, sv, g, COEFFS, chain_mem, k_mem, mem_decay)
        if winner is None:
            break
        if winner == u:
            dwell_count += 1
        else:
            advance_count += 1
        trace.append(winner)
        mem_trace.append(chain_mem[winner])
        if winner >= CHAIN_LEN - 3:
            break
    trace = np.array(trace)
    total_steps = len(trace) - 1
    v_eff_overall = (trace[-1] - trace[0]) / total_steps if total_steps > 0 else 0.0
    return dict(trace=trace, mem_trace=np.array(mem_trace), dwell=dwell_count,
               advance=advance_count, v_eff=v_eff_overall, steps=total_steps)


def windowed_velocity(trace, window=100):
    """Velocity computed over successive windows of the trajectory -- shows
    whether the chain slows down progressively (real intrinsic aging) or
    stays constant (no effect) or oscillates."""
    d = np.diff(trace.astype(float))
    out = []
    for i in range(0, len(d), window):
        chunk = d[i:i + window]
        if len(chunk) > 0:
            out.append(chunk.mean())
    return out


def main():
    print("=" * 92)
    print("INTRINSIC-MEMORY PROBE -- does a chain's OWN accumulated history make it")
    print("progressively heavier, purely from self-reference, no external source at all?")
    print(f"chain={CHAIN_LEN}, start@{PROBE_START}, steps={MAX_STEPS}")
    print("=" * 92)

    seeds = list(range(8))

    print("\n[1] CONTROL -- k_mem=0 (recovers the certified self-loop dwell rule exactly,")
    print("    matching the confirmed 'at most one free dwell' baseline)")
    ctrl = [run_probe(s, 0.0, 1.0) for s in seeds]
    v0 = np.mean([r["v_eff"] for r in ctrl])
    d0 = np.mean([r["dwell"] for r in ctrl])
    print(f"  mean v_eff={v0:.4f}  mean dwell_count={d0:.2f}")

    for k_mem, mem_decay, label in (
        (0.05, 1.0, "k_mem=0.05, decay=1.0 (pure accumulation, no fade)"),
        (0.05, 0.95, "k_mem=0.05, decay=0.95 (mild fade)"),
        (0.05, 0.8, "k_mem=0.05, decay=0.8 (fast fade -> steady-state memory)"),
        (0.2, 0.8, "k_mem=0.2, decay=0.8 (stronger coupling, fast fade)"),
    ):
        print(f"\n[2] {label}")
        rows = [run_probe(s, k_mem, mem_decay) for s in seeds]
        v = np.mean([r["v_eff"] for r in rows])
        d = np.mean([r["dwell"] for r in rows])
        ext = np.mean([1.0 if r["steps"] < MAX_STEPS and r["trace"][-1] < CHAIN_LEN - 3 else 0.0
                       for r in rows])
        print(f"  overall v_eff={v:.4f} (control {v0:.4f})  dwell_count={d:.2f} (control {d0:.2f})  "
              f"stalled_frac={ext:.2f}")

        # Windowed velocity over one representative run -- shows the SHAPE of
        # any slowdown (progressive? steady-state? none?), not just an average.
        wv = windowed_velocity(rows[0]["trace"], window=100)
        print(f"  windowed v_eff (first {min(len(wv),8)} windows of 100 steps each, seed 0): "
              + ", ".join(f"{x:.3f}" for x in wv[:8]))
        mem_final = np.mean([r["mem_trace"][-1] for r in rows])
        print(f"  mean final accumulated memory value: {mem_final:.2f}")

    print("\n" + "=" * 92)
    print("READINGS:")
    print("  decay=1.0 (no fade): memory grows without bound -- if v_eff keeps DROPPING")
    print("    across windows with no plateau, this is unbounded/runaway heaviness, not")
    print("    real mass (real mass is a constant, not an ever-growing brake).")
    print("  decay<1.0 (fading memory): memory should plateau at a steady-state value --")
    print("    if v_eff ALSO plateaus (drops then levels off, doesn't keep falling), that's")
    print("    the correct-shape signature: a genuine, stable, intrinsic, self-caused")
    print("    heaviness -- no external source, no fixed reference position, real memory")
    print("    actually read by the rule, not faked.")
    print("  v_eff unaffected regardless of k_mem/decay -- intrinsic memory alone doesn't")
    print("    do it either; would need to be combined with something else (e.g. an actual")
    print("    external field) rather than standing alone.")
    print("=" * 92)


if __name__ == "__main__":
    main()
