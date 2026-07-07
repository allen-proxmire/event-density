"""Dwell-channel probe: does a self-referential channel (a locus committing to
itself instead of a neighbor) give the certified substrate a genuine third mode
between ballistic and extinct -- and if so, does it behave like a mass (sub-
ballistic but SURVIVING propagation), or like confinement/trapping (never
advances again) or nothing at all (never wins)?

WHY THIS IS A DIFFERENT QUESTION FROM H1/H2 (both already closed negative).
H2 (patterned commitment-density condensate) was tested directly on the
certified substrate (E1, mass_from_structured_participation_probe.py) and
found to give only channeling or worldline termination -- never a genuine
dispersion gap. H1 (inserted scalar) is blocked because there is no second
Sigma-visible field and orientation is Sigma-blind by hard invariant. Both
failures trace to the SAME deeper fact: the certified update rule is
ballistic-or-extinct -- a front either advances exactly one hop, or dies.
There is no third option: commit-in-place, survive, don't advance ("dwell").

A prior attempt to license a dwell state (Dwell_Question_Answer.md, RETRACTED)
tried to source it from a four-band P04 partition -- non-canonical, archived,
correctly retracted. This probe asks the real question instead: does canonical
P02 (participation) + P03 (channel/locus indexing) + P07 (channel structure)
actually forbid a channel from a locus to ITSELF? Reading the primitive text,
none of them do -- "channel" is never defined as requiring two distinct loci;
that requirement is an artifact of how the certified graph happens to be built
(evaluation/Bits/simulator/graph.py's add_edge has no u==v check; nothing in
the graph-construction code anywhere ever wires one). So a self-loop channel is
ADMISSIBLE under canonical primitives -- not forced, but not smuggling in new
structure either. This probe adds one, with nothing else changed in the
certified update mechanics, and reads off what happens.

GROUNDING DISCIPLINE (same standard as E1): use the certified step()/Sigma/
commit() code completely unmodified. The only addition is data -- self-loop
edges in the graph, exactly as licensed by graph.py's own add_edge(u, v, bw)
with u==v, which the class already supports without special-casing. No new
term, no new coupling, no bypass of the irreversibility chokepoint (commit()
is still the sole rho writer, delta still enforced >= 0).

WHAT WOULD COUNT AS A REAL MASS SIGNATURE. A front that dwells zero times
(b_self too weak / no structural reason to ever prefer self) recovers pure
ballistic -- v_eff == 1.0 hops/step, indistinguishable from massless. A front
that dwells forever (never finds it favorable to leave) is confinement/
trapping, not mass -- report as its own outcome, not conflated with a gap.
A front that dwells some finite number of times per hop, on average, while
continuing to survive and advance net-forward over many steps, gives an
effective velocity v_eff < 1.0 hops/step with survival -- that is the real
signature: sub-ballistic but continuing propagation, exactly what H1/H2 both
lacked. The KEY discriminant is the SAME one E1 used for its own confound:
report survival alongside v_eff, so a "slow" front that is actually just
dying slowly (extinction, not mass) cannot be misread as a gap.
"""
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,  # noqa: E402
                       assign_stratum_ids, step)

CHAIN_LEN = 400          # long enough that a front hitting the far end is not the limiter
EDGE_BW = 0.5            # certified default (matches E1's build_grid)
RHO_STAR = 0.5
MAX_STEPS = 2000
JITTER_SD = 1e-3         # certified convention: tiny noise breaks exact Sigma ties structurally


def build_chain_with_selfloops(n, b_self):
    """A 1D chain 0..n-1 with nearest-neighbor edges (bandwidth EDGE_BW) plus,
    if b_self > 0, a self-loop at every node with bandwidth b_self. b_self == 0
    means no self-loop is added at all (the certified control: pure chain)."""
    g = ParticipationGraph()
    for i in range(n):
        if i + 1 < n:
            g.add_edge(i, i + 1, bandwidth=EDGE_BW)
    if b_self > 0:
        for i in range(n):
            g.add_edge(i, i, bandwidth=b_self)  # licensed by graph.py; u==v unchecked, uncalled elsewhere
    return g


