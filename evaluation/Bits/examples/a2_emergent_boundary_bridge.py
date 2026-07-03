"""A2 bridge - does an EMERGENT (dynamically-grown) decoupling boundary
reproduce A1's exactly-zero channel capacity, or the "soft wall" (nonzero
capacity) that Emergent_Decoupling_Surfaces.md predicts?

Per that foundations note: under the certified Bits update loop, a decoupling
surface can only ever be INSTALLED (a build-time flag), never EMERGE, because
the loop evolves node state on a static graph and never writes back to edge
structure. The one route that could produce a genuine structural cut is a
bandwidth-COLLAPSE dynamics on P04 (b_uv -> 0 pruning the edge) -- exactly
what the Phase-3 GR arc's dynamical-bandwidth rule already does
(dynamical_bandwidth.py: b_dot = D*grad^2(b) - kappa*rho, GR-III "The Arrow's
Engine"), just never pointed at the Bits capacity measurement.

Admissibility (the note's own flagged open question): this wires two already-
audited things together, it does not invent new substrate physics. (a) P04
bandwidth is already primitive. (b) The dynamical-bandwidth rule is already
built, run, and cross-checked against the primitives elsewhere in the corpus
(Newtonian fixed point corr 0.999, r_s~M, horizon area-law entropy, Hawking
kappa~1/r_h all measured from this exact rule in the GR arc). No new
postulate is introduced here.

Construction:
  1. Run the GR-arc rule to a strong-coupling steady state on an SxS grid,
     producing a bandwidth field b(x, y) with a genuine b<=1e-9 horizon.
  2. Build a ParticipationGraph mirroring the grid's 4-connected lattice:
     edge bandwidth = min(b) of its two endpoints (a channel is bottlenecked
     by its weakest participant -- matches the note's own P_K = sqrt(b)*e^{i
     pi} framing, where either side at b=0 kills the channel; an average
     would let a b=0 node's edges read as open just because its neighbor
     isn't also at zero, which a first pass of this script confirmed happens
     and is a construction artifact, not a physics result); edge decoupled
     iff that min bandwidth <= BW_HORIZON_THRESHOLD.
  3. Run the A1-style coding experiment: encode a K-ary message inside the
     horizon, evolve the certified Sigma-maximizing update loop, try to
     decode it from just outside the horizon (near) and from deep field
     (far, a control). Compare recovered capacity to A1's ~0-bit baseline.

Scope (first pass, stated honestly): small grid, small trial count, 2 values
of K. This is a first cut meant to distinguish "clean zero" / "soft leak" /
"no cut formed at all", not a high-precision capacity estimate.
"""
import os
import sys

import numpy as np

_BITS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_EVAL_ROOT = os.path.dirname(_BITS_ROOT)
sys.path.insert(0, _BITS_ROOT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(_EVAL_ROOT, "DynamicalBandwidth"))

from simulator import (  # noqa: E402
    ParticipationGraph, NodeState, StateVector, SigmaCoeffs,
    assign_stratum_ids, step,
)
from analysis.capacity import knn_decoder_mi  # noqa: E402
import dynamical_bandwidth as dbw  # noqa: E402

COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5, extinction_threshold=-2.0)
BW_HORIZON_THRESHOLD = 1e-6
KS = [2, 4]
N_TRIALS = 60
MAX_STEPS = 500
NOISE = 0.03
REF_SEED = 777


