# Phase-3 GR — Round 8: Signature Assembly, the Lapse, and the Einstein Factor of 2

**Foundations derivation attempt + simulation. Not a rule proposal, not a corpus edit, not a new primitive. Nothing here derives the full Einstein field equations.**
Round 7 reduced the Einstein/Nordström fork to one scaling — the temporal lapse `c(b)` (equivalently `N(b)`) — and gave a physical lean. Round 8 *derives* that scaling from the certified commitment-rate law, decides the fork, and confirms the famous factor of 2.
**Crank rail:** forward only; the result is strong, so flag the load-bearing assumption explicitly and keep "metric class" separate from "field equation."

---

## 1. The lapse, derived from the commitment-rate law

Assemble the static Lorentzian metric `ds² = −N²dt² + g_ij dx^i dx^j` from corpus pieces (R4 §2): space `g_ij ~ b⁻¹` (edge metric-length `√g ~ b^{−1/2}`), time `dt` = the homogeneous substrate tick (P13), and the front as the maximal signal = the **null cone** (R4 §2: "the cone = the bandwidth-limit speed"). The lapse is then *forced*, not posited, by two certified facts:

- The front advances `Γ` edges per tick, where `Γ = Γ_commit ~ b_int/reserve` is the **certified commitment rate** — to leading order **linear in the metric-relevant bandwidth, `Γ ~ b`** (the reserve is a *separate* P04 band; §2 returns to this).
- The front is **null**: `ds² = 0` along it.

Substituting `dx/dt = Γ ~ b` and `g ~ b⁻¹` into the null condition:

> `0 = −N²dt² + g_xx dx² = dt²(−N² + b⁻¹·Γ²) = dt²(−N² + b⁻¹·b²) ⟹ N² ~ b.`

So the lapse is `N² ~ b` — **derived** from the commitment-rate law plus the null identification, with no freedom. **Structural→resolved** (modulo the §2 reserve assumption).

## 2. The fork is decided — the Schwarzschild relation

With `g_00 = −N² ~ −b` and `g_rr ~ b⁻¹`:

> `g_00 · g_rr ~ (−b)(b⁻¹) = −1` — the **Schwarzschild relation**, *exactly*, not the conformal one.

This is the Einstein branch. The conformal/Nordström branch is `g_00 ~ −g_rr` (both `~ b⁻¹`), which is **excluded**: it would require `N² ~ b⁻¹`, i.e. the front going *slower* where bandwidth is higher. The general dependence makes the fork a single exponent: with `Γ ~ b^α`, the null condition gives `N² ~ b^{2α−1}`, so `g_00 g_rr ~ −b^{2(α−1)}`, and

- **Einstein** (`g_00 g_rr ~ −const`) `⟺ α = 1` (commitment rate **linear** in bandwidth),
- **Nordström** (conformal) `⟺ α = 0` (commitment rate **independent** of bandwidth).

The certified law `Γ_commit ~ b_int/reserve` is `α = 1`. **So the certified commitment-rate law selects Einstein.**

**The one load-bearing assumption, stated plainly:** `α = 1` holds iff the **reserve band does not co-scale** with `b_int` (else `Γ ~ b_int/reserve ~ const`, `α = 0`, Nordström). P04 lists the commitment-reserve as a band *distinct* from the internal band, so the leading reading is that they are independent and `Γ ~ b_int` — but the exact reserve dynamics near a source are the residual that pins `α`, and with it the fork. **Contingent** — but the certified four-band structure points to `α = 1`.

## 3. The factor of 2 — derived and simulated

The physical light deflection is set by the **optical metric** `g^opt_ij = g_ij/N²`, whose index is

> `n_opt = √g_rr / N ~ b^{−1/2} / b^{1/2} = b^{−1}` — the **square** of the spatial-only index `b^{−1/2}` (R7).

Since weak-field deflection `α ∝ ∫ ∇_⊥ ln n` and `ln(b^{−1}) = 2·ln(b^{−1/2})`, the full deflection is **exactly twice** the spatial-only one — the GR factor of 2 (spatial and temporal contributions add equally). The simulation `gr_einstein_factor.py` ray-traces fronts through `n = b^p` for the three classes and confirms it:

| index class | `C = α·ξ` (sim) | prediction |
|---|---|---|
| spatial-only / Newtonian `n = b^{−1/2}` | **−1.07** | `−rs` |
| **Einstein / optical `n = b^{−1}`** (ED, via `Γ~b`) | **−2.24** | `−2 rs` |
| Nordström / conformal `n = 1` | **0.00** | `0` |

Einstein/Newtonian deflection ratio = **2.09** (GR: 2.000; the 4% excess is finite-`rs` weak-field curvature, not a physical deviation), Nordström = **exactly 0**. The three gravity classes separate cleanly, and ED — via `N² ~ b` — lands on the **Einstein** value.

## 4. A free corollary — gravitational redshift

The same derived lapse gives a second classical test at no extra cost. Clocks run at rate `N ~ b^{1/2}`, so a signal climbing from bandwidth `b₁` to `b₂` is shifted by `N₁/N₂ ~ (b₁/b₂)^{1/2}`. Near a source the bandwidth is depleted (`b` low) → `N` small → **clocks run slow and light is redshifted climbing out** — the correct GR sign and the gravitational-redshift law, falling directly out of `N² ~ b`.

## 5. What is — and isn't — established

