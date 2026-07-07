"""Test (v2, redesigned): does a chain's LIVE presence make DWELLING more
attractive nearby and less attractive far away -- diminishing with distance,
per AP's proposal (2026-07-06) -- producing a front that genuinely slows near
a source and speeds back up away from it (the correct-sign mass signature)?

WHY v1 WAS THE WRONG TEST. The first version of this probe ran a front on a
chain with NO self-loops at all. Without a self-loop, a front can only ever
step left or right each turn -- it has no "stay in place" option, so it
literally cannot slow down; the only way a field bonus could show up at all
was by biasing which direction it stepped, which just reinforces or damps
ballistic motion, never genuine slowing. That test could not have shown the
mass signature no matter what the field did -- a design error, not a result.
This version fixes it directly: reuse the self-loop dwell mechanism confirmed
in dwell_channel_mass_probe.py, and make the FIELD apply specifically to the
attractiveness of the self-loop (dwell) candidate, decaying with distance
from a fixed reference ("source") position. That is the direct, correctly-
shaped test: does proximity to a source make a passing front want to dwell
more, and does that effect fade with distance, exactly as proposed.

GROUNDING DISCIPLINE (same as before). Reuse the certified update mechanics
(compute_candidates, compute_sigma, apply_tiebreak, commit()) verbatim --
only the self-loop candidate's Sigma gets one additive term, a function of
distance to the source, vanishing at k_field=0 (recovers the certified rule
with self-loops, exactly as tested and confirmed in dwell_channel_mass_probe).
This is a genuinely NEW structural ingredient (a live, decaying, per-position
modifier of the dwell attractiveness) -- flagged as CANDIDATE, not something
canonical primitives already hand you for free, the same standard applied
throughout this line of probes.
"""
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,  # noqa: E402
                       assign_stratum_ids)
from simulator.sigma import compute_sigma, compute_candidates  # noqa: E402
from simulator.update import apply_tiebreak  # noqa: E402

CHAIN_LEN = 300
EDGE_BW = 0.5
B_SELF = 1.0            # self-loop present everywhere, as in the confirmed dwell probe
RHO_STAR = 0.5
JITTER_SD = 1e-3
# certified defaults (kg=ks=kc=1): in ISOLATION this gives at most one free
# dwell then permanent advance (Dwell_Channel_Mass_Results.md Tests 2-5) --
# i.e. baseline "light" (near-ballistic) far from any source. Any slowing
# seen near the source must come from the new field term, not the baseline.
COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=RHO_STAR, increment=1.0,
                     extinction_threshold=None)

SOURCE_POS = 150
PROBE_START = 60
MAX_STEPS = 400


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


def dwell_field_bonus(u, v, source_pos, k_field, xi):
    """The one new ingredient: makes the SELF-LOOP candidate (v == u) more
    attractive near the source, decaying with distance -- zero for every
    other candidate, and zero everywhere if k_field == 0 (exact recovery of
    the certified rule)."""
    if k_field == 0.0 or v != u:
        return 0.0
    return k_field * np.exp(-abs(u - source_pos) / xi)


def apply_update_with_dwell_field(u, state, graph, coeffs, source_pos, k_field, xi):
    """Certified update.apply_update verbatim, with exactly one line changed:
    the field bonus added to Sigma, applying only to the self-loop candidate."""
    cands = compute_candidates(u, state, graph)
    if not cands:
        state[u].active = False
        return None

    sig = {v: compute_sigma(u, v, state, graph, coeffs)
          + dwell_field_bonus(u, v, source_pos, k_field, xi)
          for v in cands}
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
    return winner


def run_probe(seed, k_field, xi, source_pos=SOURCE_POS, probe_start=PROBE_START,
             max_steps=MAX_STEPS):
    g = build_chain_with_selfloops(CHAIN_LEN, B_SELF)
    sv = fresh_state(CHAIN_LEN, seed)
    assign_stratum_ids(sv, g)
    sv[probe_start].active = True

    trace = [probe_start]
    dwell_by_pos = []  # (position, dwelt_this_step: bool) for every step taken
    for t in range(1, max_steps + 1):
        active = sv.active_nodes()
        if len(active) != 1:
            break
        u = active[0]
        winner = apply_update_with_dwell_field(u, sv, g, COEFFS, source_pos, k_field, xi)
        if winner is None:
            break
        dwell_by_pos.append((u, winner == u))
        trace.append(winner)
        if winner >= CHAIN_LEN - 3:
            break
    return np.array(trace), dwell_by_pos


