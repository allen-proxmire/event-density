# Phase-3 GR — The Λ Ab-Initio Integral: Sign and Structure Confirmed, Magnitude IS the Λ-Smallness Problem

**Foundations computation — the open derivation flagged in KM-II / KM-Round-7: compute the V1 vacuum boundary integral *from scratch* and check it gives `𝒲₀ = −24π²Ω_Λ`. Not a corpus edit, not a new primitive. The honest outcome is that the magnitude is the Λ-smallness problem — and it is NOT faked.**
KM-Round-7 *matched* the khronon's EFT vacuum constant to Paper_038.5's substrate-level V1 integral, getting `𝒲₀ = −24π²Ω_Λ` at the value-inherited tier. The named open derivation was the **ab-initio** evaluation of the V1 integral — does it land on that number without inheriting the observed value? This note performs it to the point where it stops, honestly.
**Crank rail (load-bearing here):** the Λ-smallness magnitude is the corpus's flagged *think-don't-chase* / `Θ_ED ≈ 10⁻¹²²` problem. Do **not** fabricate a number. Confirm what the ab-initio integral *does* fix (sign, structure, scaling) and state plainly that the magnitude reduces to the open Route-A closure.

---

## 1. The integral

Paper_038.5: `Λ ∝ ∫_{R_H³} ρ_{\rm vac,V1}(x)\,d³x`, with the V1 vacuum density

> `ρ_{\rm vac,V1} = \tfrac12 \displaystyle\int \frac{d³k}{(2π)³}\,ω_k\,|\hat K_{V1}(k)|²`,  `ω_k = c|k|`,

finite because the V1 form factor `\hat K_{V1}` cuts off at a substrate scale `ℓ`. Evaluating with a model finite-width retarded form factor `\hat K_{V1}(k) = e^{-(kℓ)²/2}` (numeric = analytic, `evaluation/DynamicalBandwidth/`):

> `ρ_{\rm vac,V1} = \dfrac{c}{8π²\,ℓ⁴}` — finite, **positive**, `∝ 1/ℓ⁴`.

## 2. What the ab-initio integral fixes

- **Sign — `Λ > 0` (de Sitter), confirmed ab-initio.** `ρ_{\rm vac,V1} = \tfrac12\int ω|K|² ≥ 0` is positive-definite by construction, so `Λ > 0`. (KM-R7 got the sign by matching; here it is read directly off the integral — the same result, from the substrate side.)
- **Structure — finite, no mode-tower divergence.** The V1 form factor regulates the integral at `ℓ`; there is no UV divergence (Paper_038.5's point, confirmed). The naïve QFT `M_P⁴` divergence is structurally absent.
- **Scaling — `ρ_Λ ∝ 1/ℓ⁴`.** The magnitude is set *entirely* by the cutoff/evaluation scale `ℓ`.

## 3. Where it stops — the magnitude is the Λ-smallness problem

The whole Λ question is **which scale `ℓ`**:

- **`ℓ = ℓ_P` (the naïve substrate-UV cutoff):** `ρ_Λ ∼ c/ℓ_P⁴ ∼ M_P⁴` — the **Planck density**, wrong by `∼ 10¹²²` (Paper_038.5 §3.4 preserved this exact failure; the cosmological-constant problem).
- **`ℓ = ℓ_{V5}(H₀)` (the substrate-cosmology boundary memory scale):** gives `ρ_Λ ∼ H₀²M_P²` — the **observed** value — *if* `ℓ_{V5}(H₀)` is the substrate-derived boundary scale. **But that is exactly Route A** (Paper_038.5's RA-OPEN frontier; `Θ_ED ≈ 10⁻¹²²`).

> **The ab-initio integral reduces, for its magnitude, to the choice of `ℓ` — which is the substrate-derived `ℓ_{V5}(H₀)` (Route A), the corpus's named highest-leverage open derivation and the Λ-smallness / `10⁻¹²²` problem.** The integral fixes the **sign** (`+`, de Sitter) and the **structure** (finite, `∝ 1/ℓ⁴`) ab-initio; it does **not** fix the magnitude without the Route-A scale, and that magnitude is the deepest open problem in the corpus, flagged **think-don't-chase**. So `𝒲₀ = −24π²Ω_Λ` is **not** producible ab-initio here — and is not fabricated.

## 4. Verdict

**The ab-initio V1 boundary integral confirms the sign and structure of Λ from the substrate, and locates its magnitude precisely as the Λ-smallness problem — which it does not solve and does not fake.** The integral is finite (V1 form factor regulates), positive (`Λ > 0`, de Sitter), and scales as `1/ℓ⁴`, so the entire magnitude rides on the evaluation scale `ℓ`. With the naïve `ℓ_P` it gives the Planck density (the `10¹²²` cosmological-constant problem, Paper_038.5's preserved failure); with the substrate-cosmology boundary scale `ℓ_{V5}(H₀)` it gives the observed `H₀²M_P²` — but that scale is **Route A**, the corpus's named open frontier and the `Θ_ED ≈ 10⁻¹²²` think-don't-chase result. So the ab-initio computation does what it honestly can — sign and structure, confirming KM-R7's matched values from the substrate side — and stops at the magnitude, which is the deepest open problem, deliberately not chased.

**This is the right kind of "no":** not a failure of the construction, but the correct identification that the one remaining number is the cosmological-constant smallness problem itself — which the program has, from the start, flagged as value-inherited-in-principle and not a derivation target. KM-R7's `𝒲₀ = −24π²Ω_Λ` stands at its value-inherited (D-via-I) tier; the ab-initio route confirms it is *consistent* (sign, scaling) but cannot *derive* the magnitude without Route A.

---

*The Λ ab-initio integral. The V1 vacuum boundary integral is finite (`ρ_{\rm vac,V1} = c/8π²ℓ⁴`, model form factor; numeric = analytic), positive (`Λ > 0`, de Sitter — confirmed ab-initio, matching KM-R7's matched sign from the substrate side), and scales as `1/ℓ⁴` — so its magnitude is set entirely by the evaluation scale `ℓ`. With `ℓ_P` it gives the Planck density (the `10¹²²` CC problem, Paper_038.5's preserved failure); the observed `H₀²M_P²` needs the substrate-cosmology boundary scale `ℓ_{V5}(H₀)`, which is Route A — the named open frontier and the `Θ_ED ≈ 10⁻¹²²` think-don't-chase result. So `𝒲₀ = −24π²Ω_Λ` is confirmed in sign/structure but NOT derivable ab-initio without Route A, and is not faked. The magnitude is the Λ-smallness problem itself. No corpus edits, no new primitives.*