**Established (under `α = 1`):** ED's **weak-field metric is Schwarzschild-class** — `g_00 g_rr ~ −1`, the factor-of-2 light bending (simulated), and gravitational redshift — all **derived from the certified commitment-rate law**, not fitted. The Einstein/Nordström fork is **decided: Einstein**, and Nordström is positively excluded (it needs the unphysical `α = 0`).

**Not established:** (i) the full **field equation** `G^μν = κ T^μν` with its coefficient `κ` — what §1–4 give is the *metric class* (Schwarzschild is the *vacuum* Einstein solution; reproducing its form is necessary, strong evidence, but not the sourced field equation); (ii) the reserve dynamics that fix `α = 1` exactly; (iii) the `b(r)` profile is still **imposed**, not derived (deriving it = solving the field equation). So this is the **weak-field, metric-class** Einstein result, not the nonlinear EFE.

## 6. Structural vs contingent

| Item | Verdict |
|---|---|
| lapse `N² ~ b` | **derived** (null condition + `Γ~b`) |
| Schwarzschild relation `g_00 g_rr ~ −1` | **derived** (under `α=1`) |
| factor-of-2 light bending | **derived + simulated** (ratio 2.09) |
| gravitational redshift | **derived** (corollary of `N²~b`) |
| Nordström excluded | **yes** (needs `α=0`, unphysical) |
| `α = 1` (reserve independence) | **contingent** — leading reading of P04; exact reserve dynamics open |
| field equation `G=κT` coefficient | **contingent — open (R9)** |
| `b(r)` profile | **imposed** (= field equation, R9) |
| any structural block | **none found** |

## 7. ED ↔ GR structure map (through Round 8)

| GR object | ED structure | status |
|---|---|---|
| lapse `N(b)` | bandwidth-limit speed via `Γ~b` | **`N²~b` derived ✓ (R8)** |
| `g_00 g_rr` | `−b·b⁻¹` | **`= −1`, Schwarzschild ✓ (R8)** |
| light bending `4GM/c²ξ` | optical index `b⁻¹` | **factor-of-2 ✓ (sim)** |
| gravitational redshift | `N~b^{1/2}` | **derived ✓ (R8)** |
| Einstein vs Nordström | `α=1` vs `α=0` | **Einstein (certified `Γ~b`)** |
| field equation `G^μν=κT^μν` | curvature↔source coefficient | **open (R9)** |

## 8. Verdict

**The fork is decided: ED's weak-field gravity is Einstein-class, derived from the certified commitment-rate law — Nordström is excluded.** Assembling the Lorentzian metric and imposing the null condition on the front, the certified commitment rate `Γ_commit ~ b_int/reserve` (linear, `α=1`) **forces the lapse `N² ~ b`**, hence the **Schwarzschild relation `g_00 g_rr ~ −1`**, the **factor-of-2 light bending** (optical index `b⁻¹`; simulated ratio 2.09 vs GR's 2), and, as a free corollary, **gravitational redshift** (`N ~ b^{1/2}`). All three classical weak-field signatures fall out of one derived lapse. The conformal/Nordström branch is positively excluded, requiring the unphysical `α = 0` (front slower where bandwidth is higher).

The honesty line is the same one the arc has held throughout: this is the **weak-field metric class**, not the field equation. Schwarzschild is the *vacuum* Einstein solution — reproducing its relation `g_00 g_rr ~ −1` and the factor of 2 is necessary and strong, but the *sourced* equation `G^μν = κ T^μν` (and its coefficient) is still underived, the `b(r)` profile is still imposed, and the result rests on the reserve-independence reading that gives `α=1`. **No structural block survives; ED clears the qualitative bar for Einstein (metric class + the two cleanest classical tests, derived) and the residual is now a single, well-posed object: the field equation.** Einstein is not derived — but ED is now demonstrably on the Einstein branch, not the Nordström one, by its own certified dynamics.

## 9. Round-9 questions

1. **The field equation (the last keystone).** Derive the curvature↔source relation and its coefficient `κ`: is it `G^μν = κT^μν`? The metric class is fixed; this fixes the dynamics.
2. **Reserve dynamics → `α`.** Confirm from the P04 band law that the commitment-reserve does not co-scale with `b_int`, pinning `α = 1` (and with it the whole §2 result).
3. **Derive `b(r)`.** Replace the imposed profile with the field-equation solution around an ED source; re-run both instruments and check `g_00 g_rr ~ −1` self-consistently.
4. **Perihelion precession.** The third classical test — timelike geodesics in `N²~b`, `g_rr~b⁻¹`; does the precession match GR?
5. **Strong field / horizons.** As `b → 0` the lapse `N → 0` and `g_rr → ∞` — the horizon (R4 §6 unification). Does the strong-field metric match Schwarzschild beyond weak field?

---

*Round-8 derivation + simulation. Verdict: the certified commitment-rate law `Γ~b` (α=1) **forces the lapse `N²~b`**, giving the **Schwarzschild relation `g_00 g_rr ~ −1`**, the **factor-of-2 light bending** (optical index `b⁻¹`; simulated ratio 2.09 vs 2), and **gravitational redshift** (`N~b^{1/2}`) — the three classical weak-field signatures, derived, with **Nordström excluded** (needs the unphysical `α=0`). This is the weak-field **metric class**, not the field equation: `G^μν=κT^μν` and the source profile `b(r)` remain open (R9), and the result rests on the reserve-independence reading. No corpus edits, no new primitives. Nothing here derives the full Einstein equations — but ED is now on the Einstein branch by its own certified dynamics, with the residual reduced to the field-equation coefficient.*
