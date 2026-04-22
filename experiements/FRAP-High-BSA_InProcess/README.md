# FRAP in Concentrated BSA — UDM Mobility-Channel Test

**Status:** InProcess. **Protocol submitted to Creative Proteomics CIBR on 2026-04-17; CP forwarded internally to their technician team same-day.** Decision window: 2026-04-24 to 2026-05-01.

**Test of:** Universal Degenerate-Mobility (UDM) law — the ED mobility channel `M(ρ) = M_0(ρ_max − ρ)^β` with canonical `β ≈ 2` predicts the 2D porous-medium equation with `m = β + 1 = 3`, giving front-radius exponent `α_R = 1/(d(m-1)+2) = 1/6 ≈ 0.167`.

**Observable:** FRAP recovery front radius `R(t)` in concentrated BSA-FITC. ED predicts `R(t) ~ t^(1/6) ≈ t^0.16` with a **sharp** bleach boundary (compact support, PME signature). Fickian diffusion predicts `R(t) ~ t^0.50` with a Gaussian-blurred boundary.

**Concentrations tested:** 200, 250, 300, 350 mg/mL (φ = 0.15, 0.18, 0.22, 0.25). 5 bleaches per concentration = 20 total acquisitions.

**Channel exercised:** mobility (Canon principle P4 — Mobility Capacity Bound).

**Relationship to Universal_Mobility_Law_Evidence:** This is an **independent second confirmation** of the UDM 10-material result (`R² > 0.986`) via a different observable (front propagation rather than diffusion-coefficient regression). A PASS here complements the existing Evidence folder without replacing it.

**Next actions:**
1. **Await CP decision** (by 2026-05-01).
2. On approval: sample prep at CP, 2-hour microscope session, data return as full TIFF stacks.
3. **Implement analysis pipeline** `analysis/scripts/udm_frap/frap_udm_pipeline.py` per `protocol.md` §9.4 (can begin in parallel with CP decision).
4. **Execute pipeline** on 20 acquisitions; per-concentration and ensemble decision per `protocol.md` §10.
5. **Write up** PASS/NEAR-PASS/FAIL/UNDECIDABLE/SPLIT outcome.

**Budget:** ~$500–$1500 for the CP session (all-inclusive). ~2 weeks of personal analysis time. Total calendar time to publishable result: 6–8 weeks from CP decision.

**Contents of this folder:**

| File | Purpose |
|:---|:---|
| `protocol.md` | Full operational protocol. §4–§8 is the **exact text submitted to CP** (sample prep, bleach parameters, imaging, acquisition timing, replication). §1–§3 provide ED theoretical derivation of the `t^0.16` exponent. §9–§12 give the analysis pipeline and 5-outcome decision tree. §13 flags 7 review-level notes for a V2 protocol. |
| `BSA mobility high concentration revised.pdf` | Prior research document on BSA mobility at high concentration — theoretical context and background literature. |
| `README.md` | This file — status landing page. |

**Key external references** (see `protocol.md` §16 for full list):
- Orientation: [`docs/ED-Orientation.md`](../../docs/ED-Orientation.md) §7 empirical-status table row, top-of-doc 2026-04-17 entry.
- Companion UDM empirical result: [`Universal_Mobility_Law_Evidence/`](../Universal_Mobility_Law_Evidence/) — 10-material fit, published `R² > 0.986`.
- ED PDE canonical form: [`theory/PDE.md`](../../theory/PDE.md) (mobility channel) and [`theory/Architectural_Canon.md`](../../theory/Architectural_Canon.md) P4.

**Status transitions (for folder rename when outcome lands):**
- `FRAP-High-BSA_Evidence` on PASS outcome (α_R in `[0.125, 0.170]` at ≥ 3/4 concentrations, PME-front beats Fickian via AIC).
- `FRAP-High-BSA_Falsified` on FAIL outcome (α_R ≥ 0.35 or Fickian-front wins at all c).
- `FRAP-High-BSA_Inconclusive` on UNDECIDABLE / NEAR-PASS without resolution.
- Current: `_InProcess` — protocol at CP, decision pending.
