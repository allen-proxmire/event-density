"""The quadrupole RATE: does ED's scalar quadrupole luminosity match the observed binary-pulsar decay?

The polarization result showed ED radiates a scalar (breathing) mode. This probe asks the separate
quantitative question: does the RATE match? Binary-pulsar orbital decay measures the total GW
luminosity; GR attributes it to TENSOR quadrupole and matches Hulse-Taylor to ~0.1%. ED must account
for the SAME decay with SCALAR quadrupole radiation, and the coupling is NOT free: the same bandwidth
field b gives the static Newtonian potential (this session's Gauss law, coupling G), so the radiation
coupling is that same G. So the comparison is parameter-free.

Standard multipole luminosities (same G, same source second-moment M_ij = sum_i m_i x_i^a x_i^b):
  TENSOR (GR):   P_GR = (G/5 c^5) < Qdddot_ij Qdddot_ij >,  Q_ij = M_ij - (1/3) delta_ij M_kk (reduced)
  SCALAR (ED):   P_s  = (G/60 c^5) [ < (Mdddot_ii)^2 > + 2 < Mdddot_ij Mdddot_ij > ]
     (derived from a minimally-coupled massless scalar with the SAME static coupling G; the (Mdddot_ii)^2
      term is the scalar MONOPOLE/breathing radiation that GR has no analog of -- it vanishes for a
      circular orbit, contributes for an eccentric one.)

For a CIRCULAR orbit this gives the clean analytic ratio P_s/P_GR = 1/6 (derived below and confirmed
numerically): ED radiates SIX TIMES too little, so it predicts orbital decay ~6x too SLOW. Since GR
matches the pulsar decay to 0.1%, an O(1) factor like 1/6 is a GROSS mismatch, not a marginal tension.
For ECCENTRIC orbits ED additionally gains scalar monopole radiation GR lacks, so ED != GR by an O(1)
factor there too. This probe computes both.

Honest scope: the exact factor (1/6) uses the standard minimally-coupled-scalar normalization; ED has
not derived its scalar action from the substrate, so the precise number is uncertain. But the mismatch
is robust in KIND: any standard scalar gives an O(1) ratio != 1 (not 0.1%), plus a monopole term for
eccentric orbits. So the quadrupole RATE is a SECOND severe tension, on top of the polarization one.
This is a NEGATIVE result for ED gravity's radiative sector, reported straight, not spun.
"""
import numpy as np


def orbit_positions(m1, m2, a=1.0, e=0.0, n=4000):
    """Keplerian orbit (COM frame). Solve Kepler's equation for eccentricity e; return times and the
    two body positions over one period. Units: G(m1+m2)=1 so that the mean motion is set by a."""
    M = m1 + m2
    # mean motion from Kepler's third law with GM=1: n_mean = a^{-3/2}
    nmean = a ** (-1.5)
    P = 2 * np.pi / nmean
    t = np.linspace(0, P, n, endpoint=False)
    Mean = nmean * t
    E = Mean.copy()                                    # eccentric anomaly, Newton solve
    for _ in range(60):
        E = E - (E - e * np.sin(E) - Mean) / (1 - e * np.cos(E))
    # relative separation vector
    x = a * (np.cos(E) - e)
    y = a * np.sqrt(1 - e ** 2) * np.sin(E)
    rel = np.stack([x, y], axis=1)                     # r2 - r1 direction (relative coordinate)
    x1 = -(m2 / M) * rel
    x2 = +(m1 / M) * rel
    return t, x1, x2


def spectral_d3(f, t):
    """Third time-derivative via FFT (exact for periodic orbit harmonics). f shape (n,) or (n,k)."""
    n = len(t); T = t[-1] + (t[1] - t[0])
    k = np.fft.fftfreq(n, d=T / n) * 2 * np.pi
    F = np.fft.fft(f, axis=0)
    mult = (1j * k) ** 3
    if f.ndim == 2:
        mult = mult[:, None]
    return np.real(np.fft.ifft(mult * F, axis=0))


def second_moment(x1, x2, m1, m2):
    """M_ij(t) = sum_i m_i x_i^a x_i^b, the (unreduced) mass second moment. Return components as (n,3):
    [M_xx, M_yy, M_xy]."""
    def comp(x, m):
        return np.stack([m * x[:, 0] ** 2, m * x[:, 1] ** 2, m * x[:, 0] * x[:, 1]], axis=1)
    return comp(x1, m1) + comp(x2, m2)


