"""Build Step 4 demo - the ED substrate update loop.

Constructs a small path graph, seeds one active front, runs several steps, and
checks the two properties the update loop must guarantee:
  Gate 1 (monotonicity): rho never decreases, anywhere, between steps.
  Gate 2 (acyclicity):   the global state hash is distinct every step.

Plus a determinism re-run (identical trajectory for identical inputs).
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from simulator import (  # noqa: E402
    ParticipationGraph,
    NodeState,
    StateVector,
    SigmaCoeffs,
    step,
    hash_state,
)

N = 5          # path nodes 0-1-2-3-4
STEPS = 6


def build_path(n):
    g = ParticipationGraph()
    g.add_node(0)
    for i in range(1, n):
        g.add_edge(i - 1, i, bandwidth=0.5)   # uniform bw ⇒ ties resolved by node id
    return g


def fresh_state(n, seed_node=0):
    sv = StateVector()
    for i in range(n):
        sv[i] = NodeState(rho=0.0, orientation=np.array([0.0, 0.0]))
    sv[seed_node].active = True
    return sv


def rho_vector(sv, n):
    return [sv[i].rho for i in range(n)]


def run(coeffs, label):
    g = build_path(N)
    sv = fresh_state(N)
    print(f"\n--- {label} ---")
    hashes = []
    rho_prev = rho_vector(sv, N)
    print(f"  step 0  rho={rho_prev}  hash={hash_state(sv) & 0xffffffff:08x}")
    hashes.append(hash_state(sv))
    monotone = True
    for t in range(1, STEPS + 1):
        commits = step(sv, g, coeffs)
        rho_now = rho_vector(sv, N)
        h = hash_state(sv)
        # monotonicity: elementwise non-decreasing vs previous step
        if any(b < a for a, b in zip(rho_prev, rho_now)):
            monotone = False
        print(f"  step {t}  rho={rho_now}  commits={commits}  "
              f"hash={h & 0xffffffff:08x}")
        hashes.append(h)
        rho_prev = rho_now
    distinct = len(set(hashes)) == len(hashes)
    return hashes, monotone, distinct


def main():
    print("=" * 64)
    print("BUILD STEP 4 - update loop (Gates 1 & 2 preview)")
    print("=" * 64)

    coeffs = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5)  # no extinction: bounded-step demo

    h1, monotone, distinct = run(coeffs, "run 1")
    h2, _, _ = run(coeffs, "run 2 (determinism check)")
    deterministic = (h1 == h2)

    print("\nChecks")
    print(f"  Gate 1  monotonicity (rho never decreases) : {monotone}")
    print(f"  Gate 2  acyclicity   (distinct hash/step)  : {distinct}")
    print(f"  determinism (run1 hashes == run2 hashes)   : {deterministic}")

    passed = monotone and distinct and deterministic
    print("\n" + "=" * 64)
    print(f"BUILD STEP 4: {'PASS' if passed else 'FAIL'}")
    print("=" * 64)
    return passed


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
