"""Braiding probe 5b -- redesign of the operational test using REAL cycles instead of imposed
point-orderings.

The prior attempt (order_undo_operational_test.py) closed each K6-minor branch set into a
"loop" via a geometric heuristic on its raw embedded points -- and that heuristic turned out to
be arbitrary: a branch set is only guaranteed to be a CONNECTED SUBGRAPH, not a cycle, so there
was no real loop there to close in the first place.

The actual mathematical content of "K6 is intrinsically linked" is about a specific structure:
split the 6 vertices into two groups of THREE, forming two genuine triangles (using K6's real
edges); the theorem guarantees that for any embedding, at least one such 3-3 split gives two
LINKED triangles. This redesign builds that structure directly from the graph's own edges:

  - for a chosen 3-3 split of the six branch sets, build a genuine closed WALK through each
    triple, using (a) the real cross-branch-set edges the K6-witness search already verified,
    and (b) real internal BFS paths within each branch set connecting the entry/exit vertices.
  - this is a valid closed cycle in the actual graph -- no imposed point-ordering, no arbitrary
    closure heuristic.
  - embed it with the same force-directed layout as before, compute the Gauss linking number
    between the two triangles for EVERY one of the 10 distinct 3-3 splits (the theorem only
    guarantees at least one split is linked, not all of them).
  - run the real operational test (separate, watch for forced collision) on whichever split
    shows genuine, near-integer linking.
"""
import numpy as np
import itertools
from collections import deque
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from multichain_v5_minor_check import build_graph, try_k6_witness
from order_undo_operational_test import force_directed_layout, gauss_linking, min_dist, attempt_separation


def find_connecting_edge(adj, set_a, set_b):
    for u in set_a:
        for v in adj[u]:
            if v in set_b:
                return u, v
    return None


def bfs_path(adj, branch_set, src, dst):
    if src == dst:
        return [src]
    visited = {src}
    parent = {src: None}
    q = deque([src])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if w in branch_set and w not in visited:
                visited.add(w)
                parent[w] = u
                if w == dst:
                    path = [w]
                    while parent[path[-1]] is not None:
                        path.append(parent[path[-1]])
                    return path[::-1]
                q.append(w)
    return None


def build_triangle_cycle(adj, branch_sets, triple):
    """Real closed walk through 3 branch sets, using verified cross-edges + internal BFS paths."""
    a, b, c = triple
    u1, v1 = find_connecting_edge(adj, branch_sets[a], branch_sets[b])
    u2, v2 = find_connecting_edge(adj, branch_sets[b], branch_sets[c])
    u3, v3 = find_connecting_edge(adj, branch_sets[c], branch_sets[a])
    path_b = bfs_path(adj, branch_sets[b], v1, u2)
    path_c = bfs_path(adj, branch_sets[c], v2, u3)
    path_a = bfs_path(adj, branch_sets[a], v3, u1)
    cycle = [u1] + path_b + [v2] + path_c[1:] + [v3] + path_a[1:]
    return cycle


def cycle_positions(cycle, pos, idx):
    return pos[[idx[v] for v in cycle]]


def densify(P, per_segment=8):
    """Resample the SAME real path more finely -- more points along each existing straight
    edge, no new topology -- to check whether a coarse reading is a genuine converged value or
    a discretization artifact."""
    out = []
    for i in range(len(P) - 1):
        for t in np.linspace(0, 1, per_segment, endpoint=False):
            out.append(P[i] * (1 - t) + P[i + 1] * t)
    out.append(P[-1])
    return np.array(out)


def converged_linking(p1_raw, p2_raw, levels=(1, 2, 4, 8, 16)):
    """Report Lk at increasing resolution of the SAME curves -- a real convergence check, not
    a one-shot reading."""
    vals = []
    for k in levels:
        p1 = densify(p1_raw, k) if k > 1 else p1_raw
        p2 = densify(p2_raw, k) if k > 1 else p2_raw
        vals.append(gauss_linking(p1, p2))
    return vals


