# Memo_ED_ChainClassIdentification_Scoping — Scoping Memo for the Chain-Class Identification Gap

**Series:** Wave-3 Scoping Memo (Cosmology + Dynamics Arcs; companion to the Q1/Q2 Joint-Closure Project; addresses the §6.3 scope-mismatch finding from Memo_ED_Q1Q2_JointClosure_Construct)
**Status:** Substrate-graph scoping of the residual qualitative-mechanism gap that the Q1A + Q2A construction-uniqueness closure does not address: **given a substrate-side $\Psi$ configuration, which continuum-side regime or source class does it correspond to?** This is the missing half of the audit-flagged Q1/Q2 gaps required for the M2 → M3 upgrade of Paper_ED_Cos_01 + Paper_ED_Dyn_02 + Paper_ED_Dyn_03. **Not a derivation. No new primitives proposed. Negative results acceptable.**
**Date:** 2026-05-16
**Anchors:** Memo_ED_Q1Q2_JointClosure_Construct §6.3 (parent finding); Memo_ED_Q1Q2_JointClosure_Scoping (parent project); Paper_ED_Cos_01 (M2; inflation saturation case); Paper_ED_Dyn_02 (M2; RDE/MDE/LDE cases); Paper_ED_Dyn_03 (M2; EM/GW source classes); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$ + saddle Hessian); Paper_087 (13 primitives — P02, P04, P09, P10, P11, P12, P13); Paper_073 (DCGT); Paper_089 (V1 + T18); Paper_090 (V5 cross-chain + finite-memory); Paper_012 (P-RB-1 substrate-c); Paper_093 (T18 kernel-arrow); Paper_015 / T17 (gauge bundles); Paper_098_5 / T1 (spin-statistics); Paper_109 (Lorentz reps).

---

## §1 Restated gap

### §1.1 The chain-class identification problem

The Q1A + Q2A construction-uniqueness closure (Memo_ED_Q1Q2_JointClosure_Construct) established:

- Given $\mathcal{L}_{\mathrm{sub}}$, the substrate-side Noether stress-energy $T^{\mu\nu}_{\mathrm{sub}}$ is unique (A.1 surviving; A.2–A.6 eliminated).
- Given $T^{\mu\nu}_{\mathrm{sub}}$, the DCGT mapping to continuum $T^{\mu\nu}_{\mathrm{eff}}$ is unique at leading order (B.1 surviving; B.2–B.5 eliminated; B.6 outside scope).

**This leaves OPEN:** the upstream question of *which $\mathcal{L}_{\mathrm{sub}}$ structure corresponds to each cosmological regime or radiation source class*. The construction-uniqueness closure is necessary but not sufficient for the M2 → M3 upgrade.

**Concretely, for each substrate-side $\Psi$ configuration on the substrate graph, classification questions:**

| Continuum-side class | Required substrate-side discrimination |
|---|---|
| LDE / inflation saturation ($w = -1$) | $\Psi$ configuration corresponds to substrate saturation regime |
| RDE radiation ($w = 1/3$) | $\Psi$ configuration corresponds to substrate "relativistic-analog" chain content |
| MDE matter ($w = 0$) | $\Psi$ configuration corresponds to substrate "non-relativistic-analog" chain content |
| EM Larmor source class | $\Psi$ configuration corresponds to substrate-side analog of accelerated gauge-coupled charge |
| GW quadrupole source class | $\Psi$ configuration corresponds to substrate-side analog of time-varying mass-quadrupole |

The **substrate-graph criterion** that selects the correct class from the substrate-side $\Psi$ configuration is what must be supplied for the M2 → M3 upgrade.

### §1.2 Why this is load-bearing

Without chain-class identification, the continuum-side prediction is *conditional on the standard-physics-analog inheritance* that named the class in the first place. The Q1A + Q2A closure ensures that *given* the correct $\mathcal{L}_{\mathrm{sub}}$, the construction is unique; but *which* $\mathcal{L}_{\mathrm{sub}}$ to use for a given substrate state remains an inherited choice. The M2 verdict for Cos_01 + Dyn_02 + Dyn_03 is driven by this remaining inheritance.

### §1.3 Per-paper M3-upgrade requirements

Different companion papers require different chain-class identification sub-closures:

