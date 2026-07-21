# Open piece (i): ED's collapse energy functional — a MOND correction to E_G, gated on the External Field Effect

**2026-07-21. Working note (event-density), behind the EDG state-reduction papers. Status: a genuinely distinctive candidate prediction, with one decisive open gate (the EFE). Not yet a delivered number.** This is the "weapon play" flagged as open piece (i) of `physics-papers/state-reduction/StateReduction_CollapseRate_ED_Derivation.md`: the collapse-rate scaling argument *identified* the branch-clock-difference energy with Penrose's Newtonian `E_G` rather than computing it from ED's own gravity. ED's gravity is not Newtonian — it is the quadratic-strain interference structure (`Paper_QuadraticStrain_v1`, `physics-papers/gravity/`), whose diagonal is Newton and whose off-diagonal is MOND. So the honest question is: **does the ED energy functional give a different `E_G` than Penrose, and where?** The answer is yes, potentially by a large factor, for exactly the mesoscopic masses these experiments use — but whether that survives in a ground laboratory hinges on the External Field Effect, which the corpus has not computed for this regime.

## The energy functional (cited, not re-derived)

From `Paper_QuadraticStrain_v1`: reading per-channel strain as `Str_K = |Σ_a P_K^(a)|²` with `P_K = √b_K e^{iπ_K}` splits gravity into

- a **diagonal** (self) term = Newton: `a_N = GM/R²`, `Φ_N = −GM/R`;
- an **off-diagonal** (cross-source) term = the **local–horizon interference** (MOND): `a_cross = √(a_N a_0) cosΘ_LH`, with `a_0 = cH_0/(2π) ≈ 1.2×10⁻¹⁰ m/s²` (`Paper_029`).

Total: `a = a_N + √(a_N a_0)` (constructive sign, `cosΘ_LH ≈ 1`, the inherited residual). Crossover at `a_N ~ a_0`: Newtonian above, deep-MOND (`a ≈ √(a_N a_0) ≫ a_N`) below.

**Two inherited caveats, carried:** (1) the functional is conditional on **P-Quadratic-Strain** (Model C, itself a substrate-level postulate); (2) the **constructive interference sign** is supplied only at MEASURED tier (`Paper_PhaseCoherence_P12Coh`), not derived. Both ride along here.

## The decisive fact: laboratory masses are deep sub-a₀ internally

The collapse `E_G` is the gravitational self-energy of the *difference* of the two branch mass distributions. The gravitational field that distinguishes the branches is the object's own self-field, whose scale is the surface self-gravity `g_N = GM/R² = (4/3)πGρR`. Setting `g_N = a_0`:

| density | `R*` where `g_N = a_0` |
|---|---|
| silica, `ρ = 2×10³` | **≈ 215 μm** |
| tungsten, `ρ ≈ 1.9×10⁴` | **≈ 23 μm** |

Every solid object **smaller than ~hundreds of μm has surface self-gravity below `a_0`.** Typical levitated-optomechanics / matter-wave masses sit far below it:

| object | mass | `g_N` (m/s²) | `g_N/a_0` | naive `√(a_0/g_N)` |
|---|---|---|---|---|
| 100 nm silica | `8×10⁻¹⁸` kg | `5.6×10⁻¹⁴` | `5×10⁻⁴` | **46** |
| 1 µm silica | `8×10⁻¹⁵` kg | `5.6×10⁻¹³` | `5×10⁻³` | **15** |
| 10 µm silica | `8×10⁻¹²` kg | `5.6×10⁻¹²` | `0.05` | **4.6** |
| 100 µm silica | `8×10⁻⁹` kg | `5.6×10⁻¹¹` | `0.47` | 1.5 |
| 1 mm silica | `8×10⁻⁶` kg | `5.6×10⁻¹⁰` | `4.7` | 0.5 (Newtonian) |

So **the mesoscopic superpositions on which gravitational collapse would be tested live deep in ED's MOND (sub-`a_0`) regime for their own self-gravity** — not by fine-tuning, but generically, because small objects have tiny self-fields. Penrose and Diósi compute `E_G` with *Newtonian* gravity throughout; ED says that for these masses the self-gravity is in the interference-dominated regime, so the collapse energy is **enhanced** — deeper well, stronger binding of the difference — by a factor of order `√(a_0/g_N)`, i.e. **~5–50× for 100 nm–10 µm particles.** Enhanced `E_G` means `τ = ℏ/E_G` is **shorter**: ED predicts *faster-than-Penrose* gravitational collapse for mesoscopic superpositions. That is a large, directly-measurable, distinctive fork — Penrose/Diósi carry no mass- or size-dependent correction of this kind.

## The gate that decides whether this is real: the External Field Effect

This is where honesty bites, and it is why this is a candidate, not a delivered prediction. MOND is **nonlinear**, so a system's internal dynamics depend on the external gravitational field it is embedded in (the External Field Effect, EFE). A system sitting in an external field `g_ext > a_0` has its internal MOND behavior **Newtonized** — the enhancement is suppressed.

