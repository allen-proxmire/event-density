# T21 — Substrate Derivation of the Baryonic Tully–Fisher Relation

**Status:** FORCED-unconditional (ratified 2026-04-28).
**Layer:** Theorem-level structural result.

## Summary

States that the empirical baryonic Tully–Fisher relation `v⁴ = G · M · a₀` — including the slope of exactly 4 in the relation `v_flat⁴ ∝ M_b` and the prefactor `G·a₀` — is FORCED at the substrate level by composing three previously-ratified results:

- **T19** (Newton's law from substrate, `a_N = GM/R²` with `G = c³ ℓ_P² / ℏ`),
- **T20** (transition acceleration from dipole mechanism, `a₀ = c·H₀ / (2π)`),
- the **ED Combination Rule** (deep-regime gradient-combination rule, `a = √(a_N · a₀)`).

Together these yield the full empirical phenomenology of galactic gravity — flat rotation curves, slope-4 BTFR, deep-regime `1/R` force law — from substrate primitives with no tunable parameters.

## Statement

For a chain in centripetal motion at radius `R` from a baryonic mass `M` at acceleration well below the transition scale (`a_N ≪ a₀`), the substrate-derived effective acceleration `a = √(a_N · a₀)` (per the ED Combination Rule) implies, by centripetal balance:

`v² = a · R = √(a_N · a₀) · R = √(G·M·a₀)`

— a quantity independent of `R`. Consequently:

`v⁴ = G · M · a₀`

This is the baryonic Tully–Fisher relation in its slope-4 form, with the prefactor `G·a₀` fully expressible in substrate constants.

## Assumptions

The derivation rests on the following ratified ED structural commitments:

- **ED-06** — *Horizons as Event Density Decoupling Surfaces.* Establishes the cosmic decoupling surface at `R_H = c/H₀` as a real structural feature of the participation graph.
- **ED-10** — *Event Density and the Emergence of Spacetime.* Establishes that geometry is emergent and the chain's participation environment supports the substrate dynamics used here.
- **T19** — Newton's law from cumulative-strain reading + participation-count bound, with `G = c³ ℓ_P² / ℏ`.
- **T20** — Transition acceleration from the dipole-mode mechanism, with `a₀ = c·H₀ / (2π)`.
- **ED Combination Rule** — In the joint weak-gradient regime, the chain stability landscape acquires a logarithmic cross-term with coefficient `√(M·a₀)`, producing `a = √(a_N · a₀)` (`arcs/arc-SG/ED_combination_rule.md`).

No further assumption is required.

## Proof

Let a chain orbit a spherically-symmetric baryonic distribution of total mass `M` at radius `R`, with `R` large enough that `a_N(R) ≪ a₀` (the deep-acceleration regime).

By T19, the Newtonian acceleration sourced by `M` at radius `R` is

`a_N = G M / R²`,    with `G = c³ ℓ_P² / ℏ`.

By T20, the transition scale is

`a₀ = c · H₀ / (2π)`.

By the ED Combination Rule, in the joint weak-gradient regime the chain's effective acceleration is

`a = √(a_N · a₀)`.

Substituting `a_N`:

`a = √( (G M / R²) · a₀ )  =  √(G M a₀) / R`.

For circular orbital motion, centripetal balance gives `a = v² / R`, so

`v² / R = √(G M a₀) / R`

⟹  `v² = √(G M a₀)`.

The right-hand side does not depend on `R`. Therefore the orbital velocity asymptotes to a finite, mass-determined value `v_flat ≡ (G M a₀)^{1/4}` at large radius, regardless of the radial position within the deep-acceleration regime. This is the **flat rotation curve** result.

Squaring:

`v_flat⁴ = G · M · a₀`.

This is the slope-4 baryonic Tully–Fisher relation, with prefactor `G·a₀` expressed entirely in substrate constants:

`G · a₀ = (c³ ℓ_P² / ℏ) · (c H₀ / 2π) = c⁴ ℓ_P² H₀ / (2π ℏ)`.

No free parameters appear at any step. ∎

## Consequences

### 1. Flat rotation curves

The orbital velocity `v² = √(G M a₀)` is constant in `R` throughout the deep-acceleration regime. This is the empirically observed flatness of galactic rotation curves at large radii — derived structurally from the substrate, not fit to the data.

### 2. Slope-4 baryonic Tully–Fisher relation

The empirical relation `v_flat⁴ ∝ M_b` (McGaugh 2012, AJ 143:40) is recovered with slope exactly 4, with the proportionality constant `G·a₀` expressed in fundamental substrate quantities. The framework predicts a single, universal `G·a₀` value across all galactic systems in the deep regime — testable to high precision against the SPARC catalog and similar surveys.

### 3. Deep-regime `1/R` force law

The effective force per unit chain mass in the deep regime,

`a(R) = √(G M a₀) / R`,

falls off as `1/R` rather than `1/R²`. This is the characteristic deep-regime force law that produces flat rotation curves and is the structural signature distinguishing the deep-acceleration regime from the Newtonian one.

### 4. Radial-acceleration relation

For arbitrary `(a_N, a₀)` ratios, the ED Combination Rule with T19 and T20 yields a single-valued function `a(a_N)` interpolating smoothly between Newtonian (`a → a_N` for `a_N ≫ a₀`) and deep-regime (`a → √(a_N · a₀)` for `a_N ≪ a₀`) limits. This is the structural account of the radial-acceleration relation reported empirically by McGaugh, Lelli, and Schombert (2016, PRL 117:201101).

## Notes on parameter-free status and structural closure

**Parameter-free.** Every quantity entering the BTFR derivation is either a fundamental constant (`c`, `ℏ`) or a derived substrate quantity (`ℓ_P` via T19, `H₀` empirically as the cosmic rate appearing in T20, the cross-term coefficient via the Combination Rule). No free constants are tuned at any step.

**Structural closure of the gravitational sector.** With T21 ratified, the substrate-gravity arc's empirical phenomenology is now structurally complete. The chain from primitives to galactic dynamics runs:

> P-primitives + ED-06 + ED-10  ⟶  T19 (Newton, G derived)  ⟶  T20 (a₀ derived)  ⟶  ED Combination Rule  ⟶  T21 (flat curves + BTFR slope-4).

There is no remaining open articulation question in the substrate-gravity arc as currently constituted. Open questions in the broader gravitational program (Phase-3 Einstein-equation emergence, the GR-4A speculative quadrant, kernel-parameter inference) lie outside T21's scope.

**Falsifier.** Any galactic system in the certified deep-acceleration regime departing significantly from `v_flat⁴ = G·M·a₀` falsifies T21 (and, depending on which step fails, falsifies one of the upstream commitments T19, T20, or the Combination Rule). The relation is sharp and testable.

## Reference

The full derivation chain lives in this repository under `arcs/arc-SG/` (substrate-gravity arc memos including `ED_combination_rule.md`) and the corresponding paper at `papers/ED_substrate_gravity_foundations/ED_substrate_gravity_foundations.{md,tex,pdf}`. The constitutional registration of this theorem is recorded in:

- `ED-primitives/foundations/forced_theorems_inventory.md` — name-only registry
- `ED-primitives/CONSTITUTION.md` — governance

This file in `event-density/theorems/` is the theory-side index entry; the proof is given in full above and in the substrate-gravity foundations paper (§7).
