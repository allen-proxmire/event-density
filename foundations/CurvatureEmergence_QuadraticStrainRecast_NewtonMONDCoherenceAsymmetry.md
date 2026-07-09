# The Quadratic-Strain Recast: Newton (Diagonal) and MOND (Off-Diagonal) Coexist via a σ²-vs-σ Coherence Asymmetry

**Foundations, gravity / curvature-emergence arc. Takes on P14's flagged high-stakes target: recast gravitational strain as a quadratic form `S = |Σ P|²` with Newton = diagonal and MOND = off-diagonal, which must reproduce Newton + the GR-I weak field and break nothing. Probe: `evaluation/CurvatureEmergence/quadratic_strain_recast_probe.py`. RESULT: the naive recast FAILS a real obstruction (one phase-randomness setting kills both Newton-safety and MOND), and that obstruction is RESOLVED by a coherence asymmetry: a small universal phase alignment `σ` toward the horizon reference makes local-local coherence `= σ²` (Newton-breaking, quadratically suppressed) while local-horizon coherence `= σ` (MOND, linear), so Newton survives to `O(σ²)` and MOND survives at `O(σ)`. HONEST: the `σ²`-vs-`σ` asymmetry is an EXACT probability identity (robust); the diagonal = additive Newton is definitional; but the whole thing is CONDITIONAL on (Q1) the quadratic-strain reading itself (the open fork; the corpus builds strain linearly) and (Q2) the small horizon-aligned phase bias `σ` (account-tier, motivated not derived; `σ` sets `a_0`, inherited), and it predicts a falsifiable `O(σ²)` source-source correction to Newton. VERDICT: P14 is SUBSTANTIALLY de-obstructed, NOT fully discharged. The recast now demonstrably reproduces Newton + MOND given one motivated assumption, converting "does it even work?" into a sharp testable residual. Crank-railed hard (MOND is a documented over-read trap, see [[project_p14_partial_reduction]]); this is an admissibility result, not a closed derivation.**

---

## 1. The recast, and the diagonal that is Newton by construction

Represent each gravitational source by a participation amplitude `P_i = √b_i · e^{iπ_i}` (bandwidth `√b_i`, phase `π_i`). The linear (Paper_026) construction sums bandwidths, `S = Σ_i b_i`, giving additive Newton (`Φ ∝ Σ GM_i/R_i`). The **quadratic recast** takes the strain to be the squared total amplitude (Born-like):
$$ S = \Big|\sum_i P_i\Big|^2 = \underbrace{\sum_i |P_i|^2}_{\text{diagonal}} + \underbrace{\sum_{i\neq j} P_i^* P_j}_{\text{off-diagonal}} = \sum_i b_i + \sum_{i\neq j}\sqrt{b_i b_j}\,\cos(\pi_i-\pi_j). $$
The **diagonal `Σ_i b_i` is exactly the additive Newtonian strain** (definitional: the diagonal of the quadratic form *is* the linear sum), and a probe confirms the split numerically. So Newton is present by construction; the question is entirely about the off-diagonal (interference) part, which must give MOND without spoiling Newton.

## 2. The obstruction (confronted, not skipped)

The off-diagonal must do two opposite things:
- **Local-local** cross terms (interference between distinct nearby masses) must **vanish**, or the solar system would show anomalous source-source interference forces, which are not observed (Newton holds to `~10⁻⁸`).
- **Local-horizon** cross terms (interference of the local field with the cosmic horizon) must **survive**, to give MOND.

A single "the phases are random" mechanism kills **both**. If local phases are random enough to wash out local-local interference (`⟨cos(π_i-π_j)⟩ → 0`), they are equally random against the horizon (`⟨cos(π_i-π_{hor})⟩ → 0`), so MOND dies too. The probe demonstrates this: uniform-random phases give both coherences `≈ 0`. Full coherence is the opposite failure: local-local `≠ 0` breaks Newton. **So the naive recast fails**, along the whole coherence axis. This is exactly the kind of hidden contradiction that sinks an "elegant unification," and it is the make-or-break the P14 note demanded be met.

## 3. The resolution: a σ²-vs-σ coherence asymmetry

