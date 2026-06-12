"""Build Step 6 demo - decoupling-surface detection.

Reuses the two-cluster graph from strata_demo (A={0,1,2}, B={3,4,5}, decoupled
bridge (2,3)). Verifies that:
  - the decoupled bridge (2,3) is detected as a surface;
  - boundary nodes are exactly {2, 3};
  - boundary_map anchors each boundary node to its across-surface partner;
  - strata are unchanged (boundary detection does not perturb the partition).
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from simulator import (  # noqa: E402
    ParticipationGraph,
    compute_strata,
    detect_decoupled_edges,
    detect_boundary_nodes,
    boundary_map,
)


def build_two_clusters():
    g = ParticipationGraph()
    g.add_edge(0, 1, bandwidth=0.5)
    g.add_edge(1, 2, bandwidth=0.5)
    g.add_edge(3, 4, bandwidth=0.5)
    g.add_edge(4, 5, bandwidth=0.5)
    g.add_edge(2, 3, bandwidth=0.5, decoupled=True)   # decoupling surface
    return g


def main():
    print("=" * 64)
    print("BUILD STEP 6 - decoupling-surface detection")
    print("=" * 64)

    g = build_two_clusters()

    edges = detect_decoupled_edges(g)
    bnodes = detect_boundary_nodes(g)
    bmap = boundary_map(g)
    strata = compute_strata(g)

    print(f"\n  decoupled edges : {edges}")
    print(f"  boundary nodes  : {sorted(bnodes)}")
    print(f"  boundary_map    : {bmap}")
    print(f"  strata          : {dict(sorted(strata.items()))}")

    # Checks
    bridge_detected = edges == [(2, 3)]
    boundary_exact = bnodes == {2, 3}
    map_correct = bmap == {2: [3], 3: [2]}
    strata_unchanged = strata == {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1}
    deterministic = (detect_decoupled_edges(g) == edges
                     and boundary_map(g) == bmap)

    print("\nChecks")
    print(f"  (2,3) detected as decoupled      : {bridge_detected}")
    print(f"  boundary nodes == {{2,3}}          : {boundary_exact}")
    print(f"  boundary_map correct             : {map_correct}")
    print(f"  strata unchanged                 : {strata_unchanged}")
    print(f"  deterministic across runs        : {deterministic}")

    passed = (bridge_detected and boundary_exact and map_correct
              and strata_unchanged and deterministic)
    print("\n" + "=" * 64)
    print(f"BUILD STEP 6: {'PASS' if passed else 'FAIL'}")
    print("=" * 64)
    return passed


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
