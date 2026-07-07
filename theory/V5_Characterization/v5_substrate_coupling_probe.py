"""Real cross-chain V5 coupling in the certified substrate simulator (not the
phase-oscillator abstraction). Target: reproduce the local-proper-time signature
-- nearby chains lock to a shared commitment/advance rate (a composite rest
frame) while distant chains keep their own rates (time dilation preserved) --
from genuine substrate dynamics, and confirm it hinges on V5's FINITE reach.

DESIGN (honest, not rigged):
- Chains live on PARALLEL LANES, each a real certified 1D chain with self-loops.
  Fronts advance into fresh ground (no closed-ring saturation). Per-decision
  physics is the certified Sigma (compute_sigma) verbatim.
- NATURAL RATES come from the established memory mechanism: a front's own carried
  memory makes it dwell (route-2 result), so higher k_mem -> more dwelling ->
  slower advance rate. Two clusters of lanes run at different mean k_mem -> a
  genuine time-dilation setup (two composites at different proper-time rates).
- V5 COUPLING is a genuine cross-chain term with V5's actual known structure:
    * finite TRANSVERSE reach ell_V5: only nearby lanes couple (exp(-|dy|/ell_V5));
    * finite LONGITUDINAL window: only co-located fronts couple (exp(-|dx|/lam));
    * retarded: uses the PREVIOUS step's positions (past -> future).
  Mechanically the V5 term pulls each front toward the reach-weighted mean
  position of the other fronts: behind the local group -> nudge to advance;
  ahead -> nudge to dwell. This is a rate-coupling. It is NOT rigged to sync
  everything -- whether it produces LOCAL sync WITHOUT GLOBAL sync is decided by
  the finite reach ell_V5, which is exactly the open question.

HONEST CAVEATS:
- The V5 term and the memory channel are structural ADDITIONS to the certified
  substrate (honestly named), faithful to V5's known form (finite reach + finite
  memory + retarded). The certified base has neither. This tests whether V5's
  known STRUCTURE produces the required physics, not whether the bare substrate
  does (it doesn't -- shared-rho was dispersive, Collective_Pulse_Results.md).
- Coupling reads positions (a coarse-grained stand-in for "recent commitment
  activity"); the gauge PHASE is represented implicitly by relative position in
  the co-moving group rather than an explicit U(1) variable. Flagged.
- Fronts restricted to {dwell, advance-forward} (worldline moves forward in
  proper time) -- a clean modeling choice, flagged.
"""
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import ParticipationGraph, NodeState, StateVector, SigmaCoeffs  # noqa: E402
from simulator.sigma import compute_sigma  # noqa: E402

RHO_STAR = 0.5
EDGE_BW = 0.5
B_SELF = 1.0
JITTER_SD = 1e-3
MEM_DECAY = 0.9
COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=RHO_STAR, increment=1.0,
                     extinction_threshold=None)
LANE_LEN = 4000
LAM_LONG = 100.0       # longitudinal coupling window (co-moving fronts couple)


def build_lane(n):
    g = ParticipationGraph()
    for i in range(n - 1):
        g.add_edge(i, i + 1, bandwidth=EDGE_BW)
    for i in range(n):
        g.add_edge(i, i, bandwidth=B_SELF)
    return g


def make_lane_state(n, seed):
    rng = np.random.default_rng(seed)
    sv = StateVector()
    for i in range(n):
        sv[i] = NodeState(rho=float(max(0.0, RHO_STAR + rng.normal(0, JITTER_SD))))
    return sv


def run(lane_specs, ell_V5, A_V5, steps, seed):
    """lane_specs: list of dicts {y, k_mem, cluster}. One front per lane, starts
    at x=5. Returns per-lane advance-rate over the run."""
    g = build_lane(LANE_LEN)
    lanes = []
    for j, spec in enumerate(lane_specs):
        sv = make_lane_state(LANE_LEN, seed * 100 + j)
        sv[5].active = True
        lanes.append({"sv": sv, "pos": 5, "mem": 0.0,
                      "k_mem": spec["k_mem"], "y": spec["y"], "cluster": spec["cluster"],
                      "x0": 5})

    M = len(lanes)
    dy = np.array([[abs(lanes[i]["y"] - lanes[j]["y"]) for j in range(M)] for i in range(M)])
    Wtrans = np.exp(-dy / ell_V5)
    np.fill_diagonal(Wtrans, 0.0)

    for t in range(steps):
        prev_x = np.array([ln["pos"] for ln in lanes], dtype=float)   # retarded: last step
        for i, ln in enumerate(lanes):
            sv, u = ln["sv"], ln["pos"]
            if u >= LANE_LEN - 3:
                continue
            v_adv = u + 1
            # certified Sigma for the two candidates
            sig_self = compute_sigma(u, u, sv, g, COEFFS) + ln["k_mem"] * ln["mem"]
            sig_adv = compute_sigma(u, v_adv, sv, g, COEFFS)
            # V5 pull: reach-weighted mean position of the OTHER fronts, longitudinally
            # windowed; pull front toward it (behind -> favor advance, ahead -> dwell).
            w = Wtrans[i] * np.exp(-np.abs(prev_x - prev_x[i]) / LAM_LONG)
            w[i] = 0.0
            if w.sum() > 1e-9 and A_V5 > 0:
                x_target = np.sum(w * prev_x) / w.sum()
                sig_adv += A_V5 * (x_target - prev_x[i])   # behind group -> boost advance
            # decide
            if sig_adv > sig_self:
                sv[v_adv].commit(COEFFS.increment)
                sv[u].active = False
                sv[v_adv].active = True
                ln["pos"] = v_adv
            else:
                sv[u].commit(COEFFS.increment)     # dwell (self-commit)
            ln["mem"] = MEM_DECAY * ln["mem"] + 1.0

    rates = np.array([(ln["pos"] - ln["x0"]) / steps for ln in lanes])
    clusters = np.array([ln["cluster"] for ln in lanes])
    return rates, clusters


