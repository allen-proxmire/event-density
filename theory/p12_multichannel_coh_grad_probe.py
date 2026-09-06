"""Multi-channel probe: do Coh and Grad actually differ, and does it matter?

Note_GradPhase_Decomposed_2026-09-06 killed the xi discriminator and diagnosed
why every probe so far drew: the single-phase-per-node design collapses Coh's
index set onto Grad's.  It named the fix -- multiple channels per locus.

Writing both terms out per channel K, with v's own contribution included and
neighbours transported by the P05 connection, the difference is exact and it is
NOT the channel count:

    Coh(v)  = sum_K [ |P_K(v) + sum_w P_K(w) e^{iA}|^2 - (b_K(v) + sum_w b_K(w)) ]
            = 2 sum_K [ sum_w sqrt(b_v b_w) cos(dpi_vw)          <-- v-neighbour
                      + sum_{w<w'} sqrt(b_w b_w') cos(dpi_ww') ] <-- NEIGHBOUR-NEIGHBOUR

   -Grad(v) = -sum_K sum_w |P_K(v) - P_K(w) e^{iA}|^2
            = 2 sum_K sum_w sqrt(b_v b_w) cos(dpi_vw) - (const in v's phase)
                                                          <-- v-neighbour ONLY

    ==>  Coh = -Grad + 2 * NN + const,   NN = the neighbour-neighbour coherence

So the two terms differ by EXACTLY ONE OBJECT: the neighbour-neighbour cross
term.  Grad has none -- a Dirichlet form only ever compares v to a neighbour,
never two neighbours to each other.  Coh has it, because it interferes every
pair of contributions.

That is the degree of freedom the old probe lacked, and it is why |acc| (which
silently contains both) could not tell them apart.

This probe computes Coh, Grad and NN separately and asks:
  (1) do the two readings give different order/reach?
  (2) how large is NN relative to the shared v-neighbour part?
  (3) does the (A)-condition crystallization under Grad survive?

Run: python p12_multichannel_coh_grad_probe.py
"""
import cmath
import math
import sys

import numpy as np

SIM = r"C:/Users/allen/GitHub/event-density/evaluation/Bits"
THEORY = r"C:/Users/allen/GitHub/event-density/theory"
sys.path.insert(0, SIM)
sys.path.insert(0, THEORY)

from simulator import (NodeState, StateVector, SigmaCoeffs,
                       compute_sigma, compute_candidates, apply_tiebreak)
import p12_phase_in_grad_probe as P

NCH = 3          # channels per locus
NPHI = 24        # phase grid for the deposition maximisation


def run(L, bw_disorder, kappa_bw, kappa_rho, k_phase, rng, mode,
        max_commits_factor=6):
    """mode in {'coh','grad'}.  Returns per-channel phase arrays + committed."""
    g, coords, nid = P.build_grid(L, bw_disorder, rng)
    N = L * L
    state = StateVector({i: NodeState() for i in range(N)})
    coeffs = SigmaCoeffs()

    # per-node, per-channel bandwidth (quenched) and phase (deposited)
    bch = 1.0 + bw_disorder * (2 * rng.random((N, NCH)) - 1.0)
    phase = np.full((N, NCH), np.nan)
    committed = np.zeros(N, dtype=bool)

    def nbr_data(v):
        """committed neighbours: list of (b_K array, transported phase array)."""
        out = []
        for w in g.neighbors(v):
            if committed[w]:
                A = kappa_bw * (g.bw(w, v) - 1.0) + kappa_rho * (state[w].rho - state[v].rho)
                out.append((bch[w], phase[w] + A))
        return out

    def parts(v, phi_v):
        """(v-neighbour term, neighbour-neighbour term) for candidate phases phi_v."""
        nd = nbr_data(v)
        if not nd:
            return 0.0, 0.0
        vn = 0.0
        for bw_, pw in nd:
            vn += float(np.sum(np.sqrt(bch[v] * bw_) * np.cos(phi_v - pw)))
        nn = 0.0
        for i in range(len(nd)):
            for j in range(i + 1, len(nd)):
                b1, p1 = nd[i]
                b2, p2 = nd[j]
                nn += float(np.sum(np.sqrt(b1 * b2) * np.cos(p1 - p2)))
        return vn, nn

    def bonus(v, phi_v):
        vn, nn = parts(v, phi_v)
        # Coh keeps the neighbour-neighbour term; Grad does not.
        return 2.0 * (vn + nn) if mode == "coh" else 2.0 * vn

    def best_phase(v):
        """deposit the phases maximising the active bonus (mean-field angle)."""
        nd = nbr_data(v)
        if not nd:
            return rng.uniform(0, 2 * math.pi, size=NCH)
        acc = np.zeros(NCH, dtype=complex)
        for bw_, pw in nd:
            acc += np.sqrt(bw_) * np.exp(1j * pw)
        out = np.angle(acc)
        out[np.abs(acc) < 1e-12] = rng.uniform(0, 2 * math.pi, size=int((np.abs(acc) < 1e-12).sum()))
        return out % (2 * math.pi)

    def deposit(v):
        phase[v] = best_phase(v)
        committed[v] = True

    s = int(rng.choice(N))
    state[s].commit(coeffs.increment)
    state[s].active = True
    deposit(s)
    active = {s}

    max_commits = max_commits_factor * N
    commits = 0
    nn_share = []
    while active and commits < max_commits and committed.sum() < N:
        order = sorted(active)
        active = set()
        for u in order:
            if not state[u].active:
                continue
            cands = compute_candidates(u, state, g)
            if not cands:
                state[u].active = False
                continue
            base = {v: compute_sigma(u, v, state, g, coeffs) for v in cands}
            if k_phase:
                tot = {}
                for v in cands:
                    phi = best_phase(v)
                    vn, nn = parts(v, phi)
                    if abs(vn) > 1e-9:
                        nn_share.append(abs(nn) / (abs(vn) + abs(nn)))
                    tot[v] = base[v] + k_phase * (2.0 * (vn + nn) if mode == "coh" else 2.0 * vn)
            else:
                tot = base
            tmax = max(tot.values())
            winner = apply_tiebreak(u, [v for v, sc in tot.items() if sc == tmax], g)
            first = not committed[winner]
            state[winner].commit(coeffs.increment)
            if first:
                deposit(winner)
            state[u].active = False
            state[winner].active = True
            active.add(winner)
            commits += 1
    return phase, committed, coords, (float(np.mean(nn_share)) if nn_share else 0.0)


