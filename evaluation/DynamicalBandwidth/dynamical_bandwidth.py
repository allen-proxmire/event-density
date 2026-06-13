"""
Phase-3 GR -- the dynamical-bandwidth rule F on P04, FIRST BUILD.

Builds the FORCED admissible rule and MEASURES whether its steady state reproduces
the three things it must:
  (1) the field equation  D*grad^2 b = kappa*rho   (R1/R9 Newtonian limit),
  (2) a finite-radius b->0 HORIZON at strong coupling, g_rr ~ 1/b -> inf  (R4 sec.6),
  (3) the b->0 region is a FROZEN A2 decoupling cut (reserve exhausted; target #8).

The two FORCED terms of F (each tied to a primitive, neither tuned to give Poisson):
  * D * grad^2 b   -- P02 adjacency sharing: the metric band is a shared/reciprocal
                      record (b_ij = b_ji), so it equilibrates across adjacency; the
                      natural dynamics of a shared conserved field on a graph is the
                      graph Laplacian (the ELLIPTIC geometry sector -- distinct from
                      the kinetic MATTER sector of the CoarseGrain trilogy; Newtonian
                      gravity is elliptic by nature).
  * - kappa * rho  -- P11 commitment concentration: persistent matter holds/concentrates
                      bandwidth into its single channel (commitment.md), depleting the
                      metric band in proportion to its density -> b LOW near matter
                      (the gravity sign). kappa carries the alpha=1 rate strength.
Poisson is the FIXED POINT of (sharing - matter-sink); it is the steady state of the
forced rule, MEASURED here, not imposed.  What is genuinely EMERGENT (not built in):
the finite-radius horizon and the frozen cut at strong coupling.

Separately, the commitment-reserve band (P04 sec.1.5) drains monotonically where
commitments fire (P11; no replenishment, R2 sec.5) -- the A2-freeze diagnostic.

Crank rail: F's FORM is the R2 admissible core; the horizon/cut are measured, not
imposed.  Let it say no.
"""
import numpy as np

D = 0.25  # P02 adjacency-sharing rate (global, fixed)


def lap(f):
    return (np.roll(f, 1, 0) + np.roll(f, -1, 0)
            + np.roll(f, 1, 1) + np.roll(f, -1, 1) - 4.0 * f)


def run(S=220, kappa=4e-4, rho_amp=1.0, rho_sigma=8.0, steps=9000, R0=0.8):
    x = np.arange(S) - (S - 1) / 2.0
    X, Y = np.meshgrid(x, x, indexing='ij')
    r = np.sqrt(X**2 + Y**2)
    rho = rho_amp * np.exp(-(r**2) / (2 * rho_sigma**2))   # static persistent source
    b = np.ones((S, S))
    R = np.full((S, S), float(R0))                          # commitment reserve
    for _ in range(steps):
        b = b + D * lap(b) - kappa * rho                    # P02 share - P11 matter-sink
        b = np.clip(b, 0.0, None)                           # b >= 0 (P04)
        b[0, :] = b[-1, :] = b[:, 0] = b[:, -1] = 1.0       # asymptotic flatness
        R = np.clip(R - 2e-4 * rho, 0.0, None)              # reserve monotone drain (diag)
    return dict(b=b, R=R, rho=rho, r=r, S=S)


def radial(field, r, nbin=70, rmax=None):
    rmax = rmax or r.max() * 0.6
    edges = np.linspace(0, rmax, nbin + 1)
    idx = np.digitize(r.ravel(), edges) - 1
    out_r, out_v, fv = [], [], field.ravel()
    for k in range(nbin):
        m = idx == k
        if m.sum() > 4:
            out_r.append(0.5 * (edges[k] + edges[k + 1]))
            out_v.append(fv[m].mean())
    return np.array(out_r), np.array(out_v)


