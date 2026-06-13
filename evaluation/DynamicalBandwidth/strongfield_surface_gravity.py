"""
Phase-3 GR -- strong-field horizon surface gravity, CORRECTED measurement.

The 2D/3D builds found a FLAT surface gravity (kappa ~ const) and located the
Hawking T ~ 1/r_h failure to "the elliptic/minimal rule needs a hyperbolic
strong-field replacement." Before building that, re-examine the measurement --
two likely errors:

  (1) WRONG FORMULA. The builds measured d(sqrt b)/dr. But GR-I established the
      Schwarzschild relation g_00 g_rr = -1 (N^2 = b, g_rr = b^-1), so the metric
      is  ds^2 = -b dt^2 + b^-1 dr^2 + ...  -- a metric of the form -f dt^2 +
      f^-1 dr^2 with f = b. For such a metric the surface gravity is
          kappa = (1/2) f'(r_h) = (1/2) d b/dr |_horizon,
      NOT d(sqrt b)/dr. (For f = 1 - r_s/r this gives kappa = 1/(2 r_s) ~ 1/r_h.)

  (2) NON-COMPACT SOURCE. The minimal rule is LINEAR (b-dot = D grad^2 b - kappa rho),
      so its 3D vacuum steady state is harmonic: grad^2 b = 0 -> b = 1 - r_s/r.
      The horizon (b -> 0, clipped at the P04 floor) then sits at r = r_s. But that
      only holds if the horizon is OUTSIDE the source; with an extended source the
      b=0 region overlaps it and the near-horizon profile is the (D-set) relaxation
      profile, not 1 - r_s/r. Use a COMPACT source so the horizon forms in vacuum.

This script re-runs 3D with a compact source and the correct kappa = (1/2) d b/dr,
sweeping source strength, and tests kappa ~ 1/r_h. If it holds, the Hawking-scaling
"failure" was a measurement artifact and the minimal rule already carries it.
Crank rail: the profile/scaling are measured; nothing tuned to give 1/r_h.
"""
import numpy as np

D = 0.14


def lap3(f):
    return (np.roll(f, 1, 0) + np.roll(f, -1, 0)
            + np.roll(f, 1, 1) + np.roll(f, -1, 1)
            + np.roll(f, 1, 2) + np.roll(f, -1, 2) - 6.0 * f)


def run3d(S, kappa, rho_amp, rho_sigma, steps):
    a = np.arange(S) - (S - 1) / 2.0
    X, Y, Z = np.meshgrid(a, a, a, indexing='ij')
    r = np.sqrt(X**2 + Y**2 + Z**2)
    rho = rho_amp * np.exp(-(r**2) / (2 * rho_sigma**2))
    b = np.ones((S, S, S))
    for _ in range(steps):
        b = b + D * lap3(b) - kappa * rho
        b = np.clip(b, 0.0, None)
        b[0, :, :] = b[-1, :, :] = 1.0
        b[:, 0, :] = b[:, -1, :] = 1.0
        b[:, :, 0] = b[:, :, -1] = 1.0
    return b, r, rho


def radial(field, r, nbin=80, rmax=None):
    rmax = rmax or r.max() * 0.5
    edges = np.linspace(0, rmax, nbin + 1)
    idx = np.digitize(r.ravel(), edges) - 1
    rr, vv, fv = [], [], field.ravel()
    for k in range(nbin):
        m = idx == k
        if m.sum() > 6:
            rr.append(0.5 * (edges[k] + edges[k + 1]))
            vv.append(fv[m].mean())
    return np.array(rr), np.array(vv)


if __name__ == '__main__':
    np.set_printoptions(precision=4, suppress=True)
    print("Corrected horizon surface gravity: kappa = (1/2) db/dr at the horizon,")
    print("compact source (horizon forms in vacuum where b = 1 - r_s/r).\n")
    print("  amp    r_h   r_s(=def*r)   kappa=(1/2)db/dr   kappa*r_h   1/(2 r_h)")
    print("  ---    ---   ----------   ----------------   ---------   ---------")
    rows = []
    for amp in (6.0, 9.0, 13.0, 18.0, 25.0):
        b, r, rho = run3d(S=84, kappa=8e-3, rho_amp=amp, rho_sigma=2.2, steps=7000)
        rr, bb = radial(b, r, rmax=0.45 * 84)
        # horizon radius: outermost bin with b ~ 0
        zero = np.where(bb <= 1e-6)[0]
        if len(zero) == 0:
            continue
        ih = zero.max()
        r_h = rr[ih]
        # r_s from the vacuum tail (b = 1 - r_s/r) well outside the horizon
        tail = (rr > r_h + 3) & (rr < 0.4 * 84)
        r_s = np.median((1 - bb)[tail] * rr[tail]) if tail.sum() > 3 else np.nan
        # surface gravity: slope of b just outside the horizon, kappa = (1/2) db/dr
        out = (rr > r_h) & (rr < r_h + 6)
        if out.sum() < 3:
            continue
        slope = np.polyfit(rr[out], bb[out], 1)[0]
        kap = 0.5 * slope
        rows.append((amp, r_h, r_s, kap))
        print(f"  {amp:4.1f}  {r_h:4.1f}   {r_s:9.3f}    {kap:14.4f}    {kap*r_h:7.3f}    "
              f"{0.5/r_h:7.4f}")
    if len(rows) >= 3:
        rs = np.array([x[1] for x in rows]); ks = np.array([x[3] for x in rows])
        pk = np.polyfit(np.log(rs), np.log(ks), 1)[0]
        print(f"\n  kappa ~ r_h^{pk:.2f}   (Hawking 1/r_h => -1; flat => 0)")
        if pk < -0.6:
            print("  => HAWKING SCALING RECOVERED: kappa ~ 1/r_h. The earlier 'flat' result")
            print("     was a measurement artifact (wrong d sqrt(b)/dr proxy + non-compact")
            print("     source). The minimal rule already carries the Hawking scaling; NO")
            print("     hyperbolic strong-field rule is needed for it.")
        else:
            print("  => still flat: the surface-gravity scaling genuinely needs more than the")
            print("     minimal rule -- proceed to the hyperbolic strong-field build.")
    print("\ndone.")