- **Ground laboratories sit in Earth's field, `g_ext = 9.8 m/s² ≫ a_0`.** Under a *standard* MOND EFE this would fully suppress the internal enhancement: `E_G^ED ≈ E_G^Newton ≈` Penrose, and the fork closes on Earth. So the naive 5–50× must not be quoted as a ground-lab prediction.
- **Does ED even have a standard EFE?** Not established. ED's cross-term is the local–horizon interference, and `Paper_029` sources the horizon response from the chain's **total acceleration** (the dipole `ρ_cosmic ∝ |a|/c cosθ`). If the acceleration that sets the horizon response is the total (Earth-dominated) field, ED inherits an EFE-like suppression; if it is the internal self-field, it does not. **Computing this — ED's EFE from the horizon dipole — is the decisive next calculation, and the corpus has not done it for this regime** (the only EFE in the corpus is the cluster-merger foil in `Paper_117`, a different context).
- **Freefall / space removes Earth's field.** A freely-falling experiment (drop tower, satellite) locally cancels `g_ext` from Earth; the residual external field is the **Galactic** `~1.6 a_0` (borderline) or, in deep space, `≪ a_0` (pure deep-MOND). So a space-based or freefall collapse test is where ED and Penrose **sharply diverge** — if ED's EFE tracks the external field at all.

## The honest fork

1. **If ED has a full standard EFE:** ground-lab collapse is Newtonized, ED ≈ Penrose on Earth; the departure appears only in freefall/deep-space experiments, where ED predicts MOND-enhanced (faster) collapse for sub-`a_0` masses.
2. **If ED's EFE is weaker than standard MOND (or absent):** ED predicts a large (5–50×), size-dependent, faster-than-Penrose collapse even in ground labs — a sharp, already-testable departure.

Either branch is **distinctive**: Penrose/Diósi predict neither a MOND enhancement nor any EFE-dependence. Even the *existence* of an environmental-field dependence in measured collapse rates would be an ED fingerprint that the continuous-noise models do not carry. The magnitude and the ground-vs-space split both wait on the EFE computation.

## A real subtlety in the computation (do not skip in the rigorous version)

Because MOND is nonlinear, `E_G` is **not** literally "Newtonian `E_G` × `√(a_0/g_N)`." The superposition-of-difference construction (`δρ = ρ₁ − ρ₂`, self-energy of `δρ`) is a *Newtonian* identity; in the interference/MOND regime the two-branch energy must be evaluated from the nonlinear strain functional for each branch and differenced. The `√(a_0/g_N)` factor is the correct order-of-magnitude scale of the enhancement, not the exact functional. A rigorous number requires solving ED's nonlinear field structure (`Paper_036` MOND field equation) for the two-branch configuration — and, because the cross-term is local–**horizon**, tracking how the horizon-dipole contribution differs between the branches (the same object the EFE computation needs).

## Tiers

- The energy functional (Newton diagonal + MOND off-diagonal) — **structural, inherited** from `Paper_QuadraticStrain_v1`; conditional on P-Quadratic-Strain and the constructive-sign residual.
- "Lab masses are deep sub-`a_0` internally" — **solid** (arithmetic on `g_N = GM/R²` vs `a_0`).
- "So `E_G` is MOND-enhanced by `~√(a_0/g_N)`, collapse is faster" — **candidate, order-of-magnitude**, conditional on the EFE not suppressing it and on the nonlinear evaluation.
- The **EFE** (does Earth's field Newtonize the internal dynamics in ED?) — **OPEN, decisive**; not in the corpus for this regime; the next calculation.
- Net distinctiveness (a MOND + EFE structure in collapse rates, absent from Penrose/Diósi) — **real either way**, magnitude gated.

## Next steps

1. **Compute ED's EFE from the horizon dipole (`Paper_029`).** Does the horizon response to a chain's *total* acceleration Newtonize a lab system in Earth's field? This decides the ground-vs-space fork and is the single highest-leverage move.
2. **Evaluate the two-branch energy nonlinearly** (`Paper_036` field structure) to replace the `√(a_0/g_N)` scale with the actual enhancement functional, including the branch-difference of the horizon-dipole term.
3. **Only then** quote a number and a target experiment (freefall/space vs ground), and fold a properly-tiered version into the EDG derivation note's open piece (i).

*Working note. Behind `ED Generative/physics-papers/state-reduction/`. The result: ED's gravity generically wants a large MOND enhancement of the gravitational-collapse energy for mesoscopic (sub-`a_0` self-gravity) superpositions — a distinctive, faster-than-Penrose fork — but the External Field Effect (uncomputed in ED for this regime) gates whether it survives in a ground laboratory or shows only in freefall/space. The distinctiveness is real; the number is not yet delivered.*
