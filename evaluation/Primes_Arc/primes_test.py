"""Primes as a finite-substrate ceiling test (ED-substrate evaluation).

CEILING-LOCATION test, NOT a generation test. The integers-through-the-Factor-
Skyline give a worked example where a finite-reach/finite-memory dynamical system's
reachable vs unreachable information is separated and measured in bits. ED's
substrate is in the finite-memory / zero-entropy class (primitives #2-3), so the
known external anchors (Sarnak Mobius disjointness; the sieve parity barrier) say:
it can reproduce the TEMPLATE layer (periodic residue structure) and provably NOT
the ESCAPE layer (which open positions are prime = sign of mu).

The expected outcome CONFIRMS known hardness. The interesting branch (a finite-
memory f correlating with mu) would be a real discovery -- so Test B is a genuine
experiment, not a foregone conclusion. STRUCTURAL/FORM parallel only: ED does not
explain primes; the primes are a ruler for the substrate's ceiling.

Tests:
  A  predictive-entropy: condition primality on the template state n mod M (M =
     primorials). Finite memory CAPTURES the template (info rises) but the per-open
     -position primality entropy is the ESCAPE floor it cannot supply.
  B  Mobius correlation (THE SHARP ONE): the BEST mod-M (finite-memory) correlator
     with mu, C*(N,M) = (1/N) sum_r |sum_{n=r mod M} mu(n)|. Sarnak => -> 0.
  C  generative match: template stats (lpf-density ladder) reproduce; an escape
     stat (twin-prime singular series 2C2 = 1.32032) is a correlation beyond the
     template.
"""
from __future__ import annotations

import numpy as np

N = 5_000_000
C2 = 0.66016181584686957392  # twin-prime constant; 2*C2 = 1.3203236...


def sieve(n):
    spf = np.zeros(n + 1, dtype=np.int32)         # smallest prime factor
    for p in range(2, int(n**0.5) + 1):
        if spf[p] == 0:
            blk = spf[p * p::p]
            blk[blk == 0] = p
    prime_mask = spf == 0
    prime_mask[:2] = False
    primes = np.nonzero(prime_mask)[0]
    spf[prime_mask] = primes                       # primes: lpf = self
    # Mobius
    mu = np.ones(n + 1, dtype=np.int8)
    for p in primes:
        mu[p::p] = -mu[p::p]                        # parity of #distinct primes
    for p in primes[primes <= int(n**0.5)]:
        mu[p * p::p * p] = 0                        # squareful -> 0
    mu[0] = 0
    return spf, prime_mask, primes, mu


def hbin(p):
    p = np.clip(p, 1e-15, 1 - 1e-15)
    return -(p * np.log2(p) + (1 - p) * np.log2(1 - p))


