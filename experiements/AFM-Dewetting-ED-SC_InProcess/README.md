# AFM Thin-Film Polymer Dewetting — ED-SC 2.0 Cross-Scale Test #1

**Status:** InProcess. Protocol complete and session-ready; execution not yet commissioned.

**Test of:** ED-SC 2.0 architectural invariance claim — the motif-conditioned median of the field-space Hessian eigenvalue-ratio distribution satisfies `med(ℛ_motif) = r* ≈ −1.30 ∈ [−1.50, −1.10]` on 2D real-space scalar density fields.

**Observable:** height field `h(x, y)` of spin-coated polystyrene on silicon, annealed into the spinodal pre-rupture regime, measured by tapping-mode AFM at `Δx ≤ L_coh/8` resolution.

**Reference system:** Scenario D at `(n*, σ*) = (2.7, 0.0556)` gives `med(ℛ_motif) = −1.304`. AFM target system should match within `ε_med = 0.20`.

**Channel exercised:** architectural / cross-scale invariant — tests mobility-curvature geometry at the motif level, not a single PDE channel.

**Next action:** Execute Route 1 first (check 2023 *Nat Comm Phys* paper for accessible AFM data — 5 min); chain to Route 2 (email Jacobs group at Saarland) or Route 3 (book a 1–2 day session at any academic core facility with PS-on-Si dewetting samples) based on Route 1 outcome.

**Budget (Route 3):** ~$500 AFM facility + 2 weeks analysis. Total calendar time to publishable result: 4–6 weeks.

**Contents of this folder:**

| File | Purpose |
|:---|:---|
| `protocol.md` | Full operational protocol (sample prep, scan parameters, data export, analysis pipeline, 5-outcome decision tree, deliverables, risks). Canonical methods reference for this experiment. |
| `README.md` | This file — status landing page. |

**Key external references** (see `protocol.md` §10 for full list):
- Canonical ED-SC 2.0 statement: [`docs/ED-SC-2.0.md`](../../docs/ED-SC-2.0.md)
- Pilot memo (undecidable N=1 outcome that motivates this protocol): [`analysis/scripts/ed_arch_r2/ThinFilm_Pilot_Memo.md`](../../analysis/scripts/ed_arch_r2/ThinFilm_Pilot_Memo.md)
- Orientation: [`docs/ED-Orientation.md`](../../docs/ED-Orientation.md) §6.9 (ED-SC 2.0), §7 empirical-status table row.

**Status transitions (for folder rename when outcome lands):**
- `AFM-Dewetting-ED-SC_Evidence` on PASS outcome (median in band).
- `AFM-Dewetting-ED-SC_Falsified` on FAIL outcome (median outside `[−1.80, −0.90]`).
- `AFM-Dewetting-ED-SC_Inconclusive` on UNDECIDABLE outcome.
- Current: `_InProcess` — protocol ready, execution pending.
