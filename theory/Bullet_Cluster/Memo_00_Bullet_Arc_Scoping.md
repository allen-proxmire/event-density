# Memo-00 — Bullet_Arc Scoping
## Explaining the Bullet Cluster Gravitational–Baryonic Offset via Event Density

**Arc:** Bullet_Arc
**Memo:** 00 (scoping)
**Status:** Phase-1 substantially complete; Phase-2 entry
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related memos:** `Memo_Bullet_TopologicalDefect_Overshoot.md` (Phase-1 qualitative articulation)

---

## Executive Summary

The Bullet Cluster (1E 0657-56) is the most-cited single piece of "direct evidence" for non-baryonic dark matter: a ~110 kpc offset between the weak-lensing convergence peak and the X-ray gas peak following a high-velocity merger (Clowe et al. 2006). This arc develops the working hypothesis that the offset is **not** evidence for collisionless particles, but evidence for a substrate-level **organizational defect** formed when a fast cluster merger overdrives saturation faster than the substrate can relax.

The mechanism, in one sentence: the merger creates a winding in the substrate's channel-organization that cannot smoothly unwind on merger-crossing timescales, and the gravitational signal tracks that frozen winding rather than the mechanically-displaced gas.

This arc is the **cluster-scale dynamical companion** to the DF2/DF4 arc. DF2/DF4 articulated the steady-state suppression rule: in equilibrated dense environments, the cosmic horizon's enhancement is locally overpowered. Bullet_Arc adds the non-equilibrium case: in fast mergers, the substrate's organizational state freezes into a structure that doesn't track baryons.

The arc is exploratory. The qualitative reading is structurally consistent with established ED primitives. The formal *topological* claim — that the frozen structure is genuinely characterized by a homotopy class — requires three deliverables to close before "topological" earns its place as physics rather than metaphor.

---

## Arc Scope

### In scope
- The Bullet Cluster (1E 0657-56) as the primary case study
- Substrate-level mechanism for the lensing-vs-gas offset
- Topological-defect formal structure (if it earns the designation in Phase-2)
- Predictions that distinguish ED from MOND-EFE, from ΛCDM, and from holographic / emergent-spacetime alternatives
- Connection to other observed merging clusters (MACS J0025.4-1222, Abell 520, El Gordo) as test cases for the velocity-scaling prediction
- Coordination with the DF2/DF4 arc as the steady-state companion to this dynamical case

### Out of scope
- Direct rederivation of the cluster's total mass budget
- Quantitative N-body simulation of the merger itself
- Galaxy-formation dynamics within the merging clusters
- Dark-matter alternatives that don't share ED's substrate ontology
- The specifics of weak-lensing reconstruction methodology

---

## Structural Decomposition

The arc decomposes into four structural layers, each with a distinct deliverable signature.

### Layer 1 — Substrate organizational equilibrium
What is the substrate doing at cluster scales in equilibrium? Channels are bundled in some structured way; commitment-density gradients are smooth across the cluster; the cosmological-floor contribution (*a₀*) is locally absorbed by the cluster's own gravitational architecture (the DF2/DF4 saturation case). This is the pre-merger state of each subcluster.

### Layer 2 — The quench
A fast cluster merger drives the substrate's organizational state through a non-equilibrium transition on timescales much shorter than its own relaxation. Two pre-merger organizational configurations encounter each other and cannot smoothly merge. The mismatch is structural, not merely energetic.

### Layer 3 — The defect
A frozen-in mismatch in channel-orientation forms at the boundary between the saturated collision core and the surrounding shell. The mismatch carries a charge (potentially topological, in the homotopy-class sense — to be determined in Phase-2). The structure persists for some relaxation time τ.

### Layer 4 — The gravitational signal
Weak lensing reads the substrate's commitment-density structure, not the baryon position directly. In the post-merger state, that structure is anchored to the defect (co-located with the pre-merger gravitational configuration, which is approximately where the collisionless galaxies now sit). The observed offset is the spatial separation between the topological core and the ram-pressure-stripped gas.

---

## Primitive Load-Bearing Table (P / D / A / I)

Where:

- **P** = Primitive (structural commitment of ED itself)
- **D** = Derived (follows from primitives without slack)
- **A** = Assumed (boundary condition or modeling choice in this arc)
- **I** = Inherited (numerical value from observation or substrate parameter)

