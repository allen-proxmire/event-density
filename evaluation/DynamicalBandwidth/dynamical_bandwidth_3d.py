"""
Phase-3 GR -- the dynamical-bandwidth rule F in 3D.

Two jobs the 2D minimal model could not finish:
  (1) the clean 3D Newtonian profile  b = 1 - r_s/r  (2D gave only the log Green's fn),
      and the Schwarzschild mass-scaling r_s ~ M;
  (2) re-test the Hawking surface-gravity scaling kappa ~ 1/r_h -- the 2D minimal model
      gave kappa ~ const, with the cause located as the FIXED sharing length D setting a
      r_h-independent transition width. Honest expectation going in: if that diagnosis
      is right, 3D will STILL give kappa ~ const (elliptic relaxation, fixed D), which
      would isolate the Hawking-scaling failure to elliptic-vs-hyperbolic, NOT 2D-vs-3D.
      Let the run decide.

Same forced rule as the 2D build:  b-dot = D grad^2 b - kappa rho,  b >= 0 (P04),
b -> 1 at the frame.  Crank rail: not tuned to Schwarzschild; the profile and the
horizon scaling are measured.
"""
import numpy as np

# 3D diffusion CFL stability: D <= 1/(2*ndim) = 1/6 ~ 0.167 for the explicit
# 6-neighbour stencil. (2D allowed 0.25; 3D does not.)
D = 0.14


def lap3(f):
    return (np.roll(f, 1, 0) + np.roll(f, -1, 0)
            + np.roll(f, 1, 1) + np.roll(f, -1, 1)
            + np.roll(f, 1, 2) + np.roll(f, -1, 2) - 6.0 * f)


def run3d(S=80, kappa=2e-3, rho_amp=1.0, rho_sigma=4.0, steps=4000):
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
    return dict(b=b, rho=rho, r=r, S=S)


def radial(field, r, nbin=50, rmax=None):
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

    # ---- (1) the 3D Newtonian profile: deficit ~ 1/r ? ----
    print("=== 3D NEWTONIAN PROFILE: deficit ~ 1/r (Schwarzschild) ? ===")
    w = run3d(S=72, kappa=1.0e-3, rho_amp=1.0, rho_sigma=4.0, steps=9000)
    rr, bb = radial(w['b'], w['r'], rmax=0.45 * 72)
    deficit = 1.0 - bb
    o = (rr > 8) & (rr < 0.38 * 72)         # vacuum region outside the source
    # fit deficit = r_s / r  (log-log slope should be -1)
    slope = np.polyfit(np.log(rr[o]), np.log(deficit[o]), 1)[0]
    rs_fit = np.median(deficit[o] * rr[o])  # r_s = deficit * r if deficit = r_s/r
    print(f"  deficit(r) log-log slope = {slope:+.3f}   (Schwarzschild 1/r => -1; 2D was log)")
    print(f"  r_s = deficit*r (flat if 1/r): median {rs_fit:.3f}, spread "
          f"{np.std(deficit[o]*rr[o]):.3f}")

    # ---- mass scaling r_s ~ M ----
    print("\n=== MASS SCALING  r_s ~ M ===")
    for amp in (0.5, 1.0, 2.0):
        m = run3d(S=64, kappa=1.0e-3, rho_amp=amp, rho_sigma=4.0, steps=7000)
        rr, bb = radial(m['b'], m['r'], rmax=0.45 * 64)
        o = (rr > 8) & (rr < 0.38 * 64)
        rs = np.median((1 - bb)[o] * rr[o])
        print(f"  rho_amp {amp:.1f}  integrated-source {m['rho'].sum():9.1f}  r_s {rs:.3f}")

    # ---- (2) horizon surface gravity kappa vs r_h (Hawking T ~ 1/r_h ?) ----
    print("\n=== HORIZON SURFACE GRAVITY  kappa vs r_h  (Hawking T ~ 1/r_h ?) ===")
    rows = []
    for amp in (4.0, 7.0, 11.0, 16.0):
        s = run3d(S=64, kappa=8e-3, rho_amp=amp, rho_sigma=5.0, steps=7000)
        b, r = s['b'], s['r']
        hor = b <= 1e-9
        if hor.sum() < 8:
            continue
        r_h = r[hor].max()
        N = np.sqrt(b)
        ring = (r > r_h) & (r < r_h + 3)
        gN = np.zeros_like(N)
        for ax in range(3):
            gN += ((np.roll(N, -1, ax) - np.roll(N, 1, ax)) / 2.0)**2
        gN = np.sqrt(gN)
        kap = gN[ring].mean()
        rows.append((amp, r_h, int(hor.sum()), kap))
    print("  source   r_h    horizon-vol   kappa    kappa*r_h")
    for amp, r_h, V, kap in rows:
        print(f"  {amp:5.1f}  {r_h:5.1f}    {V:8d}    {kap:6.4f}   {kap*r_h:6.3f}")
    if len(rows) >= 3:
        rs = np.array([x[1] for x in rows]); ks = np.array([x[3] for x in rows])
        pk = np.polyfit(np.log(rs), np.log(ks), 1)[0]
        print(f"\n  kappa ~ r_h^{pk:.2f}   (Hawking 1/r_h => -1; flat => 0)")
        print("  => " + ("kappa ~ 1/r_h: Hawking scaling RECOVERED in 3D"
                          if pk < -0.6 else
                          "kappa still ~flat: the failure is ELLIPTIC (fixed D), not 2D"
                          " -- needs the hyperbolic strong-field rule"))
    print("\ndone.")
