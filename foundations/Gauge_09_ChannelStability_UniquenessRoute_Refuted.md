# Gauge Program · Step 9 — The Channel-Family Stability Route to {1,2,3} is REFUTED (coherence favors large N)

**Foundations — tests the flagged "next concrete target" of `Gauge_03` §5-6 (the channel-family stability calculation) for the SM gauge-group uniqueness {1,2,3}. Result: it FAILS, and points the wrong way. Both candidate routes for {1,2,3} are now down: the spatial-dimension bound (refuted `Gauge_04`, category error) and coherence-stability (refuted here). The gauge-group FORM (SU(N) from multiplicity, `Gauge_01`) stands; the specific SM group {1,2,3} remains a genuine OPEN WALL — as in standard physics, which also does not derive it. Honest tier: form-derived, specific-group-inherited.**

---

## 1. The question and the state

`Gauge_01` derived the gauge-group *form*: `N` indistinguishable same-rule-type channels + bandwidth conservation (P04) → structure group `U(N)=SU(N)×U(1)`. The SM `U(1)×SU(2)×SU(3)` ↔ channel-family multiplicities `{1,2,3}`. But the framework gives `SU(N)` for *any* `N`; deriving `N≤3` (and the realization of all of {1,2,3}) would be deriving the SM gauge group — which standard physics does not do.

- `Gauge_03` proposed `N ≤ D_spatial = 3` (channels as spatial directions). **`Gauge_04` refuted it** as a category error: `SU(N)` is a *complex-internal* count, not the *real-spatial* `SO(3)`; `N_c=3=D_space` is most likely coincidence.
- `Gauge_03` §5-6 flagged the **stability route** as "the next concrete target": a coherence-stability calculation on N-channel families forbidding `N>3`. This note builds and runs it.

## 2. The stability calculation (P12-native)

A same-rule-type family = `N` channels, amplitudes `a_i` (`b_i=a_i²`), total bandwidth conserved `Σa_i²=B` (P04). The unbroken-`SU(N)` multiplet is the **symmetric** state `a_i=√(B/N)`, phases aligned (mutually coherent). Family stability = this symmetric state is a stable extremum of the P12 landscape `F = −Coh + λ·Str`, with `Coh=Σ_{i<j}a_i a_j` (pairwise coherence) and `Str=Σa_i⁴` (concentration cost).

**Result 1 — the symmetric multiplet is stable for ALL N.** The constrained Hessian (perturbations tangent to `Σa²=B`) at the symmetric point is `Hc = P[(1+12λs²)I − J]P`, whose tangent eigenvalues are `(1+12λs²) > 0` for every `N` and every `λ ≥ 0` (verified `N=2..8`, `evaluation/ChiralGauge/gauge_multiplicity_stability.py`). So the symmetric `SU(N)` multiplet is a genuine minimum at every multiplicity — coherence-stability does **not** bound `N`.

**Result 2 — coherence-binding GROWS with N (the intuition is backwards).** The energy cost to decohere one channel (misalign its phase by `δ`) is `(N−1)·(B/N)·(1−cos δ)`, which *increases* with `N` (0.50 at N=2 → 0.875 at N=8 for `δ=π/2`). More channels ⟹ more pairwise coherence terms binding each channel ⟹ larger families are **harder** to break, not easier. This is general (it is just pair-counting), not an artifact of the chosen `F`. The corpus's hypothesis ("a large-N family may be unstable, the coherence condition harder to maintain," `Gauge_03` §5) is **the reverse of what coherence does**.

## 3. Verdict

**The stability route to {1,2,3} FAILS, and coherence in fact favors large `N`.** Both candidate mechanisms for the SM gauge-group uniqueness are now down:
- spatial-dimension bound — refuted (`Gauge_04`, category error);
- coherence-stability — refuted here (symmetric multiplet stable ∀N; coherence-binding grows with N).

**So the SM gauge-group uniqueness {1,2,3} remains a genuine OPEN WALL in ED.** This is not a failure of the gauge program — the program's real result (the gauge-group **form**: forces are `SU(N)` gauge theories, forced by channel multiplicity + bandwidth conservation, `Gauge_01`) stands and is a genuine derivation. What does not follow is the *specific* group. **Honest tier for the whole channel-topology→gauge program: the gauge-group FORM is derived; the specific SM group {1,2,3} is INHERITED** (the same form-forced / value-inherited pattern as everywhere else in ED). Standard physics also takes the SM gauge group as input; ED reduces "why gauge groups at all / why `SU(N)`" to channel multiplicity, but not "why exactly 1,2,3."

**What would still be needed (honest next, if pursued):** a bound on `N` from something *other* than coherence-stability or spatial dimension — e.g., a transport-realizability constraint (can P05/V5 actually *gauge* — position-dependently mix — more than 3 channels? `Gauge_01` open-piece 3), or an anomaly/consistency constraint tying multiplicity to the matter content. No such mechanism is in hand, and the two natural ones fail. The uniqueness is the hardest target and stays open.