def measure(L, bwd, kbw, krho, kp, seed, mode):
    fresh = lambda: np.random.default_rng(seed)
    ph, c, co, nnshare = run(L, bwd, kbw, krho, kp, fresh(), mode)
    Rs, xis = [], []
    for k in range(NCH):
        pk = ph[:, k]
        Rs.append(P.global_order(pk, c))
        xis.append(P.xi_estimate(P.corr_vs_r(pk, c, co, fresh())))
    return float(np.mean(Rs)), float(np.mean(xis)), nnshare


def main():
    L, seed = 40, 11
    print("Multi-channel Coh/Grad probe. %dx%d, %d channels per locus, single seed."
          % (L, L, NCH))
    print("Coh = -Grad + 2*NN + const;  NN = the neighbour-neighbour cross term,")
    print("which a Dirichlet form structurally cannot have.\n")

    conds = [
        ("CONTROL homogeneous (kappa=0)", 0.0, 0.0, 0.0),
        ("(A) bandwidth holonomy only", 0.5, 0.5, 0.0),
        ("(C) physical: bw + rho holonomy", 0.5, 0.5, 0.5),
    ]
    for name, bwd, kbw, krho in conds:
        print("#" * 74)
        print("### " + name)
        print("  %-14s %-26s %-26s" % ("", "Coh  (keeps NN)", "Grad (no NN)"))
        print("  %-14s %-26s %-26s %s" % ("", "R      xi", "R      xi", "NN share"))
        for kp in [1.0, 4.0, 8.0]:
            rc, xc, nns = measure(L, bwd, kbw, krho, kp, seed, "coh")
            rg, xg, _ = measure(L, bwd, kbw, krho, kp, seed, "grad")
            vc = "CRYSTAL" if (rc > 0.8 and xc > 15) else "finite"
            vg = "CRYSTAL" if (rg > 0.8 and xg > 15) else "finite"
            print("  k_phase=%-6.1f %5.3f %6.1f  %-8s %5.3f %6.1f  %-8s   %.2f"
                  % (kp, rc, xc, vc, rg, xg, vg, nns))
        print()

    print("""READING

  The whole question is whether the NEIGHBOUR-NEIGHBOUR term matters.  It is
  the one object Coh has and Grad structurally cannot: a Dirichlet form only
  ever compares v to a neighbour, never two neighbours to each other.

  "NN share" is |NN| / (|v-neighbour| + |NN|), i.e. how much of the phase
  score the neighbour-neighbour term carries.  If that is near zero the two
  readings are numerically the same object however they are written, and no
  probe will ever separate them.  If it is appreciable and the verdicts still
  agree, they differ in size but not in behaviour -- which is a real result
  and a different one.
""")


if __name__ == "__main__":
    main()
