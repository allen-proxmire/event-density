"""V5 characterization via the RELATIONAL synchronization test (AP-directed,
2026-07-06). Reframed target, per AP's insight: ED rejects a universal tick
(that's WHY it has time dilation), so the question is NOT "do all chains pulse
together" (that would be a universal clock -- physically wrong) but the
relational one:

    does V5's FINITE cross-chain reach synchronize NEARBY (bound) chains into a
    shared commitment rate -- a local proper time / rest frame, the basis of a
    composite object -- while leaving DISTANT chains free (no universal tick,
    time dilation preserved)?

V5's defining feature is finite reach (finite cross-chain memory ell_V5), and
finite reach is EXACTLY the ingredient that gives local-binding-without-a-
universal-clock. This probe tests that directly.

HONEST SCOPE (stated up front, not buried):
- This is a MODEL of V5's known structural features -- finite-reach, phase-
  carrying coupling (Paper_090: K_V5 decays over ell_V5, and carries the
  gauge-covariant relative phase e^{i(alpha_A - alpha_B)}) -- NOT the certified
  V5 (which has never been implemented in code; that's the open keystone). It
  abstracts each chain to a commitment-phase oscillator, one level up from raw
  commitment dynamics.
- The SIGN of the phase coupling (synchronizing sin(dphi), the Kuramoto form)
  is motivated by the gauge-phase structure but is NOT derived from the corpus;
  the corpus does not pin V5's coupling sign. So this characterizes "what V5's
  known structure would produce IF its phase coupling is attractive," and
  establishes what V5 must look like to produce the physically-required
  behavior -- reverse-characterization, complementary to the (failed) forward
  "what does V5 force" attempts.
- V5 is retarded; this minimal model uses instantaneous phase coupling (the
  retardation sets a delay, secondary to the reach question). Flagged.

WHAT IS BEING MEASURED. Two spatially-separated clusters of chains (a NEAR
cluster and a FAR cluster, separation D), each chain a phase oscillator with
its own natural rate (spread -> they drift without coupling). Coupling: finite-
reach phase coupling, dphi_i/dt = w_i + K * sum_j exp(-|x_i-x_j|/ell) sin(phi_j
- phi_i). Sweep the reach ell_V5. Measure WITHIN-cluster synchronization
(local) vs BETWEEN-cluster (global), and whether cross-cluster rate differences
survive (time dilation preserved).

Physically-required signature (if V5 does its job): a window of ell_V5 where
within-cluster sync is HIGH but between-cluster sync is LOW -- local proper time
without a universal tick. And ell_V5 >> D should (wrongly) force global sync =
the universal-clock regime, showing that V5's finiteness is load-bearing.
"""
import numpy as np


def simulate(positions, cluster_of, omega, ell, K, steps=4000, dt=0.05, seed=0):
    """Finite-reach Kuramoto: phase oscillators at fixed positions, coupled with
    strength decaying as exp(-distance/ell). Returns time-averaged order
    parameters (within each cluster and between clusters) over the last half."""
    rng = np.random.default_rng(seed)
    n = len(positions)
    phi = rng.uniform(0, 2 * np.pi, n)
    # distance-decaying coupling matrix (no self-coupling)
    d = np.abs(positions[:, None] - positions[None, :])
    W = np.exp(-d / ell)
    np.fill_diagonal(W, 0.0)

    clusters = np.unique(cluster_of)
    within_hist, between_hist, rate_gap_hist = [], [], []
    phi_prev = phi.copy()
    for t in range(steps):
        # coupling term: sum_j W_ij sin(phi_j - phi_i)
        dphi = np.array([omega[i] + K * np.sum(W[i] * np.sin(phi - phi[i])) for i in range(n)])
        phi = phi + dt * dphi
        if t > steps // 2:
            # within-cluster order parameter (mean over clusters)
            wr = []
            for c in clusters:
                m = cluster_of == c
                wr.append(np.abs(np.mean(np.exp(1j * phi[m]))))
            within_hist.append(np.mean(wr))
            # between-cluster: order parameter of cluster-mean phases
            cmeans = [np.angle(np.mean(np.exp(1j * phi[cluster_of == c]))) for c in clusters]
            between_hist.append(np.abs(np.mean(np.exp(1j * np.array(cmeans)))))
            # effective rate gap between the two clusters (time-dilation proxy)
            rates = (phi - phi_prev) / dt
            rate_gap_hist.append(abs(rates[cluster_of == clusters[0]].mean()
                                     - rates[cluster_of == clusters[1]].mean()))
        phi_prev = phi.copy()
    return np.mean(within_hist), np.mean(between_hist), np.mean(rate_gap_hist)


