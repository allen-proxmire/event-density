# Parked routes and open threads — mass / memory / V5 investigation

**Started:** 2026-07-06. **Purpose:** AP's explicit instruction — "don't lose track of routes we don't pursue and still can." This is the durable ledger of live-but-unpursued threads from the mass-generation / intrinsic-memory / V5-characterization work, so none of them get lost when a session ends or attention moves. Each entry: what it is, why it's live, and the concrete first move if picked up.

## Actively parked (real, unpursued, still open)

1. **Self-trail vs. other-trail behavior (the "#2" test, queued all session, never run).**
   Does a chain react to its OWN commitment trail differently than to another chain's? Real mass memory should be self-specific (a particle feels its own history, not everyone's). Test 1 (`Dwell_Trail_Detection_Results.md`) found a later front reacts to *any* trail, but never distinguished self from other. First move: tag commits with chain identity, run two fronts, compare a front's response to its own prior path vs. a stranger's. Cheap, well-scoped, unblocked now that the fade-rate question is settled-as-partial.

2. **"Waves have memory" — is QM's wave nature the macroscopic face of short chain memory? (AP, 2026-07-06.)**
   A wave equation is second-order in time (needs a one-tick look-back); a memoryless process diffuses, a finite-memory process oscillates. Finite memory is mathematically *what turns spreading into waving*. If chains are "a few commitments long," their finite memory may be exactly what produces wave behavior at the QM layer. First move: take the intrinsic-memory mechanism (`dwell_intrinsic_memory_probe.py`) and check whether a memory-carrying front shows oscillatory / interference-like position statistics (a real look-back structure) versus the pure diffusion/ballistic of the memoryless certified rule. Connects to V5 (the finite-memory kernel) and to `Paper_012`'s phase-rate content.

3. **Gauge-boson coupling, revisited with the intrinsic-memory mechanism as the starting point.**
   `Dwell_To_GaugeBoson_Coupling_Scoping.md` named four missing pieces (no gauge-boson object in the sim; H1's unbuilt vertex; trail-vs-condensate mismatch; no standing background ever built). The intrinsic-memory result is a stronger foundation than what that scoping used. First move: check whether two memory-carrying fronts can be coupled so one acquires effective mass from the other's presence — the minimal "boson gets mass from a field" analogue.

4. **V5 envelope shape from primitives — the trajectory-based re-attempt.**
   The diffusion/Green's-function analogy failed (`V5_Envelope_Shape_From_P11_Scoping.md`, third/fourth pass) because the substrate is discrete/competitive/trajectory-based, not a smooth diffusing field. A derivation starting from the substrate's *actual* character (worldline reach limited by commitment) has not been tried. First move: model V1's envelope as a survival probability along a single worldline (front survives to distance x with prob depending on commitment events en route), not as a field Green's function.

5. **Pinning k₁₁ — the recurring unexplained O(1) commitment factor.**
   The same order-1 dimensionless factor bottoms out the mass fade rate, the GR α₁ screening, the QC decoherence rate, and QFT vertex rates. If it were derived once, it cascades across all four. First move: check whether the four arcs' O(1) factors are numerically the *same* value (they're structurally analogous — are they equal?), which would itself be strong evidence they share an origin.

## Cross-connection under active investigation (this is "#1", in progress 2026-07-06)

6. **Is the mass-memory fade rate the same quantity as the GR sparse-commitment parameter? — INVESTIGATED 2026-07-06, verdict (b) plausible-not-proven** (`Mass_GR_SparseCommitment_CrossConnection.md`).
   Corroborated: both are built from the same P04 commitment-reserve band, carry the same dimensionless `k₁₁`, and share the same `ρ_event/ρ_Planck` scaling — a genuinely novel, structurally solid link. Ceiling: only `k₁₁` is truly shared; the regime magnitudes (`ρ_event` vacuum-worldline vs Solar-System) stay separately unpinned, so "pin one, pin both" holds only for `k₁₁`. Still open, two concrete next moves below.

6a. **Dependency-check gap found + CHECKED 2026-07-06** (`foundations/GR_BandDependency_Check_2026-07-06.md`). Verdict: SUBSTANTIVELY CANONICAL. The GR α₁ measurement sources its two load-bearing bands from P02 always-on sharing (`M_P²`, density-independent) vs P11 sparse commitment (`f²`, ∝ρ_event) — a canonical P02-vs-P11 decomposition, not the archived four-band structure. The α₁ safety verdict does NOT rest on archived structure. Residual: presentational only — the GR docs still cite "P04 §1.5 four-band" and want the same re-framing fix the mass sector got. RESOLVED as a research question; leaves a small presentational-cleanup task (below).

6b. **Promote #6 from (b) to (a):** show the *same numerical* `k₁₁` governs both mass and GR (they're structurally the same symbol — are they equal in value?). Blocked in practice by the multi-simulator gap (target A9); paper-level check only for now.

## Hygiene threads noted earlier tonight, still open

7. **T14 downstream cascade re-audit.** T14's promotions of U2/U5/Bell/Heisenberg were never re-checked after T14 itself was downgraded. (§G item 5 of the open-targets map.)
8. **Hawking-2π three-way reconciliation** — optional forward-pointer between `Paper_043`, `BH_Thermal2Pi`, `Paper_047` (chronological, not a bug; a one-line "see also" would tidy it).
9. **Second approach to eliminate k_mem** — the coherence-target-shift approach failed cleanly; other reduction approaches (e.g., tying coupling to bandwidth b directly) untried.
10. **Presentational fix: re-frame the GR band-partition docs** (`Phase3_GR_BandPartition_Scoping.md`, `..._TargetA_Findings.md`, and any four-band framing in `LambdaOfRho_Derivation.md`/`PinningKappaD.md`) from "P04 §1.5 four-band" to a canonical P02-vs-P11 decomposition — same class of fix already identified for Arc M + the position paper. Substance is fine (checked 2026-07-06); only the citation over-claims. Batch it with the mass-sector four-band presentational fix.
