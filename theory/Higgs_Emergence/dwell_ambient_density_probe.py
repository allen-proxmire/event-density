"""Test 2 (from Dwell_To_GaugeBoson_Coupling_Scoping.md, run now that Test 1 and
the field-decay probe both landed): does a PRE-SET region of elevated ambient
density -- using the CERTIFIED update rule completely unmodified, no new field
term at all -- reproduce the field-decay probe's genuine-slowing signature, or
does it behave like E1's already-established negative (channeling/termination,
not a smooth dispersion gap)?

WHY THIS IS THE RIGHT NEXT CHECK. The field-decay probe's positive result used
a HAND-INSERTED bonus that applies ONLY to the self-loop candidate, growing
near a source and fading with distance -- a genuinely asymmetric ingredient
(it treats "stay" and "advance" differently depending on position). Plain
elevated ambient density, fed through the CERTIFIED, UNMODIFIED Sigma
(Coh/Str/Grad, which use the SAME rho_star target for every candidate, self or
neighbor) has no such asymmetry: an elevated-density region should make BOTH
advancing into it AND dwelling within it look unattractive (both are penalized
for being far from rho_star equally). Predicted mechanism, before running:
this should reproduce E1's finding (channeling/deflection, or termination if
extinction is on) rather than the field-decay probe's clean slowing bump --
worth confirming directly rather than assuming, since this is exactly the
kind of prediction that needs a real run, not just algebra.

GROUNDING DISCIPLINE. Zero new ingredients here -- this reuses `step()` /
`apply_update()` from the certified module completely unmodified. The ONLY
thing that differs from a control run is the INITIAL rho landscape (a
pre-set bump, exactly the same discipline E1 used: an allowed initial
condition, not a new term or coupling).
"""
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,  # noqa: E402
                       assign_stratum_ids, step)

CHAIN_LEN = 300
EDGE_BW = 0.5
B_SELF = 1.0
RHO_STAR = 0.5
JITTER_SD = 1e-3
BUMP_CENTER = 150
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


def bump_landscape(n, center, amp, width, seed):
    """A pre-set Gaussian bump in rho, centered at `center`, matched-baseline
    to rho_star everywhere else -- same discipline as E1's landscape()."""
    rng = np.random.default_rng(seed)
    x = np.arange(n)
    bump = amp * np.exp(-0.5 * ((x - center) / width) ** 2)
    rho = RHO_STAR + bump
    jitter = rng.normal(0, JITTER_SD, size=n)
    return np.clip(rho + jitter, 0.0, None)


def run_probe(seed, amp, width, coeffs, probe_start=PROBE_START, max_steps=MAX_STEPS):
    g = build_chain_with_selfloops(CHAIN_LEN, B_SELF)
    rho0 = bump_landscape(CHAIN_LEN, BUMP_CENTER, amp, width, seed)
    sv = StateVector()
    for i in range(CHAIN_LEN):
        sv[i] = NodeState(rho=float(rho0[i]))
    strata = assign_stratum_ids(sv, g)
    sv[probe_start].active = True

    trace = [probe_start]
    dwell_by_pos = []
    extinguished = False
    for t in range(1, max_steps + 1):
        active = sv.active_nodes()
        if not active:
            extinguished = True
            break
        u = active[0]
        n_commits = step(sv, g, coeffs, strata=strata, t=t)
        active_after = sv.active_nodes()
        if n_commits == 0 or not active_after:
            extinguished = True
            break
        w = active_after[0]
        dwell_by_pos.append((u, w == u))
        trace.append(w)
        if w >= CHAIN_LEN - 3:
            break
    return dict(trace=np.array(trace), dwell_by_pos=dwell_by_pos, extinguished=extinguished)


def dwell_rate_by_distance(dwell_by_pos, center, bins):
    rates = {b: [0, 0] for b in bins}
    for pos, dwelt in dwell_by_pos:
        d = pos - center
        b = max([x for x in bins if x <= d], default=bins[0])
        rates[b][1] += 1
        if dwelt:
            rates[b][0] += 1
    return {b: (c[0] / c[1] if c[1] > 0 else float("nan")) for b, c in rates.items()}


