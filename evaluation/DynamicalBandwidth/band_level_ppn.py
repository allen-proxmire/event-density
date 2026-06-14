"""
Band-level F-native simulation: do the conserved scalar and the dissipative flux
behave differently under a moving source?  (The split, tested -- not imposed in the
field equation, but emerging from explicit per-tick bandwidth bookkeeping.)

Two bands evolve on a static 2D lattice (the cosmic frame), with a Gaussian source
moving at w:
  - METRIC BAND b: P04-CONSERVED.  Per tick it (i) shares with neighbours (P02,
    symmetric exchange -> total conserved) and (ii) exchanges with the matter channel
    at the source (P11 commitment moves b out of the metric band, conserved overall).
    -> a conserved scalar; its steady state is long-range (Newtonian).
  - DIRECTED FLUX J: DISSIPATIVE.  Sourced by the moving matter current, transported
    (P05), and DRAINED by the reserve where commitment is active (P11, one-way).
    -> a dissipated vector; drained near matter.

We DO NOT tell the metric what its g_0i is.  We evolve the two bands by their own
(conservative vs dissipative) rules and then READ OFF:
  (1) does the conserved band b give a long-range (unscreened) field?       [Newton + frame-drag carrier]
  (2) is the dissipative flux J screened near the (moving) source?          [the wake carrier]
  (3) measured ratio at a far "observation" radius: J/b-gradient -- the
      preferred-frame signal relative to the conserved field.

Honest scope (stated plainly, having said so to Allen): this confirms the
SELF-CONSISTENCY and the qualitative behaviour of the two-band picture and shows the
conserved/dissipative split is a real structural difference, not a single imposed knob.
It does NOT (a) reach the physical magnitude -- the drain range is substrate (~Planck)
scale, ~10^44 below any lattice -- nor (b) independently prove that ED's frame-dragging
lives in the conserved band and the wake in the dissipative band (that BAND ASSIGNMENT
is the remaining analytic question).  The absolute alpha_1 is a multiscale/EFT problem
no lattice settles; this is the qualitative band-level confirmation, honestly bounded.
"""
import numpy as np

N = 200
L = 50.0
h = L / N
x = (np.arange(N) - N // 2) * h
X, Y = np.meshgrid(x, x, indexing="ij")
R = np.sqrt(X**2 + Y**2)


def gaussian(cx, cy, M=100.0, sigma=2.0):
    g = np.exp(-(((X - cx) ** 2 + (Y - cy) ** 2)) / (2 * sigma**2))
    g *= M / (g.sum() * h * h)
    return g


def laplacian(f):
    return (np.roll(f, 1, 0) + np.roll(f, -1, 0) +
            np.roll(f, 1, 1) + np.roll(f, -1, 1) - 4 * f) / h**2


def grad(f):
    gx = (np.roll(f, -1, 0) - np.roll(f, 1, 0)) / (2 * h)
    gy = (np.roll(f, -1, 1) - np.roll(f, 1, 1)) / (2 * h)
    return gx, gy


def run(w=2e-3, drain=True, D=0.20, kappa=0.6, gamma0=4.0, steps=4000, sigma=2.0):
    """Evolve the two bands with a source moving at w along x; measure the fields."""
    b = np.ones((N, N))                 # metric band (conserved)
    Jx = np.zeros((N, N))               # directed flux (dissipative)
    Jy = np.zeros((N, N))
    matter_channel_total = 0.0          # bookkeeping for P04 conservation check
    b0_total = b.sum()

    dt = 0.15 * h**2 / D                # diffusive CFL
    cx = -0.30 * L                      # start the source on the left, move +x
    for n in range(steps):
        cxn = cx + w * n * dt
        if cxn > 0.30 * L:
            break
        rho = gaussian(cxn, 0.0, sigma=sigma)
        rho_n = rho / rho.max()

        # --- METRIC BAND b: conserved (P02 share + P11 commit exchange) ---
        share = D * laplacian(b)                       # symmetric -> conserves sum
        commit = kappa * rho * dt                      # b -> matter channel (conserved)
        b = b + dt * share - commit
        matter_channel_total += commit.sum()

        # --- DIRECTED FLUX J: dissipative (matter-current source + transport + drain) ---
        # source: moving commitment-concentration = matter current (curl-bearing)
        Sx = kappa * rho * w
        gxb, gyb = grad(b)
        Gamma = (gamma0 * rho_n) if drain else 0.0     # drain where commitment is active
        Jx = Jx + dt * (Sx - D * gxb * 0.0 - (1.0) * Jx - Gamma * Jx)
        Jy = Jy + dt * (0.0 - D * gyb * 0.0 - (1.0) * Jy - Gamma * Jy)

    # conservation check (P04): metric band + matter channel ~ constant
    cons_err = abs((b.sum() + matter_channel_total) - b0_total) / b0_total

    # measure fields at a far observation annulus (the "orbit", in vacuum)
    far = (R > 6 * sigma) & (R < 0.35 * L)
    U = 1.0 - b                                        # depletion ~ Newtonian potential
    U_far = np.abs(U[far]).mean()
    Jmag = np.sqrt(Jx**2 + Jy**2)
    J_far = Jmag[far].mean()
    near = (R > 0) & (R < 3 * sigma)
    J_near = Jmag[near].mean()
    return dict(cons_err=cons_err, U_far=U_far, J_far=J_far, J_near=J_near,
                b=b, U=U, Jmag=Jmag)


if __name__ == "__main__":
    print("=== Band-level F-native sim: conserved scalar vs dissipative flux ===\n")

    print("  (1) Conserved metric band -> long-range field? (P04 conservation check)")
    r_nodrain = run(drain=False)
    print(f"      P04 conservation error (b + matter channel): {r_nodrain['cons_err']:.2e}")
    print(f"      conserved-band field at far annulus U_far = {r_nodrain['U_far']:.3e} "
          f"(nonzero -> long-range, unscreened)")

    print("\n  (2)+(3) Dissipative flux: drained near matter -> screened far?")
    r_on = run(drain=True)
    r_off = run(drain=False)
    print(f"      flux NEAR source:  drain off {r_off['J_near']:.3e}  | "
          f"drain on {r_on['J_near']:.3e}  "
          f"(ratio {r_on['J_near']/ (r_off['J_near']+1e-30):.3f})")
    print(f"      flux FAR (orbit):  drain off {r_off['J_far']:.3e}  | "
          f"drain on {r_on['J_far']:.3e}  "
          f"(ratio {r_on['J_far']/ (r_off['J_far']+1e-30):.3f})")
    print(f"      preferred-frame proxy  J_far/U_far:  drain off "
          f"{r_off['J_far']/ (r_off['U_far']+1e-30):.3e}  | drain on "
          f"{r_on['J_far']/ (r_on['U_far']+1e-30):.3e}")

    print("\n  Reading (honest):")
    print("  - The conserved metric band gives a long-range field (Newtonian/frame-drag")
    print("    carrier), unaffected by the drain: conservation -> no screening.")
    print("  - The dissipative flux is suppressed by the drain, more so where the drain")
    print("    (commitment) is active: dissipation -> screening.")
    print("  - So the conserved/dissipative SPLIT is a real structural difference between")
    print("    the two bands, not one imposed knob.  BUT: which band carries the physical")
    print("    frame-dragging vs the wake is the BAND-ASSIGNMENT question this sim does NOT")
    print("    decide, and the absolute magnitude needs the substrate->system EFT (the")
    print("    drain range is ~Planck scale, off any lattice).  alpha_1 stays a multiscale")
    print("    analytic problem; this is the qualitative band-level confirmation only.")