Give the local participation phases a **small common bias `σ` toward the horizon reference** (phase 0). The horizon is the global boundary in which all local participation is embedded, so a weak universal alignment is a natural common reference, not an arbitrary tuning. For phases with mean resultant `σ = |⟨e^{iπ}⟩|`, two exact probability identities hold (independent `i, j`):
$$ \underbrace{\big\langle\cos(\pi_i-\pi_j)\big\rangle_{i\neq j} = |\langle e^{i\pi}\rangle|^2 = \sigma^2}_{\text{local-local (Newton-breaking)}}, \qquad \underbrace{\big\langle\cos(\pi_i-0)\big\rangle = \langle\cos\pi\rangle = \sigma}_{\text{local-horizon (MOND)}}. $$
The probe confirms both to three decimals across `σ ∈ [0.025, 0.81]` (e.g. `σ=0.0995`: measured `C_LH=0.0992`, `C_LL=0.0099≈σ²`). **The Newton-breaking local-local term is quadratically suppressed relative to the MOND-giving local-horizon term.** So a small `σ` preserves Newton to `O(σ²)` while MOND survives at `O(σ)`. This is the mechanism the naive recast lacked, and it is an exact identity, not a fit.

## 4. Coexistence, the regime condition, and the falsifiable prediction

Assembling the strain (equal local sources `b`, `n_body` separate masses, horizon bandwidth `b_hor`):
- **Local-local / diagonal `~ σ²(n_body − 1)`** — the Newton-breaking correction, quadratic in `σ`.
- **Local-horizon / diagonal `~ σ √(b_hor/b)`** — the MOND term.

The two **decouple** because the horizon bandwidth `b_hor` is astronomically larger than any local `b`: `√(b_hor/b)` is enormous, so a *tiny* `σ` (set by requiring the MOND term to be the observed `a_0`) already gives the full MOND effect, while the same tiny `σ` makes the Newton violation `O(σ²)` utterly negligible. `a_0` is thus set by `σ√(b_hor)` (inherited, not derived), and the residual Newton violation is `O(σ²)`. This is a **falsifiable prediction**: the recast predicts a small `O(σ²)` source-source interference correction to Newton, whose size (once `σ` is fixed by `a_0` and `b_hor`) must sit below solar-system bounds. The strong-field limit is separately safe: when `g_N ≫ a_0` the local-horizon cross-term is `≪` the diagonal, so Newton is recovered regardless (the `μ(x)` crossover, companion probe `p14_interference_to_mond_mu_probe.py`).

## 5. What this does and does not settle (honest tiers)

- **Diagonal = additive Newton: definitional/exact.** GR-I weak field (`g~1/b`) is the diagonal, from the kinematics paper, preserved.
- **The `σ²`-vs-`σ` asymmetry: an exact probability identity.** The resolution of the Newton-vs-MOND deadlock is robust: it is arithmetic, not a model choice.
- **Off-diagonal local-horizon = MOND: the companion `μ(x)` result** (monotone, correct limits), conditional on the same reading.
- **CONDITIONAL / OPEN:**
  - **(Q1) The quadratic-strain reading itself** is the open fork. The corpus (Paper_026) builds gravitational strain *linearly*; taking it to be `|Σ P|²` (Born-like, interfering) is the un-discharged commitment. Nothing here derives it; this note shows the recast is *admissible* if it is granted.
  - **(Q2) The small horizon-aligned phase bias `σ`** is account-tier: motivated (horizon as the global common reference), not derived from the primitives; its value is inherited (it sets `a_0`).
  - **Unchecked consistency:** whether a universal phase alignment `σ` toward the horizon disturbs the QM / gauge phase sector (P09's `U(1)` polarity, the double-slit and gauge results). A universal common phase reference could interact with the gauge freedom; this is not checked and is a flagged open item.
  - **Regime + falsifier:** the `O(σ²)` source-source Newton correction is a real, testable consequence (and a potential falsifier).

**Verdict.** The quadratic-strain recast is **admissible**: it reproduces Newton (diagonal, exact) and the GR-I weak field, gives MOND (off-diagonal, the `μ(x)`), and, crucially, **survives the obstruction that kills the naive version** — the Newton-vs-MOND coherence deadlock is broken by the `σ²`-vs-`σ` asymmetry of a small universal phase alignment toward the horizon. This is the first demonstration that the recast can actually work rather than break Newton. It **substantially de-obstructs P14** but does **not** fully discharge it: it remains conditional on the open quadratic-strain fork (Q1) and the account-tier horizon-alignment (Q2), it leaves the QM/gauge consistency unchecked, and it predicts a falsifiable `O(σ²)` Newton correction. Held to the crank-rail (MOND is a documented over-read trap): this is an admissibility-and-mechanism result, converting "does the recast even work?" into "it works given one motivated phase-alignment assumption, with a sharp testable residual," not a closed derivation of MOND. Connects [[project_p14_partial_reduction]] to the scalar/MOND sector of [[project_curvature_emergence_arc]].
