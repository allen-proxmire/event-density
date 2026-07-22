# The constants ledger, why G is weird, and where the dimension actually lives in G

**Working note, 2026-07-21 (event-density). Research/riff stage — candidate for a later EDG essay or paper if it firms up.** Grew out of a free-writing session: which fundamental constants are present at the "first events" vs. inherited later; why Newton's `G` feels un-fundamental; and a decidable sub-question — in `G = c³ℓ_P²/ħ`, does the `c³` or the `ℓ_P²` carry the spatial-dimension dependence? Answer computed below. Tiers marked throughout.

## 1. The constants ledger — what's present when

**At the first events (co-arise with the first flux / light) — the constants of a *single event*:**
- **c** — the *rate of becoming* (P-RB-1): the tick-to-hop conversion. Present as soon as one event influences a neighbor.
- **ħ** — the *action of one commitment*: how much "happens" in a single tick.
- **ℓ_P** (= ℓ_ED, P08) — the *grain*: the size of one hop.

These three are **dimensionful** — a clock, an action, a ruler. In natural units they are all **1**. So the beginning carries **units, not numbers.**

**Inherited / late (need the cosmos or matter to have accumulated):**
- **a₀ = cH₀/(2π)** (Paper_029) — needs a Hubble horizon; so late it *evolves* (a₀(z)). Same for **Λ**, **H₀**.
- **particle masses, couplings, α ≈ 1/137, mass ratios** — the matter sector (bound `b`), openly inherited; the unfinished room.

The physics-defining *dimensionless* numbers are the universe's late-acquired personality. *(Caveat: not literally number-free — the integer `d` for dimensions, graph coordination, maybe kernel exponents live in the bare rule; but the continuous physics-constants are late.)*

## 2. The trio, read as becoming / memory / extent

- **c = becoming** (the forward step, the rate of the arrow).
- **ħ = the grain of memory.** `ħ` bridges action and phase (`phase = S/ħ`), and the phase is precisely what a quantum system *remembers* (interference = memory of both paths; decoherence = forgetting). `ħ` is the pixel size of remembering — small enough to store a record, and you can't resolve beneath it (that bound *is* `ΔxΔp ≥ ħ/2`). Parallel: **ℓ_P is the grain of space, ħ is the grain of memory.** Bottoms out in ED: commitment (P11) forbids erasure, so a commitment is a permanent record, and `ħ` = the action-cost of laying down one record. The soft (reversible) phase-memory becomes hard (irreversible) memory when the accumulated action crosses `ħ` — the state-reduction threshold read as a memory event.
- **ℓ_P = extent** (the room).

The going, the keeping, the room. `c` and `ħ` co-arise as the two poles of one event: an event that left no trace wouldn't be an event. *(Tier: interpretive framing, grounded in the phase/commitment structure; not a theorem.)*

## 3. Why G is weird (three real reasons)

1. **G is a combination, not an input.** `G = c³ℓ_P²/ħ` (Paper_027 §5.2). Given the three event-scales, gravity's strength is fixed — it adds no new information.
2. **G appears *nowhere but gravity*.** `c` is universal (relativity, EM, every field); `ħ` is universal (all QM). **G is absent from the entire Standard Model** — no G in QED, QCD, electroweak. It shows up only in gravity and the Planck units. A constant that governs one "force" and appears nowhere else is a tell that the force is not fundamental — which is exactly ED's claim (gravity is emergent, `g ~ 1/b`, not a fundamental field).
3. **G is the exchange rate between two *separately coarse-grained* things** — mass (bound `b`) into curvature (`g ~ 1/b`). It lives at the seam of two coarse-grainings (the matter CG and the geometry CG), a conversion factor between two shadows, not a property of the substrate.

**Resolution of the paradox (G is un-fundamental yet the *first* emergent): G is the first *shadow*, not the first thing.** It's first out the door precisely because it's nothing new — just c, ħ, ℓ_P rearranged at the first seam where mass meets geometry. Least fundamental and first-emergent are one fact. *(Tier: synthesis, grounded.)*

## 4. The decidable question: does c³ or ℓ_P carry the dimension? — ℓ_P does.

**Claim under test:** the `3` in `c³` encodes the `3` of 3D. **Verdict: no.** Dimensional analysis in `d` spatial dimensions:

