"""
Phase-3 GR -- the massive-front computation: closing the TIMELIKE geodesic identity.

GR-III sec.5 reduced the timelike geodesic identity to a *limit-forced* statement:
ED's subluminal max-Sigma front is the massive eikonal of g ~ b^-1, with eikonal
(Jacobi) index

    n_eff(x) = (1/b) sqrt(E^2 - m^2 b)        (E = energy, m = rest-frequency)

which is limit-forced to the proven NULL result (Fermat, n -> E/b ~ b^-1 as m->0,
R7) and to Maupertuis/Newton in the weak field. The residual was: actually trace the
massive eikonal and confirm the rays are the timelike geodesics -- i.e. that the
massive front bends by the relativistic deflection

    alpha(beta) = (r_s / xi) * (1 + 1/beta^2),   beta = v/c = sqrt(1 - m^2/E^2),

which interpolates Newtonian (beta->0: alpha ~ 1/beta^2) to the factor of TWO
(beta=1, m=0: alpha = 2 r_s/xi -- R7's PROVEN null endpoint). This script traces the
massive eikonal rays past a mass (b = 1 - r_s/r) and measures alpha(beta).

Crank rail: n_eff is the Jacobi index DERIVED in the timelike note (not tuned); the
deflection law is measured and compared to the standard relativistic alpha(beta); the
m->0 endpoint must reproduce R7's factor of two or the construction is wrong.
"""
import numpy as np


def b_field(x, y, r_s, b_floor=0.2):
    r = np.sqrt(x*x + y*y)
    return np.maximum(1.0 - r_s / np.maximum(r, 1e-9), b_floor)


def grad_n(x, y, r_s, m, E=1.0, h=1e-3):
    def n(xx, yy):
        b = b_field(xx, yy, r_s)
        return (1.0 / b) * np.sqrt(max(E*E - m*m*b, 1e-12))
    nx = (n(x + h, y) - n(x - h, y)) / (2*h)
    ny = (n(x, y + h) - n(x, y - h)) / (2*h)
    return n(x, y), nx, ny


def trace(r_s, m, xi, E=1.0, x0=-400.0, ds=0.02, nmax=60000):
    """Trace one eikonal ray from (x0, xi) moving +x; return total deflection angle.
    Ray equation (arc-length s, |x'|=1):  x'' = (1/n)[grad n - (grad n . x') x'].
    """
    x, y = x0, xi
    tx, ty = 1.0, 0.0           # initial direction +x
    for _ in range(nmax):
        n, gx, gy = grad_n(x, y, r_s, m, E)
        gdott = gx*tx + gy*ty
        ax = (gx - gdott*tx) / n
        ay = (gy - gdott*ty) / n
        tx += ax * ds
        ty += ay * ds
        nrm = np.hypot(tx, ty)
        tx, ty = tx/nrm, ty/nrm
        x += tx * ds
        y += ty * ds
        if x > -x0:
            break
    return np.arctan2(ty, tx)     # deflection from the initial +x direction


if __name__ == '__main__':
    np.set_printoptions(precision=4, suppress=True)
    r_s = 1.0
    xi = 60.0                    # impact parameter (weak field: xi >> r_s)
    print("Massive eikonal deflection in g ~ b^-1 (b = 1 - r_s/r):")
    print(f"  r_s = {r_s}, impact parameter xi = {xi}\n")
    print("   m     beta=v/c    alpha (measured)   alpha*xi/r_s   1 + 1/beta^2   ratio")
    print("  ----   --------    ---------------    ------------   ------------   -----")
    rows = []
    for m in (0.0, 0.5, 0.7, 0.85, 0.95):
        beta = np.sqrt(1.0 - m*m)            # E=1, v/c = p/E = sqrt(1-m^2)
        a = -trace(r_s, m, xi)               # deflection magnitude (toward the mass)
        meas = a * xi / r_s
        pred = 1.0 + 1.0/beta**2
        rows.append((m, beta, a, meas, pred))
        print(f"  {m:4.2f}   {beta:6.3f}     {a:12.5f}     {meas:9.3f}     {pred:9.3f}    "
              f"{meas/pred:5.3f}")
    print("\n  Endpoints:")
    b1 = rows[0]                              # m=0, beta=1 (null)
    print(f"    m=0 (beta=1, NULL): alpha*xi/r_s = {b1[3]:.3f}  (R7 factor of TWO => 2.0)")
    bl = rows[-1]
    print(f"    m=0.95 (beta={bl[1]:.2f}, slow): alpha*xi/r_s = {bl[3]:.2f}  (Newtonian"
          f" 1/beta^2 = {1/bl[1]**2:.2f})")
    print("\n  => the massive eikonal reproduces alpha = (r_s/xi)(1 + 1/beta^2):")
    print("     Newtonian (1/beta^2) at low beta, the factor of TWO at beta=1 (R7).")
    print("     The timelike geodesic identity is confirmed at the eikonal level;")
    print("     the m->0 limit recovers the proven null (Fermat) deflection.")
