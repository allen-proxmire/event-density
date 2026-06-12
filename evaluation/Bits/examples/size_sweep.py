"""Robustness program, axis 1 - Delta vs substrate size.

Sweeps cluster size S over {8, 16, 32, 64, 128}. At each size: build two S-node
chains joined by a decoupled bridge, run an ensemble of independent-seed runs to
the fixed point, and measure:

    M1 = within-stratum  MI(A_left ; A_right)   [bits]
    M2 = across-boundary MI(A ; B)              [bits]
    Delta = M1 - M2

Question: does Delta settle to a size-independent value (-> intrinsic), follow a
clean trend (-> scaling law), or wander (-> configuration noise)? Also checks
that factorization (M2 ~ 0) holds at every size - it is structural, so it must.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from simulator import (  # noqa: E402
    ParticipationGraph, NodeState, StateVector, SigmaCoeffs,
    assign_stratum_ids, detect_decoupled_edges, step,
)
from analysis.delta import compute_all  # noqa: E402

SIZES = [8, 16, 32, 64, 128]
N_ENSEMBLE = 200
COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5, extinction_threshold=-2.0)


def build_substrate(S):
    g = ParticipationGraph()
    A = list(range(S))
    B = list(range(S, 2 * S))
    for chain in (A, B):
        for i in range(len(chain) - 1):
            g.add_edge(chain[i], chain[i + 1], bandwidth=0.5)
    g.add_edge(A[-1], B[0], bandwidth=0.5, decoupled=True)
    return g, A, B


def run_one(S, seed_a, seed_b, max_steps):
    g, A, B = build_substrate(S)
    sv = StateVector()
    rng_a = np.random.default_rng(seed_a)
    rng_b = np.random.default_rng(seed_b)
    for n in A:
        sv[n] = NodeState(rho=float(rng_a.uniform(0.0, 0.5)),
                          orientation=rng_a.normal(size=2))
    for n in B:
        sv[n] = NodeState(rho=float(rng_b.uniform(0.0, 0.5)),
                          orientation=rng_b.normal(size=2))
    sv[A[0]].active = True
    sv[B[0]].active = True
    strata = assign_stratum_ids(sv, g)
    steps = 0
    for t in range(1, max_steps + 1):
        c = step(sv, g, COEFFS, strata=strata)
        steps = t
        if c == 0:
            break
    return sv, A, B, steps, (steps < max_steps)


def measure(S, N=N_ENSEMBLE):
    max_steps = max(300, 40 * S)
    A_s, B_s, AL_s, AR_s = [], [], [], []
    natural = 0
    for k in range(N):
        sv, A, B, steps, term = run_one(S, 1000 + k, 5000 + k, max_steps)
        natural += int(term)
        A_s.append(sum(sv[n].rho for n in A))
        B_s.append(sum(sv[n].rho for n in B))
        half = len(A) // 2
        AL_s.append(sum(sv[n].rho for n in A[:half]))
        AR_s.append(sum(sv[n].rho for n in A[half:]))
    ds = {"A": np.array(A_s), "B": np.array(B_s),
          "A_left": np.array(AL_s), "A_right": np.array(AR_s)}
    d = compute_all(ds)
    d["natural_fraction"] = natural / N
    d["size"] = S
    return d


def main():
    print("=" * 72)
    print("ROBUSTNESS SWEEP - Delta vs substrate size")
    print(f"  ensemble N={N_ENSEMBLE} per size, bins=2, Miller-Madow, units=bits")
    print("=" * 72)
    print(f"\n  {'S':>5} {'M1':>10} {'M2':>10} {'M3':>10} "
          f"{'Delta':>10} {'M2~0?':>8} {'nat%':>6}")
    print("  " + "-" * 64)

    rows = []
    for S in SIZES:
        d = measure(S)
        m2_zero = abs(d["M2_bits"]) < 0.02
        rows.append(d)
        print(f"  {S:>5} {d['M1_bits']:>+10.4f} {d['M2_bits']:>+10.4f} "
              f"{d['M3_bits']:>+10.4f} {d['delta_bits']:>+10.4f} "
              f"{str(m2_zero):>8} {d['natural_fraction']*100:>5.0f}%")

    deltas = [r["delta_bits"] for r in rows]
    m1s = [r["M1_bits"] for r in rows]
    spread = max(deltas) - min(deltas)
    m2_all_zero = all(abs(r["M2_bits"]) < 0.02 for r in rows)

    print("  " + "-" * 64)
    print(f"\n  Delta range over sizes : [{min(deltas):+.4f}, {max(deltas):+.4f}]  "
          f"spread = {spread:.4f} bits")
    print(f"  M1 range               : [{min(m1s):+.4f}, {max(m1s):+.4f}]")
    print(f"  factorization (M2~0) holds at every size : {m2_all_zero}")

    # Crude trend read.
    if spread < 0.03:
        trend = "FLAT - Delta ~ size-independent (intrinsic candidate)"
    elif deltas[-1] < deltas[0] - 0.03:
        trend = "DECREASING with size (possible scaling law / vanishing)"
    elif deltas[-1] > deltas[0] + 0.03:
        trend = "INCREASING with size (possible scaling law)"
    else:
        trend = "NON-MONOTONE / noisy (no clean convergence yet)"
    print(f"  trend read             : {trend}")

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sweep_output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "size_sweep.json"), "w", encoding="utf-8") as fh:
        json.dump({"sizes": SIZES, "N": N_ENSEMBLE,
                   "rows": [{k: (float(v) if isinstance(v, (int, float, np.floating))
                                 else v) for k, v in r.items()} for r in rows],
                   "spread": float(spread), "trend": trend,
                   "factorization_holds": bool(m2_all_zero)}, fh, indent=2)

    # Optional plot.
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(SIZES, m1s, "o-", label="M1 (within-stratum)")
        ax.plot(SIZES, [r["delta_bits"] for r in rows], "s-", label="Delta")
        ax.plot(SIZES, [r["M2_bits"] for r in rows], "^--", label="M2 (across)")
        ax.axhline(0, color="gray", lw=0.6)
        ax.set_xlabel("cluster size S (nodes per stratum)")
        ax.set_ylabel("bits")
        ax.set_xscale("log", base=2)
        ax.set_title("Delta vs substrate size")
        ax.legend()
        fig.tight_layout()
        fig.savefig(os.path.join(out_dir, "size_sweep.png"), dpi=120)
        print(f"  plot saved             : sweep_output/size_sweep.png")
    except Exception as e:
        print(f"  (plot skipped: {e})")

    print("\n" + "=" * 72)
    print(f"SWEEP COMPLETE - factorization holds: {m2_all_zero}; trend: {trend}")
    print("=" * 72)
    return m2_all_zero


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
