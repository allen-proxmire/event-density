# Phase-3 GR — Scoping the Band-Partition Computation: Deriving `c₂` and `λ_J` from the Four Bands (Turnkey Spec)

**Foundations scoping doc — NOT a computation, NOT a result. Lays out exactly what the P04 four-band dynamics must yield to turn `c₂` (the khronon kinetic coupling) and `λ_J = c₁₄` (the preferred-frame coupling) from *inputs* into *measured outputs*, what `band_level_ppn.py` / `directed_flux.py` must add to measure them, the consistency check that closes the α₁ front's last derivation-side item, and — stated plainly up front — the honest boundary of what a lattice can and cannot settle. No number is produced or faked here; this is the spec a next session can execute directly.**

Context: `Phase3_GR_Alpha2_Vanishes_Alpha1_Reconciled.md` reduced the α₁ front to one remaining derivation-side item — confirm, *from the four-band substrate*, that `c₂ = sparsity` and that the independently-measured `λ_J = c₁₄` satisfies the `c_s=c` family relation `c₂ = c₁₄/(1−2c₁₄)`. Both sims currently **input** the couplings and confirm field structure; this scopes deriving them.

---

## 0. The honest boundary (stated first, load-bearing)

A lattice **cannot** give the absolute `α₁`: the magnitude is set by `ρ_event^vac` in the Solar System, whose value is a substrate(~Planck)-to-system multiscale/EFT problem ~10⁴⁴ below any lattice cell (`band_level_ppn.py` docstring, honestly). **What a lattice CAN give, and what this computation targets:**

1. The **dimensionless O(1) band-fraction ratios** — `k₁₁/s₀₂` (for `c₂`) and `λ_J = κ_J/κ` — which are pure numbers set by the per-tick exchange rules, lattice-independent.
2. The **scaling law** `c₂ ∝ ρ_event/ρ_Planck` — measured by *varying the commitment density* on the lattice and confirming linearity (the claim "`c₂ = sparsity`" is a *scaling* claim, lattice-testable, not a magnitude claim).
3. The **`c_s=c` consistency check** `c₂ =? λ_J/(1−2λ_J)` — two independent band-fraction measurements that must agree (the from-`F` confirmation).
4. The **factor-of-2 normalization** `λ_J` vs the Will-form `2c₁₄` — fixed by matching the measured `g_{0i}` to the verified PPN form.

Items 1–4 are the deliverable. The absolute `ρ_event^vac` (item: magnitude) stays an EFT estimate, *not* a lattice output — and that is fine, because safety already follows from the *scaling* (`c₂ ∝ ρ_event/ρ_Planck` with any plausible sub-Planck `ρ_event^vac` gives ≥70-order suppression, robustly).

---

## 1. The four bands and their per-tick exchange rules (the machinery to build)

`band_level_ppn.py` currently runs **two** effective bands (`b` conserved, `J` dissipative) with couplings as inputs. The computation needs the **explicit P04 four-band partition** with exchange rules read from the primitives, so the couplings *emerge*:

| Band (P04 §1.5) | Symbol | Dynamics (per tick) | Role |
|---|---|---|---|
| **Adjacency** | `b_adj` | symmetric P02 exchange with neighbours (graph Laplacian); **always-on, every tick** | sets the **metric stiffness `M_P²`** (density-independent) |
| **Internal** | `b_int` | the chain's own participation; local | the matter/source channel |
| **Commitment-reserve** | `b_res` | drained one-way by P11 commitment events (monotone, no replenishment) | sets the **khronon stiffness `f²`** and the **dissipative `Γ`** (density-dependent, sparse) |
| **Environmental** | `b_env` | coupling to the surroundings | the decoherence/measurement sink (background; not load-bearing for α₁) |

