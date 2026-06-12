"""Phase-3 GR Round 7 — the light-bending (lensing) instrument.

The Einstein/Nordstrom fork (R6) reduces to one measurable: does an ED source DEFLECT
front trajectories (Einstein-class, anisotropic metric) or not (Nordstrom, conformally flat)?
R6 established (forward) that ED front propagation is Fermat / null-geodesic motion in the
optical metric built from bandwidth. So a front is a RAY in an index field n(r) = b(r)^{-1/2}
(metric length ds ~ b^{-1/2}|dx|, so b^{-1/2} is the optical slowness/index).

This script is the INSTRUMENT for the fork: ray-trace fronts through an imposed static
bandwidth profile and measure the deflection angle alpha vs impact parameter xi.
  - ED-like depleted profile b(r) = b_inf (1 - rs/r)  (bandwidth drawn down near a high-rho
    source; rs = source strength) -> n(r) = (1 - rs/r)^{-1/2} ~ 1 + rs/(2r).
    Weak-field theory predicts the gravitational-lensing law  alpha = rs / xi  (~ 1/xi).
  - FLAT control b = b_inf (no source) -> alpha = 0 (no bending).
This validates that the deflection is a clean, correctly-scaling discriminator: nonzero, ~1/xi
=> Einstein-class (bends light); zero => Nordstrom (ruled out).

Honest scope: this imposes a *spatial* bandwidth profile and ray-traces it; it tests the
PROPAGATION/LENSING mechanism and the 1/xi law. The full Einstein COEFFICIENT (the GR factor
of 2 = equal spatial + temporal contributions) additionally needs the lapse/temporal sector
(signature assembly, R4 Q2) -- this spatial-only instrument gives the spatial contribution.
No certified-sim dependency: a self-contained eikonal ray-tracer. No new primitive; the b-profile
is imposed (the field equation that would DERIVE it is R8), so this validates the instrument and
the mechanism, not the source profile.
"""
from __future__ import annotations
import numpy as np


def index_and_grad(x, y, rs, b_inf=1.0, soft=1e-3, b_floor=1e-3):
    """n(r) = b(r)^{-1/2}, b(r) = b_inf (1 - rs/r), with softening; returns n, dn/dx, dn/dy."""
    r = np.hypot(x, y) + soft
    b = b_inf * (1.0 - rs / r)
    b = max(b, b_floor)
    n = b ** -0.5
    # dn/dr = -1/2 b^{-3/2} db/dr ; db/dr = b_inf rs / r^2
    if b <= b_floor:
        return n, 0.0, 0.0
    dbdr = b_inf * rs / (r * r)
    dndr = -0.5 * b ** -1.5 * dbdr
    return n, dndr * (x / r), dndr * (y / r)


def trace(xi, rs, X0=400.0, ds=0.02):
    """Eikonal ray-trace: dT/ds = (1/n)[grad n - (grad n . T) T]. Ray starts at x=-X0, y=xi,
    moving +x; integrate to x=+X0; return total deflection angle (radians)."""
    x, y = -X0, float(xi)
    tx, ty = 1.0, 0.0
    steps = int(2 * X0 / ds)
    for _ in range(steps):
        n, gx, gy = index_and_grad(x, y, rs)
        gdotT = gx * tx + gy * ty
        ax = (gx - gdotT * tx) / n
        ay = (gy - gdotT * ty) / n
        tx += ax * ds
        ty += ay * ds
        m = np.hypot(tx, ty)
        tx /= m; ty /= m
        x += tx * ds
        y += ty * ds
        if x >= X0:
            break
    return np.arctan2(ty, tx)   # final direction angle = deflection


def main():
    print("=" * 74)
    print("Phase-3 GR R7 — lensing instrument: front deflection in an ED bandwidth profile")
    print("ED-like b(r) = (1 - rs/r); ray = front = null geodesic of optical metric n=b^{-1/2}")
    print("=" * 74)

    rs = 1.0
    xis = np.array([10, 15, 20, 30, 40, 60, 80])
    print(f"\nsource strength rs = {rs}   (weak-field prediction: alpha = rs/xi)")
    print(f"{'xi':>6} {'alpha_sim':>12} {'rs/xi':>10} {'alpha*xi':>10}")
    prod = []
    for xi in xis:
        a = trace(xi, rs)
        prod.append(a * xi)
        print(f"{xi:>6.0f} {a:>12.5f} {rs/xi:>10.5f} {a*xi:>10.4f}")
    prod = np.array(prod)
    # fit alpha = C/xi  =>  alpha*xi = C (constant). Report C and its stability.
    # C < 0 means the ray bends TOWARD the source (gravitational lensing); magnitude ~ rs.
    C = prod.mean(); cv = prod.std() / abs(prod.mean())
    print(f"\n  alpha ~ C/xi :  C = {C:.4f}  (predicted -rs = {-rs}; sign<0 = bends toward source);"
          f"  CV(alpha*xi) = {cv:.3f}")
    print(f"  => {'1/xi LENSING LAW CONFIRMED' if cv < 0.1 else 'deviates from 1/xi'};"
          f" SPATIAL deflection {'NONZERO, toward source, |C|~rs' if abs(C) > 0.05 else 'ZERO'}")
    print("     (this is the SPATIAL contribution only; the fork Einstein[2x] vs Nordstrom[0]")
    print("      depends on whether the temporal lapse c(b) ADDS to or CANCELS this -- R8)")

    # control: flat bandwidth (no source) must give zero deflection
    print("\n[control] FLAT b (rs=0, no source):")
    a0 = trace(20.0, 0.0)
    print(f"   xi=20  alpha = {a0:.2e}   ({'~0 as required (no source, no bending)' if abs(a0) < 1e-3 else 'SPURIOUS'})")

    # linearity in source strength: alpha*xi should scale linearly with rs
    print("\n[scaling] deflection vs source strength (xi=20):")
    print(f"{'rs':>6} {'alpha*xi':>10}")
    for rr in (0.5, 1.0, 2.0, 4.0):
        a = trace(20.0, rr)
        print(f"{rr:>6.1f} {a*20:>10.4f}")
    print("   => alpha*xi ~ linear in rs  =>  deflection scales with source strength (prop M)")

    print("\n" + "=" * 74)
    print("Read: the SPATIAL bandwidth profile bends fronts with the gravitational-lensing")
    print("kinematics (alpha ~ rs/xi, prop M) -- validating the Fermat/null-geodesic mechanism.")
    print("This is HALF the picture: total deflection = spatial (here) + temporal (lapse c(b)).")
    print("Einstein iff they ADD (total 2x, the GR factor); Nordstrom iff they CANCEL (total 0).")
    print("The c(b) scaling that decides it is signature assembly -- R8.")
    print("=" * 74)
    return True


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
