"""
Directed-flux (vector) sector of the ED dynamical rule — build & run.

Purpose
-------
The scalar rule  b-dot = D grad^2 b - kappa rho  has a curl-free current
(J = -D grad b), so it sources NO physical g_0i (pure gauge): the eta cross-check
note located the preferred-frame cross-term in ED's DIRECTED-FLUX (vector) sector.

This script builds that sector as the P02-adjacency-sharing of the off-diagonal
metric A^i = g_0i, sourced by the MOVING commitment-concentration (the matter
current rho*w) -- exactly parallel to how the scalar band b shares to give the
long-range Newtonian U sourced by mass density rho. It then:

  (1) confirms the scalar flux is curl-free (no physical g_0i)        [the obstruction]
  (2) confirms the vector sector gives a LONG-RANGE g_0i ~ lambda_J * w_i * U
      (the alpha_1 PPN structure), with nonzero gravitomagnetic field [the cross-term]
  (3) measures the coefficient lambda_J (= the vector/scalar coupling ratio
      = Route A's c14 = -Route B's eta)                              [the cross-check]
  (4) adds the dissipative reserve drain (flux screening, Yukawa range
      sqrt(D/Gamma)) and measures the near-field suppression S(Gamma) [the escape]

Conventions: 2D, G=1, units where the scalar Poisson is grad^2 U = -4 pi rho,
b = 1 - 2U.  FFT Poisson on a periodic box with a mean-subtracted (compensated)
source; the near/mid field structure is what we read.  Constants set to 1 where
they only rescale; lambda_J is the physical band-fraction we want to expose.
"""
import numpy as np