**The one rule that must be explicit and primitive-faithful:** a **commitment event** (P11) fires at a *locus*, at a *rate* `ρ_event` set by physical determination (NOT every tick — the sparse-commitment constraint), and when it fires it (i) moves bandwidth `b_int → b_adj`/matter channel (the `−κρ` sink), (ii) pins the local foliation (the surface of constant cumulative commitment-count), and (iii) drains `b_res` one-way. The commitment **rate** `ρ_event` is the control knob to *sweep* (item 2 above). All couplings below are read off as ratios of these exchange rates.

---

## 2. Target A — `c₂ = f²/M_P²` (the khronon kinetic coupling)

`c₂` is the ratio of the **foliation-deformation stiffness** `f²` to the **metric stiffness** `M_P²`. Measure each as an energy-per-deformation on the lattice:

**(A1) `M_P²` — metric stiffness, from the always-on adjacency band.**
- *Protocol:* impose a static gradient in `b_adj` (a frozen `∇b` profile), let the P02-sharing relax, and measure the steady gradient-energy coefficient — i.e. the coefficient `M_P²` in `E_metric = ½ M_P² (∇b)²`. Equivalently (cleaner): read it from the static Poisson the sim already solves, `D∇²b = κρ` → `κ/D = 8πG = 1/M_P²` (up to the fixed factor). **The task is to derive `D` (the adjacency-share rate) from the per-tick `b_adj` exchange fraction `s₀₂`, not input it.** `M_P² ∝ s₀₂/h²` (`h ↔ ℓ_P`).
- *Expected:* **density-independent** (every adjacency shares every tick, with or without commitments). This is the check that `M_P²` does *not* scale with `ρ_event`.

**(A2) `f²` — foliation/khronon stiffness, from the sparse commitment-reserve.**
- *Protocol:* track the **cumulative-commitment-count field** `C(x)` (its level surfaces *are* the foliation; its gradient is the foliation normal / the khronon). Impose a small foliation deformation `θ` (a twist/expansion of the `C`-surfaces), and measure the restoring energy coefficient `f²` in `E_khronon = ½ f² θ²`. The restoring stiffness comes *only* from loci where commitments have fired (P11 pinning), with strength set by the commitment-pinning fraction `k₁₁`.
- *Expected:* **`f² ∝ k₁₁ · ρ_event · h²`** — *density-dependent, linear in `ρ_event`*. This is the load-bearing measurement: **sweep `ρ_event` and confirm `f²` is linear in it** (the dilute/non-interacting-pin regime; LambdaOfRho §2).

**(A3) `c₂` and the scaling.**
- `c₂ = f²/M_P² = (k₁₁/s₀₂) · ρ_event · h⁴ = (k₁₁/s₀₂) · ρ_event/ρ_Planck`.
- *Deliverables:* the **O(1) number `k₁₁/s₀₂`** (from the two stiffness measurements at fixed `ρ_event`), and the **confirmed linear scaling** `c₂ ∝ ρ_event/ρ_Planck` (from the `ρ_event` sweep). Together these *are* the lattice-level statement "`c₂ = sparsity`."

## 3. Target B — `λ_J = κ_J/κ = c₁₄` (the preferred-frame coupling)

`λ_J` is the ratio of the **vector source-coupling** `κ_J` (how strongly a *moving* commitment-concentration drives the directed flux) to the **scalar source-coupling** `κ` (how strongly a *static* one drains the metric band). Both come from the *same* P11 commitment event — the difference is whether the firing carries the source's motion `w`. `directed_flux.py` already solves the vector Poisson `D∇²A^i = κ_J ρ w^i` and confirms `g_{0i}=λ_J w_iU` — but with `λ_J` **input**.

