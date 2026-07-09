# The P14 Interference Cross-Term Yields a Valid MOND Interpolation μ(x): Monotone, Correct Limits, Sign Worry Regime-Separated (Given the Quadratic-Strain Reading)

**Foundations, gravity / curvature-emergence arc. Attacks the specific gap Paper E named: the interference cross-term carries a *sign-indefinite* `cosΔπ`, so recovering a monotone positive MOND interpolation `μ(x)` with the right limits was "assumed, not shown." Probe: `evaluation/CurvatureEmergence/p14_interference_to_mond_mu_probe.py`. RESULT: given the banked (still-open) quadratic/interfering reading of gravitational strain (P14), the cross-term = geometric mean of squared accelerations = the deep-MOND relation, and a monotone positive `μ(x)` with correct Newton and deep-MOND limits DOES emerge; the sign-indefinite phase is regime-separated (it only acts where the diagonal/Newton term already dominates). HONEST: the two *limits* + monotonicity + the sign-resolution are ROBUST; the *exact* `μ` transition shape is MODEL-DEPENDENT (the strain-to-acceleration mapping); and the whole thing is CONDITIONAL on the open quadratic-strain commitment. This UPGRADES MOND from "housed in ED's scalar sector" to "reproduced with correct limits, monotone μ shown not assumed" — it does NOT derive a unique μ from nothing. Crank-railed: the MOND arc is a documented over-read trap (see [[project_p14_partial_reduction]]).**

---

## 1. The gap being attacked

The banked P14 result: gravitational bilocal strain, read as a *quadratic/interfering* functional of amplitude, makes two sources (local mass + cosmic horizon) superpose on one bilocal channel as
$$ |P_{\text{loc}} + P_{\text{hor}}|^2 = b_{\text{loc}} + b_{\text{hor}} + 2\sqrt{b_{\text{loc}}\,b_{\text{hor}}}\,\cos\Delta\pi. $$
The diagonal (`b_loc + b_hor`) is self/Newton; the off-diagonal `2√(b_loc b_hor)cosΔπ` is the interference, whose geometric-mean modulus is MOND's structure. Paper E flagged the honest gap precisely: `cosΔπ` is **sign-indefinite** (it can be negative, the "partial-negative" envelope), so recovering a smooth, positive, monotone MOND interpolation `μ(x) ∈ [0,1]` "requires a coarse-graining / phase-averaging step that is assumed, not shown." This note shows it is not merely assumable: a valid `μ` emerges, and the sign worry is resolved by regime separation.

## 2. The model (stated so the tiers are honest)

- **(M1) Strain is field energy, `S ∝ (acceleration)²`** (standard: field energy density `∝ |∇Φ|² = g²`). So the local source strain is `S_N = g_N²` (`g_N` = Newtonian acceleration) and the horizon strain scale is `S_0 = a_0²` (`a_0` = the horizon-induced acceleration scale, ED-inherited `~ c H_0`, **not** derived here).
- **(M2) The two strains superpose on the bilocal channel** (P14, banked): felt strain `S = S_N + 2C√(S_N S_0) + [S_0]`, with `C = ⟨cosΔπ⟩` the coherence.
- **(M3) Isotropy drops the horizon *self*-term from the *net* acceleration.** The cosmic horizon pulls equally in all directions, so its diagonal self-term `S_0` sources no *net* local force; only its *interference* with the (anisotropic) local field, aligned with `g_N`, survives. This is the reason the `+S_0` constant is absent, so the result is MOND rather than merely additive accelerations. *(New argument; it is what turns the interference into an interpolation rather than a shift.)*

Given (M1)-(M3), the felt acceleration obeys the **ED interference relation**
$$ g^2 = g_N^2 + 2C\,g_N a_0 \quad\xrightarrow{\text{deep-MOND normalized}}\quad g^2 = g_N^2 + g_N a_0. $$

## 3. What is forced (robust)

**The two limits and the geometric mean are not engineered; they are what the cross-term IS.** The cross-term is `√(S_N S_0) = √(g_N² a_0²) = g_N a_0`, and the deep-MOND regime is where it dominates the diagonal `S_N = g_N²`, i.e. `g_N < a_0`:

- **Deep MOND (`g_N ≪ a_0`):** `g² ≈ g_N a_0`, so `g = √(g_N a_0)` — the MOND geometric-mean law, and the geometric mean is exactly the cross-term.
- **Newton (`g_N ≫ a_0`):** `g² ≈ g_N²`, so `g = g_N`.
- **Crossover at `g_N ~ a_0`** (the cross/diagonal ratio is `a_0/g_N`).