def summarize(rates, clusters):
    cs = np.unique(clusters)
    within = np.mean([np.std(rates[clusters == c]) for c in cs])   # within-cluster spread
    cmeans = [rates[clusters == c].mean() for c in cs]
    gap = abs(cmeans[0] - cmeans[1]) if len(cmeans) >= 2 else 0.0   # cross-cluster rate gap
    return within, gap, cmeans


def main():
    print("=" * 92)
    print("REAL-SUBSTRATE V5 COUPLING -- does a genuine cross-chain V5 term give LOCAL")
    print("shared proper time (nearby lanes lock) WITHOUT a universal tick (far lanes free)?")
    print("=" * 92)

    D = 20.0                # transverse separation between the two clusters
    # GENUINE within-cluster rate spread (rates are quantized to 1/n, so mix k_mem
    # across quanta): cluster 0 fast (k_mem 0.1/0.2/0.3/0.5 -> rates .667/.5/.5/.333),
    # cluster 1 slow (0.7/1.0/1.3/2.0 -> .333/.25/.25/.20). Both have a REAL internal
    # spread to lock, and different means (the time-dilation gap).
    k0 = [0.1, 0.2, 0.3, 0.5]
    k1 = [0.7, 1.0, 1.3, 2.0]
    specs = ([{"y": float(i), "k_mem": k0[i], "cluster": 0} for i in range(4)]
             + [{"y": D + i, "k_mem": k1[i], "cluster": 1} for i in range(4)])
    STEPS = 2500
    seeds = [0, 1, 2]

    print(f"\n8 lanes, 2 clusters of 4 with GENUINE within-cluster rate spread.")
    print(f"Cluster 0 (fast, rates ~.667-.333) at y~0; cluster 1 (slow, ~.333-.20) at y~{D:.0f}.")
    print(f"Transverse separation D={D:.0f}. Longitudinal window={LAM_LONG:.0f}.")

    # Sanity / baseline: uncoupled natural rates
    w0s, g0s = [], []
    for s in seeds:
        r, c = run(specs, ell_V5=1.0, A_V5=0.0, steps=STEPS, seed=s)
        w, g, cm = summarize(r, c)
        w0s.append(w); g0s.append(g)
    w0, g0 = np.mean(w0s), np.mean(g0s)
    print(f"\n[uncoupled A_V5=0] within-cluster rate spread={w0:.4f}  cross-cluster gap={g0:.4f}")
    print(f"  (natural: cluster rates differ = the time-dilation setup; nonzero within-spread)")

    A_V5 = 1.5
    print(f"\ncoupling A_V5={A_V5}, sweep transverse reach ell_V5:")
    print(f"{'ell_V5':>8}{'within-spread':>15}{'cross-gap':>12}{'ratio_within':>14}  regime")
    print("-" * 92)
    for ell in (0.5, 2.0, 5.0, 10.0, 30.0, 100.0):
        ws, gs = [], []
        for s in seeds:
            r, c = run(specs, ell_V5=ell, A_V5=A_V5, steps=STEPS, seed=s)
            w, g, cm = summarize(r, c)
            ws.append(w); gs.append(g)
        w, g = np.mean(ws), np.mean(gs)
        rw = w / w0 if w0 > 0 else float("nan")
        if rw < 0.5 and g > 0.5 * g0:
            regime = "LOCAL lock, gap preserved  <-- required (local proper time, no univ. tick)"
        elif g < 0.3 * g0:
            regime = "cross-cluster gap COLLAPSING -> universal tick (wrong)"
        elif rw > 0.8:
            regime = "reach too short: no local locking"
        else:
            regime = "partial"
        print(f"{ell:>8.1f}{w:>15.4f}{g:>12.4f}{rw:>14.2f}  {regime}")

    print("\n" + "=" * 92)
    print("READING: a window of ell_V5 with within-cluster spread SHRINKING (ratio<<1 = local")
    print("lock into a shared rate = local proper time) while the cross-cluster gap SURVIVES")
    print("(time dilation preserved) = V5's finite reach gives local binding without a universal")
    print("tick, now from REAL substrate dynamics. ell_V5 >> D collapsing the gap = universal")
    print("clock = wrong, confirming V5's finiteness is load-bearing for time dilation.")
    print("=" * 92)


if __name__ == "__main__":
    main()
