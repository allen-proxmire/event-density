"""
Phase-3 GR -- the sub-leading reserve speed-renormalization of the khronon.

c_s = c is the LEADING-order result (the dissipative reserve damps the khronon, it
does not supply a lambda*theta^2 second cone -- the eps=0 derivation). But integrating
out the dissipative reserve (a friction term -gamma h-dot on the khronon) renormalizes
the REAL part of the dispersion sub-leadingly. The damped wave equation

    h'' + gamma h' + omega0^2 h = 0,   omega0 = c k,

oscillates at  omega_d = sqrt(omega0^2 - gamma^2/4),  so the phase speed is

    c_s/c = omega_d/omega0 = sqrt(1 - (gamma/2 c k)^2)  ~  1 - (1/2)(gamma/2ck)^2.

This is a TINY, gamma^2-suppressed, k-dependent shift BELOW c, vanishing in vacuum
(gamma -> 0) and at high k; and the mode OVERDAMPS (stops propagating) when gamma > 2ck.
This script measures omega_d(gamma)/omega_d(0) and confirms the formula -- the ratio
cancels the lattice dispersion offset, so it is the clean physical quantity.
"""
import numpy as np

c = 1.0
dx = 1.0


def omega_d(gamma, k, S=400, periods=10):
    """Seed cos(kx); evolve h'' = c^2 lap h - gamma h'; return the damped oscillation
    frequency omega_d, measured from antinode zero-crossing intervals."""
    x = np.arange(S)
    h = np.cos(k * x)
    hp = np.zeros(S)
    keff = np.sqrt(2*(1 - np.cos(k*dx)))/dx
    omega0 = c*keff
    dt = 0.1/c
    def lap(f):
        return (np.roll(f, 1) + np.roll(f, -1) - 2*f)/dx**2
    T = int(periods * 2*np.pi/(omega0*dt))
    cross, prev = [], h[0]
    for n in range(T):
        hp = hp + dt*(c**2*lap(h) - gamma*hp)
        h = h + dt*hp
        a = h[0]
        if (prev > 0) != (a > 0):           # sign change = zero crossing
            cross.append(n*dt)
        prev = a
        if abs(a) < 1e-7 and n > T//3:      # overdamped: amplitude gone
            break
    if len(cross) < 4:
        return np.nan                        # overdamped / no oscillation
    halfT = np.median(np.diff(cross))
    return np.pi/halfT


if __name__ == '__main__':
    np.set_printoptions(precision=5, suppress=True)
    k = 0.5
    keff = np.sqrt(2*(1 - np.cos(k*dx)))/dx
    om0 = c*keff
    print("Sub-leading reserve (friction) renormalization of the khronon speed")
    print(f"  k = {k},  omega0 = c*k_eff = {om0:.4f}  (the undamped reference)\n")
    print("  gamma   omega_d/omega0 (meas)   sqrt(1-(g/2omega0)^2) (pred)   c_s/c-1")
    print("  -----   --------------------   ---------------------------   -------")
    o0 = omega_d(0.0, k)
    for g in (0.0, 0.02, 0.05, 0.10, 0.20):
        od = omega_d(g, k)
        if np.isnan(od):
            print(f"  {g:5.2f}        (overdamped)              {np.sqrt(max(1-(g/(2*om0))**2,0)):.5f}"
                  f"            -- (no propagation)")
            continue
        ratio = od/o0
        pred = np.sqrt(max(1 - (g/(2*om0))**2, 0.0))
        print(f"  {g:5.2f}      {ratio:10.5f}             {pred:10.5f}              {ratio-1:+.5f}")
    print("\n  => c_s/c = sqrt(1 - (gamma/2ck)^2): a tiny, gamma^2-suppressed shift BELOW c,")
    print("     vanishing as gamma->0 (vacuum). The khronon is at c in vacuum; near matter")
    print("     it slows slightly, then OVERDAMPS (gamma > 2ck) -- never a second cone.")
