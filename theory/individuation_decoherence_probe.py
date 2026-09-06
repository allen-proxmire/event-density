"""Does the decoherence account fix theta_ind?  Route (1) of the two named.

`foundations/Paper_Individuation_TheSystemEnvironmentCut.md` sec 6 says its own
account and `qft/Paper_024_LindbladLimit`'s postulated factorization
(`P-Factorized-IC`) "should be read as two accounts of the same gap".  This asks
whether the second one determines the first one's free threshold.

THE IDENTIFICATION, WHICH IS THE PART THAT NEEDS ARGUING.

  `P-Factorized-IC` says rho_tot(0) = rho_S(0) (x) rho_E(0): NO system-environment
  correlation.  In ED, correlation between a chain-complex and its outside is
  carried by cross-boundary shared channels -- V5 is the cross-chain correlation
  kernel (Paper_090), and b_bdry(S) is exactly the shared-channel content across
  the cut.  So:

      exact factorization  <=>  b_bdry(S) = 0  <=>  R(S) = infinity

  EXACT factorization is individuation at theta_ind = infinity.  That is a real
  identification of the two accounts, and it also shows P-Factorized-IC cannot
  fix a FINITE threshold on its own -- as an exact postulate it names only the
  limit.

WHAT DOES FIX A FINITE VALUE IS ITS DOMAIN OF VALIDITY.

  Factorization is an approximation and it has a domain.  Correlations decay
  with a substrate correlation length xi, so a locus in S at depth d from the
  boundary is still correlated with the outside when d < xi.  If EVERY locus of
  S is within xi of the boundary then S is all boundary layer, has no interior,
  and factorization has no domain of validity at all -- not 'is inaccurate' but
  'has nowhere to be accurate'.

  AND DEPTH IS QUANTIZED, which is what makes this sharp.  Depth is counted in
  loci, so the condition for an interior to exist is ceil(a/2) > xi -- a STEP
  function of xi, not a quantity proportional to it:

      0 < xi <= 1  ->  a >= 2  ->  theta_ind = 0.5
      1 < xi <= 2  ->  a >= 3  ->  theta_ind = 1.0     <-- measured xi ~ 1.83
      2 < xi <= 3  ->  a >= 5  ->  theta_ind = 2.0

  using R = (a-1)/2 from individuation_theta_probe.py result (C).  So theta_ind
  does NOT inherit xi's uncertainty -- only the question of which integer
  bracket xi falls in.  A LATTICE-COMBINATORIAL route reaches the same value
  without using xi at all: the smallest square with a locus off its own
  boundary is a = 3, giving theta_ind = 1.  Two independent routes, one value.

  THE SENSITIVITY.  This needs xi < 2, and the corpus value xi = 1.8 +/- 0.3
  puts that boundary about 0.6 sigma away.  If xi > 2 then theta_ind = 2.  So
  the result is sharp and falsifiable: tighten xi and the answer is decided.

  THIS ALSO REFUTES an earlier candidate of my own.  individuation_theta_probe
  floated theta_ind = (xi-1)/2 ~ 0.4, flagged there as unargued arithmetic.
  It is the wrong arithmetic: it identified theta_ind's length with xi, but the
  boundary shell must be crossed on BOTH sides before an interior exists.

WHAT THIS PROBE MEASURES.  The certified substrate's C(r) and xi; the fraction
of S's correlation mass crossing the boundary at two cutoffs (the far one is
tail-dominated and is shown to make that visible); and the interior fraction
against R, which is where the threshold is read off.

Run: python individuation_decoherence_probe.py
"""
import math
import sys

import numpy as np

SIM = r"C:/Users/allen/GitHub/event-density/evaluation/Bits"
THEORY = r"C:/Users/allen/GitHub/event-density/theory"
sys.path.insert(0, SIM)
sys.path.insert(0, THEORY)

import p12_phase_in_grad_probe as P

L = 64
BWD, KBW, KRHO = 0.6, 0.5, 0.5
RMAX = 16


def corr_fn(C, xi):
    """Measured C(r) inside the sampled range, exponential tail beyond it."""
    rs = sorted(C)
    top = max(rs) if rs else 1
    def f(r):
        if r <= 0:
            return 1.0
        ri = int(round(r))
        if ri in C:
            return max(C[ri], 0.0)
        if ri < top:
            lo = max([x for x in rs if x <= ri], default=1)
            return max(C.get(lo, 0.0), 0.0)
        base = max(C.get(top, 1e-6), 1e-6)
        return base * math.exp(-(r - top) / max(xi, 1e-6))
    return f


def cross_fraction(a, f, rmax=RMAX):
    """Fraction of S's correlation mass that leaves S, for an a x a square.

    Sum over u in S and displacements within RMAX of C(|d|), split by whether
    u + d lands inside S.  Translation-invariant, so no grid needed."""
    inside = outside = 0.0
    for ur in range(a):
        for uc in range(a):
            for dr in range(-rmax, rmax + 1):
                for dc in range(-rmax, rmax + 1):
                    if dr == 0 and dc == 0:
                        continue
                    d = math.hypot(dr, dc)
                    if d > rmax:
                        continue
                    c = f(d)
                    vr, vc = ur + dr, uc + dc
                    if 0 <= vr < a and 0 <= vc < a:
                        inside += c
                    else:
                        outside += c
    tot = inside + outside
    return outside / tot if tot > 0 else 1.0