def main():
    print("=" * 92)
    print("V5 SYNCHRONIZATION CHARACTERIZATION -- does finite cross-chain reach give LOCAL")
    print("binding (shared proper time) WITHOUT a universal tick (global sync)?")
    print("=" * 92)

    # Two clusters of 5 chains each: NEAR cluster around x=0, FAR cluster around x=50.
    D = 50.0
    near = np.array([-2., -1., 0., 1., 2.])
    far = near + D
    positions = np.concatenate([near, far])
    cluster_of = np.array([0] * 5 + [1] * 5)
    # Natural rates: a spread within each cluster, and the FAR cluster runs at a
    # DIFFERENT mean rate (a stand-in for two frames in relative motion / different
    # gravitational potential -> time dilation). If V5 wrongly globally-syncs, this
    # rate gap collapses (universal tick). If V5 keeps them local, the gap survives.
    rng = np.random.default_rng(0)
    omega = np.concatenate([1.0 + 0.1 * rng.standard_normal(5),      # near cluster ~ rate 1.0
                            1.4 + 0.1 * rng.standard_normal(5)])     # far cluster ~ rate 1.4
    K = 0.8

    print(f"\nTwo clusters of 5 chains, separation D={D:.0f}. Near cluster mean rate ~1.0,")
    print(f"far cluster mean rate ~1.4 (a time-dilation stand-in). Coupling K={K}.")
    print(f"\n{'ell_V5':>8}{'within-sync':>13}{'between-sync':>14}{'rate-gap':>11}  regime")
    print("-" * 92)

    # Baseline: no coupling
    w0, b0, g0 = simulate(positions, cluster_of, omega, ell=1.0, K=0.0, seed=1)
    print(f"{'K=0':>8}{w0:>13.3f}{b0:>14.3f}{g0:>11.3f}  (no coupling: drift, rate gap = natural)")

    for ell in (0.5, 2.0, 5.0, 15.0, 50.0, 200.0):
        ws, bs, gs = [], [], []
        for s in range(4):
            w, b, g = simulate(positions, cluster_of, omega, ell=ell, K=K, seed=10 + s)
            ws.append(w); bs.append(b); gs.append(g)
        w, b, g = np.mean(ws), np.mean(bs), np.mean(gs)
        if w > 0.8 and b < 0.5:
            regime = "LOCAL binding, NO universal tick  <-- physically required"
        elif w > 0.8 and b > 0.8:
            regime = "GLOBAL sync = universal tick (wrong for unbound clusters)"
        elif w < 0.5:
            regime = "reach too short: even local binding fails"
        else:
            regime = "partial"
        print(f"{ell:>8.1f}{w:>13.3f}{b:>14.3f}{g:>11.3f}  {regime}")

    print("\n" + "=" * 92)
    print("READING:")
    print("  A window of ell_V5 with within-sync HIGH + between-sync LOW = V5's finite reach")
    print("  produces LOCAL proper time (bound chains share a rate) WITHOUT a universal tick")
    print("  (distant chains stay free; the cluster rate-gap survives = time dilation preserved).")
    print("  ell_V5 >> D forcing between-sync high AND collapsing the rate-gap = the universal-")
    print("  clock regime, which would be WRONG -- showing V5's FINITENESS is load-bearing for")
    print("  reproducing time dilation. This characterizes V5's relational role: a finite-reach")
    print("  binder of local proper time, NOT a universal clock.")
    print("=" * 92)


if __name__ == "__main__":
    main()