| Paper | Regime / source classes needed | M3-upgrade requirement |
|---|---|---|
| **Paper_ED_Cos_01 (Inflation)** | Saturation (LDE) only — inflation is uniform-$\Psi$ saturation | Saturation identification only (likely tractable via §3.3 Route C3) |
| **Paper_ED_Dyn_02 (Horizon-Motion)** | All three (LDE + RDE + MDE) | Full regime classification — load-bearing on Routes C1 + C2 + C3 |
| **Paper_ED_Dyn_03 (Radiation Law)** | Two source classes (EM accelerated + GW time-varying multipole) | Full source classification — load-bearing on Routes C1 + C4 |

**This asymmetry is itself substantive:** Cos_01 may upgrade to M3 ahead of Dyn_02/Dyn_03 if saturation identification (C3) closes alone, while Dyn_02/Dyn_03 require the harder RDE/MDE / source-class discriminations.

---

## §2 Substrate-side classifying invariants

Five candidate substrate-side invariants could in principle classify regimes / source classes. Each must be evaluated for: (a) substrate-graph well-definedness; (b) load-bearing power for which regime / source class.

### (i) V1 propagation speed distribution

Per Paper_089, V1 has substrate-c bound (Paper_012 P-RB-1); per-chain propagation rates fill the interval $[0, c]$ in principle. The substrate-graph **distribution of V1 propagation rates** across chains in a given substrate region is a candidate classifier:

- Substrate region with chains concentrated near substrate-c → "relativistic-analog" → candidate RDE
- Substrate region with chains concentrated well below substrate-c → "non-relativistic-analog" → candidate MDE

**Substrate-graph well-definedness:** PARTIAL. Paper_089 supplies substrate-c as a propagation ceiling; the per-chain propagation rate as a substrate-graph parameter is not directly supplied. Paper_087 P04 (bandwidth) + P10 (multiple rule-types) supply structural support for distinguishing chains, but the specific *propagation rate* per chain is not constructed at substrate-graph level. **Load-bearing OPEN for substrate-graph V1 propagation-rate parameter.**

### (ii) V5 coupling-strength spectrum

Per Paper_090, V5 has finite-memory cross-chain coupling with directional weighting. The **spectrum of V5 coupling strengths** across substrate-graph locations is a candidate classifier:

- Substrate regions with strong V5 cross-chain coupling → potentially correlated content (substrate-side analog of fluid-like behavior; could distinguish thermal radiation from cold dust)
- Substrate regions with weak V5 coupling → uncorrelated content (substrate-side analog of free-streaming particles)

**Substrate-graph well-definedness:** PARTIAL. Paper_090 supplies V5's finite-memory structure but the per-substrate-locus coupling-strength parameter is not directly constructed. **Load-bearing OPEN for substrate-graph V5 coupling-strength parameter.**

### (iii) SC-4.9 Hessian eigenvalue structure

Per Paper_ED_SC_4_9, the substrate-action saddle Hessian classifies each substrate locus into compression-dominant and expansion-dominant orthogonal axes (S1/S2/S3 partition). The **Hessian eigenvalue-signature pattern** is a substrate-graph-clean invariant:

- All compression-dominant (S1-class) → collapsing region → potentially correlates with high-density / matter-dominated
- All expansion-dominant (S3-class) → expanding region → potentially correlates with low-density / radiation- or vacuum-dominated
- Mixed (S2-class saddle) → boundary / horizon → potentially correlates with non-stationary phases

**Substrate-graph well-definedness:** STRONG. Paper_ED_SC_4_9 supplies the Hessian classification directly. **The mapping from S1/S2/S3 to specific cosmological-phase $w$ values is OPEN substrate-graph.**

### (iv) $\Psi$-gradient magnitude and sign structure

The spatial gradient $\nabla \Psi$ and temporal gradient $\partial_t \Psi$ are substrate-graph well-defined quantities. The structure of these gradients classifies:

- Vanishing gradients ($\nabla \Psi = 0$, $\partial_t \Psi = 0$) → uniform $\Psi$ → **saturation regime** (LDE / inflation)
- Non-vanishing spatial gradient, vanishing temporal → spatially-varying stationary → candidate non-saturation stationary (RDE / MDE depending on form)
- Non-vanishing temporal gradient → time-varying $\Psi$ → candidate radiation source class

**Substrate-graph well-definedness:** STRONG. Gradients of $\Psi$ are directly defined on the substrate graph; no additional primitive content required.

