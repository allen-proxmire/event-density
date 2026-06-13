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
    print("\ndone.")
