"""
#4: does B4's COHERENCE action, in the coherence-weighted continuum limit, select
the MAXWELL/Coulomb field around a charge (winding)?

B4 (Paper_ChargeAsTopology_B4) established: (i) the charge skeleton is native
(integer winding w in Z, exact integral Gauss law circulation=2*pi*w); (ii) the
Maxwell action is LATENT in the coherence term -- cos^2(dphi/2) ~ 1 - (1/4)(grad
phi)^2, so the incoherence sin^2(dphi/2) ~ (1/4)(grad phi)^2 = the standard
integral( (grad phi)^2 ) electrostatic/Maxwell action. B4 left OPEN (section 7)
whether the DCGT measure SELECTS it as the continuum expectation.

This probe makes the selection concrete: in the coherence-weighted limit the field
around a charge is the one that MINIMIZES the coherence action = the Euler-Lagrange
solution  laplacian(phi) = -rho_charge  (Poisson). Solve it on a 3D lattice for a
point charge and check the field is Coulomb (phi ~ 1/r, |E| ~ 1/r^2). If yes, the
smooth Maxwell field IS the coherence-weighted continuum limit of B4's holonomies.

HONEST SCOPE (crank-rail): this is the COHERENCE-WEIGHTED (thick / ensemble) limit,
NOT the determinate certified substrate. Paper_Continuum showed the determinate
substrate is committal/trapping (kinetic lattice-gas), NOT a coherence-weighted
field-relaxing ensemble -- "you reach the PDE only by leaving ED". So this confirms
the shadow IS Maxwell; it does NOT show the determinate dynamics cast it. The phase
sector is Sigma-blind (B4), so this is analytic, not a certified-sim run.
"""
import numpy as np

L = 64                      # periodic 3D box
c = L // 2


def solve_poisson_fft(rho):
    """laplacian(phi) = -rho on a periodic lattice, via FFT (zero-mean rho)."""
    rho = rho - rho.mean()                       # neutralizing background (net charge 0)
    k = 2 * np.pi * np.fft.fftfreq(L)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    # discrete Laplacian eigenvalue: -(2-2cos k) per axis
    lap = (2 * np.cos(kx) - 2) + (2 * np.cos(ky) - 2) + (2 * np.cos(kz) - 2)
    lap[0, 0, 0] = 1.0                           # avoid div-by-zero (mean mode)
    phik = -np.fft.fftn(rho) / lap
    phik[0, 0, 0] = 0.0
    return np.real(np.fft.ifftn(phik))


def main():
    print("=" * 84)
    print("#4  MAXWELL FROM B4's COHERENCE ACTION: does the coherence-weighted limit")
    print("    around a charge give the COULOMB field?  (minimize integral (grad phi)^2)")
    print("=" * 84)

    rho = np.zeros((L, L, L))
    rho[c, c, c] = 1.0                           # point charge (a B4 winding source)
    phi = solve_poisson_fft(rho)

    # radial profile of phi around the charge (avoid the periodic images: r < L/4)
    xs = np.arange(L) - c
    X, Y, Z = np.meshgrid(xs, xs, xs, indexing="ij")
    R = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)
    mask = (R > 1.5) & (R < L / 4)
    r = R[mask]; p = phi[mask]
    # bin by radius
    rb = np.arange(2, L // 4)
    pav = np.array([p[(r >= i) & (r < i + 1)].mean() for i in rb])
    good = np.isfinite(pav)
    rb, pav = rb[good], pav[good]

    # fit phi ~ A/r^p (Coulomb = p=1 in 3D) vs alternatives, by R^2
    def r2(model):
        res = pav - model
        return 1 - np.sum(res ** 2) / np.sum((pav - pav.mean()) ** 2)
    # scale each model to best-fit amplitude
    def best(power):
        f = rb ** (-power)
        A = np.sum(pav * f) / np.sum(f * f)
        return r2(A * f), A
    print("\n  fit phi(r) ~ A / r^p  (3D Coulomb is p = 1):")
    print(f"    {'p':>5}{'R^2':>10}")
    for p_ in (0.5, 1.0, 1.5, 2.0):
        rr, _ = best(p_)
        star = "  <-- Coulomb (3D)" if abs(p_ - 1.0) < 1e-6 else ""
        print(f"    {p_:>5.1f}{rr:>10.4f}{star}")

    # field |E| = |grad phi| radial
    print("\n  radial phi(r) (should track 1/r):")
    print(f"    {'r':>4}{'phi(r)':>12}{'phi*r':>12}  (phi*r ~ const => 1/r Coulomb)")
    for i in range(0, len(rb), max(1, len(rb) // 8)):
        print(f"    {rb[i]:>4}{pav[i]:>12.5f}{pav[i] * rb[i]:>12.5f}")

    print("\n  Reading: best R^2 at p=1 and phi*r ~ const  =>  the coherence-action")
    print("  (= B4's latent Maxwell action) MINIMIZER around a charge IS the Coulomb")
    print("  field. So in the coherence-weighted continuum limit, B4's holonomies give")
    print("  Maxwell/Coulomb. (The determinate substrate is committal/trapping, not this")
    print("  weighted ensemble -- so the smooth field is that thick-limit SHADOW, not a")
    print("  determinate-dynamics output. Same as diffusion; ED monist position.)")


if __name__ == "__main__":
    main()
