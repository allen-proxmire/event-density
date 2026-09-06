# Note — Two bankings from the external mass reading, plus the √2 and the 3s

**Date:** 2026-09-06
**Status:** Two banked items (§§1–2) at stated tiers, plus two answers to AP's follow-up (§§3–4).
**Occasion:** An external model (Gemini) offered a mass-sector reading in ED's idiom. Most of it re-derives corpus content; **two things are worth keeping and are banked here, and the rest deliberately is not** — re-banking existing results under a new name is how a corpus ends up citing itself through a third party.
**Check:** arithmetic in `ED Generative/internal notes/_check_w_of_N.py` and this session's transcript.

---

## 1. BANKED — `P-Commitment-Linear` reconciles the amount-reading and the rate-reading of mass

**The apparent conflict.** `Paper_113` gives mass as rest-frame **bandwidth content** — an *amount*. The external reading gives mass as a **commitment rate** — the particle's ticking cadence, `ω = mc²/ℏ` taken literally. **That is the same amount-versus-rate distinction that forced the propagation sector from P04 to P05** (ledger #96): canonical P04 carries amount, not rate.

**They reconcile, through a postulate the corpus already has.** `Paper_GR-I` §2, **`P-Commitment-Linear`**: `Γ_commit ∼ b_int/reserve` — *the commitment rate is linear in the metric-relevant bandwidth.* So with `m ∝ b` (Paper_113) and `Γ ∝ b/reserve` (GR-I):

$$m \;\propto\; \Gamma_{\rm commit}\times{\rm reserve}$$

**The rate-reading is not a rival to `Paper_113`; it is the same quantity read from the other side, bridged by a named ED postulate.** That connection was not previously drawn, and it is cheap: it uses nothing new.

**The cost, which the external reading does not state.** The proportionality holds **only if the commitment reserve is common across generations.** If `reserve` differs between `e`, `μ` and `τ`, then `m ∝ b` and `Γ ∝ b/reserve` come apart — **and they come apart precisely where the generations differ, which is the only place the identification is being asked to work.**

**Tier: a stated bridge, conditional on a common reserve.** Not a derivation of either side, and not evidence for the rate-reading over the amount-reading. **`P-Commitment-Linear` is itself a declared postulate**, so this bridges one posit to another rather than grounding either.

## 2. BANKED — `Q = 2/3` is the midpoint in `Q` alone; "equilibrium" arguments from it are parametrization artifacts

**Recorded so it is not re-derived**, including by me. The claim in circulation is that `2/3` is a *"geometric equilibrium"* between the degenerate case (`Q = 1/3`, all masses equal) and the disjoint case (`Q → 1`, one mass dominant). The first half is right — those are the endpoints. **The "equilibrium" is not:**

| variable | range | midpoint | leptons | |
|---|---|---|---|---|
| `Q` | [0.333, 1] | 0.667 | **0.667** | **midpoint** |
| `w = √(6Q−2)` | [0, 2] | 1.000 | 1.414 | not the midpoint |
| `CV = w/√2` | [0, 1.414] | 0.707 | 1.000 | not the midpoint |

**A midpoint is not a distinguished point unless something selects the parametrization, and nothing does.** `Q` is one of at least three natural coordinates on the same one-parameter family, and the leptons are central in exactly one of them.

**This is the second parametrization artifact found in this material in one day** — the first being that the `√2` in `w = √2` is itself an artifact of the Brannen normalization (§3). **When a "significant number" turns out to be a midpoint or a normalization constant, that is the finding.**

## 3. On the `√2` — AP's question, and the honest split

**AP:** *"don't you think it's interesting to see √2? the diagonal of the unit square and all the Tsirelson Bell stuff?"*

**Half of it is an artifact and half of it is real, and the two must be separated.**

**The artifact.** `w = √2·(σ_A/μ_A)` — the `√2` enters because Brannen writes the modulation as `1 + w·cos(δ + 2πk/3)` and the mean of `cos²` over three 120°-separated points is `1/2`. **A different normalization gives a different number for the same physics.** So the `√2` in *"the wobble depth is `√2`"* carries no information; the physical statement is `CV = 1`.

