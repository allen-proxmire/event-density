"""Braiding probe 4 -- does GEOMETRICALLY LOCAL V5 coupling (not uniform-random) still reach a
K6 minor, or does the earlier positive result depend on V5 correlating chains globally at random?

The prior check (multichain_v5_minor_check.py) added V5 cross-links uniformly at random between
ANY two chains, regardless of separation -- but V5's own definition (Paper_090 sec.3) is a
proximity kernel, finite reach in space (ell_V5) and time (tau_V5), so real V5 coupling should
be LOCAL: a chain mostly correlates with nearby chains, rarely with distant ones. Uniform-random
coupling is known to be much MORE efficient at building rich minors than local coupling at the
same average degree (this is the whole point of small-world theory), so the prior result may
have overstated how easy intrinsic linking is to reach.

To test this WITHOUT re-introducing the circularity problem (assuming a 3D embedding to test
whether 3D embedding matters), "locality" here is defined combinatorially: chains are given an
abstract index ordering (a label, not spatial coordinates -- it could represent commitment order
or any other purely graph-native adjacency notion), and V5 links are built with a
Watts-Strogatz-style MIX of local (nearby-index) edges and long-range (random) edges, controlled
by a single rewiring parameter beta:
  - beta=0:  PURELY LOCAL -- every V5 edge connects nearby-index chains only (a ring lattice).
  - beta=1:  PURELY RANDOM -- every V5 edge goes to a uniformly random chain (recovers probe 3).
  - beta in between: a small-world mixture.

This isolates the real question: is uniform-randomness ITSELF doing the work in probe 3, or does
local coupling get there too, just at higher density? If beta=0 never reaches K6 no matter how
high the local reach/density goes, that is a real, structurally meaningful limit on the previous
result -- not a proof about ED (still doesn't touch the operational "is this what holds order"
question), but an honest correction to how easily reachable the prior result made intrinsic
linking look.
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from multichain_v5_minor_check import make_chain, try_k6_witness


def build_local_graph(n_chains, k_branches, reach, density, beta, rng):
    """Ring-lattice-plus-rewiring V5 coupling: each chain candidate-links to its `reach` nearest
    neighbors (by abstract index) at probability `density`; each such edge is, independently,
    REWIRED to a uniformly random other chain with probability beta (Watts-Strogatz)."""
    nodes, edges = [], []
    chain_nodes = []
    for c in range(n_chains):
        nds, eds = make_chain(c, k_branches, None)
        chain_nodes.append(nds)
        nodes += nds
        edges += eds

    for i in range(n_chains):
        for d in range(1, reach + 1):
            j = (i + d) % n_chains
            if i == j or rng.random() >= density:
                continue
            if rng.random() < beta:
                j = rng.integers(0, n_chains)
                tries = 0
                while j == i and tries < 5:
                    j = rng.integers(0, n_chains)
                    tries += 1
                if j == i:
                    continue
            u = rng.choice(chain_nodes[i])
            v = rng.choice(chain_nodes[j])
            edges.append((u, v))

    adj = {n: set() for n in nodes}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return nodes, adj, chain_nodes


def main():
    print("=" * 78)
    print("LOCAL vs RANDOM V5 COUPLING — does purely local coupling ever reach a K6 minor?")
    print("=" * 78)
    n_chains, k_branches, branch_size, tries = 40, 2, 6, 3000
    print(f"\n  {n_chains} chains, {k_branches} branches each, branch-set size {branch_size}, "
          f"{tries} trials")
    print("  (search validated against controls in probe 3 already — literal K6, K30 both found)")

    for reach, density in [(4, 0.9), (8, 0.9), (14, 0.9), (19, 0.9)]:
        print(f"\n  --- local reach={reach} (max possible neighbors, density={density}) ---")
        for beta in [0.0, 0.05, 0.10, 0.20, 0.40, 0.70, 1.0]:
            rng = np.random.default_rng(7)
            nodes, adj, chain_nodes = build_local_graph(n_chains, k_branches, reach, density, beta, rng)
            n_edges = sum(len(v) for v in adj.values()) // 2
            avg_deg = 2 * n_edges / len(nodes)
            found, _ = try_k6_witness(adj, chain_nodes, n_chains, branch_size, rng, tries=tries)
            tag = "K6 FOUND" if found else "not found"
            print(f"    beta={beta:4.2f} (0=purely local, 1=purely random):  "
                  f"{n_edges:4d} edges, avg deg {avg_deg:.2f}  ->  {tag}")

    print("\n  READ: beta=0 rows are PURELY LOCAL coupling (nearest-index-neighbors only, no")
    print("  long-range links at all) — if K6 never appears there even at the widest local reach")
    print("  (reach=19, i.e. connecting to nearly half the other chains), that means locality")
    print("  ITSELF blocks intrinsic linking regardless of density, and probe 3's positive result")
    print("  depended specifically on long-range (non-local) mixing, not on density alone.")
    print("=" * 78)


if __name__ == "__main__":
    main()