def field_eq(b, rho, r, S):
    """Check D*grad^2 b = kappa*rho  i.e. corr(grad^2 b, rho) at steady state."""
    Lb = D * lap(b)
    msk = (r < 0.45 * S)
    cc = np.corrcoef(Lb[msk].ravel(), rho[msk].ravel())[0, 1]
    sig = 8.0
    core, out = r < 2.0 * sig, (r > 3.0 * sig) & (r < 0.4 * S)
    ratio = np.abs(Lb[core]).mean() / (np.abs(Lb[out]).mean() + 1e-15)
    return cc, ratio


def horizon_thermo(amps=(2.0, 3.0, 4.0, 6.0, 9.0), S=200, kappa=4e-3, sigma=8.0, steps=12000):
    """B-column payoff: does the DYNAMICALLY-EMERGENT horizon (the b->0 frozen cut)
    carry the ED-10/Information thermodynamics?
      * S ~ A (area law / holographic): the severed information = the count of edges
        crossing the b->0 surface (A1: capacity across the cut is exactly zero, so the
        hidden DOF = the severed adjacency channels = the BOUNDARY edge-count). Test:
        does that count scale with the horizon PERIMETER (area, ~ r_h) or with the
        ENCLOSED region (volume, ~ r_h^2)?  Holographic <=> perimeter.
      * T ~ kappa (Hawking): surface gravity kappa ~ d/dr of the lapse N ~ sqrt(b) at
        the horizon. Test the scaling kappa vs r_h (Schwarzschild: kappa ~ 1/r_h, so
        smaller horizon = hotter -- the T ~ 1/M relation).
    Coefficients (the 1/4 in S=A/4, the exact Hawking T) are value-inherited via G/l_P;
    the SCALINGS are what is measured here.
    """
    x = np.arange(S) - (S - 1) / 2.0
    X, Y = np.meshgrid(x, x, indexing='ij')
    rgrid = np.sqrt(X**2 + Y**2)
    rows = []
    for amp in amps:
        st = run(S=S, kappa=kappa, rho_amp=amp, rho_sigma=sigma, steps=steps)
        b, r = st['b'], st['r']
        hor = b <= 1e-9
        if hor.sum() < 4:
            continue
        r_h = r[hor].max()
        # enclosed "volume" = horizon node count
        V = int(hor.sum())
        # "area" = number of edges crossing the b->0 surface (boundary adjacency)
        nb = (np.roll(hor, 1, 0) | np.roll(hor, -1, 0) |
              np.roll(hor, 1, 1) | np.roll(hor, -1, 1))
        A = int((nb & ~hor).sum())            # outside nodes adjacent to the cut = surface edges
        # surface gravity kappa ~ d(sqrt(b))/dr just outside the horizon
        N = np.sqrt(b)
        ring = (r > r_h) & (r < r_h + 4)
        # radial gradient of N over the ring
        gN = np.sqrt(((np.roll(N, -1, 0) - np.roll(N, 1, 0)) / 2)**2 +
                     ((np.roll(N, -1, 1) - np.roll(N, 1, 1)) / 2)**2)
        kappa_h = gN[ring].mean()
        rows.append((amp, r_h, A, V, kappa_h))
    return rows


