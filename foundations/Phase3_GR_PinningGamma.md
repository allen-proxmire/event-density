# Phase-3 GR — Pinning `Γ`: the Reserve-Drain Range, and the Preferred-Frame Verdict (Leans Safe, Assumptions Flagged)

**Foundations derivation — the last load-bearing step of the `α₁, α₂` front: estimate the P11 reserve-drain range `Γ` near matter and evaluate the screening `𝒮(Γ)`. Not a corpus edit, not a new primitive.**

The `λ_J` note closed the covariance escape: `α₁` is not symmetry-protected, so ED's PPN safety rests entirely on the dissipative screening `𝒮(Γ)`, with `α₁ ∝ (λ_J − 4)𝒮(Γ)`. This note pins `Γ`.

**Crank rail — extra load-bearing here.** Two notes ago I overstated cleanliness and had to correct it. So: this note reaches a *favorable* estimate, and I will flag exactly which assumptions carry it and refuse to upgrade "leans safe" to "safe." A favorable estimate resting on two motivated-but-unproven assumptions is reported as exactly that.

---

## 1. What sets the screening range

The dissipative reserve drains the directed flux near matter, turning the vector Poisson into a screened (Yukawa) equation `(D_J∇² − Γ)A^i = κ_J ρ w^i`, with **screening range `ℓ_scr = √(D_J/Γ)`**. The non-covariant preferred-frame wake is suppressed by `𝒮 ~ exp(−R/ℓ_scr)` at distance `R` from where it is sourced. So everything turns on `ℓ_scr` relative to the source size.

## 2. The substrate values — and the range comes out Planck-scale

From `Phase3_GR_PinningKappaD.md`, the rule's coefficients in substrate terms are

> `D = s_{02}\,c\,ℓ_P`   (P02 adjacency-sharing rate),   `κ = k_{11}\,c/ℓ_P`   (P11 commitment sink rate),

with `s_{02}, k_{11}` dimensionless O(1) band-fractions. The vector sector shares by the *same* P02 adjacency, so `D_J ~ D = s_{02} c ℓ_P`. The flux is drained by the *same* P11 commitment-reserve mechanism that sets `κ`, and near matter — where commitment is *active* (matter is persistent commitment, the reserve runs fast, `Γ_commit ~ b_int/reserve` large) — the drain rate is substrate-fast, `Γ ~ κ = k_{11}\,c/ℓ_P`. Then

> **`ℓ_scr = √(D_J/Γ) = √(\dfrac{s_{02}\,c\,ℓ_P}{k_{11}\,c/ℓ_P}) = √(s_{02}/k_{11})\;ℓ_P ~ ℓ_P`.**

The screening range near matter is the **Planck length**. For any macroscopic body (`R` from microns to a solar radius, `R/ℓ_P ≳ 10^{30}`), the suppression is `𝒮 ~ exp(−R/ℓ_P) ≈ 0` — overwhelmingly complete.

## 3. Why this does not also kill the legitimate frame-dragging (the load-bearing split)

If the screening hit *all* of `g_{0i}`, it would erase the standard gravitomagnetic frame-dragging (`4 w_i U`), which is observed (Gravity Probe B) and must survive. It does not, *if* the following split holds — and this is the load-bearing assumption:

- **Covariant part `4 w_i U`** = the *boost of the static scalar field*. The scalar `b` is **conserved** (P04, redistributed not destroyed), so its steady state is long-range (`∇²b ~ ρ`, unscreened Newton). Its boost — the frame-dragging — is therefore *also* long-range and **unscreened**. Kinematic, not a dissipative response.
- **Non-covariant wake `(λ_J − 4) w_i U`** = the *dynamical khronon flux*, which is **dissipative** (P11 one-way, the `ε = 0` sector). This is what gets drained → screened at `ℓ_P`.

This is precisely the `ε = 0` picture (`Phase3_GR_DerivingEpsilon_KhrononSpeed.md`) applied here: the khronon is overdamped near matter, clean in vacuum. The conserved scalar carries Newton + the correct frame-dragging unscreened; the dissipative khronon carries the preferred-frame wake and is screened to nothing near matter. **The scalar-conserved / vector-dissipated asymmetry is the whole mechanism.**

## 4. The verdict — leans safe, by a wide margin, conditional on §3

Putting it together: `α₁ ∝ (λ_J − 4)\,𝒮(Γ)` with `(λ_J − 4) = O(1)` and `𝒮 ~ exp(−R/ℓ_P) ≈ 0`, so

> **`α₁ ≈ 0`, `α₂ ≈ 0` — ED is PPN-safe, with the standard frame-dragging preserved (unscreened conserved-scalar boost) and MOND preserved (in vacuum/weak-field `Γ → 0`, the khronon is unscreened and operates freely).**

Consistent, and the same `ε = 0` dissipation does triple duty: keeps the khronon at `c` (vacuum), overdamps it near matter (no second cone), and now screens the preferred-frame near-field. The observable khronometric signature survives where it should — the *vacuum* scalar gravitational-wave polarization at `c` — while the dangerous near-field preferred-frame effects are screened away.

## 5. Honesty — the two assumptions carrying the verdict

