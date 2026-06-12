# CoarseGrain Arc — what continuum law does the certified substrate generate?

**Question:** does ED's coarse-graining actually produce a continuum law from the certified substrate — and which one? The cleanest, most falsifiable instance of the program's deepest open thread (*does coarse-graining give the continuum*). Let the data pick the PDE class; diffusion and the corpus Q-C PDE are hypotheses, not assumptions.

**This is the program's first *tested* (not merely *located*) substrate result** — and it can come back "no."

## Verdict (one line)

**The certified ED substrate is QUALITATIVELY generative (kinetic lattice-gas: ballistic worldlines + disorder scattering, isotropic fast-relaxing equilibrium, genuine saturation-driven mobility degeneracy) but QUANTITATIVELY non-generative under the methods tried: NOT diffusion, NO clean closed continuum PDE (even with exact bandwidth conservation [R6]), and NOT the UDM mobility law (β≈0 not β≈2 — both without blocking [R4] and with saturation-extinction blocking [R5]).** Same form-yes / precise-law-no shape the wider program keeps finding. The program's clearest *tested* (build-and-run, came-back-no) negative.

**The bridge (R6 + §6a):** located, not crossed. The missing ingredient is **scale separation** (collision time τ≈1.5 ≈ transport time → no Chapman-Enskog closure), **not conservation** (R6 added it exactly, current still didn't close). A PDE-generating ED substrate would need the **thick/over-damped regime** (τ≪transport, isotropic lattice, steady) — the opposite end from ED's natural thin/ballistic/determinate character. ED makes facts; fluids relax; opposite limits of one architecture.

**The bridge, forced (ThickRegime R1 + §6b):** built the thick regime and interpolated the carrier rule from pure Σ-selection (ε=0) to pure random scatter (ε=1). A clean diffusion PDE (validated D≈0.25 = analytic random-walk value) appears at **exactly ε=1**, where Σ-selection is fully replaced by scattering; for **any** ε<1 the certified rule **traps** (sub-diffusive, non-exponential mode decay, nothing closes). **The obstruction is structural, not parametric — Σ-selection is a *trapping* operator, not a *collision* operator.** The thick regime that yields a PDE is reached only by deleting ED's selection rule. **The price of the PDE is the whole ED character.**

**The legitimate route (ShadowEmergence R1 + §6c):** does *pure* ED (ε=0) cast its own shadow by **emergent mixing** — the way deterministic molecular dynamics gives diffusion *without* injected noise (so determinism per se is not the blocker)? Across 300 independent self-roughening landscapes: **no.** Persistence never decorrelates (p≈0.45, not 0.25), transport is sub-diffusive and **worsens with density** (α 0.93→0.57 — opposite of mixing), and D is scale-unstable (CV≈1.2 vs the ε=1 control's flawless CV=0.00, D=0.25, R²=1.00). **ED's determinism is committal/trapping, not mixing/chaotic** — it locks configurations rather than decorrelating them. Both routes agree: **you reach the PDE only by leaving ED.** Two description-scales (substrate beneath, continuum as its forgetful summary), not two layers of reality — now empirical, not just argued.

## Contents

| File | What |
|---|---|
| `CoarseGrain_ContinuumLimit_Paper.md` | **The paper** — consolidated Rounds 1–3, method, results, verdict, limitations, Round-4 plan |
| `coarsegrain_test.py` | Round 1 — PDE-class regression + single-chain straightness |
| `coarsegrain_round2.py` | Round 2 — `(ρ,φ,J)` transport closure; single-chain drift `v`, diffusion `D` |
| `coarsegrain_round3.py` | Round 3 — merge (collision) operator; directional persistence; scaling |
| `coarsegrain_round4.py` | Round 4 — ensemble + matched space-time coarsening; velocity-resolved BGK; UDM (mobility-vs-concentration) test |
| `coarsegrain_round5.py` | Round 5 — saturation/extinction on; extinction-rate + effective-mobility vs concentration; UDM-form test |
| `bandwidth_conservation_test.py` | Round 6 — the bridge test: faithful P04 bandwidth conservation; coarse-grain the conserved field; constitutive-current closure |
| `thick_regime_test.py` | ThickRegime R1 — force the over-damped regime; ε-sweep Σ-selection→random scatter; mode-decay + MSD + Fickian closure (the constructive bridge test) |
| `shadow_emergence_test.py` | ShadowEmergence R1 — pure ED (ε=0); does collective determinacy cast its own diffusion shadow? multi-mode scale-stability of D over 300 landscapes; ε=1 calibration |
| `docs/CoarseGrain_Round1_Results.md` | Round-1 results note (superseded by the paper for synthesis) |
| `docs/ThickRegime_Round1_Results.md` | ThickRegime Round-1 results note (the constructive bridge test) |
| `docs/ShadowEmergence_Round1_Results.md` | ShadowEmergence Round-1 results note (pure-ED mixing test; trapping not mixing) |

## Status: arc CLOSED (Rounds 1–6 + ThickRegime R1 + ShadowEmergence R1)

Qualitative kinetic characterization solid; quantitative continuum closure unachieved; UDM shares the saturation *ingredient* but not its *form*; conservation added exactly (R6) yet the current still doesn't close → **bridge located (scale separation), not crossed**. The constructive ThickRegime R1 then *forced* the over-damped regime and found a clean diffusion PDE only at ε=1 (Σ-selection fully replaced by random scatter) — for any ε<1 the certified rule traps → **structural, not parametric; the price of the PDE is the whole ED character.** ShadowEmergence R1 closed the last route — pure ED (ε=0) does **not** cast its own shadow by emergent mixing (trapping, sub-diffusive, worsens with density; scale-unstable D) → **ED's determinism is committal/trapping, not mixing/chaotic; you reach the PDE only by leaving ED.** The PDE ingredients (§6a), the two constructive tests (§6b inject-noise, §6c emerge-noise), and the verdict are in the paper. Further closure is a dedicated computational-physics project, not banked.

## The robust core (survived all three rounds, two self-corrections)

chain/worldline propagator (no branching) → ballistic free-flight + scattering off ρ-disorder → ρ is a *slaved deposition field* → **not diffusion, not a closed ρ-PDE**. R1 read it as drift-diffusion; R2 corrected to ballistic+scattering; R3 falsified R2's "merging breaks continuity" (merging is ~1%, negligible) and located the residual as measurement-limited.

## Status

Rounds 1–3 **done**. Round 4 (matched space-time coarse-graining + ensembles + velocity-resolved lattice-Boltzmann; test whether the over-damped limit is the Q-C/UDM diffusion) is a deliberate numerical study, **not** banked here.