Inverting `g² = g_N² + g_N a_0` via `μ(x) = g_N/g`, `x = g/a_0` gives
$$ \mu_{\text{ED}}(x) = \frac{\sqrt{1+4x^2}-1}{2x}, $$
which the probe confirms is **monotone increasing, bounded in `(0,1)`, with `μ→x` (deep) and `μ→1` (Newton)** exactly (`μ/x → 1.0000` at `x=10⁻³`; `μ → 0.9995` at `x=10³`). So a monotone positive interpolation *does* emerge, not by assumption.

## 4. The sign worry, resolved by regime separation (the Paper E gap)

The probe tests coherence models `C(g_N)` that are coherent (`≈+1`) at low acceleration and **sign-indefinite** (oscillating through negative values) at high acceleration, e.g. `C = cos(3 ln(g_N/a_0))` for `g_N > a_0`. In every case:

- `μ →` (high accel) `≈ 1.000` (Newton), **regardless of the sign of `C` there**, because the diagonal `g_N²` dominates and the cross-term (with its sign-indefinite `C`) is subdominant;
- `μ/x →` (low accel) `≈ const` (MOND), where `C ≈ +1` (coherent).

So **the sign-indefinite `cosΔπ` only acts where the diagonal already dominates** (`μ → 1` there whatever the phase does), and where MOND lives (low acceleration, weak gradient) the phase is coherent `≈ +1`. The Paper E worry is not swept under a rug; it is regime-separated: the phase is dangerous only in the regime where it is irrelevant. This is the concrete content of P14's banked "`cosΔπ ≈ 1` in the joint weak-gradient regime."

## 5. What is model-dependent (honest)

The *exact* `μ` shape depends on the strain-to-acceleration mapping (M1). The probe runs two natural mappings:

- **(A) `S ∝ g²`** (field energy): `g² = g_N² + g_N a_0` → `μ_ED = [√(1+4x²)−1]/(2x)`.
- **(B) `S ∝ g`** (linear): `g = g_N + √(g_N a_0)` → a softer curve.

Both hit the **same two limits** (`μ→x` deep, `μ→1` Newton) but differ through the transition (at `x=1`, A gives `0.618`, B gives `0.382`). So the two limits + monotonicity are forced; the transition shape is not. Compared to the data-favored interpolations, `μ_ED` (mapping A) sits **between** the "simple" `x/(1+x)` (RAR-preferred; ED within `0.12` of it) and the "standard" `x/√(1+x²)` (ED within `0.11`), both of which are acceptable for rotation curves. Near the transition `x ~ 1` ED differs from each by up to `~0.12`, so *if* the exact form were pinned (it is not, pending M1), it would be a testable discriminator against the Radial Acceleration Relation. As it stands, ED lands in the viable interpolation family with a specific but model-dependent shape.

## 6. Honest tiers and verdict

- **ROBUST (forced by the cross-term structure):** the cross-term is the geometric mean of squared accelerations `= g_N a_0` = the deep-MOND relation; diagonal dominance = Newton; crossover at `g_N ~ a_0`; a monotone positive `μ(x) ∈ (0,1)` with both correct limits emerges; and the sign-indefinite `cosΔπ` is regime-separated (harmless where it is non-positive).
- **MODEL-DEPENDENT:** the exact `μ` transition shape (the strain→acceleration mapping M1, plus the isotropy-drop M3). Two natural mappings both give valid forms in the simple-standard family.
- **CONDITIONAL:** on the banked, still-**OPEN** quadratic/interfering reading of gravitational strain (P14 step-3: the corpus, via Paper_026, currently builds gravitational strain *linearly*, which has no source-source interference). This is the single load-bearing commitment; nothing here discharges it.

**Verdict.** Given the quadratic-strain reading, the P14 interference cross-term **produces a valid MOND interpolation function**: monotone, positive, bounded, with the correct Newton and deep-MOND limits, and the sign-indefinite-phase obstruction that Paper E flagged is resolved by regime separation (the phase is only sign-indefinite where the Newtonian diagonal already dominates). This **upgrades MOND in ED from "housed in the scalar/khronon sector" to "reproduced with correct limits, with a monotone `μ` shown rather than assumed"** — it closes Paper E's specific gap *conditional on* the quadratic reading. It is **not** a from-nothing derivation of a unique `μ(x)`: the exact transition shape is model-dependent, and the whole result hangs on the unresolved quadratic-strain commitment. Held to the same bar as a negative (per the crank note on the MOND over-read trap): the elegant "interference → MOND-μ" picture is now *demonstrated to be internally consistent and limit-correct*, which it was not before, but it remains a candidate gated on the one open commitment, not a closed result. Connects the scalar/MOND sector of [[project_curvature_emergence_arc]] to [[project_p14_partial_reduction]].
