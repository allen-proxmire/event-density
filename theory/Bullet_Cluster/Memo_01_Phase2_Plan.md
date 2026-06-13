# Memo-01 — Bullet_Arc Phase-2 Execution Plan

**Arc:** Bullet_Arc (ED-Bullet-01)
**Memo:** 01 (Phase-2 execution plan)
**Status:** Phase-1 complete; Phase-2 initiated
**Date filed:** June 2026
**Author:** Allen Proxmire
**Authoritative scope document:** `Memo_00_Bullet_Arc_Scoping.md`

---

## 1. Phase-2 Overview

### What Phase-2 is responsible for delivering

Phase-2 determines whether **"topological"** is physics or metaphor in the Bullet_Arc reading. Phase-1 captured the qualitative claim: a fast cluster merger overdrives substrate saturation, the substrate cannot equilibrate, a frozen-in winding forms, and gravity tracks the winding rather than the displaced gas. Phase-2 must close three formal deliverables to convert that qualitative reading into a structural claim that earns its formal designation.

The three deliverables are:

- **D2.1** — Identify the substrate's organizational order parameter at cluster scales; identify its vacuum manifold *M*; compute π_n(*M*); determine whether nontrivial topology supports stable defects.
- **D2.2** — If D2.1 succeeds, define the integer topological charge a Bullet-class defect carries; show conservation under substrate dynamics on timescales much greater than the merger crossing time.
- **D2.3** — Derive (or phenomenologically estimate) the substrate's organizational relaxation timescale τ_relax at cluster scales; compare to merger crossing times.

Phase-2 also delivers a synthesis paper (`Paper_ED_Bullet_TopologicalDefect.md`) that integrates D2.1–D2.3 with the Phase-1 qualitative reading.

### How Phase-2 builds on Phase-1

Phase-1 produced:
- The qualitative articulation (`Memo_Bullet_TopologicalDefect_Overshoot.md`)
- The Kibble-mechanism analogy
- The arc scoping (`Memo_00_Bullet_Arc_Scoping.md`)
- Four qualitative predictions (P1–P4) and four falsification paths (F1–F4)

Phase-2 takes those predictions and falsification paths as structural targets and asks: what formal commitments would the substrate have to make for these predictions to be *forced*, not just consistent? D2.1 answers the question "what's the order parameter?"; D2.2 answers "what's conserved?"; D2.3 answers "for how long?". Together they convert the Kibble analogy into a substrate-native mechanism.

### How Phase-2 prepares for Phase-3

Phase-3 is the observational engagement layer — testing predictions P1–P4 against weak-lensing data from multiple merging clusters. Phase-2 enables Phase-3 by:

- **D2.3 → critical merger velocity.** The freeze-in condition (t_merger ≪ τ_relax) determines a critical velocity. Phase-3 catalogs systems above and below the threshold.
- **D2.1 → discrete-vs-smooth prediction.** Whether the vacuum manifold admits stable topological defects determines whether Phase-3 should expect a knee (F2) or a smooth roll-off in the offset-vs-velocity relation.
- **D2.2 → multi-merger complexity.** The structure of the topological charge determines whether multi-component mergers (P4) produce predictable defect superpositions.

---

## 2. Work Breakdown Structure

### D2.1 — Vacuum Manifold

| Field | Specification |
|---|---|
| **Inputs** | ED primitives P01–P13; V5 kernel structure (channel-organization at outer scales); V1 kernel for vacuum-coherence interpretation; DF2/DF4 saturation rule as steady-state baseline |
| **Process** | Survey candidate order parameters (scalar, vector, tensor and variants); compute vacuum manifold *M* for each; compute π_n(*M*) for *n* = 1, 2 (line and point defects in 3D); map each candidate to ED's substrate primitives; test compatibility with V5 quench dynamics; recommend a candidate |
| **Outputs** | `Paper_ED_Bullet_VacuumManifold.md` — specified order parameter, vacuum manifold *M*, homotopy classification, recommended candidate |
| **Dependencies** | P01–P13 register (canonical primitive labels); V5 kernel structure; Cos-05 / *a₀* derivation for the cosmological-floor baseline |
| **Risks** | (R2.1a) All candidates give trivial homotopy → topological framing fails → fallback to slow-relaxation defect; (R2.1b) Multiple candidates work equally well → require additional selection criterion (Phase-3 observational constraint); (R2.1c) Candidate works in V5 but not V1 → kernel-portability question raised |
| **Success criteria** | (i) A specific order parameter is named; (ii) its vacuum manifold *M* is identified; (iii) at least one nontrivial π_n(*M*) is found; (iv) candidate is consistent with V5 kernel structure; (v) candidate's defects could plausibly produce the Bullet's two-peak offset structure |

