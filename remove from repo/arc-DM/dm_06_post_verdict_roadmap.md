# DM.6 — Post-Verdict Roadmap and Program Integration

**Date:** 2026-04-27
**Arc:** Dark Matter — closure memo
**Status:** **DM arc officially closed.** Canonical activity-source ED is structurally refuted at the BTFR test (DM.5 verdict: FAIL on RC #1 + RC #3); universality of κ_act (RC #2) is preserved as a partial positive finding. Damage is contained to the galactic-disc-dynamics sector. Foundational arcs (R, M, N, Q, B, GR, GR-SC) and cluster-scale calibration are intact. The DM-arc as currently scoped (mass-source → activity-source canonical PDE) has run to completion. Open structural questions surfaced by BTFR.01–09 are forwarded to the foundational and empirical arcs. **No further tasks are scheduled for the DM-arc itself.**
**Predecessor:** DM.5 (production-run verdict and structural diagnosis).
**Successor:** None within the DM-arc. Forwarded items: BTFR.10 candidate (foundational), merger-lag retrodiction (empirical), weak-lensing activity-dependent tests (empirical).

---

## 1. DM.5 verdict at the program level

The DM-arc was scoped (DM.0–DM.6 architectural memos) to test whether canonical ED, with the screened-Poisson penalty-channel PDE and an activity-dependent source, could reproduce SPARC galactic rotation curves and the Tully-Fisher relation without per-galaxy parameter tuning.

The DM2 production run executed that test on 175 SPARC galaxies (149 post-quality-cut). The BTFR sub-arc (BTFR.01–09) then provided the structural explanation for the run's outcome.

**Three program-level findings:**

- **Canonical ED fails BTFR structurally.** The failure is not numerical, not parameter-dependent, and not curable by re-running with different constants. Two independent structural conditions (C1: log far-field; C2: √M_b coupling) both fail. The numerical slope of 0.24 is what such a structurally-deficient theory produces under fitting; the structurally honest prediction of canonical self-consistent ED is slope-2, still inconsistent with the empirical slope-4.

- **Universality of κ_act survives.** σ(κ_act) / mean ≈ 2.1% across 149 galaxies, with all Spearman correlations against galaxy properties below 0.12. This is the qualitative ED prediction that *did* hold, distinguishing ED from per-galaxy-tuned dark-matter halos and from environment-dependent MOND variants. The result is provisional pending a longer-optimizer re-run (max_evals = 50 was hit during the production run), but the structural posture is correct.

- **Damage is contained to the galactic-disc-dynamics prediction.** No other ED prediction is affected. The cluster-scale merger-lag calibration that anchored D_T is unchanged. The screening length L ≈ 980 kpc is unchanged. Foundational arcs (R, M, N, Q, B, GR, GR-SC) and their forced theorems (T1–T9) are unchanged.

---

## 2. Downstream implications for the ED program

### 2.1 Foundational arcs

| Arc | Topic | Status after DM.5 |
|---|---|---|
| R | Relativistic emergence (KG, spin-statistics, Cl(3,1), Dirac, g=2) | **Unaffected.** No D_T or κ_act dependence. |
| M | Matter-wave structure (σ_τ form FORCED, values INHERITED) | **Unaffected.** |
| N | Vacuum kernel (Theorem N1: V1 finite-width) | **Unaffected** by canonical-ED BTFR. *Conditionally affected* if a future DM-arc revival pursues the nonlinear ED variant (BTFR.07 Option C); Theorem N1 was derived assuming linear PDE structure. |
| Q | Quantum sector (GRH, UV-FIN, canonical commutation, SM gauge structure) | **Unaffected.** |
| B | Born-Gleason / measurement foundations | **Unaffected.** |
| GR (Phase-3) | V1 with Synge world function (Theorem GR.1) | **Unaffected** by canonical-ED BTFR. *Conditionally affected* by Option C in the same way as Arc N. |
| GR-SC | Curvature-invariant taxonomy | **Unaffected.** |
| RG | Wilsonian three-regime structure | **Unaffected.** |
| ED-SC 3.x | Cross-scale invariance | **Unaffected.** |

The DM-arc result is structurally local to the gravitational-sector galactic-disc-regime prediction. **No upstream theorem revisions are required.**

### 2.2 Cluster-scale calibration

The cluster-merger-lag observation that anchors D_T (DM.0 §2) operates at scales R ~ Mpc, where the geometry is roughly 3D-isotropic and the deep-acceleration regime that MOND requires does not apply. The BTFR-relevant in-galaxy regime (R < 50 kpc, deep-acceleration window) and the cluster regime are observationally separate. The DM.5 verdict therefore does not retroactively threaten the cluster anchor, and any future BTFR-compatible extension of ED would need to preserve the cluster prediction as a consistency check.

### 2.3 Phase-3 gravitational sector

The Phase-3 work (six memos GR.0–GR.5, Theorem GR.1: V1 with Synge world function FORCED) extended Theorem N1 to curved spacetime via Hadamard-parametrix construction. None of this depends on the galactic-disc activity-source PDE. The Phase-3 gravitational-sector predictions (cosmological-constant from V1 kernel integral; V1-induced dispersion modifications; V5-mediated cosmological correlations; curvature-vacuum coupling) are **unaffected** by the DM.5 verdict.

The DM-arc's canonical PDE was always understood as a coarse-grained galactic-regime equation, not as the foundational gravitational equation. DM.5's failure is at the coarse-graining level, not at the foundational level.

---

## 3. Open structural questions surfaced by BTFR.01–09

The BTFR sub-arc traced the canonical-ED failure to specific structural causes and identified the structural ingredients any BTFR-compatible theory must contain. Four questions emerged that are open at arc closure:

### 3.1 The C2 (slope-4) structural mechanism

No version of ED examined in BTFR.01–09 produces slope-4 BTFR without an external structural commitment. The minimal commitment sets identified are:

- **Route II-A:** import an MOND-like coupling weighting ν(a/a₀). Recovers slope 4 in deep-acceleration regime. No theoretical advance over MOND.
- **Route II-B:** postulate a sublinear (√ρ_b-yielding) source functional. Less canonical, more degrees of freedom.
- **Route II-C / Option C:** replace the linear screened-Poisson with a nonlinear operator (analogous to MOND's μ(|∇φ|/a₀)·∇φ structure but sourced by activity). Single mechanism does both jobs (C1 + C2). Most ambitious; potentially affects Theorem N1 and GR.1.

**None of these emerges automatically from ED's existing primitives.** Whether ED's substrate physics can produce a coupling form that gives slope-4 *naturally* — without importing MOND machinery — is the central open structural question. It is not currently within the DM-arc scope.

### 3.2 Foundational ambiguity P1 vs P2 (origin of D_T)

The cluster-anchored D_T and the galactic-anchored κ_act do not numerically satisfy the Einstein-like relation `D_T = c²·κ_act` that BTFR.08 identified as the structural condition for self-consistent log-kernel emergence. Two readings:

- **(P1)** D_T and κ_act are independently calibrated; the relation is not structurally forced. BTFR.06's anisotropy path is the canonical extension.
- **(P2)** A substrate-level derivation of D_T from ED primitives would yield D_T = c²·κ_act automatically; current calibration of κ_act is a relative anchor. Self-consistent ED gives slope-2 BTFR with flat curves "for free."

**Settling P1 vs P2 requires a foundational substrate-physics derivation of D_T that has not been carried out.** This is BTFR.10-candidate work: substrate-level, not galactic-level.

### 3.3 Self-consistent ED as a numerical comparison

The DM2 production run used the linearized PDE (with v_baryon as fixed external input to A). The structurally honest prediction of canonical ED — when v_T is allowed to back-react on A through v_total = √(v_baryon² + v_T²) — is slope-2 BTFR with flat-ish rotation curves. The 0.24 numerical result from DM2 reflects the linearization, not the structure of canonical ED itself.

**This is a bounded engineering task** (modify `_build_activity_source` to include the v_T contribution; re-run on a subset of galaxies) that would sharpen the FAIL verdict from "ED predicts ~0 slope" to "ED predicts ~2 slope." It does not change the qualitative verdict (still FAIL against empirical slope 4), but it would close the DM-arc with a more honest empirical record. **Out of scope for the closed DM-arc; recommended only if a future revival is contemplated.**

### 3.4 Whether ED can derive BTFR without MOND-like machinery

The structural pattern uncovered by BTFR.01–09 is that producing slope-4 BTFR requires a coupling-form whose deep-regime asymptotic gives `μ(a/a₀) → a/a₀`. Every framework that succeeds at BTFR — MOND, emergent gravity, certain scalar-tensor theories — has this structure built in. ED currently does not.

The user's pushback during BTFR.08 (taking the slow-time interpretation seriously, which surfaced the c²-coupling and the relational-structure framing) suggested that ED's foundational c-and-λ scales might naturally produce an a₀-equivalent (c·H_0 ≈ a₀ within factor 6). Whether this can be worked into a *concrete* structural derivation of the coupling form — rather than a dimensional coincidence — is open. **Not a DM-arc task; would be Phase-2 foundational work.**

---

## 4. Roadmap for the next phase

### 4.1 DM-arc tasks: none

The DM-arc is closed. No further DM.x memos are scheduled. Future revival of the arc would require either:

- a new empirical anchor that re-motivates the activity-source mechanism (e.g., a post-DM2 weak-lensing or cluster-outskirts result that activity-source uniquely predicts),
- a structural advance that resolves the C2 problem (substrate-level derivation of slope-4 from ED primitives, or a clean nonlinear-ED reformulation),
- or a reinterpretation that recasts the BTFR mismatch as informative rather than refutational (e.g., the "structure is relational" framing taken to a stronger conclusion: that BTFR's universality is a feature of *which* ED relations the substrate enforces, and ED's mismatch identifies which substrate relations are not enforced in nature).

Absent one of these, the DM-arc remains closed.

### 4.2 Foundational Phase-2 tasks (open, not scheduled)

- **BTFR.10 candidate — substrate derivation of D_T.** Examine whether ED's primitives (event-density discretization, propagation rules, activity coupling) admit a bottom-up derivation of D_T as a macroscopic diffusion coefficient. Output: foundational evidence for or against the Einstein-like relation. Settles P1 vs P2. Estimated scope: substrate-physics arc, similar in flavor to Arc N's V1 derivation.

- **Coupling-form structural derivation.** Examine whether the ED-derived acceleration scale c·H_0 (within factor 6 of MOND's a₀) plays a structural role in any source-coupling derivation. If yes, ED's a₀-equivalent emerges naturally and Route II-A becomes parameter-free. Estimated scope: smaller; could be a single memo if the structural derivation is direct.

- **Nonlinear ED variant (Option C) feasibility study.** Sketch the proposed nonlinear PDE; examine whether Theorems N1 and GR.1 admit nonlinear analogs; estimate whether the nonlinear formulation produces slope-4 BTFR cleanly. Estimated scope: 2–3 memos; substantial, since it touches multiple closed arcs.

These three tasks are forwarded for future consideration. **None is currently scheduled.**

### 4.3 Empirical arc tasks (active, prioritized)

The DM.5 verdict establishes that ED's galactic-disc-dynamics prediction fails. ED's other empirical predictions remain to be tested:

- **Merger-lag retrodiction (active per project_next_predictions).** ED's flagship cluster-scale prediction; tests the D_T anchor independently of any galactic-scale modification. Re-derivation of merger-lag under self-consistent PDE may also be informative.
- **Weak-lensing activity-dependent stacking.** ED's distinctive prediction (from the activity-source mechanism) is that lensing signal should correlate with kinematic activity, not just baryon mass. Independent test of the activity-source idea, decoupled from BTFR.
- **Extended-source / cluster-outskirts environmental tension.** Queued in project_next_predictions.

These tasks are independently motivated and proceed regardless of the DM-arc closure.

### 4.4 Tasks deferred indefinitely

- A full re-run of DM2 with the self-consistent PDE. Engineering-bounded but provides only marginal new information (sharpens the slope-2 vs slope-0.24 distinction without changing the FAIL verdict). Not worth the implementation cost unless a DM-arc revival is contemplated.
- Implementation of any of the BTFR-extension routes (A, B, C from BTFR.07) without the foundational work in §4.2 first. Implementing any extension as a numerical fit, before its structural status is settled, would just produce another fitted-not-derived BTFR — no theoretical advance.

---

## 5. Official closure of the DM arc

### 5.1 What has been completed

- **DM.0–DM.6:** Architectural and protocol memos. Mass-source hypothesis (DM.0) refuted; activity-source hypothesis (DM.1) advanced; SPARC simulation design (DM.2–DM.4); branch-A implementation chosen (DM.6); DM.5 verdict (FAIL with structural diagnosis); DM.6 closure.
- **DM.7–DM.13:** Coding-session implementation memos. Eight Python modules implementing the canonical PDE solver, activity source, boundary conditions, single-galaxy and full-sample runners, and validation suite.
- **DM.14:** Production-run protocol and reproducibility notebook (25 cells, 13 sections).
- **BTFR.01–09:** Sub-arc structural analysis of why canonical ED fails BTFR. Two-condition theorem (BTFR.02); ED viability test (BTFR.03); minimal extensions (BTFR.04–06); parameter accounting (BTFR.07); self-consistency analysis (BTFR.08); foundational check on the Einstein-like relation (BTFR.09).
- **DM.5:** Production-run verdict integrating all of the above.

### 5.2 What remains open but out-of-scope

- C2 (slope-4) structural mechanism. Open, not assigned.
- Foundational substrate derivation of D_T (BTFR.10 candidate). Open, forwarded to Phase-2 candidate work.
- Nonlinear ED variant feasibility. Open, not scheduled.
- Self-consistent re-run of DM2. Bounded engineering task; not scheduled.

### 5.3 Citation guidance for future arcs

When future arcs reference the DM result:

- For the **headline empirical finding** (canonical ED fails BTFR with universality preserved), cite **DM.5 §1.3** (numerical results table) and **DM.5 §3** (verdict).
- For the **structural explanation** (why canonical ED fails BTFR), cite **DM.5 §2** and the **BTFR.01–09** chain.
- For the **damage-containment statement** (which arcs are and are not affected), cite **DM.5 §4** and **DM.6 §2**.
- For the **closure statement** and the **roadmap forward**, cite **DM.6 §4–5**.
- For the **provisional caveat on the universality result** (max_evals = 50 limitation), cite **DM.5 §3.2**.

The DM-arc's complete record is the chain DM.0 → DM.6 + BTFR.01 → BTFR.09 + the engineering memos (DM.7–DM.14) and the run log (`dm2_run_log.json`, `dm5_fill_cheat_sheet.json` in `analysis/outputs/dm2_2026-04-27_b4c809b/`).

---

## 6. Recommended Next Steps

Three concrete next steps for the broader ED program after DM-arc closure:

1. **Pivot to the merger-lag retrodiction (highest priority).** The active prediction queued in `project_next_predictions` is the most informative next test of ED's gravitational-sector predictions. Unlike BTFR (which probed deep-acceleration galactic-disc physics), merger-lag probes the cluster-scale time-domain physics that anchors D_T. A clean retrodiction would either strengthen ED's cluster-scale claim or expose a second empirical mismatch. Either outcome is more informative than further BTFR-extension work.

2. **Spin off the substrate-derivation question (BTFR.10 candidate) as a Phase-2 foundational memo.** Not as an active arc; as a single-memo scoping document that frames the derivation problem and assesses whether ED's primitives can support a bottom-up derivation of D_T. If the assessment is positive, a full derivation arc can be opened later. If the assessment is negative, the P1 reading is locked in and BTFR.06's anisotropy path is the canonical BTFR-extension if BTFR is ever revisited.

3. **Update the program-level orientation document.** The `docs/ED-Orientation.md` and `MEMORY.md` project entries should be updated to reflect the DM.5 + DM.6 closure: the DM-arc is no longer "active" in the working-arcs list; the BTFR-extension routes are open foundational questions; the universality-preserved-but-BTFR-failed pairing is the canonical DM-arc outcome. This is a small documentation task but matters for future-session orientation.

The DM-arc has produced a clean, structurally-explained scientific result. Closure is appropriate. The next phase of ED work proceeds on independent empirical and foundational tasks, with the DM-arc record available as authoritative reference.

Status: complete.
