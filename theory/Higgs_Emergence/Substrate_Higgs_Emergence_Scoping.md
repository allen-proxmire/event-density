# Substrate-Higgs Emergence — Scoping and First Probe

**Status:** Scoping memo, 2026-07-05. Frames the open substrate-Higgs question sharply enough to run, decomposes it into a tractable ladder, and specifies a grounded first probe on the real ED simulator.

**E1 HAS RUN (2026-07-05), and its first headline was RETRACTED.** Result in `E1_MassFromStructure_Results.md`. Corrected headline: on the certified substrate's native ρ-field, **H2 does NOT give a mass.** An initial read claimed isotropic patterning grounded a σ_τ-like mass; a second-session cross-check pushed two fixes (correlation-length sweep + extinction-immune paired test) that overturned it. What the substrate actually does: uniform → nothing (blindness confirmed); anisotropic → a **crystal** (channeling); isotropic → **worldline termination at gradient peaks** (extinction, late-time), NOT a propagation mass — there is no early-time velocity gap (extinction on or off), and a σ_τ mass would slow the front from t=0. So substrate-Higgs via H2/σ_τ is **not grounded** on the reference substrate; `Paper_113` row 10 stays OPEN. Two things survived: the **field-mapping correction** (Σ reads ρ, not edge bandwidth — §4 is written to it) and the structural finding that **the certified substrate has no amplitude-invariant native field** for σ_τ to live on. Next is NOT E2; it is the H1 (inserted-τ_H, mass-from-amplitude-coupling) leg + kicking the σ_τ-faithfulness gap upstream to Arc M.

**Provenance.** Opened off the 2026-07-05 corpus-dive open-targets map (`docs/ED_Open_Targets_Map_2026-07-05.md`, target A5 + §C). The substrate-Higgs mechanism is the M2-downgrading OPEN flag on `Paper_113` (audit row 10) and the ADMISSIBLE-CLEAN-but-not-forced verdict of Arc Q Stage Q.4 (`arcs/arc-Q/higgs_mechanism_scoping.md`). Both stop at "ED can host a Higgs; it does not force one." This memo asks the next question: does an electroweak-symmetry-breaking structure **emerge** from the substrate, or is it **inserted**? And it isolates the one place where ED's own machinery says something sharp and ED-specific about it.

---

## 1. What is closed, and what is open

**Closed (do not re-litigate):**
- The enumeration. Q.4 evaluated five candidate mechanisms and gave a clean verdict: **H1** scalar rule-type τ_H (ADMISSIBLE-CLEAN), **H2** patterned-bandwidth condensate (CANDIDATE), **H3** composite ⟨Ψ̄Ψ⟩ condensate (ADMISSIBLE-EFFECTIVE), **H4** gauge-fixing artefact (REFUTED), **H5** vacuum-anchored (reduces to H1/H2). ED hosts SSB cleanly; it does not select a mechanism. That is settled and correct.
- The structural skeleton of mass. Arc M's σ_τ bandwidth-signature is Lorentz-scalar, amplitude-invariant, energy-dimensional; gauge masslessness (MR-P) and chiral masslessness (MR-R) are the two structural σ_τ = 0 slots. Form-forced; values inherited.

**Open (the target):**
- **Emergence.** All of H1/H2/H3 are "admissible" because ED can *carry* them. None is *forced* or shown to *emerge* from coarse-graining the microrule. The Higgs sector is, at present, a thing ED permits you to install, not a thing the substrate produces. `Paper_113` rows 10 (substrate-Higgs) and 11 (substrate-Yukawa) are OPEN for exactly this reason, and they are what hold the mass paper at M2 instead of M3.
- This is not a values question. Nobody expects ED to output 125 GeV. The open question is whether the *mechanism form* (a symmetry-breaking ground state that gives gauge bosons a mass term) is an output of the substrate or an input to it.

---

## 2. The ED-native handle: the log-derivative blindness, and the fork it exposes

This is the one place ED's own machinery says something sharp, ED-specific, and testable about the Higgs. It is worth stating precisely, because the existing scoping half-buries it.

Arc M's mass functional is

  σ_τ = ℏ · √( Σ_X w_τ^X · ⟨ (∂_μ ln b_τ^X)(∂^μ ln b_τ^X) ⟩_τ ).

The mass reads the **log-derivative** of the bandwidth field, `∂_μ ln b`. By construction (selection criterion SC2) this is **blind to any uniform rescaling** `b → α b`, since `∂_μ ln(α b) = ∂_μ ln b`. A condensate that raises the bandwidth amplitude uniformly everywhere changes nothing about σ_τ. **A uniform condensate cannot give mass through the ED bandwidth-signature route.** Mass through this route requires a *spatially patterned* condensate `δb(x)` whose gradients feed the integral. This is a real, primitive-level, ED-specific constraint (Q.4 §7.2), and it is the crux.

