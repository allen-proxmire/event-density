"""Quantify effect 2: alignment gain at matched connection.

Ledger #109 found two effects in the phase term and identified only one:

  (1) CONNECTION effect -- the canonical terms steer the front into territory
      with 2-3x the transport connection |A|, and a wide connection scrambles
      whatever passes through it.  Identified.

  (2) ALIGNMENT effect -- old-"Coh" (|acc|/n) reaches xi = 3.83 against the
      control's 2.13 at essentially IDENTICAL connection (0.364 vs 0.362).
      Same transport, nearly double the reach.  Unquantified.

Effect 2 is the binding the paper was written to establish.  If it is real and
separable, claim 2 is fixable -- the phase term does bind, and the problem is
only that the extensive forms drag the growth front somewhere bad.  If it is
not, claim 2 is fatal.

METHOD.  Sweep k_phase on every arm and record (mean|A|, xi) together.  Then
regress xi on mean|A| across ALL points: the fit is effect 1, and each arm's
RESIDUAL from that fit is effect 2 -- reach it gains or loses that the
connection does not account for.

Grid is 48 here rather than 64 to afford the sweep; the control is re-run at
the same size so every number below is internally comparable.

Run: python p12_effect2_probe.py
"""
import sys

import numpy as np

THEORY = r"C:/Users/allen/GitHub/event-density/theory"
sys.path.insert(0, THEORY)

import p12_faithful_replay_probe as F
import p12_phase_in_grad_probe as P

F.L = 48                                  # smaller grid; control re-run to match
SEEDS = [11, 12, 13]
KS = [1.0, 2.0, 4.0, 8.0]


def point(seed, kp, mode):
    ph, c, co, rec, coordn = F.live(seed, kp, mode)
    xi = P.xi_estimate(P.corr_vs_r(ph, c, co, np.random.default_rng(seed)))
    sd, mn = F.a_spread(rec)
    return xi, mn, coordn


def main():
    print("Effect-2 probe. Condition (C), %dx%d, %d seeds." % (F.L, F.L, len(SEEDS)))
    print("Sweeping k_phase and tracking (mean|A|, xi) together.\n")

    rows = []          # (label, arm, k, xi, meanA)

    ctrl = [point(s, 0.0, "coh") for s in SEEDS]
    xi0 = float(np.mean([r[0] for r in ctrl]))
    a0 = float(np.mean([r[1] for r in ctrl]))
    rows.append(("control k=0", "control", 0.0, xi0, a0))
    print("  %-22s %7s %9s %9s" % ("arm", "k", "mean|A|", "xi"))
    print("  %-22s %7.1f %9.3f %9.2f" % ("control", 0.0, a0, xi0))

    for mode, label in (("coh_v3", "old-Coh |acc|/n"),
                        ("grad", "Grad    |acc|"),
                        ("coh", "CANON   Coh")):
        for kp in KS:
            res = [point(s, kp, mode) for s in SEEDS]
            xi = float(np.mean([r[0] for r in res]))
            mA = float(np.mean([r[1] for r in res]))
            rows.append((label, mode, kp, xi, mA))
            print("  %-22s %7.1f %9.3f %9.2f" % (label, kp, mA, xi))

    # ---- effect 1: regress xi on mean|A| across every point ----------------
    A = np.array([r[4] for r in rows])
    X = np.array([r[3] for r in rows])
    b, a = np.polyfit(A, X, 1)
    pred = a + b * A
    resid = X - pred
    r = float(np.corrcoef(A, X)[0, 1])

    print("""
EFFECT 1 -- the connection, fitted across every point
""")
    print("  xi = %.3f + (%.3f) * mean|A|      r = %.3f  (n = %d)" % (a, b, r, len(rows)))
    print("  Reach falls by %.2f lattice units per unit of connection." % (-b))

    print("""
EFFECT 2 -- what each arm gains or loses that the connection does NOT explain
""")
    print("  %-22s %7s %9s %9s %10s" % ("arm", "k", "mean|A|", "xi", "residual"))
    for (label, mode, kp, xi, mA), rr in zip(rows, resid):
        print("  %-22s %7.1f %9.3f %9.2f %+10.2f" % (label, kp, mA, xi, rr))

    by_arm = {}
    for (label, mode, kp, xi, mA), rr in zip(rows, resid):
        by_arm.setdefault(label, []).append(rr)
    print("\n  mean residual by arm:")
    for label, rs in by_arm.items():
        print("    %-22s %+6.2f" % (label, float(np.mean(rs))))

    print("""
READING

  The fit is effect 1: how much reach the transport connection costs, common
  to every arm.  The residual is effect 2: reach an arm has that its
  connection does not account for.

  If old-Coh's residual is clearly positive while the canonical arms' are near
  zero, then the phase term DOES bind -- effect 2 is real -- and the canonical
  terms lose their reach entirely through effect 1, i.e. through where they
  drag the growth front.  That makes claim 2 a fixable problem in candidate
  selection rather than a fatal one in the phase functional.

  If every residual is near zero, there is no separate alignment gain: all the
  reach differences are the connection, old-Coh included, and the paper's
  binding claim has nothing behind it in this probe.
""")


if __name__ == "__main__":
    main()
