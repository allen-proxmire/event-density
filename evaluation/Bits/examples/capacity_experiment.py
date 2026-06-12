"""A1 - Channel-capacity experiment for the ED substrate.

Encode a K-ary message m into the initial condition of region A's LEFT half;
evolve the certified substrate; try to decode m from (i) region A's RIGHT half
[within-stratum channel] and (ii) region B [across the decoupling boundary].
Sweep K and read the recovered mutual information I(m; readout):

  within  I(m; A_right): plateau -> intrinsic capacity ceiling (an ED invariant);
                          tracks log2(K) -> near-lossless, no intrinsic number.
  across  I(m; B):       ~0 for all K -> capacity 0 (observable-INDEPENDENT
                          severance, stronger than MI~0 on chosen observables).
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from simulator import NodeState, StateVector, assign_stratum_ids, step  # noqa: E402
from size_sweep import build_substrate, COEFFS  # noqa: E402
from analysis.capacity import knn_decoder_mi  # noqa: E402

S = 32                         # nodes per cluster (converged regime)
HALF = S // 2
KS = [2, 4, 8, 16, 32]         # message-alphabet sizes
N_TRIALS = 600                 # trials per K
MAX_STEPS = 40 * S
NOISE = 0.03                   # within-message input jitter
REF_SEED = 777                 # FIXED reference for all non-message init


def run_message(m, K, jitter_seed):
    """Encode message m into A_left init; ALL other init held at a fixed reference
    (so the only cross-trial variation is the message). Evolve; return
    (A_right_rho, B_rho). Fixed A_right baseline isolates the within channel;
    fixed + decoupled B makes any m-dependence in B pure leakage."""
    g, A, B = build_substrate(S)
    A_left, A_right = A[:HALF], A[HALF:]
    ref = np.random.default_rng(REF_SEED)            # SAME every trial -> fixed baseline
    jit = np.random.default_rng(jitter_seed)

    level = (m / (K - 1)) * 0.4 if K > 1 else 0.0    # distinguishable message level
    sv = StateVector()
    for n in A_left:                                 # message: rho carries m + jitter
        sv[n] = NodeState(rho=float(level + jit.normal(0, NOISE)),
                          orientation=ref.normal(size=2))
    for n in A_right:                                # fixed baseline (same every trial)
        sv[n] = NodeState(rho=float(ref.uniform(0, 0.5)), orientation=ref.normal(size=2))
    for n in B:                                      # fixed baseline (same every trial)
        sv[n] = NodeState(rho=float(ref.uniform(0, 0.5)), orientation=ref.normal(size=2))
    sv[A[0]].active = True                           # front starts in the source half
    sv[B[0]].active = True
    strata = assign_stratum_ids(sv, g)

    for t in range(1, MAX_STEPS + 1):
        if step(sv, g, COEFFS, strata=strata) == 0:
            break
    return ([sv[n].rho for n in A_right], [sv[n].rho for n in B])


def measure_K(K):
    rng = np.random.default_rng(10_000 + K)
    msgs, A_right, B = [], [], []
    for trial in range(N_TRIALS):
        m = int(rng.integers(0, K))
        ar, b = run_message(m, K, jitter_seed=100_000 * K + trial)
        msgs.append(m); A_right.append(ar); B.append(b)
    msgs = np.array(msgs)
    I_within = knn_decoder_mi(np.array(A_right), msgs, K)
    I_across = knn_decoder_mi(np.array(B), msgs, K)
    return I_within, I_across


def main():
    print("=" * 68)
    print(f"A1 - CHANNEL CAPACITY (coding experiment)   S={S}, N={N_TRIALS}/K")
    print("=" * 68)
    print(f"\n  {'K':>4} {'log2(K)':>9} {'I_within':>10} {'I_across':>10} "
          f"{'within/cap?':>14}")
    print("  " + "-" * 56)

    rows = []
    for K in KS:
        Iw, Ia = measure_K(K)
        rows.append((K, np.log2(K), Iw, Ia))
        # crude per-row read: is within tracking log2(K) or saturating?
        frac = Iw / np.log2(K)
        tag = "tracks log2K" if frac > 0.85 else ("partial" if frac > 0.4 else "saturated")
        print(f"  {K:>4} {np.log2(K):>9.2f} {Iw:>10.3f} {Ia:>10.3f} {tag:>14}")

    Iw_last = [r[2] for r in rows]
    Ia_all = [r[3] for r in rows]
    # Plateau test: does within-MI stop growing at large K?
    growth_tail = Iw_last[-1] - Iw_last[-2]
    plateaued = growth_tail < 0.15
    across_zero = max(abs(x) for x in Ia_all) < 0.10

    print("  " + "-" * 56)
    print(f"\n  across-boundary I(m;B) max over K : {max(abs(x) for x in Ia_all):.3f} bits"
          f"  -> capacity ~ 0: {across_zero}")
    print(f"  within I growth on last K step    : {growth_tail:+.3f} bits"
          f"  -> plateaued (intrinsic ceiling?): {plateaued}")
    if plateaued:
        print(f"  within capacity estimate          : ~{Iw_last[-1]:.2f} bits "
              f"(intrinsic candidate)")
    else:
        print(f"  within MI still growing with K    : near-lossless; capacity "
              f"input-limited (NOT intrinsic)")
    print("\n" + "=" * 68)
    print(f"A1 COMPLETE - across-severance intrinsic: {across_zero}; "
          f"within-plateau: {plateaued}")
    print("=" * 68)
    return across_zero


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
