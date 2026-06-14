# Phase-3 GR — Pinning `λ_J`: the Covariance Escape Is Closed (and the Earlier Identification, Corrected)

**Foundations derivation + build-and-run — the decisive step on the preferred-frame front: is the directed-flux coupling `λ_J` forced by the primitives to the value that makes `α₁ = α₂ = 0` outright? Not a corpus edit, not a new primitive. Sim: `evaluation/DynamicalBandwidth/boost_noncovariance.py`.**

The directed-flux build (`Phase3_GR_DirectedFluxSector.md`) reduced the front to `α₁ ∝ λ_J 𝒮(Γ)` and named the decisive question: does ED's structure lock `λ_J` to the value giving `α₁ = 0`? This note answers it — and the answer is **no, and it cannot, because the same irreversibility (P11) that gives ED its preferred frame forbids it.** It also corrects an identification the earlier notes got wrong.

**Crank rail:** the qualitative result (covariance escape closed) is sim-confirmed and robust; the *magnitude* of `λ_J` (hence how much `𝒮(Γ)` must suppress) is **not** computed here and is not faked. Honest tiers throughout.

---

## 1. The covariant value — what `α₁ = 0` actually requires

`α₁, α₂` are *deviations from Lorentz covariance.* A Lorentz-invariant theory has `α₁ = α₂ = 0` because the momentum density `T^{0i}` and energy density `T^{00}` are one tensor with one locked coupling. The `g_{0i}` such a theory predicts for a mass moving at `w` is just the **boosted static field.** Boosting ED's static metric (`g_{00} = −(1−2U)`, `g_{ij} = (1+2U)δ_{ij}`, `γ=1`) to velocity `w`, to O(wU):

> `g'_{0i} = −w_i(1−2U) + w_i(1+2U) = 4\,w_i U`   *(the standard factor-of-4 gravitomagnetic value).*

So the boost-covariant `g_{0i}` is `4 w_i U`, and:

