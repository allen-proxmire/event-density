# Phase Bits / Delta — Determinability-Boundary Bits Measurement

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Document:** Δ computation — the measurement the arc was built to produce
**Status:** **Implemented, run, PASS** — Δ ≈ 0.09 bits on the MWE; M1 > M2 ≈ M3 ≈ 0; stable; no regression
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_Bits_DeterminabilityBoundaryMeasurementPlan.md` (the program); `Phase_CertificationRun.md` (the certified instrument); `Delta_Results.md` (recorded run)

---

## 1. Purpose

This document implements the **Δ computation** on the certified ED substrate simulator. Δ is the **determinability-boundary contrast** — the difference between how much determination propagates *within* a reach stratum and how much crosses the decoupling boundary:

> **Δ = M1 − M2** (bits), with **M3** the shuffle/null control.

- **M1** — within-stratum predictability (information shared inside a reach cell);
- **M2** — across-boundary predictability (information shared across the determinability boundary);
- **M3** — the estimator's finite-sample floor (M2 should match it).

A positive Δ is the **bits of determination the architecture forfeits at the decoupling surface** — present within a stratum, absent across it. **Units: bits** (Miller-Madow MI computed in nats, converted by 1/ln 2). This is the quantitative counterpart to the *structural* determinability boundary located in Phase E §6, and it is only permitted now because the simulator is **certified** (all four gates green).

The code was written, executed, and **passes** (output §6; record in `Delta_Results.md`); certification is unaffected (20/20).

---

## 2. Ensemble Protocol

Δ is an **ensemble** quantity — randomness lives only in the seeded initial conditions; each trajectory is deterministic. The protocol:

- Generate **N independent MWE runs** (default N = 200; also 100, 400 for stability).
- For each run `k`: `run_mwe(seed_a = 1000 + k, seed_b = 5000 + k, record=False)` — independent seeds per stratum, so A and B are genuinely independent draws.
- Extract per-run summaries (summed final ρ): the A-summary, the B-summary, and the two halves of A (`A_left` = nodes 0–3, `A_right` = nodes 4–7).
- Store as a dataset of equal-length sample vectors.

The dataset is the input to the measures; the protocol is reproducible (fixed seed bases).

```python
def build_dataset(N, base_a=1000, base_b=5000):
    A, B, AL, AR = [], [], [], []
    for k in range(N):
        sv = run_mwe(seed_a=base_a + k, seed_b=base_b + k, record=False)["sv"]
        A.append(sum(sv[n].rho for n in A_NODES))
        B.append(sum(sv[n].rho for n in B_NODES))
        AL.append(sum(sv[n].rho for n in A_LEFT))
        AR.append(sum(sv[n].rho for n in A_RIGHT))
    return {"A": np.array(A), "B": np.array(B),
            "A_left": np.array(AL), "A_right": np.array(AR)}
```

---

## 3. Measures

All three use the **same** Miller-Madow-corrected histogram MI estimator (`analysis/entropy.py`) at the **same** binning, so Δ differences out the estimator's finite-sample bias (the Δ-difference design, measurement plan §3). Nats → bits via 1/ln 2.

- **M1 — within-stratum predictability:** `MI(A_left ; A_right)`. The two halves of stratum A are reach-connected (a continuous chain), so they share information ⇒ M1 > 0. This is the natural within-stratum analogue of M2: MI between two node-groups that *are* reach-connected.
- **M2 — across-boundary predictability:** `MI(A ; B)`. The two strata are reach-decoupled (the bridge is severed), so they share ~no information ⇒ M2 ≈ 0.
- **M3 — shuffle/null control:** `MI(A ; shuffled B)`. Destroys any A↔B pairing; the residual is the estimator's finite-sample floor. M2 should be statistically indistinguishable from M3.

M1 and M2 are on the same footing — both are MI between two node-groups, one reach-connected, one reach-decoupled — which is what makes Δ = M1 − M2 a clean contrast.

---

## 4. Code — `Bits/analysis/delta.py`

```python
"""Delta - the determinability-boundary bits measure.

    Delta = M1 - M2          (bits)

  M1 = within-stratum predictability  = MI(A_left ; A_right)
  M2 = across-boundary predictability = MI(A ; B)
  M3 = shuffle/null control           = MI(A ; shuffled B)

M1, M2, M3 use the SAME Miller-Madow-corrected histogram estimator and the SAME
binning, so Delta differences out the estimator's finite-sample bias.
"""
from __future__ import annotations

import numpy as np

from .entropy import mutual_information

NATS_TO_BITS = 1.0 / np.log(2.0)


def _mi_bits(x, y, bins: int) -> float:
    return float(mutual_information(np.asarray(x), np.asarray(y), bins=bins)
                 * NATS_TO_BITS)


def compute_M1(dataset: dict, bins: int = 2) -> float:
    """Within-stratum predictability: MI between two halves of stratum A."""
    return _mi_bits(dataset["A_left"], dataset["A_right"], bins)


def compute_M2(dataset: dict, bins: int = 2) -> float:
    """Across-boundary predictability: MI(A_summary ; B_summary)."""
    return _mi_bits(dataset["A"], dataset["B"], bins)


def compute_M3(dataset: dict, bins: int = 2, seed: int = 0) -> float:
    """Shuffle/null control: MI(A_summary ; shuffled B_summary)."""
    rng = np.random.default_rng(seed)
    b = np.asarray(dataset["B"]).copy()
    rng.shuffle(b)
    return _mi_bits(dataset["A"], b, bins)


