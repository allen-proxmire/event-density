# Memo-02 — Bullet_Arc Phase-2 Integration

**Arc:** Bullet_Arc (ED-Bullet-01)
**Memo:** 02 (Phase-2 integration and closure)
**Status:** Phase-2 COMPLETE; Phase-3 entry
**Date filed:** June 2026
**Author:** Allen Proxmire
**Integrates:** D2.1 (`Paper_ED_Bullet_VacuumManifold.md`), D2.2 (`Paper_ED_Bullet_WindingNumber.md`), D2.3 (`Paper_ED_Bullet_RelaxationTime.md`), Synthesis (`Paper_ED_Bullet_TopologicalDefect.md`)
**Supersedes scope tracking in:** Memo-00 (scoping), Memo-01 (Phase-2 plan)

---

## 1. Purpose of Memo-02

**Phase-2 of the Bullet_Arc is complete.** The three Phase-2 deliverables — D2.1 (topology), D2.2 (dynamics), and D2.3 (numerical closure) — have each been delivered in full, and the Phase-2 synthesis paper integrating them has been written.

This memo is the internal integration document. It is distinct from the synthesis paper in audience and function:

- The **synthesis paper** (`Paper_ED_Bullet_TopologicalDefect.md`) is the *public-facing* statement of record — accessible, non-technical, written to be cited and read without the derivations. It is the document the program presents externally.
- This **memo** is the *internal* integration — directive, structured, written for the ED research program itself. It records what Phase-2 established, what the program now stands behind, what remains open, and what Phase-3 must do.

Memo-02 closes the Phase-2 scope opened in Memo-00 and planned in Memo-01, and it defines the Phase-3 observational program. It is the hand-off document from the theoretical phase of the arc to the observational phase.

---

## 2. What Phase-2 Established

### D2.1 — Topology

D2.1 (`Paper_ED_Bullet_VacuumManifold.md`, 11 sections) identified the substrate's organizational order parameter at cluster scales as a unit vector field on the vacuum manifold *S²* — the field of channel orientations, taking values on the sphere of directions. The decisive structural fact is that the second homotopy group of this manifold is non-trivial: π₂(*S²*) = ℤ. The field can wrap the sphere of orientations an integer number of times around a point in space, and each wrapping is a stable, topologically protected point defect — a monopole, labeled by an integer winding number.

D2.1 constructed the effective Lagrangian for this order parameter, identifying each term as forced by an ED substrate primitive or by the V5 outer-scale machinery, and showed that a fast cluster merger drives the field through a Kibble-Zurek quench that traps monopole defects. It established the kernel-portability profile (the topology is kernel-independent; the formation dynamics is V5-native) and verified cosmological-rate consistency: the predicted defect-formation rate is consistent with the observed merging-cluster population, the mechanism predicts no orphan lensing peaks, and the defects contribute negligibly to the cosmological mass budget. The recommended candidate — a vector field on *S²* supporting point-monopole defects — survived all four selection criteria where five alternative order parameters did not.

### D2.2 — Dynamics

D2.2 (`Paper_ED_Bullet_WindingNumber.md`, 7 sections) defined the conserved topological charge — the winding number — and verified its conservation under all four required conditions: as a mathematical identity, under the equations of motion, at the substrate grain cutoff, and under the V5 outer-scale coupling. It established that conservation *forces* pair production: because the total winding number is zero before the merger and cannot change through any smooth process, defects must form in monopole-antimonopole pairs of total charge zero. This is the topological origin of the Bullet's two-peak lensing signature — the two peaks are the two halves of a single conserved-charge pair, not two independent objects.

D2.2 then derived the complete post-formation evolution. Each defect advects with its subcluster's collisionless galaxies — which carry the organizational orientation through the merger — rather than with the ram-stripped gas, placing the lensing peaks with the galaxies and offset from the gas. The pair separates with the outgoing subclusters far faster than it can annihilate; the annihilation timescale exceeds the age of the universe by many orders of magnitude. And the observable signature is decoherence-limited, not annihilation-limited: the conserved winding persists indefinitely, but the extended coherent field that makes it gravitationally visible relaxes over the substrate organizational relaxation time, so the lensing signal fades while the charge remains. This resolved the apparent tension between an exactly conserved integer charge and a finite-lifetime observable.

### D2.3 — Numerical closure

