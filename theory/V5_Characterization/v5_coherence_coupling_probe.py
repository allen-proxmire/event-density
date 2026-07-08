"""V5 forward-derivation, decisive build: is V5's ATTRACTIVE sign DERIVED from
P12's reward-coherence structure, or must it be assumed?

Prior art (`v5_substrate_coupling_probe.py`) showed a real cross-chain V5 term in
the certified substrate gives finite-reach local synchronization (nearby chains
lock to a shared proper-time rate, distant chains stay free = time dilation
preserved). BUT its coupling was a hand-put rate term `A_V5*(x_target - x_i)` with
the attractive sign PUT IN BY HAND. That assumed sign is the gap Paper_090 leaves
open (090 fixes existence [P10], retardation [P11], and the gauge phase [P05+P09],
but NOT the sign of the envelope F_V5).

THIS build removes the hand-put sign. The cross-chain coupling is the COHERENCE
CONTENT of the two chains' participation superposition, entered into the certified
selection Sigma with P12's OWN sign (Sigma = Coh - Str - Grad; Coh has the +
coefficient BY DEFINITION of P12). Each chain carries a U(1) phase phi = Dphi *
(forward proper-time progress) [gauge phase, 090 sec 4.3]. For a front's two
choices (advance / dwell) we add + k_c5 * Coh(choice) to the certified sigma,
    Coh(choice) = sum_j w_ij * cos( phi_j^retarded + A_ij - phi_i^choice ),
w_ij = exp(-|dy|/ell_V5) [transverse reach] * exp(-|dx|/lam) [longitudinal window],
A_ij = kappa_bw*(bw-1) [P05 connection carrying quenched substrate disorder, the
Step-4 finite-reach mechanism]. Retarded: phi_j from last step (090 sec 5.1, P11).

THE SIGN IS NOT ASSUMED. We use P12's + sign on Coh and READ OFF whether that
synchronizes. A front phase-behind its reach-group raises coherence by advancing
(catches up); phase-ahead lowers it (dwells). If local synchronization EMERGES
from + k_c5 alone, V5's attractive sign is derived from P12-Coh. Controls:
  * k_c5 = 0  -> natural rates, no coupling (baseline).
  * k_c5 < 0  -> P12 sign FLIPPED; must anti-synchronize / fail to bind (shows the
                 + sign is doing the work, not the machinery).

HONEST MODELING NOTES (flagged, not buried):
- rho/advance-vs-dwell physics is the certified compute_sigma verbatim + the route-2
  memory rate mechanism (higher k_mem -> more dwell -> slower). Real substrate rates.
- phi advances by Dphi on ADVANCE, 0 on DWELL (proper-time clock progresses with
  forward worldline motion; dwelling holds it relative to advancing). Clean choice.
- This is closer to the substrate than the earlier phase-oscillator model: the
  advance/dwell decision stays certified; only a P09 phase channel + a P12-Coh
  cross-chain term are added (exactly what 090 says V5 is: P05+P09+P12 cross-chain).
- G1 caveat: 090 writes F_V5 as a GENERAL envelope, not an interference modulus.
  Identifying V5's coupling with Coh is a HYPOTHESIS (H-V5-Coh) tested here, not a
  claim inherited from 090. A positive result is substrate evidence for it, not a
  theorem that 090's F_V5 must be this.
"""
import numpy as np
import sys, os, math

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
LAM_LONG = 100.0        # longitudinal window (co-moving fronts couple)
DPHI = 0.05             # gauge-phase increment per forward advance (U(1) clock)


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


def run(lane_specs, ell_V5, k_c5, steps, seed, kappa_bw=0.0):
    """lane_specs: list of {y, k_mem, cluster}. One front per lane from x=5.
    Returns per-lane forward-advance rate over the run."""
    g = build_lane(LANE_LEN)
    rng = np.random.default_rng(seed * 977 + 3)
    lanes = []
    for j, spec in enumerate(lane_specs):
        sv = make_lane_state(LANE_LEN, seed * 100 + j)
        sv[5].active = True
        lanes.append({"sv": sv, "pos": 5, "mem": 0.0, "phi": 0.0,
                      "k_mem": spec["k_mem"], "y": spec["y"],
                      "cluster": spec["cluster"], "x0": 5})
    M = len(lanes)
    dy = np.array([[abs(lanes[i]["y"] - lanes[j]["y"]) for j in range(M)] for i in range(M)])
    Wtrans = np.exp(-dy / ell_V5); np.fill_diagonal(Wtrans, 0.0)
    # quenched P05 connection holonomy between lane pairs (frozen, disorder)
    A = kappa_bw * (2 * rng.random((M, M)) - 1.0)
    A = np.triu(A, 1); A = A - A.T                 # antisymmetric: A_ij = -A_ji

    for t in range(steps):
        prev_x = np.array([ln["pos"] for ln in lanes], dtype=float)   # retarded
        prev_phi = np.array([ln["phi"] for ln in lanes], dtype=float)
        for i, ln in enumerate(lanes):
            sv, u = ln["sv"], ln["pos"]
            if u >= LANE_LEN - 3:
                continue
            v_adv = u + 1
            sig_self = compute_sigma(u, u, sv, g, COEFFS) + ln["k_mem"] * ln["mem"]
            sig_adv = compute_sigma(u, v_adv, sv, g, COEFFS)
            # cross-chain coherence content, reach- and longitudinally-weighted,
            # with the quenched P05 holonomy; retarded neighbor phases.
            if k_c5 != 0.0:
                w = Wtrans[i] * np.exp(-np.abs(prev_x - prev_x[i]) / LAM_LONG)
                w[i] = 0.0
                if w.sum() > 1e-9:
                    # coherence GRADIENT wrt phi_i: d/dphi_i[ sum w cos(phi_j+A-phi_i) ]
                    #  = sum w sin(phi_j + A - phi_i). Advancing moves phi_i UP the
                    # coherence gradient (toward neighbors' phase). Bias advance by it.
                    # + k_c5 = P12 sign (reward coherence). Attractive iff + wins.
                    grad = np.sum(w * np.sin(prev_phi + A[i] - ln["phi"]))
                    sig_adv += k_c5 * grad
            if sig_adv > sig_self:
                sv[v_adv].commit(COEFFS.increment)
                sv[u].active = False; sv[v_adv].active = True
                ln["pos"] = v_adv; ln["phi"] += DPHI
            else:
                sv[u].commit(COEFFS.increment)          # dwell
            ln["mem"] = MEM_DECAY * ln["mem"] + 1.0

    rates = np.array([(ln["pos"] - ln["x0"]) / steps for ln in lanes])
    clusters = np.array([ln["cluster"] for ln in lanes])
    return rates, clusters


