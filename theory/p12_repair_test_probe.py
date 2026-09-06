"""Test the repair: canonical Coh entered into candidate selection NORMALISED.

Ledger #110 established two effects and told them apart:

  effect 1  CONNECTION -- reach falls ~4.7 lattice units per unit of transport
            connection |A|.  The canonical terms triple |A| and pay for it.
  effect 2  ALIGNMENT  -- +81% reach at matched connection, measured on the
            |acc|/n arm.  The phase term DOES bind.

and identified the mechanism: |acc| and canonical Coh reward agreement TIMES
QUANTITY, and the quantity part chases cells with many committed neighbours,
which sit in high-rho pockets where |A| is large.  |acc|/n rewards agreement
QUALITY only, so it does not chase them.

THE REPAIR, proposed there and tested here: enter the canonical term into
candidate selection in NORMALISED form.

    canonical Coh      bonus = |acc| + (|acc|^2 - n)/2
    normalised Coh     bonus = [ |acc| + (|acc|^2 - n)/2 ] / n     <-- REPAIR

This is a SCORING CONVENTION -- how the term enters the selection rule -- and
not a change to Coh as a functional.  Everything the corpus has settled about
Coh is untouched by it.

WHAT WOULD COUNT AS SUCCESS.  Normalised Coh should show:
    (a) flat mean|A| across a k sweep, like |acc|/n and unlike canonical Coh
    (b) xi well above the no-phase control
If both, claim 2 is closed with the actual canonical term.  If (a) holds but
(b) does not, the /n's benefit is tied to that specific functional and the
paper's binding claim is back in question.

Run: python p12_repair_test_probe.py
"""
import sys

import numpy as np

THEORY = r"C:/Users/allen/GitHub/event-density/theory"
sys.path.insert(0, THEORY)

import p12_faithful_replay_probe as F
import p12_phase_in_grad_probe as P

F.L = 48
SEEDS = [11, 12, 13]
KS = [1.0, 2.0, 4.0, 8.0]

# effect-1 fit from ledger #110, same grid and seeds
FIT_A, FIT_B = 4.786, -4.684


def point(seed, kp, mode):
    ph, c, co, rec, coordn = F.live(seed, kp, mode)
    xi = P.xi_estimate(P.corr_vs_r(ph, c, co, np.random.default_rng(seed)))
    _, mn = F.a_spread(rec)
    return xi, mn


def sweep(mode, label, ks=KS):
    out = []
    for kp in ks:
        res = [point(s, kp, mode) for s in SEEDS]
        xi = float(np.mean([r[0] for r in res]))
        mA = float(np.mean([r[1] for r in res]))
        out.append((kp, mA, xi))
        print("  %-24s %6.1f %10.3f %9.2f %+11.2f"
              % (label, kp, mA, xi, xi - (FIT_A + FIT_B * mA)))
    return out


def main():
    print("Repair test. Condition (C), %dx%d, %d seeds." % (F.L, F.L, len(SEEDS)))
    print("Normalised canonical Coh: bonus = [|acc| + (|acc|^2 - n)/2] / n\n")
    print("  %-24s %6s %10s %9s %11s" % ("arm", "k", "mean|A|", "xi", "vs effect-1"))

    ctrl = [point(s, 0.0, "coh") for s in SEEDS]
    a0 = float(np.mean([r[1] for r in ctrl]))
    x0 = float(np.mean([r[0] for r in ctrl]))
    print("  %-24s %6.1f %10.3f %9.2f %+11.2f"
          % ("control (no phase)", 0.0, a0, x0, x0 - (FIT_A + FIT_B * a0)))

    ref = sweep("coh_v3", "|acc|/n  (reference)")
    canon = sweep("coh", "canonical Coh")
    rep0 = sweep("coh_norm", "Coh/n (naive)")
    rep = sweep("coh_int", "INTENSIVE Coh  <==")

    print("""
READING -- the two success criteria
""")
    def flatness(rows):
        As = [r[1] for r in rows]
        return max(As) - min(As)

    print("  (a) connection flat across the k sweep -- spread of mean|A|:")
    print("      |acc|/n reference    %.3f" % flatness(ref))
    print("      canonical Coh        %.3f" % flatness(canon))
    print("      Coh/n naive          %.3f" % flatness(rep0))
    print("      INTENSIVE Coh        %.3f" % flatness(rep))
    print("      control |A| = %.3f" % a0)

    print("\n  (b) reach against the no-phase control (xi = %.2f):" % x0)
    for label, rows in (("|acc|/n reference", ref), ("canonical Coh", canon),
                        ("Coh/n naive", rep0), ("INTENSIVE Coh", rep)):
        xs = [r[2] for r in rows]
        print("      %-20s xi %.2f - %.2f   (control %.2f)"
              % (label, min(xs), max(xs), x0))

    best = max(r[2] for r in rep)
    print("""
  VERDICT""")
    flat = flatness(rep) < 2 * flatness(ref)
    binds = best > x0
    if flat and binds:
        print("""  Normalised canonical Coh keeps its connection flat AND reaches past the
  control.  The repair works with the actual canonical term: claim 2 closes,
  and the fix is a scoring convention rather than a change to the functional.""")
    elif flat:
        print("""  Normalised canonical Coh keeps its connection flat but does NOT reach past
  the control.  So the /n removes the growth-side cost without delivering the
  binding -- the benefit measured on |acc|/n is tied to that functional, and
  the paper's binding claim is back in question.""")
    else:
        print("""  Normalisation did NOT flatten the connection.  The chasing is not purely
  the coordination factor, and the diagnosis in #110 is incomplete.""")


if __name__ == "__main__":
    main()
