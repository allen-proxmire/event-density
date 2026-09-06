# Note — The generation pattern read as a commitment-DOF count, not a mass fit

**Date:** 2026-09-06
**Status:** Scoping note, **Path B reopened** on AP's instruction: *"construct the pattern for other particles using your relational commitment principles, do not look for masses directly. Look for the degrees of freedom that define the commitment."*
**Tier:** structural postdiction of an **ordering**. Not a derivation, and no value is produced.
**Check:** `ED Generative/internal notes/_check_commitment_dof_ordering.py` (re-runnable).
**Builds on:** `Note_MassArc_Koide_CoherenceReframe.md`, `Paper_Koide_GenerationCoherenceMap.md` (both this folder), `Paper_MS-I_GaugeFromChannels` → superseded by `Paper_MS-II_MatterSectorFromTheArrow`, `Paper_087` P07/P09/P11, and the Branch 3 band result (`ED Generative/primitives/P04_bandwidth.md`, gravity ledger #93).

---

## 1. Why this reframe is not a workaround

`arc-M/mass_ratio_constraints.md` §6.3 rules Koide-style relations **not derivable from ED primitives**, and gives a reason rather than a shrug:

> ED's primitive structure produces **classifications and dichotomies cleanly**, but **does not produce continuous numerical relationships**.

**A degrees-of-freedom count is a classification.** So the instruction aims at exactly the half arc-M says works, and deliberately away from the half it says does not. **That verdict is not being challenged here; it is being taken at its word.**

## 2. What the corpus already had, and what it had wrong

The existing reframe collapsed the whole Koide phenomenology to one line via the Brannen form:

$$Q=\tfrac13+\tfrac{w^2}{6}$$

so **`Q` depends only on the wobble depth `w`** — not on the phase offset `δ`, not on the scale `M`. The charged leptons' `Q = 2/3` is exactly `w = √2`.

It then mapped `w` across families against **electric charge**: `w ≈ 1.61 + 0.20·Q_charge`, which extrapolated neutrinos to `w ≈ 1.63`, `Q_ν ≈ 0.77`. **That was falsified in 2026-08**: the measured mass-squared splittings bound `Q_ν ≤ 0.586` (normal ordering) *regardless of the unknown lightest mass*. **The wobble shrinks toward the neutral corner; it does not grow.**

**The map failed because charge is not a count.** It is a continuous label, and fitting a line through it is precisely the "continuous numerical relationship" arc-M says ED does not supply.

## 3. What ED says the commitment degrees of freedom are

**P11, canonically:** *"a chain's multi-channel participation collapses to single-channel participation, with the un-selected channels' phase content randomized."*

**Read in band language — which is only available since Branch 3 (#93) — this says something sharper.** The **Environmental** class is *defined* as the channels whose phase content is randomized, licensed by P11. So:

> **A commitment selects one channel and moves every other participating channel into the Environmental class.**

That is P11 restated in the band vocabulary, and it follows directly from Branch 3's licensing rather than being an extra assumption. **The degrees of freedom that define a commitment are therefore the participating channels that are not already Environmental** — the alternatives it selects among. Their count is the chain's **channel multiplicity**, `N`.

## 4. The identification that makes this non-trivial

`Paper_MS-I` §3 (superseded by `MS-II`, which absorbs the result): **the gauge group is `SU(N)` from channel multiplicity** — derived from bandwidth conservation on the `N`-channel amplitude.

**So the same `N` plays two roles**: it is the number of alternatives a commitment selects among (P11), *and* it is the rank of the gauge structure the chain carries (MS-I/II). **The degrees of freedom that define the commitment are the degrees of freedom that define the gauge content.** That is the corpus's own identification, in half-form, and it is what makes a DOF count something other than numerology: **it is not a new variable introduced to fit the pattern; it is a variable ED already uses for something else.**

## 5. The test

Count, per family, how many **distinct classes of P05-transporting channel** — gauge sectors — the family couples to. **This fits nothing; it checks an ordering.**

| family | `Q` | `w = √(6Q−2)` | sectors | couples to |
|---|---|---|---|---|
| neutrinos | ≤ 0.586 **(bound)** | ≤ **1.231** | **1** | weak |
| charged leptons | 2/3 **(exact)** | **1.4142** | **2** | weak + EM |
| down quarks | 0.731 *(scheme-dep.)* | 1.5447 | **3** | weak + EM + colour |
| up quarks | 0.849 *(scheme-dep.)* | 1.7590 | **3** | weak + EM + colour |

**`w` is monotone in the sector count, with no inversion.**

**And the neutrino direction — the datum that killed the charge map — is the datum that supports this one.** The charge-linear map sent neutrinos *up*; a count sends them *down*, because they couple to fewer sectors. **The measurement went down.**

## 6. What this does not do, stated plainly

1. **It does not split `d` from `u`.** Both are 3-sector families and their `w` differs by 14%. **The count is degenerate exactly where charge is not** — so charge is carrying real information the count does not, and a complete account needs both. This supplies one of two.
2. **It produces no value.** Not `w = √2`, not `δ ≈ 2/9`, not the masses.
3. **It does not explain the `Z₃`.** Checked and negative: P10's rule-types are **three** (matter, gauge, kernel) but generations are all *matter*, so that trichotomy is the wrong one; P09's `U(1)` admits `Z_n` for every `n` and picks none. **Whether the generation 3 is ED's spatial `D = 3` (P06) remains the open fishing question the reframe already named.**
4. **The evidence is weak and is stated as weak** — four families, three distinct DOF values, two `w`s scheme-dependent.

## 7. What it changes

**The one thing it earns:** the wobble ordering now has a candidate explanatory variable that is **a count in ED's own primitives** rather than a fitted line through a continuous label — which is the difference between the falsified map and this one, and it is the difference the instruction was aimed at.

**Where a derivation would have to live:** a mechanism connecting **channel multiplicity `N` to the spread of generation amplitudes**. The directional intuition is that more alternatives at each commitment means more phase-randomization into the Environmental class, hence more spread among the surviving mode amplitudes — **but that is an intuition, not a calculation, and nothing here computes `w(N)`.** Producing `w(N)` and checking it against `√2` at `N = 2` is the first real test this line admits, and it would be a *value*, not an ordering.

**Falsifier.** A family whose `w` inverts against its sector count. The sharpest available case is the neutrino bound tightening: **if `Q_ν` were measured above the charged-lepton `2/3`, the ordering is dead.** Current bounds (`≤ 0.586` normal, `≤ 0.500` inverted) sit comfortably below, so the test is live and currently passing.
