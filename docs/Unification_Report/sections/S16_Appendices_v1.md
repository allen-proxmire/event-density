# Appendices

*Draft v1, 2026-07-10. The reference layer of the report: every claim traces to a paper (Appendix A), every open and wall to a ledger line (Appendix B), every measured result to a runnable simulation (Appendix C). This is the audit trail that makes the report verification-grade — a reader can follow any ✅ to its proof and any ⚠️ to its honest status.*

---

## Appendix A — Paper index by box

Each box of the report is delivered by one or more corpus papers. The cold-reader papers (in `physics-papers/`, ED-Generative repo) are the primary citations — the ones a physicist would open. Where a result is newer than its published paper, the working note carrying it (in `event-density/foundations/` or `/theory/`) is named and flagged.

| § | Box | Authoritative paper(s) | Location |
|---|---|---|---|
| §3 | The arrow / minimal foundation | *Commitment and Participation (Minimal Ontology)*; *The Arrow Sorts the Continuum*; the position paper (`Paper_087_13Primitives`) | `physics-papers/substrate-evaluation/`; `physics-papers/foundations/` (Paper_087) |
| §4 | Quantum mechanics | *The Quantum-Logic Keystone (Gleason Reconstruction)*; Paper_004 (the postulated inner product it reconstructs); Paper_001 (ℂ-amplitude) | `physics-papers/substrate-evaluation/`, `physics-papers/qm-kinematics/` |
| §5 | Gravity (GR + DM + DE) | *GR-I..IV*; *KM-I/II*; *One Field (letter)*; Papers 025–038 (G, a₀, combination rule, BTFR, MOND field eqn, Λ). λ-bound: working note `Khronometric_Lambda_HealthyBranch_FromStandingKeystone` | `physics-papers/gravity/`; `event-density/foundations/` (λ note) |
| §6 | QM + gravity unified | *Commitment and Participation* §8 (the keystone synthesis + its "account, not theorem" guard) | `physics-papers/substrate-evaluation/` |
| §7 | Gauge structure | *The Gauge Structure of ED (SU(N), F², mass gap, single hypercharge)* | `physics-papers/substrate-evaluation/` |
| §8 | Charge + electromagnetism | *The Topological Skeleton of Charge (B4)*; *Maxwell as an Emergent Shadow*; *The Continuum: a Kinetic Lattice-Gas* | `physics-papers/substrate-evaluation/` |
| §9 | Chirality / parity | *The Clean Substrate Is Vector* (supersedes *The Parity Wall* on the verdict's tier) | `physics-papers/substrate-evaluation/` |
| §10 | Matter (spinor + mass) | *Mass Without Mass (Binding Inertia)*; Paper_106 (the Dirac equation); working note `T4_14_Closure_SubstrateToDirac` (form-completeness + undoubling) | `physics-papers/substrate-evaluation/`, `physics-papers/relativistic-qm/`; `event-density/foundations/` (T4 note) |
| §11 | The constants | *Common Cause, Not Channel (A1)* (the zero-scalar result); working notes `SCBU_SubstrateEvaluation_Bridge`, `Scoping_ThetaED_FirstPrinciples` | `physics-papers/substrate-evaluation/`; `event-density/foundations/`, `/docs/` |
| §12 | Anomalies | working note `Anomaly_State_After_CleanVectorTheorem_2026-07-10`; *B4* (conservation face); *Clean Substrate Is Vector* §6 (baseline) | `event-density/theory/Anomaly_Cancellation/`; `physics-papers/substrate-evaluation/` |
| §13 | The walls | *Template, Not Escape (Primes)* (the one proven wall); *A1*; gauge paper §7 (#1); ontology paper §6 (dimension); clean-vector §5 (casting) | `physics-papers/substrate-evaluation/` |
| §14 | Falsifier frontier | *Paper_101 — Falsification Register and Prediction Inventory* §0 (weapons-first, 2026-07-10); `ED_Master_Predictions_List` | `physics-papers/predictions/`; `event-density/docs/` |

*Navigation aids in the EDG repo: `PAPERS_INDEX.md` (the full corpus index) and each folder's `README.md` (per-arc tiering). The authoritative open/closed map is `event-density/docs/ED_Research_Targets.md`.*

---

## Appendix B — Provenance and honesty ledger

The report's honesty tiers are not set by each paper's own framing; they are set against the research map. This is the condensed ledger — the full audit trail (with dated updates) is `event-density/docs/ED_Open_Derivations_Ledger.md` and `ED_Research_Targets.md`.

**The five derivations tracked this session, at close:**

| # | Derivation | Status at close |
|---|---|---|
| 1 | Channel-topology → representation spectrum | **Open (tooling-walled).** Reduces to "why internal-d = 3"; ED's stability route refuted; the one lead (3D-linking bridge) needs a published linkless-embedding algorithm. Delegatable; unsolved in the SM too. |
| 2 | Mass / electroweak / Higgs | **Honest-closed.** Native binding-mass mechanism (measured, V5-conditional); k₁₁ separated as time-dilation, not mass; fundamental Higgs inherited. |
| 3 | Anomaly-freedom as a forced constraint | **Structural candidate, gated.** Conservation + clean-vector baseline solid; the "forced" claim retracted; nontrivial chiral cancellation inherited; one candidate gated on substrate→Dirac. |
| 4 | DCGT → Maxwell | **Done.** Coherence-weighted limit = Coulomb (computed); smooth field an emergent shadow. |
| 5 | Exact khronometric λ | **Done (bound) / inherited (value).** Healthy branch λ<1/3, λ≠1 derived; exact λ inherited. |

**The map of "no" (from §13):**
- **Proven wall (1):** primality — theorem-anchored (Möbius orthogonality + parity barrier), the finite-memory ceiling.
- **Structural opens (2):** #1 (rep-spectrum, delegatable tooling task) and #3 (anomaly, gated on substrate→Dirac) — one deep arc plus one tooling task.
- **Principled inheritances:** dimension (selected, conditional linking route home); casting (SU(2) pseudoreality).
- **Inherited-by-design:** the constants (no intrinsic scalar; A1).

**Confirmation status:** one confirmed forward prediction (the Universal Degenerate-Mobility law, peer-reviewed); `c_GW = c` survived (consilience); **no distinctive, argument-ending weapon confirmed** — the honest ceiling.

---

## Appendix C — The certified simulations

The "measured" tier means a result was produced by a built-and-run simulation of the certified substrate (or, for the analytic probes, a direct computation of the stated quantity). These are the runnable artifacts behind the report's measured claims; paths are in the ED-Generative and event-density repos.

| Result (§) | Script | What it runs |
|---|---|---|
| Charge skeleton, integral Gauss law (§8) | `holonomy_test.py`, `coupling_test.py`, `sourcing_test.py`, `relaxation_test.py` | B4: winding quantization to ℤ; `w`-indexed bandwidth ladder; circulation = 2πw loop-independent; the ontology fork (`1/r²` only off-ED) — `evaluation/B4_Arc/` |
| Maxwell shadow (§8) | `maxwell_from_coherence_probe.py` | FFT Poisson solve of the coherence-action minimizer around a point charge; p=1 (3D Coulomb) fit R²=0.97 — `evaluation/B4_Arc/` |
| QM orthogonality + covering law (§4) | `move1_operational_orthogonality.py`, `gleason_nonboolean_probe.py` | perfect distinguishability ⟺ orthogonality (`1−c²`); the non-Boolean complementarity gate — `evaluation/ChiralGauge/` |
| Chirality: clean-vector theorem (§9) | `rep_spectrum_casting_winding.py` | parity-clean point-gap winding = 0 for N=1..6 (control on the theorem); broken-case winding = N — `evaluation/ChiralGauge/` |
| Spinor undoubling (§10) | `chiral_3p1d.py` | Nielsen–Ninomiya: Hermitian naive = 16 doublers, arrow (Wilson term) = 1 survivor at the origin — `evaluation/ChiralGauge/` |
| Binding mass + inertia (§10) | `mass_from_binding_probe.py` | free front v=0.98; unbound vs V5-confined (extent 55 vs 1.4–2.3); COM sub-luminal; inertia 0.72 vs unbound-control 0.97; the k₁₁ time-dilation discriminator — `theory/Higgs_Emergence/` |
| Khronon dynamical rule (§5) | GR-III simulation (`ḃ = D∇²b − κρ`) | Newtonian fixed point; r_s ∝ M; frozen b→0 horizon + area law; khronon speed c_s = c — gravity arc |
| Channel capacity = 0 (§8, §11, §13) | A1 channel-capacity probe | controlled capacity exactly zero (the internal reading of the finite-reach ceiling) |
| Finite-memory ceiling (§13) | `primes_test.py` | sieve to N=5×10⁶: template reproduced (1.700-bit invariant, lpf ladder); escape blocked (optimal Möbius correlator → 0; twin density needs 2C₂) — `evaluation/Primes_Arc/` |

*Verification status (2026-07-10): every script path above was confirmed present. Four were re-run this session and reproduce their cited numbers exactly — `rep_spectrum_casting_winding.py` (clean winding 0 ∀N, broken = N), `chiral_3p1d.py` (16 doublers → 1 survivor at the origin), `maxwell_from_coherence_probe.py` (p=1 3D-Coulomb, R²=0.97), and `mass_from_binding_probe.py` (inertia 0.72 vs unbound-control 0.97). The remainder (the B4 holonomy suite, `move1`/`gleason`, GR-III, A1, `primes_test.py`) are path-verified with numbers as last run in their source papers; re-run before publication for a clean provenance stamp.*

*Honest scope note: the gauge sector's non-abelian action and mass-gap (§7) are analytic (gauge-program tier), not certified-simulator runs — only the abelian/Maxwell case is simulator-grounded. The chirality theorem's winding computation is a control on a proof, not an independent measurement. Both are flagged as such in their sections.*

---

*Draft notes for finalization:*
- *Verify every paper title and repo path against `PAPERS_INDEX.md` before locking — some cold-reader papers use house short-titles; use the exact filenames a reader will search for.*
- *Appendix B is deliberately condensed; keep it a pointer to the full ledger, not a copy (the full ledger has the dated audit trail and must stay the single source of truth).*
- *Appendix C: confirm each script path exists and the cited numbers match the current script output before publication (the mass and Maxwell probes were re-run this session; re-verify the others or mark them "as last run").*
- *If the report is published from the EDG repo, prefer physics-papers/ citations over event-density/ working-note citations wherever a published paper carries the result; name the working note only where the result is genuinely newer than any paper (λ-bound, T4_14, the anomaly state note).*