`[G_d] = m^d · kg⁻¹ · s⁻²` (Poisson `∇²Φ = 4πGρ`, with `ρ` = mass per `d`-volume). Write `G_d = c^a ℓ_P^b ħ^e`:

| dimension | equation | result |
|---|---|---|
| kg | `e = −1` (ħ is the only mass-carrier) | `e = −1` |
| s | `−a − e = −2` | **`a = 3` (all d)** |
| m | `a + b + 2e = d` → `3 + b − 2 = d` | **`b = d − 1`** |

$$\boxed{\;G_d = \dfrac{c^{3}\,\ell_P^{\,d-1}}{\hbar}\;}\qquad (d=3:\ G=c^3\ell_P^2/\hbar\ \checkmark)$$

**The c-power is 3 in *every* dimension.** It is pinned by *time/mass* bookkeeping, not space: `G` carries `s⁻²`, `ħ` (forced to power `−1` to supply `kg⁻¹`) drags in `s⁺¹`, so `c` must supply `s⁻³` → `c³`. The `3` in `c³` is a *time* count (`G`'s 2 + `ħ`'s 1), an ironic `2+1` that has nothing to do with the `3+1` of spacetime. **So "c³ = 3D" is a coincidence — drop it.**

**The spatial dimension lives entirely in `ℓ_P^{\,d-1}`.** And `d−1` is not random: it is the **holographic area exponent**. The substrate source distributes over the `(d−1)`-surface (`N(R) ~ R^{d−1}/ℓ_P^{d−1}`, Paper_027 §3), the surface tiled by grains of size `ℓ_P^{d−1}`. So `ℓ_P^{d−1}` in `G` *is* the holographic area-element.

**Consequence — this is *not* a new independent road to 3D.** The dimension-signature in `G` (`ℓ_P^{d−1}`) is the **same holographic/area-law structure** that `Paper_MetricFromTheGraph` already uses to select 3D (bandwidth = boundary cut `~ R^{d−1}`; only `d=3` gives `g ~ 1/b`). So `G` *does* carry the dimension — but through its area-law factor, which is the reach-law road wearing a constant's clothes, not a fourth witness. Honest: it reinforces the holographic road; it does not add to the count.

*(What the naive `c³` hope got right, salvaged:* **`G`'s *units* still encode `d`** — `[G_d] = m^d…`, so `G` remains the first constant whose units know the dimension count. That insight stands; it just lives in `ℓ_P^{d−1}`, not `c³`.)*

## 5. "Cheap Physics"
The beginning needs only three numbers — really just units (c, ħ, ℓ_P, all = 1) — and the first thing it produces (`G`) is free, a rearrangement that adds nothing. The dimensionless zoo is inherited later, with matter and cosmos. The universe **starts nearly free and grows expensive.** Cheap postulates, rich payoff, told through the constants.

## 6. Tiers
- Constants ledger (c/ħ/ℓ_P present; a₀/Λ/masses late) — **grounded** (P-RB-1; P08; Paper_027; Paper_029; masses inherited).
- `G = c³ℓ_P²/ħ`, `G` absent from the SM, `[G_d] = m^d` — **solid** (corpus + dimensional analysis).
- `G_d = c³ℓ_P^{d−1}/ħ`; c-power dimension-blind; dimension in `ℓ_P^{d−1}` = holographic area — **derived** (dimensional analysis; the `ℓ_P^{d−1}` ↔ area identification uses Paper_027 §3).
- "The dimension-signature in G is the holographic reach-law road, not a new one" — **grounded synthesis** (ties Paper_027 §3 to Paper_MetricFromTheGraph).
- ħ-as-grain-of-memory, becoming/memory/extent, G-as-first-shadow — **interpretive framing**, grounded but not theorems.

## 7. Path forward
If this firms up, the essay/EDG-paper spine is: **the constants sort into event-scale (present, dimensionful, ≈ units) vs. accumulated (inherited, dimensionless, the universe's personality); `G` is the first shadow at the seam; and its lone dimensional fingerprint is the holographic area-law, not the speed of light.** The one genuinely computable result here (`G_d = c³ℓ_P^{d−1}/ħ`, c-power dimension-blind) is small but clean and worth stating. Open: whether Paper_027's `d`-dimensional derivation introduces any dimensionless `d`-dependent factor beyond the powers (it shouldn't change the power result, but worth a full pass).
