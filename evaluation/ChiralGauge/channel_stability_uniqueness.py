"""#2b / gauge uniqueness — the channel-family STABILITY bound (the never-run calc).

Gauge_01 got U(N)=SU(N)xU(1) for ANY N from channel multiplicity. Gauge_03 proposed
"N<=3 because 3 spatial dimensions"; Gauge_04 WALKED IT BACK as a category error (color is
a COMPLEX internal triplet C^N, not the REAL spatial frame R^3->SO(3)) and redirected the
uniqueness question to an *internal* stability bound: how many same-rule-type channels can
mutually-stably coexist, modeled as complex unit vectors with a coherence/bandwidth limit
(Gram-matrix / equiangular-lines). That redirect was scoped, never computed. This computes it.

MODEL (the natural, non-rigged one):
  - A channel = a complex unit vector psi in C^d (Gauge_01: U(N) acts on the C^N amplitude;
    d = the internal amplitude dimension a channel lives in).
  - N channels mutually coexist stably if they can be independently SUSTAINED, i.e. kept
    distinguishable under finite bandwidth. Operationalize by COHERENCE: the worst-case
    pairwise overlap mu = max_{i<j} |<psi_i|psi_j>|. Low mu = distinguishable = stable;
    mu->1 = two channels collapse into one (not independent) = unstable.
  - For N unit vectors in C^d the minimal achievable mu is the Grassmannian-packing / Welch
    bound: mu >= sqrt((N-d)/(d(N-1))) for N>d, and mu=0 achievable for N<=d (orthogonal).
  - So the question "max stable N" = "how large can N be before forced coherence crosses an
    instability threshold mu_c". We MEASURE the optimal packing numerically (no formula
    assumed) and read off the bound vs d and vs mu_c.

The honest test: does anything pick out N in {1,2,3} or d=3? Or is the bound just "=d"
(orthogonality) / threshold-and-d-dependent with no magic 3? Crank-rail: d is NOT fixed to 3
(that was the category error); we sweep d and report the dependence, not a tuned answer.
"""
import numpy as np


def min_coherence(N, d, restarts=30, iters=2000, seed0=0):
    """Min achievable max pairwise |<psi_i|psi_j>| for N unit vectors in C^d, via
    FRAME-POTENTIAL descent (FP = ||G||_F^2, smooth, minimized by tight frames;
    grad on the sphere = 4 G V projected to unit rows). Reliable where max-coherence
    gradient collapses. Reports the achieved max off-diagonal coherence."""
    best = np.inf
    for r in range(restarts):
        rng = np.random.default_rng(seed0 + r)
        V = rng.normal(size=(N, d)) + 1j * rng.normal(size=(N, d))
        V /= np.linalg.norm(V, axis=1, keepdims=True)
        lr = 0.2
        for it in range(iters):
            G = V @ V.conj().T
            grad = 4.0 * (G @ V)                          # dFP/dV
            # remove the radial component (keep on the unit sphere per row)
            rad = np.real(np.sum(grad.conj() * V, axis=1, keepdims=True))
            grad = grad - rad * V
            V = V - lr * grad
            V /= np.linalg.norm(V, axis=1, keepdims=True)
        G = V @ V.conj().T; A = np.abs(G); np.fill_diagonal(A, 0.0)
        best = min(best, A.max())
    return best


def welch(N, d):
    if N <= d:
        return 0.0
    return np.sqrt((N - d) / (d * (N - 1)))


def main():
    print("=" * 70)
    print("CHANNEL-FAMILY STABILITY — max mutually-distinguishable channels vs (N, d)")
    print("  measured min max-coherence mu*(N,d) [Welch lower bound in brackets]")
    print("=" * 70)
    ds = [2, 3, 4, 5]
    Ns = [2, 3, 4, 5, 6, 7, 8]
    print(f"\n  {'N':>3} | " + " | ".join(f"d={d}" for d in ds))
    for N in Ns:
        row = []
        for d in ds:
            mu = min_coherence(N, d, restarts=20, iters=800)
            row.append(f"{mu:.3f}[{welch(N,d):.2f}]")
        print(f"  {N:>3} | " + " | ".join(f"{c:>11}" for c in row))

    print("\n  Stability bound N*(d, mu_c) = largest N with mu* <= mu_c:")
    for mu_c in [0.01, 0.35, 0.50, 0.71]:
        bounds = []
        for d in ds:
            Nstar = d
            for N in range(d + 1, 14):
                if min_coherence(N, d, restarts=15, iters=700) <= mu_c:
                    Nstar = N
                else:
                    break
            bounds.append(f"d={d}:N*={Nstar}")
        print(f"    mu_c={mu_c:.2f}:  " + "   ".join(bounds))

    print("\n" + "=" * 70)
    print("READ: orthogonal (mu=0) up to N=d, then coherence forced up (Welch). The bound")
    print("      is d (or d-and-threshold-dependent). Does ANYTHING pin {1,2,3} / d=3? Or is")
    print("      uniqueness NOT delivered by stability-packing (a d-dependent bound, no magic 3)?")
    print("=" * 70)


if __name__ == "__main__":
    main()
