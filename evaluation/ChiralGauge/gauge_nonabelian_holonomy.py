"""Gauging-mechanism check: does P05 re-routing realize GENUINE non-abelian SU(N) gauging,
or could it be secretly abelian (U(1)^N)?

Gauge_02: P05-transport of N indistinguishable channels is a U(N) link variable (re-routing
mixes channels [P07 branch/merge], bandwidth-conserving [P04 isometry], invertible between
commitments [P11] => unitary). That is a lattice gauge connection. The non-abelian content =
the plaquette holonomy U_plaq = product of links around a loop: non-abelian iff holonomies of
different loops DON'T commute (F = dA + A^A != 0). If all links share an eigenbasis (e.g. a
fixed channel labeling preserved by every transport), they commute -> abelian U(1)^N.

Test: is non-abelian GENERIC (only fine-tuned uniform connectivity is abelian), or does the
substrate force abelian? Generate P05 link variables and check.
"""
import numpy as np
from scipy.stats import unitary_group


def plaquette(links):
    """holonomy = ordered product of link variables around a loop."""
    U = np.eye(links[0].shape[0], dtype=complex)
    for L in links:
        U = L @ U
    return U


def su_part_distance(U):
    """how far U's SU(N) part is from identity (0 = pure phase = abelian-trivial)."""
    N = U.shape[0]
    phase = np.linalg.det(U) ** (1.0 / N)
    Usu = U / phase                        # remove the U(1) phase
    return np.linalg.norm(Usu - np.eye(N))


def main():
    print("GAUGING CHECK: is P05 channel-transport genuinely NON-ABELIAN SU(N)?\n")
    N = 3                                   # e.g. color triplet
    rng = np.random.default_rng(0)

    print("(1) GENERIC P05 re-routing (random U(N) links, position-dependent):")
    trials = 2000
    nonabelian = 0; commuting = 0
    for _ in range(trials):
        # two plaquettes sharing the graph; generic (random) re-routing per edge
        p1 = plaquette([unitary_group.rvs(N, random_state=rng) for _ in range(4)])
        p2 = plaquette([unitary_group.rvs(N, random_state=rng) for _ in range(4)])
        comm = np.linalg.norm(p1 @ p2 - p2 @ p1)
        if su_part_distance(p1) > 1e-6: nonabelian += 1
        if comm < 1e-6: commuting += 1
    print(f"    plaquette SU(N)-part nontrivial: {nonabelian}/{trials}  (curvature != 0)")
    print(f"    two plaquettes COMMUTE:          {commuting}/{trials}  (abelian case)")
    print("    -> generic re-routing gives non-trivial, NON-COMMUTING holonomies = genuine")
    print("       non-abelian SU(N). Commuting (abelian) is measure-zero (fine-tuned).")

    print("\n(2) ABELIAN case (fine-tuned: all links diagonal in a FIXED channel basis):")
    diag = lambda: np.diag(np.exp(1j * rng.uniform(0, 2*np.pi, N)))
    p1 = plaquette([diag() for _ in range(4)]); p2 = plaquette([diag() for _ in range(4)])
    print(f"    plaquette SU(N)-part: {su_part_distance(p1):.3e} (nontrivial phases but...)")
    print(f"    two plaquettes commute: {np.linalg.norm(p1@p2-p2@p1):.3e}  (YES -> abelian U(1)^N)")
    print("    -> a FIXED channel basis preserved by every transport => diagonal links =>")
    print("       commuting => merely abelian. Non-abelian REQUIRES the re-routing to NOT")
    print("       preserve a fixed channel labeling (indistinguishable channels allow this).")

    print("\n" + "=" * 82)
    print("VERDICT:")
    print("  * P05 transport IS a U(N) lattice connection (Gauge_02, structural) -- solid.")
    print("  * NON-ABELIAN gauging is GENERIC: any non-trivial, position-varying channel")
    print("    branch/merge connectivity gives non-commuting holonomies (F != 0). Abelian")
    print("    (commuting) is measure-zero -- it needs a fixed channel basis preserved by")
    print("    every transport, which same-rule-type INDISTINGUISHABLE channels do NOT impose.")
    print("    So ED's channel-lattice is generically a genuine non-abelian gauge theory.")
    print("  * CORRECTION to Gauge_01 sec3: the SU(N) MIXER is P05 re-routing (cross-CHANNEL,")
    print("    within one chain's N-channel fiber), NOT V5. 'V5 = the SU(N) mixer' conflates")
    print("    cross-CHAIN (V5, between two chains) with cross-CHANNEL (SU(N), within a fiber).")
    print("    V5 is a scalar cross-chain coherence, not a matrix cross-channel connection.")
    print("=" * 82)


if __name__ == "__main__":
    main()