def summarize(rates, clusters):
    cs = np.unique(clusters)
    within = np.mean([np.std(rates[clusters == c]) for c in cs])
    cmeans = [rates[clusters == c].mean() for c in cs]
    gap = abs(cmeans[0] - cmeans[1]) if len(cmeans) >= 2 else 0.0
    return within, gap, cmeans


def main():
    print("=" * 94)
    print("V5 COHERENCE-COUPLING: is the attractive sign DERIVED from P12's + Coh, or assumed?")
    print("No hand-put attractive term. Coupling = P12-Coh of the cross-chain superposition.")
    print("=" * 94)

    D = 20.0
    k0 = [0.1, 0.2, 0.3, 0.5]    # fast cluster (rates ~.667-.333)
    k1 = [0.7, 1.0, 1.3, 2.0]    # slow cluster (rates ~.333-.20)
    specs = ([{"y": float(i), "k_mem": k0[i], "cluster": 0} for i in range(4)]
             + [{"y": D + i, "k_mem": k1[i], "cluster": 1} for i in range(4)])
    STEPS = 2500; seeds = [0, 1, 2]

    print(f"\n8 lanes, 2 clusters of 4, genuine within-cluster rate spread, separation D={D:.0f}.")
    print(f"Dphi={DPHI} rad/advance (U(1) gauge clock). Longitudinal window={LAM_LONG:.0f}.")

    def sweep(tag, k_c5, kappa_bw):
        w0s, g0s = [], []
        for s in seeds:
            r, c = run(specs, ell_V5=1.0, k_c5=0.0, steps=STEPS, seed=s)
            w, g, _ = summarize(r, c); w0s.append(w); g0s.append(g)
        w0, g0 = np.mean(w0s), np.mean(g0s)
        print(f"\n### {tag}  (k_c5={k_c5}, kappa_bw={kappa_bw}) ###")
        print(f"[uncoupled baseline] within-spread={w0:.4f}  cross-gap={g0:.4f}")
        print(f"{'ell_V5':>8}{'within':>10}{'cross-gap':>11}{'w/w0':>8}  regime")
        print("-" * 94)
        for ell in (0.5, 2.0, 5.0, 10.0, 30.0, 100.0):
            ws, gs = [], []
            for s in seeds:
                r, c = run(specs, ell_V5=ell, k_c5=k_c5, steps=STEPS, seed=s, kappa_bw=kappa_bw)
                w, g, _ = summarize(r, c); ws.append(w); gs.append(g)
            w, g = np.mean(ws), np.mean(gs); rw = w / w0 if w0 > 0 else float("nan")
            if rw < 0.5 and g > 0.5 * g0:
                reg = "LOCAL lock + gap preserved  <== attractive, finite-reach (required)"
            elif g < 0.3 * g0:
                reg = "gap COLLAPSED -> universal tick"
            elif rw > 0.85:
                reg = "no local locking"
            else:
                reg = "partial"
            print(f"{ell:>8.1f}{w:>10.4f}{g:>11.4f}{rw:>8.2f}  {reg}")

    # (1) HEADLINE: P12 sign (+), no imposed disorder -> does attraction EMERGE?
    sweep("P12 SIGN (+), no disorder", k_c5=1.5, kappa_bw=0.0)
    # (2) SIGN-FLIP control: - Coh must NOT bind (proves the + sign does the work)
    sweep("SIGN-FLIPPED (-) control", k_c5=-1.5, kappa_bw=0.0)
    # (3) with quenched P05 disorder (Step-4 finite-reach mechanism)
    sweep("P12 SIGN (+), quenched disorder", k_c5=1.5, kappa_bw=0.8)

    print("\n" + "=" * 94)
    print("READ: if (1) shows a window of ell_V5 with within-spread<<baseline (local lock) and")
    print("cross-gap preserved (time dilation), from + k_c5 ALONE, the attractive sign is DERIVED")
    print("from P12-Coh. (2) flipping the sign must break binding. (3) checks the finite reach")
    print("survives the substrate's own quenched disorder. Tier: MEASURED evidence for H-V5-Coh,")
    print("conditional on the coupling=coherence identification (G1); existence stays a P10 posit.")
    print("=" * 94)


if __name__ == "__main__":
    main()
