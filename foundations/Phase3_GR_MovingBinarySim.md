# Phase-3 GR — The Moving-Binary F-Simulation: Mechanism Confirmed, Verdict Unchanged (Leans Safe)

**Foundations build-and-run — the `F`-native test of the `α₁` verdict: a binary drifting through the cosmic frame, with the preferred-frame wake and its reserve screening measured directly. Not a corpus edit, not a new primitive. Sim: `evaluation/DynamicalBandwidth/moving_binary.py`.**

The `Γ` note reached "leans PPN-safe" resting on two assumptions: (1) the reserve-drain range near matter is substrate-short (`~ℓ_P`); (2) the screening spares the covariant frame-dragging (the conserved-scalar/dissipative-khronon split). This simulation tests the *mechanism* those assumptions invoke.

**Crank rail (load-bearing, and I am watching it after two prior over-corrections):** state precisely what the sim measures vs. imposes. It measures the wake and the screening scaling; it *imposes* the split and cannot reach the absolute (Planck-scale) magnitude. It therefore **confirms the mechanism and is consistent with safety — it does not upgrade "leans safe" to "proven safe."**

---

## 1. What the sim measures vs. imposes

A binary (two masses) drifts at `w` through the cosmic frame. The metric-band rule, comoving, is the convection–diffusion equation `D∇²B + w·∇B = κρ`. Solved by FFT; the static baseline is the same solver at `w=0` (so the wake `→0` as `w→0` by construction).

- **Measured (genuine):** the wake `B − B_static`, and the Yukawa-screening suppression as a function of range.
- **Imposed (not derived here):** that the reserve drain screens *only* the dynamical wake while the covariant frame-dragging (the conserved-scalar boost) is held fixed. The sim shows the *consequence* of the split; it does not derive that ED realizes it.

## 2. Results

**(1) The preferred-frame wake is real, linear in `w`, dipolar.** For `w = 5×10⁻⁴ … 2×10⁻³`:

| `w` | `max\|wake\|/w` | dipole/monopole |
|---|---|---|
| 5×10⁻⁴ | 217.0 | 0.0125 |
| 1×10⁻³ | 217.2 | 0.0249 |
| 2×10⁻³ | 217.5 | 0.0499 |

`max\|wake\|` is exactly linear in `w` (`/w` constant), and the wake is **dipolar** (dipole/monopole `∝ w`) — a fore/aft asymmetry along the motion. This is the preferred-frame engine, and it is genuinely present: **ED is not boost-covariant.** (Not imposed — it falls out of solving the rule.)

**(2)+(3) The reserve drain suppresses the wake, and the field relaxes toward covariance.** Screening the wake with range `ℓ_scr` (`= √(D/Γ)`), holding the covariant frame-dragging fixed:

| `ℓ_scr / sep` | wake / wake₀ | `α₁` proxy (wake / frame-drag) |
|---|---|---|
| 10 | 0.989 | 2.62 |
| 3 | 0.889 | 2.35 |
| 1 | 0.486 | 1.29 |
| 0.3 | 0.079 | 0.21 |
| 0.1 | 0.009 | 0.024 |
| 0.03 | 0.0008 | 0.0022 |

As the screening range drops below the binary separation, the wake is suppressed steeply (`~10³×` by `ℓ_scr = 0.03 sep`), and the `α₁` proxy — the preferred-frame signal relative to the (preserved) frame-dragging — falls toward zero. The surviving field is the covariant frame-dragging: **the dissipation drives the field toward the covariant configuration, not toward zero.**

## 3. Where the physical point sits

The table stops at `ℓ_scr = 0.03 sep` (grid-resolvable). The physical screening range is `ℓ_scr ~ ℓ_P`, while a real binary separation is astronomical: `ℓ_scr/sep ~ 10⁻³⁵/10⁹ ~ 10⁻⁴⁴` — **44 orders below the bottom row.** Extrapolating the steep (exponential-in-`sep/ℓ_scr`) suppression, the `α₁` proxy at the physical point is `≈ exp(−10⁴⁴) ≈ 0`. The sim cannot render that scale; it confirms the *mechanism and the steep scaling that carry the field there.*

