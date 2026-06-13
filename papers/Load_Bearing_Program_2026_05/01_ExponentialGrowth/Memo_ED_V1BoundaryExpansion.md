# Memo_ED_V1BoundaryExpansion — Construction Memo (Path-β Attempt)

**Series:** Wave-3 Construction Memo (Cosmology Arc; inflation sub-thread; Path-β from Memo_ED_ExponentialGrowth_Scoping)
**Status:** Substrate-graph attempt to derive super-linear-in-volume boundary expansion of the unbalanced-saddle region from V1 finite-width retarded propagation in default-flat substrate geometry. Closure would supply exponential scale-growth $\dot a \propto a$ for Paper_ED_Cos_01 row 13. **Not a derivation. Not a claimed closure. No new primitives.** Outcome: **negative — V1 finite-width retarded propagation in default-flat geometry produces linear boundary advance regardless of region size.** None of five candidate substrate-graph feedback mechanisms supplies super-linear scaling.
**Date:** 2026-05-16
**Anchors:** Paper_ED_Cos_01 (Inflation, row 13 OPEN); Paper_089 (V1 retarded kernel, T18, finite-width support); Paper_073 (DCGT); Paper_012 (P-RB-1 substrate-c bound); Memo_ED_ExponentialGrowth_Scoping (Path-β candidate identification).

---

## §1 Geometric setup

The unbalanced-saddle Hessian-signature region (per Paper_ED_Cos_01 §3.3) expands via V1 retarded propagation (Paper_089) in default-flat substrate geometry (post-SCBU homogeneity per Paper_ED_CCC §3.6 + SC-4.x scale-collapse). Identifying the substrate-graph region scale with the continuum-side scale factor $a(t)$ via DCGT (Paper_073), the question for Path-β is whether $\dot a \propto a$ can be derived from V1's substrate-graph propagation structure alone.

**The continuum-side target:** $a(t) \propto e^{Ht}$ requires $\dot V / V \propto $ constant in 3D, where $V \propto a^3$. Equivalently: boundary advance rate must scale with the scale factor $V^{1/3} = a$, not with substrate-c (which is constant).

**The substrate-graph question:** is there any substrate-graph feedback mechanism in V1's finite-width retarded structure (or in collective V1-active substrate content) where boundary expansion rate scales with interior volume rather than with boundary surface area alone?

---

## §2 Linear-growth baseline

The default-flat substrate-graph reading:

- V1 retarded support has fixed finite-width $\ell_{V_1}$ per Paper_089 (set by substrate parameters, not region-size-dependent).
- Boundary advance happens via V1 propagating unbalanced-saddle content from boundary loci into adjacent balanced loci.
- Per Paper_012 P-RB-1 + Paper_089, V1 propagation is bounded by substrate-c.
- Boundary advance rate at any locus: substrate-c (constant).

In 3D flat geometry:
- Surface area $\propto a^2$
- Volume $\propto a^3$
- Boundary advance: $\dot a = c$ (constant) → $a(t) = a_0 + ct$ → **linear**
- Equivalently: $\dot V = c \cdot S \propto c \cdot a^2 \propto V^{2/3}$ → power-law $V \propto t^3$, $a \propto t$ → **linear**

This is the baseline. For exponential growth, the substrate-graph must supply a mechanism where boundary advance rate scales with $a$ (or, equivalently, where $\dot V \propto V$ rather than $V^{2/3}$).

---

## §3 Candidate substrate-graph feedback mechanisms

Five candidates examined.

### Candidate 1: Long-range V1 coupling (interior contributes to boundary)

**Proposal:** if V1 finite-width $\ell_{V_1}$ supports interior loci's V1 reach extending to the boundary, each such interior locus contributes to boundary advance. Total boundary contribution: (number of interior loci within $\ell_{V_1}$ of boundary) × (V1 substrate-c contribution per locus).

**Calculation:** the interior shell within distance $\ell_{V_1}$ of the boundary has volume $\propto S \cdot \ell_{V_1} \propto a^2 \cdot \ell_{V_1}$. Boundary surface area $\propto a^2$. Ratio (contributing interior volume / boundary surface) = $\ell_{V_1}$ = constant. Boundary advance rate per unit boundary area: constant.

**Result:** no super-linear scaling. Boundary still advances at substrate-c; linear growth preserved.

**Status: negative.** V1's finite-width support constrains the bulk contribution to a fixed-thickness surface shell. Interior loci beyond $\ell_{V_1}$ from the boundary do not contribute via V1 to boundary advance.

### Candidate 2: Bulk-driven volumetric source