### D2.2 — Winding Number / Topological Charge

| Field | Specification |
|---|---|
| **Inputs** | D2.1 output (specified vacuum manifold *M* with nontrivial homotopy); substrate dynamics from V5; standard topological-charge formulations from field theory |
| **Process** | Define the integer topological charge carried by a Bullet-class defect (winding number, monopole charge, Hopf charge — whichever D2.1 makes natural); show conservation under substrate dynamics; identify possible decay channels and their timescales (relate to D2.3) |
| **Outputs** | `Paper_ED_Bullet_WindingNumber.md` — defined conserved charge, conservation argument, decay-channel analysis |
| **Dependencies** | D2.1 (closed); V5 dynamics; possibly insights from D2.3 on relaxation timescales |
| **Risks** | (R2.2a) D2.1 succeeds but D2.2 finds the charge is not strictly conserved (only quasi-conserved) → arc transitions to long-lived-metastable framing rather than topological; (R2.2b) Multiple inequivalent charges exist → need to determine which is observationally relevant for Bullet |
| **Success criteria** | (i) Charge is defined formally; (ii) conservation argument is structurally sound; (iii) decay timescale is consistent with D2.3's τ_relax |

### D2.3 — Substrate Organizational Relaxation Timescale τ_relax

| Field | Specification |
|---|---|
| **Inputs** | V5 kernel structure (channel-propagation rate, commitment-density gradient propagation); substrate primitives P05 (finite reach), P06 (finite memory); multi-cluster offset observations from Phase-3 catalog for phenomenological fit |
| **Process** | Attempt first-principles derivation of τ_relax from V5 (preferred); if not tractable, perform phenomenological fit to multiple observed merging clusters; compare result to merger crossing times (~10⁸ yr) to verify freeze-in condition |
| **Outputs** | `Paper_ED_Bullet_RelaxationTime.md` — timescale τ_relax (derived or fit), freeze-in condition statement, critical merger velocity prediction |
| **Dependencies** | V5 propagation machinery; Phase-3 catalog work (which can proceed in parallel) |
| **Risks** | (R2.3a) τ_relax much shorter than 10⁸ yr → no Bullet defect possible → arc fails F1; (R2.3b) τ_relax not derivable from first principles → must be inherited from observation (acceptable but weakens predictive power and makes the arc form-forced rather than form-and-value-derived) |
| **Success criteria** | (i) τ_relax determined within order of magnitude; (ii) Bullet's merger satisfies freeze-in (t_merger ≪ τ_relax); (iii) Phase-3 catalog can be designed with a specific critical-velocity threshold |

---

## 3. Integration Map

### V1 / V5 Kernel Integration

**V1 (Vacuum Kernel; Paper_013) — equilibrium interpretation.** V1 supplies the concept of substrate vacuum coherence that D2.1's order parameter formalizes. The order parameter at cluster scales is structurally the cluster-scale projection of V1's vacuum-coherence field. D2.1's vacuum manifold *M* should be expressible in V1 terms; if it is, kernel portability is established.

**V5 (current production kernel; Paper_090) — quench dynamics.** V5 supplies the outer-scale machinery and the saturation regime. The quench in Phase-1's framing is a V5-native event: V5 defines what "saturation overshoot" means by relating substrate commitment-density to outer-scale-coupling rates. D2.2's conservation argument and D2.3's relaxation timescale both rely on V5 propagation structure.

**Cross-kernel consistency check.** Phase-2 must verify that D2.1's vacuum manifold is consistent with both V1 and V5. If a manifold is V5-native but V1-incompatible, the kernel relationship itself requires examination — and the result is informative about V5 being a strict extension of V1 vs. an incompatible refinement.