## 4. What this does and does not settle

- **Confirmed (measured):** the preferred-frame wake is real and `∝ w` (ED is not boost-covariant — consistent with the `λ_J` note); the reserve drain suppresses it, steeply, as `ℓ_scr` shrinks; in the suppressed limit the field is the covariant frame-dragging (frame-dragging preserved). The mechanism behaves exactly as the verdict requires.
- **Not settled (still assumptions):**
  1. **the absolute magnitude** — rests on `ℓ_scr ~ ℓ_P`, off the grid by `~10⁴⁴`; the sim shows the scaling, not the number.
  2. **the split** — the sim *imposes* that only the wake is screened. Whether ED's band-level dynamics actually screen only the dynamical wake while sparing the conserved-scalar boost is the genuine open question; it needs a band-level `F`-native simulation where both sectors and the reserve emerge, not a field-level solve.

So the simulation is **consistent with "leans PPN-safe" and demonstrates the mechanism concretely** — the wake exists, the reserve screens it, the limit is covariant — but it leaves the two load-bearing inputs (the Planck-scale range, the split) exactly where the `Γ` note left them. It does not, and at the field level cannot, convert the verdict to "proven."

## 5. Verdict

**The moving-binary F-simulation confirms the mechanism the `α₁` verdict rests on, without changing the verdict.** It measures, genuinely: a real, `w`-linear, dipolar preferred-frame wake (ED is not boost-covariant); a steep reserve-screening suppression of that wake as the drain range shrinks; and a suppressed limit that is the covariant frame-dragging (preserved, not killed). The physical screening range (`~ℓ_P`) sits `~44` orders below the simulable window, so the absolute `α₁ ≈ 0` follows from the scaling plus the substrate-scale estimate, not from the grid. The split (only the dynamical wake screened) is *imposed* here and remains the open structural assumption. **Net: "ED leans PPN-safe" stands, now with its mechanism explicitly demonstrated and quantified — but honestly still resting on the Planck-scale-range estimate and the conserved/dissipative split, which only a band-level `F`-native simulation (or a clean analytic derivation) can settle.**

## 6. Next (to convert "leans safe" → settled)

1. **Band-level `F`-native simulation:** evolve actual bandwidth bands (metric band, reserve, directed flux) under the primitive update rule (P02 sharing + P11 commitment/drain + P05 transport) for a moving source, and check whether the reserve drain *emergently* spares the conserved-scalar frame-dragging while screening the wake. This is the only build that can derive the split rather than impose it.
2. **Analytic proof of the split:** show from the conservation (P04) of the scalar vs. the dissipation (P11) of the khronon that the frame-dragging sector is undrained.
3. Either settles the front; until then it is honestly "leans safe."

---

*Moving-binary F-sim (`moving_binary.py`). Measured (genuine): the preferred-frame wake of a binary drifting at `w` is real, exactly linear in `w`, and dipolar — ED is not boost-covariant; the reserve drain screens it steeply as the range `ℓ_scr` drops below the separation (`~10³×` by `ℓ_scr=0.03 sep`); the suppressed limit is the covariant frame-dragging (preserved, not zeroed). Imposed (not derived): that only the dynamical wake is screened (the split). Cannot reach: the absolute magnitude — physical `ℓ_scr ~ ℓ_P` is `~10⁴⁴` below the grid, so `α₁ ≈ 0` follows from the scaling + the substrate estimate, not the sim. Net: confirms the mechanism, leaves the verdict at "leans PPN-safe" resting on the Planck-range estimate + the split; a band-level F-native sim (split emergent) or an analytic proof is what would settle it. No corpus edits, no new primitives; Einstein not derived; the number not faked.*
