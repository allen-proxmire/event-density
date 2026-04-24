# ED Quantum Program — Project Outline

**Author:** Allen Proxmire
**Started:** 2026-04-24
**Location:** `C:/Users/allen/GitHub/Event Density/quantum/`
**Status:** Living document — updated as work progresses

---

## 0. Purpose of This Outline

A single reference document for the ED quantum work. Captures:

- Current state of what's been absorbed
- The strategic principle (primitives-first)
- The phase-by-phase work plan
- The artifact list
- Publication outlets
- The strategic logic for why each step matters

Referenced at the top of every work session so we stay oriented.

---

## 1. Current State (as of 2026-04-24)

### Papers absorbed (in `quantum/papers/`)

**Ontological backbone (five papers):**
1. ED-09 — Event Density and Quantum Behavior: Participation, Discreteness, and Relational Becoming
2. ED-10 — Emergence of Spacetime, Geometry, Information
3. ED-I-04 — Event Density and the Quantum–Classical Boundary
4. Q-C Boundary Transition: Theory, Prediction, Path (ED-09.5 quantitative layer)
5. ED-Arch-08 — ED and QM (simulation study; gamma reveals architectural quantization)

**Interpretation papers demonstrating the primitives cover phenomena:**
6. ED-I-02 — ED-Entanglement: Non-Individuation, Gradient Sparsity
7. ED-I-07 — The Double-Slit Experiment in ED Terms
8. ED-I-11 — ED-Baryogenesis: Aligned-Tension Stability
9. ED-I-12 — ED-Photonics (Yablonovitch, Pendry, Capasso)
10. ED-I-13 — ED-Quantum Information (Bennett, Brassard, Deutsch, Jozsa, Shor)
11. ED-I-14 — ED-Topological Effects (Aharonov, Berry, Bohm, Casher, Tonomura)
12. ED-I-23 — ED-Josephson Junction Physics

**Plus the ED Interpretation Chronicle** — 30+ recent physics results scored against ED, average fit 4.75/5.

### Primitives identified (the thirteen)

1. Micro-event — atomic unit of becoming
2. Chain — sequence of micro-events with a consistent update rule
3. Participation — relational substrate integrating micro-events across regions
4. Participation bandwidth — graded measure of integration richness
5. ED (event density) — scalar field measuring accumulated becoming
6. ED gradient — variation in ED across regions; drives large-scale behavior
7. Channel — stable participation pathway through ED gradients
8. Multiplicity — count/measure of viable channels in a region
9. Tension polarity — phase relation between a chain's update rule and local relaxation direction
10. Individuation — threshold condition on internal ED structure required for distinct identity
11. Commitment — irreversible selection of a single viable channel by a micro-event
12. Thickening — accumulation of committed structure producing classical stability
13. Relational timing — phase-like coupling between participation channels

These are referenced across the interpretation papers. They are not yet consolidated into one canonical reference document. That is Phase 1.

### Operational / quantitative pieces that already exist

- **Simulator**: `ED Update Rule` / Scenario E update rule, ED-Arch simulations (64² and 128²). Demonstrates architectural quantization through gamma-sweep, radius-spectra, orbit-distance, scattering-grid studies.
- **PDE layer**: ED-Phys-16, ED-Phys-17, P6, 00.3 produce specific quantitative predictions — D = 0.5 sharp transition, N_osc ≈ 9 at D < 0.1, Q ≈ 3.5, triad coupling ≈ 0.03, 3–6% third-harmonic generation, ground state energy αγρ₀, relaxation timescale ρ₀/(αγ).
- **Dimensional atlas**: referenced in the Prediction Path paper as the bridge from experiment-control-parameter x to effective channel weight D(x).

These already provide the quantitative backbone. Phase 1 consolidates the primitives that the simulator and PDE operationalize.

---

## 2. Strategic Principle

### The principle (captured from conversation 2026-04-24)

> *"If every quantum phenomenon is 'obvious once explained in ED vocabulary,' then the math aimed at deriving Schrödinger, Born, Bell is aimed at the wrong level. The right level is: formalize the primitives once, and every ED-I paper becomes a consequence. Formalize thirteen primitives once — the phenomenology falls out."*

### Why this is the correct order