**Proposal:** treat each substrate locus in the unbalanced-saddle region as a V1 "source" contributing to the propagating field at the boundary. Total bulk-to-boundary flux scales with bulk volume; if boundary advance rate scales with bulk-to-boundary flux divided by boundary area, advance rate $\propto V / S \propto V^{1/3} = a$ → exponential.

**Examination:** in standard PDE wave-source physics, bulk sources produce far-field amplitudes that grow with source volume. The mechanism requires source-amplitude to *not* decay with distance (or to decay slower than the geometric spread).

In V1's substrate-graph structure (Paper_089), V1 is a retarded kernel with finite-width support: V1 transports content from source to target only within $\ell_{V_1}$ substrate-distance. Beyond $\ell_{V_1}$, V1 contribution is zero. **Bulk interior loci beyond $\ell_{V_1}$ from the boundary do not contribute to boundary advance via V1.** Only the surface shell of thickness $\ell_{V_1}$ contributes — which scales as $a^2$, same as boundary area, giving constant per-unit-area advance rate.

**Result:** Candidate 2 collapses to Candidate 1 under V1's finite-width restriction. No super-linear scaling.

**Status: negative.** Would require V1 to have non-finite-width (long-range) retarded support, contradicting Paper_089.

### Candidate 3: V1 cascade / amplification (downstream re-emission)

**Proposal:** each substrate locus that V1 propagates content to becomes itself a new V1 source. The boundary advance is then a cascading wave where each newly-converted locus re-radiates outward at substrate-c. Total wavefront amplitude grows with the population of V1-active loci behind it.

**Examination:** in the saturation regime per Paper_ED_Cos_01 §3.4, all loci in the unbalanced region are V1-active. The boundary's advance via V1 retarded propagation IS the cascade — each new locus that the boundary reaches becomes V1-active, and its V1 then continues propagating outward.

However, the cascade rate is still bounded by substrate-c per Paper_012 P-RB-1. The "amplification" intuition would require the wavefront to advance faster than substrate-c, which is a structural bound. Cascading at substrate-c gives the same linear boundary advance.

**Result:** cascading happens at substrate-c regardless of cascade extent. No super-linear scaling.

**Status: negative.** Substrate-c bound forecloses cascade-based super-luminal advance.

### Candidate 4: Collective synchronous V1 (constructive interference at boundary)

**Proposal:** multiple V1-active interior loci with synchronized P09 phases produce constructive interference at the boundary, effectively raising the substrate-side V1 amplitude at the boundary above what any single locus contributes. If interference-amplitude scales with the population of synchronized loci, boundary advance rate could grow with bulk volume.

**Examination:** P09 phase content can in principle synchronize across loci. Constructive interference at the boundary would give larger V1 amplitude at the boundary. But:

- The *propagation speed* of the resulting V1 wavefront is still substrate-c (P-RB-1 bound).
- Amplitude affects what's transported, not how fast it transports.
- Even with infinitely large amplitude, the wavefront cannot exceed substrate-c.

**Result:** amplitude effects do not yield super-luminal propagation. No super-linear boundary advance.

**Status: negative.** Substrate-c is a propagation-speed bound, not an amplitude bound; amplitude effects do not produce super-linear scaling.

### Candidate 5: Effective dimensionality via V1 long-range connectivity

**Proposal:** if V1's substrate-graph structure supports a higher effective dimensionality (loci connected to many neighbors via V1, beyond the standard 3D nearest-neighbor pattern), boundary expansion could scale faster than $a^2$.

**Examination:** V1's finite-width support gives each locus a limited number of neighbors within $\ell_{V_1}$. In 3D flat geometry, the count of neighbors within radius $\ell_{V_1}$ is $\propto \ell_{V_1}^3$ — a constant. Effective dimensionality is 3, not higher.

For V1 to produce higher effective dimensionality, $\ell_{V_1}$ would need to scale with region size (substrate-state-dependent finite-width). This is Candidate P2 (state-dependent DCGT) from the scoping memo, not P1.

**Result:** V1's finite-width is fixed; effective dimensionality is 3. No super-linear scaling from connectivity alone.

**Status: negative.** Reduces to Candidate P2 (state-dependent V1 / DCGT extension), which is Path-α territory not Path-β.

---

## §4 Honest negative finding

**V1 finite-width retarded propagation in default-flat substrate geometry produces linear boundary advance regardless of region size.**

None of five candidate substrate-graph feedback mechanisms supplies super-linear-in-volume boundary expansion:

- Candidates 1 and 2 (long-range / bulk-driven) are blocked by V1's finite-width support restricting bulk contribution to a surface shell.
- Candidate 3 (cascade) is blocked by substrate-c being a structural propagation-speed bound.
- Candidate 4 (collective interference) cannot exceed substrate-c regardless of amplitude.
- Candidate 5 (effective dimensionality) requires V1 finite-width to be substrate-state-dependent, pushing to Path-α (state-dependent DCGT) outside Path-β scope.

**The substrate-graph default reading is confirmed: at-most-linear scale-growth from V1 finite-width retarded propagation in default-flat substrate geometry.** Path-β yields a clean negative result.

---

## §5 IDENTIFIED vs OPEN

### IDENTIFIED:

- **V1 finite-width retarded propagation produces at-most-linear boundary advance** in default-flat substrate geometry. Linear growth $a(t) \propto t$ is the substrate-graph default for V1-driven region expansion.
- **No super-linear-in-volume boundary expansion** arises from V1's substrate-graph structure alone. The five candidate feedback mechanisms all fail for structural reasons (finite-width, substrate-c bound, fixed neighbor connectivity).
- **The exponential-growth condition $\dot a \propto a$ does not close via V1's substrate-graph structure** without ontology extension. Closure routes via Path-α (state-dependent DCGT) or alternative substrate-graph mechanisms remain to be examined.

### OPEN (carried forward):

- **Path-α (state-dependent V1 / DCGT extension):** whether $\Gamma_{\mathrm{diff}}$ or $\ell_{V_1}$ admits state-dependence at substrate-graph level. Most-leverage potential closure.
- **Path-γ (DCGT non-Euclidean coarse-graining):** whether DCGT's substrate→continuum bridge produces exponential coarse-grained geometry in the saturation regime, even from substrate-graph linear propagation.
- **Quantitative substrate-side reading of GR-side Hubble parameter $H$** under at-most-linear substrate-graph propagation. Either $H$ corresponds to substrate-c-bounded linear rate (mismatch with standard cosmology phenomenology) or to a substrate-graph quantity not yet identified.

### Consequence for Paper_ED_Cos_01:

The current framing of row 13 OPEN is structurally sound: substrate-c-bounded propagation does NOT give exponential growth from V1 structure alone. Path-β confirms this negative reading. The remaining options are Path-α closure (substrate-research-frontier work on DCGT) or Path-γ acceptance (reframe Paper_ED_Cos_01 to make at-most-linear substrate-graph reading explicit, lean entirely on SCBU inheritance for horizon resolution).

---

## §6 Recommended next steps

The negative result on Path-β is informative and lowers the prior probability of any V1-structural closure for exponential growth. Three honest paths:

**Path-α (attempt DCGT state-dependent extension):** focused construction memo examining whether DCGT (Paper_073) admits state-dependent diffusion rates or whether substrate-graph saturation-regime DCGT produces non-Euclidean continuum coarse-graining. Higher-leverage but harder substrate-research work.

**Path-γ (accept and reframe):** update Paper_ED_Cos_01 to make the at-most-linear substrate-graph reading explicit. Reframe inflation in ED as "linear region-growth via V1 retarded propagation; horizon-resolution wholly via SCBU inheritance; GR-side Hubble parameter $H$ does not have direct substrate-graph correspondence in this framework." Verdict stays M2 with row 13 OPEN reframed as "fundamental substrate-graph limitation, not derivation gap."

**Path-δ (alternative substrate-graph mechanism search):** broader scoping memo examining whether any substrate-graph content beyond V1 + DCGT might supply exponential growth — e.g., V5 cross-chain coupling effects, saddle-Hessian eigenvalue dynamics from Paper_ED_SC_4_9, multi-aeon CCC contributions. Speculative but worth scoping if Path-α doesn't close.

**My recommended next step:** Path-α attempt via focused memo Memo_ED_DCGT_StateDependent. State-dependent DCGT is the highest-leverage candidate for exponential-growth closure and would have cross-arc impact regardless of outcome (DCGT is upstream of much of the corpus).

**Cross-arc note:** the negative result from Path-β has a parallel to the chirality cascade — *"V1 cannot supply chain-typing $\mathbb{Z}_2$"* maps structurally to *"V1 cannot supply super-linear boundary expansion."* Both indicate that V1's substrate-graph structure is structurally too symmetric / too direct to supply specialized features that standard physics treats as load-bearing. The substrate-ontology-discipline finding accumulates: **ED's substrate is structurally leaner than standard physics machinery; specialized features (chirality, exponential growth, etc.) require either ontology extension or paper-specific postulates.**

This is consistent with the corpus's substrate-ontology lineage (Wolfram, 't Hooft, causal-set) and not a defect — it is the honest substrate-research-frontier characterization of the ED ontology.

---

**End Memo_ED_V1BoundaryExpansion.**