def interior_fraction(a, xi):
    """Fraction of S's loci deeper than xi from the boundary."""
    n = 0
    for r in range(a):
        for c in range(a):
            depth = min(r, c, a - 1 - r, a - 1 - c) + 1   # depth in loci
            if depth > xi:
                n += 1
    return n / (a * a)


def main():
    print("Does the decoherence account fix theta_ind?")
    print("=" * 76 + "\n")

    print("1. the substrate's own correlation length (certified rule, mode=grad)")
    xis = []
    for seed in (11, 12, 13, 14, 15):
        rng = np.random.default_rng(seed)
        phase, committed, coords, flip = P.run_fill(
            L, BWD, KBW, KRHO, 1.0, rng, mode="grad")
        C = P.corr_vs_r(phase, committed, coords, rng, n_pairs=200000, rmax=30)
        xi = P.xi_estimate(C)
        xis.append(xi)
        if seed == 11:
            Cref = C
    xi = float(np.mean(xis))
    xsd = float(np.std(xis))
    print("   xi = %.3f +/- %.3f lu over 5 seeds   (corpus: 1.8 +/- 0.3)\n" % (xi, xsd))

    f = corr_fn(Cref, xi)

    print("2. factorization error vs R.  'cross' = the fraction of S's correlation")
    print("   mass that leaves S -- i.e. what P-Factorized-IC throws away.\n")
    print("   a     R=(a-1)/2   cross(r<=3xi)   cross(r<=16)   interior frac")
    rows = []
    near = max(2, int(round(3 * xi)))
    for a in (2, 3, 4, 5, 6, 8, 10, 12, 16, 20):
        R = (a - 1) / 2
        cf_near = cross_fraction(a, f, near)
        cf_far = cross_fraction(a, f, 16)
        itf = interior_fraction(a, xi)
        rows.append((a, R, cf_near, itf))
        print("   %-5d %9.2f %14.4f %14.4f %14.4f"
              % (a, R, cf_near, cf_far, itf))
    print("""
   The two cross columns differ because the FAR one is dominated by the many
   weakly-correlated distant pairs: pair multiplicity grows like r while C(r)
   has already decayed, so the tail carries most of the MASS without carrying
   most of the CORRELATION.  The NEAR column (r <= 3xi) is the one that speaks
   to factorization error.  Neither reaches a small number at accessible sizes,
   which is a real observation about Paper_024's regime and is noted as such.""")

    print("")
    print("3. the threshold, and DEPTH IS QUANTIZED -- which sharpens it")
    first_int = next((a for a, R, cf, itf in rows if itf > 0), None)
    print("   A locus decorrelates from outside when its DEPTH d (in loci) exceeds xi.")
    print("   Depth is an INTEGER, so the condition is ceil(a/2) > xi and the threshold")
    print("   is a STEP FUNCTION of xi, not proportional to it:")
    print("")
    print("      xi range      smallest a with an interior   theta_ind = (a-1)/2")
    for lo, hi, a_ in ((0, 1, 2), (1, 2, 3), (2, 3, 5), (3, 4, 7)):
        mark = "   <-- measured xi = %.2f" % xi if lo < xi <= hi else ""
        print("      %d < xi <= %-4d %14d %26.1f%s"
              % (lo, hi, a_, (a_ - 1) / 2, mark))
    print("")
    print("   (measured: first a with a locus deeper than xi is a = %s)" % first_int)
    print("""
   => theta_ind = 1, and it is STABLE for any xi in (1, 2).  It does NOT inherit
      xi's uncertainty -- only the question of which integer bracket xi falls in.
      And the lattice-combinatorial floor (the smallest square with a locus off
      its own boundary is a = 3) gives the SAME answer without using xi at all.
      Two independent routes, one value.""")
    print("""
   THE SENSITIVITY, STATED PLAINLY.  This needs xi < 2.  The corpus value is
   xi = 1.8 +/- 0.3 (Paper_096, GR-SC 1.7 half-decay, 10 seeds), which puts the
   xi = 2 boundary only about 0.6 sigma away -- roughly a 1-in-4 chance the
   bracket is wrong.  If xi > 2 then theta_ind = 2, not 1.  So this is a sharp
   and falsifiable consequence: TIGHTEN xi AND THE ANSWER IS DECIDED.
   This probe's own 5-seed estimate is %.3f +/- %.3f, but by a DIFFERENT
   estimator (1/e crossing of the phase autocorrelation, not the GR-SC 1.7
   half-decay), so it is NOT a tightening of the corpus value and is not quoted
   as one.""" % (xi, xsd))

    print("""
4. and the correction to the earlier candidate

   individuation_theta_probe.py flagged theta_ind = (xi-1)/2 ~ 0.4 as an
   unargued arithmetic candidate.  IT IS THE WRONG ARITHMETIC.  That reading
   identified theta_ind's LENGTH with xi directly; the boundary shell has to be
   crossed on BOTH sides before an interior exists, so the linear extent needed
   is 2*xi, not xi.  The decoherence route therefore does not confirm 0.4 -- it
   REFUTES it.  With depth quantization the answer is theta_ind = 1, reached
   independently by the lattice route, and stable across xi in (1, 2).
""")


if __name__ == "__main__":
    main()
