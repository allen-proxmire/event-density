# #5c, the Decisive Test — ED's Non-Gaussianity Is 100% in the Phases (Structure-Making, Not Mixing)

**Evaluation result — route 3 of the Gaussianity routes (the *correct* test). Sim: `evaluation/CoarseGrain_Arc/fourier_phase_test.py`. A Gaussian random field is DEFINED by random, independent Fourier phases; amplitude-Gaussianity is a trap (a CLT-in-Fourier-space makes almost any field's amplitudes ~Gaussian, since each mode is a sum over all space). The discriminator is the PHASES. Built the phase-randomized surrogate — ED's *exact* power spectrum with phases randomized = "the most Gaussian field that still has ED's power spectrum" — and compared real-space cumulants. Result: the surrogate is *perfectly Gaussian* (skew 0.003, exkurt −0.001) while ED's field is strongly non-Gaussian (skew 0.96); **100% of ED's non-Gaussianity is in the phases** (97% at R_cg=4). #5c CONFIRMED decisively (not flipped) — and sharpened: ED's field is non-Gaussian precisely because its phases are correlated, and correlated phases ARE structure (filaments).**

---

## Result (sparse seeding, strong filaments — the hardest test)

| R_cg | field | skew | exkurt |
|---|---|---|---|
| 1 | **ED field** | **0.958** | −0.325 |
| 1 | phase-surrogate (ED's power spectrum, random phases) | 0.003 | −0.001 |
| 4 | **ED field** | **0.862** | 0.317 |
| 4 | phase-surrogate | −0.007 | −0.025 |

- The surrogate keeps ED's **exact amplitudes** and only randomizes the phases → it comes out **perfectly Gaussian**. This both (i) validates the method (random phases ⇒ Gaussian, as a GRF must be) and (ii) proves the amplitude/power-spectrum carries **none** of the non-Gaussianity.
- ED's actual field — same amplitudes, ED's actual phases — is strongly non-Gaussian. So **the non-Gaussianity is entirely the phase correlations.**

## What it means

**A Gaussian field has random phases = no structure beyond its power spectrum. ED has correlated phases = structure (filaments, coherence, the committal worldlines).** So:

> "ED's coarse field is non-Gaussian" and "ED commits / builds coherent structure instead of mixing" are **the same statement** — the structure lives in the phases.

This is the sharpest formulation of the committal/trapping character: a mixing (Gaussianizing) substrate would randomize the phases; ED's commit-and-advance dynamics *align* them (that's what a filament is). The non-Gaussianity is not a defect — it is the signature of structure-making. It is the distributional face of the arrow, exactly as reversibility-vs-arrow is the dynamical face.

## For the consilience ledger / the debt

- **The Gaussianity shadow is NOT cast at this substrate layer** — the field is genuinely, definitively non-Gaussian (route 3, the decisive test). The CMB-Gaussianity debt, if ED ever pays it, is paid at a *different* layer (cosmological / inflationary, where the relevant field and the mixing are different), not at the committal substrate.
- Routes 1 (coarse-grain past the correlation length) and 2 (log-density) remain open as ways a Gaussian *description* might appear at another scale — but the field *itself* is not a GRF.
- Slots into the Atlas/pole map: ED is a **structure-making, hyperbolic-pole, phase-correlating** substrate. Gaussianity is the **structureless thermal shadow** — a floor ED doesn't reach by *building*, because building is the opposite of the mixing that erases phases.

**Crank-rail:** this CONFIRMED the prior (non-Gaussian), did not force a flip toward the hoped-for Gaussian; reported the confirm straight. The value is the *form* — 100% phase-localized — which is cleaner and more meaningful than the earlier trimming test. **Notebook documentation; no external prediction shipped (per AP).**

---

*#5c decisive test (`fourier_phase_test.py`, route 3). Phase-randomized surrogate (ED's exact power spectrum, randomized phases) = perfectly Gaussian (skew 0.003); ED field strongly non-Gaussian (skew 0.96) → 100% (97% at R_cg=4) of the non-Gaussianity is in the PHASES. A GRF has random phases (structureless); ED has correlated phases (filaments = structure). "ED non-Gaussian" = "ED builds structure / commits, doesn't mix" — same statement, the distributional face of the arrow. #5c CONFIRMED decisively, not flipped; sharpened to its cleanest form. Gaussianity debt unpaid at this layer (CMB debt, if payable, is cosmological-layer). Atlas: ED = structure-making hyperbolic-pole phase-correlating substrate; Gaussianity = structureless thermal shadow. Notebook only; no external prediction (per AP).*
