# Phase-3 GR — Deriving `ε`: the Khronon Speed from P04 + P11

**Foundations derivation — fixes the single open coefficient of the hyperbolic build (`Phase3_GR_DynamicalRule_HyperbolicBuild`). Not a corpus edit, not a new primitive. Nothing here derives the Einstein field equations.**
The hyperbolic build reduced the khronon speed to `c_s/c = √(1+ε)`, with `ε` a *foliation-specific kinetic term* (a `λθ²`-type contribution): `ε = 0` → khronon at light speed (`c_s = c`, maximal predictivity); `ε ≠ 0` → a second cone (generic khronometric). It left one question: **does ED's foliation/reserve sector (P04 + P11) supply a nonzero `ε`?** This note answers it.
**Crank rail:** derive `ε` forward from what P04 + P11 actually are; do not assume `ε = 0` to get `c_s = c`. The decisive distinction — kinetic (speed-shift) vs dissipative (damping) — is checkable, and the rule is allowed to produce either. Sim: `evaluation/DynamicalBandwidth/hyperbolic_modes.py`.

---

## 1. What `ε` would have to be

`ε ≠ 0` requires a **conservative kinetic term acting on the scalar/trace (khronon) sector** beyond the single P05 transport — the khronometric `λθ²`, where `θ` is the expansion of the preferred (commitment-time) foliation. A conservative kinetic term shifts the **real** part of the dispersion `ω(k)` — it gives the khronon its own *speed* (a second cone). So the question is precise: **does P04 + P11 generate a conservative `λθ²` term for the commitment-foliation, or not?**

## 2. The arrow does two distinct things — only one is kinetic

The khronon owes its existence to the arrow (P11/P13). But "the arrow" decomposes into two structurally different operations:

1. **Gauge-breaking (kinematic).** The arrow-in-the-law breaks the time-reparametrization gauge that, in GR, removes the trace mode (hyperbolic build §1). This makes the khronon **physical** — but it is a statement about *which modes survive*, not about their *kinetic term*. It contributes **nothing** to `ε`: un-freezing a mode does not give it a new speed.
2. **Reserve dynamics (P04 + P11).** The commitment-reserve band drains as commitments fire (`Γ ~ b_int/reserve`), and — load-bearing — it drains **monotonically, one-way, with no replenishment** (P11 irreversibility; R2 §5; the `α=1` note). This is the only candidate for a new term in the khronon sector. Is it kinetic or not?

## 3. The reserve is dissipative, not kinetic — so it cannot be `λθ²`

A **monotone, one-way** variable is the definition of a **dissipative** degree of freedom. Dissipative couplings enter the dispersion as the **imaginary** part of `ω` (damping, `ω → ω + iγ`) — they make modes *decay*, not propagate faster or slower. A conservative `λθ²` kinetic term, by contrast, is **even in time-derivatives** and shifts the **real** part of `ω` (the speed). **P11 irreversibility makes the reserve one-way, hence dissipative, hence incapable of being the conservative `λθ²` term that `ε ≠ 0` requires.**

The simulation confirms the distinction is real and not semantic (`hyperbolic_modes.py`): adding a dissipative reserve term `−γ ḣ` to the khronon sector,

| reserve coupling `γ` | speed (real `ω`)/c | amplitude | reading |
|---|---|---|---|
| 0.00 | ≈ 1 | steady | undamped |
| 0.05 | ≈ 1 (**unshifted**) | decays (0.10) | **damped, same cone** |
| 0.20 | — | → 0 | **overdamped (no propagation)** |
| 0.80 | — | → 0 | overdamped |

The reserve **damps** the khronon — and overdamps it at strong coupling — but **does not move its cone**. Contrast the `ε`-knob, which shifts the cone cleanly (`c_s/c = √(1+ε)`). They are different physics: **`ε` is a speed-shift; the reserve is damping.** The reserve is not a `λθ²` term.

## 4. Minimality closes it: `ε = 0`

The forced rule is **P05 transport** (the wave operator, one speed `c` for all of `b`) **+ P11 commitment drain** (dissipative). The transport supplies the kinetic term — *the same one for tensor and trace* — and the drain supplies damping. **Neither supplies a conservative `λθ²` term.** A nonzero `ε` would require an *additional* conservative foliation-kinetic coupling that **no primitive declares** — positing one would be adding structure (a retrofit), exactly what the crank rail forbids. Therefore:

> **`ε = 0`, derived: the khronon propagates at `c_s = c` — at the speed of light — damped near active matter and clean in vacuum.** The foliation/reserve sector contributes *dissipation*, not a second cone. KM-II §6 resolves, **derived**, toward the maximal-predictivity horn: ED's scalar gravitational-wave polarization is at `c`.

**Observational consistency (a check, not a claim).** A khronon that is *overdamped where commitment is active* (near matter) but *undamped in vacuum* is exactly what is wanted: the far-field, vacuum khronon a detector would see propagates cleanly at `c`, while near a source it is dissipated. This is consistent with clean tensor GWs at `c` (GW170817) plus a scalar mode that does not show up as a fast/slow second cone.

## 5. The arrow wears three hats

This is the third time P11 — the single commitment, the arrow-in-the-law — has selected the Einstein/khronometric structure, each independently:

1. **`α = 1` at the lapse** — the reserve cannot replenish to track `b_int`, so the Einstein branch is forced and Nordström excluded (`AlphaOne` note).
2. **the khronon physical at the mode count** — the arrow breaks the time-gauge that would freeze the scalar (R10 / hyperbolic build).
3. **the khronon at light speed** — the reserve is dissipative (one-way), so it damps rather than supplying a `λθ²` second cone (this note).

