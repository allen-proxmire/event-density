# ED's Gravitational Effective Action: the FORM Is Determined (Khronometric, Aether = the Arrow), the Parameters Reduce to ONE Distinctive Number (lambda), and the Equivalence-Principle Limit Decouples the Scalar from Radiation. NOT a Derivation of the Couplings.

**Foundations, gravity / curvature-emergence arc, the effective action. HONEST FRAMING FIRST: this is NOT a first-principles derivation of ED's coupling coefficients from the substrate. That is a research-program-scale computation (coarse-graining the substrate dynamics into a gravitational effective action), and it is not done here; claiming it would be fabrication. What this note does, honestly, is three things. (1) It fixes the FORM of the action: ED gravity's effective action is the khronometric / Hořava form (the hypersurface-orthogonal Einstein-aether action), because ED has a dynamical metric plus a preferred frame, and the preferred frame (the aether) IS the arrow (P11). This is grounded (ED is khronometric). (2) It reduces the parameters via ED's structural conditions: the action `S = (1/16πG)∫ N√h [K_ij K^ij − λ K² + ξ ³R + η a_i a^i]` has GR at `(λ,ξ,η) = (1,1,0)`, and ED's conditions give `ξ = 1` (shared light cone → `c_T = c`, GW170817) and `η → 0` (equivalence principle → small preferred-frame PPN), leaving `λ` (the K²-coefficient, the GR-deviation carrying the scalar sector) as the ONE distinctive parameter. (3) It computes one consequence that matters, from the standard khronometric scalar-mode formula: in ED's equivalence-principle limit (`c_14 → 0`) the scalar mode speed DIVERGES, so the scalar decouples from RADIATION (probe: `c_S² ~ 87, 870, 8700` as `c_14 = 10^{-3}, 10^{-4}, 10^{-5}`), leaving near-pure-tensor (GR-like) gravitational waves plus a static (non-radiating) scalar that can still supply MOND, the cleanest possible resolution (ED radiates like GR, the scalar gives only static galactic MOND). Probe: `evaluation/CurvatureEmergence/khronometric_effective_action_probe.py`. Tiers: FORM determined (grounded); parameter reduction (account arguments); scalar-decoupling (from the standard formula, suggestive, the limit is singular); `λ` and the full coefficient computation OPEN, the real frontier, with the obstruction named (the substrate's rigidity for foliation-expansion = the K² coefficient, to be read off the P12 stability landscape).**

---

## 1. The form is determined: khronometric, aether = the arrow

ED gravity has (a) a dynamical emergent metric (with a genuine spin-2 sector, shown in the spin-2 note) and (b) a preferred frame, the arrow (P11, the irreversible commitment direction). A dynamical-metric gravity with a preferred frame is, by construction, the Lorentz-violating (Einstein-aether / Hořava) class, and the hypersurface-orthogonal (khronometric) restriction is the natural one because ED's preferred frame is a global time foliation (the arrow defines a "now"). So the effective action FORM is fixed:
$$S = \frac{1}{16\pi G}\int N\sqrt{h}\,\Big[\,K_{ij}K^{ij} - \lambda K^2 + \xi\,{}^3\!R + \eta\, a_i a^i\,\Big] + S_{\text{matter}},$$
in ADM variables adapted to the arrow's foliation (`N` lapse, `h_ij` spatial metric, `K_ij` its extrinsic curvature, `a_i = ∂_i \ln N` the acceleration, `³R` the spatial Ricci). The **aether `u^μ` is the arrow**: the unit timelike normal to the commitment foliation. General relativity is the single point `(λ, ξ, η) = (1, 1, 0)`, where general covariance is restored and the extra modes disappear. This identification is grounded, it is what "ED is khronometric with a dynamical spin-2 metric" means, written as an action.

## 2. ED's structural conditions reduce the parameters to one

Two of the three parameters are fixed near their GR values by ED's structure (account-tier arguments, established earlier in this arc):

- **`ξ = 1` (equivalently `c_13 = 0`), from the shared light cone.** The tensor mode speed is `c_T² = ξ`, and ED's photons and gravitons, both emergent substrate modes, share the one substrate light cone (protected by the universal coupling), so `c_T = c` and `ξ = 1`. This is exactly GW170817's requirement (`|c_T − c|/c < 10^{-15}`), structurally natural.
- **`η → 0` (equivalently `c_14 → 0`), from the equivalence principle.** `η` is the acceleration/preferred-frame coupling, controlling the PPN parameters `α_1, α_2`. ED's universal coupling (`Q ∝ M`, the equivalence principle that also killed the scalar dipole) suppresses preferred-frame effects on matter, so `η → 0`.
- **`λ` is the one distinctive parameter.** The `K²` coefficient `λ` is the genuine GR-deviation: `λ = 1` is GR (general covariance), `λ ≠ 1` is the Lorentz-violating deformation whose extra scalar mode is ED's non-GR content. `λ` is **not** fixed by the above; it is the one number that carries ED's distinctive gravitational physics, and it is the target of the (open) coefficient computation. Physically `λ` is *the substrate's rigidity for foliation-expansion*, how much the arrow resists changing its expansion rate (`K = ∇·u`).