- *Protocol κ (static):* a static source; measure the `b`-depletion rate per unit `ρ` from the per-tick commitment exchange = `κ`. (Currently input as `kappa`; derive it from the commit-exchange fraction.)
- *Protocol κ_J (moving):* a source moving at `w`; measure the directed-flux source strength per unit `ρw` from how a moving commitment imparts directional bandwidth = `κ_J`. (Currently the source `Sx = kappa*rho*w` in `band_level_ppn.py` *assumes* `κ_J=κ`, i.e. `λ_J=1` — that assumption is exactly what must be replaced by a *measured* directional response.)
- *Deliverable:* **`λ_J = κ_J/κ`**, the O(1) band-fraction. The key physics question (DirectedFlux §5): does a moving commitment drive directional flux at the *boost-covariant* rate (which would force `α₁=0`) or deviate? `λ_J` measures the deviation.

## 4. The consistency check — the from-`F` confirmation (the heart)

`c₂` (Target A, a *stiffness* ratio) and `c₁₄ = λ_J` (Target B, a *source-coupling* ratio) are **independent measurements**. The derived, established `c_s=c` (ε=0) imposes the family relation:

> **`c₂ = c₁₄/(1−2c₁₄) = λ_J/(1−2λ_J)`**   — must hold between the two independently-measured band-fractions.

This is the decisive check. Three clean outcomes:

