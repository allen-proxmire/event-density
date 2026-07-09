# Computing λ: ED's Metric Sits on the Healthy Low-λ Branch (λ ∈ [0, 1/3), Natural Value 0, Definitively Not GR's λ=1)

**Foundations, gravity / curvature-emergence arc. This computes the one number the Σ-to-action setup left open: `λ`, the compression-vs-shear kinetic weighting of ED's emergent metric. Probe: `evaluation/CurvatureEmergence/lambda_compression_shear_probe.py`. HONEST FRAMING: the exact decomposition and the three reference points are DERIVED (machine-precision); ED's *placement* (natural value 0, bounded range, healthy branch, `λ≠1`) is a STRUCTURAL ARGUMENT resting on the Coh→kinetic association, not a first-principles single number. The genuine result is a bounded value with a definitive qualitative conclusion.**

---

## 1. The exact handle (derived)

Decompose the extrinsic curvature `K_ij = A_ij + (1/3)h_ij K`, `A` traceless (shear, spin-2), `K` trace (compression, spin-0). Machine-precision identity (probe, max rel error 6e-16):
$$ K_{ij}K^{ij} - \lambda K^2 = A_{ij}A^{ij} + \left(\tfrac13 - \lambda\right)K^2. $$
So the shear weight is `w_A = 1` and the compression weight is `w_K = 1/3 − λ`. **`λ` is nothing but the compression-vs-shear kinetic weighting**: `λ = 1/3 − w_K/w_A`. Three reference points, each with a clear physical meaning:

| `λ` | `w_K` (compression weight) | meaning |
|---|---|---|
| **0** | `+1/3` | compression is a **normal positive-energy mode**, same natural weight as shear (isotropic / identity substrate kinetic term `K_ij K^ij`). Minimal. |
| **1/3** | `0` | compression carries **no** kinetic energy (fully constrained / removed). |
| **1 (GR)** | `−2/3` | compression is a **negative-energy conformal ghost** (the DeWitt supermetric, forced by 4D diffeo invariance, tamed by the Hamiltonian constraint). |

The load-bearing fact: **GR's `λ=1` is *forced* by full 4D diffeomorphism invariance** (it makes the trace mode a ghost). A khronometric substrate has only 3D spatial diffeos + the arrow's preferred time, so it is **not** forced to `λ=1`; `λ` is a genuine free parameter set by the substrate inertia (this is exactly why Hořava/khronometric gravity carries `λ` as a coupling).

## 2. ED's placement (structural argument)

- **Natural/minimal value `λ = 0`.** The kinetic term is the coherence / participation-velocity channel (RBG: Relation; the reversible channel `v`). That inertia gives the compression *and* shear modes **positive** kinetic energy, isotropically (the substrate has no built-in preference splitting trace from traceless), which is the identity supermetric `K_ij K^ij` → `λ = 0`. ED is not forced to GR's ghost value; its minimal inertia is `λ=0`.
- **Conservation pushes toward `λ = 1/3`, never past.** Bandwidth conservation (P04) ties the compression mode `∂_t b` to the current via continuity `∂_t b + ∇·J = 0`. A constraint on a mode can only **suppress** its free kinetic weight (`w_K`: from `+1/3` toward `0`), pushing `λ` from 0 toward `1/3`. It cannot drive `w_K < 0`: ED's substrate modes are positive-energy, so it never reaches GR's conformal ghost. **Result: `λ ∈ [0, 1/3)`, natural value 0.**
- **Definitively `λ ≠ 1`.** ED's compression mode is a healthy dynamical field, not GR's constrained negative-energy ghost. This is the sharp, qualitative conclusion: **ED's metric kinetic structure differs from GR's in the trace sector**, and it does so on the *healthy* side.

## 3. What this does and does not change

- **Tensor (shear, spin-2) sector: GR-like, for any `λ`.** The shear weight is `1` in ED and GR alike; `λ` never touches it. So the spin-2 graviton and its **tensor radiation are GR-like** regardless of `λ`. This is why the earlier "GR-like tensor + extra scalar" reading is consistent with `λ ≠ 1`.
- **Scalar (compression) sector: healthy, and it is the MOND/khronon.** `λ` sets only the extra scalar mode. The standard khronometric health result: the scalar graviton is ghost-free / stable on the **low branch `λ < 1/3`** (and on `λ > 1`); the window `1/3 < λ < 1` is unhealthy; `λ = 1` is GR (scalar non-dynamical). **ED's `[0, 1/3)` lands squarely in the healthy low branch** — not by tuning, but because the substrate's positive-energy inertia + conservation put it there. ED's extra scalar (the khronon = the MOND/static sector) is a well-behaved positive-energy field.

## 4. Honest tiers and verdict

- **The decomposition and the three reference `λ` values: DERIVED** (machine-precision identity + standard DeWitt/Hořava facts).
- **`λ = 0` as ED's natural value: a structural argument** resting on the Coh→kinetic association (participation-velocity inertia is isotropic and positive-energy). Not a first-principles single number.
- **`λ ∈ [0, 1/3)`: bounded** by the compression-mode physics (positive-energy floor at ghost; conservation suppression ceiling at fully-constrained). The residual (exactly *where* in `[0,1/3)`) is how strongly P04+P05 conservation constrains the compression weight, which needs the full mode-resolved substrate inertia.
- **`λ ≠ 1` (not GR) and the healthy-low-branch placement: robust** given positive-energy substrate modes.

**Verdict.** The one open number of ED gravity is now a **bounded, signed result**: `λ ∈ [0, 1/3)`, natural value `0`, the **healthy low-λ branch** of khronometric gravity, with a **GR-like tensor (spin-2) sector** and a **healthy dynamical scalar** (the khronon / MOND sector), and **definitively `λ ≠ 1`** — ED's emergent metric is a *healthy Lorentz-violating deformation of GR*, differing only in the trace/scalar sector, and on the well-behaved side of it. That is as far as an honest structural computation reaches: not a single decimal, but a bounded value, a definite branch, a definite health verdict, and a definite break from GR. Pinning the exact point in `[0,1/3)` (hence the precise scalar-mode speed and the MOND interpolation constant) is the remaining calculation, now needing only the mode-resolved P04+P05 inertia. See [[project_curvature_emergence_arc]].
