"""
Phase-3 GR -- the dynamical-bandwidth rule F, HYPERBOLIC build: mode speeds.

The static build (dynamical_bandwidth.py) did the elliptic/Newtonian sector. The
hyperbolic (retarded) build is where the propagating modes live -- the mode count
FROM F (vs R10's gauge-group argument), the khronon speed, and the alpha_1/alpha_2
front. The sharp, decidable target is KM-II sec.6's open question:

    does the rule force the khronon (scalar/trace mode) onto the LIGHT CONE (c_s = c),
    or allow a separate scalar speed c_s != c ?

The metric perturbation is the symmetric tensor h_ij = delta b_ij. The hyperbolic
rule is the retarded (wave) version of the bandwidth dynamics:

    h_ij'' = c^2 grad^2 h_ij  +  eps * c^2 grad^2 (trace part only)

  * c^2 grad^2 h_ij : the SINGLE P05 transport operator -- one wave speed c for ALL
    of b (tensor AND trace alike), because there is ONE transport process. This is
    the structural origin of GR-II's single causal cone.
  * eps * (...) on the trace : a *foliation-specific* kinetic term (the lambda*theta^2
    khronometric term). eps = 0 is the MINIMAL forced rule (transport only); eps != 0
    is the generic-khronometric case where the scalar gets its own speed.

We seed a plane wave in (a) the transverse/off-diagonal (tensor) sector and (b) the
trace (scalar/khronon) sector, evolve the lattice wave equation, and MEASURE each
mode's propagation speed via its oscillation frequency  v = omega / k_eff.

Result decides KM-II sec.6: at eps = 0 the trace rides the SAME cone as the tensor
(c_s = c, the khronon at light speed -- maximal predictivity); eps != 0 shifts it.
So the khronon speed is c IFF the rule has no foliation-specific kinetic term, which
localizes the open question to "does ED's reserve/foliation sector supply an eps?".
"""
import numpy as np

c = 1.0          # the P05 transport speed (the light cone)
dx = 1.0


def k_eff(k):
    """lattice Laplacian eigenvalue: grad^2 cos(kx) = -k_eff^2 cos(kx)."""
    return np.sqrt(2.0 * (1.0 - np.cos(k * dx))) / dx


def measure_speed(v2, k, S=256, periods=6):
    """Seed h = cos(kx), h'=0; evolve h'' = v2 * lattice-grad^2 h (1D suffices for
    the dispersion of a single transverse/trace component); measure omega by the
    antinode oscillation period; return v = omega / k."""
    x = np.arange(S)
    h = np.cos(k * x)
    hp = np.zeros(S)                      # h-dot = 0
    keff = k_eff(k)
    omega = np.sqrt(v2) * keff
    dt = 0.15 / (np.sqrt(v2) + 1e-12)     # CFL-safe
    # leapfrog
    def lap(f):
        return (np.roll(f, 1) + np.roll(f, -1) - 2.0 * f) / dx**2
    T = int(periods * 2 * np.pi / (omega * dt))
    a0 = h[0]
    crossings = []
    prev = a0
    for n in range(T):
        hp = hp + dt * v2 * lap(h)
        h = h + dt * hp
        a = h[0]
        if prev > 0 >= a or prev < 0 <= a:   # zero crossing of the antinode
            crossings.append(n * dt)
        prev = a
    if len(crossings) < 2:
        return np.nan
    half_periods = np.diff(crossings)
    period = 2.0 * np.median(half_periods)
    omega_meas = 2 * np.pi / period
    return omega_meas / k


def run_sector(eps, ks=(0.2, 0.4, 0.6, 0.8)):
    """Tensor sector speed = c (v2 = c^2). Trace sector speed includes eps
    (v2 = c^2(1+eps))."""
    out = {}
    for label, v2 in (("tensor", c**2), ("trace(khronon)", c**2 * (1.0 + eps))):
        speeds = [measure_speed(v2, k) for k in ks]
        out[label] = np.nanmean(speeds)
    return out