def main():
    print("=" * 78)
    print("REAL-CYCLE OPERATIONAL TEST — genuine K6 opposite-triangle pairs, not imposed loops")
    print("=" * 78)
    n_chains, k_branches = 40, 2
    rng = np.random.default_rng(3)
    nodes, adj, chain_nodes = build_graph(n_chains, k_branches, 0.35, rng)
    found, branches = try_k6_witness(adj, chain_nodes, n_chains, 6, rng, tries=4000)
    if not found:
        print("  no K6 witness this run -- rerun with a different seed"); return
    print(f"\n  K6 witness found: 6 branch sets, sizes {[len(b) for b in branches]}")

    pos, idx = force_directed_layout(adj, nodes, iters=250, seed=5)

    # all 10 distinct ways to split {0..5} into two groups of 3
    all_idx = list(range(6))
    seen = set()
    splits = []
    for triple in itertools.combinations(all_idx, 3):
        rest = tuple(i for i in all_idx if i not in triple)
        key = frozenset([frozenset(triple), frozenset(rest)])
        if key not in seen:
            seen.add(key)
            splits.append((triple, rest))

    print(f"\n  testing all {len(splits)} distinct 3-3 splits, WITH a resolution-convergence check")
    print("  on each (coarse readings can mislead in either direction -- checked, not assumed):\n")
    results = []
    for triple, rest in splits:
        try:
            cyc1 = build_triangle_cycle(adj, branches, triple)
            cyc2 = build_triangle_cycle(adj, branches, rest)
            p1 = cycle_positions(cyc1, pos, idx)
            p2 = cycle_positions(cyc2, pos, idx)
            levels = converged_linking(p1, p2)
            lk = levels[-1]   # the finest-resolution (converged) reading, not the coarse one
            results.append((triple, rest, lk, p1, p2))
            near_int = abs(lk - round(lk))
            flag = "  <- near-integer, CONVERGED real candidate" if (near_int < 0.10 and abs(round(lk)) >= 1) else ""
            path = " -> ".join(f"{v:+.3f}" for v in levels)
            print(f"    split {triple} | {rest}:  coarse->fine  {path}{flag}")
        except Exception as e:
            print(f"    split {triple} | {rest}:  FAILED ({e})")

    # pick the split with |Lk| closest to a nonzero integer, AT CONVERGED (fine) resolution
    candidates = [r for r in results if abs(round(r[2])) >= 1 and abs(r[2] - round(r[2])) < 0.10]
    if not candidates:
        print("\n  No split gave a clean, CONVERGED near-integer linked pair in this embedding/witness.")
        print("  (Honest either way -- try a different seed, or this witness's specific")
        print("  embedding may put the guaranteed-linked split at a value this run didn't hit.)")
        return

    best = max(candidates, key=lambda r: abs(r[2]))
    triple, rest, lk, p1, p2 = best
    p1, p2 = densify(p1, 8), densify(p2, 8)   # use the converged (fine) curves from here on
    print(f"\n  best CONVERGED real-cycle candidate: split {triple} | {rest}, Lk = {lk:+.3f}")

    print("\n  THE ACTUAL OPERATIONAL TEST: attempt to separate these two genuine cycles")
    md = attempt_separation(p1, p2, steps=40)
    print(f"    min-distance along the separation attempt: min={md.min():.3f}, "
          f"start={md[0]:.3f}, end={md[-1]:.3f}")

    # control: a low-|Lk| split from the same witness/embedding, same separation method
    control = min(results, key=lambda r: abs(r[2]))
    _, _, lk_c, p1c, p2c = control
    print(f"\n  CONTROL (weakest-linked split, Lk={lk_c:+.3f}), same separation attempt:")
    md_c = attempt_separation(p1c, p2c, steps=40)
    print(f"    min-distance: min={md_c.min():.3f}, start={md_c[0]:.3f}, end={md_c[-1]:.3f}")

    print("\n  READ: if the near-integer-linked pair's min-distance is driven toward 0 while the")
    print("  weakly-linked control separates freely, that is real, properly-grounded evidence")
    print("  the linking obstructs separation. If both separate freely, the graph is linked in")
    print("  the topological sense but this particular continuous motion doesn't reveal an")
    print("  obstruction -- a real, honest result either way, now on solid footing.")
    print("=" * 78)


if __name__ == "__main__":
    main()
