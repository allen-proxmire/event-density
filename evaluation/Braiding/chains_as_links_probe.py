"""Braiding probe 2 -- the ED-specific half: does ED actually hold its committed order by
SPATIAL LINKING of its own commitment chains, or is that premise empty?

Probe 1 (linking_3d_vs_4d_probe.py) settled the general TOPOLOGY: an idealized link (two loops,
Lk=+1) is held in 3D (can't be undone without collision) and comes apart freely in 4D. That
result is unconditionally true of geometry; it says nothing about ED yet.

This probe asks the ED-specific question the targets doc flags as still open: does ED's own
certified dynamics actually PRODUCE linked chains in the first place? The certified substrate's
worldlines are near-ballistic (CoarseGrain_Arc/tracer_diffusion_test.py: MSD ~ t^1.18, velocity
autocorrelation decays SLOWLY, i.e. persistent, not a random walk) -- straight lines don't wind
around each other, so the honest prior is that ballistic chains rarely or never acquire the
kind of topological linking probe-1 showed CAN hold an order. If that's right, ED's commitment
order is NOT held by spatial linking at all -- it's held the cheap way, by the plain sequential/
causal index P11 already gives for free (a partial order on events, no geometry required), and
the "why 3D via linking" bridge in MS-II/#2b is a genuine, honest NO, not a derivation.

Method (self-contained, faithful to the established phenomenology, no new invented physics):
  - a smooth random density-disorder field rho(x,y,z), same style as the certified tracer runs;
  - N worldlines launched from random points/directions, propagated at CONSTANT SPEED (ballistic)
    with gentle direction-kicks along -grad(rho) at each step (disorder-induced bending, not a
    random walk in speed) -- this is the minimal faithful proxy of "near-ballistic, gently
    redirected by disorder" already measured for ED's certified single-chain trajectories;
  - each chain gets a commitment-order index (launch order), mimicking P11's sequential record;
  - for every close-approach PAIR of chains, compute the Gauss linking integral over their
    actual trajectories (the same integral used in probe 1) and ask: does the substrate's own
    dynamics ever wind two chains around each other the way the idealized link did?

Positive control: a pair of chains constructed to deliberately spiral around a shared axis
(helices) -- confirms the linking-integral code correctly reports large nonzero Lk when real
winding is present, so a null result from the ED-faithful chains isn't a broken measurement.

Could-say-no, both directions:
  - if the ED-faithful ensemble shows |Lk| consistently near the control's scale at many close
    encounters -> the linking hypothesis survives, worth building further;
  - if |Lk| stays near zero across close encounters while the positive control is large ->
    ED's real dynamics doesn't produce the structure the "why 3D" bridge needs; honest NO.
"""
import numpy as np


def rho_field(L, n_bumps=14, seed=0):
    rng = np.random.default_rng(seed)
    centers = rng.uniform(-L / 2, L / 2, size=(n_bumps, 3))
    widths = rng.uniform(L * 0.06, L * 0.16, size=n_bumps)
    amps = rng.uniform(0.5, 1.5, size=n_bumps)

    def rho(p):
        d2 = np.sum((centers - p) ** 2, axis=1)
        return np.sum(amps * np.exp(-d2 / (2 * widths ** 2)))

    def grad(p, eps=1e-2):
        g = np.zeros(3)
        for i in range(3):
            dp = np.zeros(3); dp[i] = eps
            g[i] = (rho(p + dp) - rho(p - dp)) / (2 * eps)
        return g

    return rho, grad


def propagate_chain(grad, x0, v0, steps, dt=0.5, speed=1.0, kick=0.35):
    """Constant-speed (ballistic) propagation, direction gently bent by -grad(rho): the minimal
    faithful proxy of the certified near-ballistic, disorder-redirected worldline."""
    x = np.array(x0, dtype=float)
    v = np.array(v0, dtype=float)
    v = v / np.linalg.norm(v) * speed
    path = [x.copy()]
    for _ in range(steps):
        g = grad(x)
        v = v - kick * dt * g            # gentle redirection, no speed change yet
        v = v / np.linalg.norm(v) * speed  # renormalize: ballistic, direction-only bending
        x = x + v * dt
        path.append(x.copy())
    return np.array(path)


