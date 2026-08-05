# The Perron Closure of the Structure→{b_K} Direction Is Refuted (and the Fork Is a Disorder-vs-Coherence Localization Competition)

**Date:** 2026-07-27
**Status:** Failed-closure record + a grounding of the #16 gap. Follows `MatterWave_Direction_and_StructureToChannel_Map_2026-07-24.md` (which ruled the folded-vs-unfolded direction INDETERMINATE). **Do NOT re-attempt the Perron argument below.** The INDETERMINATE verdict STANDS; this note only sharpens *why*.

## The tempting (wrong) closure
The 07-24 note left the direction indeterminate because the collective-mode coupling operator could either *concentrate* its dominant eigenvector (Perron mode → lower `M_eff` → folded-first) or *spread* it (GOE-eigenvector regime → higher `M_eff` → unfolded-first), and "ED says nothing about which regime." A natural-looking closure (attempted 2026-07-27): the corpus separately **derives V5's attractive sign** (`Paper_V5AttractiveSign_P12Coh.md`), so if the coupling operator is the V5 kernel and "attractive" means a **non-negative matrix**, then Perron-Frobenius forces the single-signed dominant eigenvector, the GOE-spread branch is excluded, and the fork collapses to **folded-first** — resolving toward Paper_060 and giving the only-ED directional weapon.

## Why it fails (verified against the actual derivation)
Read `Paper_V5AttractiveSign_P12Coh.md` §3–§4. V5's "attractive sign" is a **dynamical reward-coherence sign** (`k_c5 > 0`: the certified selection functional moves a front *up* the coherence gradient), **not** a non-negative coupling matrix. The actual cross-chain coupling entered into the dynamics is

> `sig_advance += k_c5 · Σ_j w_ij · sin(φ_j^ret + A_ij − φ_i)`, with `w_ij = e^{−|Δy_ij|/ℓ_V5} ≥ 0` and `A_ij` a **quenched P05 connection (substrate disorder)**.

The coupling weight is `w_ij · cos(Δπ_ij − A_ij)` (the `sin` is its gradient). The reach backbone `w_ij` is non-negative, but the `cos(Δπ − A_ij)` factor is **sign-varying**, because `A_ij` is a *random quenched holonomy* (the paper runs it explicitly, "disorder-robust"). So the V5 coupling matrix is **not** non-negative; Perron-Frobenius does not apply; the GOE/spread branch is **not** excluded. The Perron closure is refuted.

## What is actually true (grounded, INDETERMINATE stands)
The V5 coupling is a **non-negative reach backbone (`w_ij`) dressed by quenched-holonomy disorder (`A_ij`)**. Structurally this is a **coherence-vs-disorder localization competition** (Anderson-flavored): the coherent backbone tends to *concentrate* the dominant mode (→ folded-first), the quenched disorder tends to *spread* it (→ unfolded-first). Which wins is set by V5's **disorder strength and reach `ℓ_V5`** — which `Paper_090` §3.3 and `Paper_V5AttractiveSign` §5 both label **inherited value-layer content, not derived**.

- Tier of the localization framing: **observation/analogy**, not a theorem. The claim that survives firmly is the *negative*: attractive-sign ⇏ non-negative matrix ⇏ Perron closure.
- Do **not** now over-flip to "disorder ⇒ spread ⇒ unfolded-first." Whether adding contacts (folding) net-concentrates or net-spreads in a disordered coupling depends on how folding changes *both* the backbone connectivity and the effective disorder, and on the inherited disorder strength. Genuinely undetermined at the derived level.

## Net
- The folded-vs-unfolded direction (the only-ED falsifiable core of the matter-wave weapon) **remains blocked**, now precisely: it is gated on V5's **inherited disorder strength / reach**, the same value-layer content the #16 structure→{b_K} gap is about.
- Getting the direction would require **deriving V5's envelope/disorder** (open in Paper_090 and the sign paper), a deep separate lift — not extractable from the currently-derived structure.
- Discipline note: the hypothesis died at verification, before any stand-in graph computation was run. That is the intended order (read-first / verify-before-compute), and it prevented banking a wrong direction.

## Cross-references
- `theory/MatterWave_Direction_and_StructureToChannel_Map_2026-07-24.md` (the INDETERMINATE verdict this sharpens).
- `ED Generative/physics-papers/substrate-evaluation/Paper_V5AttractiveSign_P12Coh.md` (§3 coupling = coherence content; §4 the quenched-disorder build).
- `ED Generative/physics-papers/foundations/Paper_090_V5Kernel.md` (§3.3 envelope/reach inherited).
- `docs/ED_Research_Targets.md` #16 (the structure→{b_K} gap).