def dwell_rate_by_distance(dwell_by_pos, source_pos, bins):
    """Fraction of steps that were dwells, binned by signed distance to the source."""
    rates = {b: [0, 0] for b in bins}  # [dwell_count, total_count]
    for pos, dwelt in dwell_by_pos:
        d = pos - source_pos
        b = max([x for x in bins if x <= d], default=bins[0])
        rates[b][1] += 1
        if dwelt:
            rates[b][0] += 1
    return {b: (c[0] / c[1] if c[1] > 0 else float("nan")) for b, c in rates.items()}


def main():
    print("=" * 92)
    print("DWELL-FIELD-DECAY PROBE v2 -- does proximity to a fixed source make DWELLING")
    print("more attractive (genuine slowing), decaying with distance, as proposed?")
    print(f"chain={CHAIN_LEN}, source@{SOURCE_POS} (fixed reference), probe starts@{PROBE_START}")
    print("=" * 92)

    seeds = list(range(10))
    bins = list(range(-60, 41, 10))

    print("\n[1] CONTROL -- k_field=0 (recovers the confirmed certified dwell rule exactly:")
    print("    at most one free dwell, then permanent advance -- near-ballistic overall)")
    all_traces0, all_dwells0 = [], []
    for s in seeds:
        t, d = run_probe(s, 0.0, 10.0)
        all_traces0.append(t)
        all_dwells0.append(d)
    v0 = np.mean([np.mean(np.diff(t.astype(float))) for t in all_traces0])
    dwell_frac0 = np.mean([sum(1 for _, dw in d if dw) / len(d) for d in all_dwells0])
    print(f"  mean v_eff = {v0:.3f}   mean dwell fraction = {dwell_frac0:.4f}")

    for k_field, xi in ((2.0, 15.0), (5.0, 15.0), (5.0, 30.0)):
        print(f"\n[2] WITH FIELD -- k_field={k_field}, xi={xi}")
        traces, dwells = [], []
        for s in seeds:
            t, d = run_probe(s, k_field, xi)
            traces.append(t)
            dwells.append(d)
        v1 = np.mean([np.mean(np.diff(t.astype(float))) for t in traces])
        dwell_frac1 = np.mean([sum(1 for _, dw in d if dw) / len(d) if d else 0.0 for d in dwells])
        print(f"  mean v_eff = {v1:.3f} (control was {v0:.3f})   "
              f"mean dwell fraction = {dwell_frac1:.4f} (control was {dwell_frac0:.4f})")

        # Pooled dwell rate by signed distance to source across all seeds.
        pooled = []
        for d in dwells:
            pooled.extend(d)
        rates = dwell_rate_by_distance(pooled, SOURCE_POS, bins)
        print(f"  {'dist_to_source':>16}{'dwell_rate':>12}{'n_steps':>10}")
        for b in bins:
            c = [1 for pos, _ in pooled if max([x for x in bins if x <= pos - SOURCE_POS],
                                                default=bins[0]) == b]
            if c:
                print(f"  {b:>16}{rates[b]:>12.4f}{len(c):>10}")

    print("\n" + "=" * 92)
    print("READINGS:")
    print("  Control dwell fraction near 0 (near-ballistic) confirms the field-off baseline")
    print("  matches the earlier confirmed result (at most one free dwell overall).")
    print("  dwell_rate PEAKING near dist_to_source=0 and falling off toward the bin edges,")
    print("  WITH v_eff dropping below the control as k_field grows -- would be the correct-")
    print("  sign mass signature: genuine slowing near an active source, fading with distance,")
    print("  unlike Test 1's permanent-trail repulsion.")
    print("  dwell_rate flat/unaffected -- would mean this construction still doesn't produce")
    print("  the effect; the self-loop's Sigma may be dominated by its own Coh/Str terms")
    print("  (which still want rho near rho_star) regardless of the added field bonus.")
    print("=" * 92)


if __name__ == "__main__":
    main()
