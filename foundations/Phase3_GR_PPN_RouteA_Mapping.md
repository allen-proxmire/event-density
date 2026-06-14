# Phase-3 GR — The PPN Map (Route A): ED → Khronometric `α₁, α₂`, and the One Coupling That Decides

**Foundations derivation — executes "Route A" of the `α₁, α₂` number-crunch: map ED's derived gravitational facts onto the *verified* khronometric PPN formulas and read off where the falsification number lives. Not a corpus edit, not a new primitive. This is the first appearance of the actual literature coefficients in the ED program; they are cited, not recalled.**

The structural note (`Phase3_GR_PreferredFrame_Alpha12.md`) established that ED is driven toward the suppressed corner and scoped the number-crunch. With `κ, D` now pinned (`Phase3_GR_PinningKappaD.md`), this note does the map. The honest outcome is **sharper and less comfortable than the optimistic lean**: the luminal-cone conditions ED derives are *necessary but not sufficient* for PPN safety; the entire open number collapses onto a **single coupling**, the khronon acceleration coupling `c₁₄`, with `α₁ = −4 c₁₄` exactly (given `β = 0`). ED is PPN-safe in the conservative sector **iff** `c₁₄` is tiny — and a *propagating* luminal khronon (which ED has) sits at `c₁₄ ≠ 0`. So the conservative map does **not** hand ED a free pass; it localizes the verdict to one number and shows ED's survival rests on either a naturally-tiny `c₁₄` or the **non-conservative** dissipative near-field, which the conservative formulas cannot see. That is the precise boundary where Route A stops and Route B (direct PPN expansion of `F`) must begin.

**Crank rail (load-bearing):** the khronometric formulas below are **from the literature and cited**, not invented; the ED→coupling identifications are flagged as *map steps*; the final number is **not fabricated** — it is reduced to one unpinned coupling and a stated kill-threshold. A clean reduction is a reduction, not a verdict of safety.

---

## 1. The verified khronometric facts

Khronometric gravity (the hypersurface-orthogonal / preferred-frame Einstein-aether theory; the IR limit of Hořava gravity) has three dimensionless couplings. From Blas–Sibiryakov and the binary-pulsar constraint literature:

- **Couplings** (eq. 5 of Blas–Lim/Blas–Sibiryakov): `λ ≡ c₂`, `β ≡ c₁ + c₃`, `α ≡ c₁ + c₄`.
- **Tensor (spin-2) speed:** `c_T² = 1/(1 − β)`.
- **Scalar (spin-0 / khronon) speed:** `c_s² = (α − 2)(β + λ) / [ α (β − 1)(2 + β + 3λ) ]`.
- **Preferred-frame PPN parameters:**
  - `α₁ = 4(α − 2β)/(β − 1)`,
  - `α₂ = (α − 2β)·[ −β(3 + β + 3λ) − λ + α(1 + β + 2λ) ] / [ (α − 2)(β − 1)(β + λ) ]`.
- **The lever:** both `α₁` and `α₂` carry the **common factor `(α − 2β)`**. Therefore

> **`α₁ = α₂ = 0  ⟺  α = 2β`**   *(verified; the single condition for an exactly preferred-frame-free khronometric theory).*

- **Bounds:** `|α₁| ≲ 10⁻⁴` (lunar laser ranging), `|α₂| ≲ 10⁻⁷` (solar-spin alignment; `~10⁻⁹` from pulsars).

*(Sources: Blas & Sibiryakov, "Phenomenology of theories of gravity without Lorentz invariance: the preferred-frame case," arXiv:1412.4828, eqs. (5), (19), (27); coupling/speed/PPN expressions cross-checked against the binary-pulsar constraint papers arXiv:1311.7144 and arXiv:1811.07786.)*

## 2. ED's derived inputs to the map

What ED brings, each already established:

| ED fact | Status | Source |
|---|---|---|
| `κ/D = 8πG` (Einstein coupling) | derived | GR-II/R9; `PinningKappaD` |
| `c_T = c` (single P05 cone, tensor luminal) | derived | GR-II |
| `c_s = c` (khronon luminal, `ε = 0`) | derived | `DerivingEpsilon` |
| metric-only matter coupling (no direct khronon–matter term) | structural | KM-I |
| dissipative khronon near matter (overdamped, non-conservative) | derived + measured | `DerivingEpsilon`; `hyperbolic_modes.py` |