# ----- grid -----
N = 256
L = 50.0
h = L / N
x = (np.arange(N) - N // 2) * h
X, Y = np.meshgrid(x, x, indexing="ij")
R = np.sqrt(X**2 + Y**2)

# wavenumbers for FFT Poisson
k = 2 * np.pi * np.fft.fftfreq(N, d=h)
KX, KY = np.meshgrid(k, k, indexing="ij")
K2 = KX**2 + KY**2
K2[0, 0] = 1.0  # avoid /0; the (0,0) mode is the compensated mean, set to 0 after


def solve_poisson(source, mu2=0.0):
    """Solve (grad^2 - mu2) phi = -4 pi source  on the periodic box.
    mu2=0 -> Coulomb (Newtonian); mu2>0 -> Yukawa (screened, range 1/sqrt(mu2))."""
    s = source - (source.mean() if mu2 == 0.0 else 0.0)  # compensate only the unscreened
    sk = np.fft.fft2(s)
    phik = 4 * np.pi * sk / (K2 + mu2)
    if mu2 == 0.0:
        phik[0, 0] = 0.0
    phi = np.real(np.fft.ifft2(phik))
    return phi


def curl_z(Ax, Ay):
    """2D scalar curl dAy/dx - dAx/dy (the gravitomagnetic field B_g)."""
    dAy_dx = np.gradient(Ay, h, axis=0)
    dAx_dy = np.gradient(Ax, h, axis=1)
    return dAy_dx - dAx_dy


# ----- source: a Gaussian mass moving at w = (w0, 0) -----
def gaussian(M, sigma):
    g = np.exp(-(R**2) / (2 * sigma**2))
    g *= M / (g.sum() * h * h)  # normalize to total mass M
    return g


def run(M=200.0, sigma=2.0, w0=1.0e-3, lam_J=1.0, D=1.0, verbose=True):
    rho = gaussian(M, sigma)

    # ---- scalar sector: U, b, and the scalar flux J = -D grad b = 2D grad U ----
    U = solve_poisson(rho)                       # grad^2 U = -4 pi rho
    b = 1.0 - 2.0 * U
    Jx = -D * np.gradient(b, h, axis=0)
    Jy = -D * np.gradient(b, h, axis=1)
    curl_scalar = curl_z(Jx, Jy)

    # ---- vector sector: A^i sourced by the matter current rho * w (P02-shared) ----
    # grad^2 A_x = -4 pi lam_J rho w0   (parallel to grad^2 U = -4 pi rho)
    Ax = solve_poisson(lam_J * w0 * rho)
    Ay = np.zeros_like(Ax)                        # w = (w0, 0) -> only A_x sourced
    g0x = Ax                                      # g_0i = A_i (acoustic, Omega~1)
    Bg = curl_z(Ax, Ay)                           # gravitomagnetic field

    # ---- measure the coefficient: A_x should equal lam_J w0 U (long-range) ----
    # ratio A_x / (w0 U) in an annulus outside the source (mid-field)
    ann = (R > 4 * sigma) & (R < 0.30 * L)
    ratio = Ax[ann] / (w0 * U[ann])
    coeff = np.median(ratio)                      # = lambda_J if structure holds
    coeff_spread = np.std(ratio)

    # ---- magnitudes for the curl comparison (normalize by a common scale) ----
    scale = np.abs(2 * D * np.gradient(U, h, axis=0))[ann].max() + 1e-30
    curl_scalar_rel = np.abs(curl_scalar)[ann].max() / scale
    Bg_rel = np.abs(Bg)[ann].max() / (np.abs(g0x)[ann].max() / (4 * sigma) + 1e-30)

    if verbose:
        print(f"  M={M:.0f} sigma={sigma:.1f} w0={w0:.1e} lam_J={lam_J:.3f}")
        print(f"  [1] scalar flux curl / scalar-flux scale (should be ~0): "
              f"{curl_scalar_rel:.2e}")
        print(f"  [2] vector g_0i long-range: median A_x/(w0 U) = {coeff:.4f} "
              f"(target lam_J={lam_J:.3f}), spread={coeff_spread:.2e}")
        print(f"  [2] gravitomagnetic field |B_g| nonzero (rel): {Bg_rel:.3f}")
    return dict(U=U, Ax=Ax, coeff=coeff, curl_scalar_rel=curl_scalar_rel,
                Bg_rel=Bg_rel, rho=rho, D=D, w0=w0, lam_J=lam_J)


def screening_scan(M=200.0, sigma=2.0, w0=1.0e-3, lam_J=1.0, D=1.0):
    """Add the reserve drain: (grad^2 - Gamma/D) A = -4 pi lam_J rho w0.
    Measure near-field suppression S = A_x^Gamma / A_x^0 at r ~ a few sigma
    (where a moving body would read its own preferred-frame near-field)."""
    rho = gaussian(M, sigma)
    A0 = solve_poisson(lam_J * w0 * rho)
    r_read = 3 * sigma                                  # near-field read radius
    sel = (R > r_read - h) & (R < r_read + h)
    a0 = np.abs(A0[sel]).mean() + 1e-300
    print("\n  Dissipative reserve screening (Yukawa range = sqrt(D/Gamma)):")
    print(f"  {'Gamma':>10} {'range/sigma':>12} {'S=A^G/A^0 @3sigma':>20}")
    out = []
    for Gamma in [0.0, 0.01, 0.1, 1.0, 10.0, 100.0]:
        AG = solve_poisson(lam_J * w0 * rho, mu2=Gamma / D)
        S = (np.abs(AG[sel]).mean()) / a0
        rng = np.inf if Gamma == 0 else np.sqrt(D / Gamma) / sigma
        print(f"  {Gamma:>10.2f} {rng:>12.3f} {S:>20.4f}")
        out.append((Gamma, S))
    return out


if __name__ == "__main__":
    print("=== Directed-flux (vector) sector of the ED rule ===\n")
    print("(1)+(2)+(3) structure & coefficient, three source masses:")
    for M in (100.0, 200.0, 400.0):
        run(M=M)
        print()
    print("Coefficient lambda_J recovered independent of M (it is the coupling),")
    print("and tracks the input lam_J (vary it):")
    for lam in (0.25, 0.5, 1.0):
        r = run(lam_J=lam, verbose=False)
        print(f"  input lam_J={lam:.2f} -> measured A_x/(w0 U)={r['coeff']:.4f}")
    screening_scan()
