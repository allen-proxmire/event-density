# ED Validation

Reproducible computational tests of the seven architectural principles.

This folder contains six self-contained test scripts, each validating a
specific structural principle (P1–P7) of the Event Density architecture.
Every test solves the canonical ED PDE from scratch, extracts the
architectural signature, and produces a results file and a diagnostic
figure. No precomputed data is required. The outputs are fully
regenerable from the scripts alone.

---

## Role in the ED Program

The Architectural Canon (ED-Arch-12) states the seven principles. The
Rigour Paper (Appendix C) proves them analytically. ED Validation answers
the computational question: *does the canonical PDE, solved numerically,
exhibit each principle as a measurable signature?*

Each test is binary. The signature is either present or absent. A failure
of any test would indicate either a numerical error or a gap between the
analytic theory and the discrete implementation. All six tests pass.

These tests are distinct from the ED-SIM invariant atlas (in
`ED Simulation/`). The Validation tests are targeted: one test per
principle, minimal parameter sets, fast execution. The ED-SIM atlas is
comprehensive: sixteen invariant families across sixty-four parameter
regimes with meta-analyses and a global consistency certificate. The
Validation tests confirm the principles individually; ED-SIM confirms
that they hold together across the parameter space.

---

## Tests

### P1 — Modal Funnel

**Principle:** The Laplacian operator has eigenvalues proportional to k²,
so higher Fourier modes decay exponentially faster than lower modes. The
spectral content funnels onto the dominant surviving mode.

**Test:** Initialize with a broadband perturbation (modes k = 1–8).
Integrate the canonical PDE. Measure the modal amplitudes over time.
Confirm that each mode k decays at rate proportional to k² and that
the spectral energy concentrates onto k = 1.

**Script:** `P1_modal_funnel/test_modal_funnel.py`
**Output:** `results.json` (decay rates, amplitude time series),
`modal_funnel.png` (semilog-y plot of modal amplitudes vs time).

---

### P2 — D/H Complementarity

**Principle:** The direct channel (weight D) and the participation channel
(weight H = 1 − D) partition the operator output. Varying D shifts energy
between channels without changing the total operator weight.

**Test:** Run the canonical PDE at several D values. Measure the
dissipation contributed by each channel. Confirm that D + H = 1 is
maintained and that the channel partition shifts smoothly with D.

**Script:** `P2_DH_complementarity/test_DH_complementarity.py`
**Output:** `results.json` (channel dissipation fractions),
`DH_complementarity.png` (channel balance vs D).

---

### P3 — Manifold Collapse

**Principle:** The unique equilibrium (ρ*, 0) is a global attractor. All
initial conditions converge to the same point — the state-space manifold
collapses to a single point.

**Test:** Initialize with multiple distinct initial conditions (different
amplitudes, different mode structures). Integrate each to late time.
Confirm that all trajectories converge to the same equilibrium within
numerical tolerance.

**Script:** `P3_manifold_collapse/test_manifold_collapse.py`
**Output:** `results.json` (final states, convergence metrics),
`manifold_collapse.png` (trajectories converging to the attractor).

---

### P4 — Horizon Formation

**Principle:** The mobility M(ρ) vanishes at ρ = ρ_max, creating an
impassable barrier. The density cannot reach or exceed the capacity bound.

**Test:** Initialize with a density profile that approaches ρ_max. Integrate
the PDE. Confirm that the density remains strictly below ρ_max at all times
and that the approach rate slows as the mobility collapses.

**Script:** `P4_horizon_formation/test_horizon_formation.py`
**Output:** `results.json` (proximity margins, mobility values),
`horizon_formation.png` (density profile near the capacity bound).

---

### P6 — Damping Discriminant

**Principle:** The discriminant D₀ = (D·P*' − ζ/τ)² − 4H·P*'/τ classifies
the homogeneous-mode dynamics as oscillatory (D₀ < 0), critical (D₀ = 0),
or monotonic (D₀ > 0).

**Test:** Sweep the (D, ζ) parameter plane. At each point, compute the
discriminant and classify the regime. Integrate the PDE and confirm that
the observed dynamics (oscillatory vs monotonic) matches the discriminant
prediction.

**Script:** `P6_discriminant_boundary/test_discriminant_boundary.py`
**Output:** `regime_map_data.npz` (discriminant values, regime labels),
`regime_map.png` (colour-coded regime map of the (D, ζ)-plane).

---

### P7 — Nonlinear Triad Coupling

**Principle:** The gradient-squared term M'(ρ)|∇ρ|² generates inter-modal
coupling with the selection rule: modes m and n interact to produce modes
|m − n| and m + n. No other couplings exist.

**Test:** Initialize with exactly two modes (m, n). Integrate the PDE.
Measure the amplitude of all modes over time. Confirm that only modes
|m − n| and m + n are generated, and that their amplitude ratio matches
the analytic triad coupling coefficient.

**Script:** `P7_triad_ratio/test_triad_ratio.py`
**Output:** `results.json` (triad amplitudes, coupling ratios, selection
compliance), `triad_ratio.png` (modal amplitudes showing triad activation).

---

## Running the Tests

Each test is self-contained. To run a single test:

```
cd "ED Validation/P4_horizon_formation"
python test_horizon_formation.py
```

To run all tests:

```
cd "ED Validation"
for d in P*/; do echo "=== $d ===" && python "$d"test_*.py; done
```

Each test completes in under two minutes on a standard machine. The
outputs (JSON + PNG) are written to the same directory as the script.

---

## Output Format

Every test produces:

- **`results.json`** — Numerical results: parameters, measured quantities,
  pass/fail status, and diagnostic metadata. Machine-readable for
  automated verification.

- **`*.png`** — Diagnostic figure illustrating the architectural signature.
  Publication-quality, generated by matplotlib with no interactive display.

The P6 test additionally produces **`regime_map_data.npz`** containing the
full discriminant grid for downstream analysis.

---

## Test Summary

| Test | Principle | Signature | Status |
|------|-----------|-----------|--------|
| P1 | Operator Structure | Modal decay rates scale as k² | **Pass** |
| P2 | Channel Complementarity | D + H = 1 with smooth channel partition | **Pass** |
| P3 | Penalty Equilibrium | All ICs converge to (ρ*, 0) | **Pass** |
| P4 | Mobility Capacity Bound | ρ < ρ_max maintained; mobility collapse confirmed | **Pass** |
| P6 | Damping Discriminant | Regime classification matches discriminant sign | **Pass** |
| P7 | Nonlinear Triad Coupling | Only |m−n| and m+n modes generated | **Pass** |

All six tests pass. Principle P5 (Participation Feedback) is validated
implicitly through P2 (which tests the participation channel) and P6
(which tests the discriminant, whose structure depends on the participation
time scale τ and damping rate ζ).

---

## Connection to Other Folders

| Folder | Relationship |
|--------|-------------|
| **ED Architecture** | ED-Arch-12 (Architectural Canon) defines the seven principles tested here. |
| **ED PAPERS** | The Rigour Paper (Appendix C) provides the analytic proofs that these tests verify numerically. |
| **ED Physics** | ED-Phys modules 25–28 (robustness tests) and module 34 (unified verification) perform broader parameter-space versions of these tests. |
| **ED Simulation** | ED-SIM v1 extends these targeted tests into a sixteen-family invariant atlas across 64 parameter regimes, with a global consistency certificate. |
| **ED Experiments** | The architectural signatures validated here underpin the falsifiable predictions in the Open Note and the Applications Paper. |

---

## Citation

Proxmire, Allen T., *Event Density Ontology*, 2026
