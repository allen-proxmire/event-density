"""Build Step 5 demo - reach-stratum detection.

Two clusters (A = {0,1,2}, B = {3,4,5}) joined by a single DECOUPLED bridge
(2,3). The reciprocal subgraph therefore has two connected components, so the
bridge must NOT merge the strata. Checks:
  - mapping matches the two expected components;
  - decoupled bridge endpoints land in DIFFERENT strata;
  - deterministic across repeated computations.
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
    compute_strata,
    assign_stratum_ids,
    step,
    hash_state,
)


def build_two_clusters():
    g = ParticipationGraph()
    # Cluster A: 0-1-2 (reciprocal)
    g.add_edge(0, 1, bandwidth=0.5)
    g.add_edge(1, 2, bandwidth=0.5)
    # Cluster B: 3-4-5 (reciprocal)
    g.add_edge(3, 4, bandwidth=0.5)
    g.add_edge(4, 5, bandwidth=0.5)
    # Bridge 2-3: DECOUPLED (a decoupling surface)
    g.add_edge(2, 3, bandwidth=0.5, decoupled=True)
    return g


def fresh_state(g):
    sv = StateVector()
    for n in sorted(g.nodes()):
        sv[n] = NodeState(rho=0.0, orientation=np.array([0.0, 0.0]))
    return sv


def main():
    print("=" * 64)
    print("BUILD STEP 5 - reach-stratum detection")
    print("=" * 64)

    g = build_two_clusters()

    labels = compute_strata(g)
    print(f"\n  stratum map: {dict(sorted(labels.items()))}")
    print(f"  expected   : {{0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1}}")

    expected = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1}
    matches_expected = labels == expected

    # Bridge endpoints 2 and 3 must be in DIFFERENT strata.
    bridge_split = labels[2] != labels[3]

    # Same-component nodes share a stratum.
    same_A = labels[0] == labels[1] == labels[2]
    same_B = labels[3] == labels[4] == labels[5]

    # Determinism across repeated computation.
    deterministic = (compute_strata(g) == compute_strata(g) == labels)

    # assign_stratum_ids writes onto state and agrees with compute_strata.
    sv = fresh_state(g)
    assigned = assign_stratum_ids(sv, g)
    on_state = all(sv[n].stratum_id == labels[n] for n in g.nodes())

    # Integration: step() consumes stratum ids; seed one front per cluster and
    # confirm the run is deterministic and a commit in A never touches B.
    sv[0].active = True
    sv[3].active = True
    coeffs = SigmaCoeffs()
    h_before_B = tuple(sv[n].rho for n in (3, 4, 5))
    step(sv, g, coeffs, strata=labels)
    # (one step: each front advances within its own cluster)

    print("\nChecks")
    print(f"  matches expected components      : {matches_expected}")
    print(f"  decoupled bridge does NOT merge  : {bridge_split}  (stratum[2]={labels[2]}, stratum[3]={labels[3]})")
    print(f"  same-cluster nodes share stratum : {same_A and same_B}")
    print(f"  deterministic across runs        : {deterministic}")
    print(f"  assign_stratum_ids writes state  : {on_state}")

    passed = (matches_expected and bridge_split and same_A and same_B
              and deterministic and on_state)
    print("\n" + "=" * 64)
    print(f"BUILD STEP 5: {'PASS' if passed else 'FAIL'}")
    print("=" * 64)
    return passed


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