**The real part, and AP's intuition is right about it.** Decompose the generation-amplitude vector `A = (A₁,A₂,A₃)` into its component along the democratic diagonal `(1,1,1)/√3` and the orthogonal remainder:

$$\lVert A_\parallel\rVert=\sqrt3\,\mu,\qquad \lVert A_\perp\rVert=\sqrt3\,\sigma,\qquad \frac{\lVert A_\perp\rVert}{\lVert A_\parallel\rVert}=\frac{\sigma}{\mu}={\rm CV}$$

**So `CV` is the tangent of the angle between the amplitude vector and the diagonal, and `CV = 1` is exactly 45°.** That is a genuine geometric statement — **the spread component equals the mean component** — and it *is* the diagonal-of-the-unit-square `√2`. (It is also Foot's 1994 observation in another dress; **prior art, not ours.**)

**On the Tsirelson link — shared arena, not shared mechanism.** Tsirelson's `2√2` likewise traces to a 45° bisection in a real inner-product space, and in ED both angles live in **the same object**: the sesquilinear inner product on participation amplitudes (`Paper_004`, `Paper_007`). **That is a real structural commonality and it is worth exactly that much.** `√2` is the generic Euclidean signature of *a vector bisecting two orthogonal directions*, which is common enough that co-appearance is weak evidence for a shared cause.

**And there is a substantive disanalogy that should stop the connection from being pushed further: Tsirelson's `2√2` is a MAXIMUM** — a bound saturated by optimal states, with a variational principle behind it. **Koide's 45° is not a maximum.** `CV` runs to `√2`, and the quarks sit above `1`. **One is an extremal principle; the other is an interior point.** Until something makes `CV = 1` extremal, the two `√2`s are the same *arithmetic* and not the same *kind of fact*.

## 4. On the 3s — the corpus already tried, and the route was refuted

**AP:** *"And 3 colors, 3 channels, 3Ds, 3 particles in 3 families?"*

**Four independent 3s, and all four are inherited or postulated:**

| the three | status in ED |
|---|---|
| spatial `D = 3` | **P06, postulated.** The card is emphatic: *"not derived from compactification of higher-dimensional structure, not derived from a counting argument, not derived from anthropic reasoning."* |
| three generations | **not derivable** — `arc-M/mass_ratio_constraints.md` §6.3 |
| `SU(3)` colour rank | **not selected** — see the wall below |
| P10's three rule-types (matter/gauge/kernel) | a primitive **classification**, and *not* the generation triplet (generations are all *matter*) |

**And the unification route was tested, not merely unattempted.** `substrate-evaluation/Paper_HowPDECoarseGrainReality` §2:

> There is also a standing **wall**: the multiplicities `{1,2,3}` — why three families, why these group ranks — are **not** selected. **ED's own route to derive them was tested and refuted (a symmetric channel-multiplet is stable for *all* `N`)**, so this is a genuine open limit, not an oversight.

**So the pattern AP is noticing is real in the world, and ED's position on it is a banked negative.** Nothing in ED picks `N = 3`, and the one mechanism that would have — stability selection on channel multiplicity — **is stable for every `N`**, which is a refutation with a stated cause rather than a failure to look.

**The honest statement: the corpus has four separate 3s and no bridge between any two of them.** Treating their coincidence as a signature would be reading a Standard-Model fact as an ED result. **That does not make the question uninteresting — it makes it a known wall with a specific mechanism already ruled out**, which is the most useful thing to know before spending on it again.

## 5. Deliberately NOT banked

The external reading's other three claims — that `√m` is the substrate amplitude, that the three generations are 120° phase modes of one loop, and that `Q = 2/3` means `Σm = 4Σ√(mᵢmⱼ)` — are **already corpus content**: `Paper_113` plus the amplitude carrier `P = √b e^{iπ}`; the Brannen form in `Note_MassArc_Koide_CoherenceReframe`; and ledger #81's `Coh = ½Str`, which is that rearrangement verbatim. **Independent convergence is mildly reassuring and is not new information.** They are recorded here as *not banked*, on purpose.