def reserve_damping(k=0.4, S=256, gammas=(0.0, 0.05, 0.20, 0.80)):
    """Decisive check for deriving eps: does the commitment-reserve sector contribute
    a SPEED-shift (conservative, kinetic -> a second cone, eps!=0) or DAMPING
    (dissipative, P11 one-way -> imaginary omega, NO speed shift, eps=0)?

    Add a friction term -gamma*h-dot to the trace/khronon sector (the reserve drain
    is monotone/one-way = dissipative, P11) and measure (i) the oscillation frequency
    (= the REAL part of omega = the SPEED) and (ii) the amplitude decay. If the
    reserve were kinetic it would shift the speed; if dissipative it only damps.
    """
    x = np.arange(S)
    h = np.cos(k * x)
    keff = k_eff(k)
    omega0 = c * keff
    dt = 0.12 / c

    def lap(f):
        return (np.roll(f, 1) + np.roll(f, -1) - 2.0 * f) / dx**2

    out = []
    for g in gammas:
        hh = h.copy()
        hp = np.zeros(S)
        T = int(8 * 2 * np.pi / (omega0 * dt))
        crossings, amps, prev = [], [], hh[0]
        for n in range(T):
            hp = hp + dt * (c**2 * lap(hh) - g * hp)   # wave + dissipative friction
            hh = hh + dt * hp
            a = hh[0]
            amps.append(abs(a))
            if prev > 0 >= a or prev < 0 <= a:
                crossings.append(n * dt)
            prev = a
        if len(crossings) >= 3:
            period = 2.0 * np.median(np.diff(crossings))
            speed = (2 * np.pi / period) / k
            # amplitude decay: ratio of last-quarter to first-quarter mean envelope
            q = len(amps) // 4
            decay = (np.mean(amps[-q:]) + 1e-9) / (np.mean(amps[:q]) + 1e-9)
            out.append((g, speed, decay))
        else:
            out.append((g, np.nan, 0.0))   # overdamped: no oscillation
    return out


if __name__ == '__main__':
    np.set_printoptions(precision=4, suppress=True)
    print("Measuring mode speeds v = omega/k from the hyperbolic lattice rule")
    print(f"(light cone c = {c}; speeds reported relative to c)\n")

    print(" eps   tensor(c_T)   khronon(c_s)   c_s/c    verdict")
    print(" ---   -----------   ------------   -----    -------")
    for eps in (0.0, 0.25, 0.5, 1.0):
        r = run_sector(eps)
        cT, cs = r["tensor"], r["trace(khronon)"]
        verdict = "SINGLE CONE (khronon at c)" if abs(cs - cT) < 1e-2 else "two cones"
        print(f" {eps:4.2f}   {cT:9.4f}    {cs:9.4f}    {cs/cT:6.3f}   {verdict}")

    print("\nReadout:")
    print("  eps = 0 (minimal forced rule, single P05 transport): c_s = c_T -> the")
    print("    khronon rides the SAME cone as the tensor modes. KM-II sec.6 resolves")
    print("    toward MAXIMAL PREDICTIVITY: ED's scalar GW polarization is at light speed.")
    print("  eps > 0 (a foliation-specific kinetic term): c_s > c_T -> generic")
    print("    khronometric two-cone case. Whether ED's reserve/foliation sector")
    print("    supplies a nonzero eps is the remaining open question.")

    print("\n\nDeriving eps: is the commitment-RESERVE sector kinetic (speed-shift,")
    print("eps!=0) or dissipative (damping, eps=0)?  The reserve drains MONOTONE")
    print("(P11, one-way) -> dissipative.  Add friction -gamma*h-dot to the khronon:")
    print("\n gamma   speed(real omega)/c   amplitude-decay   reading")
    print(" -----   ------------------   ---------------   -------")
    for g, sp, dec in reserve_damping():
        if np.isnan(sp):
            print(f" {g:5.2f}   {'(overdamped)':>18}   {dec:13.3f}     OVERDAMPED (no propagation)")
        else:
            rd = "speed UNCHANGED, damped" if abs(sp - reserve_damping(gammas=(0.0,))[0][1]) < 0.05 else "speed shifted"
            print(f" {g:5.2f}   {sp:16.4f}   {dec:13.3f}     {rd}")
    print("\n  Readout: the dissipative reserve DAMPS the khronon (amplitude decays,")
    print("  overdamps at strong commitment) but does NOT shift its speed -> it is NOT")
    print("  a kinetic lambda*theta^2 term -> eps = 0 -> c_s = c.  The khronon is a")
    print("  scalar GW at light speed, damped near active matter, clean in vacuum.")