### (v) Chain-mass / chain-velocity distributions

Per Paper_087 P04 (bandwidth) + Paper_098_5/T1 (spin-statistics), substrate-graph chains have effective mass content (bandwidth-weighted). Chain "velocity" corresponds to the V1-propagation rate per (i). The joint **mass-velocity distribution** across chains is a candidate classifier — substrate-side analog of standard kinetic-theory distribution function.

**Substrate-graph well-definedness:** PARTIAL. Paper_087 P04 supplies bandwidth; effective chain-mass requires composition with P02 (participation) + P12 (ED-threshold); construction at substrate-graph level is implicit but not explicit. Together with (i), this is the substrate-graph analog of the standard kinetic-theory phase-space distribution. **Load-bearing OPEN for substrate-graph chain-mass parameter construction.**

---

## §3 Continuum-side invariants that must match

For each candidate substrate-side classifier, the closure must show that the classifier reproduces standard continuum-side regime / source-class invariants.

### §3.1 Equation-of-state parameter $w$

The cosmological regime equation-of-state $w$ values: $-1$ (LDE), $0$ (MDE), $1/3$ (RDE). The substrate-side classifier must reproduce these specific values from substrate-graph content, not from inheritance.

### §3.2 Multipole moment structure

Radiation source classification by multipole structure: monopole + dipole gravitational radiation forbidden by conservation; quadrupole is leading; higher multipoles subleading. EM analog: monopole forbidden by charge conservation; dipole leading; higher subleading.

### §3.3 Acceleration class

Radiation source classification by acceleration: uniformly moving (no radiation); uniformly accelerated (Larmor; constant); oscillating (Larmor; periodic + spectrum). Substrate-side classifier must reproduce per-class predictions.

### §3.4 Horizon behavior

Cosmological-phase classification by horizon behavior: de Sitter constant horizon (LDE); power-law growing horizon (RDE/MDE per phase). Substrate-side classifier must reproduce horizon kinematics.

---

## §4 Route map for closure strategies

### §4.1 Route C1 — V1 / V5 spectral classification

**Mechanism:** combine substrate-side invariants (i) + (ii) + (v). Construct substrate-graph kinetic-theory-analog phase-space distribution per chain (mass, velocity, V5-coupling); map distribution moments to continuum-side regime / source classifications.

- Rapid V1 propagation + weak V5 coupling → free-streaming relativistic → RDE
- Slow V1 propagation + strong V5 coupling → bound non-relativistic → MDE
- Time-varying chain distribution at source locus → radiation source

**Plausibility:** MEDIUM. The substrate-graph kinetic-theory-analog construction is the natural pathway but rests on three load-bearing OPEN sub-claims (per-chain V1 propagation rate; per-locus V5 coupling strength; substrate-graph chain-mass parameter) that the corpus supplies structurally but not constructively.

**Load-bearing for Dyn_02 RDE/MDE upgrade + Dyn_03 source-class identification.**

### §4.2 Route C2 — SC-4.9 Hessian signature → $w$-class identification

**Mechanism:** use substrate-side invariant (iii). Map Hessian eigenvalue signatures (S1/S2/S3 classes per locus; bulk partition over substrate region) to continuum equation-of-state $w$ values via DCGT averaging.

- Saturation (uniform Ψ at saddle) → all-equal Hessian eigenvalues → vacuum-energy ($w = -1$)
- Compression-dominant bulk (S1-dominated) → high-density → matter-like ($w = 0$)
- Mixed compression / expansion → relativistic-like / radiation ($w = 1/3$)