1. **Consistent + both `→ sparsity`** (`c₂ ∝ ρ_event/ρ_Planck`, `λ_J = c₂/(1+2c₂) ≈ c₂`): the from-`F` confirmation succeeds — `λ_J = c₁₄` is intrinsically the sparsity, the dissipative `𝒮(Γ)` is confirmed redundant, and **F1's rectification becomes from-primitives** (no longer leaning on LambdaOfRho's stiffness-origin argument alone). The cleanest win.
2. **Inconsistent with the family relation** (the two band-fractions don't satisfy `c₂ = λ_J/(1−2λ_J)`): a real finding — `c_s=c` (derived) is in tension with the band-fraction identifications, and one of {the `ε=0` derivation, the `M_P²`/`f²` band-assignment, the `κ_J/κ` band-assignment} needs revisiting. An honest "no" that bounds the keystone.
3. **Scaling confirmed, ratios O(1), magnitude still EFT** (the expected realistic outcome): `c₂ ∝ ρ_event` and `λ_J` consistent, both O(1) band-fractions pinned — but the absolute `ρ_event^vac` stays an EFT estimate (the honest boundary §0). This still *upgrades* the safety verdict from "asserted screening" to "derived scaling + measured O(1) coefficients," which is the real target.

## 5. The factor-of-2 normalization (small, do alongside)

`directed_flux.py` reads the `g_{0i}` coefficient as `λ_J` (`A_x/(w0 U) → λ_J`), but the verified Will form wants the `w_iU` coefficient `= −½(α₁−2α₂) = 2c₁₄` (at `α₂=0`). So either `λ_J = 2c₁₄` (a factor-of-2 in the metric-assembly `η`/`A_i` normalization) or the sim's `g_{0i}=A_i` convention carries it. **Fix by matching the measured `g_{0i}` annulus profile to the full Will `g_{0i}` (with the verified `V_i, W_i` standard-gravitomagnetic terms included)** — `directed_flux.py` already has `g0x=Ax`; add the `V_i/W_i` matter-current pieces and read `α₁` against the verified prefactors. Doesn't affect `α₂=0` or the `α₁ ∝ c₁₄` conclusion; nails the coefficient.

## 6. What each script needs (turnkey diff)

**`band_level_ppn.py`** (the main lift):
- Replace the 2-band (`b`, `J`) model with the **explicit 4-band partition** (§1): add `b_int`, `b_res`, the cumulative-commitment field `C(x)`, and a sparse commitment-event process with rate `ρ_event` (the swept knob).
- Derive `D`, `κ` from per-tick exchange fractions (`s₀₂`, commit-fraction) instead of inputting them.
- Add the two stiffness measurements (§2: `M_P²` from a static `b_adj` gradient; `f²` from a `C`-surface deformation) and the directional source-coupling measurement (§3: `κ_J` from a moving commitment's directional response, *measured* not set to `κ`).
- Add the **`ρ_event` sweep** and fit `f² ∝ ρ_event` (the scaling) and `M_P²` = const (the density-independence check).

**`directed_flux.py`** (smaller):
- Keep the vector-Poisson machinery; feed it the **measured** `λ_J` from `band_level_ppn.py` rather than the input.
- Add the `V_i/W_i` standard-gravitomagnetic terms and match to the full Will `g_{0i}` to settle the factor-of-2 (§5).

**New tiny driver** `band_partition_check.py`:
- Pull measured `c₂(ρ_event)` and `λ_J` from the above, run the consistency check `c₂ =? λ_J/(1−2λ_J)`, print the O(1) ratios `k₁₁/s₀₂` and `λ_J`, and report which of the three §4 outcomes obtained.

## 7. Crank-rail reminders (so the execution stays honest)

- **Report ratios and scalings, not an absolute `α₁`.** The lattice cannot reach `ρ_event^vac`; say so (it is already said in `band_level_ppn.py`).
- **The band assignment is the physics.** Which band carries the metric stiffness vs the khronon stiffness vs the directional response is the substantive claim being *tested*, not imposed — if the natural per-tick rules don't put `M_P²` in the always-on adjacency band and `f²` in the sparse reserve, that is a result, not a bug to paper over.
- **`α₂` is not in this computation.** It is already `0` (verified, gauge-invariant; §2 of the reconciliation doc). This computation is `c₂`/`λ_J` only.
- **A "no" (outcome 2) is a real result** and must be reported as such, not tuned away.

## 8. Verdict (scope only)

The band-partition computation is **well-posed and turnkey**: build the explicit four bands with primitive-faithful per-tick exchange (§1); measure `M_P²` (adjacency, density-independent), `f²` (commitment-reserve, `∝ ρ_event`), and `κ_J/κ = λ_J` (directional commitment response) as *outputs* (§2–§3); run the consistency check `c₂ =? λ_J/(1−2λ_J)` and the `ρ_event` scaling (§4); settle the factor-of-2 against the Will form (§5). The deliverable is the **O(1) band-fractions + the `c₂ ∝ ρ_event/ρ_Planck` scaling + the `c_s=c` consistency** — which confirms (or refutes) "`c₂ = sparsity` and `λ_J = c₁₄ ≈ sparsity`" from the substrate, upgrading F1's rectification from internally-argued to from-primitives. The **absolute magnitude stays an EFT estimate by construction** (§0) — and does not need the lattice, because the *scaling* already delivers the ≥70-order safety. No number is produced here; this is the spec.

---

*Scoping the band-partition computation. The four bands (adjacency=always-on→`M_P²`; commitment-reserve=sparse→`f²`,`Γ`; internal=source; environmental=sink) with primitive-faithful per-tick exchange. Two targets as OUTPUTS not inputs: `c₂=f²/M_P²` (stiffness ratio → O(1) `k₁₁/s₀₂` + linear scaling in `ρ_event`) and `λ_J=κ_J/κ=c₁₄` (directional commitment-response ratio). Decisive consistency check: `c₂ =? λ_J/(1−2λ_J)` (the c_s=c family relation) — outcome 1 (consistent, both→sparsity) closes F1 from-primitives; outcome 2 (inconsistent) bounds the keystone; outcome 3 (scaling confirmed, ratios O(1), magnitude EFT) is the realistic upgrade. Plus the λ_J-vs-2c₁₄ factor-of-2 against the verified Will form. Honest boundary stated FIRST: the lattice gives ratios + scaling + consistency, NOT the absolute ρ_event^vac (Planck-scale, multiscale-EFT, ~10⁴⁴ off-lattice) — and doesn't need to, since the scaling already gives ≥70-order safety. Turnkey diffs for band_level_ppn.py (the lift: explicit 4 bands + stiffness/source measurements + ρ_event sweep), directed_flux.py (feed measured λ_J + Will-form match), and a new band_partition_check.py. No corpus edits, no new primitives; no number produced or faked — this is the spec.*
