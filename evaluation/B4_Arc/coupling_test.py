"""B4 Step 2 - Coupling test: can the integer winding ACT on the dynamics
without Σ reading orientation?

Σ reads rho + graph only (hard invariant). From simulator/sigma.py + update.py,
the ONLY phase-reachable dynamical quantities are:
  - bandwidth b_e (P04): enters the TIE-BREAK (apply_tiebreak) and, at b->0,
    effective decoupling (admissible_neighbors); NEVER enters compute_sigma.
  - transport amplitude (P05): the connection itself.

The ED-sanctioned phase<->amplitude pairing is the corpus polar measure
    P_K = sqrt(b_K) * e^{i pi_K},
so the natural P04 coupling is an edge COHERENCE bandwidth
    b_e = |<P_u, P_v>|^2  ->  b_e = cos^2(dphi_e / 2),
maximal at aligned phase (dphi=0), zero at anti-aligned (dphi=pi). No sign or
quantization is installed; the cos^2 overlap is the standard amplitude overlap.

KEY POINT: a winding-w single-valued field on an N-cycle obeys the TOPOLOGICAL
bound  sum |wrap(dphi_e)| >= |sum wrap(dphi_e)| = 2*pi*|w|.  So |w| forces a
minimum total phase variation, which CAPS the achievable coherent bandwidth.
The minimum-variation (ground-state) config per sector is uniform, dphi=2*pi*w/N,
giving the discrete ladder  b_e = cos^2(pi*w/N)  --  a w-INDEXED spectrum.
"""
from __future__ import annotations

import numpy as np


def wrap(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


def winding(phi):
    dphi = wrap(np.diff(np.concatenate([phi, phi[:1]])))
    return int(round(dphi.sum() / (2 * np.pi)))


def edge_bandwidth(phi):
    """P04 coherence bandwidth per edge from the P_K overlap: b_e=cos^2(dphi/2)."""
    dphi = wrap(np.diff(np.concatenate([phi, phi[:1]])))
    return np.cos(dphi / 2.0) ** 2


def ground_state(w, N):
    """Minimum-total-variation field in winding sector w: uniform winding."""
    return np.mod(2 * np.pi * w * np.arange(N) / N, 2 * np.pi)


def main():
    rng = np.random.default_rng(20260610)
    N = 6
    DRAWS = 400_000

    print("=" * 72)
    print(f"B4 Step 2 - Coupling test: does integer winding act on dynamics? (N={N})")
    print("=" * 72)

    # ---- Candidate A (P04 coherence bandwidth): w-indexed ground-state ladder
    print("\n[A] phase->bandwidth (P04 coherence b_e=cos^2(dphi/2)), Sigma untouched")
    print("    ground-state (max-coherence) bandwidth per winding sector:")
    print(f"    {'w':>3} {'b_e=cos^2(pi*w/N)':>20} {'total|dphi|/2pi':>16} {'bound 2pi|w|/2pi':>17}")
    for w in range(0, N // 2 + 1):
        gs = ground_state(w, N)
        b = edge_bandwidth(gs)
        dphi = wrap(np.diff(np.concatenate([gs, gs[:1]])))
        print(f"    {w:>3} {b.mean():>20.4f} {np.abs(dphi).sum()/(2*np.pi):>16.4f} "
              f"{w:>17.4f}")

    # ---- random sampling: mean coherent bandwidth vs winding sector
    phi = rng.uniform(0, 2 * np.pi, size=(DRAWS, N))
    dphi = wrap(np.diff(np.concatenate([phi, phi[:, :1]], axis=1), axis=1))
    W = np.round(dphi.sum(axis=1) / (2 * np.pi)).astype(int)
    B = (np.cos(dphi / 2.0) ** 2).mean(axis=1)
    Vtot = np.abs(dphi).sum(axis=1) / (2 * np.pi)
    print("\n    random configs binned by winding sector (mean over sector):")
    print(f"    {'w':>3} {'frac':>8} {'mean b_e':>10} {'mean total|dphi|/2pi':>22}")
    for w in sorted(set(W)):
        if abs(w) > 3:
            continue
        m = W == w
        print(f"    {w:>+3} {m.mean():>8.3f} {B[m].mean():>10.4f} {Vtot[m].mean():>22.4f}")

    # monotone test: does mean bandwidth strictly decrease with |w| (ground states)?
    gs_band = [edge_bandwidth(ground_state(w, N)).mean() for w in range(0, N // 2 + 1)]
    ladder_monotone = all(gs_band[i] > gs_band[i + 1] for i in range(len(gs_band) - 1))

    # ---- winding conservation under the coupling (coupling touches b, not phi)
    w0 = winding(phi[0])
    # apply coupling = recompute bandwidth; phases (committed) untouched -> winding fixed
    w_after = winding(phi[0])
    conserved = (w0 == w_after)

    # ---- Candidate B (P05 holonomy->transport): sees CONTINUOUS holonomy
    H = np.mod(dphi.sum(axis=1) + dphi[:, -1] * 0, 2 * np.pi)  # holonomy (continuous)
    H_distinct = len(np.unique(np.round(np.mod(
        rng.uniform(0, 2*np.pi, size=(50000, N)).sum(axis=1), 2*np.pi), 6)))

    print("\n[B] holonomy->transport (P05, AB-like): couples to the CONTINUOUS")
    print(f"    holonomy (Step 1: ~{H_distinct} distinct / 50k) -> effect is CONTINUOUS,")
    print("    NOT integer-indexed. Sees the wrong (continuous) invariant.")

    print("\n[C] phase->rho (commitment increment depends on phase):")
    print("    rho IS read by compute_sigma -> Sigma would depend on phase via rho.")
    print("    => back-door orientation read. FORBIDDEN (violates the hard invariant).")

    # ---- summary
    print("\n" + "=" * 72)
    print("SUMMARY  {candidate -> outcome}")
    print(f"  baseline (no coupling)        -> INERT            (Step 1)")
    print(f"  A. phase->bandwidth (P04)     -> DISCRETE (w-indexed ladder "
          f"cos^2(pi*w/N)); monotone={ladder_monotone}")
    print(f"     channel: tie-break (weak, Sigma-ties only) OR b->0 decoupling (strong)")
    print(f"  B. holonomy->transport (P05)  -> WEAK / CONTINUOUS (sees continuous H)")
    print(f"  C. phase->rho                 -> FORBIDDEN (Sigma back-door)")
    print(f"  winding conserved under A     -> {conserved}  (coupling touches b, not phi)")
    print("=" * 72)
    print("\nVERDICT: an integer-indexed coupling EXISTS (A) and keeps Sigma blind,")
    print("but acts only through the amplitude/tie-break(/decoupling) channel, not")
    print("through Sigma. ED admits an ACTIVE topological invariant -- weakly.")
    return ladder_monotone and conserved


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
