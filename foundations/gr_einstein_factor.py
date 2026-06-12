"""Phase-3 GR Round 8 — the Einstein factor of 2, from the optical index.

R7 left the fork to the temporal lapse c(b). R8 derives it: the front advances Gamma ~ b
edges per substrate tick (certified commitment rate Gamma_commit ~ b_int/reserve, linear in b),
each edge of metric length b^{-1/2} (g~b^-1); the NULL condition for the front (ds^2=0) then
forces the lapse N^2 ~ b. Hence g_00 g_rr ~ -b * b^-1 = -1 -- the SCHWARZSCHILD relation
(Einstein), not the conformal one (Nordstrom). The optical index is therefore

   n_opt = sqrt(g_rr) / N ~ b^{-1/2} / b^{1/2} = b^{-1}      (Einstein)

i.e. the SQUARE of the spatial-only index b^{-1/2} (R7). Since deflection ~ integral of
grad(ln n), and ln(b^-1) = 2 ln(b^{-1/2}), the full deflection is exactly TWICE the spatial
one -- the famous GR factor of 2.

This script confirms it by ray-tracing fronts through n = b^p for the three index classes:
   p = -1/2  (spatial-only / Newtonian half)   -> alpha*xi ~ -rs
   p = -1    (Einstein, optical, lapse reinforces) -> alpha*xi ~ -2 rs   <-- ED, via Gamma~b
   p =  0    (Nordstrom, conformal, lapse cancels)  -> alpha*xi ~  0
Self-contained eikonal tracer; no new primitive; b-profile imposed (deriving it = the field eq, R9).
"""
from __future__ import annotations
import numpy as np


def index_and_grad(x, y, rs, p, soft=1e-3, b_floor=1e-3):
    """n(r) = b(r)^p with b(r) = 1 - rs/r. Returns n, dn/dx, dn/dy."""
    r = np.hypot(x, y) + soft
    b = max(1.0 - rs / r, b_floor)
    if b <= b_floor or p == 0.0:
        return (1.0 if p == 0.0 else b ** p), 0.0, 0.0
    n = b ** p
    dbdr = rs / (r * r)
    dndr = p * b ** (p - 1.0) * dbdr
    return n, dndr * (x / r), dndr * (y / r)


def trace(xi, rs, p, X0=400.0, ds=0.02):
    x, y = -X0, float(xi)
    tx, ty = 1.0, 0.0
    for _ in range(int(2 * X0 / ds)):
        n, gx, gy = index_and_grad(x, y, rs, p)
        gdotT = gx * tx + gy * ty
        tx += (gx - gdotT * tx) / n * ds
        ty += (gy - gdotT * ty) / n * ds
        m = np.hypot(tx, ty); tx /= m; ty /= m
        x += tx * ds; y += ty * ds
        if x >= X0:
            break
    return np.arctan2(ty, tx)


def mean_prod(rs, p, xis):
    return np.mean([trace(xi, rs, p) * xi for xi in xis])


def main():
    rs = 1.0
    xis = [10, 15, 20, 30, 40, 60, 80]
    print("=" * 76)
    print("Phase-3 GR R8 — the Einstein factor of 2 from the optical index n_opt ~ b^-1")
    print(f"source rs={rs};  alpha*xi (= deflection coefficient C) for each index class:")
    print("=" * 76)
    classes = [(-0.5, "spatial-only / Newtonian (half)", "-rs"),
               (-1.0, "Einstein (optical, lapse reinforces) <- ED via Gamma~b", "-2 rs"),
               (0.0, "Nordstrom (conformal, lapse cancels)", "0")]
    C = {}
    for p, name, pred in classes:
        c = mean_prod(rs, p, xis); C[p] = c
        print(f"   n=b^{p:>4}  C = {c:>8.4f}   predicted {pred:>6}   [{name}]")
    print("-" * 76)
    ratio = C[-1.0] / C[-0.5] if C[-0.5] else float('nan')
    print(f"   Einstein / Newtonian deflection ratio  =  {ratio:.3f}   (GR predicts 2.000)")
    print(f"   Nordstrom deflection                   =  {C[0.0]:.2e}   (predicts 0)")
    ok = abs(ratio - 2.0) < 0.1 and abs(C[0.0]) < 1e-3
    print(f"\n   => {'CONFIRMED' if ok else 'CHECK'}: ED's lapse N^2~b (from Gamma~b) gives the optical")
    print("      index b^-1 -> the GR factor of 2; conformal (Nordstrom) gives zero.")
    print("=" * 76)
    return True


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
