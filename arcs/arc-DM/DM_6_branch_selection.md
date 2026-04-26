# DM.6 — Branch Selection

**Date:** 2026-04-25
**Arc:** Dark Matter (DM) — seventh memo
**Status:** Branch selected. Implementation phase begins.
**Predecessor:** DM.5-TEMPLATE (verdict scaffold awaiting real data).
**Successor:** First coding session per §4 below; subsequent execution sessions; eventual DM.5.
**Premise:** the arc has progressed through derivation (DM.0), structural rescue (DM.1), simulation design (DM.2), implementation plan (DM.3), execution protocol (DM.4), and verdict template (DM.5-TEMPLATE). Real data does not yet exist. The arc cannot advance to a real DM.5 verdict by writing more planning memos. It can only advance through engineering work.

---

## 1. The three available branches

Given the current arc state, three structurally distinct paths are open.

### Branch A — Implementation and execution

Begin building the eight Python modules in `ed-lab/simulations/edsim/dm/` per DM.3, run them through DM.4's gate sequence, fill in DM.5-TEMPLATE with real numbers, and return a real verdict. Multi-session coding work. Concrete outputs at each step.

### Branch B — Pause

Leave DM.5-TEMPLATE as the terminal state of the arc until a future session resumes it. The five planning memos (DM.0–DM.4) and the template (DM.5) sit committed on disk; the arc is dormant but recoverable.

### Branch C — Reopen the theoretical architecture

Set DM.5-TEMPLATE aside and explore the V₁ + acoustic-metric channel as an alternative galactic-scale mechanism. This was named as the FAIL-branch destination in DM.4 §7.4 — the move appropriate *if* DM.5 returns FAIL. Pursuing it now means treating the V₁ channel as worth scoping before the activity-source mechanism has been empirically tested.

---

## 2. Evaluation of each branch

### 2.1 Branch A

**For.**
- DM.0–DM.4 represent ~40 pages of planning work whose value is realized only by execution.
- DM.1's structural argument is unusually clean: the activity-source PDE produces flat curves under Reading B with the natural dimensional scale matching MOND's a₀ to factor of one. This is too crisp to abandon without empirical confrontation.
- The framework's verdict ledger is the artifact that grounds its credibility. Writing a real DM.5 with real numbers — pass, partial, or fail — directly serves that discipline. Writing more planning memos does not.
- The compute envelope is small: ~50 hours single-CPU, ~3 days implementation effort. Bounded, achievable on a laptop.
- The four-way verdict architecture in DM.4 means the run produces information in every outcome. There is no "wasted run" — even a FAIL is a finding that constrains what the framework can claim.

**Against.**
- Multi-session work. No single coding session can produce a complete DM.5; the eight modules and validation sequence span several days minimum.
- Risk of partial completion: the work is staged, and if it stalls partway, the arc sits in an awkward intermediate state.
- The implementation work is not reversible in the sense that effort spent here is not effort spent on outreach, website, or other arcs.

### 2.2 Branch B

**For.**
- The arc is in a clean state. DM.0–DM.4 are coherent; DM.5-TEMPLATE waits patiently. Pausing is recoverable at any future date.
- Allows attention to the website pages, outreach, NotebookLM materials, and other parallel program work that is currently in-flight.
- No compute or coding effort required.

**Against.**
- The structural argument is unfinished. DM.1's positive verdict is structural plausibility, not empirical confirmation. Without DM.5, the arc has not produced a real result.
- Indefinite pauses tend to become permanent. The arc accumulates context-rot the longer it sits.
- The verdict ledger gains nothing. The program's empirical record stands at three confirmed (universal mobility, cluster merger-lag, structural QM recovery) and three inconclusive (Eibenberger, Fein, weak-lensing activity). DM.5 either adds a fourth confirmed or a fourth inconclusive (or a refuted) — meaningful in any case, absent if paused.

### 2.3 Branch C

**For.**
- The V₁ vacuum kernel (Theorem N1 / T8) is one of the framework's nine forced theorems. Connecting it to galactic dynamics through the curved-spacetime extension (Theorem GR1 / T9) and the acoustic metric (ED-Phys-10) is a structurally clean move that has not yet been attempted.
- If the activity-source mechanism eventually fails, the V₁ channel is the natural alternative; scoping it now would have it ready.

**Against.**
- DM.4 §7.5 was explicit: "Branching to V₁ + acoustic-metric channel is the right move only if DM.5 returns FAIL after validation passes and NGC 3198 / 30-galaxy gates clear cleanly. Speculative branching before the test is premature."
- The activity-source argument is not refuted. Pursuing an alternative without testing the standing hypothesis is the speculation pattern the program is built to avoid.
- It would mean writing more planning memos (DM-V1.0, DM-V1.1, …) rather than producing real data. The arc would gain depth without gaining empirical weight.

