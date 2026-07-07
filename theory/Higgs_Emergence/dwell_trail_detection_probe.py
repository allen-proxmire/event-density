"""Test 1 (Dwell_To_GaugeBoson_Coupling_Scoping.md): does a front's dwell trail
leave anything a LATER, DIFFERENT front can actually detect -- or is it
completely private to the front that made it?

This is the cheapest possible check of whether the dwell mechanism's output
could ever be condensate-like (a shared, lasting effect other objects notice)
versus being pure bookkeeping local to one front's own history (in which case
"coupling to gauge bosons" is a dead end before any bigger build is worth
trying).

METHOD (paired, same-seed, single-variable). Build ONE initial substrate state
(same jitter, same self-loop bandwidth, same coefficients as the confirmed
dwell-mass run). Clone it into two copies:
  - TRAIL copy: run front 1 through it first (letting it dwell-and-advance,
    per the confirmed kg>ks mechanism), well past a marked "test region",
    then leave its rho history in place.
  - CONTROL copy: untouched -- no front has ever passed through it.
Then run front 2, starting at the SAME position just before the test region,
on BOTH copies, with nothing else different. Compare front 2's dwell count,
advance count, effective velocity, and survival on the TRAIL copy versus the
CONTROL copy. Any measurable difference at all means the trail is a REAL,
detectable, lasting effect -- not private bookkeeping. No difference means it
is private, and the "coupling to gauge bosons" line of attack is closed here,
cheaply, before a bigger build.
"""
import copy
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,  # noqa: E402
                       assign_stratum_ids, step)

CHAIN_LEN = 600
EDGE_BW = 0.5
RHO_STAR = 0.5
JITTER_SD = 1e-3
# Confirmed long-run dwell regime from Dwell_Channel_Mass_Results.md Test 7.
COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=10.0, rho_star=RHO_STAR, increment=0.1,
                     extinction_threshold=None)
B_SELF = 1.0

FRONT1_START = 5
# Confirmed long-run v_eff for this coefficient regime is ~0.0105 hops/step
# (Dwell_Channel_Mass_Results.md Test 7) -- reaching position ~150 needs
# roughly (150-5)/0.0105 ~ 13,800 steps. Budget generously above that.
FRONT1_STEPS = 35000
TEST_REGION_START = 100      # front 2 starts just before here
TEST_REGION_END = 180        # front 1 must be well past this before front 2 starts
FRONT2_STEPS = 800


def build_chain_with_selfloops(n, b_self):
    g = ParticipationGraph()
    for i in range(n):
        if i + 1 < n:
            g.add_edge(i, i + 1, bandwidth=EDGE_BW)
    if b_self > 0:
        for i in range(n):
            g.add_edge(i, i, bandwidth=b_self)
    return g


def fresh_state(n, seed):
    """One canonical initial rho field (jitter around rho_star) -- the
    single shared starting point cloned into the TRAIL and CONTROL copies."""
    rng = np.random.default_rng(seed)
    sv = StateVector()
    for i in range(n):
        jitter = rng.normal(0, JITTER_SD)
        sv[i] = NodeState(rho=float(max(0.0, RHO_STAR + jitter)))
    return sv


def run_front(sv, g, strata, start, max_steps, coeffs=COEFFS):
    """Run one front from `start`; returns full trajectory stats. Mutates sv
    in place (rho commits are real, irreversible, exactly as the certified
    rule requires)."""
    pre_existing_active = sv.active_nodes()
    if pre_existing_active:
        raise RuntimeError(
            f"run_front called with {len(pre_existing_active)} already-active "
            f"node(s) {pre_existing_active} still in the state -- a prior front "
            "was not deactivated first; trajectories would silently mix.")
    sv[start].active = True
    trace = [start]
    dwell = advance = 0
    extinguished = False
    for t in range(1, max_steps + 1):
        active = sv.active_nodes()
        if len(active) != 1:
            raise RuntimeError(
                f"expected exactly one active front, found {len(active)}: {active} "
                f"at step {t} -- tracking a single front is no longer valid.")
        u = active[0]
        n_commits = step(sv, g, coeffs, strata=strata, t=t)
        active_after = sv.active_nodes()
        if n_commits == 0 or not active_after:
            extinguished = True
            break
        w = active_after[0]
        if w == u:
            dwell += 1
        else:
            advance += 1
        trace.append(w)
    steps_run = len(trace) - 1
    v_eff = (trace[-1] - trace[0]) / steps_run if steps_run > 0 else 0.0
    return dict(trace=trace, dwell=dwell, advance=advance, extinguished=extinguished,
               final_pos=trace[-1], v_eff=v_eff, steps=steps_run)


def rho_snapshot(sv, lo, hi):
    return np.array([sv[i].rho for i in range(lo, hi)])


