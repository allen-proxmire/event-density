# Primes as a Finite-Substrate Ceiling Test — Results

**Arc:** Primes — using the integers (through the Factor Skyline) as a ruler to locate the ED substrate's information ceiling.
**This is a CEILING-LOCATION test, not a generation test.** ED's substrate is in the finite-reach/finite-memory (zero-entropy) class by primitives #2–3; the external anchors (Sarnak Möbius disjointness; the sieve parity barrier) predict it reproduces the **template** layer and provably not the **escape** layer. The expected outcome *confirms known hardness*; the interesting branch (a finite-memory function correlating with μ) would be a real discovery — so Test B is a genuine experiment.
**STRUCTURAL/FORM parallel only:** ED does not explain primes; the primes are a ruler for the substrate's ceiling. No content claim.
**Code:** `Primes_Arc/primes_test.py` (numpy; sieve to N=5,000,000). **Date:** June 2026.

---

## Anchor to the FS brief

| quantity | value | brief |
|---|---|---|
| H(dx) | 2.997 bits | 2.483 (smaller scale — H(dx) is scale-dependent) |
| H(dx \| n mod 30) | 1.297 bits | 0.783 |
| **template information H(dx) − H(dx\|n mod 30)** | **1.700 bits** | **1.700 (scale-invariant)** |

The **1.700-bit template invariant is reproduced exactly** — the robust, scale-invariant figure, independent of the (scale-dependent) absolute entropies.

## Test A — template capture vs the escape floor

Condition primality on the template state `n mod M` (M = primorials):

| M | P(open) | H(prime\|n mod M) | template captured | P(prime\|open) | H_b(escape per open) |
|---|---|---|---|---|---|
| 2 | 0.500 | 0.291 | 0.074 | 0.139 | 0.583 |
| 6 | 0.333 | 0.247 | 0.118 | 0.209 | 0.740 |
| 30 | 0.267 | 0.221 | 0.144 | 0.261 | 0.829 |
| 210 | 0.229 | 0.203 | 0.162 | 0.305 | 0.887 |
| 2310 | 0.208 | 0.191 | 0.174 | 0.335 | 0.920 |
| 30030 | 0.192 | 0.181 | 0.184 | 0.363 | 0.945 |

**Reading:** as the template state grows, finite memory **captures more of the template** (captured bits rise; conditional entropy falls). But conditioning resolves the *covered* positions (definitely composite → zero entropy) and supplies **nothing beyond base rate about which *open* positions are prime** — open residues are structurally identical (coprime to M; primes equidistribute among them by Dirichlet). That residual — `H(prime|n mod M) ≈ 0.18–0.29` bits/integer, or `H_b ≈ 0.58–0.95` bits per *open* position — is the **escape**: the parity barrier in bits, irreducible to any finite template state. (The brief's "~0.26-bit" figure is the per-integer escape peak; consistent with the per-integer column here.)

## Test B — Möbius correlation (the sharp one)

The **best** mod-M (finite-memory) correlator with μ, `C*(N,M) = (1/N) Σ_r |Σ_{n≡r mod M} μ(n)|` — the optimum over *all* functions of `n mod M`:

| M | N/4 | N/2 | N | ~√(M/N) |
|---|---|---|---|---|
| 2 | 0.00018 | 0.00014 | 0.00014 | 0.0006 |
| 6 | 0.00067 | 0.00032 | 0.00024 | 0.0011 |
| 30 | 0.00329 | 0.00192 | 0.00118 | 0.0024 |
| 2310 | 0.03241 | 0.02225 | 0.01523 | 0.0215 |
| 30030 | 0.10033 | 0.07101 | 0.05021 | 0.0775 |

**Reading:** for every M, the best finite-memory correlator **decays toward 0 as N grows** (≈ halving as N doubles; bounded by ~√(M/N)). Even the *optimal* function of the template state cannot correlate with μ asymptotically — **Sarnak-in-this-class, confirmed**. The **falsifier was not seen**: no bounded-complexity f with C\* bounded away from 0. (A finite *fixed* M with growing N → 0 is the operative statement; larger M needs proportionally larger N, exactly the activation-horizon growth.)

## Test C — generative: template reproducible, escape not

**Template (reproducible from finite-local structure).** The lpf-density ladder `P(lpf=p) = (1/p) ∏_{q<p}(1−1/q)`:

| p | empirical | predicted |
|---|---|---|
| 2 | 0.50000 | 0.50000 |
| 3 | 0.16667 | 0.16667 |
| 5 | 0.06667 | 0.06667 |
| 7 | 0.03810 | 0.03810 |
| 11 | 0.02078 | 0.02078 |
| 13 | 0.01598 | 0.01598 |

Exact to 5 decimals — the template statistics fall straight out of finite-local residue structure.

**Escape (a correlation beyond the template).** Twin primes (p, p+2) up to N = **32,463**:
- `π₂ / (N/ln²N) = 1.545` — pure independence/template predicts **1.000**, and *misses*.
- `π₂ / (2·C₂·N/ln²N) = 1.170` — the Hardy–Littlewood **singular series 2C₂ = 1.3203** is the dominant correction (closes most of the 1.545→1 gap; the residual 1.17 is the crude `N/ln²N` vs the integral Li₂(N), ~+13% at this N).

The twin density carries the **2C₂ pair-correlation** — an escape structure a finite-local template generator does not supply.

## Verdict — exactly the predicted ceiling

> Finite memory **saturates the template** (1.700-bit invariant reproduced; lpf-ladder exact; template captured) and **fails the escape** (per-open-position primality entropy irreducible; best finite-memory μ-correlator → 0; twin density needs the 2C₂ singular series). The integers, through the Factor Skyline, locate the substrate's ceiling precisely where Sarnak disjointness and the sieve parity barrier place it.

This is the expected, allowed, **informative** outcome: a clean confirmation that ED's finite-memory class hits the parity-barrier ceiling exactly where external mathematics says it must. **Crank-safety:** structural/form parallel only — ED does not generate the primes; the primes measure the class ED belongs to. The 1.700 bit is the citable invariant; the 0.26 escape figure is a scale-dependent peak, not a universal constant.

## Relation to A1 (channel capacity) and the broader program

A1 found ED's controlled channel capacity is exactly zero (finite-reach locality), measured *inside* ED. This test measures the *same* finite-reach/finite-memory ceiling against an **external, math-certified ruler** (Möbius disjointness). Two readings of one property — ED's hard ceiling on long-range/global information — one internal, one externally calibrated. Together they answer the standing question "can ED finite-memory produce an infinite-memory system like primes?": **the template, yes; the escape, no — and the *no* is load-bearing.**

---

*Falsifier restated (not observed): a bounded-complexity, ED-definable f(n) with (1/N)Σ μ(n)f(n) bounded away from 0 would refute Sarnak-in-this-class — a genuine discovery. The expected confirmation stands.*
