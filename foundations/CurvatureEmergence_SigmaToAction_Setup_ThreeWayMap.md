# Setting Up the Σ-to-Action Coarse-Graining: a Three-Way Map (Coh → Kinetic/K², Str → Potential, Grad → ³R), the Gradient Sector Verified, and λ Reduced to the Coherence Term's Conformal-vs-Shear Weighting

**Foundations, gravity / curvature-emergence arc, the Σ-to-action setup. HONEST FRAMING: this SETS UP the coarse-graining and delivers the one piece that is computable (the gradient sector); it does NOT compute λ. It also folds in a structural ASSOCIATION from AP's older cosmological work (`The Unified Cosmological Equation of ED`, March 2026, non-canonical, flagged as such) and AP's "RBG" (Relation-Boundary-Gradient) reading of Σ, which organize the whole map. Probe: `evaluation/CurvatureEmergence/sigma_to_K2_setup_probe.py`. Canonical P12: `Σ = Coh − Str − Grad`, `a = −∇Σ` (Newton's 2nd law, so Σ is a POTENTIAL; the kinetic term is separate). The khronometric effective action `S = (1/16πG)∫ N√h [K_ij K^ij − λ K² + ξ ³R + η a²]` then splits by a three-way map: (Grad → ³R) is the emergent spatial curvature, VERIFIED (`³R = 2∇²b − (5/2)(∇b)²/b`, the gradient content of `b`); (Str → potential/mass) is the restoring/equilibrium term (AP's older `P_SY2`, giving a unique equilibrium `ρ*`); and (Coh → the kinetic term, hence `λ`) is the coherence / reversible-participation channel (the participation velocity `v` of the older work), the inertial part that makes gravity dynamical and radiative. So `λ` is not in the potential (Σ's Grad/Str); it lives in the COHERENCE (participation-velocity) sector, and the open computation sharpens to: the coherence term's kinetic weighting of the conformal (compression) mode vs the shear mode. Structural argument for `λ ≠ 1`: bandwidth conservation (P04) ties the conformal mode to the current (compression), distinguishing it from the free shear mode, breaking the GR (`λ=1`) covariant balance. Tiers: Grad→³R VERIFIED; the three-way map is a structural correspondence, with Coh→kinetic an ASSOCIATION (non-canonical source, suggestive); `λ`'s VALUE OPEN, now sharply posed.**

---

## 1. The split, from canonical P12

Canonical Paper_087 P12: `Σ_C = Coh − Str − Grad`, with `a = −∇_adj Σ`. The acceleration being the *negative gradient of Σ* is Newton's second law, so **Σ is a potential**, and the *kinetic* term (the inertia that makes the geometry a wave-carrying dynamical field) is a separate structure, not in Σ. This is the load-bearing organizing fact: the effective action's potential sector (`ξ ³R`, `η a²`) comes from Σ, while the kinetic sector (`K_ij K^ij − λ K²`) comes from the inertia. So `λ` (the `K²` coefficient) is *not* read off Σ's Grad or Str; it is the inertial/kinetic weighting.

## 2. The three-way map (organized by the RBG reading)

AP's "RBG" (Relation-Boundary-Gradient) reading of `Coh − Str − Grad`, together with the structure of AP's older cosmological work (a scalar density `ρ` with a reversible *participation velocity* `v` and a *restoring penalty* `P_SY2`, non-canonical but structurally suggestive), organizes the whole `Σ → action` map:

| RBG | Σ term | substrate role | effective-action term | status |
|---|---|---|---|---|
| **Gradient** | Grad | spatial-gradient penalty | `ξ ³R` (spatial curvature) | **VERIFIED** (§3) |
| **Boundary** | Str | restoring/equilibrium (`P_SY2`, unique `ρ*`) | a potential / mass term (cosmological-constant / khronon-mass sector) | association |
| **Relation** | Coh | coherence = reversible participation channel (velocity `v`) | the **kinetic** term `K_ij K^ij − λ K²`, i.e. `λ` | association |

The organizing content: **the `K²` kinetic term maps to the *coherence* (Relation) sector** — the reversible participation channel that carries inertia and hence radiation, while the restoring penalty (Boundary/Str) is a potential and the gradient (Grad) is `³R`. The Coh→kinetic identification is an *association* (from AP's older, non-canonical cosmology and the RBG reading), flagged as such, but it is a genuinely useful pointer: it says *which* part of Σ supplies the kinetic term, sharpening the open λ-computation. It also matches the older work's finding that the *inertial/wave* sector dominates near the ceiling (high density/acceleration) while the *diffusive* sector dominates in the bulk, consistent with "high acceleration → wave/GR sector" (pulsars).

## 3. The gradient sector, verified: Σ's Grad IS the spatial curvature

The one computable piece. The emergent spatial metric is `h_ij = (1/b)δ_ij` (conformal, from reach `~ b^{1/2}` in 3D). For a conformally-flat 3-metric `h_ij = e^{2ω}δ_ij` with `ω = −½ ln b`, the scalar curvature is (derived, and probe-verified to finite-difference accuracy, `~1%`):
$$ {}^3R = -2 e^{-2ω}\big[2\nabla^2\omega + (\nabla\omega)^2\big] = 2\nabla^2 b - \tfrac52\frac{(\nabla b)^2}{b}. $$
The `∇²b` piece is a total derivative (integrates to the boundary); the remaining `−(5/2)(∇b)²/b` is the **gradient content** of `b`, which is exactly Σ's **Grad** term. So `ξ ³R` is (a multiple of) Σ's Grad: **the emergent spatial-curvature energy IS the substrate's gradient penalty.** The potential sector's spatial-curvature term is done. (The `η a²` acceleration term likewise comes from the gradient of the lapse, part of the same gradient sector; the `Str` restoring term is the potential/mass.)

## 4. The conformal mode, and why λ ≠ 1

- **The conformal (expansion) mode is the bandwidth density `b`.** The trace `K = −∂_t(\ln√h)/N = (3/2)(∂_t b/b)/N` (3D), so the geometry's volume/expansion mode is `b`'s time-evolution. `λ` is the kinetic weight of *this* mode relative to the shear (traceless) mode.
- **`λ ≠ 1` structurally.** Bandwidth conservation (P04) ties the conformal (compression) mode `∂_t b` to the current via continuity `∂_t b + ∇·J = 0`, distinguishing it kinetically from the *free* (transverse) shear mode. GR's `λ=1` treats them covariantly (the DeWitt supermetric, no distinction); ED's conservation constraint breaks that, so `λ ≠ 1` — the extra scalar (the khronon / MOND sector) is dynamical. A structural reason, not a value.

## 5. What remains, now sharply posed

The open computation is reduced to one well-defined quantity: **the coherence (participation-velocity) term's kinetic weighting of the compression (conformal, `∂_t b`, conserved) mode versus the shear (transverse) mode**, calibrated against the GR/DeWitt value. That ratio *is* `λ`. It requires the mode-resolved structure of the Coh/participation-velocity kinetic term (the reversible channel `v` of the older work, grounded in canonical Coh), which is not yet computed. The gradient sector (Grad → ³R) is done; the potential/mass sector (Str) is identified; the kinetic sector (Coh → K²) is located and its parameter `λ` is the one number left.

## 6. Honest tiers and verdict

- **Grad → ³R: verified** (probe; the emergent spatial curvature is the substrate gradient penalty).
- **The three-way map (Coh→kinetic, Str→potential, Grad→³R): a structural correspondence**, with Grad→³R solid, and **Coh→kinetic an association** (from AP's older non-canonical cosmology + the RBG reading), suggestive and useful for locating `λ`, not a derivation. Treat the older cosmological paper as an association, not a canonical source (canonical is Paper_087).
- **`λ ≠ 1`: a structural argument** (P04 conservation distinguishes compression from shear).
- **`λ`'s value: OPEN**, now sharply posed as the coherence term's compression-vs-shear kinetic weighting.

**Verdict.** The Σ-to-action coarse-graining is set up and half-built: the potential sector is mapped (Grad → ³R verified; Str → potential), the kinetic sector is *located* in the coherence / participation-velocity channel (organized by the RBG reading, an association), the conformal mode is identified as `b`, and `λ ≠ 1` has a structural reason (conservation). The one remaining number, `λ`, is reduced to a single sharply-posed computation, the coherence term's compression-vs-shear kinetic weighting, which is the real open frontier of ED gravity. This is a genuine setup with one sector verified and the rest cleanly posed, not a derivation of `λ`.