This is a favorable result; here is exactly what it rests on, neither hidden nor oversold:

1. **`Γ ~ κ ~ c/ℓ_P` near matter** — that the flux is drained by the commitment-reserve at the same substrate-fast rate that sets the scalar sink. Motivated (same P11 mechanism, commitment active near matter), but an order-of-magnitude estimate, not a derived coefficient. If the flux drain were instead macroscopically slow, `ℓ_scr` would be large and `𝒮 ~ 1` — back to danger. The verdict is *not* robust to `Γ` being many orders smaller than `κ`.
2. **The covariant / non-covariant split of §3** — that only the dissipative khronon flux is screened while the conserved-scalar frame-dragging is spared. Strongly motivated (the scalar is conserved, the khronon dissipative — the established `ε = 0` asymmetry), and *required* for consistency with observed frame-dragging, but not a line-by-line derivation. If the screening bled into the covariant part, ED would mispredict frame-dragging instead.

Both assumptions point the same way and are grounded in already-established ED structure, but they are assumptions. **Having just corrected an over-optimistic step, I state this as "ED leans PPN-safe, strongly, conditional on two motivated assumptions" — not "ED is PPN-safe."**

## 6. Verdict

**Pinning `Γ` gives a favorable estimate: the reserve-drain range near matter is `~ ℓ_P` (Planck-scale), so the non-covariant preferred-frame wake is screened to essentially zero (`𝒮 ~ exp(−R/ℓ_P)`), giving `α₁ ≈ α₂ ≈ 0` — ED PPN-safe, with frame-dragging (unscreened conserved-scalar boost) and MOND (vacuum, `Γ→0`) both preserved, and the vacuum scalar-GW signature intact.** This rests on two flagged assumptions — `Γ ~ κ` near matter (substrate-fast drain) and the conserved-scalar/dissipative-khronon split — both grounded in established structure (the rate law; the `ε = 0` asymmetry) and consistency with observed frame-dragging, but neither a rigorous derivation. **So the honest standing is: the front is no longer wide open — the mechanism is identified, the estimate lands safe by a wide margin — but it is "leans safe, assumptions flagged," not "closed safe." The remaining work is to firm those two assumptions (a clean derivation of `Γ` near matter, and a proof that the screening spares the covariant sector), or, decisively, to measure `α₁` directly in a moving-binary `F`-simulation.** No number is fabricated; `(λ_J − 4)` and the exact `𝒮` remain order-of-magnitude.

## 7. The whole front, summarized

| step | result |
|---|---|
| Route A | `α₁ = α₂ = 0 ⟺ α = 2β`; ED `c_T=c ⟹ β=0`; reduced to `c₁₄` |
| Route B | `α₁` from the directed-flux normalization `η`; boost-non-invariance is the engine |
| `η` cross-check | scalar rule curl-free → cross-term needs the vector sector (Route A `c₁₄` = Route B `η` = its coupling) |
| vector sector built | `g_{0i} = λ_J w_iU` long-range; cross-check holds; screening `𝒮(Γ)` real |
| pin `λ_J` | covariant value is `λ_J=4`; ED not boost-covariant ⟹ `α₁` **not symmetry-protected** (the arrow's first liability); reduced to `Γ` |
| **pin `Γ`** | **range `~ℓ_P` ⟹ `𝒮≈0` ⟹ `α₁≈0`: leans PPN-safe, two assumptions flagged** |

## 8. Next (to firm or falsify)

1. **Derive `Γ(x)` near matter** rigorously from the P11 commitment/reserve profile (replace the `Γ ~ κ` estimate with a coefficient).
2. **Prove the covariant sector is spared** — show the screening acts only on the dissipative khronon flux, not the conserved-scalar boost (firm the §3 split).
3. **Moving-binary `F`-simulation** — the decisive `F`-native measurement of `α₁, α₂` with both sectors and the reserve drain present, bypassing the analytic assumptions entirely.

---

*Pinning `Γ`, the last load-bearing quantity. Screening range `ℓ_scr = √(D_J/Γ)`; with `D_J ~ D = s_{02} c ℓ_P` and the near-matter drain `Γ ~ κ = k_{11} c/ℓ_P` (commitment active near matter), `ℓ_scr ~ √(s_{02}/k_{11}) ℓ_P ~ ℓ_P` — Planck-scale. So the non-covariant preferred-frame wake is screened by `𝒮 ~ exp(−R/ℓ_P) ≈ 0`, giving `α₁ ≈ α₂ ≈ 0`: ED leans PPN-safe by a wide margin, with frame-dragging (unscreened conserved-scalar boost) and MOND (vacuum, Γ→0) preserved and the vacuum scalar-GW signature intact. CONDITIONAL on two flagged assumptions: `Γ ~ κ` near matter (substrate-fast drain, rate-law-motivated) and the conserved-scalar/dissipative-khronon split (the ε=0 asymmetry; required for consistency with observed frame-dragging). Both grounded, neither airtight — reported as "leans safe, assumptions flagged," NOT "closed safe," having just corrected an over-optimistic step. Firm by deriving Γ + proving the split, or measure α₁ in a moving-binary sim. No corpus edits, no new primitives; Einstein not derived; the number not faked.*