def main():
    print("=" * 92)
    print("TEST 2 -- PRE-SET ambient density bump, CERTIFIED rule unmodified (no new term).")
    print("Prediction: should reproduce E1's negative (channeling/termination), NOT the")
    print("field-decay probe's clean slowing bump, because Coh/Str/Grad treat self and")
    print("neighbor candidates symmetrically -- there is no reason for this to single out")
    print("dwelling near the bump as favorable rather than just avoiding the bump entirely.")
    print(f"chain={CHAIN_LEN}, bump center={BUMP_CENTER}, probe starts@{PROBE_START}")
    print("=" * 92)

    seeds = list(range(10))
    bins = list(range(-60, 41, 10))

    NOEXT = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=RHO_STAR, increment=1.0,
                        extinction_threshold=None)
    WITHEXT = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=RHO_STAR, increment=1.0,
                          extinction_threshold=-2.0)

    print("\n[1] CONTROL -- flat background (amp=0), extinction OFF")
    ctrl = [run_probe(s, 0.0, 20.0, NOEXT) for s in seeds]
    v_ctrl = np.mean([np.mean(np.diff(r["trace"].astype(float))) for r in ctrl])
    dwell_ctrl = np.mean([sum(1 for _, d in r["dwell_by_pos"] if d) / len(r["dwell_by_pos"])
                         for r in ctrl if r["dwell_by_pos"]])
    ext_ctrl = np.mean([1.0 if r["extinguished"] else 0.0 for r in ctrl])
    print(f"  v_eff={v_ctrl:.3f}  dwell_frac={dwell_ctrl:.4f}  extinguished_frac={ext_ctrl:.2f}")

    for amp, width, coeffs, label in (
        (2.0, 15.0, NOEXT, "amp=2.0 width=15, extinction OFF"),
        (5.0, 15.0, NOEXT, "amp=5.0 width=15, extinction OFF"),
        (2.0, 15.0, WITHEXT, "amp=2.0 width=15, extinction ON (-2.0)"),
        (5.0, 15.0, WITHEXT, "amp=5.0 width=15, extinction ON (-2.0)"),
    ):
        print(f"\n[2] {label}")
        rows = [run_probe(s, amp, width, coeffs) for s in seeds]
        v = np.mean([np.mean(np.diff(r["trace"].astype(float))) for r in rows])
        dwell_frac = np.mean([sum(1 for _, d in r["dwell_by_pos"] if d) / len(r["dwell_by_pos"])
                              if r["dwell_by_pos"] else 0.0 for r in rows])
        ext_frac = np.mean([1.0 if r["extinguished"] else 0.0 for r in rows])
        print(f"  v_eff={v:.3f} (control {v_ctrl:.3f})  dwell_frac={dwell_frac:.4f} "
              f"(control {dwell_ctrl:.4f})  extinguished_frac={ext_frac:.2f} (control {ext_ctrl:.2f})")

        pooled = []
        for r in rows:
            pooled.extend(r["dwell_by_pos"])
        rates = dwell_rate_by_distance(pooled, BUMP_CENTER, bins)
        print(f"  {'dist_to_bump':>14}{'dwell_rate':>12}{'n_steps':>10}")
        for b in bins:
            c = [1 for pos, _ in pooled if max([x for x in bins if x <= pos - BUMP_CENTER],
                                                default=bins[0]) == b]
            if c:
                print(f"  {b:>14}{rates[b]:>12.4f}{len(c):>10}")

    print("\n" + "=" * 92)
    print("READINGS:")
    print("  dwell_rate rising smoothly near the bump, WITHOUT extinguished_frac rising too,")
    print("  would mean plain ambient density (no new ingredient) already reproduces genuine")
    print("  slowing -- a much stronger result than the field-decay probe (needs no new term).")
    print("  extinguished_frac rising sharply near/in the bump (with extinction ON), or")
    print("  dwell_rate NOT tracking the bump cleanly -- confirms the prediction: plain")
    print("  ambient density reproduces E1's negative (channeling/termination), not slowing --")
    print("  meaning the field-decay probe's asymmetric ingredient really was necessary,")
    print("  not just \"more density nearby\" in disguise.")
    print("=" * 92)


if __name__ == "__main__":
    main()