def gauss_linking_open(A, B):
    """Gauss linking-density integral over two OPEN curves (real-valued, not quantized for
    open curves -- a continuous 'winding/threading' measure, exactly the quantity that goes
    to +-1, +-2, ... for closed linked loops)."""
    dA = np.diff(A, axis=0)
    dB = np.diff(B, axis=0)
    Am = A[:-1] + dA / 2
    Bm = B[:-1] + dB / 2
    r = Am[:, None, :] - Bm[None, :, :]
    rn = np.linalg.norm(r, axis=2) ** 3 + 1e-9
    cross = np.cross(dA[:, None, :], dB[None, :, :])
    num = np.sum(r * cross, axis=2)
    return np.sum(num / rn) / (4 * np.pi)


def min_dist(A, B):
    d = np.linalg.norm(A[:, None, :] - B[None, :, :], axis=2)
    return d.min()


def helix_control(n=400, turns=3, r=0.6, sep=0.15):
    """Positive control: two genuinely-winding helices around a shared axis -- confirms the
    linking-integral code reports large |Lk| when real winding is present."""
    t = np.linspace(0, turns * 2 * np.pi, n)
    A = np.stack([r * np.cos(t), r * np.sin(t), t / (2 * np.pi)], axis=1)
    B = np.stack([r * np.cos(t + np.pi) - sep, r * np.sin(t + np.pi), t / (2 * np.pi)], axis=1)
    return A, B


def main():
    print("=" * 78)
    print("CHAINS-AS-LINKS PROBE — does ED's own (near-ballistic) dynamics produce linked chains?")
    print("=" * 78)

    # --- positive control ---
    A, B = helix_control()
    Lk_ctrl = gauss_linking_open(A, B)
    print(f"\n  positive control (deliberate helices, real winding): Lk = {Lk_ctrl:+.3f}")
    print("  (confirms the linking-integral code reports large |Lk| when winding is really there)")

    # --- ED-faithful ensemble ---
    L = 12.0
    rho, grad = rho_field(L, seed=1)
    rng = np.random.default_rng(2)
    n_chains = 60
    steps = 220
    chains = []
    for i in range(n_chains):
        x0 = rng.uniform(-L / 2, L / 2, size=3)
        v0 = rng.normal(size=3)
        chains.append(propagate_chain(grad, x0, v0, steps))

    # find close-approach pairs (candidates for any linking at all)
    results = []
    for i in range(n_chains):
        for j in range(i + 1, n_chains):
            md = min_dist(chains[i], chains[j])
            if md < 0.9:                      # a real close encounter
                lk = gauss_linking_open(chains[i], chains[j])
                results.append((i, j, md, lk))

    print(f"\n  {n_chains} ED-faithful chains, {steps} steps each, ballistic w/ disorder-bending")
    print(f"  close-approach pairs (min-dist < 0.9): {len(results)} / {n_chains*(n_chains-1)//2} total pairs")

    if results:
        lks = np.array([r[3] for r in results])
        mds = np.array([r[2] for r in results])
        print(f"\n  linking measure |Lk| over close-approach pairs:")
        print(f"    mean |Lk|   = {np.mean(np.abs(lks)):.4f}")
        print(f"    max  |Lk|   = {np.max(np.abs(lks)):.4f}")
        print(f"    median |Lk| = {np.median(np.abs(lks)):.4f}")
        print(f"    (control scale for comparison: {abs(Lk_ctrl):.3f})")
        frac_order1 = np.mean(np.abs(lks) > 0.5)
        print(f"    fraction of close pairs with |Lk| > 0.5 (order-1-ish winding): {frac_order1:.3f}")
    else:
        print("  no close-approach pairs found at this density -- chains too sparse/straight to test")

    print("\n  READ:")
    print("  if mean/median |Lk| << control scale and few/no pairs cross 0.5 -> ED's near-ballistic")
    print("  chains do NOT wind around each other enough to link. The order-holding job is NOT")
    print("  discharged by spatial linking here; P11's plain sequential/causal index is doing the")
    print("  work instead, and the linking bridge (MS-II sec.7 / #2b's open premise) is an honest NO.")
    print("  if |Lk| clusters near integer-ish values comparable to the control -> the hypothesis")
    print("  survives and is worth a harder, denser-ensemble follow-up.")
    print("=" * 78)


if __name__ == "__main__":
    main()