- Going phenomenon-by-phenomenon (derive Bell from ED, derive Schrödinger from ED, derive Born from ED) treats each as a separate math project with QM's formalism as the target. That is *formalizing QM's outputs*, not ED's inputs. It positions ED as a supplement to QM.
- Going primitives-first positions ED as a substrate whose coarse-grainings produce QM (thin regime) and GR (thick regime) as effective descriptions. That is the actual ED claim.
- Once the primitives are formalized, every ED-I paper can cite the primitives reference rather than re-introduce them. Consistency across the framework becomes enforced.
- Future phenomena (ED-I-15 through 31 and beyond) become derivable rather than needing independent ontology.

### The principle as a one-liner

**Formalize the primitives once. The phenomenology is consequence.**

---

## 3. Work Phases

### Phase 1: Primitives Formalization (ACTIVE)

Deliverable: `quantum/primitives/` folder containing one document per primitive, each with:
- Precise definition (what it is, distinct from what it's not)
- Mathematical object or structure it maps to
- Relations to other primitives
- Experimentally-measurable quantity it corresponds to
- Example application to one or two phenomena
- Open questions / unsettled math

Plus `quantum/primitives/README.md` as the index and quick-reference.

**Status:** Phase 1 COMPLETE as of 2026-04-24 — all thirteen primitives drafted in `quantum/primitives/`.

**Estimate:** A few focused sessions. 30–50 pages of reference material total when done.

**Output form:** Markdown files. Citable from Zenodo if bundled later.

### Phase 2: Decision point — three candidate paths

After primitives are formalized, three paths are available. Not mutually exclusive; we pick based on appetite.

**Path A — QM as thin-regime effective theory.**
Show that the standard QM formalism (Hilbert space structure, unitary evolution, operator algebra, Born rule) is what the primitives produce in the thin, uncommitted regime. Not deriving QM as a target, but showing the formalism falls out as an effective description. Output: a reference document `quantum/effective_theory/qm_as_thin_regime.md`.

**Path B — GR as thick-regime effective theory.**
Parallel to A. Show that the standard GR formalism (metric, curvature, Einstein equations) is what the primitives produce in the thick, committed regime. Output: `quantum/effective_theory/gr_as_thick_regime.md`. Connects to ED-10 and the GR-SC work already done.

**Path C — Retrodiction pass.**
Use the existing PDE predictions (D = 0.5, N_osc ≈ 9, etc.) and the dimensional atlas to compute D(x) for one or two published experimental systems — Arndt molecular interferometry, Haroche cavity QED, Devoret-Martinis-Clarke superconducting qubits. Show that D(x_c) = 0.5 at the measured transition point using published data only. Output: `quantum/retrodictions/` folder with one memo per system tested.

**Recommended sequence:** C first (quickest external-credibility gain, works with published data, no new calculation needed beyond the dimensional atlas + arithmetic), then A and B in parallel (they reinforce each other).

### Phase 3: Two consolidation papers

Once Phase 1 is done and at least one Path C retrodiction lands:

**Paper α — Baryogenesis mechanism paper.**
Title draft: "Aligned-Tension Stability and the Structural Origin of Matter-Antimatter Asymmetry."
Claim: The baryon-to-photon ratio arises from ED gradient saturation in the early universe; no new particles, no enhanced CP violation, no sterile neutrinos. Falsifiers listed. Retrodicts ALPHA-g, forbids antimatter domains, explains why antimatter is stable today.
Outlet: Zenodo DOI, PhilPapers cross-post, GitHub.

**Paper β — Nineteen Nobel results under one vocabulary.**
Title draft: "A Unified Structural Reading of Modern Physics: Nineteen Nobel-Level Results Through Event Density Primitives."
Claim: Photonics (5 results), quantum information (5), topological effects (4), Josephson physics (Nobel 2025), all reinterpreted under the thirteen primitives. Plus baryogenesis as the one open-problem member of the set. Accessible to a general physics audience.
Outlet: same as above.

### Phase 4: Quantitative predictions

**Priority target: η (baryon-to-photon ratio) derivation.**
Status: hardest open target. Current value η ≈ 6 × 10⁻¹⁰. No existing baryogenesis model derives this without free parameters. If ED can produce it (or a band like 10⁻¹¹ to 10⁻⁹) from the saturation-relaxation dynamics of the ED field in the early universe, that is a publishable independent prediction.

**Secondary targets:**
- Cosmic-web filament/void statistics vs. ED gradient structure (connects to the "cosmic web = 5.0" entry in the Chronicle)
- Specific Q-C transition locations on additional experimental platforms (extension of Path C)
- Inflation from ED primitives — user noted this is easy to do in ED and is covered in one of the interpretation papers; find it and write it up

---

## 4. Publication Outlets (adjusted 2026-04-24)

**Primary:**
- **Zenodo** — DOI, timestamped, CERN-backed archive. This is the citable primary outlet.
- **PhilPapers** — for the philosophical / foundational papers, cross-posted.
- **GitHub** — working repository; every paper linked, every artifact versioned.

**Strategy:**
- Every paper gets a Zenodo DOI before any outreach.
- Outreach is always *one specific checkable claim* + one GitHub link, never a reading list.
- Target specific researchers whose experiments map to specific ED predictions (Arndt, Aspelmeyer, Haroche's group, ALPHA-g team), not broad physicist-population blasts.
- First sentence of outreach: "Your measurement of X retrodicts to Y using no free parameters under this framework. Here's the one-page derivation."

**Non-goal:** arXiv. Access blocked; not the route. Zenodo is the real primary.

---

## 5. Artifact List (current + planned)

### Current
- `quantum/papers/` — ten interpretation papers (QM-focused set)
- `quantum/PROJECT_OUTLINE.md` (this document)
- `ED_Interpretations_Chronicle.md` on Desktop — 30+ scored results
- Existing simulator, PDE memos, ED-Arch studies (outside `quantum/` folder, in broader repo)

### Planned (Phase 1)
- `quantum/primitives/README.md` — index and quick-reference
- `quantum/primitives/01_micro_event.md`
- `quantum/primitives/02_chain.md`
- `quantum/primitives/03_participation.md`
- `quantum/primitives/04_participation_bandwidth.md`
- `quantum/primitives/05_event_density.md`
- `quantum/primitives/06_ed_gradient.md`
- `quantum/primitives/07_channel.md`
- `quantum/primitives/08_multiplicity.md`
- `quantum/primitives/09_tension_polarity.md`
- `quantum/primitives/10_individuation.md`
- `quantum/primitives/11_commitment.md`
- `quantum/primitives/12_thickening.md`
- `quantum/primitives/13_relational_timing.md`

### Planned (Phase 2)
- `quantum/effective_theory/qm_as_thin_regime.md` (Path A)
- `quantum/effective_theory/gr_as_thick_regime.md` (Path B)
- `quantum/retrodictions/arndt_interferometry.md` (Path C example)
- `quantum/retrodictions/devoret_martinis_clarke.md` (Path C example)
- `quantum/retrodictions/haroche_cavity_qed.md` (Path C example)

### Planned (Phase 3)
- `quantum/papers_draft/baryogenesis_mechanism.md` (Paper α)
- `quantum/papers_draft/nineteen_nobel_vocabulary.md` (Paper β)

### Planned (Phase 4)
- `quantum/predictions/eta_derivation.md` (if achievable)
- `quantum/predictions/inflation.md`
- `quantum/predictions/cosmic_web_statistics.md`

---

## 6. Open Questions Flagged During This Pass

- **D_crit provenance.** What's the derivation of D = 0.5 from the PDE (P6 / 00.3)? Need to read those memos to confirm the calculation and trace whether an earlier value preceded 0.5.
- **UDM 10-panel format.** What's the visual/structural grammar? Any retrodiction papers should match that format rather than inventing new layouts.
- **Inflation paper location.** User indicated ED explains inflation easily and it's in one of the interpretation papers already. Find and catalog.
- **Connection from simulator parameters (α, m, γ) to PDE parameters (D, oscillation count, Q, triad).** Tight mapping needed before Phase 4 predictions can be grounded.

---

## 7. Working Cadence

- Top-of-session: re-read this outline, check current phase.
- Every new file gets committed to git with a clear message.
- Completion of each primitive document → mark it in this outline's §5.
- Completion of each phase → new section added to this outline describing what changed.
- When in doubt about scope: primitives first, applications follow. That's the principle.

---

## 8. One-Line Summary

> **ED is a framework whose thirteen primitives, once formalized, produce QM and GR as coarse-grained effective descriptions. The work is to write those primitives down cleanly, use them to retrodict published measurements, then produce at least one quantitative prediction (baryon-to-photon ratio η being the priority target) that no existing framework derives without free parameters.**
