# The Matter-Wave "Arrangement" Prediction Is Gated on a Structure→Channel-Bandwidth Map (and So Are the Singularity Caps)

**Date:** 2026-07-24
**Status:** Working note (finding, adversarially reviewed). Documents where the matter-wave quantum-to-classical weapon's *directional* prediction actually stands, and names the single missing construction that gates it — the same construction that gated the singularity-family caps this session.

---

## The question

ED's strongest testable weapon is the matter-wave Q-C wall (Paper_056, `M_eff = M_cap`; Paper_060). Its *distinctive* content — the part no mass-based rival (standard QM, CSL, Diósi–Penrose) can match — is that the wall is set by **internal multiplicity/arrangement, not mass**: two objects of the *same mass* but different internal arrangement should hit the wall at different points. Confirmed this session that this is genuinely ED's mechanism (`M_eff` is an inverse-participation-ratio over channels, an arrangement quantity), not an overlay — see the earlier pressure-test.

To be a *falsifiable* weapon it needs a **direction**: for a maximally-controlled pair — **folded vs unfolded protein** (same atoms, same covalent bonds, same mass; only non-covalent tertiary contacts differ) — which state has higher `M_eff` and hits the wall (goes classical) first?

## The attempt and verdict — INDETERMINATE (adversarially checked)

Attempted the direction via the `M_eff = (Σ_K b_K)²/(Σ_K b_K²)` definition. Provisional lean was "folding correlates channels → lowers the effective independent count → *unfolded* hits the wall first." **The adversarial check refuted the lean and returned INDETERMINATE, on four grounds:**

1. **The IPR premise is one of two regimes, not forced.** In the plain site basis, folding leaves the marginal `{b_K}` unchanged → `M_eff` unchanged. Any effect requires moving to the collective-mode basis, and there bandwidth may *concentrate* (dominant Perron mode → lower `M_eff`, the lean) **or** *spread* (disordered coupling, GOE-eigenvector regime → higher `M_eff`, against it). ED says nothing about which regime a real contact graph lands in.
2. **Basis pinned only in *type*, not in the assignment.** The einselection result (`StateReduction_ChannelGranularity.md`) pins the channel basis to "einselected / environment-set / operationally-distinguishable coarse" — a real constraint — but its residual #2 flags the floor as environment-/regime-dependent and *not yet quantified*. So the actual `{b_K}` induced by folded vs unfolded in a given interferometer is exactly the unwritten map.
3. **ED's own two papers point OPPOSITE ways.** Paper_056's **IPR** framing leans *unfolded*-first (more independent channels). Paper_060's **"internal-rule-type-content"** framing leans *folded*-first (folding *adds* contacts = more coupling relations = more rule-type content → saturates `M_crit` sooner). The corpus contradicts itself on this molecule and supplies no map to adjudicate.
4. **The conformational-freedom support was a category error.** Thermodynamic conformational entropy (classically accessible microstates, a *mixture*) is not the coherent-superposition channel count `M_eff` measures; and to the extent floppy internal modes matter they feed *decoherence*, which Paper_056 §7.3 explicitly excludes as "not the wall."

**Net: ED does not currently determine whether folded or unfolded goes classical first.** Neither direction is an ED prediction; presenting either would be over-banking. The process worked — the lean was flagged provisional and killed by review before it was banked.

## The named gate — a structure→`{b_K}` map

Everything above reduces to one missing construction:

> **A derived map from a real object's physical structure (atoms, bonds, 3D contact topology) to its substrate channels and their bandwidths `{b_K}` in the einselected basis.**

Paper_056 §3.2 collapses all structural content into `M_eff(m) ≈ αβ(m/m_u)` and §8.2/§8.6 declare `α, β` **empirically inherited, not derived**. Folded/unfolded (identical `m`, atoms, `N_DOF`) live *entirely* inside those inherited coefficients. Until the map exists, the arrangement-direction — the weapon's only-ED, falsifiable core — cannot be called.

## Cross-cutting: this is the same gap that blocked the singularity caps

This is the **fourth** time in the 2026-07-24 session that a high-value thread bottomed out at the *same* missing construction:
- The finite-grain singularity family's density cap `ρ_max` (`FiniteGrain_Singularity_Lemma_Attempt_2026-07-24.md`) — the derivation failed because ED lacks a map from a collapsing configuration to a local per-cell density/capacity.
- The matter-wave arrangement-direction (this note) — blocked on structure→`{b_K}`.

Both are instances of **"how does ED represent a specific real physical configuration as substrate channels + bandwidths."** That map is ED's single most load-bearing current gap, and it surfaced independently from gravity/PDE singularities *and* from the strongest laboratory prediction. See the research target logged from this note.

## Honest status of the matter-wave weapon

- **Mechanism** (arrangement, not mass, sets the wall): confirmed, genuine ED.
- **Distinctiveness vs standard QM** (a sharp fundamental wall vs no wall): real.
- **Directional prediction** (which arrangement dies first — the only-ED, falsifiable part): **blocked on the structure→`{b_K}` map, and not internally settled (Paper_056 vs Paper_060 disagree).** A research frontier, not a near-term deliverable.
- **Second-harmonic fingerprint** (Paper_056/proposal: 3–6% second-harmonic vs decoherence's pure exponential): **NOT blocked on the map.** A separate, map-independent distinctive observable, plausibly checkable in existing Fein-2019 / Jan-2026-nanoparticle interferometry data. This is the near-term actionable test.

**External note (real-source check, July 2026):** matter-wave interference is now demonstrated at ≥170 kDa (sodium nanoparticles, ~7,000 atoms; Nature 2026, `s41586-025-09917-9`), *inside* the 140–250 kDa extrapolated window. Standard-QM-consistent so far (interference preserved). This makes the wall imminently testable but also means the bare mass-window is under pressure from below; the distinctive weapon is the arrangement-dependence (map-gated) and the second-harmonic (map-independent), not the bare number.

## Cross-references
- `ED Generative/physics-papers/q-compute/Paper_056_ClassA_Wall.md` (§3.1 `M_eff`; §3.2, §8.2/§8.6 α,β inherited; §7.3 decoherence≠wall); `Paper_060_Mcrit_Unification.md` (§3.1 "internal-rule-type-content" — opposite lean).
- `ED Generative/physics-papers/state-reduction/StateReduction_ChannelGranularity.md` (einselected coarse basis; residual #2 environment-dependence).
- `ED Generative/physics-papers/predictions/QC-Mass-Extrapolation_InProcess/proposal.md` (the second-harmonic distinguishing test; the pre-registered protocol).
- `theory/FiniteGrain_Singularity_Lemma_Attempt_2026-07-24.md` (the singularity-cap instance of the same missing map).
- Research target: `docs/ED_Research_Targets.md` (the structure→`{b_K}` map, logged from this note).
