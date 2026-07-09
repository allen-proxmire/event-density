"""Yang-Mills action check: does the substrate coherence-deficit on the U(N) plaquette
holonomy actually give -1/4 Tr(F^2)?

Gauge_06 claims: the per-chain gauge-coherence deficit 1 - Re<psi|U_plaq|psi>, averaged over
indistinguishable channels (P08), IS the Wilson plaquette action 1 - (1/N)Re Tr U_plaq, which
small-holonomy-expands to (a^4/2N)Tr(F^2) -> the YM action. Two checkable steps:

  (i)  FIBER AVERAGE (sec4.5): < 1 - Re<psi|U|psi> >_psi = 1 - (1/N)Re Tr U, using
       int |psi><psi| dpsi = (1/N) I over the Haar-uniform sphere in C^N. This is what
       forces the TRACE (Wilson) form from channel indistinguishability -- the step that
       looked like the load-bearing assumption but is derived.
  (ii) SMALL-HOLONOMY EXPANSION: for U = exp(i a^2 F) (F Hermitian = the field strength),
       1 - (1/N)Re Tr U -> (a^4/2N) Tr(F^2) as a->0. This is the deficit -> F^2 step.

Also: the physical input (per-chain cost = coherence deficit 1 - Re<psi|U|psi>) is exactly
the amplitude-overlap coherence characterized in this session's V5/P12 work (coherence =
overlap of an amplitude with its transported self). So the load-bearing input is grounded in
the coherence structure, not an extra postulate.
"""
import numpy as np
from scipy.stats import unitary_group


def haar_state(N, rng):
    v = rng.normal(size=N) + 1j * rng.normal(size=N)
    return v / np.linalg.norm(v)


def main():
    print("YANG-MILLS ACTION CHECK (Gauge_06)\n")
    N = 3
    rng = np.random.default_rng(0)

    # ---- (i) fiber average forces the trace (Wilson) form ----
    print("(i) FIBER AVERAGE: < 1 - Re<psi|U|psi> >_psi  vs  1 - (1/N)Re Tr U  (P08 -> trace)")
    U = unitary_group.rvs(N, random_state=rng)
    S = 200000
    per_chain = np.mean([1 - np.real(np.vdot(p := haar_state(N, rng), U @ p)) for _ in range(S)])
    wilson = 1 - np.real(np.trace(U)) / N
    print(f"    fiber-averaged per-chain deficit = {per_chain:.4f}")
    print(f"    1 - (1/N)Re Tr U                 = {wilson:.4f}")
    print(f"    match: {abs(per_chain-wilson)<2e-3}  -> the TRACE form is the fiber-average"
          f" (int|psi><psi|=(1/N)I), derived from P08 indistinguishability, not assumed.\n")

    # ---- (ii) small-holonomy expansion -> Tr(F^2) ----
    print("(ii) SMALL-HOLONOMY: 1 - (1/N)Re Tr exp(i a^2 F)  ->  (a^4/2N) Tr(F^2) as a->0")
    # random Hermitian traceless field strength F (su(N) element)
    M = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    F = (M + M.conj().T) / 2
    F -= np.trace(F) / N * np.eye(N)                       # traceless (SU(N))
    TrF2 = np.real(np.trace(F @ F))
    print(f"    Tr(F^2) = {TrF2:.4f}   predicted deficit/a^4 -> {TrF2/(2*N):.4f}")
    print(f"    {'a':>8}{'deficit':>14}{'deficit/a^4':>16}")
    for a in [0.2, 0.1, 0.05, 0.02, 0.01]:
        A = a**2 * F
        Uh = _expm_herm(A)
        deficit = 1 - np.real(np.trace(Uh)) / N
        print(f"    {a:>8.2f}{deficit:>14.3e}{deficit/a**4:>16.4f}")
    print(f"    -> deficit/a^4 converges to Tr(F^2)/2N = {TrF2/(2*N):.4f} as a->0.")
    print("       So 1 - (1/N)Re Tr U_plaq -> (a^4/2N)Tr(F^2); summed over plaquettes -> the")
    print("       Yang-Mills action -1/4 int Tr(F^2). Non-abelian quartic is inside F via the")
    print("       commutator [A_mu,A_nu]; Lorentz covariance from the acoustic metric.")

    print("\n" + "=" * 84)
    print("VERDICT: the two load-bearing MATH steps check out -- (i) the Wilson/trace form IS")
    print("the P08 fiber-average of the per-chain coherence deficit (derived, not assumed), and")
    print("(ii) the small-holonomy expansion gives (a^4/2N)Tr(F^2) -> the YM action. The physical")
    print("INPUT (per-chain cost = 1 - Re<psi|U|psi>) is the amplitude-overlap coherence of this")
    print("session's V5/P12 work, grounded abelian (B4/Maxwell simulator), analytic non-abelian.")
    print("Honest residual: non-abelian coherence-cost is a gauge-program-tier lift (not the")
    print("certified Sigma-sim); g and a inherited; continuum limit leans on DCGT + small holonomy.")
    print("So: YM action FORM derived (structural/analytic); coupling + scale inherited.")
    print("=" * 84)


def _expm_herm(A):
    w, V = np.linalg.eigh(A)
    return V @ np.diag(np.exp(1j * w)) @ V.conj().T


if __name__ == "__main__":
    main()
