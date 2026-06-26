# #2 Charge → Maxwell — Does ED's Coarse-Graining Select Maxwell? Honest NO (the committal/trapping wall again)

**Evaluation result — answers the one open question of the B4 charge paper (§7): *does ED's DCGT coarse-graining select the Maxwell-action configuration as the continuum expectation of the holonomies?* Sim: `evaluation/B4_Arc/maxwell_continuum_test.py` (built on the B4 `relaxation_test.py`). Method: ensemble-average the gauge-invariant deficit field over many **ED-as-built** commit configs (orientation-blind Σ relaxed, **P11 kept / irreversible**, random commit orders), and compare to the **Mod-B XY-relaxation** target (P11 broken = the Maxwell-action minimizer, deficit·r² ≈ 0.126 = Coulomb 1/r²). Result, nuanced: **the angular (gauge) ambiguity washes out — the ensemble becomes isotropic — but the radial profile is NOT Coulomb: deficit·r² grows with r (0.22→6.7 vs the flat 0.126 of Maxwell) and sits far above the minimizer, dominated by residual *trapped incoherence*.** So **ED's committal coarse-graining does not select Maxwell.** The per-edge ambiguity is gauge (confirmed), but P11's commit-once traps high-action incoherence that ensemble-averaging removes *angularly* (gauge) yet not *radially* (physical). Maxwell is the thermal/action-minimizing limit (Mod-B = removing P11), which is **not** ED's dynamics — the same wall as diffusion (#3) and Gaussianity (#5c): ED's committal substrate doesn't sample the thermal ensemble the standard continuum object lives in.**

---

## What was tested

The B4 paper realized charge = integer winding (topological skeleton, M3) and located the Coulomb field one coarse-graining layer up, leaving §7's question: at the discrete layer a single ED-as-built commit gives a sweep-dependent anisotropic *seam* (no determined field), but in lattice gauge theory the determined field is the gauge-invariant **ensemble expectation** of the link variables. So: does the ensemble-average of ED-as-built configs (P11 kept) converge to Coulomb 1/r², or not?

- **Target (Maxwell):** Mod-B XY relaxation (orientation-blindness *and* P11 removed) — the action minimizer — gives isotropic **deficit·r² ≈ 0.126** (Coulomb 1/r²). Confirmed.
- **Test (ED):** ensemble-average the deficit field over `N` ED-as-built configs (orientation-blind Σ, **P11 kept**, random commit orders = sampling the gauge orbit). Does it reach the target *without* breaking P11?

## Result

| N (ensemble) | deficit·r² at r = [3,6,12,24] | flatness (cv) | isotropy (cv @ r=12) |
|---|---|---|---|
| 1 | [0.00, 1.18, 3.29, 2.46] | 0.72 | 1.87 |
| 8 | [0.21, 1.02, 2.68, 6.75] | 0.94 | 1.20 |
| 32 | [0.18, 0.96, 2.72, 6.58] | 0.95 | 0.57 |
| 128 | [0.22, 0.95, 2.97, 6.72] | 0.93 | **0.28** |
| *Maxwell target (Mod-B)* | *[0.18, 0.14, 0.13, 0.13]* | *~0.1* | *~0.01* |

Two clear, opposite movements as the ensemble grows:

1. **Isotropy emerges (the gauge part of §7 confirmed).** The angular spread of ⟨deficit⟩ at fixed r collapses (cv 1.87 → 0.28). The per-config *seam location* is gauge-redundant — different commit orders put the seam in different places — and it washes out under ensemble-averaging, exactly as the lattice-gauge reframe predicts. So the "per-edge config is gauge freedom" claim is borne out.
2. **The radial profile is NOT Coulomb (Maxwell selection fails).** For 1/r², deficit·r² is *constant* (the Mod-B target, flat ≈ 0.126). The ED ensemble's deficit·r² instead **grows with r** (0.22 → 6.72) and is **10–50× above** the Maxwell minimizer. The ensemble is dominated not by the winding's Coulomb field but by **residual trapped incoherence** — the committal seam energy that P11's commit-once locks in and never relaxes.

## MAJOR CORRECTION (AP's reframe) — the "no" was a field-vs-entropy measurement error; the coherent part IS Coulomb

`maxwell_coherent_decomp.py`. The test above averaged the **deficit** (energy ~ (∇φ)²) = coherent-field energy **+** incoherent trapped disorder, and reported the *sum* as non-Coulomb. AP's reframe: coarse-graining *is* losing the arrow, which should **relocate to entropy** — the trapped incoherence is the thermodynamic content, and the *coherent* part may be clean Maxwell. Tested by separating them (average the **field** ⟨e^{iφ}⟩, not the energy):

| | r=3 | r=6 | r=12 | r=24 |
|---|---|---|---|---|
| Maxwell ref (Mod-B) | 0.18 | 0.14 | 0.13 | **0.126** |
| total deficit (the old "no") | 0.22 | 0.95 | 2.97 | **6.72** |
| **coherent field only (N=128)** | 0.25 | 0.23 | 0.19 | **0.165** |
| incoherence 1−|⟨e^{iφ}⟩| (N=128) | 0.88 | 0.76 | 0.50 | **0.135** |

- The **coherent field deficit·r² → ~0.17**, trending to the 0.126 Maxwell value as N grows (vs 6.7 for the un-separated total) — **the coherent part is approximately Coulomb.**
- The **incoherence is concentrated near the source (0.88) and falls toward 0 far away (0.135)** — clean Coulomb far field, disorder/heat near the core = **the entropy.**

**So CGing ED gives Maxwell (coherent) + entropy (incoherent) — the inverted stack working correctly, not a wall. The earlier "no" summed the field and the entropy and called the sum non-Maxwell — a measurement error.** Honest tier: strongly supported, trending right, **not yet tight** (N=128, ~70% coherent, coherent deficit·r²~0.17 not exactly 0.126 — needs more configs / bigger box). And **#3 (diffusion) and #5c (Gaussianity) are not yet re-checked this way** — the strong hypothesis is they flip the same way (signal+disorder summed). Read the rest of this doc (the §Result "no" and the committal-wall framing) as **superseded by this decomposition**, kept for the record.

## Refinement (AP's catch): the blocker is *advance-vs-relax*, not *commit-once-vs-re-commit*

A sharper framing, prompted by the question "isn't a re-adjustment just another commitment?" — and checked against the certified rule (`Bits/simulator/update.py`):

- The certified `apply_update` is **commit-and-advance**: score candidates → tie-break → **commit at the winner (irreversibility chokepoint)** → **advance the front** (`active u→v`). A worldline that commits and moves on; ρ accumulates from passing fronts.
- So **re-commitment does happen** — a node can be committed by multiple fronts; it is *not* strictly "commit-once-and-freeze" (the Mod-A sweep was a simplification on that point). And a fresh commitment doesn't reverse a prior one or recover lost information, so it does **not** violate per-step P11 irreversibility. AP is right that far.
- **But the certified re-commits *advance* (forward worldline deposit); they do not *relax* (re-negotiate toward neighbour-coherence).** The front never sits and settles to balance. **Advance-not-relax is the macro arrow.** Maxwell is the *relaxing* limit (Mod-B: sit and re-negotiate to equilibrium = the arrow-free, time-symmetric state); the certified rule is the *advancing* limit (move on, deposit, trap).

So the blocker is not "commit-once" (re-commit happens) — it is **advance vs relax**. A re-commitment that *advances* keeps the arrow and traps; one that *relaxes toward coherence* dissolves the arrow and reaches Maxwell. The certified rule advances (and the CoarseGrain arc independently measured these front dynamics as trapping/non-mixing), so the result is confirmed against the *actual* rule, not just the simplified sweep. This is the cleaner statement of the §6 wall below.

## Why: the committal/trapping wall

§7's hope was that the expectation is "dominated by low-action (coherent) configurations" — i.e. the *thermal* (Gibbs-weighted) ensemble, which gives Maxwell by construction (low action = Coulomb). But ED's dynamics are **committal/trapping, not thermal** (the CoarseGrain/Shadow arc; #5c). The orientation-blind commit-once locks each node to the coherent mean of *whatever was already committed* — and P11 forbids the re-adjustment that relaxation to the action minimum needs. So ED traps in **high-action** configs (deficit far above the minimizer), and ensemble-averaging over commit orders removes the *gauge* (angular) part but leaves the *physical* trapped incoherence (radial). The thermal ensemble (Mod-B, = removing P11) reaches Maxwell; ED's own dynamics do not sample it.

This is the **same wall** as:
- **#3 diffusion** — ED's certified substrate is a kinetic lattice-gas, not a diffusion PDE ("you reach the PDE only by leaving ED").
- **#5c Gaussianity** — ED's coarse field is non-Gaussian; the CLT route is blocked by committal/trapping ("locks configs, doesn't decorrelate").

All three: the standard continuum object (Maxwell field / diffusion PDE / Gaussian field) is the **thermal/reversible** limit, and ED's arrow-bearing committal substrate **doesn't sample it** — it lives "a model/layer up," reached only by removing the commitment irreversibility that makes ED ED.

## Verdict

**#2's open §7 question — does ED's coarse-graining select Maxwell? — answers NO.** The angular (gauge) ambiguity washes out under ensemble-averaging (confirming the lattice-gauge reframe's "per-edge config is gauge freedom"), but the radial profile is not Coulomb: P11's committal trapping leaves high-action incoherence that ensemble-averaging cannot remove, so the ED-as-built expectation is isotropic-but-non-Maxwell, far above the action minimizer. **The Coulomb field is real but lives in the thermal/action-minimizing limit (Mod-B = removing P11), not in ED's committal coarse-graining** — the same committal/trapping wall as #3 and #5c. This also informs MS-I's open item (the Yang–Mills/F² action via DCGT): ED's *committal* coarse-graining does not select the YM action; the thermal limit does. Honest could-say-no: it could have washed out to Coulomb (it didn't); the gauge part confirmed, the Maxwell-selection part refuted.

**Honest scope:** one arena (L=61, w=1, single winding), one coarse-graining (uniform ensemble over random commit orders); the deficit-grows-with-r is robust across N=8/32/128, and the Mod-B Coulomb control on the *same* box rules out a finite-box artifact. A thermal (action-weighted) ensemble would give Maxwell by construction — but that is the standard-LGT thermal limit, not ED's dynamics, which is exactly the point.

---

*#2 charge→Maxwell, §7 open question (`maxwell_continuum_test.py`). Ensemble-average the gauge-invariant deficit over ED-as-built commit configs (orientation-blind, P11 KEPT, random orders) vs the Mod-B XY target (P11 broken = Maxwell minimizer, deficit·r²≈0.126=Coulomb). Result: isotropy EMERGES (iso cv 1.87→0.28 as N grows — angular seam is gauge, washes out, confirming the lattice-gauge reframe) BUT deficit·r² GROWS with r (0.22→6.72, vs flat 0.126) and sits 10-50× above the minimizer — dominated by residual TRAPPED INCOHERENCE. So ED's committal coarse-graining does NOT select Maxwell: the gauge (angular) part washes out, the committal/trapping (radial) part doesn't. Maxwell = the thermal/action-minimizing limit (Mod-B = removing P11), NOT ED's dynamics — same wall as #3 diffusion + #5c Gaussianity (the standard continuum object lives in the thermal limit ED's arrow-bearing committal substrate doesn't sample). Informs MS-I's open YM-action-via-DCGT item: committal coarse-graining doesn't select the F² action either. Could-say-no: could have washed out to Coulomb, didn't; gauge part confirmed, Maxwell-selection refuted. Scope: one arena/winding/coarse-graining; deficit-grows robust across N; Mod-B control rules out box artifact. No Maxwell faked.*
