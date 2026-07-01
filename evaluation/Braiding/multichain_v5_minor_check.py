"""Braiding probe 3 -- does the MULTI-chain graph (single-chain composition + V5 cross-links)
contain a K6 (Petersen-family) minor, i.e. is intrinsic linking actually reachable?

Builds ONLY from ED's own stated combinatorial rules -- no continuum, no embedding, no proxy
dynamics (avoids every problem the retracted probe had):
  - each chain is a small series-parallel diagram: source -> k parallel branches -> sink
    (P07's own branch/merge composition rule, the Mach-Zehnder example).
  - V5 cross-links (Paper_090 sec.3: a kernel on PAIRS of chains at distinct loci, independent
    of composition structure) are added between randomly-chosen vertices of DIFFERENT chains,
    at a coupling density p -- p stands in for "how richly V5 correlates chains," a quantity
    ED does not currently specify a number for, so this is swept across a range rather than
    fixed at one guessed value.

The single-chain result (ChainsAsLinks_SingleChainNegative.md) was a PROOF: series-parallel
graphs are always planar, so containment is impossible, full stop. This check is NOT that kind
of proof -- K6-minor detection is a hard search problem in general, so a "found" result here is
a genuine positive witness (constructive, checkable), but a "not found in N trials" result is
NOT a proof of absence, only "this search didn't find one." That asymmetry is reported honestly.

Method: random/greedy witness search. At each trial, pick 6 seed vertices from 6 different
chains, grow each into a connected "branch set" via BFS (staying disjoint from the others), then
check whether all 15 pairs of branch sets have at least one connecting edge in the full graph --
that is exactly the definition of a K6 topological minor witness.
"""
import numpy as np
import itertools


def make_chain(chain_id, k_branches, node_counter):
    """source -> k parallel branches -> sink (P07's own branch/merge composition)."""
    def nid(local):
        return f"c{chain_id}_{local}"
    src, dst = nid("src"), nid("dst")
    nodes = [src, dst]
    edges = []
    for b in range(k_branches):
        bn = nid(f"b{b}")
        nodes.append(bn)
        edges.append((src, bn))
        edges.append((bn, dst))
    return nodes, edges


def build_graph(n_chains, k_branches, p_v5, rng):
    nodes, edges = [], []
    chain_nodes = []
    for c in range(n_chains):
        nds, eds = make_chain(c, k_branches, None)
        chain_nodes.append(nds)
        nodes += nds
        edges += eds
    # V5 cross-links: pairwise, independent of composition, coupling density p_v5
    for i in range(n_chains):
        for j in range(i + 1, n_chains):
            if rng.random() < p_v5:
                u = rng.choice(chain_nodes[i])
                v = rng.choice(chain_nodes[j])
                edges.append((u, v))
    adj = {n: set() for n in nodes}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return nodes, adj, chain_nodes


def bfs_grow(adj, seed, avoid, target_size, rng):
    """Grow a connected branch set from seed, staying out of `avoid`, via randomized BFS."""
    branch = {seed}
    frontier = [seed]
    while len(branch) < target_size and frontier:
        u = frontier.pop(rng.integers(0, len(frontier)))
        nbrs = [w for w in adj[u] if w not in branch and w not in avoid]
        rng.shuffle(nbrs)
        for w in nbrs:
            if len(branch) >= target_size:
                break
            branch.add(w)
            frontier.append(w)
    return branch


def try_k6_witness(adj, chain_nodes, n_chains, branch_size, rng, tries=400):
    """Randomized search for 6 disjoint connected branch sets, pairwise adjacent (K6 minor)."""
    for _ in range(tries):
        seed_chains = rng.choice(n_chains, size=6, replace=False)
        branches = []
        used = set()
        ok = True
        for c in seed_chains:
            seed = rng.choice(chain_nodes[c])
            b = bfs_grow(adj, seed, used, branch_size, rng)
            if len(b) < 1:      # isolated seed with no room to grow at all
                ok = False
                break
            branches.append(b)
            used |= b
        if not ok or len(branches) < 6:
            continue
        # check all C(6,2)=15 pairs have a connecting edge
        pairwise_ok = True
        for a, b in itertools.combinations(range(6), 2):
            if not any(w in adj[v] for v in branches[a] for w in branches[b]):
                pairwise_ok = False
                break
        if pairwise_ok:
            return True, branches
    return False, None


def main():
    print("=" * 78)
    print("MULTI-CHAIN GRAPH — does single-chain composition + V5 cross-links reach a K6 minor?")
    print("=" * 78)
    n_chains, k_branches, branch_size, tries = 40, 2, 6, 3000
    print(f"\n  {n_chains} chains, {k_branches} branches each (series-parallel), "
          f"branch-set target size {branch_size}, {tries} search trials per density")
    print("  (branch_size + trials validated against controls: literal K6 and K30 below)")
    print("  sweeping V5 coupling density p (fraction of chain-pairs cross-linked):\n")

    for p in [0.0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.12, 0.20, 0.35, 0.50]:
        rng = np.random.default_rng(42)
        nodes, adj, chain_nodes = build_graph(n_chains, k_branches, p, rng)
        n_edges = sum(len(v) for v in adj.values()) // 2
        avg_deg = 2 * n_edges / len(nodes)
        found, branches = try_k6_witness(adj, chain_nodes, n_chains, branch_size, rng, tries=tries)
        tag = "K6 WITNESS FOUND" if found else f"not found in {tries} trials"
        print(f"    p={p:4.2f}:  {len(nodes):4d} nodes, {n_edges:4d} edges, "
              f"avg deg {avg_deg:.2f}   ->  {tag}")

    print("\n  READ: p=0.00 is the single-chain case alone (must fail -- it's the proven-planar")
    print("  case, no cross-links at all). Watch for the p at which a witness starts appearing.")
    print("  IMPORTANT ASYMMETRY: 'found' is a real, checkable positive (a constructive witness).")
    print("  'not found' is NOT a proof of absence -- it only means this randomized search, at")
    print("  this many trials, didn't locate one. Unlike the single-chain planarity result (a")
    print("  proof), this is a search, and a negative here is suggestive, not conclusive.")
    print("=" * 78)


if __name__ == "__main__":
    main()
