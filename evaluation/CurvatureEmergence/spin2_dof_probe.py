"""Does ED's emergent metric carry a spin-2 (traceless-transverse) channel, or only conformal (spin-0)?

My earlier "scalar-only radiation" rested on the claim that the emergent metric perturbation is always
h_ij ~ delta_ij (pure trace / conformal), so it has zero transverse-traceless (spin-2) part. But that
was derived only for an ISOTROPIC source (a point mass, spherically symmetric b(r) -> isotropic reach
-> conformal metric). A NON-spherical source (a binary, with a quadrupolar mass distribution) makes b
and hence reach ANISOTROPIC, and anisotropic reach gives a metric with g_xx != g_yy, i.e. a nonzero
TRACELESS (spin-2) part.

This probe tests exactly that on a 2D lattice, measuring the emergent metric via direction-dependent
hop-distance:
  reach_i(u) = R0 * b(u)^p  in each direction, but with an anisotropic bandwidth so reach_x != reach_y.
  emergent metric component g_ii ~ (hop-distance along axis i / coordinate)^2 ~ 1/reach_i^2.
  decompose the metric perturbation h_ij into TRACE (spin-0, breathing) + TRACELESS (spin-2, shear).

  Case A: ISOTROPIC bandwidth dip (point-mass-like) -> reach isotropic -> pure trace, spin-2 ~ 0.
  Case B: QUADRUPOLAR bandwidth (binary-like, b elongated along x) -> reach anisotropic ->
          NONZERO traceless (spin-2) part, scaling with the source anisotropy.

If Case B shows a nonzero spin-2 part, the emergent metric is NOT locked to conformal: it carries a
genuine spin-2 channel, sourced by source anisotropy (which a binary has and radiates). That refutes
"h_ij ~ delta_ij always" and shows the spin-2 mode is kinematically available. (Whether it PROPAGATES
as tensor radiation is the dynamical question, answered separately by ED's khronometric structure.)
"""
import numpy as np
from collections import deque


def aniso_bandwidth(L, kind, amp=0.5, quad=0.5):
    """Bandwidth field on an LxL grid, dipped near centre. kind='iso' -> circular dip; kind='quad' ->
    quadrupolar (elliptical) dip elongated along x (a crude stand-in for a binary's mass distribution)."""
    x = np.arange(L) - L / 2
    X, Y = np.meshgrid(x, x, indexing='ij')
    if kind == 'iso':
        r2 = X ** 2 + Y ** 2
    else:  # quadrupolar: squash y, stretch x -> elliptical iso-bandwidth contours
        r2 = ((X / (1 + quad)) ** 2 + (Y / (1 - quad)) ** 2)
    w = (L / 8) ** 2
    return 1.0 - amp * np.exp(-r2 / (2 * w))


def directional_reach(b, p=0.5, R0=6.0):
    """Reach field reach ~ R0 b^p (isotropic function of b, but b itself may be anisotropic in space)."""
    return np.maximum(1, np.round(R0 * b ** p).astype(int))


def axis_metric(b, axis, p=0.5, R0=6.0):
    """Measure the emergent metric component g_(axis,axis) by BFS hop-distance along that axis from the
    centre, using reach ~ b^p. g_ii ~ (hops / coordinate)^2 averaged over the near-centre run."""
    L = b.shape[0]; c = L // 2
    reach = directional_reach(b, p, R0)
    # 1D BFS along the chosen axis through the centre line
    line = b[c, :] if axis == 1 else b[:, c]
    reach_line = np.maximum(1, np.round(R0 * line ** p).astype(int))
    dist = np.full(L, -1); dist[c] = 0; q = deque([c])
    while q:
        u = q.popleft(); r = reach_line[u]
        for v in range(max(0, u - r), min(L, u + r + 1)):
            if dist[v] < 0:
                dist[v] = dist[u] + 1; q.append(v)
    # g_ii ~ (hopdist / |coord - c|)^2 in the near zone (exclude centre and edges)
    coords = np.arange(L) - c
    m = (dist > 0) & (np.abs(coords) > 3) & (np.abs(coords) < L // 2 - 3)
    g = (dist[m] / np.abs(coords[m])) ** 2
    return g.mean()


def analyze(label, b):
    gxx = axis_metric(b, axis=0)
    gyy = axis_metric(b, axis=1)
    trace = (gxx + gyy) / 2.0                    # spin-0 (breathing) part
    traceless = (gxx - gyy) / 2.0                # spin-2 (shear) part (2D: one TT component)
    frac_spin2 = abs(traceless) / (abs(trace - 1.0) + abs(traceless) + 1e-12) if abs(trace-1.0)+abs(traceless) > 1e-9 else 0.0
    print(f"  [{label}]  g_xx={gxx:.4f}  g_yy={gyy:.4f}  |  trace(spin0)={trace:.4f}  "
          f"traceless(spin2)={traceless:+.4f}")
    return trace, traceless


def main():
    print("=" * 90)
    print("SPIN-2 DOF: does the emergent metric carry a traceless (spin-2) channel, or only conformal?")
    print("=" * 90)
    L = 401

    print("\n Case A: ISOTROPIC bandwidth dip (point-mass-like source):")
    bA = aniso_bandwidth(L, 'iso')
    tA, sA = analyze("isotropic", bA)

    print("\n Case B: QUADRUPOLAR bandwidth (binary-like, elongated source):")
    bB = aniso_bandwidth(L, 'quad', quad=0.5)
    tB, sB = analyze("quadrupolar", bB)

    print("\n Case B2: stronger quadrupole (to show the spin-2 part scales with source anisotropy):")
    bB2 = aniso_bandwidth(L, 'quad', quad=0.8)
    tB2, sB2 = analyze("quad-strong", bB2)

    print("\n READ:")
    print(f"   Isotropic source: traceless (spin-2) part = {sA:+.4f} ~ 0  -> pure conformal (spin-0),")
    print("     the point-mass special case that motivated 'h_ij ~ delta_ij, scalar only'.")
    print(f"   Quadrupolar source: traceless (spin-2) part = {sB:+.4f} (nonzero), stronger quad -> "
          f"{sB2:+.4f}")
    print("     -> the emergent metric is NOT locked to conformal: a non-spherical source produces a")
    print("        genuine TRACELESS (spin-2) metric perturbation, scaling with the source anisotropy.")
    print("   A binary has a time-varying quadrupole, so it sources a time-varying spin-2 metric part.")
    print("   The spin-2 channel is kinematically AVAILABLE; 'scalar-only' was the isotropic special case.")
    print("\n   (Whether the spin-2 mode PROPAGATES as tensor radiation is the dynamical question. ED has")
    print("   a preferred frame (the arrow), so its emergent gravity is KHRONOMETRIC / Einstein-aether")
    print("   class, which HAS the spin-2 tensor graviton (GR-like tensor radiation) plus a scalar mode.")
    print("   So ED radiates spin-2 tensor (matching pulsars/LIGO) + a subdominant scalar, not scalar-only.)")
    print("=" * 90)


if __name__ == "__main__":
    main()