D2.3 (`Paper_ED_Bullet_RelaxationTime.md`, 7 sections) closed the numerical content that D2.1 and D2.2 left open. It derived the substrate organizational relaxation time from substrate primitives — the Planck-scale organizational stiffness and the cosmological outer-scale quench coupling — arriving at τ_relax of order a billion years (interface-enhanced). It closed the five Lagrangian constants and produced the three headline numbers: the defect-formation threshold v_crit of order 150 km/s (the Bullet is roughly twenty times supercritical), the Kibble-Zurek freeze-out length ξ_KZ of order 860 kpc (matching the observed ~700 kpc peak separation within about twenty percent), and the full three-regime offset-velocity law.

The offset-velocity law — zero offset below v_crit, near-linear growth above it, saturation at ξ_KZ for the fastest mergers — reproduces both the Bullet's ~700 kpc lensing-peak separation and its ~110 kpc per-subcluster gas-lag offset from a single underlying scale (the advection separation, merger velocity times time since pericenter). D2.3 also surfaced and resolved the arc's central internal-consistency check: the same closed parameter set that produces v_crit also reproduces ξ_KZ, via the two-timescale core/dressing structure that D2.2 had independently established.

### Consolidated statement

Across the three deliverables, the Bullet offset is established as a topological-defect phenomenon: a monopole-antimonopole pair on the substrate's *S²* organizational field, forced into existence by winding conservation, tracking the galaxies and offset from the gas, with numerical predictions matched to the observed system. The consolidated result of Phase-2 is this:

> **The Bullet Cluster's gravitational-baryonic offset is not merely explainable but predictable.** The mechanism derives a specific, structured relationship between merger velocity and lensing-gas offset from the substrate's own fundamental scales, rather than fitting a single system after the fact.

---

## 3. The Three Synthesis-Level Claims

These are the claims the ED program stands behind as the output of the Bullet_Arc. They are recorded here exactly as stated in the synthesis paper, and they are the claims to be cited, defended, and tested.

**Claim 1 — The Bullet offset arises from a monopole-antimonopole pair in an *S²* order parameter.** The substrate's organizational state at cluster scales is a channel-orientation field on *S²*; the topology π₂(*S²*) = ℤ guarantees that a fast merger's quench produces point-monopole defects; the two offset lensing peaks are the two members of a single monopole-antimonopole pair. *(Grounded in D2.1.)*

**Claim 2 — The pair's dynamics reproduce the observed phenomenology.** Charge conservation forces the defects to form in opposite-charge pairs (two peaks). Each defect advects with its subcluster's collisionless galaxies, not the ram-stripped gas, placing the lensing peaks with the galaxies and offset from the gas. The pair cannot annihilate within cosmic history, and its observable signature persists for roughly the relaxation time before fading. *(Grounded in D2.2.)*

**Claim 3 — The numerical predictions match the Bullet and define falsifiable tests.** Closure from substrate primitives gives v_crit ~ 150 km/s, ξ_KZ ~ 860 kpc, and a three-regime offset-velocity law that reproduces both the Bullet's peak separation and its gas-lag offset. The law's distinctive shape — sharp knee, linear growth, saturation — defines tests that distinguish the mechanism from both ΛCDM and MOND-EFE. *(Grounded in D2.3.)*

Together these three claims constitute the arc's case: the Bullet offset is a topological-defect phenomenon, its dynamics reproduce the observed structure, and its quantitative predictions are testable and falsifiable.

---

## 4. The Two Open Items

Phase-2's closure rests on two substrate-physics ingredients that were used with physically-motivated estimates but not derived from first principles. They are recorded here explicitly as the program's known exposure.

**Open Item 1 — The super-linear substrate shock response.** The numerical values of τ_relax and v_crit depend on the substrate's organizational density rising at the merger interface by considerably more than the gas compression alone (a factor of about four). The arc assumes a super-linear substrate response, giving τ_relax ~ 10⁹ years and v_crit ~ 150 km/s. If the response is merely linear, τ_relax ~ 10¹⁰ years and v_crit ~ 15 km/s. This single question controls the *precise values* of the relaxation time and the critical velocity — i.e., exactly where the knee in the offset-velocity relation sits.

**Open Item 2 — The two-timescale core/dressing structure.** The arc uses a slow clock (the relaxation time, setting v_crit and the observable lifetime) and a fast clock (the core response time, setting ξ_KZ). The two differ because the defect is stabilized by the cluster's own structure rather than being a self-contained soliton — consistent with the core-versus-dressing distinction of D2.2, but the detailed stabilization mechanism is not fully derived. This question controls why the freeze-out scale and the critical velocity are governed by different clocks, and hence the internal consistency between ξ_KZ and v_crit.