One primitive, three structural results: the factor of two, the extra scalar, and that scalar's speed. The same irreversibility that *makes* the khronon *keeps it on the light cone.*

## 6. The `α₁, α₂` front — no free foliation knob left

With `ε = 0` derived, the foliation kinetic sector has **no free parameter**. Combined with KM-I's **universal (metric-only) matter coupling** — the feature that saved lensing (no separate khronon-matter coupling) — ED sits in the **maximally-constrained khronometric corner**: a physical scalar, on the light cone, coupled only through the metric. Both structural indicators (`c_s = c`; metric-only coupling) are the directions in which preferred-frame effects are *suppressed*. The explicit `α₁, α₂` are now a **definite computation with no free foliation knob** — the last input being the matter coupling, already fixed to universal by KM-I. **This note does not compute the numbers** (that is the final calculation), but it removes the freedom that made them ambiguous and points them toward PPN-safety.

## 7. Structural vs contingent

| Item | Verdict |
|---|---|
| `ε` = a conservative `λθ²` foliation-kinetic term (shifts the real `ω`) | **definitional** |
| arrow's gauge-breaking is kinematic (no kinetic contribution) | **structural** (un-freezing ≠ new speed) |
| reserve drains monotone/one-way → **dissipative** | **structural** (P11; R2 §5) |
| dissipative ⟹ damping (imaginary `ω`), not speed-shift | **structural + measured** (§3) |
| forced rule (P05 transport + P11 drain) has no `λθ²` term | **minimality** (no primitive supplies one) |
| **`ε = 0` ⟹ `c_s = c`** (khronon at light speed) | **derived** (§4) |
| khronon damped near matter, clean in vacuum | **structural + measured**; obs-consistent |
| sub-leading real speed renormalization from integrating out the reserve | **contingent** — possible small correction; does not restore a second cone |
| `α₁, α₂` numbers | **not computed** — but now knob-free (the final calc) |
| any structural block | **none** |

## 8. Verdict

**`ε = 0` is derived: ED's khronon propagates at the speed of light.** The only candidate for a foliation-specific kinetic term (`ε ≠ 0`, a second cone) is the commitment-reserve sector, and P11 makes that sector **one-way / dissipative** — it contributes **damping** (imaginary `ω`, confirmed: the reserve damps and overdamps the khronon without moving its cone), not the conservative `λθ²` kinetic term a second cone requires. The forced rule (P05 transport + P11 drain) supplies no `λθ²` term, and minimality forbids positing one, so `ε = 0` and `c_s = c`. This resolves KM-II §6's open question **as a derivation**, toward the maximal-predictivity horn: ED's scalar GW polarization is at `c`, damped near active matter and clean in vacuum (observationally consistent). The same P11 irreversibility that makes the khronon physical keeps it on the light cone — the arrow's third Einstein/khronometric selection, alongside `α = 1` and the mode count.

**The honesty lines.** (i) `ε = 0` is leading-order: integrating out the dissipative reserve could renormalize the khronon speed by a small amount, but cannot restore a conservative second cone — the *kind* of correction is damping, not a cone-split. (ii) "No `λθ²` term" is a **minimality** statement about the forced rule; a hidden conservative foliation coupling, if the full P04 dynamics secretly contained one, would reopen `ε` — none is declared. (iii) `α₁, α₂` are now **knob-free but uncomputed** — the maximally-constrained corner, pointing toward PPN-safety, with the explicit numbers the remaining calculation. **Einstein/khronometric is not newly derived; the last free coefficient of the propagating sector is fixed, and the program's sharpest open phenomenology now has a definite, foliation-knob-free target.**

## 9. Next

1. **Compute `α₁, α₂`.** With `ε = 0` and the universal metric coupling, the preferred-frame PPN parameters are a definite (no-free-foliation) computation — the GR-II falsification numbers, finally cornered.
2. **The reserve speed-renormalization (sub-leading).** Integrate out the dissipative reserve explicitly; quantify the small real correction to `c_s` (it stays one cone) — a possible tiny `|c_s/c − 1|` signature.
3. **Feed back to KM-II §6.** Update the open caveat to "the khronon is at light speed, derived (dissipative reserve), damped near matter" — a sharper published prediction, if/when the papers are revised.
4. **B-column numbers** (#4): with the full `F` (static horizon + hyperbolic modes + `ε=0`), compute the ED-10 scalings as numbers (`S = A/4`, Hawking `T`).

---

*Derives the last free coefficient of the hyperbolic build. `ε` (the foliation-specific `λθ²` kinetic term that would give the khronon a second cone) is **zero**: its only candidate source is the commitment-reserve sector, which P11 makes **one-way / dissipative** — contributing **damping** (imaginary `ω`; confirmed numerically: the reserve damps and overdamps the khronon without shifting its cone), not a conservative kinetic term. The forced rule (P05 transport + P11 drain) has no `λθ²` term and minimality forbids adding one, so `ε = 0` and **`c_s = c`**: ED's scalar GW polarization is at the speed of light, damped near matter, clean in vacuum — resolving KM-II §6 as a derivation toward maximal predictivity. The arrow's third Einstein/khronometric selection (with `α=1` and the mode count). `α₁,α₂` are now knob-free but uncomputed (the final calc). No corpus edits, no new primitives; Einstein not derived; the propagating sector's last coefficient fixed.*
