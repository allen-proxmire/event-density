"""
Phase-3 GR -- the HYPERBOLIC strong-field rule, built and run (the unbuilt piece).

State of the arc: the ELLIPTIC minimal rule  b_dot = D grad^2 b - kappa rho  gives the
weak field, Schwarzschild r_s ~ M, and a b->0 horizon -- but a DIRECT dynamical surface
gravity came out FLAT (kappa ~ r_h^0.09, dynamical_bandwidth_3d.py). Diagnosed structural:
the elliptic rule has a fixed sharing length (set by D) that makes the near-horizon
transition width r_h-INDEPENDENT, so the measured slope kappa = 1/2 db/dr does not scale.
The Hawking scaling kappa ~ 1/r_h held only ANALYTICALLY (the formula on the harmonic
b = 1 - r_s/r profile + measured r_s ~ M), not as a direct dynamical measurement.

The fix the arc names but never built: the HYPERBOLIC (wave) rule. hyperbolic_modes.py
built its LINEAR sector (h'' = c^2 grad^2 h, mode speeds, c_s = c). This script builds its
STRONG-FIELD sector -- the wave rule driven to a b->0 horizon -- and asks the decidable
question:

    does the HYPERBOLIC rule give a DIRECT dynamical  kappa ~ 1/r_h  where the elliptic
    rule gave flat kappa ?

Rationale (why it might): the wave rule has NO fixed diffusion length. The near-horizon
profile is set by the source + wave dynamics + the b>=0 clip (a hard wall the wave meets),
not by a D-set relaxation width -- so the transition can sharpen with the source and the
slope can scale.

The rules, identical source/clip/BC, only the time-operator differs:
  * ELLIPTIC   :  b_dot   = D c grad^2 b - kappa rho           (parabolic; the built rule)
  * HYPERBOLIC :  b_ddot  = c^2 grad^2 b - kappa rho - gamma b_dot
                  (the single-P05 transport wave operator + the DISSIPATIVE RESERVE as a
                   velocity damping gamma -- GR-III: the reserve damps, it is not a spatial
                   smoothing length, so it settles the wave WITHOUT reintroducing a fixed D.)
Both clip b>=0 (P04 floor -> the horizon) and hold asymptotic flatness b=1 at the box edge.

Measurement (the corrected one, strongfield_surface_gravity.py): metric -b dt^2 + b^-1 dr^2,
so kappa = 1/2 db/dr at the horizon. Compact source so the horizon forms in vacuum. Sweep
source strength -> sweep r_h -> fit kappa ~ r_h^p. Schwarzschild: p = -1.

Crank rail: the two rules share everything but the time-operator; nothing is tuned to give
1/r_h; the elliptic baseline reproducing FLAT in the same script is the control. Could-say-no
if the hyperbolic rule is ALSO flat (then the hyperbolic rule does not carry it either).
"""
import numpy as np

def lap3(f):
    return (np.roll(f, 1, 0) + np.roll(f, -1, 0)
            + np.roll(f, 1, 1) + np.roll(f, -1, 1)
            + np.roll(f, 1, 2) + np.roll(f, -1, 2) - 6.0 * f)


def _src(S, rho_amp, rho_sigma):
    a = np.arange(S) - (S - 1) / 2.0
    X, Y, Z = np.meshgrid(a, a, a, indexing="ij")
    r = np.sqrt(X**2 + Y**2 + Z**2)
    rho = rho_amp * np.exp(-(r**2) / (2 * rho_sigma**2))
    return rho, r


def _edge_flat(b):
    b[0, :, :] = b[-1, :, :] = 1.0
    b[:, 0, :] = b[:, -1, :] = 1.0
    b[:, :, 0] = b[:, :, -1] = 1.0


def run_elliptic(S, kappa, rho_amp, rho_sigma, steps, D=0.14):
    rho, r = _src(S, rho_amp, rho_sigma)
    b = np.ones((S, S, S))
    for _ in range(steps):
        b = b + D * lap3(b) - kappa * rho
        b = np.clip(b, 0.0, None)
        _edge_flat(b)
    return b, r


def run_hyperbolic(S, kappa, rho_amp, rho_sigma, steps, c=1.0, gamma=0.04, dt=0.4):
    rho, r = _src(S, rho_amp, rho_sigma)
    b = np.ones((S, S, S))
    bp = b.copy()                      # b at previous step (b_dot = 0 initially)
    c2dt2 = (c * dt) ** 2
    for _ in range(steps):
        accel = c2dt2 * lap3(b) - dt * dt * kappa * rho
        # damped leapfrog: b_new = b + (1-g)(b - bp) + accel ; g = gamma*dt
        g = gamma * dt
        b_new = b + (1.0 - g) * (b - bp) + accel
        b_new = np.clip(b_new, 0.0, None)
        _edge_flat(b_new)
        bp, b = b, b_new
    return b, r


def radial(field, r, nbin=140):
    rmax = (field.shape[0] - 1) / 2.0
    edges = np.linspace(0, rmax, nbin + 1)
    idx = np.digitize(r.ravel(), edges) - 1
    fr = field.ravel()
    prof, cen = [], []
    for k in range(nbin):
        m = idx == k
        if m.sum() >= 4:
            prof.append(fr[m].mean()); cen.append(0.5 * (edges[k] + edges[k + 1]))
    return np.array(cen), np.array(prof)