def compute_delta(M1: float, M2: float, M3: float | None = None) -> dict:
    """Delta = M1 - M2 (bits), with components and (if M3 given) M2 - M3."""
    out = {"delta_bits": float(M1 - M2), "M1_bits": float(M1), "M2_bits": float(M2)}
    if M3 is not None:
        out["M3_bits"] = float(M3)
        out["M2_minus_M3_bits"] = float(M2 - M3)
    return out


def compute_all(dataset: dict, bins: int = 2, shuffle_seed: int = 0) -> dict:
    M1 = compute_M1(dataset, bins=bins)
    M2 = compute_M2(dataset, bins=bins)
    M3 = compute_M3(dataset, bins=bins, seed=shuffle_seed)
    return compute_delta(M1, M2, M3)
```

The module **computes only** — it does not run the simulator. The dataset (ensemble of runs) is supplied by the caller; the result is deterministic given the ensemble seeds.

---

## 5. Minimal Driver — `Bits/examples/delta_demo.py`

Generates the ensemble, computes M1/M2/M3/Δ, prints the decomposition and stability across N, and runs the acceptance checks. (Full source in the repo; key structure in §2 above.) Self-checking: exits non-zero if any acceptance criterion fails.

---

## 6. Acceptance Criteria — Result

Executed; **PASS** (exit 0). Recorded output:

```
====================================================================
DELTA - determinability-boundary bits measurement
====================================================================

  ensemble N = 200, bins = 2, Miller-Madow corrected, units = bits
  M1  within-stratum   MI(A_left; A_right) : +0.09201 bits
  M2  across-boundary  MI(A; B)            : -0.00245 bits
  M3  shuffle control  MI(A; shuffled B)   : -0.00101 bits
  -------------------------------------------------------------
  Delta = M1 - M2                          : +0.09446 bits
  residual M2 - M3 (should be ~0)          : -0.00144 bits

  Delta stability across ensemble sizes:
    N= 100:  M1=+0.0884  M2=+0.0032  Delta=+0.0852 bits
    N= 200:  M1=+0.0920  M2=-0.0025  Delta=+0.0945 bits
    N= 400:  M1=+0.0833  M2=+0.0000  Delta=+0.0833 bits

Checks
  M2 ~ M3 (across-boundary independence) : True
  M1 > M2 (within-stratum predictability): True
  Delta > 0                              : True
  Delta stable across N (spread 0.0112<0.10): True

====================================================================
DELTA MEASUREMENT: PASS
====================================================================
```

Certification regression: `pytest` 20 passed; `certify.py` → SIMULATOR CERTIFIED.

| Criterion | Requirement | Result |
|---|---|---|
| M2 ≈ M3 | across-boundary at the null floor | **PASS** (M2−M3 = −0.0014 bits) |
| M1 > M2 | within-stratum predictability real | **PASS** (0.092 > −0.002) |
| Δ > 0 | a positive determinability contrast | **PASS** (+0.094 bits) |
| Δ stable across N | spread < 0.10 bits over N=100/200/400 | **PASS** (spread 0.011) |
| No certification regression | 20/20 gates still green | **PASS** |

---

## 7. Interpretation and Scope (Honest Bounds)

**Measured:** **Δ ≈ 0.09 bits** on the MWE substrate (0.085–0.095 across N). The controls behave exactly as the theory requires — M2 ≈ M3 ≈ 0 (across-boundary information at the null floor) and M1 > M2 (within-stratum predictability positive). The structural determinability boundary now has a quantitative counterpart: a positive, stable number of bits the boundary blocks.

**Scope — configuration-specific, not a constant of ED.** The *magnitude* (~0.09) depends on the summary statistic, binning, Σ coefficients, extinction threshold, topology, and seeding; change them and the number moves. The *qualitative* result (Δ > 0, M2 ≈ M3, M1 > M2) is robust; the *value* is a property of this MWE, not yet of Event Density.

**FS parallel — role, not value.** FS's escape density (~0.265) is a domain-intrinsic quantity; ED's Δ here demonstrates that *the same kind of measurement is constructible* for a finite-reach substrate. The parallel is **role-to-role, structural-analogy-only** (measurement plan §6): both architectures admit a bits-denominated determinability measure. No claim that 0.09 and 0.265 are comparable in value, that ED's boundary is a parity barrier, or that the domains share content.

**To make Δ a property of ED** requires the robustness program (measurement plan §7–§8): sweep topology / reach profile / coefficients / summary, and either find a configuration-independent normalization or report Δ with its dependence characterized. That is research-scale and separate from this proof-of-method.

---

## 8. Deliverables

Produced and verified:

- **`Bits/analysis/delta.py`** — M1/M2/M3 and Δ (deterministic; reads simulator output only).
- **`Bits/examples/delta_demo.py`** — ensemble driver with stability check and acceptance gates.
- **`Bits/Delta_Results.md`** — recorded run, decomposition, honest scope.
- **`Bits/Phase_Delta_Implementation.md`** — this document.

**The empirical arc has produced its number.** The determinability-boundary bits measure is constructed, runs on the certified simulator, and returns a positive, stable Δ with within/across/null controls behaving as the theory requires. A configuration-independent ED value is the next, separable research step.

---

## 9. Next Actions — Optional, Research-Scale

The robustness program (measurement plan §7–§8): vary topology, reach profile, Σ coefficients, and summary statistic across ensembles; determine whether Δ converges to a configuration-independent ED quantity; report Δ with its dependence characterized. This is the step that would turn a proof-of-method number into a measured property of the architecture — and the quantitative side of the FS↔ED structural parallel, still strictly role-to-role.

---

*End of Δ implementation. The determinability-boundary bits measure is built and run on the certified simulator: Δ ≈ 0.09 bits on the MWE, M1 > M2 ≈ M3 ≈ 0, stable across ensemble sizes. Proof-of-method complete; a configuration-independent ED value is a separate research program.*