**Status of the open items.** Both affect *precision, not qualitative structure.* Whichever way they resolve, the offset-velocity relation retains its three-regime shape — threshold, linear rise, ceiling — and the sharp knee that distinguishes the mechanism from its rivals persists. The open items shift only where the knee sits (somewhere in the range 15–1500 km/s) and how high the ceiling stands. Furthermore, the longer-τ_relax case actually improves the predicted-versus-observed agreement on the active-defect population, so the arc is robust to the outcome.

**Designation: Phase-4 theoretical target.** Resolving these two items — deriving the substrate shock response and the defect stabilization mechanism from substrate primitives — is designated a Phase-4 theoretical workstream. It is not a prerequisite for Phase-3 observational work, which tests the qualitative structure (the existence and character of the knee) independently of the precise parameter values.

---

## 5. Phase-3 Observational Program

**Phase-3 goal.** Measure the offset-velocity relation across the population of merging galaxy clusters, and determine its shape. The shape distinguishes the three candidate mechanisms (ED topological defect, ΛCDM dark matter, MOND-EFE modified gravity); the Bullet alone does not.

**The three falsifiers, mapped to observation.**

- **F1 — The knee (threshold).** Plot lensing-gas offset against merger velocity across the catalog. ED predicts a flat stretch at low velocity (no offset), a bend, then a rise. ΛCDM predicts a scatter with no clean relation; MOND-EFE predicts a smooth curve with no bend. *Test: does the offset-velocity relation exhibit a knee at all?* Its presence favors the topological mechanism; its absence challenges the arc.

- **F2 — The sharpness of the knee (transition).** If a knee exists, its character is decisive. ED predicts a *sharp*, step-like turn-on (defect formation is all-or-nothing). MOND-EFE, if it produced any bend, would produce a *gradual* one. *Test: is the turn-on sharp or smooth?* This is the cleanest single discriminator between the topological mechanism and modified gravity, and it most directly tests the topological character of the mechanism. Requires sampling mergers at velocities near the inferred threshold.

- **F3 — The saturation scale and multi-peak regime.** ED predicts the offset levels off at the freeze-out scale (~860 kpc) for the fastest mergers, and that the very fastest collisions may trap more than one defect pair, showing more than two offset peaks. ΛCDM and MOND-EFE predict no ceiling and no multiplicity. *Test: does the offset saturate at high velocity, and do the fastest mergers show multiple peaks?* Requires sampling the rarest, fastest mergers — a regime future wide-area surveys will populate.

**Required data products (per cluster).** For each merging cluster entered into the catalog:

- **v_rel** — the merger relative velocity (from X-ray shock analysis, where available)
- **Δr_offset** — the lensing-gas offset and/or the lensing-peak-to-lensing-peak separation (from weak-lensing reconstruction plus X-ray gas mapping)
- **t_post** — the time since pericenter (from merger-stage modeling)
- **mass ratio** — the subcluster mass ratio (affects the merger geometry and the defect-formation efficiency)
- **projection corrections** — the merger axis orientation relative to the line of sight (the measured offset is a projection of the true 3D separation)

**Candidate catalog (initial).** The Bullet Cluster (1E 0657-56), MACS J0025.4-1222, Abell 520 ("Train Wreck"), El Gordo (ACT-CL J0102-4915), and additional merging systems as the sample grows. Future surveys (Euclid, Roman, LSST) will substantially expand the high-velocity and well-characterized sample.

**The governing principle.** The Bullet alone cannot decide among the three mechanisms — all reproduce it. The distinguishing information lives in the *pattern across the catalog*: the shape of the offset-velocity relation, traced by many systems at many velocities. Phase-3 is not "examine the Bullet more closely"; it is "examine the population and read its shape."

---

## 6. Integration with the Broader ED Dark-Matter Account

The Bullet mechanism is the third of three independent, mutually reinforcing ED accounts of phenomena attributed to dark matter. The three arise from the same substrate physics expressed under different conditions, and they should be tracked, cited, and eventually published as a unified account.

- **The universal acceleration scale a₀** (`Paper_029`, Cos-05). Ordinary galaxy rotation curves bend at a₀ = cH₀/(2π), the cosmological horizon expressed as an acceleration. This is the substrate's *steady-state* response — a settled galaxy in the substrate's outer-scale field, with the "missing gravity" appearing wherever the local acceleration drops below a₀. Explains ordinary rotation curves without a halo.

- **The DF2/DF4 environmental suppression** (`Paper_ED_DF2_DF4_GroupSuppression`). Two galaxies lacking dark-matter-like behavior, both deep inside a massive group where the group's gravity overpowers the substrate's gentle outer-scale contribution. This is the substrate's *environmental* response — the same a₀ physics, locally drowned out by a strong external field.