def run_once(n, b_self, coeffs, seed, max_steps=MAX_STEPS, start=5):
    """One front, started at `start`, moving through a uniform rho_star
    background (matched-mean, no H2-style patterning -- isolates the dwell
    mechanism alone). Returns the full position trace and survival info."""
    rng = np.random.default_rng(seed)
    g = build_chain_with_selfloops(n, b_self)
    sv = StateVector()
    for i in range(n):
        jitter = rng.normal(0, JITTER_SD)
        sv[i] = NodeState(rho=float(max(0.0, RHO_STAR + jitter)))
    sv[start].active = True

    trace = [start]
    dwell_count = 0
    advance_count = 0
    extinguished = False
    strata = assign_stratum_ids(sv, g)

    for t in range(1, max_steps + 1):
        active_before = sv.active_nodes()
        if not active_before:
            extinguished = True
            break
        u = active_before[0]  # exactly one front in this probe
        n_commits = step(sv, g, coeffs, strata=strata, t=t)
        active_after = sv.active_nodes()
        if n_commits == 0 or not active_after:
            extinguished = True
            break
        w = active_after[0]
        if w == u:
            dwell_count += 1
        else:
            advance_count += 1
        trace.append(w)
        if w >= n - 5:  # ran off the far end -- stop, not a mass-relevant event
            break

    total_steps = len(trace) - 1
    net_displacement = trace[-1] - trace[0]
    v_eff = net_displacement / total_steps if total_steps > 0 else 0.0
    return dict(v_eff=v_eff, steps=total_steps, dwell_count=dwell_count,
                advance_count=advance_count, extinguished=extinguished,
                final_pos=trace[-1], start=start)


def summarize(n, b_self, coeffs, seeds, max_steps=MAX_STEPS, start=5):
    rows = [run_once(n, b_self, coeffs, s, max_steps=max_steps, start=start) for s in seeds]
    agg = {k: float(np.mean([r[k] for r in rows])) for k in
           ("v_eff", "steps", "dwell_count", "advance_count", "final_pos")}
    agg["survived_frac"] = float(np.mean([0.0 if r["extinguished"] and r["advance_count"] == 0
                                          and r["final_pos"] == r["start"] else 1.0 for r in rows]))
    agg["extinguished_frac"] = float(np.mean([1.0 if r["extinguished"] else 0.0 for r in rows]))
    return agg