So ED's effective action reduces to a **one-parameter** deformation of GR: GR in `ξ` and `η`, with `λ` the single distinctive knob.

## 3. The equivalence-principle limit decouples the scalar from radiation

A consequence worth stating, computed from the standard khronometric scalar-mode formula (on the `ξ=1` slice, `c_S² = c_2(2 − c_14)/[c_14(2 + 3c_2)]`): **as `c_14 → 0` (ED's equivalence-principle limit) the scalar mode speed diverges** (probe: `c_S² ≈ 87, 870, 8700` for `c_14 = 10^{-3}, 10^{-4}, 10^{-5}`). A mode with `c_S → ∞` is instantaneous, non-dynamical, and does **not radiate** (no retardation, no energy flux to infinity), while it can still mediate a static/quasi-static force. So in ED's near-exact equivalence-principle limit:

> **ED radiates near-pure tensor (GR-like) gravitational waves, and the scalar mode does not radiate but survives as a static field that supplies MOND at galactic scales.**

This is the cleanest possible resolution of the radiative sector: ED's gravitational waves are essentially GR's (tensor, right speed, right polarization, matching pulsars and LIGO with no scalar admixture and no over-radiation), while the non-radiating scalar gives only *static* galactic MOND. It resolves the earlier "would the scalar over-radiate to 7/6?" worry: in the equivalence-principle limit the scalar simply does not radiate. The caveat, stated honestly: the `c_14 → 0` limit is singular, and whether ED's `c_14` is small *enough* (how exact ED's equivalence principle is) is open; small-but-nonzero `c_14` leaves a tiny scalar-radiation admixture, within current bounds.

## 4. The substrate roadmap for the coefficients (a correspondence to build, not a derivation)

Each action term has a plausible substrate origin, which is the roadmap for the actual (open) derivation:

- **`K_ij K^ij − λ K²` (kinetic):** the time-evolution of the geometry along the *arrow* (the foliation's extrinsic curvature). The arrow (P11) is `u`; this term is the substrate's kinetic energy for the bending foliation.
- **`ξ ³R` (spatial curvature):** the emergent `g~1/b` metric's spatial Ricci, from the holographic/reach structure already derived.
- **`η a_i a^i` (acceleration):** the foliation's acceleration coupling, suppressed by the universal coupling.
- **`λ` (the `K²` coefficient, the open number):** the substrate's rigidity for foliation-expansion. Reading it off the **P12 stability landscape** (`Σ = Coh − Str − Grad`), coarse-grained and covariantized with the arrow as `u`, is the actual open derivation. The obstruction is concrete: it requires the substrate's energy cost for changing the commitment foliation's expansion rate, which is not yet computed.

## 5. Honest tiers and verdict

- **Effective action FORM: grounded.** Khronometric / Hořava, aether = arrow, from ED being a dynamical-metric preferred-frame gravity.
- **Parameter reduction `ξ=1`, `η→0`: account arguments** (shared light cone; equivalence principle), established earlier in the arc.
- **Scalar decoupling in the `c_14→0` limit: derived from the standard formula, suggestive** (the limit is singular; ED's `c_14` smallness is open). It gives the clean "near-pure-tensor GW + static MOND scalar" picture.
- **`λ` and the full coefficient computation: OPEN, the real frontier.** Not derived; the roadmap (Σ-landscape → action) and the obstruction (foliation-expansion rigidity = the `K²` coefficient) are named.

**Verdict.** ED's gravitational effective action is *determined in form* (khronometric, aether = the arrow) and *reduced to a single distinctive parameter* `λ` by ED's structural conditions, with `ξ=1` (GW170817) and `η→0` (equivalence principle) near-GR, and with the equivalence-principle limit decoupling the scalar from radiation (near-pure-tensor GW + static MOND). This is a genuine step, the form and the parameter reduction, and it is *not* the full derivation: computing `λ` (and confirming `ξ=1`, `η=0`) by coarse-graining the substrate `Σ` dynamics is the stated open problem, with its obstruction named. ED gravity is now pinned to a one-parameter khronometric deformation of GR, GR in the radiative/high-acceleration sector and MOND (the `λ` scalar) at low acceleration, awaiting the single number `λ` from the substrate.