- **The Bullet dynamical topological defect** (this arc). A violent merger drives the substrate through a quench, trapping a topological defect whose gravity is offset from the gas. This is the substrate's response to *rapid change* — the regime the steady-state and environmental pieces do not reach.

**Three regimes, one substrate.** A settled galaxy shows the steady-state a₀ enhancement; a galaxy in a dense environment shows that enhancement suppressed; a cluster caught in a fast merger shows a frozen-in dynamical defect. The galaxy-rotation evidence, the dark-matter-free galaxies, and the Bullet Cluster — three headline pieces of "dark matter evidence" — are three faces of the same substrate physics, read under steady, suppressed, and dynamical conditions. None requires a dark-matter particle. They require the substrate to have an outer scale (a₀), to be locally overpowerable (DF2/DF4), and to trap defects when rushed (the Bullet) — properties of one substrate, not three separate hypotheses.

**Program-level implication.** A combined paper integrating the three (a₀ + DF2/DF4 + Bullet) into a single ED account of the dark-matter evidence is a strong candidate for standalone publication, with its own Zenodo DOI. It would present the unified claim — one substrate, three regimes, no particle — that no single arc states in full. This is recorded as a downstream deliverable.

---

## 7. Phase-2 Closure Statement

**Phase-2 of the Bullet_Arc is formally complete.** All four documents are delivered:

- D2.1 — Vacuum Manifold (topology) ✓
- D2.2 — Winding Number (dynamics) ✓
- D2.3 — Relaxation Time (numerical closure) ✓
- Synthesis — Topological Defect (integration) ✓

**What is now ready:**

- **The synthesis paper** is complete and ready for rendering to PDF, for assignment of a Zenodo DOI, and for inclusion in the ED-generative repository.
- **The three synthesis-level claims** are recorded (Section 3) and are the program's statement of record on the Bullet Cluster.
- **The two open items** are documented (Section 4) and designated a Phase-4 theoretical target.
- **The Phase-3 observational program** is defined (Section 5), with falsifiers, data products, and an initial candidate catalog.

**Next active workstream: Phase-3 catalog assembly.** The theoretical phase of the Bullet_Arc is closed. The next active work is observational: assembling the merging-cluster catalog, gathering the required data products for each system, and plotting the offset-velocity relation to test for the knee. This is a data-gathering and analysis program, distinct in character from the Phase-2 theoretical work, and it is the workstream that would confirm or refute the arc's central prediction.

---

## 8. Recommended Next Actions

In order of priority:

**Immediate:**

1. **Render the synthesis paper to PDF** and assign a Zenodo DOI. The synthesis paper is the public-facing artifact and should be made citable. (Same pipeline as the PhilPapers paper: markdown → pandoc → PDF.)

2. **Add the four Bullet_Arc papers to the ED-generative repository** under an appropriate cluster (cosmology or a new `bullet-arc` subfolder), and update the repository README to note the arc and its completed Phase-2 status.

3. **Cross-reference the DF2/DF4 paper.** The DF2/DF4 paper (already in the cosmology cluster) and the Bullet synthesis are the two halves of the environmental/dynamical dark-matter story. Ensure each references the other.

**Near-term:**

4. **Draft the combined ED dark-matter paper** (a₀ + DF2/DF4 + Bullet). This is the unified-account document flagged in Section 6 — the strongest standalone-publication and Zenodo candidate, presenting the one-substrate-three-regimes claim in full.

5. **Begin Phase-3 catalog assembly.** Compile the initial candidate catalog (Bullet, MACS J0025, Abell 520, El Gordo) with the five required data products per system. Identify which systems already have published v_rel, Δr_offset, and t_post measurements, and which require new analysis.

6. **Produce a Bullet_Arc outreach one-pager** (NotebookLM format) drawn from the synthesis paper's Section 7.4 ("the arc in one page") — the accessible, shareable summary for cold contact and social distribution. Note: defer until the synthesis-paper Zenodo DOI exists, so the one-pager can point to a citable source.

**Phase-4 (theoretical, deferred):**

7. **Derive the super-linear shock response** from substrate primitives (Open Item 1).

8. **Derive the defect external-stabilization mechanism** from substrate primitives (Open Item 2).

These two would convert the arc's order-of-magnitude predictions into precise ones, but are not prerequisites for Phase-3.

---

*End of Memo-02. Phase-2 is complete. Phase-3 is the active observational workstream.*