---

## 3. Selection — Branch A

**The arc proceeds with Branch A — implementation and execution.**

The reasons, in order of weight:

1. **The discipline demands it.** Five planning memos cannot substitute for one real run. The framework's core commitment is checkability; checkability requires the check to actually happen.
2. **The structural argument is too clean to leave untested.** DM.1's flat-curve emergence and dimensional-scale match are crisp. Either the math is right and the run will return PASS or PARTIAL, or it isn't and the run will return FAIL with a specific failure mode that tells us what's missing. Both outcomes are genuinely informative.
3. **The cost is bounded.** ~3 days implementation, ~50 hours compute on a laptop. No HPC, no specialized hardware, no novel dependencies. The cost is real but tractable.
4. **The risk profile is symmetric in usefulness.** PASS confirms a major program claim. PARTIAL identifies a structural gap precisely. FAIL constrains the framework honestly and unblocks Branch C as the appropriate next move — but only after the test has been run.

Branches B and C are not selected for the reasons above. Branch B is recoverable but unproductive. Branch C is premature and contradicts the discipline DM.4 §7.5 explicitly committed to.

---

## 4. First implementation session

### 4.1 Scope

The first coding session implements **DM.4 Step 1** in full: `ed-lab/simulations/edsim/dm/disk_geometry.py` with unit tests.

This is the single best first session because:

- It is the most upstream module — every other module depends on it directly or indirectly.
- It is the cleanest module to implement: pure functions, no PDE solver, no iteration, no parameter fitting.
- It has well-known analytic comparison cases (exponential disk Bessel-function potential), so unit tests are straightforward and decisive.
- Completing it produces the foundation for Step 2 (`activity_source.py`) to be implemented in the next session.

### 4.2 Functions to implement

Per DM.3 §1.1.3:

#### `baryonic_velocity(R, v_gas, v_disk, v_bulge) -> np.ndarray`

- **Input:** four 1-D numpy arrays of equal length: R (kpc), v_gas (km/s), v_disk (km/s), v_bulge (km/s).
- **Output:** v_bar = √(v_gas² + v_disk² + v_bulge²) in km/s.
- **Edge cases:** handle missing bulge (zeros), handle NaN entries (propagate), handle empty arrays.

#### `baryonic_potential_inplane(R, v_bar) -> np.ndarray`

- **Input:** R (kpc), v_bar (km/s).
- **Output:** Φ_bar(R) (km²/s²), computed as cumulative integral of v²_bar / R from R_min outward.
- **Method:** trapezoidal integration. The constant of integration is fixed by Φ_bar(R_max) = 0 convention (or equivalently, output Φ relative to outermost point).

#### `exponential_disk_potential(R_grid, z_grid, M_disk, R_d) -> np.ndarray`

- **Input:** 1-D arrays R_grid (kpc), z_grid (kpc); scalars M_disk (M☉), R_d (kpc).
- **Output:** 2-D array Φ_disk(R, z) in km²/s² for an exponential thin disk.
- **Method:** standard Bessel-function form (Binney & Tremaine §2.6.1):

  Φ_disk(R, z) = −π G Σ_0 R_d ∫₀^∞ J_0(k R) [1 − k R_d / (1 + (k R_d)²)^(3/2)] e^(−k|z|) (1 + (k R_d)²)^(−3/2) dk,

  with Σ_0 = M_disk / (2π R_d²). Implement via `scipy.integrate.quad` over k for each (R, z) point. Caching across calls is optional; profile first.

#### `baryonic_potential_grid(R_grid, z_grid, R_sparc, v_bar_sparc, R_d_fit=None) -> np.ndarray`

- **Input:** simulation grid arrays + SPARC R, v_bar arrays. Optional pre-fit R_d.
- **Output:** 2-D Φ_bar(R, z) on the simulation grid.
- **Method:** if R_d_fit is provided, use the analytic exponential-disk form. Otherwise, fit R_d to the SPARC v_disk profile (separate utility). Add gas and bulge contributions: gas as a thin-disk approximation with its own R_d_gas; bulge as a Plummer or Hernquist potential.

For the first session, the bulge contribution may be deferred to a follow-up commit and replaced by `bulge_contribution = 0` with a TODO comment.

### 4.3 Unit tests

Tests live in `ed-lab/simulations/edsim/dm/tests/test_disk_geometry.py`.

#### Test 1 — Quadrature sum

- Input: synthetic v_gas = [10, 20, 30], v_disk = [40, 30, 20], v_bulge = [0, 10, 20].
- Expected v_bar = [√(100 + 1600 + 0), √(400 + 900 + 100), √(900 + 400 + 400)] = [41.23, 37.42, 41.23].
- Tolerance: 10⁻⁶ km/s relative.

#### Test 2 — In-plane potential of constant rotation curve

