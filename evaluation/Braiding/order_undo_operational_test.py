"""Braiding probe 5 -- the operational test the whole arc has been building toward: given a
multi-chain graph that provably contains a K6 (intrinsically-linked) minor, does trying to
UNDO the committed order between two of its chains actually force a collision, the same way
probe 1 showed for an idealized pair of linked loops?

This is the test the scoping note named as the real content of the hypothesis, and the two prior
positive results (K6 reachable; locality doesn't change that) only ever established that linking
is POSSIBLE in the graph. Neither showed linking is what's actually holding an order.

Method, staying honest about what's assumed and what's not:
  1. Build the same multi-chain graph as before (series-parallel chains + V5 cross-links) at a
     density known to contain a K6 minor. Extract an actual witness (6 branch sets).
  2. This graph has no natural coordinates -- it's abstract. To even ask "does separating two
     chains force a collision," SOME embedding into 3D is needed. This is legitimate, not the
     earlier circularity: Robertson-Seymour-Thomas guarantees intrinsic linking shows up in
     EVERY embedding, so testing with one honestly-built embedding (a force-directed layout
     driven by the graph's own edges, not hand-placed to force an answer) is a fair test of
     whether that guaranteed linking translates into an order-holding obstruction.
  3. Build a closed loop through each branch set's embedded points (a minimum-distance nearest-
     neighbor tour, closed) -- a labeled modeling step, needed because linking number is only
     well-defined for closed curves.
  4. Measure pairwise linking numbers across all 15 loop pairs in this embedding; find the most
     linked pair.
  5. THE ACTUAL TEST: attempt to continuously separate that pair (translate one chain's loop away
     from the other, self-avoiding) exactly as probe 1 did for the idealized loops, and watch
     whether minimum distance is forced toward zero (order held) or stays clear (order not held).
  6. Control: run the identical separation attempt on the least-linked pair in the SAME
     embedding, which should separate freely -- confirms the test discriminates linked from
     unlinked pairs rather than reporting a forced collision for everything indiscriminately.
"""
import numpy as np
import itertools
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from multichain_v5_minor_check import build_graph, try_k6_witness


def force_directed_layout(adj, nodes, iters=300, seed=0):
    """Simple spring layout: edges attract, all pairs repel -- an honest embedding driven by the
    graph's own connectivity, not hand-placed."""
    rng = np.random.default_rng(seed)
    idx = {n: i for i, n in enumerate(nodes)}
    pos = rng.normal(scale=1.0, size=(len(nodes), 3))
    edges = [(idx[u], idx[v]) for u in adj for v in adj[u] if idx[u] < idx[v]]
    for it in range(iters):
        disp = np.zeros_like(pos)
        # repulsion (all pairs, subsampled for speed on larger graphs)
        diff = pos[:, None, :] - pos[None, :, :]
        dist2 = np.sum(diff ** 2, axis=2) + 1e-6
        rep = diff / dist2[:, :, None] ** 1.5
        disp += 0.02 * np.sum(rep, axis=1)
        # attraction along edges
        for a, b in edges:
            d = pos[b] - pos[a]
            disp[a] += 0.05 * d
            disp[b] -= 0.05 * d
        pos += disp * (0.9 ** (it / iters))
    return pos, idx


def loop_from_branch_set_greedy(branch_set, pos, idx):
    """RETIRED -- kept for the control comparison only. Greedy nearest-neighbor tour: shown to
    produce self-crossing curves (and erratic, non-integer linking numbers) once points are
    scattered anything like a real force-directed layout. Do not use for the actual test."""
    pts_idx = [idx[n] for n in branch_set]
    remaining = pts_idx[:]
    tour = [remaining.pop(0)]
    while remaining:
        last = pos[tour[-1]]
        d = [np.linalg.norm(pos[r] - last) for r in remaining]
        nxt = remaining.pop(int(np.argmin(d)))
        tour.append(nxt)
    tour.append(tour[0])  # close it
    return pos[tour]


def loop_from_branch_set(branch_set, pos, idx):
    """Close a connected vertex set into a curve by projecting onto its best-fit plane and
    sorting by angle around the centroid -- a standard, much more robust construction than a
    greedy tour (star-shaped-from-centroid, avoids self-crossing for compact clusters)."""
    pts_idx = [idx[n] for n in branch_set]
    pts = pos[pts_idx]
    centroid = pts.mean(axis=0)
    centered = pts - centroid
    # best-fit plane: top two singular directions
    _, _, vt = np.linalg.svd(centered)
    u, v = vt[0], vt[1]
    proj = np.stack([centered @ u, centered @ v], axis=1)
    angles = np.arctan2(proj[:, 1], proj[:, 0])
    order = np.argsort(angles)
    tour = [pts_idx[i] for i in order]
    tour.append(tour[0])  # close it
    return pos[tour]