**Plausibility:** MEDIUM-LOW. The Hessian signature is substrate-graph-clean but its mapping to specific $w$ values is not standard kinetic-theory content; it would require a substrate-graph derivation that DCGT averaging of the Hessian partition reproduces the standard equation-of-state values. Possibly vocabulary-level (Hessian signature reframes the same phenomenology as Route C1 without supplying additional substrate-graph content), possibly substantive (Hessian gives a primitive-derived discrimination Route C1 doesn't).

**Possibly load-bearing for Dyn_02 RDE/MDE upgrade; possibly vocabulary-level.**

### §4.3 Route C3 — $\Psi$-gradient sign structure → saturation vs non-saturation

**Mechanism:** use substrate-side invariant (iv). Identify saturation regime by vanishing $\Psi$-gradients; non-saturation regimes by non-vanishing gradients.

- $\nabla \Psi = 0$, $\partial_t \Psi = 0$ → uniform → LDE saturation / inflation ($w = -1$)
- $\nabla \Psi \neq 0$, $\partial_t \Psi = 0$ → spatially-varying stationary → non-saturation (RDE/MDE; C3 doesn't discriminate further)
- $\partial_t \Psi \neq 0$ → time-varying → radiation source (C3 doesn't discriminate EM vs GW)

**Plausibility:** HIGH for the saturation / non-saturation discrimination; substrate-graph trivial (gradients are directly defined on substrate). LOW for RDE vs MDE discrimination (both are non-uniform stationary; C3 alone doesn't separate them).

**Load-bearing for Cos_01 saturation case M2 → M3 upgrade. Not sufficient for Dyn_02 / Dyn_03 full upgrade.**

### §4.4 Route C4 — Multipole-moment structure → radiation-source class

**Mechanism:** combine substrate-side invariants (iv) + (v). Compute substrate-graph spatial moments of $\Psi$-distribution and gauge-bundle content (per Paper_015 T17); map moment time-derivative structure to radiation-source classification.

- Time-varying spatial second-moment of $\Psi$-distribution → mass-quadrupole → GW source class
- Time-varying spatial first-moment of gauge-bundle content (Paper_015 T17 charge) → electric-dipole → EM source class (Larmor)
- Higher multipoles → subleading source classes

**Plausibility:** HIGH for source-class identification; multipole moments of $\Psi$-distribution + T17 gauge-bundle content are substrate-graph well-defined.

**Load-bearing for Dyn_03 source-class identification.**

---

## §5 Load-bearing vs vocabulary-level routes

| Route | Load-bearing? | Per paper |
|---|---|---|
| **C1** (V1/V5 spectral classification) | **YES** | Required for Dyn_02 RDE/MDE upgrade; required for Dyn_03 acceleration class within source classes |
| **C2** (Hessian signature → $w$) | Possibly vocabulary; possibly substantive — needs explicit construction | If substantive: alternative path for Dyn_02 RDE/MDE |
| **C3** ($\Psi$-gradient → saturation/non-saturation) | **YES (partial)** | Sufficient for Cos_01 saturation upgrade; insufficient for Dyn_02 RDE/MDE; insufficient for Dyn_03 |
| **C4** (multipole structure → source class) | **YES** | Required for Dyn_03 source-class identification |

**Net assessment:**

- **Best closure path for Cos_01:** Route C3 alone may suffice (saturation case is the cleanest; Q1A handles the construction; C3 confirms saturation regime selection). **Cos_01 may upgrade M2 → M3 ahead of Dyn_02/Dyn_03.**
- **Best closure path for Dyn_02:** Routes C1 + C3 jointly (C3 for LDE; C1 for RDE/MDE discrimination). C2 may serve as supporting / tightening route if substantive.
- **Best closure path for Dyn_03:** Routes C1 + C4 jointly (C1 for accelerated-chain definition within EM source class; C4 for source-class identification + multipole structure).
- **Joint upgrade pathway for all three papers:** Routes C1 + C3 + C4 jointly — three load-bearing routes; C1 carries the highest closure-uncertainty (three sub-OPEN substrate-graph parameters); C3 + C4 likely close cleanly.

---

## §6 OPEN subproblems

### §6.1 Load-bearing OPEN substrate-graph parameter constructions (for Route C1)

| Sub-OPEN | Description | Closure path |
|---|---|---|
| **CC-OPEN-1** | Per-chain V1 propagation rate as substrate-graph parameter | Construction from Paper_087 P04 (bandwidth) + P10 (rule-types) + Paper_089 V1 substrate-c-bound structure |
| **CC-OPEN-2** | Per-substrate-locus V5 coupling strength as substrate-graph parameter | Construction from Paper_090 finite-memory + directional weighting structure |
| **CC-OPEN-3** | Substrate-graph chain-mass parameter | Construction from Paper_087 P04 (bandwidth) + P02 (participation) + P12 (ED-threshold) composition |
| **CC-OPEN-4** | Substrate-graph kinetic-theory-analog distribution function over (chain-mass, V1-rate, V5-coupling) | Composition of CC-OPEN-1 + 2 + 3 into joint distribution; map distribution moments to continuum-side regime classifications via DCGT averaging |

CC-OPEN-1 through CC-OPEN-4 are jointly load-bearing for Route C1 closure. **Likely closure plausibility: MEDIUM** — corpus supplies the structural support but not the explicit constructions; the work is *construction* using existing primitive content (consistent with Q1A's successful pattern).

### §6.2 Load-bearing OPEN identification map (for Route C2)

| Sub-OPEN | Description |
|---|---|
| **CC-OPEN-5** | Substrate-graph derivation that DCGT averaging of S1/S2/S3 Hessian-signature partition reproduces standard continuum equation-of-state $w$ values per regime |

CC-OPEN-5 is the load-bearing question for Route C2. **Likely closure plausibility: LOW-MEDIUM** — no standard kinetic-theory precedent for Hessian → $w$ mapping; novel substrate-research-frontier construction.

### §6.3 Load-bearing OPEN identification map (for Routes C3 + C4)

| Sub-OPEN | Description |
|---|---|
| **CC-OPEN-6** | Substrate-graph derivation that uniform $\Psi$ → saturation regime / $w = -1$ at continuum (substrate-graph composition with Q1A vacuum-energy derivation) |
| **CC-OPEN-7** | Substrate-graph derivation that time-varying $\Psi$ spatial second-moment → continuum GW source via Paper_ED_SC_4_9 saddle-Hessian framework + DCGT |
| **CC-OPEN-8** | Substrate-graph derivation that time-varying Paper_015 T17 gauge-bundle dipole → continuum EM source via DCGT |

CC-OPEN-6 is **likely closure plausibility: HIGH** (Q1A already handles the substrate-side; C3's saturation identification is the trivial discrimination case).

CC-OPEN-7 and CC-OPEN-8 are **likely closure plausibility: MEDIUM-HIGH** — multipole structure is substrate-graph clean; the DCGT translation to standard continuum source forms is the load-bearing step (potentially substantively closed by Q2A's coarse-graining invariance result).

### §6.4 Auxiliary OPEN (not load-bearing for M3 upgrade)

- Substrate-graph derivation of cosmological phase-transition times (RDE→MDE; MDE→LDE) — quantitative-magnitude question tied to Route A and substrate temperature evolution; not addressed by chain-class identification.
- Substrate-graph derivation of radiation-reaction self-force effects — standard physics inheritance.
- Substrate-graph derivation of higher-multipole subleading radiation — extends from C4 same template.

---

## §7 Expected audit flags

Anticipated audit qualifications for the closure attempts:

**For Route C1:** the substrate-graph parameter constructions (CC-OPEN-1 through 4) may require composition steps that are *structurally implicit* in Paper_087's primitive set rather than *explicitly constructed*. Audit will examine whether the implicit-vs-explicit distinction matters for load-bearing content. **Anticipated audit verdict: ACCEPTED with structural-construction qualification** (analogous to Q1A's audit pattern), provided the constructions don't require new primitives.

**For Route C2:** the Hessian → $w$ mapping (CC-OPEN-5) is the highest audit-risk component. **Anticipated audit verdict: possibly REJECTED for failing to supply load-bearing content beyond Route C1** (vocabulary-level finding) or **ACCEPTED with novel-construction qualification** if a substantive substrate-graph derivation closes it.

**For Route C3:** CC-OPEN-6 is the cleanest sub-closure. **Anticipated audit verdict: ACCEPTED** (composition of Q1A's saturation case with $\Psi$-gradient identification is structurally clean).

**For Route C4:** CC-OPEN-7 and CC-OPEN-8 are multipole-structure closures. **Anticipated audit verdict: ACCEPTED with DCGT translation qualification** (similar to Q2A's coarse-graining inheritance level).

### Negative-finding possibilities (acceptable outcomes)

- **N1:** CC-OPEN-1 through 4 cannot be constructed from existing primitives without standard-physics-analog inheritance — substrate ontology genuinely does not supply per-chain V1 propagation rate as a substrate-graph parameter. Dyn_02 RDE/MDE + Dyn_03 acceleration class remain M2 permanently; Cos_01 (saturation only) upgrades M2 → M3 via Route C3 alone.
- **N2:** Route C2 is purely vocabulary-level — Hessian signature reframes but doesn't supply additional substrate-graph content beyond Route C1. Substrate-research-frontier finding: Hessian classification is structural reframing tool, not a load-bearing closure mechanism for $w$-class identification.
- **N3:** Joint C1 + C2 + C3 + C4 closure shows that substrate-graph chain-class identification works structurally but reduces to a relabeling of standard-physics analog choices — substrate ontology genuinely closes the construction-uniqueness side but not the regime-identification side. Substantive corpus contribution: substrate ontology supports standard cosmology / radiation phenomenology *via* standard-physics-analog inheritance even at the chain-class level.

All three negative-finding outcomes are corpus-informative.

---

## §8 Recommended next steps

**Path-C3-Construction (highest closure plausibility; targets Cos_01 alone):** focused construction memo attempting CC-OPEN-6 — substrate-graph derivation that uniform $\Psi$ → saturation regime / $w = -1$ at continuum. Likely closes cleanly (composition with Q1A's saturation case). **If this closes, Cos_01 upgrades M2 → M3 ahead of Dyn_02/Dyn_03.**

**Path-C4-Construction (high closure plausibility; targets Dyn_03):** focused construction memo attempting CC-OPEN-7 + CC-OPEN-8 — multipole-structure substrate-graph derivations for GW and EM source classes. Likely closes at Q2A-equivalent level.

**Path-C1-Construction (medium closure plausibility; targets Dyn_02 + Dyn_03):** focused construction memo attempting CC-OPEN-1 through 4 — substrate-graph parameter constructions for per-chain V1 rate, per-locus V5 coupling, chain-mass, and joint kinetic-theory-analog distribution function. **Highest-impact substrate-research-frontier work in the chain-class identification project.**

**Path-C2-Construction (lowest closure plausibility; possibly vocabulary-level):** attempt only after C1 + C3 + C4 to determine whether Hessian-signature mapping supplies additional substrate-graph content or is vocabulary-level.

**Path-Joint-Audit:** Claude-B-class adversarial audit of the composed C1 + C3 + C4 closure once construction memos exist.

### My recommendation

**Sequence: Path-C3-Construction → Path-C4-Construction → Path-C1-Construction → Path-Joint-Audit → Path-C2-Construction (if needed for tightening).**

This sequence prioritizes the highest-plausibility closures first (C3 closes Cos_01 fastest), supplies Dyn_03 source-class identification next (C4), and then attempts the harder C1 substrate-graph parameter construction (Dyn_02 RDE/MDE + Dyn_03 accelerated-chain definition). If C1 fails (N1 negative finding), Cos_01 M3 upgrade still proceeds via C3 alone; Dyn_02 / Dyn_03 honestly remain M2.

### Cross-program impact summary

| Sequence outcome | Cos_01 | Dyn_02 | Dyn_03 |
|---|---|---|---|
| C3 closes (CC-OPEN-6) | **M3** | M2 | M2 |
| + C4 closes (CC-OPEN-7 + 8) | **M3** | M2 | **M3 (source-class) but possibly M2 if C1-acceleration-class blocks** |
| + C1 closes (CC-OPEN-1 through 4) | **M3** | **M3** | **M3** |
| All four close + Q1A + Q2A audits accept | **M3** | **M3** | **M3** |

**Best case:** all four routes close + Q1A/Q2A audits accept → **three-paper simultaneous M2 → M3 upgrade**.

**Mid case (most likely):** C3 + C4 close cleanly + C1 partially closes → **Cos_01 + Dyn_03 (source-class) upgrade to M3; Dyn_02 + Dyn_03 (acceleration-class) remain M2**.

**Worst case (N1):** C3 closes only → **Cos_01 upgrades M2 → M3; Dyn_02 + Dyn_03 honestly remain M2 with sharpened substrate-ontology characterization** (substrate ontology supports saturation-regime substrate-graph derivation but not non-saturation regime identification beyond standard-physics inheritance).

All outcomes are corpus-informative. The chain-class identification scoping clarifies which substrate-research-frontier sub-problems are tractable and which honestly cap the M2 → M3 upgrade.

**Closure plausibility for the full chain-class identification closure: MEDIUM**, comparable to Q1/Q2 joint closure overall. The work is *construction* using existing primitive content; if any sub-construction fails, the failure is a corpus-informative substrate-ontology characterization, not wasted effort.

---

**End Memo_ED_ChainClassIdentification_Scoping.**
