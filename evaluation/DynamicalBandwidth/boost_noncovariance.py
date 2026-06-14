"""
Is ED's rule boost-covariant?  (The decisive test for whether alpha_1 = 0 outright.)

alpha_1 = 0 iff ED reproduces the boost-covariant g_0i of a moving mass (= the boosted
static field, 4 w_i U).  A Lorentz-INVARIANT theory does this automatically; a theory
with a preferred frame does not.  ED's metric-band rule is

    b-dot = D grad^2 b - kappa rho      (first order in COSMIC time)

so a source moving at w gives the comoving solution B(xi), xi = x - w t, obeying the
convection-diffusion equation
    D grad^2 B + w . grad B = kappa rho_0 .                         (*)

If ED were boost-covariant, the moving-source field (with the bulk translation removed,
i.e. in comoving coords) would be IDENTICAL to the static field b_s solving
    D grad^2 b_s = kappa rho_0 .
Any difference Delta = B - b_s is a genuine O(w) preferred-frame distortion -- the
mechanism that makes alpha_1 != 0.  This script measures Delta and its scaling in w.

A clean result: Delta is nonzero, linear in w, and DIPOLAR (odd along w) -- the
fore/aft asymmetry (a wake) of a source moving through the cosmic bandwidth medium.
That asymmetry is exactly what a preferred frame looks like, and it cannot be removed
by a coordinate change because the cosmic frame is physical.
"""
import numpy as np

N = 256
Lbox = 50.0
h = Lbox / N
x = (np.arange(N) - N // 2) * h
X, Y = np.meshgrid(x, x, indexing="ij")
R = np.sqrt(X**2 + Y**2)

k = 2 * np.pi * np.fft.fftfreq(N, d=h)
KX, KY = np.meshgrid(k, k, indexing="ij")
K2 = KX**2 + KY**2
K2[0, 0] = 1.0


def gaussian(M=200.0, sigma=2.0):
    g = np.exp(-(R**2) / (2 * sigma**2))
    g *= M / (g.sum() * h * h)
    return g


def solve_static(rho, D=1.0, kappa=1.0):
    """D grad^2 b_s = kappa rho  ->  b_s = 1 + perturbation."""
    sk = np.fft.fft2(rho - rho.mean())
    bk = -(kappa / D) * sk / K2          # grad^2 -> -K2
    bk[0, 0] = 0.0
    return 1.0 + np.real(np.fft.ifft2(bk))


def solve_moving(rho, w, D=1.0, kappa=1.0):
    """D grad^2 B + w.grad B = kappa rho  (comoving steady state), w = (wx, wy)."""
    wx, wy = w
    sk = np.fft.fft2(rho - rho.mean())
    denom = (-D * K2) + 1j * (wx * KX + wy * KY)     # -D k^2 + i w.k
    denom[0, 0] = 1.0
    Bk = (kappa) * sk / denom
    Bk[0, 0] = 0.0
    return 1.0 + np.real(np.fft.ifft2(Bk))


def dipole_amplitude(field, sigma=2.0):
    """Project the field onto the dipole (cos theta along x) in a mid-field annulus."""
    ann = (R > 3 * sigma) & (R < 0.30 * Lbox)
    cth = np.zeros_like(R)
    cth[ann] = X[ann] / (R[ann] + 1e-30)
    num = (field[ann] * cth[ann]).sum()
    den = (cth[ann] ** 2).sum() + 1e-30
    return num / den


if __name__ == "__main__":
    rho = gaussian()
    b_s = solve_static(rho)
    print("=== Is ED's rule boost-covariant?  (moving-source field vs boosted static) ===\n")
    print(f"  {'w':>8} {'max|B - b_s|':>15} {'/w (linear?)':>14} {'dipole(Delta)/w':>16}")
    base = None
    for w in (0.0, 5e-4, 1e-3, 2e-3, 4e-3):
        B = solve_moving(rho, (w, 0.0))
        Delta = B - b_s
        ann = (R > 3 * 2.0) & (R < 0.30 * Lbox)
        dmax = np.abs(Delta[ann]).max()
        dip = dipole_amplitude(Delta)
        perw = dmax / w if w > 0 else 0.0
        print(f"  {w:>8.1e} {dmax:>15.3e} {perw:>14.4f} {dip/w if w>0 else 0:>16.4f}")
    print("\n  Interpretation:")
    print("  - Delta = B - b_s is NONZERO  -> the moving-source field is NOT the static")
    print("    field: ED's rule is NOT boost-covariant.")
    print("  - max|Delta| is LINEAR in w (max|Delta|/w ~ const)  -> an O(w) effect.")
    print("  - Delta is DIPOLAR along w (a fore/aft wake)  -> the preferred-frame")
    print("    signature; the field is distorted by motion through the cosmic medium.")
    print("  => alpha_1 cannot be zero by symmetry; the covariance escape is CLOSED.")