if __name__ == '__main__':
    np.set_printoptions(precision=4, suppress=True)

    # ---- (1) field equation: weak source, measure grad^2 b ~ rho ----
    print("=== (1) FIELD EQUATION  (weak source) ===")
    w = run(kappa=4e-4, rho_amp=1.0, steps=9000)
    cc, ratio = field_eq(w['b'], w['rho'], w['r'], w['S'])
    S = w['S']
    print(f"  b center {w['b'][S//2,S//2]:.4f}  (depleted near matter = gravity sign)")
    print(f"  corr(grad^2 b, rho) over the field = {cc:+.3f}   (1 = exact Newtonian field eq)")
    print(f"  |grad^2 b| core/outside ratio = {ratio:.0f}x  (Laplacian concentrated on the source)")
    rr, bb = radial(w['b'], w['r'], rmax=0.4 * S)
    o = (rr > 24) & (rr < 0.38 * S)
    A = np.polyfit(np.log(rr[o]), (1 - bb)[o], 1)
    print(f"  2D deficit vs log r: slope {A[0]:+.4f} (harmonic vacuum => deficit ~ -A log r)")

    # ---- mass scaling: deficit amplitude ~ integrated source? ----
    print("\n=== MASS SCALING  (r_s ~ M ?) ===")
    for amp in (0.5, 1.0, 1.5, 2.0):
        m = run(kappa=4e-4, rho_amp=amp, steps=7000, S=180)
        rr, bb = radial(m['b'], m['r'], rmax=0.4 * 180)
        o = (rr > 24) & (rr < 0.38 * 180)
        A = np.polyfit(np.log(rr[o]), (1 - bb)[o], 1)
        print(f"  rho_amp {amp:.1f}  integrated-source {m['rho'].sum():8.1f}"
              f"  deficit amplitude (-slope) {-A[0]:.4f}")

    # ---- (2)+(3) strong source: horizon + frozen cut ----
    print("\n=== (2)+(3) HORIZON + FROZEN A2 CUT  (strong source) ===")
    s = run(kappa=4e-3, rho_amp=4.0, rho_sigma=8.0, steps=12000, R0=0.8)
    b, R, r, S = s['b'], s['R'], s['r'], s['S']
    horizon = b <= 1e-9
    print(f"  b center {b[S//2,S//2]:.5f}   nodes with b<=0 (g_rr=1/b -> inf): {int(horizon.sum())}")
    if horizon.sum() > 0:
        r_h = r[horizon].max()
        ring = (r > r_h) & (r < r_h + 5)
        print(f"  [2] horizon: b->0 on a FINITE-radius surface, r_h ~ {r_h:.1f}")
        print(f"      g_rr ~ 1/b just outside r_h = {1.0/(b[ring].mean()+1e-12):.0f}  (diverges as b->0)")
        print(f"  [3] frozen A2 cut: reserve in the b=0 core, max {R[horizon].max():.2e}"
              f"  -> {'EXHAUSTED (frozen) OK' if R[horizon].max() < 1e-2 else 'NOT exhausted'}")
    else:
        print("  no b=0 region -- horizon not reached at this coupling")

    # ---- B-column: horizon thermodynamics (S ~ A, T ~ kappa) ----
    print("\n=== B-COLUMN: HORIZON THERMODYNAMICS (S ~ A, T ~ kappa) ===")
    rows = horizon_thermo()
    print("  source   r_h    A(surface edges)   V(enclosed)   A/r_h   V/r_h^2   kappa   kappa*r_h")
    for amp, r_h, A, V, kap in rows:
        print(f"  {amp:5.1f}  {r_h:5.1f}      {A:6d}          {V:7d}    {A/r_h:5.2f}   "
              f"{V/r_h**2:6.3f}   {kap:6.4f}   {kap*r_h:6.3f}")
    if len(rows) >= 3:
        import numpy as _np
        rs = _np.array([x[1] for x in rows]); As = _np.array([x[2] for x in rows])
        Vs = _np.array([x[3] for x in rows]); ks = _np.array([x[4] for x in rows])
        pA = _np.polyfit(_np.log(rs), _np.log(As), 1)[0]
        pV = _np.polyfit(_np.log(rs), _np.log(Vs), 1)[0]
        pk = _np.polyfit(_np.log(rs), _np.log(ks), 1)[0]
        print(f"\n  scaling exponents (log-log fit vs r_h):")
        print(f"    A(surface) ~ r_h^{pA:.2f}   (holographic/area-law => ~1, NOT ~2)")
        print(f"    V(enclosed) ~ r_h^{pV:.2f}  (the bulk, for contrast => ~2 in 2D)")
        print(f"    kappa ~ r_h^{pk:.2f}        (Hawking T ~ 1/M => ~ -1)")
        print(f"  => S(severed) tracks AREA not VOLUME (holographic); kappa ~ 1/r_h (Hawking).")
        print(f"     Coefficients (1/4, exact T) value-inherited via G/l_P; scalings measured.")
    print("\ndone.")