def run_once(seed):
    g = build_chain_with_selfloops(CHAIN_LEN, B_SELF)
    strata = assign_stratum_ids(fresh_state(CHAIN_LEN, seed), g)  # topology-only; same for both copies

    # Shared starting point.
    base_sv = fresh_state(CHAIN_LEN, seed)

    # TRAIL copy: run front 1 through it first.
    trail_sv = copy.deepcopy(base_sv)
    r1 = run_front(trail_sv, g, strata, FRONT1_START, FRONT1_STEPS)
    # Sanity: front 1 must have actually cleared the test region before front 2 starts.
    cleared = r1["final_pos"] >= TEST_REGION_END or r1["extinguished"]
    # CRITICAL: this dwell regime does not reliably extinguish (that is the whole
    # point of the mechanism), so front 1 is very likely still ACTIVE at its own
    # final position when front 2 is about to start. Force it inactive explicitly
    # -- otherwise step() processes BOTH fronts every step and run_front's
    # single-active-node tracking silently mixes the two trajectories together.
    if not r1["extinguished"]:
        trail_sv[r1["final_pos"]].active = False
    rho_trail_region = rho_snapshot(trail_sv, TEST_REGION_START, TEST_REGION_END)

    # CONTROL copy: untouched, no front has passed through it.
    control_sv = copy.deepcopy(base_sv)
    rho_control_region = rho_snapshot(control_sv, TEST_REGION_START, TEST_REGION_END)

    # Front 2 on the TRAIL copy, starting just before the test region.
    r2_trail = run_front(trail_sv, g, strata, TEST_REGION_START - 5, FRONT2_STEPS)

    # Front 2 on the CONTROL copy, IDENTICAL start, IDENTICAL steps, nothing
    # else different -- this is the single-variable comparison.
    r2_control = run_front(control_sv, g, strata, TEST_REGION_START - 5, FRONT2_STEPS)

    return dict(
        seed=seed, front1_final=r1["final_pos"], front1_cleared_region=cleared,
        rho_trail_mean=float(rho_trail_region.mean()), rho_trail_max=float(rho_trail_region.max()),
        rho_control_mean=float(rho_control_region.mean()), rho_control_max=float(rho_control_region.max()),
        trail_dwell=r2_trail["dwell"], trail_advance=r2_trail["advance"],
        trail_v_eff=r2_trail["v_eff"], trail_extinguished=r2_trail["extinguished"],
        trail_final=r2_trail["final_pos"],
        control_dwell=r2_control["dwell"], control_advance=r2_control["advance"],
        control_v_eff=r2_control["v_eff"], control_extinguished=r2_control["extinguished"],
        control_final=r2_control["final_pos"],
    )


def main():
    print("=" * 92)
    print("TEST 1 -- does a SECOND front detect the FIRST front's dwell trail at all?")
    print(f"chain={CHAIN_LEN}, test region=[{TEST_REGION_START},{TEST_REGION_END}), "
          f"front2 start={TEST_REGION_START-5}, front2 steps={FRONT2_STEPS}")
    print("=" * 92)

    seeds = list(range(10))
    rows = [run_once(s) for s in seeds]

    n_cleared = sum(1 for r in rows if r["front1_cleared_region"])
    print(f"\nfront 1 cleared the test region in {n_cleared}/{len(rows)} runs "
          f"(must be high for the test to be valid)")

    print("\n[A] Is rho ACTUALLY different in the test region after front 1's trail?")
    print(f"{'seed':>6}{'rho_trail_mean':>16}{'rho_trail_max':>15}"
          f"{'rho_ctrl_mean':>15}{'rho_ctrl_max':>14}")
    for r in rows:
        print(f"{r['seed']:>6}{r['rho_trail_mean']:>16.4f}{r['rho_trail_max']:>15.2f}"
              f"{r['rho_control_mean']:>15.4f}{r['rho_control_max']:>14.4f}")

    print("\n[B] Does front 2 behave differently on the TRAIL copy vs the CONTROL copy?")
    print(f"{'seed':>6}{'trail_dwell':>12}{'ctrl_dwell':>11}{'trail_v':>9}{'ctrl_v':>8}"
          f"{'trail_ext':>10}{'ctrl_ext':>9}")
    for r in rows:
        print(f"{r['seed']:>6}{r['trail_dwell']:>12}{r['control_dwell']:>11}"
              f"{r['trail_v_eff']:>9.4f}{r['control_v_eff']:>8.4f}"
              f"{str(r['trail_extinguished']):>10}{str(r['control_extinguished']):>9}")

    dwell_diff = np.array([r["trail_dwell"] - r["control_dwell"] for r in rows])
    v_diff = np.array([r["trail_v_eff"] - r["control_v_eff"] for r in rows])
    print("\n" + "=" * 92)
    print("READINGS:")
    print(f"  mean(trail_dwell - control_dwell) = {dwell_diff.mean():.2f}  "
          f"(sd {dwell_diff.std():.2f}, seeds {len(rows)})")
    print(f"  mean(trail_v_eff - control_v_eff) = {v_diff.mean():.5f}  "
          f"(sd {v_diff.std():.5f})")
    print("  A rho difference in [A] confirms the trail is REAL (as expected -- rho commits")
    print("  are permanent/irreversible by construction). The decisive question is [B]:")
    print("  a systematic, non-zero dwell/velocity difference means front 2 actually")
    print("  REACTS to front 1's trail -- a real, detectable, lasting effect, worth taking")
    print("  further. Differences consistent with zero (noise-sized, no systematic sign)")
    print("  mean front 2 never crosses paths with anything front 1 changed enough to")
    print("  matter -- the trail is real but functionally invisible to a later front,")
    print("  closing the 'condensate' reading here, cheaply.")
    print("=" * 92)


if __name__ == "__main__":
    main()
