# Note — Computing `w(N)`: the attempt failed, and two things survive it

**Date:** 2026-09-06
**Status:** **NEGATIVE RESULT** with a reframe attached. Path B.
**Tier:** no mechanism produced; one restatement and one structural relocation.
**Check:** `ED Generative/internal notes/_check_w_of_N.py` (re-runnable).
**Follows:** `Note_CommitmentDOF_GenerationPattern_2026-09-06.md` (#98), which named `w(N)` as the first real test its line admits — because an ordering is the weakest thing that line can produce and a value is the strongest.

---

## 0. Headline

**The task did not succeed. No mechanism here computes `w(N)`.** Three candidates were fixed from ED's machinery *before* computing, and all three fail.

Two things survive: **what `w` actually is**, and **a structural threshold the measured values sit on.** Neither is a derivation.

## 1. Method, stated first because it constrains everything

The corpus explicitly forbids bolting Koide on by matching a stray fraction (`Paper_ChargeAsTopology_B4`'s retrofit trap), and the instruction that opened this line said *not* to chase the masses. **So the candidates were fixed from the primitives first and computed second.** No distribution was searched for, and none was adjusted after seeing its answer.

## 2. What `w` is, before any mechanism

The Brannen form puts the three generation amplitudes 120° apart: `√m_k = M(1 + w·cos(δ + 2πk/3))`. Over three 120°-separated points, `Σcos = 0` and `Σcos² = 3/2` **for any `δ`**. So for the amplitudes `A_k = √m_k`:

$$\mu_A = M,\qquad \sigma_A^2 = \tfrac{M^2w^2}{2},\qquad \boxed{\,w=\sqrt2\,\cdot\,\frac{\sigma_A}{\mu_A}\,}$$

**`w` is `√2` times the coefficient of variation of the generation amplitudes.** So Koide's `Q = 2/3` says exactly:

> **The standard deviation of the three generation amplitudes equals their mean. `CV = 1`.**

| family | `N` | `Q` | `w` | `CV` |
|---|---|---|---|---|
| neutrinos | 1 | ≤ 0.586 | ≤ 1.231 | **≤ 0.871** |
| charged leptons | 2 | 2/3 | 1.4142 | **1.0000** |
| down quarks | 3 | 0.731 | 1.5447 | **1.0922** |
| up quarks | 3 | 0.849 | 1.7590 | **1.2438** |

This is a restatement, not a result. **But it is the variable any mechanism has to deliver, and it is sharper than "why `√2`".**

## 3. The three candidates, and how they fail

**(a) Simplex sharing.** P04 gives non-negative bandwidth; `P-Locus-Bandwidth-Bound` gives a finite per-locus total. `N` channels sharing a fixed budget with no further information is uniform on the simplex — Dirichlet(1,…,1) — so one channel's share is Beta(1, N−1).

**(b) Random-phase superposition.** P11 randomizes un-selected phases. At the limit, an amplitude is the modulus of `N` equal contributions with iid uniform phases: a 2-D random walk, Rayleigh amplitude.

**(c) Maximum entropy.** Non-negativity (P04) plus a fixed mean and nothing else gives the exponential.

| candidate | N=2 | N=3 | N=4 | N→∞ |
|---|---|---|---|---|
| (a) simplex, CV of the share | 0.5774 | 0.7071 | 0.7746 | 0.9975 |
| (a′) simplex, CV of √share | 0.3536 | 0.4146 | 0.4430 | 0.5220 |
| (b) Rayleigh amplitude | 0.5227 | 0.5227 | 0.5227 | 0.5227 |
| (c) exponential | **1.0000** | 1.0000 | 1.0000 | 1.0000 |
| **target** | **1.0000** | — | — | rising to **1.2438** |

**They fail in complementary ways, and that is the informative part.**

- **(a)/(a′)** give real `N`-dependence **in the right direction** — but never reach `CV = 1`. The share's CV approaches 1 only as `N → ∞`, and at `N = 2` gives 0.577.
- **(b)** is `N`-independent at 0.523. Wrong value, no dependence.
- **(c)** gives `CV = 1` **exactly** — the lepton value — but is likewise `N`-independent, so it predicts `w = √2` for *every* family and **is falsified by the quarks.**

**One candidate supplies the lepton value and precludes the variation; another supplies the variation and precludes the value.** Any mechanism has to do both, and neither natural route does.

## 4. The one structural thing that fell out

A standard result (**inherited mathematics, not derived here**): a **log-concave** density on `[0,∞)` has `CV ≤ 1`, with **equality iff exponential**. Applied to the measured values — the CVs are arithmetic from the measured `Q`, and the threshold is a theorem, so **nothing here is fitted**:

| family | `CV` | generation-amplitude distribution |
|---|---|---|
| neutrinos | ≤ 0.871 | log-concave **allowed** |
| **charged leptons** | **1.0000** | **exactly the log-concave boundary** (exponential) |
| down quarks | 1.0922 | **cannot** be log-concave |
| up quarks | 1.2438 | **cannot** be log-concave |

> **Koide's `2/3` places the charged leptons exactly on the log-concavity boundary of the generation-amplitude distribution. Neutrinos sit below it, quarks above it, and the crossing is ordered by `N`.**

**Be clear about what this is not.** `CV = 1` **is** Koide's relation — the boundary statement is the same fact in another variable, **not independent evidence**. What is new is that **the boundary has a known structural meaning**, which relocates the question:

- **from** *"why `w = √2`?"* — a **value** question, the half `arc-M` says ED does not do;
- **to** *"why does the generation-amplitude distribution sit at the log-concave boundary at `N = 2`, and cross it as `N` grows?"* — a **classification** question, the half `arc-M` says ED does cleanly.

**And a threshold crossing at one of four points is a coincidence until something explains it.** This is a better-posed place to put the question and nothing more.

## 5. Honest accounting

**Held to the same bar as a positive** (per the corpus's standing instruction on negatives): this is a **negative result**. `w(N)` was not computed. The falsifier named in #98 — *compute `w(N)` and check `√2` at `N = 2`* — **was attempted and not met.**

What the DOF line still has is what it had before: **an ordering**, `ν < ℓ < q`, with the neutrino direction right where the corpus's charge map was wrong. **It has not been upgraded to a value, and should not be described as though it had been.**

## 6. What would actually decide it

A distribution over generation amplitudes that is **`N`-dependent and crosses `CV = 1` at `N = 2`**. The two natural families each supply exactly one of those properties, so the mechanism — if there is one — is not either of them, and is not a small variation on either. **Nothing in ED currently points at a third.**