**The fork it exposes (a clarifying result, not yet drawn out anywhere).** The Standard Model gives gauge bosons mass from a *uniform* VEV, ⟨φ⟩ = v everywhere. It works because the mass comes not from any gradient of φ but from the covariant-derivative vertex |D_μφ|² = |(∂_μ − igA_μ)φ|², where the gauge field A_μ enters even when ∂_μφ = 0, leaving g²v²A_μA^μ. So the two ED candidates are physically *different animals*:

- **H2 (σ_τ route):** mass = bandwidth-signature of the propagating rule-type itself. **Blind to uniform b. Requires patterning.** Distinctively ED. Structurally *unlike* the SM.
- **H1 (τ_H |D_μφ|² route):** mass = gauge coupling to a scalar rule-type's amplitude. **Uniform amplitude works**, exactly as in the SM, but only because you have *inserted* the scalar rule-type τ_H and its |D_μφ|² vertex by hand.

So the blindness is not a bug and not a side note. It is the thing that **separates ED's two Higgs candidates into two genuinely different mechanisms**, and it forces a clean dichotomy for the emergence question:

> Either (H2) ED mass-generation is intrinsically a **patterning/gradient** phenomenon, in which case the "condensate" is spatially structured and possibly leaves a fingerprint the SM's uniform VEV does not — a candidate ED-distinctive claim; or (H1) gauge-boson mass routes through an **inserted** τ_H vertex, in which case the emergence question reduces to "does a scalar rule-type with a |D_μφ|² coupling emerge from the microrule," which is a rule-type-genesis question, not a condensate question.

Drawing that dichotomy cleanly, and testing the H2 leg on the real substrate, is the work.

---

## 3. The emergence question, decomposed into a runnable ladder

Emergence is too big to attack whole. Three rungs, increasing difficulty, decreasing tractability. Each is honestly labelled for what a positive result would and would not establish.

**E1 — Mechanism (runnable now).** *Does patterned bandwidth structure actually produce an effective-mass propagation signature on the real substrate, and does it scale as σ_τ predicts, while a uniform condensate produces none?*
This tests the H2 leg directly and grounds the log-derivative blindness as a measured fact rather than an analytic assertion. It is a build-and-run on `evaluation/Bits/simulator.py` (spec in §4). Positive result: ED's bandwidth-signature mass mechanism is real and quantitatively σ_τ-shaped on the substrate, and the uniform-blindness is confirmed by control. This **grounds the mechanism half of H2** and upgrades the σ_τ → mass link from "analytic form" to "measured on the substrate." It does **not** show the pattern forms spontaneously (that is E2), and it does **not** touch H1.

**E2 — Formation (the hard, shared rung).** *Does a symmetry-breaking bandwidth configuration ⟨b⟩ ≠ 0 with the gradient structure E1 needs arise spontaneously from the microrule, or must it be installed as an initial condition?*
This is the actual "spontaneous" in SSB. It is the same open piece as the emergent-ordering / emergent-stiffness question that curvature-emergence and the Bullet order-parameter arc both bottom out on (see `docs/ED_Open_Targets_Map_2026-07-05.md` substrate-evaluation target, and `theory/Bullet_Cluster/Paper_ED_Bullet_Phase3_EmergentFreeEnergy.md`): does an ordering coupling *emerge* from coarse-graining, or is it an assumed input? The Higgs "does the condensate form" question is one face of that shared bridge. It is not runnable as a clean could-say-no until E1 fixes what signature we are even looking for. **Do not attempt E2 before E1.**

**E3 — Selection (expected to stay empirical).** *Which subgroup stays unbroken (SU(2)×U(1) → U(1)_em), the specific breaking pattern, the multiplet content.* Q.4 §6.8 already lists these as empirical; nothing in the dive suggests otherwise. Park it.

The recommendation is E1, alone, first. It is the only rung that is both runnable now and a clean could-say-no, and its result decides whether E2 is even the right next question or whether the H1 (inserted-τ_H) leg is where the emergence question actually lives.

---

## 4. The E1 probe — specification (grounded, no stand-in)

**Grounding discipline (why this is not a φ⁴ crank-leak).** The probe sets an **allowed substrate initial condition** — the per-edge `bandwidth` on the participation graph, which is already a settable parameter in `simulator.py` (currently uniform 0.5) — and then runs the **certified `step()`** with the standard `SigmaCoeffs`. It adds no new coupling, no new term, no double-well potential. It reads a **propagation observable** off the commit sequence. The only manipulation is the bandwidth *landscape*, which is a legitimate initial condition, exactly as the curvature-emergence probes set a bandwidth profile and read the induced geometry (`evaluation/CurvatureEmergence/metric_from_bandwidth_probe.py`). This keeps us testing ED's real simulator, not a hand-built proxy (the standing discipline in the memory).

