"""Is condition (A)'s crystallization robust, or one growth history?

Everything in gravity ledger #103-#105 rests on a single seed.  #105 found that
with the Coh arm written canonically, condition (A) -- bandwidth holonomy only
-- crystallizes under BOTH canonical terms, and re-attributed that from "Grad's
known problem" to "a property of the phase-coherence operationalization".

That re-attribution is only worth as much as the single seed it came from.
This run sweeps 10 seeds.  Each seed re-draws the quenched bandwidth disorder,
the start node and the deposition randomness, so the seeds are independent
disorder realizations and not just different growth orders on one lattice.

The control that matters is k_phase = 0: no phase feedback at all.  Phases are
still deposited, but they do not influence which candidate wins, so any order
measured there is the deposit rule plus the lattice, not the phase term.  If
(A) already crystallizes at k_phase = 0, the crystallization is not about the
phase term at all -- and #105's re-attribution would itself need re-attributing.

Run: python p12_condA_multiseed.py
"""
import sys

import numpy as np

THEORY = r"C:/Users/allen/GitHub/event-density/theory"
sys.path.insert(0, THEORY)

import p12_coh_canonical_probe as Q
import p12_phase_in_grad_probe as P

L = 64
SEEDS = list(range(11, 21))

# CRYSTAL IS THE FAILURE MODE, not the target.  "Knots, Not Crystals" is the
# companion result: the certified substrate has NO long-range ordering
# coupling.  Total disorder is also a failure -- V5 has to bind chains into
# local clocks.  The target is the middle: FINITE REACH, xi finite and nonzero.
CONDITIONS = {
    "A": (0.5, 0.5, 0.0),      # bandwidth holonomy only  -- the partial case
    "C": (0.5, 0.5, 0.5),      # bw + rho holonomy        -- THE PHYSICAL CASE
}
COND = sys.argv[1].upper() if len(sys.argv) > 1 else "A"
BWD, KBW, KRHO = CONDITIONS[COND]


def one(seed, kp, mode):
    fresh = lambda: np.random.default_rng(seed)
    ph, c, co = Q.run_fill(L, BWD, KBW, KRHO, kp, fresh(), mode=mode)
    R = P.global_order(ph, c)
    xi = P.xi_estimate(P.corr_vs_r(ph, c, co, fresh()))
    return R, xi


def is_crystal(R, xi):
    return R > 0.8 and xi > 15


def block(label, results):
    Rs = np.array([r for r, _ in results])
    xis = np.array([x for _, x in results])
    ncry = sum(is_crystal(r, x) for r, x in results)
    print("  %-26s R: %.2f [%.2f, %.2f]   xi: %4.1f [%4.1f, %4.1f]   CRYSTAL %d/%d"
          % (label, Rs.mean(), Rs.min(), Rs.max(),
             xis.mean(), xis.min(), xis.max(), ncry, len(results)))
    return ncry


def main():
    print("Condition (%s) multi-seed: %d seeds, %dx%d.  CRYSTAL = FAILURE (Knots, Not Crystals);" % (COND, len(SEEDS), L, L))
    print("total disorder is also failure. The target is FINITE REACH.")
    print("Each seed re-draws the quenched disorder, start node and deposition noise.\n")

    print("CONTROL -- k_phase = 0, no phase feedback (all arms identical):")
    ctrl = [one(s, 0.0, "coh") for s in SEEDS]
    n_ctrl = block("no phase term", ctrl)
    print()

    summary = {}
    for kp in (1.0, 8.0):
        print("k_phase = %.1f:" % kp)
        for mode, label in (("grad", "Grad  |acc|"),
                            ("coh_v3", "old 'Coh'  |acc|/n"),
                            ("coh", "CANONICAL Coh")):
            res = [one(s, kp, mode) for s in SEEDS]
            summary[(kp, mode)] = block(label, res)
        print()

    print("=" * 78)
    print("READING\n")
    print("  control (no phase term)            : CRYSTAL in %d/%d seeds" % (n_ctrl, len(SEEDS)))
    for kp in (1.0, 8.0):
        print("  k_phase=%.1f  Grad / old-Coh / Coh   : %d / %d / %d  of %d"
              % (kp, summary[(kp, "grad")], summary[(kp, "coh_v3")],
                 summary[(kp, "coh")], len(SEEDS)))
    # Fisher exact on the k_phase=1 Grad-vs-Coh split, one-tailed:
    # the direction was PREDICTED (NN is an extra alignment reward, so Coh
    # should order at weaker coupling), so a one-tailed test is the right one.
    from math import comb
    a, b = summary[(1.0, "grad")], summary[(1.0, "coh")]
    n = len(SEEDS)
    tot = comb(2 * n, a + b)
    p1 = sum(comb(n, k) * comb(n, a + b - k) / tot for k in range(0, a + 1)
             if 0 <= a + b - k <= n)
    print("\n  Fisher exact, k_phase=1, Grad %d/%d vs Coh %d/%d : one-tailed p = %.4f"
          % (a, n, b, n, p1))
    print("""
  If the CONTROL already crystallizes in most seeds, condition (A)'s
  crystallization is a property of the lattice and the deposit rule, not of
  the phase-coherence term -- and #105's re-attribution ("a property of the
  operationalization") is still too generous: there would be nothing to
  attribute.

  If the control stays disordered and the phase arms crystallize, the
  single-seed finding holds up and (A)-crystallization is real.

  The old-'Coh' column is the |acc|/n arm, kept because it is the one that
  stayed finite-reach on the single seed.  Whether that survives ten seeds is
  a check on #104's diagnosis as much as on anything else.
""")


if __name__ == "__main__":
    main()
