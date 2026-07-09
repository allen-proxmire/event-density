"""Does ED's radiative sector survive the binary-pulsar / LIGO tension? The dipole question.

Paper E flagged the sharpest open tension: ED's metric is kinematic (a read-out of the bandwidth
field b), so gravitational radiation in ED is radiation of the SCALAR bandwidth field (b propagates
retarded via the V1 kernel + the arrow's finite substrate speed, so [] b = source has radiative
solutions). But a scalar gravitational field generically produces DIPOLE radiation, which binary
pulsars exclude most tightly and which kills most scalar-tensor theories. So the decisive question:

  Does ED structurally suppress dipole radiation?

The candidate structural reason (from this session's Gauss result): a mass IS its bandwidth-influence
Q, with a UNIVERSAL coupling Q proportional to M (same Q/M for every body -- the equivalence
principle for the bandwidth charge). Then the scalar dipole moment D = sum_i Q_i x_i equals (Q/M)
times the MASS dipole, whose second time derivative is d(total momentum)/dt = 0 for an isolated
binary. So D_dotdot = 0: NO dipole radiation, and the leading radiation is quadrupole, like GR.

This probe demonstrates it on a two-body circular orbit, and contrasts UNIVERSAL coupling (Q_i/m_i
the same) with NON-UNIVERSAL coupling (Q_i/m_i differing, as in generic scalar-tensor theories):
  - scalar dipole moment D(t) = sum_i Q_i x_i  (in the COM frame)
  - dipole radiated power  ~ <|D_dotdot|^2>
  - mass quadrupole Q_ij and its third derivative  (the quadrupole radiation source)
  - report dipole/quadrupole power ratio for both couplings.

Expected: universal -> D == 0 -> dipole power ~ machine zero, radiation starts at quadrupole (GR-like).
Non-universal -> D != 0 -> dipole radiation ~ (Delta(Q/m))^2, the scalar-tensor dipole the pulsars
exclude. So universal bandwidth coupling STRUCTURALLY evades the dipole catastrophe.

Honest scope: this settles the dipole question (the strongest pulsar killer) structurally; it does
NOT show the quadrupole RATE or POLARIZATION match GR (scalar quadrupole differs from GR's tensor
quadrupole in coefficient and polarization -- the sharpened remaining tension). And Q proportional
to M universally is the "mass = bandwidth-influence Q" reading of P04, a reading, not a canonical
statement.
"""
import numpy as np


def orbit(m1, m2, a=1.0, w=1.0, n=2000):
    """Two-body circular orbit in the COM frame. Return times and positions x1(t), x2(t) (2D)."""
    t = np.linspace(0, 2 * np.pi / w, n, endpoint=False)
    M = m1 + m2
    r1 = (m2 / M) * a; r2 = (m1 / M) * a
    x1 = np.stack([r1 * np.cos(w * t), r1 * np.sin(w * t)], axis=1)
    x2 = np.stack([-r2 * np.cos(w * t), -r2 * np.sin(w * t)], axis=1)
    return t, x1, x2, w


def ddt(f, t):
    """Periodic time-derivative via spectral (FFT) differentiation -- exact for the orbit harmonics."""
    n = len(t); T = t[-1] + (t[1] - t[0])
    k = np.fft.fftfreq(n, d=T / n) * 2 * np.pi
    F = np.fft.fft(f, axis=0)
    return np.real(np.fft.ifft(1j * k[:, None] * F, axis=0)) if f.ndim == 2 else \
           np.real(np.fft.ifft(1j * k * np.fft.fft(f)))


def analyze(label, m1, m2, q1, q2):
    t, x1, x2, w = orbit(m1, m2)
    # scalar dipole moment D(t) = q1 x1 + q2 x2  (COM frame)
    D = q1 * x1 + q2 * x2
    Dd = ddt(D, t); Ddd = ddt(Dd, t)                       # first, second derivative
    dipole_power = np.mean(np.sum(Ddd ** 2, axis=1))       # ~ <|D_dotdot|^2>

    # mass quadrupole Q_ij = sum q_i (x_i^a x_i^b) (reduced trace-free), radiation ~ <|d3Q/dt3|^2>
    def quad(x, q):
        Qxx = q * (x[:, 0] ** 2); Qyy = q * (x[:, 1] ** 2); Qxy = q * (x[:, 0] * x[:, 1])
        return Qxx, Qyy, Qxy
    Qxx = np.zeros(len(t)); Qyy = np.zeros(len(t)); Qxy = np.zeros(len(t))
    for x, q in [(x1, q1), (x2, q2)]:
        a, b, c = quad(x, q); Qxx += a; Qyy += b; Qxy += c
    tr = (Qxx + Qyy) / 2.0
    comps = np.stack([Qxx - tr, Qyy - tr, Qxy], axis=1)    # trace-free
    d3Q = ddt(ddt(ddt(comps, t), t), t)
    quad_power = np.mean(np.sum(d3Q ** 2, axis=1))

    ratio = dipole_power / quad_power
    print(f"  [{label}]  Q1/m1={q1/m1:.3f}, Q2/m2={q2/m2:.3f}")
    print(f"      |D|max (dipole moment)      = {np.max(np.linalg.norm(D, axis=1)):.3e}")
    print(f"      dipole radiated power       = {dipole_power:.3e}")
    print(f"      quadrupole radiated power   = {quad_power:.3e}")
    print(f"      dipole/quadrupole ratio     = {ratio:.3e}")
    return dipole_power, quad_power


def main():
    print("=" * 88)
    print("ED RADIATIVE SECTOR: does universal bandwidth coupling (Q ~ M) suppress DIPOLE radiation?")
    print("=" * 88)
    m1, m2 = 1.4, 1.0                 # a mass-asymmetric binary (worst case for dipole)
    alpha = 0.7                       # bandwidth charge-to-mass coupling

    print("\n (1) UNIVERSAL coupling  Q_i = alpha * m_i  (equivalence principle for the bandwidth charge):")
    dU, qU = analyze("universal", m1, m2, alpha * m1, alpha * m2)

    print("\n (2) NON-UNIVERSAL coupling  Q_i/m_i differs by 30% (generic scalar-tensor):")
    dN, qN = analyze("non-universal", m1, m2, alpha * m1, alpha * 1.3 * m2)

    print("\n READ:")
    print(f"   Universal coupling: the scalar dipole moment is exactly zero in the COM frame (|D|~{dU/qU:.0e}")
    print("   of quadrupole), so DIPOLE radiation vanishes and radiation starts at QUADRUPOLE -- like GR.")
    print("   This is the equivalence principle for the bandwidth charge: Q_i x_i = (Q/M) * (mass dipole),")
    print("   whose second derivative is d(momentum)/dt = 0 for an isolated binary.")
    print(f"   Non-universal coupling: dipole radiation reappears (ratio {dN/qN:.2e}, ~ (Delta(Q/m))^2) --")
    print("   the scalar-tensor dipole radiation binary pulsars exclude.")
    print("\n VERDICT: universal bandwidth coupling (Q ~ M, the 'mass = bandwidth-influence Q' reading)")
    print(" STRUCTURALLY evades the dipole catastrophe -- the strongest pulsar killer of scalar gravity.")
    print(" The remaining, sharpened tension: the scalar QUADRUPOLE rate and POLARIZATION vs GR's TENSOR")
    print(" quadrupole (pulsar 0.1% match + LIGO polarization) -- open, not shown here.")
    print("=" * 88)


if __name__ == "__main__":
    main()