def main():
    seeds = list(range(12))
    print("=" * 84)
    print("DWELL-CHANNEL PROBE -- self-referential channel on the certified substrate")
    print(f"chain len={CHAIN_LEN}, edge_bw={EDGE_BW}, rho_star={RHO_STAR}, "
          f"jitter_sd={JITTER_SD}, seeds={len(seeds)}")
    print("=" * 84)

    # --- Test 1: control -- b_self = 0 (no self-loop at all). Must recover pure
    # ballistic (v_eff == 1.0) with the certified extinction threshold OFF, since
    # this is exactly the certified update rule with nothing added. ---
    NOEXT = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=RHO_STAR, increment=1.0,
                        extinction_threshold=None)
    print("\n[1] CONTROL -- b_self=0 (recovers certified ballistic-or-extinct exactly)")
    base = summarize(CHAIN_LEN, 0.0, NOEXT, seeds)
    print(f"  v_eff={base['v_eff']:.3f}  dwell={base['dwell_count']:.2f}  "
          f"advance={base['advance_count']:.2f}  extinguished_frac={base['extinguished_frac']:.2f}")

    # --- Test 2: sweep the self-loop bandwidth. Per the Sigma-mechanics reasoning
    # (Grad(u,u) is exactly 0, always; a real neighbor generically has nonzero
    # Grad from jitter), bandwidth itself should mostly NOT matter -- ties are
    # structurally rare with jitter present, so the winner is decided by Sigma,
    # not tie-break. Swept anyway, for completeness and to check this prediction. ---
    print("\n[2] SWEEP b_self (increment=1.0, kc=ks=kg=1.0, rho_star=0.5)")
    print(f"{'b_self':>8}{'v_eff':>8}{'dwell':>8}{'advance':>9}{'ext_frac':>10}")
    for b_self in (0.1, 0.5, 1.0, 2.0, 5.0):
        r = summarize(CHAIN_LEN, b_self, NOEXT, seeds)
        print(f"{b_self:>8.1f}{r['v_eff']:>8.3f}{r['dwell_count']:>8.2f}"
              f"{r['advance_count']:>9.2f}{r['extinguished_frac']:>10.2f}")

    # --- Test 3: sweep the coherence weight kc, which sets how sharply the
    # substrate penalizes drifting rho away from rho_star. This is the actual
    # candidate "mass knob": stronger kc should punish repeated self-commits
    # (which drive rho away from rho_star) faster, forcing earlier advance --
    # i.e. SMALLER kc -> MORE dwelling -> LOWER v_eff (heavier); LARGER kc ->
    # LESS dwelling -> v_eff closer to 1.0 (lighter). ---
    print("\n[3] SWEEP kc (coherence weight) at fixed b_self=1.0")
    print(f"{'kc':>8}{'v_eff':>8}{'dwell':>8}{'advance':>9}{'ext_frac':>10}")
    for kc in (0.2, 0.5, 1.0, 2.0, 5.0):
        cf = SigmaCoeffs(kc=kc, ks=1.0, kg=1.0, rho_star=RHO_STAR, increment=1.0,
                         extinction_threshold=None)
        r = summarize(CHAIN_LEN, 1.0, cf, seeds)
        print(f"{kc:>8.1f}{r['v_eff']:>8.3f}{r['dwell_count']:>8.2f}"
              f"{r['advance_count']:>9.2f}{r['extinguished_frac']:>10.2f}")

    # --- Test 4: sweep the commitment increment, the other candidate mass knob.
    # A larger per-commit increment should push rho away from rho_star FASTER
    # per dwell, forcing earlier advance (fewer dwells, v_eff -> 1.0, lighter);
    # a smaller increment should allow more dwells before the coherence penalty
    # bites (v_eff -> 0, heavier). ---
    print("\n[4] SWEEP commit increment at fixed b_self=1.0, kc=1.0")
    print(f"{'increment':>10}{'v_eff':>8}{'dwell':>8}{'advance':>9}{'ext_frac':>10}")
    for inc in (0.05, 0.1, 0.25, 0.5, 1.0, 2.0):
        cf = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=RHO_STAR, increment=inc,
                         extinction_threshold=None)
        r = summarize(CHAIN_LEN, 1.0, cf, seeds)
        print(f"{inc:>10.2f}{r['v_eff']:>8.3f}{r['dwell_count']:>8.2f}"
              f"{r['advance_count']:>9.2f}{r['extinguished_frac']:>10.2f}")

    # --- Test 5: with the certified EXTINCTION threshold back ON, does the
    # dwelling front ever actually die (confound guard, same discipline as E1
    # Test 2b) -- or does it survive throughout, the way a real mass-carrying
    # particle must (mass != a slow death)? ---
    print("\n[5] EXTINCTION CONFOUND GUARD (certified threshold=-2.0 back on, kc=0.5, inc=0.1)")
    CF_EXT = SigmaCoeffs(kc=0.5, ks=1.0, kg=1.0, rho_star=RHO_STAR, increment=0.1,
                         extinction_threshold=-2.0)
    r = summarize(CHAIN_LEN, 1.0, CF_EXT, seeds)
    print(f"  v_eff={r['v_eff']:.3f}  dwell={r['dwell_count']:.2f}  "
          f"advance={r['advance_count']:.2f}  extinguished_frac={r['extinguished_frac']:.2f}")

    # --- Test 6: kg vs ks. Hand-derivation of the Sigma comparison shows the
    # decisive quantity at the k-th potential dwell is
    #   Sigma(self) - Sigma(neighbor) = -kc*(k*increment)^2 + k*increment*(kg - ks)
    # (k = number of PRIOR self-commits since arrival; self's Grad term is always
    # exactly 0 by construction, so its only cost is the growing Coh/Strain
    # penalty from drifting off rho_star, while a neighbor's cost is the growing
    # Grad gap to the now-elevated self). With kg == ks (tests 2-5 above) this is
    # -kc*(k*increment)^2 < 0 for ALL k >= 1 -- self can win AT MOST the very
    # first round (round 0, before anything has accumulated, decided by jitter
    # alone) and never again: exactly one dwell, then permanent advance, no
    # matter what kc or increment are set to. That is exactly what tests 2-4
    # show (identical numbers regardless of kc/increment: the identity is not a
    # bug, it is this closed-form fact). Making kg > ks changes the sign for
    # small k, predicting a critical dwell count k* ~ (kg-ks)/(kc*increment)
    # before advancing becomes forced -- i.e. a genuinely tunable, repeated
    # dwell count, not just a single one-off delay. Testing this prediction
    # directly rather than trusting the algebra.
    print("\n[6] kg > ks -- does this unlock REPEATED dwelling (the real mass knob)?")
    print(f"{'kg':>6}{'ks':>6}{'kc':>6}{'inc':>6}{'pred_k*':>9}{'v_eff':>8}{'dwell':>8}"
          f"{'advance':>9}{'ext_frac':>10}")
    for kg, ks, kc, inc in ((1.0, 1.0, 1.0, 0.5), (3.0, 1.0, 1.0, 0.5),
                           (10.0, 1.0, 1.0, 0.5), (10.0, 1.0, 1.0, 0.1),
                           (30.0, 1.0, 1.0, 0.1), (50.0, 1.0, 0.5, 0.1)):
        cf = SigmaCoeffs(kc=kc, ks=ks, kg=kg, rho_star=RHO_STAR, increment=inc,
                         extinction_threshold=None)
        r = summarize(CHAIN_LEN, 1.0, cf, seeds)
        pred_kstar = (kg - ks) / (kc * inc) if kc * inc > 0 else float("inf")
        print(f"{kg:>6.1f}{ks:>6.1f}{kc:>6.1f}{inc:>6.2f}{pred_kstar:>9.2f}"
              f"{r['v_eff']:>8.3f}{r['dwell_count']:>8.2f}"
              f"{r['advance_count']:>9.2f}{r['extinguished_frac']:>10.2f}")
    print("   dwell_count tracking pred_k* (rising with kg/ks and 1/(kc*increment)) would")
    print("   confirm a genuinely tunable, repeated dwell mechanism -- a real mass knob.")
    print("   dwell_count stuck near 1.0 regardless would mean the one-off-delay finding")
    print("   from tests 2-5 is the whole story, not a tunable suppression.")

    # --- Test 7: is [6] a genuinely PERIODIC dwell-k*-then-advance-once cycle,
    # repeating at each new node (a real, stable, tunable sub-ballistic velocity),
    # or did the highest-kg rows just get cut off mid-dwell by the step budget
    # (in which case "advance" counts of 2-8 over 2000 steps could be an
    # artifact, not a stable rate)? Needs a MUCH longer run and a much longer
    # chain to have room to keep advancing. Track the full position trace's
    # linearity (does displacement grow steadily, or stall) as the real check.
    print("\n[7] LONG-RUN CHECK -- is [6]'s high-kg regime a stable repeating cycle,")
    print("    or a step-budget artifact? (kg=10, ks=1, kc=1, inc=0.1, pred_k*=90,")
    print("    chain=6000, steps=20000, 6 seeds)")
    LONG_CHAIN = 6000
    LONG_STEPS = 20000
    cf7 = SigmaCoeffs(kc=1.0, ks=1.0, kg=10.0, rho_star=RHO_STAR, increment=0.1,
                      extinction_threshold=None)
    long_seeds = list(range(6))
    print(f"{'seed':>6}{'final_pos':>11}{'v_eff':>8}{'dwell':>8}{'advance':>9}{'extinguished':>13}")
    v_effs = []
    for s in long_seeds:
        r = run_once(LONG_CHAIN, 1.0, cf7, s, max_steps=LONG_STEPS, start=5)
        v_effs.append(r["v_eff"])
        print(f"{s:>6}{r['final_pos']:>11}{r['v_eff']:>8.4f}{r['dwell_count']:>8}"
              f"{r['advance_count']:>9}{str(r['extinguished']):>13}")
    print(f"  mean v_eff over long run = {np.mean(v_effs):.4f}  "
          f"(predicted 1/(k*+1) = {1.0/91.0:.4f})")
    print("  v_eff STABLE and close to 1/(k*+1), position advancing steadily, never")
    print("  extinguished -> genuine repeating sub-ballistic mode, not a step-budget artifact.")
    print("  v_eff still collapsing/position stuck near start -> was an artifact; retract.")

    print("\n" + "=" * 84)
    print("READINGS:")
    print("  [1] should read v_eff ~ 1.0 exactly -- confirms probe recovers the certified")
    print("      control when no self-loop is added (no regression vs the existing rule).")
    print("  [2] flat v_eff across b_self would confirm the tie-break-rarely-matters")
    print("      prediction (Sigma, not bandwidth, is doing the work).")
    print("  [3]/[4] a MONOTONE v_eff response to kc / increment, WITH extinguished_frac")
    print("      staying near 0, is the actual mass signature: a tunable, survivable,")
    print("      sub-ballistic propagation speed -- something H1 and H2 both lacked.")
    print("  [5] extinguished_frac near 0 here means dwelling itself is not a slow death;")
    print("      a high extinguished_frac would mean this is extinction wearing a disguise,")
    print("      exactly the confound E1's Test 2b was built to catch.")
    print("=" * 84)


if __name__ == "__main__":
    main()
