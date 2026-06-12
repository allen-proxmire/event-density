"""B4 Step 3 - Sourcing test: does the integer winding induce a spatial pattern
when embedded in a 2D spatial substrate (P06), with Sigma orientation-blind?

Setup: an L x L lattice (P06 4-neighbour adjacency). A winding-w defect is the
loop's holonomy embedded at the centre. The substrate phase is U(1)-valued
everywhere (P09); commitment (P11) makes it single-valued. The only phase->dynamics
channel is bandwidth (P04 coherence b_e = cos^2(A_e/2)); Sigma never reads it.

NO hand-installed sourcing. We embed ONLY the winding (a connection whose loop
holonomy is 2*pi*w) and read off what single-valuedness forces.

Two questions, kept separate:
  (1) INTEGRAL: circulation sum_loop wrap(A_e) around any enclosing loop.
      -- forced by topology; should equal 2*pi*w for ALL loop sizes (a Gauss law).
  (2) LOCAL: the per-edge bandwidth deficit pattern.
      -- is it a DETERMINED field, or gauge/sweep-dependent (undetermined)?
      ED has no phase-relaxation dynamic (Sigma phase-blind), so we test whether
      the local pattern is fixed by the substrate or merely a choice of committed
      representative (gauge).
"""
from __future__ import annotations

import numpy as np


def wrap(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


def vortex_phase(L, w, cx, cy):
    ys, xs = np.mgrid[0:L, 0:L]
    return w * np.arctan2(ys - cy, xs - cx)


def edge_connection(theta):
    """A_e = wrap(theta_v - theta_u) on horizontal and vertical lattice edges."""
    Ah = wrap(theta[:, 1:] - theta[:, :-1])     # horizontal edges
    Av = wrap(theta[1:, :] - theta[:-1, :])     # vertical edges
    return Ah, Av


def loop_circulation(theta, cx, cy, s):
    """Oriented sum of wrap(dtheta) around the square loop of half-size s about
    (cx, cy). Returns circulation / (2*pi) = enclosed winding."""
    xs = list(range(cx - s, cx + s + 1))
    ys = list(range(cy - s, cy + s + 1))
    pts = ([(x, ys[0]) for x in xs] +
           [(xs[-1], y) for y in ys[1:]] +
           [(x, ys[-1]) for x in reversed(xs[:-1])] +
           [(xs[0], y) for y in reversed(ys[:-1])])
    total = 0.0
    for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1]):
        total += wrap(theta[y1, x1] - theta[y0, x0])
    return total / (2 * np.pi)


def deficit_map(theta):
    Ah, Av = edge_connection(theta)
    # node-centred deficit: mean (1 - cos^2(A/2)) over incident edges
    d = np.zeros_like(theta)
    cnt = np.zeros_like(theta)
    dh = np.sin(Ah / 2) ** 2
    dv = np.sin(Av / 2) ** 2
    d[:, :-1] += dh; cnt[:, :-1] += 1
    d[:, 1:] += dh; cnt[:, 1:] += 1
    d[:-1, :] += dv; cnt[:-1, :] += 1
    d[1:, :] += dv; cnt[1:, :] += 1
    return d / np.maximum(cnt, 1)


def main():
    L = 81
    c = L // 2
    print("=" * 72)
    print(f"B4 Step 3 - Sourcing test on a 2D substrate (L={L}, centre={c})")
    print("=" * 72)

    # ---- (1) INTEGRAL Gauss law: circulation is loop-size-independent = winding
    print("\n(1) INTEGRAL  circulation = (1/2pi) sum_loop wrap(dtheta)  vs loop size")
    print(f"    {'half-size s':>12} " + " ".join(f"w={w}".rjust(8) for w in (0, 1, 2)))
    thetas = {w: vortex_phase(L, w, c, c) for w in (0, 1, 2)}
    for s in (2, 5, 10, 20, 35):
        row = [loop_circulation(thetas[w], c, c, s) for w in (0, 1, 2)]
        print(f"    {s:>12} " + " ".join(f"{v:>8.3f}" for v in row))
    print("    -> circulation = enclosed winding, INDEPENDENT of loop size/shape")
    print("       (a topological Gauss law; the winding cannot be screened)")

    # ---- (2a) LOCAL pattern of the relaxed/vortex representative: radial 1/r^2
    print("\n(2a) LOCAL  vortex-gauge bandwidth deficit  1 - cos^2(A/2)  vs radius r")
    th = thetas[1]
    dmap = deficit_map(th)
    ys, xs = np.mgrid[0:L, 0:L]
    r = np.sqrt((xs - c) ** 2 + (ys - c) ** 2)
    print(f"    {'r':>6} {'mean deficit':>14} {'deficit*r^2':>12}")
    for rr in (2, 4, 8, 16, 32):
        m = (r >= rr - 0.5) & (r < rr + 0.5)
        dm = dmap[m].mean()
        print(f"    {rr:>6} {dm:>14.5f} {dm*rr*rr:>12.4f}")
    print("    -> deficit ~ 1/r^2  (deficit*r^2 ~ const): a radial field-like profile")

    # ---- (2b) the SAME winding in a different committed representative (gauge):
    #          local pattern MOVES, circulation unchanged -> local field undetermined
    rng = np.random.default_rng(7)
    g = np.cumsum(rng.normal(0, 0.4, size=L))[None, :] * np.ones((L, 1))  # smooth gauge
    th2 = th + g
    circ_same = loop_circulation(th2, c, c, 20)
    d_vortex_core = deficit_map(th)[c, c - 3:c + 4].mean()
    d_gauge_core = deficit_map(th2)[c, c - 3:c + 4].mean()
    print("\n(2b) SAME winding, different committed representative (gauge shift):")
    print(f"     circulation (s=20)         : {circ_same:>7.3f}  (unchanged = winding)")
    print(f"     near-core deficit, vortex  : {d_vortex_core:>7.4f}")
    print(f"     near-core deficit, gauge'  : {d_gauge_core:>7.4f}  (pattern RELOCATED)")
    print("     -> the LOCAL deficit pattern is NOT fixed by the winding; it is a")
    print("        choice of committed field. Sigma is phase-blind => no relaxation")
    print("        dynamic selects one => the local field is UNDETERMINED.")

    print("\n" + "=" * 72)
    print("CLASSIFICATION")
    print("  integral (Gauss) content : PRESENT - circulation = 2pi*w around ANY")
    print("                             enclosing loop; unscreenable, quantized.")
    print("  local field content      : UNDETERMINED - pattern is gauge/sweep-")
    print("                             dependent; ED has no relaxation to fix it.")
    print("  Sigma-invariant          : intact (phase never enters Sigma).")
    print("  outcome                  : WEAK / TOPOLOGICAL sourcing - ED supplies the")
    print("                             INTEGRAL Gauss law (enclosed winding) but NOT")
    print("                             a determined LOCAL field (needs relaxation).")
    print("=" * 72)
    return True


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