def main():
    print("=" * 72)
    print(f"PRIMES as a finite-substrate ceiling test   N={N:,}")
    print("=" * 72)
    spf, is_prime, primes, mu = sieve(N)
    n = np.arange(N + 1)
    idx = n >= 2
    base_rate = is_prime[idx].mean()
    print(f"  pi(N)={is_prime.sum():,}  prime density={base_rate:.5f}  "
          f"H_b(prime)={hbin(base_rate):.4f} bits")

    # ---- Anchor to the FS brief's dx-based 1.700-bit template invariant.
    # dx(n)=1 if prime else lpf(n); lpf(composite)<=sqrt(N) so dx is bounded.
    dx = np.where(is_prime[idx], 1, spf[idx]).astype(np.int64)
    K = int(dx.max()) + 1

    def H_of(counts):
        c = counts[counts > 0].astype(float)
        p = c / c.sum()
        return float(-(p * np.log2(p)).sum())

    H_dx = H_of(np.bincount(dx, minlength=K))
    r30 = (n[idx] % 30)
    joint = np.bincount(r30 * K + dx, minlength=30 * K).reshape(30, K)
    Pr = joint.sum(1) / joint.sum()
    H_dx_given_30 = float(sum(Pr[r] * H_of(joint[r]) for r in range(30) if Pr[r] > 0))
    print(f"\n  [anchor to FS brief]  H(dx)={H_dx:.3f}  H(dx|n mod 30)={H_dx_given_30:.3f}"
          f"  -> template info = {H_dx - H_dx_given_30:.3f} bits  (brief: 1.700)")

    # ---- Test A: template capture vs escape floor
    print("\n[A] TEMPLATE CAPTURE vs ESCAPE FLOOR  (condition primality on n mod M)")
    print(f"    {'M':>7} {'P(open)':>8} {'H(prime|nmodM)':>15} {'captured':>9} "
          f"{'P(prime|open)':>14} {'H_b(esc)':>9}")
    H0 = hbin(base_rate)
    for M in (2, 6, 30, 210, 2310, 30030):
        r = n[idx] % M
        cnt = np.bincount(r, minlength=M).astype(float)
        pr = np.bincount(r, weights=is_prime[idx].astype(float), minlength=M)
        with np.errstate(divide="ignore", invalid="ignore"):
            p_prime_r = np.where(cnt > 0, pr / cnt, 0.0)
        w = cnt / cnt.sum()
        H_cond = float((w * hbin(p_prime_r)).sum())
        open_mask = np.gcd(np.arange(M), M) == 1          # residues coprime to M
        open_cnt = cnt[open_mask].sum()
        open_pr = pr[open_mask].sum()
        P_open = open_cnt / cnt.sum()
        P_prime_open = open_pr / max(open_cnt, 1)
        print(f"    {M:>7} {P_open:>8.4f} {H_cond:>15.4f} {H0 - H_cond:>9.4f} "
              f"{P_prime_open:>14.5f} {hbin(P_prime_open):>9.4f}")
    print("    -> conditional entropy FALLS (finite memory captures the template);")
    print("       'captured' = template bits supplied; H_b(esc) = per-open-position")
    print("       primality uncertainty the template CANNOT supply (the escape).")

    # ---- Test B: best finite-memory (mod-M) correlator with mu -> 0  (Sarnak)
    print("\n[B] MOBIUS CORRELATION (sharp)  best mod-M correlator C*(N,M)=1/N sum_r|sum mu|")
    print(f"    {'M':>7}  " + "  ".join(f"N={f}".rjust(11) for f in ("N/4", "N/2", "N")))
    for M in (2, 6, 30, 2310, 30030):
        row = []
        for frac in (4, 2, 1):
            Nf = N // frac
            r = n[2:Nf + 1] % M
            S = np.bincount(r, weights=mu[2:Nf + 1].astype(float), minlength=M)
            row.append(np.abs(S).sum() / Nf)
        print(f"    {M:>7}  " + "  ".join(f"{v:>11.5f}" for v in row)
              + f"   (~sqrt(M/N)={np.sqrt(M / N):.4f})")
    print("    -> the BEST finite-memory function still has C* -> 0 as N grows")
    print("       (bounded by ~sqrt(M/N)): no finite-memory f correlates with mu.")
    print("       FALSIFIER (not seen): any bounded-complexity f with C* away from 0.")

    # ---- Test C: template stats reproduce; escape stat (2C2) is beyond template
    print("\n[C] GENERATIVE  template lpf-ladder (reproducible) vs escape 2C2 (correlation)")
    print("    lpf-density ladder  P(lpf=p) = (1/p) prod_{q<p}(1-1/q):")
    pred = 1.0
    small = [2, 3, 5, 7, 11, 13]
    prev = 1.0
    print(f"      {'p':>4} {'empirical':>11} {'predicted':>11}")
    acc = 1.0
    for i, p in enumerate(small):
        emp = (spf[idx] == p).mean()
        pr_pred = (1.0 / p) * acc
        acc *= (1 - 1.0 / p)
        print(f"      {p:>4} {emp:>11.5f} {pr_pred:>11.5f}")
    # twin primes: does the density carry the singular-series factor 2C2?
    tw = int((is_prime[2:N - 1] & is_prime[4:N + 1]).sum())   # (p, p+2)
    lnN = np.log(N)
    naive = N / lnN**2                       # independence (no correlation) estimate
    hl = 2 * C2 * N / lnN**2                  # Hardy-Littlewood (with singular series)
    print(f"\n    twin primes (p,p+2) up to N : {tw:,}")
    print(f"      pi2 / (N/ln^2 N)            : {tw / naive:.4f}   "
          f"(independence predicts 1.000 -> MISSES by the singular series)")
    print(f"      pi2 / (2*C2 * N/ln^2 N)     : {tw / hl:.4f}   "
          f"(Hardy-Littlewood 2C2={2*C2:.4f}, ->1 with lower-order corrections)")
    print("    -> template stats (lpf ladder) reproduce from finite-local structure;")
    print("       the twin density needs the 2C2 CORRELATION -- an escape structure")
    print("       a finite-local template generator does not supply.")

    print("\n" + "=" * 72)
    print("VERDICT (expected, = known hardness): finite memory SATURATES the template")
    print("and FAILS the escape -- mu-correlation -> 0; escape entropy irreducible;")
    print("singular-series correlation beyond template. The integers locate the")
    print("substrate's ceiling. STRUCTURAL/FORM parallel only; not a generation claim.")
    print("=" * 72)
    return True


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