### SCBU (Substrate Cosmology Boundary Universe) Integration — Route A Closure

**SCBU describes boundary structure of the substrate at cosmological scales.** The Bullet defect, if topological, is a substrate-level structure carrying a conserved charge — a kind of localized boundary condition on the substrate's organizational state. Whether the defect respects SCBU's Route A closure (the specific consistency condition by which SCBU's boundary handles internal substrate structure) is a cross-arc consistency check.

**Working assumption:** The Bullet defect is small (~Mpc scale) compared to SCBU's cosmological boundary (~Hubble scale). Defect existence should not perturb the global boundary closure to leading order. If a calculation shows it does — i.e., if a topological defect at cluster scale couples nontrivially to SCBU's Route A constraint — that's a substantive result and requires either modification of SCBU or revision of the arc.

**Verification deferred to Phase-2 synthesis.** This integration is flagged for explicit treatment in the Phase-2 synthesis paper. It should not block D2.1–D2.3 execution.

### Gravity Arc Integration (a₀, BTFR, ED-30/31)

**Paper_029 (a₀ = cH₀/(2π)) — the floor.** The cosmological outer-scale acceleration is the baseline against which the Bullet defect generates an enhancement. The defect doesn't replace a₀; it adds a localized contribution that augments the lensing signal at the defect's location. D2.1's vacuum manifold should connect formally to the a₀ floor: the manifold's "vacuum value" is the equilibrium state where the substrate carries a₀ but no defect enhancement.

**Paper_031 (BTFR — Baryonic Tully-Fisher Relation) — the constituent-galaxy check.** The constituent galaxies inside the merging clusters should continue to satisfy BTFR. The defect-contributed gravity acts at cluster scale, not at individual-galaxy scale, so individual galaxies should not be affected. This is a Phase-3 sanity check: if BTFR fails for Bullet-cluster galaxies, the defect's spatial extent is wrong.

**Paper_030 (Combination Rule) — how contributions add.** ED-30 specifies how multiple gravitational contributions combine. The Bullet defect's contribution to the cluster's lensing signal should add to standard cluster gravity according to ED-30's rule. D2.2 must respect ED-30's combination structure.

**Paper_031 (BTFR) — kernel portability check.** BTFR is derived in the gravity arc as a consequence of substrate channel-bundling at galaxy scales. Bullet_Arc's order parameter is the cluster-scale extension of the same channel-organization concept. The two should be related by a coarse-graining (galaxy-scale → cluster-scale). D2.1 should verify that its proposed order parameter coarse-grains correctly from the BTFR-supporting galaxy-scale structure.

---

## 4. FORM-FORCED / VALUE-INHERITED / OPEN Updates

Items whose classification changes upon entering Phase-2 (relative to Memo-00):

| Claim | Memo-00 Status | Phase-2 Status | Notes |
|---|---|---|---|
| Substrate has organizational state at cluster scales | FORM-FORCED | FORM-FORCED (confirmed) | The concept is structurally forced; specific identification is the D2.1 task |
| Order parameter is a vector field with vacuum manifold *S²* | n/a | **PROPOSED** (D2.1 working candidate) | This Memo-01's recommendation, pending paper completion |
| The post-quench state contains a frozen defect | OPEN | OPEN (D2.1 active) | |
| Defect is topological in the strict homotopy sense | OPEN | OPEN (D2.1 will resolve) | |
| Defect persists on ≳ 10⁸ year timescales | OPEN | OPEN (D2.3 will resolve) | |
| Anchored to pre-merger channel orientation | OPEN | OPEN (follows from D2.1 + D2.2 if they close) | |
| Defect type is point-monopole (hedgehog) | n/a | **PROPOSED** (consequence of vector + *S²* candidate) | Pending D2.1 closure |
| Each Bullet subcluster carries one monopole/antimonopole | n/a | **PROPOSED** (consequence of pair-production at the merger boundary) | Pending D2.1 + D2.2 |

---

## 5. Falsification-Path Alignment

Mapping of Phase-2 deliverables to Memo-00 falsification register:

| Falsification path | Connected deliverable | How it falsifies |
|---|---|---|
| **F1** — No velocity scaling | D2.3 (τ_relax → critical velocity); Phase-3 catalog tests | If τ_relax fit yields no critical velocity, OR Phase-3 finds no scaling, F1 triggers |
| **F2** — No discrete transition | D2.1 (vacuum manifold homotopy determines whether transition is discrete) + Phase-3 | If D2.1 finds trivial homotopy, F2 already triggered structurally; if homotopy is nontrivial but Phase-3 finds smooth transition, F2 triggers empirically |
| **F3** — No vacuum manifold structure | D2.1 directly | If all candidate order parameters give trivial homotopy, F3 triggers and arc transitions to slow-relaxation framing |
| **F4** — Numerical mismatch | D2.3 + Phase-3 catalog quantitative comparison | If τ_relax produces a critical velocity consistent with observation but offset *magnitudes* fail to match, F4 triggers as weak falsification (suggests modeling error in the substrate-to-lensing mapping rather than core arc failure) |

Note that F3 is the deepest falsification path because it operates at the structural-mathematics level (homotopy classification). F1 and F2 operate at the empirical-prediction level. F4 operates at the quantitative-comparison level.

---

## 6. Deliverables

### Phase-2 papers (to produce)

| File | Status | Description |
|---|---|---|
| `Paper_ED_Bullet_VacuumManifold.md` | **IN PROGRESS** — opening section filed alongside this memo | D2.1 — order parameter, manifold, homotopy |
| `Paper_ED_Bullet_WindingNumber.md` | NOT STARTED | D2.2 — conserved charge, conservation argument |
| `Paper_ED_Bullet_RelaxationTime.md` | NOT STARTED | D2.3 — τ_relax, freeze-in condition, critical velocity |
| `Paper_ED_Bullet_TopologicalDefect.md` | NOT STARTED | Synthesis — integrates D2.1–D2.3 with Phase-1 qualitative reading |

### Phase-2 memos (to produce)

| File | Status | Description |
|---|---|---|
| `Memo_01_Phase2_Plan.md` | **COMPLETE** (this document) | Phase-2 execution plan |
| `Memo_02_Bullet_Arc_Integration.md` | NOT STARTED | Closes Phase-2; integrates with full corpus; updates dependency graph |

### Cross-arc updates

- Update `Paper_095_FormForced_ValueInherited.pdf` with Bullet_Arc Phase-2 entries upon completion
- Update `Paper_087_13Primitives.pdf` if P10–P13 require canonical addition (decide after D2.1 closure)
- Update README to note Phase-2 in progress

---

## 7. Hand-off — Begin D2.1

Phase-2 begins immediately with **D2.1 (Vacuum Manifold)**.

The opening section of `Paper_ED_Bullet_VacuumManifold.md` is filed in this folder alongside this memo. It contains:

1. Survey of candidate order parameters (scalar, vector, tensor and variants)
2. Vacuum manifolds and homotopy groups for each
3. Mapping to ED substrate primitives
4. Compatibility analysis with V5 quench dynamics
5. Specific match-test against the Bullet Cluster's observed two-peak offset structure
6. Recommended candidate

The recommended candidate emerging from the opening section is a **vector order parameter with vacuum manifold *S²*** — supporting π₂(*S²*) = ℤ point-monopole defects. The recommendation follows from three converging arguments:

- The candidate has a direct mapping to ED primitive P10 (channel-orientation field)
- It is compatible with V5 quench dynamics via the standard Kibble mechanism for vector fields
- The defect type (point monopoles, formable in monopole/antimonopole pairs) naturally produces the Bullet's observed two-peak structure

Subsequent Phase-2 work will:

1. Complete the body of `Paper_ED_Bullet_VacuumManifold.md` (D2.1 closure)
2. Begin `Paper_ED_Bullet_WindingNumber.md` (D2.2) — formalize the monopole charge in the substrate-specific case
3. Begin `Paper_ED_Bullet_RelaxationTime.md` (D2.3) — derive or fit τ_relax

In parallel, Phase-3 catalog work (T3.1–T3.4 from Memo-00) can begin assembling the multi-cluster observational dataset; the catalog is independent of D2.1–D2.3 closure and may inform the formal work.

---

*End of Memo-01.*
