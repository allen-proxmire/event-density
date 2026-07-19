"""V5-coherence condensation probe (dark-sector / superfluid-relic program).

QUESTION: does a gas of committed relics coupled by the REAL V5 coherence functional
phase-LOCK (condense) in a calm environment and DECOHERE in a hot one -- and is the
transition mass-independent?

REAL V5 coupling (from evaluation/ChiralGauge/homochirality_v5_verify.py, Paper_090):
    E = sum_{i<j} w(r_ij) * cos(phi_i - phi_j),   w(r) = exp(-r/ell_V5)   [finite reach]
Note: the functional contains ONLY positions and phases. There is NO mass in it. So any
condensation it produces is mass-independent BY CONSTRUCTION -- unlike a de-Broglie (BEC)
condensation, which needs a light boson. That is the structural crux of the mass tension.

DYNAMICS (overdamped Langevin / Kuramoto with the V5 reach kernel; gradient ascent on E):
    dphi_i = K * sum_j w(r_ij) sin(phi_j - phi_i) dt  +  sqrt(2 D dt) * eta_i
  * K, ell : V5 coupling strength and reach (the coherence glue).
  * D      : DECOHERENCE = environmental phase noise. Proxy for the environment ("temperature"):
             low D = calm / low-acceleration = a galaxy (below a0);
             high D = hot / high velocity dispersion = a cluster (above a0).
  * eta    : unit Gaussian.

ORDER PARAMETER (the faithful V5 coherence):
    C = [sum_{i<j} w_ij cos(phi_i - phi_j)] / [sum_{i<j} w_ij]     in [-~0, 1]
  C ~ 1 : condensed (reach-weighted phases aligned).  C ~ 0 : dispersed (decohered).

TESTS:
  (1) sweep D (the environment): is there a condensation transition (C: ~0 -> ~1 as D falls)?
  (2) sweep N (relic count / abundance): does the transition move? (robustness)
  (3) mass-independence is structural (no mass in E); confirmed by the functional's form.
"""
import numpy as np


def run(N, D, K=1.0, ell=1.0, L=2.5, steps=6000, dt=0.02, burn=0.5, seed=0):
    rng = np.random.default_rng(seed)
    pos = rng.uniform(0.0, L, size=(N, 3))
    d = np.linalg.norm(pos[:, None, :] - pos[None, :, :], axis=2)
    W = np.exp(-d / ell)
    np.fill_diagonal(W, 0.0)
    Wsum = W.sum()  # sum over ordered pairs (i!=j); C uses the same normalization
    phi = rng.uniform(0.0, 2 * np.pi, size=N)
    acc = []
    for t in range(steps):
        # drive_i = K * sum_j W_ij sin(phi_j - phi_i)   (gradient ascent on E)
        diff = np.sin(phi[None, :] - phi[:, None])      # (N,N): sin(phi_j - phi_i)
        drive = K * np.sum(W * diff, axis=1)
        phi = phi + drive * dt + np.sqrt(2.0 * D * dt) * rng.standard_normal(N)
        if t > steps * burn:
            cosd = np.cos(phi[:, None] - phi[None, :])
            acc.append(float(np.sum(W * cosd) / Wsum))
    return float(np.mean(acc))


def main():
    print("V5-coherence condensation probe -- REAL V5 functional E=sum w(r)cos(dphi), no mass.\n")
    Ds = [0.02, 0.05, 0.1, 0.2, 0.35, 0.5, 0.75, 1.0, 1.5, 2.5]
    Ns = [20, 40, 80]

    print("(1)+(2) coherence order parameter C vs decoherence D (env), for several relic counts N:")
    print("        D:  " + "  ".join(f"{d:5.2f}" for d in Ds))
    Ccurves = {}
    for N in Ns:
        row = [run(N, D, seed=100 + N) for D in Ds]
        Ccurves[N] = row
        print(f"   N={N:3d}:  " + "  ".join(f"{c:5.2f}" for c in row))

    # transition D (where C crosses 0.5), per N
    def crossing(row):
        for i in range(len(Ds) - 1):
            if row[i] >= 0.5 >= row[i + 1]:
                # linear interp in D
                f = (row[i] - 0.5) / (row[i] - row[i + 1] + 1e-12)
                return Ds[i] + f * (Ds[i + 1] - Ds[i])
        return None

    print("\n  condensation threshold D_c (C=0.5), per N:")
    dcs = []
    for N in Ns:
        dc = crossing(Ccurves[N])
        dcs.append(dc)
        print(f"    N={N:3d}:  D_c = {dc:.3f}" if dc else f"    N={N:3d}:  D_c = (none)")

    print("\n" + "=" * 78)
    print("READ:")
    calm = np.mean([Ccurves[N][0] for N in Ns])   # D=0.02 (calm/galaxy)
    hot = np.mean([Ccurves[N][-1] for N in Ns])   # D=2.5  (hot/cluster)
    print(f"  calm (D=0.02, ~galaxy): C = {calm:.2f}   ->  {'CONDENSED' if calm>0.7 else 'not condensed'}")
    print(f"  hot  (D=2.5,  ~cluster): C = {hot:.2f}   ->  {'DISPERSED' if hot<0.2 else 'not dispersed'}")
    if all(d is not None for d in dcs):
        spread = (max(dcs) - min(dcs)) / np.mean(dcs)
        print(f"  D_c across N (20->80): {min(dcs):.3f} .. {max(dcs):.3f}  (relative spread {spread:.0%})")
        print(f"    -> threshold {'≈ N-independent' if spread < 0.25 else 'N-dependent'}"
              f"  (governed by coupling-vs-noise, not relic count).")
    print("  mass-independence: STRUCTURAL -- the V5 functional E=sum w(r)cos(dphi) has no mass term,")
    print("    so condensation cannot depend on relic mass (contrast: BEC needs a light boson).")
    print("=" * 78)


if __name__ == "__main__":
    main()
