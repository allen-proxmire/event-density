# Phase-3 GR — The Magnitude of `α₁`: Safe by ≥70 Orders if Commitment Is Sparse; the One Pivotal Question

**Foundations computation — turns the derived scaling `λ ∼ ρ_event/ρ_Planck` into a numerical `α₁` for the Solar System, from ED's primitives only. Not a corpus edit, not a new primitive. Result: the magnitude reduces to ONE pivotal ED question — is commitment (P11) a sparse *physical determination event* or a dense *every-tick* process? If sparse (which ED's ontology favors: P11 ≠ P13), then `α₁` is safe by ≥70 orders of magnitude, robustly across every plausible identification of `ρ_event`. If commitment were Planck-dense (every tick commits everywhere), `α₁ = O(1)` (tension). The number is conditional on the sparse branch, which is strongly motivated but load-bearing; I do not pick it silently.**

The `λ(ρ)` derivation gave `λ = (k₁₁/s₀₂)·ρ_event/ρ_Planck`. This note computes `ρ_event` and hence `α₁`.

**Crank rail — maximal, this is the number step.** I give order-of-magnitude estimates for *candidate* identifications of `ρ_event`, show the conclusion is robust across them, and state explicitly the one assumption (sparse commitment) the favorable number rests on. No single value is presented as THE answer; the robust statement is the ≥70-order margin *conditional on sparsity*, plus the honest alternative (dense → tension).

---

## 1. `ρ_event` defined, and the pivotal fork

`ρ_event(x)` ≡ the local density of **irreversible commitment events** (P11) per 4-volume, and `ρ_Planck = 1/ℓ_P⁴` is the maximal density (every Planck cell commits every Planck tick). `λ ∼ ρ_event/ρ_Planck`.

Everything hinges on one question:

> **Is commitment (P11) a *sparse physical determination event*, or a *dense every-tick* process?**

- **P13 is the tick** — the clock, fires every Planck time everywhere.
- **P11 is commitment** — an *irreversible determination* (indeterminate → determinate). 

These are **separate primitives.** If commitment fired at *every* tick in *every* cell, `ρ_event = ρ_Planck`, `λ = O(1)`, `α₁ = O(1)` — tension (the old unfavorable branch). But that would make P11 redundant with P13. ED's ontology says commitment is *determination* — a physical event (decoherence-like), not a clock tick. **A coherent/undetermined region does not commit just because the clock ticks.** So commitment is **sparse**: `ρ_event ≪ ρ_Planck` wherever the substrate is not maximally determining. This is the favorable branch, and it is the one ED's `P11 ≠ P13` distinction supports — but it is the load-bearing assumption, stated openly.

The rest of this note computes the *sparse* branch and shows the conclusion is robust; §6 states the dense-branch alternative.

## 2. `ρ_event` in three regimes (sparse branch)

If commitment tracks physical determination, `ρ_event` tracks the local physical activity. Candidate identifications (all sub-Planck), with `ρ_Planck ≈ 5×10¹¹³` J/m³:

| regime | candidate physical density | `ρ_event/ρ_Planck` |
|---|---|---|
| Solar-System vacuum (1 AU), **field energy** `g²/8πG` (`g ≈ 6×10⁻³` m/s²) | `≈ 2×10⁴` J/m³ | `≈ 10⁻¹¹⁰` |
| 1 AU, **ambient matter** (solar wind `∼10⁻²⁰` kg/m³) | `≈ 10⁻³` J/m³ | `≈ 10⁻¹¹⁶` |
| **source** (Sun mean, `ρc² ≈ 1.3×10²⁰` J/m³) | `≈ 10²⁰` J/m³ | `≈ 10⁻⁹³` |
| cosmological floor (`ρ_Λ ∼ 10⁻¹²² ρ_Planck`) | — | `≈ 10⁻¹²²` |
| (extreme stress-test: **nuclear density** `∼10³⁵` J/m³) | — | `≈ 10⁻⁷⁸` |

Every plausible identification of the density the khronon samples is between `∼10⁻⁷⁸` (nuclear, far denser than anything in the Solar System) and `∼10⁻¹²²` (cosmological). The Solar-System-relevant ones cluster around `10⁻⁹³` (source) to `10⁻¹¹⁶` (local).

## 3. Which density the khronon samples

The `θ²` stiffness is a property of the foliation in the region the orbital dynamics probe. Whether `λ` is set by the *local vacuum* density (`∼10⁻¹¹⁰`), the *source* density (`∼10⁻⁹³`), or an average is not pinned here — **but it does not matter for the verdict:** the densest plausible choice (the source) gives `∼10⁻⁹³`, and even the absurdly conservative nuclear-density stress-test gives `∼10⁻⁷⁸`. All are `≪` the bound. So I take the **most conservative (densest)** as the upper bound on `λ` and proceed; the true value is almost certainly far smaller.

## 4. `λ_vacuum` and `α₁`

With the `O(1)` band-fraction prefactor `k₁₁/s₀₂`:

> **`λ_Solar-System ≲ 10⁻⁹³`** (conservative, source-density) — and plausibly `∼10⁻¹¹⁰` (local field energy).
>
> **`α₁ = −4λ ≲ 4×10⁻⁹³`** (conservative) to `∼10⁻¹⁰⁹` (local).

Against the experimental bound `|α₁| < 2.5×10⁻⁵`:

> **`α₁` is below the bound by ≥ 88 orders of magnitude** (conservative source-density), and by `~104` orders on the local-field-energy identification. Even the nuclear-density stress-test (`λ ∼ 10⁻⁷⁸`) clears the bound by `~73` orders.

**The margin is so enormous that the identification uncertainty is irrelevant to safety:** every plausible sparse identification gives `α₁` safe by `≥70` orders.