def gauss_linking(A, B):
    dA = np.diff(A, axis=0)
    dB = np.diff(B, axis=0)
    Am = A[:-1] + dA / 2
    Bm = B[:-1] + dB / 2
    r = Am[:, None, :] - Bm[None, :, :]
    rn = np.linalg.norm(r, axis=2) ** 3 + 1e-9
    cross = np.cross(dA[:, None, :], dB[None, :, :])
    num = np.sum(r * cross, axis=2)
    return np.sum(num / rn) / (4 * np.pi)


def min_dist(A, B):
    return np.linalg.norm(A[:, None, :] - B[None, :, :], axis=2).min()


def attempt_separation(loopA, loopB, steps=30):
    """Translate loopB directly away from loopA's centroid, self-avoiding attempt -- probe 1's
    exact method, applied to real embedded curves instead of idealized ones."""
    centroidA = loopA.mean(axis=0)
    centroidB0 = loopB.mean(axis=0)
    direction = (centroidB0 - centroidA)
    direction = direction / (np.linalg.norm(direction) + 1e-9)
    far = np.linalg.norm(loopA.max(axis=0) - loopA.min(axis=0)) * 6
    mds = []
    for s in np.linspace(0, 1, steps):
        shift = direction * far * s
        mds.append(min_dist(loopA, loopB + shift))
    return np.array(mds)


def main():
    print("=" * 78)
    print("OPERATIONAL TEST — does undoing a committed order force a collision?")
    print("=" * 78)
    n_chains, k_branches = 40, 2
    rng = np.random.default_rng(3)
    nodes, adj, chain_nodes = build_graph(n_chains, k_branches, 0.30, rng)  # known K6-density regime
    found, branches = try_k6_witness(adj, chain_nodes, n_chains, 6, rng, tries=4000)
    if not found:
        print("  no K6 witness found this run -- rerun with a different seed/density"); return
    print(f"\n  K6 witness found: 6 branch sets, sizes {[len(b) for b in branches]}")

    pos, idx = force_directed_layout(adj, nodes, iters=250, seed=5)
    loops = [loop_from_branch_set(b, pos, idx) for b in branches]

    print("\n  pairwise linking numbers across the 6 embedded branch-set loops (15 pairs):")
    lks = {}
    for a, b in itertools.combinations(range(6), 2):
        lk = gauss_linking(loops[a], loops[b])
        lks[(a, b)] = lk
        print(f"    loops ({a},{b}):  Lk = {lk:+.3f}")

    best_pair = max(lks, key=lambda k: abs(lks[k]))
    worst_pair = min(lks, key=lambda k: abs(lks[k]))
    print(f"\n  most-linked pair:  {best_pair}  (Lk={lks[best_pair]:+.3f})")
    print(f"  least-linked pair: {worst_pair}  (Lk={lks[worst_pair]:+.3f})  -- the control")

    print("\n  ATTEMPT 1 (the real test): separate the MOST-linked pair, self-avoiding")
    md_linked = attempt_separation(loops[best_pair[0]], loops[best_pair[1]])
    print(f"    min-distance along the attempt: min={md_linked.min():.3f}, "
          f"start={md_linked[0]:.3f}, end={md_linked[-1]:.3f}")

    print("\n  ATTEMPT 2 (control): separate the LEAST-linked pair, same method")
    md_unlinked = attempt_separation(loops[worst_pair[0]], loops[worst_pair[1]])
    print(f"    min-distance along the attempt: min={md_unlinked.min():.3f}, "
          f"start={md_unlinked[0]:.3f}, end={md_unlinked[-1]:.3f}")

    print("\n  READ: if the most-linked pair's min-distance is driven near 0 while the")
    print("  least-linked (control) pair's stays well clear, the test discriminates correctly")
    print("  AND the linking is genuinely obstructing separation -- real evidence toward 'order")
    print("  is held.' If BOTH separate freely, or both get stuck, the test isn't discriminating")
    print("  and this embedding doesn't show the obstruction (honest either way).")
    print("=" * 78)


if __name__ == "__main__":
    main()