def _cross(cen, prof, level):
    """outermost-from-core radius where prof first rises through `level` going outward."""
    above = np.where(prof >= level)[0]
    if len(above) == 0 or above[0] == 0:
        return None
    j = above[0]
    r0, r1, p0, p1 = cen[j - 1], cen[j], prof[j - 1], prof[j]
    return r0 + (level - p0) * (r1 - r0) / (p1 - p0 + 1e-12)


def measure(field, r):
    """Surface gravity at the b->0 horizon, three ways, all near the horizon (no far window):
      - r_h        = radius where b crosses 0.05 (just outside the clipped core)
      - kappa_w    = 0.45 / (r(b=0.5) - r(b=0.05))  -- INNER transition width (robust)
      - kappa_dir  = 1/2 db/dr in a tight 3-cell window AT the horizon
      - r_s        = vacuum-fit Schwarzschild radius from b=1-r_s/r over b in [0.3,0.8]
                     (cross-check: kappa should be ~ 1/(2 r_s) for a sharp horizon)."""
    cen, prof = radial(field, r)
    if prof[0] > 0.05:                       # core never clipped to ~0: no horizon
        return None
    r05 = _cross(cen, prof, 0.05)
    r50 = _cross(cen, prof, 0.50)
    if r05 is None or r50 is None or r50 <= r05:
        return None
    w = r50 - r05
    kappa_w = 0.45 / w
    # direct tight slope at the horizon
    win = (cen >= r05) & (cen <= r05 + 3.0)
    kappa_dir = 0.5 * np.polyfit(cen[win], prof[win], 1)[0] if win.sum() >= 3 else np.nan
    # vacuum fit b = 1 - r_s/r  over the mid band
    band = (prof >= 0.3) & (prof <= 0.8) & (cen > r05)
    r_s = np.nan
    if band.sum() >= 4:
        # (1-b) = r_s * (1/r) through origin
        x = 1.0 / cen[band]; y = 1.0 - prof[band]
        r_s = float(np.dot(x, y) / np.dot(x, x))
    return dict(r_h=r05, kappa_w=kappa_w, kappa_dir=kappa_dir, r_s=r_s, b0=prof[0])


def sweep(rule_fn, label, S, kappa_c, amps, sigma, steps):
    print(f"\n  {label}", flush=True)
    rh, kwl, kdl = [], [], []
    for amp in amps:
        b, r = rule_fn(S, kappa_c, amp, sigma, steps)
        m = measure(b, r)
        if m is None:
            print(f"    amp={amp:5.1f}:  no horizon", flush=True); continue
        rh.append(m["r_h"]); kwl.append(m["kappa_w"]); kdl.append(m["kappa_dir"])
        print(f"    amp={amp:5.1f}:  r_h={m['r_h']:5.2f}  kappa_w={m['kappa_w']:.4f}  "
              f"kappa_dir={m['kappa_dir']:.4f}  r_s(fit)={m['r_s']:5.2f}  1/2r_s={0.5/m['r_s']:.4f}",
              flush=True)
    pw = pd = None
    if len(rh) >= 3:
        pw = np.polyfit(np.log(rh), np.log(kwl), 1)[0]
        good = [(a, b) for a, b in zip(rh, kdl) if b == b and b > 0]
        if len(good) >= 3:
            pd = np.polyfit(np.log([g[0] for g in good]), np.log([g[1] for g in good]), 1)[0]
        print(f"    --> kappa_w ~ r_h^{pw:+.2f}    kappa_dir ~ r_h^{pd if pd is None else round(pd,2)}"
              f"   (Hawking -1.00; flat 0.00)", flush=True)
    return pw


def main():
    # NR-GRADE CONFIG (dedicated compute): S=144 + strong sources resolves the sharp
    # hyperbolic horizons, but it is a ~2-hour run on a laptop -- not a background task.
    # The documented S=80 result (Hyperbolic_StrongField_Finding.md) shows: rule built,
    # measurement sound (elliptic control scales -0.34), hyperbolic horizons sub-resolution.
    # Run THIS config on real compute to get the decisive direct kappa~1/r_h (or an honest no).
    S = 144
    sigma = 2.5            # near-point source so the horizon forms in clean vacuum
    print("=" * 78, flush=True)
    print("HYPERBOLIC strong-field rule, v3 -- finer grid to RESOLVE the sharp horizons", flush=True)
    print(f"  (3D, S={S}, near-point source sigma={sigma}, light damping; inner-transition kappa)", flush=True)
    print("=" * 78, flush=True)
    amps = [40.0, 80.0, 160.0, 320.0, 600.0]
    pe = sweep(run_elliptic, "ELLIPTIC  b_dot = D grad^2 b - kappa rho   (control)",
               S, 6e-3, amps, sigma, steps=3200)
    ph = sweep(run_hyperbolic, "HYPERBOLIC b'' = c^2 grad^2 b - kappa rho - gamma b'  (gamma=0.04)",
               S, 6e-3, amps, sigma, steps=4800)
    print("\n" + "=" * 78, flush=True)
    print(f"  elliptic   kappa_w ~ r_h^{pe if pe is None else round(pe,2)}   (expect flat ~0)", flush=True)
    print(f"  hyperbolic kappa_w ~ r_h^{ph if ph is None else round(ph,2)}   (Hawking = -1)", flush=True)
    print("  READ: hyperbolic near -1 while elliptic flat => wave rule carries Hawking", flush=True)
    print("        scaling directly. Both flat => no (or still resolution-limited).", flush=True)
    print("=" * 78, flush=True)


if __name__ == "__main__":
    main()
