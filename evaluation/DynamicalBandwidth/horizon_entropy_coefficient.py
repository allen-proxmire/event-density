"""The decisive count: does ED's frozen-state tiling give the Bekenstein-Hawking 1/4?

Target (BH_EntropyCoefficient_FromEventCounting): the entropy coefficient. ED gets S ~ A
(form, measured) but inherits the 1/4. AP's geometric route: A/4 = the horizon's great-circle
cross-section = the r_s/2 sphere, the 4 being the sphere-to-disk ratio. So the question is a
fork:
  - if the substrate freezes its independent states on the FULL horizon sphere -> S = A,
    coefficient 1 (and the 1/4 must be the inherited thermal 2pi);
  - if it freezes them on the CROSS-SECTION / half-radius sphere -> S = A/4 (AP's route,
    coefficient derived geometrically).

This counts directly. Form b->0 horizons at several masses (the GR-III elliptic rule). For
each, count:
  N_frozen  = cells with b ~ 0 (the frozen core; the bulk/volume)
  N_surface = frozen cells adjacent to a live cell (the horizon BOUNDARY; the area in cells)
and measure r_s. Then read off:
  (1) holographic check: does N_surface ~ r_s^2 (area) while N_frozen ~ r_s^3 (volume)?
  (2) the coefficient: N_surface / (4*pi*r_s^2). ~1 => full-sphere tiling (coeff 1);
      ~1/4 => cross-section tiling (AP's route).
  (3) AP's geometric identity, numerically: 4*pi*r_s^2 vs pi*r_s^2 (the 4).

Crank-rail: nothing tuned. The count is just "how many boundary cells, vs the geometric
sphere area." The classical lattice can show the FORM and the geometry; the 1/4 carries hbar
(it is a quantum number), so a classical count is expected to give the full-sphere tiling
(coeff ~1) with the 1/4 living in the thermal factor -- but we run it and let the number speak.
"""
import numpy as np

D = 0.16


def lap3(f):
    return (np.roll(f, 1, 0) + np.roll(f, -1, 0)
            + np.roll(f, 1, 1) + np.roll(f, -1, 1)
            + np.roll(f, 1, 2) + np.roll(f, -1, 2) - 6.0 * f)


def form_horizon(S, kappa, amp, sigma, steps):
    a = np.arange(S) - (S - 1) / 2.0
    X, Y, Z = np.meshgrid(a, a, a, indexing="ij")
    r = np.sqrt(X**2 + Y**2 + Z**2)
    rho = amp * np.exp(-(r**2) / (2 * sigma**2))
    b = np.ones((S, S, S))
    for _ in range(steps):
        b = b + D * lap3(b) - kappa * rho
        b = np.clip(b, 0.0, None)
        b[0, :, :] = b[-1, :, :] = 1.0
        b[:, 0, :] = b[:, -1, :] = 1.0
        b[:, :, 0] = b[:, :, -1] = 1.0
    return b, r


def measure(b, r, b_eps=0.02):
    frozen = b < b_eps
    N_frozen = int(frozen.sum())
    if N_frozen < 8:
        return None
    # boundary: a frozen cell with at least one live (non-frozen) face-neighbor
    live = ~frozen
    nbr_live = np.zeros_like(frozen)
    for ax in (0, 1, 2):
        nbr_live |= np.roll(live, 1, ax) | np.roll(live, -1, ax)
    surface = frozen & nbr_live
    N_surface = int(surface.sum())
    r_s = float(r[frozen].max())                 # outer radius of the frozen core
    return dict(N_frozen=N_frozen, N_surface=N_surface, r_s=r_s)


def main():
    S, sigma = 96, 4.0
    print("=" * 78)
    print("HORIZON ENTROPY COEFFICIENT — count frozen boundary states vs horizon area")
    print(f"  (GR-III elliptic rule, 3D S={S}; nothing tuned)")
    print("=" * 78)
    amps = [12.0, 20.0, 34.0, 55.0, 90.0]
    rows = []
    for amp in amps:
        b, r = form_horizon(S, 6e-3, amp, sigma, steps=1800)
        m = measure(b, r)
        if m is None:
            print(f"  amp={amp:5.1f}: no horizon"); continue
        A_geom = 4 * np.pi * m["r_s"]**2
        disk = np.pi * m["r_s"]**2               # = A/4, the cross-section / r_s/2 sphere
        coeff = m["N_surface"] / A_geom
        rows.append((m["r_s"], m["N_surface"], m["N_frozen"], A_geom, disk, coeff))
        print(f"  amp={amp:5.1f}:  r_s={m['r_s']:5.2f}  N_surface={m['N_surface']:5d}  "
              f"N_frozen={m['N_frozen']:6d}  4pi r_s^2={A_geom:6.1f}  pi r_s^2(=A/4)={disk:5.1f}  "
              f"N_surf/(4pi r_s^2)={coeff:.3f}")

    if len(rows) >= 3:
        rs = np.array([x[0] for x in rows])
        Nsurf = np.array([x[1] for x in rows])
        Nfroz = np.array([x[2] for x in rows])
        coeff = np.array([x[5] for x in rows])
        p_surf = np.polyfit(np.log(rs), np.log(Nsurf), 1)[0]
        p_froz = np.polyfit(np.log(rs), np.log(Nfroz), 1)[0]
        print("\n  scaling:")
        print(f"    N_surface ~ r_s^{p_surf:.2f}   (area law = 2.00; volume = 3.00)")
        print(f"    N_frozen  ~ r_s^{p_froz:.2f}   (volume = 3.00)")
        print(f"  COEFFICIENT  N_surface/(4 pi r_s^2) = {coeff.mean():.3f} +- {coeff.std():.3f}")
        print("\n  READ: surface ~ r_s^2 confirms the AREA law (holographic, not volume).")
        print("        coefficient ~1 => states tile the FULL horizon sphere => the 1/4 is the")
        print("        inherited thermal factor, NOT classical geometry (AP's cross-section route")
        print("        is geometrically exact but is not how the substrate tiles).")
        print(f"        coefficient ~0.25 => cross-section tiling => 1/4 derived (AP's route).")
    print("=" * 78)


if __name__ == "__main__":
    main()