| ID | Primitive / Concept | Role in Bullet_Arc | Class |
|---|---|---|---|
| **P01** | Discrete events | Substrate's atomic units | **P** |
| **P02** | Channels (constraint structure between events) | The order-parameter carrier | **P** (load-bearing for topology) |
| **P03** | Participation (coordinated channel flows) | What gas / galaxies "ride" on | **P** |
| **P04** | Commitment (irreversible registration) | Why post-merger structure persists | **P** (load-bearing) |
| **P05** | Finite reach | Why substrate can't equilibrate at infinite speed | **P** (load-bearing for quench logic) |
| **P06** | Finite memory | Sets relaxation timescale τ | **P** (load-bearing for Layer 3) |
| **P07** | Substrate grain (Planck scale) | Bounds the smallest defect scale | **P** |
| **P08** | Outer-scale (cosmological horizon; *a₀*) | The equilibrium background; entered via Cos-05 / *a₀* derivation | **P** |
| **P09** | Update rule (irreversible substrate progression) | Why the merger is a one-way quench | **P** (load-bearing) |
| **P10** | Channel-orientation field at outer scale | The candidate organizational order parameter | **D** (from V5 kernel structure) |
| **P11** | Saturation state | Cluster-core equilibrium; from DF2/DF4 arc | **D** |
| **P12** | Saturation overshoot | Working hypothesis: quench past equilibrium | **A** (this arc's central conjecture) |
| **P13** | Organizational topological charge | The conserved quantity, if it exists | **A** (Phase-2 will attempt to derive) |

**Note:** P01–P09 are primitives in the standard ED sense (Paper_087 register). P10–P13 are derived / assumed quantities specific to this arc. The classification should be cross-checked against the canonical primitive register before publication.

---

## Kernel Load-Bearing Table

| Kernel | Source | Role in Bullet_Arc |
|---|---|---|
| **V1 Vacuum Kernel** | Paper_013_V1_VacuumKernel | Load-bearing for the equilibrium organizational state. The relaxation argument is constructed against V1's notion of vacuum coherence — what kind of coherence the substrate carries in the unperturbed cluster vacuum. |
| **V5 Kernel** | Paper_090_V5Kernel | Load-bearing for the quench dynamics. The saturation regime and its overdrive are V5 concepts. The outer-scale (horizon-coupling) machinery that grounds *a₀* in cluster contexts is V5. |

The arc is **V5-native**. If Phase-2 succeeds in identifying a homotopy structure, it should be expressible in V1 vacuum-coherence language as well — establishing kernel-portability of the result. If it can only be expressed in V5, that asymmetry is itself informative about the relative completeness of the two kernels.

---

## FORM-FORCED / VALUE-INHERITED / OPEN Register

| Claim | Status | Notes |
|---|---|---|
| Substrate exists; has finite reach, memory, grain | **FORM-FORCED** | Primitives P01–P09 |
| Substrate has organizational state at cluster scales | **FORM-FORCED** | Implied by V5 outer-scale machinery |
| Fast mergers drive a quench of that state | **FORM-FORCED** | Finite-reach + fast-perturbation; both already in ED |
| The post-quench state contains a frozen defect | **OPEN** | Working hypothesis; structurally consistent but not formally derived |
| The defect is *topological* in the strict (homotopy) sense | **OPEN** | Requires Phase-2 D2.1: vacuum-manifold identification + nontrivial π_n |
| The defect persists on ≳ 10⁸ year timescales | **OPEN** | Requires Phase-2 D2.3: substrate organizational relaxation time τ |
| The defect is anchored to the pre-merger channel orientation | **OPEN** | Follows from quench logic if the prior OPEN claims close |
| The gravitational signal tracks the defect, not the gas | **FORM-FORCED** *if* defect exists | Channels register substrate structure; gravity reads channels |
| The ~110 kpc Bullet offset matches the predicted scale | **VALUE-INHERITED** | Numerical scale depends on merger velocity (measured) and τ (open) |
| The factor-of-two MOND-cluster residual is the defect contribution | **OPEN** | Numerical comparison reserved for Phase-3 |
| Offset magnitude scales with merger velocity | **FORM-FORCED** *if* Kibble framing applies | Defect density goes with quench rate (standard Kibble result) |
| Offset *direction* is set by pre-merger channel orientation | **FORM-FORCED** *if* defect anchors pre-merger geometry | Standard for topological defects in any field theory |
| Discrete (not smooth) transition at a critical merger speed | **FORM-FORCED** *if* topology is nontrivial | Below the threshold, substrate has time to relax; no defect forms |
| Multi-component mergers show complex defect topology | **FORM-FORCED** *if* the above closes | Multiple winding contributions |

---

## Falsification Register

The arc is falsifiable in three structurally distinct ways and one phenomenological way.

### F1 — No velocity scaling
If careful weak-lensing observations across merging clusters of varying merger velocities show no systematic dependence of offset magnitude on merger speed — specifically if low-velocity mergers (~500–1000 km/s) produce offsets comparable in scale to the Bullet's ~3000 km/s case — then either the defect is not Kibble-formed or the substrate's relaxation time is short enough that all sampled mergers are subcritical. Either falsifies the central claim of the arc.

### F2 — No discrete transition
If the offset-vs-velocity relation is smooth across the predicted threshold (a critical merger speed below which the substrate has time to relax and no defect forms), the topological-defect framing is wrong. A smooth transition is consistent with MOND-EFE-class field-interpolation accommodations but not with topological-defect dynamics. The Kibble mechanism requires a knee.

### F3 — No vacuum manifold structure
Phase-2 Deliverable D2.1 attempts to construct the substrate's organizational order parameter and identify a vacuum manifold *M* with nontrivial π_n(*M*). If no such construction is possible — if the organizational state turns out to be path-connected and simply-connected under every formulation tried — then "topological" is metaphor, not physics. The arc reduces to a weaker "slow-relaxation defect" framing, which retains the qualitative reading without the topological guarantee.

### F4 — Numerical mismatch (weak falsification)
If the quantitative magnitude of the offset systematically fails to match the observed ~factor-of-two MOND-cluster residual across multiple merging-cluster cases, the arc requires modification even if F1–F3 individually survive. This is a weaker falsification because the numerical comparison involves multiple inherited values (τ, pre-merger geometry, merger orbit), and a mismatch could indicate an inheritance error rather than a structural one.

---

## Dependency Graph

```
                       ┌─────────────────────┐
                       │   V1 Vacuum Kernel  │
                       │   (Paper_013)       │
                       └──────────┬──────────┘
                                  │
                                  ▼
                       ┌─────────────────────┐
                       │   V5 Kernel         │
                       │   (Paper_090)       │
                       └──────────┬──────────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        ▼                         ▼                         ▼
┌────────────────┐       ┌────────────────┐       ┌────────────────┐
│ 13 Primitives  │       │  Cos-05        │       │ DF2/DF4 Arc    │
│ (Paper_087)    │       │  Λ + a₀        │       │ Steady-state   │
│ P01–P13        │       │ (Paper_029,    │       │ Saturation     │
│                │       │  Paper_ED_     │       │                │
│                │       │  Cos_05)       │       │                │
└────────┬───────┘       └────────┬───────┘       └────────┬───────┘
         │                        │                        │
         └────────────────────────┼────────────────────────┘
                                  │
                                  ▼
                       ┌─────────────────────┐
                       │    BULLET_ARC       │
                       │    (this memo)      │
                       └──────────┬──────────┘
                                  │
                                  ▼
                       ┌─────────────────────┐
                       │ Dark-Matter         │
                       │ Synthesis Arc       │
                       │ (future)            │
                       └─────────────────────┘
```

### Upstream dependencies (feed into Bullet_Arc)
- **V1 Vacuum Kernel** (Paper_013) — original substrate field formulation
- **V5 Kernel** (Paper_090) — current production formulation; supplies outer-scale and saturation structure
- **13 Primitives** (Paper_087) — primitive register P01–P13
- **Cos-05 / *a₀*** (Paper_029, Paper_ED_Cos_05) — cosmological outer-scale baseline (*a₀ = cH₀/(2π)*)
- **DF2/DF4 Arc** — steady-state companion case; supplies the saturation rule that Bullet_Arc overdrives

### Downstream dependencies (Bullet_Arc feeds)
- **Dark-Matter Synthesis Arc** (future) — combining *a₀* (universal), DF2/DF4 (steady-state suppression), and Bullet_Arc (dynamical defect) into one unified ED account of dark-matter evidence
- **Potential: Early-Universe Defect Arc** — if substrate organizational defects also form during cosmological phase transitions (a natural extension of the Kibble framing)

---

## Phase Map

### Phase-1 — Qualitative Articulation [SUBSTANTIALLY COMPLETE]

**Captured in:** `Memo_Bullet_TopologicalDefect_Overshoot.md`

**Achieved:**
- Substrate organizational state named as the order parameter
- Saturation-overshoot mechanism articulated
- Kibble-mechanism analogy drawn
- Gravitational-signal-anchor argument established (channels carry the structure, not displaced gas)
- Four qualitative predictions extracted (P1–P4 in the memo)
- Three formal deliverables identified for Phase-2
- Honest "solid vs speculative" register produced

**Remaining for Phase-1 closure:**
- This Memo-00 (scoping)
- Cross-reference primitive labels against canonical Paper_087 register

### Phase-2 — Formal Structure

**Goal:** Determine whether "topological" is physics or metaphor.

**Three deliverables, ordered by depth:**

#### D2.1 — Vacuum manifold of the substrate organizational order parameter
- Specify the order parameter at cluster scales (scalar / vector / higher-rank field of channel orientations)
- Identify its vacuum manifold *M*
- Compute π_n(*M*) for relevant *n*
- If π₁(*M*) or π₂(*M*) is nontrivial → defects of that homotopy type can form
- If all π_n(*M*) are trivial → only metastable structures, not topological defects

#### D2.2 — Conserved topological charge
- If D2.1 succeeds: define the integer winding number a Bullet-class defect carries
- Show conservation by substrate dynamics on timescales ≫ merger crossing time
- Identify possible decay channels and their timescales

#### D2.3 — Substrate organizational relaxation timescale τ
- Derive (or phenomenologically estimate from multi-cluster fit) the relaxation time τ
- Compare to merger crossing times (~10⁸ years for the Bullet)
- Verify the freeze-in condition (τ ≫ t_merger) for the Bullet and other observed merging clusters

**Phase-2 exit criterion:**
- If D2.1, D2.2, and D2.3 all close → topological framing is physics; Phase-3 proceeds with topological framing
- If one or more fail → arc transitions to "slow-relaxation defect" framing; Phase-3 still proceeds but with weaker structural claims

### Phase-3 — Observational Engagement

**Goal:** Test the predictions against existing and forthcoming data.

**Test programmes:**

- **T3.1** — Catalogue well-characterized merging galaxy clusters with weak-lensing-vs-gas offset measurements (Bullet, MACS J0025, Abell 520, El Gordo, others). Tabulate offset magnitude vs measured merger velocity. Test P1.
- **T3.2** — Identify low-velocity (subcritical) merger candidates. Test whether they show suppressed or absent offsets per P3.
- **T3.3** — Identify multi-component mergers (three-way collisions; sequential mergers). Look for complex offset topologies per P4.
- **T3.4** — Pre-merger orientation: test whether offset *direction* tracks the pre-merger axis of symmetry per P2.

**Phase-3 exit criterion:**
- Predicted patterns observationally supported → publication-ready synthesis (Bullet + DF2/DF4 + *a₀*)
- Predicted patterns observationally absent → memo revision; possible arc retraction

---

## Deliverables List

### Phase-1 (in-progress or complete)
- `Memo_00_Bullet_Arc_Scoping.md` (this document)
- `Memo_Bullet_TopologicalDefect_Overshoot.md` — qualitative articulation [DONE]
- Optional: Bullet_Arc NotebookLM one-pager for public outreach [DEFERRED]

### Phase-2 (to produce)
- `Paper_ED_Bullet_VacuumManifold.md` — order parameter, manifold construction, homotopy classification
- `Paper_ED_Bullet_WindingNumber.md` — topological charge definition, conservation argument
- `Paper_ED_Bullet_RelaxationTime.md` — substrate organizational relaxation derivation or phenomenological fit
- `Paper_ED_Bullet_TopologicalDefect.md` (synthesis) — combines the above three with Phase-1 qualitative reading into a publishable paper

### Phase-3 (to produce)
- Test catalogue of merging clusters with offset-vs-velocity data
- Updated synthesis paper with observational comparisons
- `Paper_ED_DarkMatter_Synthesis.md` — combined Bullet + DF2/DF4 + *a₀* + others (likely the Zenodo standalone)

### Cross-arc deliverables
- Update to `Paper_095_FormForced_ValueInherited.pdf` with Bullet_Arc entries
- Update to `Paper_087_13Primitives.pdf` if P10–P13 require canonical addition

---

## What This Arc Is NOT Claiming

To prevent the arc from being read as more than it is:

1. **Not claiming the Bullet Cluster's total mass budget is wrong.** The cluster is ~10¹⁵ M☉ of real gravitating commitment density. The arc disputes only the *interpretation* of the lensing-vs-gas offset, not the overall mass scale.

2. **Not claiming standard cluster physics is wrong.** Ram-pressure stripping, gas dynamics, galaxy distributions — all the standard analyses remain valid. The arc adds a substrate-level interpretation of why the lensing peak tracks the galaxies and not the gas.

3. **Not yet claiming the structure is topological in the strict homotopy sense.** Phase-2 must close before that word becomes physics. Phase-1 uses it as a structural metaphor.

4. **Not claiming all dark-matter evidence reduces to topological defects.** This arc addresses the cluster-merger offset specifically. Other evidence (galactic rotation curves, CMB acoustic peaks, structure formation, BBN) is handled by other ED arcs (Cos-02 through Cos-06, DF2/DF4) and has its own substrate-level account.

5. **Not claiming the Bullet specifically rules out collisionless dark matter.** It claims the offset can be accounted for without invoking such a particle. The arc is *consistent* with there being no dark-matter particle; it does not formally *exclude* one.

6. **Not in competition with MOND-EFE accounts.** MOND-EFE provides an EFE-class accommodation through field non-linearity. ED's reading is mechanistically distinct (defect formation rather than field interpolation) and predicts a sharper transition. Phase-3 is designed to distinguish them empirically.

7. **Not making claims about cosmological-scale topological defects (yet).** Whether substrate organizational defects also form during cosmological phase transitions is a separate (downstream) arc. Bullet_Arc constrains itself to cluster-merger-scale defects.

---

## Recommended Next Steps

In order of immediate execution:

### Step 1 — File and verify
File this Memo-00 in the Bullet_Arc folder alongside the Phase-1 memo. Cross-check the P01–P09 primitive labels against the canonical Paper_087 register. Adjust P10–P13 classification if needed.

### Step 2 — Begin Phase-2 with D2.1 (vacuum manifold)
This is the deepest of the three deliverables and the gate that determines whether the arc earns "topological" as a formal designation. Recommended approach: a focused workflow that surveys candidate order parameters in field theory with cluster-scale physical interpretations (scalar field of channel-orientation amplitude, vector field of channel direction, higher-rank tensors), then attempts to construct the substrate's analogue with explicit vacuum manifold and homotopy computation.

### Step 3 — Begin Phase-3 catalogue work in parallel
Tabulating the observational catalogue for T3.1–T3.4 can proceed independently of Phase-2's formal work. It may surface empirical constraints (e.g., observed offset-velocity correlations) that inform the formal construction.

### Step 4 — Coordinate with the DF2/DF4 arc
The two arcs are tightly coupled — same primitive set, same outer-scale grounding, different regimes. Ensure the eventual synthesis paper carries both cleanly. The DF2/DF4 paper articulates the steady-state saturation rule; Bullet_Arc articulates the dynamical overdrive. Together they cover both regimes of substrate response to environmental gravitational density.

### Step 5 — Update the corpus README
Note Bullet_Arc as an active arc with its own subfolder. Indicate Phase-1 complete, Phase-2 entry.

### Step 6 — Defer outreach until Phase-2 closes
The NotebookLM one-pager and any public-facing communication of the topological framing should wait for Phase-2 D2.1's outcome. If "topological" earns its place, the outreach copy can use it confidently. If it falls back to "slow-relaxation defect," the framing changes and the public-facing language must change with it.

---

*End of Memo-00.*
