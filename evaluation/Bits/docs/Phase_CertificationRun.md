# Phase Bits / Certification Run — Build Step 10

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Document:** Build Step 10 — full certification run
**Status:** **CERTIFIED** — all four gates pass together on the MWE; Δ measurement permitted
**Date filed:** June 2026
**Author:** Allen Proxmire
**Code:** `Bits/certify.py`; artifacts in `Bits/certification_output/`
**Related:** `Phase_TestSuite_Implementation.md`; `TestSuite_Results.md`

---

## 1. Purpose

This document performs the **final certification run** of the ED substrate simulator. It executes all four correctness gates **together** on the MWE substrate, consolidates the evidence, and records the verdict.

This is the **acceptance milestone**. The program's standing discipline — *no Δ is measured until all four gates pass* — is discharged here: the gates were defined in advance (Phase A1/A2 criteria, the four-gate plan), the simulator was built to them across Build Steps 1–9, and Build Step 10 runs them as a single consolidated acceptance bar. The simulator is **CERTIFIED**; the run is reproduced below from `certify.py` (exit 0).

---

## 2. Procedure

`certify.py` performs, in one run:

1. **Canonical MWE** — `run_mwe(seed_a=1, seed_b=2)` deterministically; records ρ/orientation history.
2. **Gate 1–3 evidence computed directly** from the run and a fresh factorization ensemble (structural perturbation + 200-run MI).
3. **Full pytest suite** (20 tests) executed as a subprocess; pass/fail parsed.
4. **Consolidation** — all gates ANDed into a single `certified` verdict.
5. **Artifacts written** — `certification_results.json`, `certification_log.txt`, `certification_snapshot.md`.

### Recorded console output

```
================================================================
BUILD STEP 10 - CERTIFICATION RUN
================================================================

  pytest          : 20 passed, 0 failed
  Gate 1 mono     : True
  Gate 2 acyclic  : True
  Gate 3 factor   : True  (MI=-0.001700 nats, exact A<->B True)
  Gate 4 tiebreak : True
  MWE integrity   : two_strata=True, natural_term=True (step 9/200)
  final rho A     : [0.2559, 1.4743, 1.4139, 1.0138, 1.1649, 1.2267, 2.1017, 1.1402]
  final rho B     : [1.1308, 2.046, 0.094, 0.3287, 0.2163, 0.3166, 0.1958, 0.2555]

  artifacts -> certification_output/

================================================================
SIMULATOR: CERTIFIED
Delta measurement is now PERMITTED.
================================================================
```

### Consolidated record

- **Pass/fail summary:** 20 passed, 0 failed (pytest returncode 0).
- **Per-gate:** Gate 1 ✓, Gate 2 ✓, Gate 3 ✓, Gate 4 ✓; MWE integrity ✓.
- **MI values:** MI(A;B) = **−0.001700 nats**; MI(A; shuffled B) = **−0.000699 nats**; tolerance 5e-3.
- **Structural factorization verdict:** A independent of B (exact) = **True**; B independent of A (exact) = **True**.
- **Termination mode:** natural fixed point at **step 9** of max 200; 11 commits.
- **Final ρ_A:** `[0.2559, 1.4743, 1.4139, 1.0138, 1.1649, 1.2267, 2.1017, 1.1402]`
- **Final ρ_B:** `[1.1308, 2.046, 0.094, 0.3287, 0.2163, 0.3166, 0.1958, 0.2555]`

---

## 3. Certification Criteria

All five conditions hold (from the consolidated record):

| Criterion | Requirement | Result |
|---|---|---|
| **Gate 1 — Monotonicity** | all ρ deltas ≥ 0 | **PASS** |
| **Gate 2 — Acyclicity** | all global states unique | **PASS** |
| **Gate 3 — Factorization** | structural exactness **and** MI ≈ 0 | **PASS** (exact A↔B; \|MI\| = 1.7e-3 < 5e-3) |
| **Gate 4 — Tie-break** | deterministic, orientation-blind | **PASS** |
| **MWE integrity** | strata, boundary, natural termination, round-trip | **PASS** |

Gate 3 is the load-bearing one and is satisfied two independent ways: **exact** (perturbing either stratum's seed leaves the other byte-identical) and **informational** (across-boundary MI indistinguishable from zero and from its shuffle control). The determinability boundary verifiably severs reciprocal participation.

---

## 4. Output Artifacts

Written to `Bits/certification_output/`:

- **`certification_results.json`** — machine-readable summary: `certified: true`, per-gate booleans, factorization evidence (exact flags + MI values), MWE integrity (strata, bridge `[7,8]`, steps_run 9, commits 11), final ρ_A/ρ_B, seeds. (Committed as the canonical certification record.)
- **`certification_log.txt`** — full pytest `-v` output (20 PASSED). (Gitignored as a regenerable log.)
- **`certification_snapshot.md`** — human-readable one-page summary with the gate table and factorization evidence. (Committed.)

The run is deterministic: re-running `certify.py` reproduces the same verdict, MI values, and final ρ (randomness lives only in the seeded initial conditions; the dynamics are deterministic).

---

## 5. Final Verdict

> ## SIMULATOR CERTIFIED
>
> All four correctness gates pass together on the MWE substrate (20/20 tests, exit 0). The ED substrate simulator is a **faithful, verified executable transcription** of the closed ED-substrate specification: discrete Σ-maximization with a deterministic tie-break (never averaging), monotone and irreversible (Gate 1), acyclic (Gate 2), reach-factorized across the determinability boundary (Gate 3), and uniquely-determined at ties (Gate 4).
>
> **Δ measurement is now PERMITTED.**

The discipline that governed the entire empirical arc is discharged: the gates were fixed before the simulator was built, the circularity guard was never touched, and only now — with every gate green on a substrate that exhibits two causally independent strata separated by a determinability boundary — does the program proceed to a measured number.

---

## 6. Deliverables

Produced and verified:

- **`Bits/Phase_CertificationRun.md`** — this document.
- **`Bits/certify.py`** — the certification harness (reproducible, exit 0).
- **`Bits/certification_output/certification_results.json`** — machine-readable gate summary (committed).
- **`Bits/certification_output/certification_log.txt`** — pytest output (gitignored).
- **`Bits/certification_output/certification_snapshot.md`** — human-readable summary (committed).

---

## 7. Next Actions — Δ Measurement Opens

With certification complete, the empirical arc proceeds to its purpose: **Δ = predictability_within_stratum − predictability_across_boundary**, in bits.

The remaining build is the analysis layer:

- **`analysis/delta.py`** — assemble M1/M2/M3 (the measurement plan's measures) into Δ: the within-stratum predictability baseline minus the across-boundary predictability, over an ensemble, with the matched-separation design that differences out estimator artifacts.
- **Δ estimate** — a central value with spread (and, if it varies, as a function of reach profile), reported with the robustness analysis.
- **FS comparison** — place ED's Δ beside FS's escape density, role-to-role, structural-analogy-only.

`analysis/entropy.py` (the Miller-Madow MI kernel, already built and exercised by Gate 3) is the first component of this layer. The simulator is certified; the boundary is real and severs cleanly; the measurement the whole arc was built to produce can now begin.

---

*End of Certification Run. The ED substrate simulator is CERTIFIED: all four gates pass together on the MWE, 20/20 tests, exit 0. Δ measurement is permitted. The empirical arc proceeds to assemble the determinability-boundary bits measure.*