## 5. Consistency — preserved, with one correction and one flag

- **`c_T = c`** (P05 tensor sector): untouched by the scalar `λ`. ✓
- **vacuum `c_s = c`**: the `ε=0` locking gives `c_s → c` as `λ → 0`; GW170817 (vacuum) is exactly that regime. ✓
- **`κ/D = 8πG`**: density-independent ratio (P02-sharing `M_P²` always on). Gravity is full-strength even though `λ ≪ 1`. ✓
- **Correction to the earlier "khronometric near matter":** `λ` reaches `O(1)` only at `ρ_event ∼ ρ_Planck` — i.e. at **Planck density** (black-hole cores, the Big Bang), *not* ordinary matter. For *all* ordinary densities (Solar System, stars, even neutron stars) `λ ≪ 1`, so **ED is observationally General Relativity everywhere we test gravity, and khronometric only at the Planck-density frontier.** This is the natural and favorable reading: ED's Lorentz violation is density-suppressed, derived (not assumed), and switches on only where quantum gravity lives anyway.
- **Flag — the MOND sector (KM-I):** MOND is a khronon effect in the *low-acceleration* (galactic-outskirt) regime. If `λ ∼ ρ/ρ_Planck`, the *local* khronon coupling is tiny there too — so MOND cannot come from the *local* `λ`; it must come from the khronon's *cosmological background* value (the `H₀`-scale foliation, KM-II's "one scale, four roles"). The `α₁` (local) and MOND (cosmological-background) roles of the khronon are then distinct, governed by *acceleration relative to `a₀ = cH₀`*, not local density. **This reconciliation is a real task, but it does not threaten `α₁` safety** — it refines how the same field plays two roles. (It is the one genuinely open consistency item.)

## 6. The honest alternative branch

If commitment is **not** sparse — if P11 fires at every P13 tick in every cell — then `ρ_event = ρ_Planck`, `λ = O(1)`, `α₁ = O(1)`, **tension.** This is the branch the field-theory default assumed. It is disfavored because it makes P11 redundant with P13 (commitment ≠ ticking; determination is a physical event), but it is the assumption the favorable number rests on, and it is what a critic would press. **So the verdict is conditional, and the condition is sharp and checkable.**

## 7. Verdict

**The magnitude reduces to one pivotal, sharp ED question — is commitment a sparse physical determination event (P11 ≠ P13) or a dense every-tick process? — and ED's ontology favors sparse.** On the sparse branch, `ρ_event/ρ_Planck ≲ 10⁻⁹³` in the Solar System (conservative source-density; `∼10⁻¹¹⁰` for local field energy), so

> **`α₁ ≲ 4×10⁻⁹³`, below the experimental bound `2.5×10⁻⁵` by ≥ 88 orders of magnitude — robustly, across every plausible identification of `ρ_event` (the margin is ≥70 orders even at the absurd nuclear-density stress-test).**

This is consistent with `c_T = c`, vacuum `c_s = c` (GW170817's regime), and `κ/D = 8πG`; it makes ED *observationally GR everywhere gravity is tested* and khronometric only at Planck density; and it leaves one genuine consistency task (reconciling the local-tiny `λ` with the khronon's cosmological MOND role via acceleration, not density). **The `α₁` front is, on ED's own ontology, not merely safe but safe by a vast, derived margin — conditional on the single, well-motivated, checkable assumption that commitment is sparse (a physical determination event, not every clock tick).** I do not assert the sparse branch as proven; I assert that it is what ED means by commitment, that it gives overwhelming safety, and that the alternative (dense) is the disfavored field-theory reading. The number is conditional and the condition is named.

## 8. Next

1. **Pin the sparse branch rigorously** — establish from P11/P13 that commitment is a determination event, not an every-tick process (the load-bearing point), ideally with the event rate tied to a physical scale.
2. **The MOND reconciliation** — show the khronon's cosmological-background (`a₀ = cH₀`) role coexists with the local-tiny `λ` (the one open consistency item).
3. **Write up** the screened-khronometric resolution: `α₁` safe by ≥70 orders on the sparse branch, ED = GR observationally, khronometric at the Planck frontier.

---

*Magnitude of `α₁` from the derived `λ ∼ ρ_event/ρ_Planck`. The whole number reduces to ONE pivotal question: is commitment (P11) a SPARSE physical determination event or a DENSE every-tick process? ED's ontology favors sparse (P11 ≠ P13: determination is a physical event, not a clock tick) — load-bearing, stated openly. On the sparse branch, `ρ_event/ρ_Planck` in the Solar System is `≲10⁻⁹³` (conservative source-density; `∼10⁻¹¹⁰` local field energy; `∼10⁻¹²²` cosmological floor), so `λ ≲ 10⁻⁹³` and `α₁ = −4λ ≲ 4×10⁻⁹³` — below the bound `2.5×10⁻⁵` by ≥88 orders (≥70 even at a nuclear-density stress-test). Robust across all identifications. Consistent with c_T=c, vacuum c_s=c (GW170817 regime), κ/D=8πG. Correction: λ→O(1) only at PLANCK density (BH cores, Big Bang), NOT ordinary matter → ED is observationally GR everywhere gravity is tested, khronometric only at the Planck frontier. One open consistency item: the MOND/KM-I role of the khronon is its cosmological background (a₀=cH₀), distinct from the local-tiny λ — reconcile via acceleration, not density (does not threaten α₁ safety). Alternative branch (dense commitment, every tick): α₁=O(1), tension — the disfavored field-theory reading. Verdict CONDITIONAL on the sparse branch, which is named, motivated, and checkable. No single value asserted as THE answer; the robust claim is ≥70-order safety on the sparse branch. No corpus edits, no new primitives; Einstein not derived; no number fabricated, the conditionality explicit.*