> **`α₁ = 0  ⟺  ED's directed flux gives `g_{0i} = 4 w_i U`,  i.e. `λ_J = 4` (covariant), NOT `λ_J = 0`.**

**Correction to the earlier notes.** Route B and the directed-flux note identified `λ_J = c₁₄ = −η` directly. That conflated the *coupling* with its *deviation from covariance.* The correct statement is `c₁₄ ∝ (λ_J − λ_J^{cov}) = (λ_J − 4)`: `c₁₄` (which is `0` in the GR/covariant limit) is the **deviation**, and `α₁ = −4c₁₄ ∝ −(λ_J − 4)`. The Route-A/Route-B cross-check is unaffected — Route A's `c₁₄` and Route B's `η` are still the *same* object (the deviation from covariance); we have only sharpened *what* that common object is.

## 2. The decisive test — is ED's rule boost-covariant?

`α₁ = 0` would hold if ED's rule reproduced the boosted-static field. The metric-band rule `ḃ = D∇²b − κρ` is **first order in cosmic time**, so a source moving at `w` gives the comoving convection–diffusion equation `D∇²B + w·∇B = κρ₀`. If ED were boost-covariant, `B` (in comoving coordinates, bulk translation removed) would equal the static field `b_s` (`D∇²b_s = κρ₀`). It does not.

`boost_noncovariance.py` solves both by FFT for a Gaussian source and measures `Δ = B − b_s`:

| `w` | `max\|B − b_s\|` | `/w` (linear?) | dipole(`Δ`)/w |
|---|---|---|---|
| 0 | 0 | — | — |
| 5×10⁻⁴ | 6.26×10⁻² | 125.1 | 120.6 |
| 1×10⁻³ | 1.25×10⁻¹ | 125.2 | 120.6 |
| 2×10⁻³ | 2.51×10⁻¹ | 125.5 | 120.6 |
| 4×10⁻³ | 5.04×10⁻¹ | 126.0 | 120.5 |

> **The moving-source field is *not* the static field: `Δ ≠ 0`, exactly linear in `w`, and `DIPOLAR` along `w` (a fore/aft wake).** A source moving through the cosmic bandwidth medium distorts the field asymmetrically — and that asymmetry cannot be removed by a coordinate change, because the cosmic frame is physical (the khronon background). **ED's rule is not boost-covariant.**

## 3. The result — the covariance escape is closed, and the arrow closes it

Because ED's rule is provably not boost-covariant, **`λ_J` is not locked to the covariant value `4`; `α₁` is not protected to zero by any symmetry.** The hoped-for clean outcome — that the primitives force `α₁ = α₂ = 0` outright — does **not** happen. And the reason is exactly ED's signature:

> **The same P11 irreversibility that defines the arrow defines the cosmic preferred frame, and writing the rule in that frame (first order in cosmic time) is what makes it non-covariant.** The arrow that selects Einstein at the lapse, makes the khronon physical, and pins it to the light cone *also* sources a non-covariant `g_{0i}` — a fourth consequence of the same commitment, and the first one that is a **liability** rather than an asset. The arrow giveth and the arrow taketh: it cannot give ED a preferred frame *and* protect it from preferred-frame effects.

This is a genuine could-have-gone-either-way result, and it came back against the easy escape.

## 4. Magnitude — scoped honestly, not computed

With the covariance escape closed, the size of `α₁` is set by how far `λ_J` sits from `4`, times the dissipative screening:

> **`α₁ ∝ (λ_J − 4)\,𝒮(Γ)`**  — ED safe iff `|λ_J − 4|\,𝒮(Γ) ≲ 2.5×10⁻⁵`.

- The boosted-static (covariant) part `4 w_i U` is kinematic — the metric is a genuine tensor and boosts correctly; this part is the standard frame-dragging and is *not* the danger.
- The **deviation** `(λ_J − 4) w_i U` is the dynamically-generated non-covariant wake measured in §2 — this is what `α₁` sees, and what the dissipative reserve screens.
- A naive co-moving-conservation estimate (the moving concentration's matter current only, missing gravitational field-momentum) gives `λ_J ~ O(1)`, i.e. a deviation `|λ_J − 4| = O(1)` — so the *conservative* `α₁ = O(1)`, far above the bound. **But the precise `λ_J` requires the full vector-sector dynamics (field-momentum included) and is not computed here.** What is certain is that it is not `4`, so the deviation is nonzero.

## 5. Consequence — the burden is now entirely on `𝒮(Γ)`

Since no symmetry zeroes `α₁`, **ED's PPN safety rests entirely on the dissipative screening `𝒮(Γ)`** — which the directed-flux build showed *can* deliver `<10⁻⁴` suppression for a short reserve-drain range (`Γ ≳ 10`, range `≲ 0.1` source-radii). So the front reduces, finally, to a single load-bearing quantity:

> **Is the P11 reserve-drain range near matter short enough that `𝒮(Γ)` suppresses the `O(1)` non-covariant deviation below `2.5×10⁻⁵`?**

The arrow created the problem (the preferred frame) and the arrow's reserve (the same P11 irreversibility, dissipative) is the only thing that can solve it. The whole front now turns on pinning `Γ`.

## 6. Verdict

**Attempting to pin `λ_J` returns a decisive structural result: the covariance escape is closed.** ED's rule is provably not boost-covariant (sim: a moving source produces a dipolar `O(w)` wake, linear in `w`), so `α₁` is not protected to zero by symmetry — and it is the arrow (P11, the cosmic preferred frame) that forecloses the protection, the first time ED's defining commitment acts as a liability. The earlier `λ_J = c₁₄` identification is corrected: `c₁₄ ∝ (λ_J − 4)` is the deviation from the covariant value `λ_J = 4`; the cross-check survives (same object, sharpened). The conservative deviation is `O(1)` (naive `λ_J ~ 1` vs covariant `4`; exact value awaits the full vector dynamics, not faked). **The entire front therefore reduces to one quantity — the reserve-drain range `Γ` — through `α₁ ∝ (λ_J − 4)𝒮(Γ)`, safe iff `|λ_J − 4|𝒮(Γ) ≲ 2.5×10⁻⁵`.** Pinning `Γ` is the last load-bearing step, and it decides ED's preferred-frame fate.

## 7. Next

1. **Pin `Γ(x)`** — the P11 reserve-drain rate near matter (the overdamping range) from the band/commitment structure → evaluate `𝒮(Γ)`. This is now *the* decisive computation.
2. **Compute the exact `λ_J`** from the full directed-flux dynamics (matter current + gravitational field-momentum) → the precise deviation `(λ_J − 4)`. Sets how much suppression `𝒮(Γ)` must supply.
3. **Combine:** `α₁ = (coeff)(λ_J − 4)𝒮(Γ)`, `α₂` (anisotropic) → compare to `10⁻⁴, 10⁻⁷`. Front closes.
4. **Full moving-binary sim** as the `F`-native cross-check.

---

*Pinning `λ_J`: the covariance escape is CLOSED. The boost-covariant `g_{0i}` of a moving mass is `4w_iU` (boosted static), so `α₁=0 ⟺ λ_J=4`, not `λ_J=0` (correcting the earlier `λ_J=c₁₄` identification: `c₁₄ ∝ (λ_J−4)` is the deviation from covariance; cross-check survives, sharpened). Sim `boost_noncovariance.py` shows ED's rule is NOT boost-covariant — a moving source gives a dipolar `O(w)` wake (`Δ=B−b_s ≠ 0`, linear in `w`), unremovable because the cosmic frame is physical. So `α₁` is not symmetry-protected to zero, and it is P11 (the arrow = the preferred frame) that forecloses the protection — the arrow's first liability. Magnitude: `α₁ ∝ (λ_J−4)𝒮(Γ)`; naive co-moving `λ_J~1` ⟹ `O(1)` deviation (exact value needs full vector dynamics, not faked); ED safe iff `|λ_J−4|𝒮(Γ) ≲ 2.5×10⁻⁵`. The whole front now reduces to one quantity — the reserve-drain range `Γ`. No corpus edits, no new primitives; Einstein not derived; the number deliberately not faked.*