The first three are the ones the conservative khronometric formulas can consume directly. The last two are **outside** the conservative action the PPN formulas assume — hold that thought; it is the whole story.

## 3. The map (symbolic, first pass)

**Step 1 — `c_T = c` fixes `β`.** `c_T² = 1/(1 − β) = 1 ⟹` **`β = 0`**. (ED's single shared cone, GR-II, *is* the statement `β = 0`.)

**Step 2 — `c_s = c` fixes `λ(α)`.** With `β = 0`,
`c_s² = (α − 2)λ / [ α(−1)(2 + 3λ) ] = (2 − α)λ / [ α(2 + 3λ) ] = 1`
`⟹ (2 − α)λ = α(2 + 3λ) ⟹ 2λ − αλ = 2α + 3αλ ⟹ λ(1 − 2α) = α ⟹` **`λ = α/(1 − 2α)`**.

So ED's two luminal conditions cut the 3-parameter khronometric space down to a **one-parameter family**, coordinatized by `α = c₁₄` (the khronon acceleration coupling), with `β = 0` and `λ = α/(1 − 2α)`.

**Step 3 — read off the PPN parameters on that family.** With `β = 0`:

> **`α₁ = 4(α − 2·0)/(0 − 1) = −4α = −4 c₁₄`**   *(exact, on ED's luminal family).*

and `α₂`, carrying the same `(α − 2β) = α` factor, is likewise `α₂ = O(α)`, vanishing iff `α = 0`. Both preferred-frame parameters vanish **only at `α = c₁₄ = 0`** — which, on this family (`λ → 0`, `β = 0`), is the GR point where the khronon decouples and stops propagating.

## 4. What this says — the honest verdict

**The entire falsification number is now one coupling.** On ED's derived surface, `α₁ = −4 c₁₄` and `α₂ = O(c₁₄)`. The verified vanishing condition `α = 2β` becomes, at ED's `β = 0`, simply **`c₁₄ = 0`**.

**The luminal conditions are necessary, not sufficient.** `c_T = c` and `c_s = c` do *not* by themselves give `α₁ = α₂ = 0`. They leave `α₁ = −4 c₁₄`. This corrects the optimistic reading: putting both gravitational cones at light speed is *not* the same as killing the preferred-frame effects.

**A propagating luminal khronon sits at `c₁₄ ≠ 0`.** The point `c₁₄ = 0` on this family is pure GR — no propagating scalar. ED's hyperbolic build *measured* a genuine propagating khronon at `c_s = c`. Read as a **conservative** khronometric theory, that places ED at `c₁₄ ≠ 0`, hence `α₁ = −4 c₁₄ ≠ 0`. So the conservative map does **not** certify ED safe; it says ED is safe **iff** its effective `c₁₄` is tiny: `|α₁| ≲ 10⁻⁴ ⟹ |c₁₄| ≲ 2.5×10⁻⁵`, and the `α₂` bound is tighter still.

**Where ED's real escape lives — and why Route A can't evaluate it.** ED's khronon is **not** a conservative khronometric scalar near matter: the `ε = 0` derivation showed its only self-interaction is the **dissipative** commitment-reserve (P11, one-way), which contributes *damping*, not a conservative kinetic/acceleration term. The conservative PPN formulas of §1 assume a conservative action and therefore **cannot represent** ED's dissipative near-field — exactly the regime (`α₁, α₂` are read from the near-field of a moving source) where ED claims its strongest suppression. So:

> **Route A localizes the open number to the single coupling `c₁₄` and shows the conservative sector is generically *unsafe* at `c_s = c` unless `c₁₄` is tiny. Whether ED is actually safe turns on (i) the value of `c₁₄` that the rule `F` generates, and (ii) whether ED's dissipative near-field — invisible to these formulas — replaces the conservative `α₁ = −4 c₁₄` with something smaller. Neither is settled by the conservative map. The front stays formally OPEN, now pinned to one coupling and one non-conservative mechanism.**

**The internal tension that is the next computation.** ED simultaneously asserts (a) a *propagating* luminal khronon (hyperbolic build ⟹ a conservative kinetic structure exists ⟹ `c₁₄ ≠ 0` in the conservative reading) and (b) khronon self-coupling is *dissipative-only* (`ε = 0` ⟹ no conservative foliation term ⟹ `c₁₄ → 0`). These are not contradictory only if the propagating khronon's kinetic term descends from the **metric/tensor (`β`-)sector coupling**, not from a pure-khronon conservative `c₁₄ a²` / `c₂ θ²` term. Settling which is the precise content of Route B.

## 5. Success / kill criteria (now concrete)

- **Kill:** the direct PPN expansion of `F` (Route B) yields an effective `c₁₄` with `|α₁| = 4|c₁₄| ≳ 10⁻⁴` (or `|α₂| ≳ 10⁻⁷`) **and** the dissipative near-field does not cancel it. Then ED is observationally excluded — cleanly, at a single number.
- **Pass:** Route B yields effective `α₁, α₂` below the bounds, either because `c₁₄` is structurally tiny/zero (the `α = 2β` locus, here `c₁₄ = 0`) or because the dissipative near-field suppresses the conservative response. The mechanism must be *exhibited*, not asserted.
- **The lever to aim Route B at:** the verified identity `α₁ = α₂ = 0 ⟺ α = 2β`. With ED's `β = 0`, Route B's single job is to compute (or bound) `c₁₄` and the dissipative correction to it.

## 6. Verdict

**Route A is executed, and it does its job by *narrowing*, not by declaring victory.** Mapping ED's three consumable facts (`c_T = c`, `c_s = c`, `κ/D = 8πG`) onto the verified khronometric PPN formulas reduces the falsification front from "two numbers as functions of three couplings" to **one number, `α₁ = −4 c₁₄`, on a one-parameter family**, with the exact safety condition `c₁₄ = 0` (the `α = 2β` locus at `β = 0`). It also delivers an honest, non-flattering correction: the luminal cones ED derived are *not* sufficient for PPN safety, and a conservative reading of ED's *propagating* khronon would put `α₁ = −4 c₁₄ ≠ 0`. ED's escape, if it has one, is the **non-conservative dissipative near-field** that these formulas cannot evaluate — so the verdict moves to Route B (a direct PPN expansion of the dissipative rule `F`), now with a single, well-posed target: the effective `c₁₄` and its dissipative correction. **The front is still open as a number; it is now open in exactly one coupling, with a verified kill-threshold and a definite computation to run.**

## 7. Next (Route B, now well-posed)

1. **Expand `F` to post-Newtonian order around a source moving at `w` through the cosmic (khronon) frame.** Read off the `O(w/c)` field correction = effective `α₁`; the `O(w/c)²` = effective `α₂`.
2. **Separate conservative vs dissipative pieces.** The conservative part should reproduce `α₁ = −4 c₁₄` with `c₁₄` expressed in P04 band-fractions; the dissipative part (the overdamped near-field) is the ED-specific correction the literature formulas omit.
3. **Numerical sanity check** (only if the analytic expansion gives a ballpark): a two-body ED simulation drifting through the cosmic frame, measuring the gravitational anisotropy directly — an `F`-native measurement of `α₁, α₂` that bypasses the conservative-action assumption entirely.
4. **Compare to `10⁻⁴, 10⁻⁷`.** Then, and only then, the front closes — favorably or not.

---

*Route A of the `α₁, α₂` crunch, executed against the verified khronometric formulas (Blas–Sibiryakov 1412.4828; constraint papers 1311.7144, 1811.07786). Couplings `λ=c₂, β=c₁+c₃, α=c₁+c₄`; `c_T²=1/(1−β)`, `c_s²=(α−2)(β+λ)/[α(β−1)(2+β+3λ)]`; `α₁=4(α−2β)/(β−1)`, both PPN parameters ∝ `(α−2β)` so `α₁=α₂=0 ⟺ α=2β`. ED's `c_T=c ⟹ β=0`; `c_s=c ⟹ λ=α/(1−2α)`; hence `α₁=−4c₁₄` exactly and safety `⟺ c₁₄=0`. The luminal cones are necessary, not sufficient; a conservative reading of ED's propagating khronon gives `α₁≠0`; ED's only escape is the non-conservative dissipative near-field, invisible to these formulas. The open number is reduced to one coupling `c₁₄` with kill-threshold `|c₁₄|≳2.5×10⁻⁵`; closing it needs Route B (direct PPN expansion of `F`). No corpus edits, no new primitives; Einstein not derived; the number deliberately not faked.*