def luminosities(t, M):
    """Given M_ij(t) (as [xx,yy,xy]), return (P_GR_tensor, P_scalar, monopole_fraction_of_scalar)
    in units with G=c=1 (only ratios matter)."""
    Mxx, Myy, Mxy = M[:, 0], M[:, 1], M[:, 2]
    trace = Mxx + Myy
    # reduced traceless quadrupole (for GR)
    Qxx = Mxx - trace / 3.0
    Qyy = Myy - trace / 3.0
    Qzz = -trace / 3.0
    Qxy = Mxy
    Q = np.stack([Qxx, Qyy, Qzz, Qxy], axis=1)
    d3Q = spectral_d3(Q, t)
    # Q_ij Q_ij (with off-diagonals doubled)
    QdotdotdotSq = d3Q[:, 0] ** 2 + d3Q[:, 1] ** 2 + d3Q[:, 2] ** 2 + 2 * d3Q[:, 3] ** 2
    P_GR = (1.0 / 5.0) * np.mean(QdotdotdotSq)

    # scalar: use full second moment M_ij (with M_zz = 0 since motion is planar)
    Mfull = np.stack([Mxx, Myy, np.zeros_like(Mxx), Mxy], axis=1)   # xx,yy,zz,xy
    d3M = spectral_d3(Mfull, t)
    trace3 = d3M[:, 0] + d3M[:, 1] + d3M[:, 2]                      # d3/dt3 of M_ii
    MdotdotdotSq = d3M[:, 0] ** 2 + d3M[:, 1] ** 2 + d3M[:, 2] ** 2 + 2 * d3M[:, 3] ** 2
    monopole = np.mean(trace3 ** 2)
    P_scalar = (1.0 / 60.0) * (monopole + 2.0 * np.mean(MdotdotdotSq))
    mono_frac = (1.0 / 60.0) * monopole / P_scalar if P_scalar > 0 else 0.0
    return P_GR, P_scalar, mono_frac


def main():
    print("=" * 90)
    print("QUADRUPOLE RATE: ED scalar quadrupole luminosity vs GR tensor quadrupole (same G)")
    print("=" * 90)
    m1, m2 = 1.44, 1.39           # ~ Hulse-Taylor neutron-star masses (solar)
    print(f"\n  binary masses m1={m1}, m2={m2} (Hulse-Taylor-like)\n")
    print(f"   {'eccentricity':>12} {'P_scalar/P_GR':>16} {'scalar monopole frac':>22}   verdict")
    for e in (0.0, 0.3, 0.617):
        t, x1, x2 = orbit_positions(m1, m2, a=1.0, e=e)
        M = second_moment(x1, x2, m1, m2)
        P_GR, P_s, mono = luminosities(t, M)
        ratio = P_s / P_GR
        note = "circular: analytic 1/6" if e == 0 else ("Hulse-Taylor e" if abs(e-0.617) < 1e-3 else "")
        print(f"   {e:>12.3f} {ratio:>16.4f} {mono:>21.1%}   {note}")

    print("\n  READ:")
    print("   Circular orbit: P_scalar/P_GR = 1/6 exactly (ED radiates 6x too little -> orbital decay")
    print("   ~6x too SLOW). GR matches the binary-pulsar decay to 0.1%, so a factor ~1/6 is a GROSS")
    print("   mismatch, not a marginal tension. Eccentric orbits: the ratio stays O(1) and ED gains")
    print("   SCALAR MONOPOLE (breathing) radiation that GR has no analog of (monopole frac > 0).")
    print("\n  VERDICT: the quadrupole RATE is a SECOND severe tension. ED's scalar radiation luminosity")
    print("  differs from GR's tensor quadrupole by an O(1) factor (~1/6 circular), with the coupling")
    print("  fixed (no freedom) by the static Newtonian G. Combined with the scalar POLARIZATION result,")
    print("  ED gravity's radiative sector -- as a kinematic scalar metric -- is substantially in tension")
    print("  with / falsified by binary-pulsar + GW data. This is the same wall that ruled out scalar")
    print("  gravity theories. Honest NEGATIVE result: the static/relational/MOND-rotation results stand,")
    print("  but the radiative predictions (polarization AND rate) are wrong, unless ED acquires a")
    print("  genuine dynamical-tensor sector -- which would mean abandoning the pure kinematic metric.")
    print("  (Exact 1/6 uses the standard scalar normalization; the O(1)-mismatch KIND is robust.)")
    print("=" * 90)


if __name__ == "__main__":
    main()
