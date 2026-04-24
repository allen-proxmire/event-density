# Jin 1997 Retrodiction — Parking Memo

**Date:** 2026-04-24
**Location:** `quantum/retrodictions/jin1997_todo.md`
**Status:** **Phase-2: paused with a loaded test.** The BEC platform-bridge and retrodiction scaffolding are complete; only literature retrieval and arithmetic remain before a verdict can be produced.
**Purpose:** Capture the BEC-bridge state cleanly before pivoting to QM Step 1, so that returning to this work in a future session requires no rediscovery of the setup.

---

## 1. Ready (the loaded side of the test)

### 1.1 Theory chain complete

- **ρ ↔ n** — **FORCED** via Madelung anchoring (Dimensional Atlas quantum regime).
- **v ↔ φ** — CANDIDATE (phase field chosen; alternatives noted).
- **τ ↔ 1/ω_m** — CANDIDATE (regime-specific anchoring).
- **y_m = ε_m · τ = 1** — CANDIDATE (forced at collective-mode scale).
- **D = 0** — CANDIDATE (pure participation channel at BEC collective-mode scale).
- **ζ = 1/Q_m** — CANDIDATE (derived from ED discriminant + collective-mode matching).

Derivation in [`quantum/effective_theory/bec_pde_mapping.md`](../effective_theory/bec_pde_mapping.md).

### 1.2 Three blockers resolved

- **Q-formula inconsistency:** resolved via τ_ED_base = 1/ω_m anchoring, which forces y_m = 1 and D = 0.
- **Typical Q-range mismatch:** resolved — ED target Q ≈ 3.5 corresponds to high-T/T_c regime (T/T_c ≈ 0.93–0.95) accessible in Jin 1997.
- **Non-homogeneous n_eq:** resolved via mode-by-mode linearization on Thomas-Fermi profile; standard Stringari modes become ED eigenfunctions.

### 1.3 Prediction in hand

At T* where Q(T*) ≈ 3.5:
- **N_osc_predicted ∈ [7, 16]** (depending on SNR; consistent with ED-Phys-17 §4.1 range [8, 19]).
- **Decay envelope:** damped-exponential sinusoid structure.
- **Mode:** m = 0 breathing or m = 2 quadrupole.

---

## 2. Missing (the unloaded side)

- **Jin 1997 PDF** — not in session.
- **Specific Q(T) numerical values** — pending PDF.
- **Time-resolved ring-down trace at T*** — structurally uncertain whether Jin 1997 Fig. 1 contains such a trace or only frequency-domain data.
- **N_osc_measured** — cannot be counted without a visible time-resolved trace.

---

## 3. What to do when we return

### Step A — Retrieval

1. Obtain Jin, Matthews, Ensher, Wieman, Cornell (1997), *PRL* 78, 764. arXiv or JILA preprint server likely has it.

### Step B — Extraction

2. From Fig. 2 (or equivalent): extract Q(T) curve for m=0 breathing mode (and m=2 quadrupole if shown).
3. Identify **T\* where Q(T\*) ≈ 3.5**. Interpolate or extrapolate from published points if needed.
4. Check whether a time-resolved trace is shown at T near T* (Fig. 1 likely candidate).

### Step C — Comparison

5. **If trace exists:** digitize, count visible oscillation peaks above noise floor, report N_osc_measured.
6. **If no trace at T*:** use reported ω_m, γ_m at T* plus SNR estimate to **infer** expected N_osc; flag as indirect rather than direct comparison.
7. **If paper reports only Q(T) scatter without time traces at all:** pivot to fallback dataset.

### Step D — Verdict

8. Compare N_osc_measured (or inferred) to [7, 16] range.
9. Classify as: strong match / partial match / no match / not testable.
10. Output: `quantum/retrodictions/jin1997_verdict.md` (currently scaffolded; execute the comparison template in §3 of that memo).

### Step E — If Jin 1997 insufficient

Fallback datasets (per [`jin1997_verdict.md §6`](jin1997_verdict.md)):
- **Meppelink et al. 2009** *PRA* 80, 043605 — explicit time-resolved hydrodynamic-regime traces.
- **Stamper-Kurn et al. 1998** *PRL* 81, 500 — MIT Na-23 BEC.
- **Chevy, Madison, Dalibard 2000** *PRL* 85, 2223 — scissors mode.
- **Tung et al. 2010** *PRL* 105, 230408.

Each would require a small amendment to the BEC bridge memo (different trap parameters) but the structural mapping carries over.

---

## 4. Distinguishing-content gap (flagged, not blocking the Q-match)

Even if Q and N_osc both match, this is a **consistency check**, not distinguishing. Standard Landau-damping theory (Giorgini, Szépfalusy-Kondor) predicts the same Q(T). A distinguishing test requires additional work:

- Derive envelope-shape deviations specific to ED's D = 0 pure-participation regime.
- Check for 2nd-harmonic (ED-Phys-16 §7.2, 3–6%) content in the ring-down density profile.
- Compare breathing vs. quadrupole mode Q-values for mode-independent signatures.

This work is flagged for future sessions but does not block the Q-match retrodiction.

---

## 5. Cross-references

- BEC PDE mapping (theory basis): [`quantum/effective_theory/bec_pde_mapping.md`](../effective_theory/bec_pde_mapping.md)
- Jin 1997 scaffolded verdict: [`quantum/retrodictions/jin1997_verdict.md`](jin1997_verdict.md)
- Optomechanics scaffold (source of the three blockers): [`quantum/retrodictions/optomechanics_scaffold.md`](optomechanics_scaffold.md)
- Platform-bridges durable memo: [`memory/project_platform_bridges.md`](../../.claude/projects/C--Users-allen-GitHub-Event-Density/memory/project_platform_bridges.md)

---

## 6. One-line summary

> **BEC platform-bridge is the first completed Phase-2 derivation. Loaded test: Q ≈ 3.5, N_osc ∈ [7, 16] at T/T_c ≈ 0.93–0.95. Execution blocks only on Jin 1997 PDF retrieval and arithmetic. Status: Phase-2: paused with a loaded test.**