def build_emergent_substrate(S=36, kappa=8e-3, rho_amp=4.0, rho_sigma=4.0, steps=6000):
    """Run the GR-arc dynamical-bandwidth rule to steady state; build a
    ParticipationGraph over the grid whose edges are decoupled wherever the
    converged bandwidth field crosses BW_HORIZON_THRESHOLD."""
    st = dbw.run(S=S, kappa=kappa, rho_amp=rho_amp, rho_sigma=rho_sigma, steps=steps)
    b, r = st["b"], st["r"]
    horizon = b <= 1e-9
    if horizon.sum() == 0:
        raise RuntimeError(
            f"no horizon formed at kappa={kappa}, rho_amp={rho_amp} -- increase coupling")

    g = ParticipationGraph()

    def nid(i, j):
        return i * S + j

    for i in range(S):
        for j in range(S):
            g.add_node(nid(i, j))

    for i in range(S):
        for j in range(S):
            if i + 1 < S:
                bw = min(b[i, j], b[i + 1, j])
                g.add_edge(nid(i, j), nid(i + 1, j), bandwidth=bw,
                           decoupled=bool(bw <= BW_HORIZON_THRESHOLD))
            if j + 1 < S:
                bw = min(b[i, j], b[i, j + 1])
                g.add_edge(nid(i, j), nid(i, j + 1), bandwidth=bw,
                           decoupled=bool(bw <= BW_HORIZON_THRESHOLD))

    interior = [nid(i, j) for i in range(S) for j in range(S) if horizon[i, j]]
    r_h = r[horizon].max()
    cx = cy = (S - 1) / 2.0
    near_exterior, far_exterior = [], []
    for i in range(S):
        for j in range(S):
            if horizon[i, j]:
                continue
            rr = float(np.hypot(i - cx, j - cy))
            if rr < r_h + 3:
                near_exterior.append(nid(i, j))
            elif rr > r_h + 8:
                far_exterior.append(nid(i, j))
    return g, interior, near_exterior, far_exterior, b, horizon, r_h


def run_message(g, interior, exterior, m, K, jitter_seed):
    """Encode message m inside the horizon; fixed reference baseline
    elsewhere; evolve; return the exterior readout."""
    ref = np.random.default_rng(REF_SEED)
    jit = np.random.default_rng(jitter_seed)
    level = (m / (K - 1)) * 0.4 if K > 1 else 0.0

    sv = StateVector()
    for n in g.nodes():
        sv[n] = NodeState(rho=float(ref.uniform(0.0, 0.5)), orientation=ref.normal(size=2))
    for n in interior:
        sv[n].rho = float(level + jit.normal(0, NOISE))
    strata = assign_stratum_ids(sv, g)

    sv[interior[0]].active = True
    sv[exterior[0]].active = True
    for _ in range(1, MAX_STEPS + 1):
        if step(sv, g, COEFFS, strata=strata) == 0:
            break
    return [sv[n].rho for n in exterior]


def measure_K(g, interior, exterior, K, n_trials=N_TRIALS):
    rng = np.random.default_rng(20_000 + K)
    msgs, readouts = [], []
    for trial in range(n_trials):
        m = int(rng.integers(0, K))
        y = run_message(g, interior, exterior, m, K, jitter_seed=200_000 * K + trial)
        msgs.append(m)
        readouts.append(y)
    return knn_decoder_mi(np.array(readouts), np.array(msgs), K)


def main():
    print("=" * 72)
    print("A2 BRIDGE - emergent (dynamically-grown) decoupling boundary")
    print("=" * 72)
    g, interior, near_ext, far_ext, b, horizon, r_h = build_emergent_substrate()
    print(f"  horizon: {horizon.sum()} nodes, r_h~{r_h:.1f}, "
          f"interior={len(interior)}, near-exterior={len(near_ext)}, "
          f"far-exterior={len(far_ext)}")
    if len(near_ext) == 0 or len(far_ext) == 0:
        print("  ERROR: exterior region empty at this grid size -- widen grid or rings.")
        return None

    results = {}
    for label, exterior in (("near", near_ext), ("far", far_ext)):
        print(f"\n  -- {label} exterior --")
        print(f"  {'K':>4} {'log2(K)':>9} {'I(m;readout)':>14}")
        vals = []
        for K in KS:
            I = measure_K(g, interior, exterior, K)
            vals.append(I)
            print(f"  {K:>4} {np.log2(K):>9.2f} {I:>14.3f}")
        max_abs = max(abs(v) for v in vals)
        results[label] = max_abs
        print(f"  max |I| over K = {max_abs:.3f} bits -> capacity ~0: {max_abs < 0.10}")

    print("\n" + "=" * 72)
    print(f"A2 BRIDGE COMPLETE - near-exterior capacity~0: {results['near'] < 0.10}, "
          f"far-exterior capacity~0: {results['far'] < 0.10}")
    print("=" * 72)
    return results


if __name__ == "__main__":
    main()