**Setup.**
1. Build a 2D participation graph (as the blindness/curvature probes do). Two arms, identical except for the bandwidth landscape:
   - **Uniform arm (control):** all edge bandwidths = b₀.
   - **Patterned arm:** edge bandwidths b(x) = b₀ · (1 + A·profile(x)), where `profile(x)` is a smooth spatial pattern (e.g. a slab, a sinusoid, or a localized well) with tunable amplitude A and length-scale λ. Crucially, choose profiles that hold the *mean* bandwidth fixed across arms, so any difference is from **gradient content**, not amplitude — this is the whole point of the blindness.
2. Seed active nodes on one side; let commitment propagate across the landscape under the certified dynamics.

**Observable (the "effective mass").** Mass shows up as a modification of free propagation. Measure the commit-front propagation across the graph and fit a dispersion: a free (massless) worldline propagates ballistically (front position ∝ t); an effective mass shows as a departure — a slowing, a gap/threshold in the commit rate, or a dispersive spread — quantified as an effective m_eff extracted from front kinematics or the commit-rate spectrum. (Exact estimator to be pinned in the build; candidates: front-velocity deficit vs the massless control, or a low-`k` gap in the spatial commit-rate transform.)

**Predictions (the could-say-no):**
- **Uniform arm → m_eff ≈ 0** (within the massless-control band). If the uniform arm shows a mass, the σ_τ log-derivative form is wrong, and the whole bandwidth-signature route is in trouble. Sharp kill.
- **Patterned arm → m_eff > 0**, and, across a sweep of (A, λ), **m_eff² should track the gradient integral** ⟨(∂ ln b)²⟩ that σ_τ names — i.e. grow with A, grow as λ shrinks (steeper gradients), and be *invariant under a uniform rescale* of the whole landscape b → αb (re-run with α = 2, expect no change). That last invariance is the blindness itself, measured.
- A monotone m_eff-vs-gradient relation with the right rescale-invariance is a **positive**: the mechanism is grounded. A patterned arm that stays massless, or an m_eff that responds to uniform rescaling, is a **negative** that falsifies the σ_τ mechanism on the substrate.

**Confound watch (learned from the micro-stiffness probe's extinction confound).** The `SigmaCoeffs` include an `extinction_threshold`; steep bandwidth wells can collapse commit density and *look* like a mass while actually being extinction. Guard: track the surviving commit count per arm and per (A, λ); if the patterned arm's signal correlates with extinction rather than with the gradient integral at fixed survival, the "mass" is a collapse artefact, not σ_τ. Report survival alongside m_eff, always. Do not read a positive through an extinction cliff.

---

## 5. Honest scope — what a clean E1 pass would and would not buy

**Would buy:** the H2 mechanism, grounded on the real substrate; the log-derivative blindness as a measured invariant (not just an SC2 design choice); `Paper_113` row 10's "asserted" softened to "mechanism grounded, formation open" — a real, defensible step off the M2 floor for the H2 leg; and the clean H1-vs-H2 dichotomy of §2 promoted from prose to a tested distinction.

**Would not buy:** spontaneous formation (E2), the SM breaking pattern (E3), any mass *value*, or the H1 leg. It also would not by itself resolve whether nature's Higgs is the ED-distinctive patterned kind (H2) or the SM-like inserted kind (H1); it establishes that IF it is H2, the substrate delivers the mechanism. The emergence headline stays partly open; what changes is that its mechanism half stops being an assertion.

This is the same posture as the rest of the corpus and the reason it is worth doing: form grounded, formation and value honestly still owed.

---

## 6. Recommended next action

Build the E1 probe as `theory/Higgs_Emergence/mass_from_patterned_bandwidth_probe.py` against `evaluation/Bits/simulator.py`, run the uniform-vs-patterned dichotomy with the (A, λ, α) sweep and the survival guard, and write the result as a working-repo findings doc. If E1 comes back positive and clean, the next question is E2 (formation), and it should be run jointly with the curvature-emergence / Bullet emergent-ordering probes, since it is the same shared bridge. If E1 comes back negative, the σ_τ mechanism is falsified on the substrate and the emergence question moves entirely onto the H1 inserted-τ_H leg — itself a clarifying outcome worth having.

**Crank-guards (standing):** set only the bandwidth landscape and read a propagation observable; never add a potential or coupling; hold the mean fixed so the effect is gradient-not-amplitude; report survival to rule out extinction; translate every step back to plain substrate language; and state at the end exactly which rung (E1/E2/E3) the result touches, claiming nothing above it.