- Input: R = [1, 2, 5, 10, 20] kpc, v_bar = [100, 100, 100, 100, 100] km/s (constant).
- Expected: Φ_bar(R) = 100² · ln(R) + const, monotonically increasing.
- Tolerance: 1% on the slope.

#### Test 3 — Exponential disk potential at z = 0

- Input: M_disk = 5×10¹⁰ M☉, R_d = 3 kpc; evaluate at R = [0.1, 1, 3, 10, 30] kpc, z = 0.
- Expected: known analytic values (computed from Binney & Tremaine §2.6.1 reference table or independent integration).
- Tolerance: 1%.

#### Test 4 — Exponential disk potential at z ≠ 0

- Input: same disk; evaluate at R = 5 kpc, z = [0, 0.5, 1, 2, 5] kpc.
- Expected: Φ decreases monotonically with |z| (more negative away from plane).
- Tolerance: monotonicity check, no quantitative tolerance for first session.

#### Test 5 — Asymptotic Keplerian falloff

- Input: same disk; evaluate at R = [50, 100, 200, 500] kpc.
- Expected: Φ_disk(R) → −G M_disk / R for R ≫ R_d.
- Tolerance: 5% at R = 100 kpc, 1% at R = 500 kpc.

### 4.4 Session-complete criteria

The session is complete when all of the following hold:

- [ ] `disk_geometry.py` exists with the four functions above implemented.
- [ ] `tests/test_disk_geometry.py` exists with the five tests above.
- [ ] All five tests pass on the local machine.
- [ ] The module imports cleanly; no syntax errors, no missing dependencies.
- [ ] Docstrings document the inputs, outputs, units, and any external references for each function.
- [ ] A single-line entry has been added to the arc's running log: `2026-MM-DD: disk_geometry.py implemented and tested. Step 1 of DM.4 complete.`

### 4.5 What not to do in this session

- **Do not** implement other modules. Resist the pull to write `activity_source.py` "while in the file." The Step 1 → Step 2 boundary exists for a reason: it gates the next session on a clean foundation.
- **Do not** run the full validation suite (Tests 1–3 of DM.4 §2). That requires `pde_solver.py`, which is Step 3.
- **Do not** download or preprocess the SPARC tables. That is a Step-1.5 utility (a one-time data-ingestion step) and can be done in parallel with Step 2 in the next session.
- **Do not** start the notebook. The notebook is a downstream artifact and depends on all eight modules being implemented.

### 4.6 Estimated session time

3–5 hours of focused implementation work. This includes:

- Writing the four functions (~2 hours).
- Writing the five unit tests (~1 hour).
- Debugging and tolerance-tuning (~1 hour).
- Documentation and commit (~30 minutes).

If the session exceeds 6 hours, something is structurally wrong. Likely candidates: SPARC table format more complex than expected (unlikely for this module since SPARC data is not loaded yet); `scipy.integrate.quad` behaving unexpectedly on the Bessel integral (possible — fall back to a tabulated reference if so); or scope creep into Step 2 territory.

---

## 5. Expectations for the coding phase

### 5.1 Time budget

Total implementation effort across all eight modules and three analysis scripts: ~3 days of focused coding, distributed across however many sessions are available. Per DM.3 §5.4 and DM.4 §6.2:

| Phase | Effort | Cumulative |
|---|---|---|
| Step 1 — disk_geometry | 3–5 hr | 3–5 hr |
| Step 2 — activity_source | 2–3 hr | 5–8 hr |
| Step 3 — pde_solver | 6–10 hr | 11–18 hr |
| Step 4 — boundary_conditions | 2–4 hr | 13–22 hr |
| Step 5 — validation_tests | 2–3 hr | 15–25 hr |
| Step 6 — run_single_galaxy | 3–5 hr | 18–30 hr |
| Step 7 — fit_activity_parameters | 2–3 hr | 20–33 hr |
| Step 8 — run_full_sample | 1–2 hr | 21–35 hr |
| Analysis scripts (3 files) | 4–6 hr | 25–41 hr |
| Notebook | 2–3 hr | 27–44 hr |
| **Total implementation** | **~30–45 hr** | |

Plus compute time:
- Validation suite: minutes.
- NGC 3198 proof of concept: 1–8 minutes.
- 30-galaxy fit (with optimization): 30–50 hours single-CPU.
- Full-sample run: 7–8 hours single-CPU; 1 hour parallelized 8-core.

**Total wall time from "start coding" to "real DM.5 verdict": 2–4 weeks**, depending on coding cadence and whether parallelization is set up.

### 5.2 Risks

The DM.3 §6 risk inventory remains active. Most likely-to-bite, ordered:

1. **Tier 3 outer-loop convergence on a subset of galaxies.** Mitigation already specified (damping, fall back to Tier 2).
2. **SPARC data ingestion overhead.** SPARC tables may need bespoke parsing if not already in `ed-lab/data/`. One-time cost, ~2 hours.
3. **Solver instability at small R.** Pole regularization is in place but may need tightening.
4. **Bessel-function integration in `disk_geometry.py`.** Convergence of `scipy.integrate.quad` on the disk-potential integral is occasionally flaky. Tabulated reference fallback exists.
5. **Multigrid migration.** If SOR is too slow for the 30-galaxy fit (estimated ~50 hours of optimization runs), implement multigrid via PyAMG. ~4 hours of additional work.

### 5.3 Checkpoints

After each step in the implementation order:

- **Step 1 complete → Step 2 begins.** Required: §4.4 criteria met.
- **Step 5 complete → Validation gate runs.** Required: all five preceding modules pass unit tests; production-grid validation suite executes and Tests 1, 2, 3 each pass at the DM.4 §2 tolerances.
- **Validation gate clears → NGC 3198 runs.** No exceptions.
- **NGC 3198 passes → Step 7 (`fit_activity_parameters.py`) begins.**
- **30-galaxy fit clears → full-sample run.**
- **Full-sample run complete → DM.5 written from template.**

Each checkpoint is a natural commit point. The repo HEAD at each checkpoint should be a coherent state that can be re-run by an independent operator.

### 5.4 When DM.5 (real) will be ready

Optimistically: **2 weeks** from session start, assuming 3–4 coding sessions of 3–5 hours each, plus an overnight full-sample run.

Realistically: **3–4 weeks**, accounting for unanticipated debugging, SPARC ingestion overhead, solver-tuning iterations, and the inevitable surprises that surface during actual implementation.

### 5.5 What does not change during the coding phase

The structural argument from DM.0–DM.1 does not change. The simulation design from DM.2 does not change. The implementation plan from DM.3 does not change. The execution protocol from DM.4 does not change. The verdict template from DM.5-TEMPLATE does not change.

If during implementation a structural decision is found to require revision, that revision is recorded as a DM.X-AMENDMENT memo, not as a silent change to the plan. The discipline of pre-registration extends to the simulation design itself: the design is committed before the run, and any modification is dated, justified, and visible.

---

## 6. Parallel-session considerations

The coding phase is implementation-bounded, not research-bounded. While it proceeds, other arcs and program activities are not blocked:

- Website page revisions (Forced Theorems, Predictions, Ledger, Refutation, Changelog, For Physicists, For Everyone Else, Papers, DIY) — these are independent of DM execution.
- NotebookLM audio overview generation — independent.
- Outreach work — independent.
- Ongoing retrodictions in other channels (FRAP-High-BSA at Creative Proteomics; AFM-dewetting; matter-wave distinguishing-signature analysis on Eibenberger / Fein archival data) — independent.

If session attention is constrained, prioritizing one of these alongside DM.6 implementation is reasonable. The DM arc does not demand exclusive attention; it demands consistent forward progress.

---

## Recommended Next Step

**Begin implementation of `ed-lab/simulations/edsim/dm/disk_geometry.py` in the next coding session.**

Concretely:

1. Create the directory `ed-lab/simulations/edsim/dm/` with an empty `__init__.py`.
2. Create `ed-lab/simulations/edsim/dm/disk_geometry.py`.
3. Implement the four functions per §4.2.
4. Create `ed-lab/simulations/edsim/dm/tests/test_disk_geometry.py`.
5. Implement the five unit tests per §4.3.
6. Run the test suite. Verify all five pass.
7. Commit with message: `Add disk_geometry.py and tests — DM Step 1 complete`.
8. Add a one-line entry to `ed-lab/arcs/arc-DM/run_log.md` (or create the file if it does not exist): `2026-MM-DD: Step 1 complete. disk_geometry.py implemented and tested.`

After the commit lands, Step 2 is unblocked. The next session implements `activity_source.py` per DM.3 §1.1.2.

The alternative branches (B — pause; C — V₁ channel) are explicitly not selected. If circumstances force a pause, DM.5-TEMPLATE remains the terminal state and the arc resumes from this DM.6 memo when work resumes. If DM.5 eventually returns FAIL, Branch C activates per DM.4 §7.4. Neither alternative is the right move now.

---

## End-of-turn summary

**What got done this turn:** the branch decision is committed. The arc's path forward is implementation. The first coding session is fully scoped — module, functions, tests, completion criteria, anti-scope-creep guardrails, time estimate.

**What did not get done:** any code. The DM.6 memo is a planning document; it commits the program to engineering work but does not perform that work.

**What this means for the program:** the arc is now blocked on engineering, not on planning. Five planning memos and a verdict template stand in front of the work; the next move is to start writing Python.

**Decision:** Branch A. Begin `disk_geometry.py` next session.

**When DM.5 will be real:** 2–4 weeks after coding starts, depending on cadence and unanticipated complications.
