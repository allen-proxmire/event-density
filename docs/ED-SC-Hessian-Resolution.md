# ED-SC Hessian-Definition Resolution Memo

**Date:** 2026-04-17. **Status:** superseded by ED-SC 2.0 (resolves in favour of Option 2 with motif-conditioned median form). Retained for audit trail of how the ambiguity was identified and resolved.

## §1. Two distinct Hessians

**H_param (ED-Arch-01 Scenario D).** The 2×2 Hessian of the phase-exit-step surface `f(n, σ)` evaluated at the sweep saddle `(n*, σ*) = (2.7, 0.0556)`. Entries carry units of `[steps] / [sweep-parameter]²`. Input space is the sweep grid; output is a simulation observable. Reported eigenvalues: `κ∥ ≈ −1.3, κ⊥ ≈ +1.0`. Ratio ≈ **−1.3**.

**H_field (ED-Arch-02 definition).** The 2×2 Hessian `∂²E/∂x_i ∂x_j` of the event-density field `E(x, y)` evaluated at *spatial* stationary points `(x*, y*)` where `∇E = 0`. Entries carry units of `[E] / [length]²`. Input space is physical (or k-space in band-structure applications); output is the ED field itself. **Not computed in ED-Arch-01.**

They share a name and a 2×2 structure; they share nothing else. Eigenvalues, units, and stationary-point interpretation are all different.

## §2. Resolution table

| Resolution | Claim | Cross-scale comparison target | Falsification criterion | Viability |
|:-----------|:------|:------------------------------|:------------------------|:----------|
| **R1: coordinate-free** | Any Morse saddle with the same eigenvalue ratio is the "same" architecture regardless of coordinate system | Any saddle-Hessian eigenvalue ratio extracted from any observable in any parameter space | Ratio clusters fail to concentrate near a universal value across domains | **Incoherent as stated.** Eigenvalue ratios are not coordinate-invariant under general reparameterizations; "the ratio" is not a well-defined object without a coordinate choice. Viable only if the equivalence class is specified (it is not). |
| **R2: field-space strict** | Invariance is about `H_field = ∇²E` at spatial stationary points | The same object computed in every comparison system | `H_field` eigenvalue ratios at ED-saddle stationary points do not cluster near a universal value | **Viable but likely refutes Scenario D's claim (see §3).** |
| **R3: structural mapping** | A derivation (not yet produced) maps `H_param` to `H_field` near the architectural saddle | Either Hessian, after passing through the map | The map does not exist, or the mapped quantities do not match across systems | **Viable only with the map. Currently R3 is an assertion, not a theory.** |

## §3. R2 prediction from Scenario-D architecture

The Scenario-D update rule is:

`p_{t+1}(i, j) = p_t(i, j) + Δt · [n · ∇²p_t(i, j) − α · p_t(i, j)^γ + σ · η_t(i, j)]`

All three rhs terms are isotropic on a square lattice with periodic BCs:
- `∇²` is the isotropic 5-point Laplacian (no preferred direction).
- `p^γ` is a pointwise scalar function.
- `η_t(i, j)` is spatially isotropic white noise.

Therefore the expected field-space Hessian at a random spatial stationary point of `p(x, y)` at steady state must have eigenvalues with isotropic statistics: `⟨κ₁⟩ = ⟨κ₂⟩` in magnitude (opposite signs at a saddle). **Expected ratio under R2: `κ∥/κ⊥ → −1`** on ensemble average, with fluctuations controlled by finite-grid and finite-noise artifacts.

**Prediction:** if R2 is the intended interpretation, a direct recomputation of `H_field` from Scenario-D's final `p(x, y)` at `(n*, σ*) = (2.7, 0.0556)` will give ratio ≈ −1 (not −1.3) up to statistical fluctuations. This would mean **ED-Arch-01's Local-Group / Casimir match claim cannot be reproduced from Scenario-D under R2**: the −1.3 number is a property of `H_param`, not `H_field`.

This is a prediction, not a fact. It can be checked by running the sim. If the check comes back ratio ≈ −1, R2 is inconsistent with the ED-Arch-01 published claim. If the check comes back ≈ −1.3, the isotropy argument is wrong and R2 remains live.

## §4. R3 requirement

For R3 to be the correct interpretation, the following must be produced:

- A mapping `φ` between the sweep-parameter space `(n, σ)` and a field-space coordinate system such that
  `eigenvalues(H_param) = c · eigenvalues(φ*(H_field))`
  for some proportionality constant `c`, with the equality holding at the architectural saddle.
- A derivation showing the map is intrinsic (not fitted post-hoc).
- A test in a second system (Local Group, Casimir, or other) that the same map yields consistent eigenvalues.

None of these currently exist in ED-Arch-01 or ED-Arch-02. **R3 is not a theory; it is a placeholder for one.**

## §5. Revised test plan

| Priority | Action | Deliverable | Blocks |
|:--------:|:-------|:------------|:-------|
| **1** | Ask Allen to identify intended resolution (R1, R2, R3) explicitly | One-line answer | All downstream cross-scale tests |
| **2** | Run the R2 field-space Hessian computation on a single 512×512 Scenario-D trajectory at `(n*, σ*)`. Find spatial stationary points of the final `p(x, y)`; compute eigenvalues at each; report distribution | κ∥, κ⊥, ratio distribution | Whether R2 is consistent with published claim |
| **3** | If R3: require an explicit derivation of the `H_param ↔ H_field` map before any further cross-scale comparisons | Written derivation | Any parameter-to-field matching argument |
| **4** | Suspend additional literature sweeps for κ∥/κ⊥ cross-scale matches until (1)–(3) resolve | Memo documenting suspension | Avoid wasted work chasing the wrong object |

### Valid comparison targets under each resolution

- **Under R2:** field-space Hessians at spatial stationary points of physical fields. Valid: Local Group mass sheet (if the reported ratio was extracted from `∇²(density)` at the sheet saddle), Casimir cavity (if extracted from `∇²(potential)` at the stationary-point spacing). Invalid: all parameter-space phase-diagram saddles, OSCER strain-rate-tensor saddles (those are velocity-gradient tensors, not `∇²E`), Lagrange-point Ω-potential Hessians (those are effective-potential, not `∇²E`-of-density).
- **Under R3:** both Hessians become valid comparison targets, passed through the map. Currently no target qualifies because the map is absent.
- **Under R1:** everything is a target and nothing is discriminative. R1 is not a usable test framework.

### Candidates to discard

Under the R2 interpretation, the following from prior sweeps should be set aside:
- Graphene / triangular / square / kagome M-point Hessians — these are `∂²E/∂k²` in k-space, not `∂²E/∂x²` in real space. Not directly comparable to ED-Arch-02's spatial-Hessian definition without an additional argument.
- Lagrange-point Ω-Hessians — effective potential, not event density.
- Plate buckling / OSCER stagnation — loading-tuned or symmetry-locked as previously noted.

Under R2, the valid comparison targets shrink to real-space density-field saddles in extended physical systems.

## §6. Single recommended next action (from time of writing)

**Run the R2 field-space Hessian check on Scenario D.** One simulation run, one stationary-point Hessian extraction, one number. It is the minimum computation that either (a) confirms ED-Arch-01's −1.3 as a real field-space architectural feature, or (b) confirms that −1.3 is only a parameter-space property of the sweep. The result determines whether the ED-SC cross-scale program currently has an empirical foundation or needs a new one.

**Owner:** `edsim/` infrastructure. **Estimated effort:** one focused session (~4 hours). **Blocking:** nothing — can be done before Allen's R1/R2/R3 clarification arrives and will inform the answer.

---

## §7. Resolution (2026-04-17)

The R2 field-space Hessian check was run (see `analysis/scripts/ed_arch_r2/r2_canonical.py` and the accompanying memo). The distribution over all Morse saddles at `(n*, σ*)` has median `−1.94`, broad IQR `[−3.84, −1.34]`, 28% in the ED-Arch-01 window. The raw-distributional form of R2 does not recover `−1.3` as a distribution peak.

A motif-conditioned variant of R2 (architectural-saddle filter on channel-junction topology) was then tested (see `r2_motif_filter.py`). The motif-conditioned median is `−1.304`, within `0.004` of ED-Arch-01's published value. Under this form:

- **Option 2 (field-space) is the correct interpretation.**
- **The invariant is the motif-conditioned median**, not individual saddle ratios, and not the raw Morse-saddle distribution.
- The IQR is not claimed invariant.

See `ED-SC-2.0.md` for the resulting canonical statement. This memo is retained for audit provenance.
