# ED-SC 2.0 r* from Local Geometry: Saddle PDE + Quasi-Potential

**Status:** Derivation memo. Analytic, self-contained. Starts from the Scenario D
intermediate-regime PDE; ends with r* expressed in local geometric quantities
(principal spatial curvatures at the saddle + mobility/penalty coefficients +
a single non-local M₂ correction). Successor to
`ED_SC_2_0_r_star_Derivation_Attempt.md` and
`ED_SC_2_0_r_star_Derivation_Extended.md`.

**Scope marker.** What is *derived* here: the saddle PDE, the quasi-potential
Hamilton–Jacobi equation for ED drift, the structure of the field-space Hessian
H of Ψ at a saddle motif, and the closed symbolic form of r* in terms of local
data. What is *still empirical*: the actual saddle shape δ*(x,y) at the
Scenario D parameters — i.e. the specific values of (κ∥, κ⊥, δ*_max, w)
obtained by numerical integration of the nonlinear elliptic problem. The memo
cleanly separates the two.

---

## 1. Scenario D PDE (intermediate regime)

The canonical Scenario D stochastic PDE on a 2D real-space density field δ(x,t)
is

    ∂_t δ  =  ∇·( M(δ) ∇δ )  −  P(δ)  +  ξ(x,t)                    (1.1)

with

    M(δ)  =  M_0 + ½ M_2 δ²                                         (1.2)
    P(δ)  =  P_0 δ + (1/6) P_3 δ³                                   (1.3)
    ⟨ξ(x,t) ξ(x',t')⟩ = 2 σ² δ²(x−x') δ(t−t')                       (1.4)

Sign conventions for Scenario D:

    M_0 > 0   (baseline mobility, rescale M_0 = 1)
    M_2 ≠ 0   (amplitude-dependent mobility; small parameter)
    P_0 > 0   (linear restoring penalty at δ = 0)
    P_3 < 0   (cubic softening; enables finite-amplitude stationary motifs)
    σ²  > 0   (weak noise; quasi-potential regime σ² → 0)

Canonical Scenario D numbers (ED-Arch-01, carried through ED-SC 2.0):

    n* = 2.7 (mobility exponent in full model; here absorbed into M₂/M₀ ratio)
    σ* = 0.0556
    α_penalty = 0.03,   γ = 0.5 (concave)
    dt = 0.05, grid = 64²–512², IC = uniform[0.3, 0.7], seed = 77.

The motif filter (pre-registered): α = 0.25, L_ray = 2, δ = 0.10. Sets the
symmetry class of the motifs whose field-space Hessian we diagonalize.

Deterministic drift:

    F[δ](x)  ≡  M(δ) ∇²δ  +  M'(δ) |∇δ|²  −  P(δ)
            =  (M_0 + ½ M_2 δ²) ∇²δ  +  M_2 δ |∇δ|²  −  P_0 δ − (1/6) P_3 δ³.
                                                                    (1.5)

Saddle equation: F[δ*] = 0 pointwise.

---

## 2. Deterministic saddle equation

Dropping noise and setting ∂_t δ = 0,

    (M_0 + ½ M_2 δ*²) ∇²δ*  +  M_2 δ* |∇δ*|²
          −  P_0 δ*  −  (1/6) P_3 δ*³   =   0.                      (2.1)

Equivalently in divergence form,

    ∇·( M(δ*) ∇δ* )  =  P_0 δ*  +  (1/6) P_3 δ*³.                   (2.2)

**Boundary / asymptotic conditions encoding Scenario D "ray" geometry.**

(B1) Localization:  δ*(x) → 0  as |x| → ∞.
(B2) D₂ (two-fold) symmetry of the ray motif: δ*(x,y) = δ*(−x,y) = δ*(x,−y).
(B3) A preferred axis of elongation (the "ray"): the spatial Hessian at the
    central stationary point x_0 has two distinct principal curvatures κ∥, κ⊥
    with κ∥ ≠ κ⊥. WLOG orient ∥ along x̂.
(B4) Motif-filter compatibility (§1.4 of ED-SC-2.0.md): δ*(x_0) ≥ δ = 0.10 and
    the ray length L_ray ≥ 2 defined at threshold α = 0.25.

The saddle is a spatially stationary point of δ*: ∇δ*(x_0) = 0. The |∇δ*|²
term in (2.1) therefore vanishes *at* x_0, but not in a neighbourhood, which is
where the non-gradient obstruction will show up in §3.

**Reduction around x_0.** Taylor-expand δ* at the central stationary point,

    δ*(x) = δ*_max + ½ κ∥ x² + ½ κ⊥ y²  +  O(|x|⁴)                  (2.3)

with (κ∥, κ⊥) the two eigenvalues of the spatial Hessian K_ij = ∂_i ∂_j δ*(x_0)
in principal axes. At this point ∇²δ*(x_0) = κ∥ + κ⊥, so (2.1) evaluated at x_0
gives the **amplitude-curvature relation**

    M(δ*_max) · (κ∥ + κ⊥)  =  P_0 δ*_max + (1/6) P_3 δ*_max³.       (2.4)

Equation (2.4) is the only piece of (2.1) that constrains κ∥ + κ⊥ from local
data alone. The *difference* κ∥ − κ⊥ and the individual values κ∥, κ⊥ require
the full nonlinear elliptic problem (2.1)+(B1–B4); they are genuinely non-local.

---

## 3. Freidlin–Wentzell quasi-potential equation

For the Langevin-type SPDE (1.1), the weak-noise stationary density is

    P_∞[δ]  ∝  exp( − Ψ[δ] / σ² )   (σ² → 0)                        (3.1)

with the quasi-potential Ψ[δ] a non-negative functional satisfying the
**functional Hamilton–Jacobi equation**

    (1/2) ∫ ( δΨ / δδ(x) )²  d²x   +   ∫ ( δΨ / δδ(x) ) · F[δ](x) d²x  =  0.
                                                                    (3.2)

The minimizing variational condition is

    δΨ / δδ(x)  =  − 2 F*[δ](x)                                     (3.3)

where F*[δ] is the time-reversed drift (with the gradient part intact and the
non-gradient part sign-flipped).

**Gradient baseline.** Define

    Φ[δ]  =  ∫ [ ½ M(δ) |∇δ|²  +  U(δ) ] d²x,   U'(δ) = P(δ).       (3.4)

Then

    − δΦ / δδ   =   ∇·(M ∇δ)  −  ½ M'(δ) |∇δ|²  −  P(δ)
                =   F[δ]  −  (3/2) M_2 δ |∇δ|² 

wait — let us be careful. From (1.5) and (3.4),

    δΦ/δδ  =  ½ M'(δ)|∇δ|²  −  ∇·(M(δ)∇δ)  +  P(δ)
           =  ½ M_2 δ |∇δ|²  −  M ∇²δ  −  M_2 δ |∇δ|²  +  P(δ)
           =  − M ∇²δ  −  ½ M_2 δ |∇δ|²  +  P(δ).                  (3.5)

Therefore

    F  −  (− δΦ/δδ)   =   ( M ∇²δ + M_2 δ|∇δ|² − P )
                       −  ( M ∇²δ + ½ M_2 δ |∇δ|² − P )
                       =   ½ M_2 δ |∇δ|².                          (3.6)

This is the **variational obstruction**: the drift differs from any gradient
flow of Φ by the transverse field

    G[δ](x)  ≡  ½ M_2 δ(x) |∇δ(x)|².                                (3.7)

At the saddle point x_0 itself G = 0 because ∇δ*(x_0) = 0. Away from x_0,
however, G ≠ 0 and it is this bulk term that makes Ψ ≠ 2Φ.

**Expansion of Ψ in M_2.** Set

    Ψ[δ]  =  2 Φ[δ]  +  M_2 Ψ_1[δ]  +  M_2² Ψ_2[δ]  +  …           (3.8)

Inserting into (3.2) and matching orders:

O(M_2⁰):    ( δΦ/δδ )² = ( δΦ/δδ )·(− F_0)   with F_0 = M_0∇²δ − P(δ);
this is automatic since F_0 = − δΦ_0/δδ with Φ_0 = Φ|_{M_2=0}.      (3.9a)

O(M_2¹):    the transport equation

    ∫ ( δΦ/δδ ) · [ δΨ_1/δδ  −  2 δ|∇δ|²/M_2·(…)  ] d²x = 0,

which after rearrangement reads

    ∫ ( δΦ/δδ )(x) · ( δΨ_1/δδ )(x) d²x
        =   2 ∫ ( δΦ/δδ )(x) · ( δ(x) |∇δ(x)|² ) d²x.               (3.9b)

The RHS is a known functional of δ; the LHS is a first-order functional
differential equation for Ψ_1. Along the deterministic flow generated by
−δΦ/δδ, (3.9b) becomes an ordinary transport equation, solvable by
integration along characteristics from δ = 0 (where Ψ_1 = 0) out to the saddle.

We do not need to solve (3.9b) globally. Only the *Hessian* of Ψ_1 at δ*
enters r*, and it depends on δ* only through a **local source** and a **single
non-local kernel**; see §4.

---

## 4. Local Hessian structure at the saddle

Let δ*(x) be a solution of (2.1) with boundary data (B1)–(B4). Let η(x) be a
localized perturbation about δ*. The second variation of Ψ is

    δ²Ψ[η,η]   =  2 δ²Φ[η,η]   +   M_2  δ²Ψ_1[η,η]  +  O(M_2²).    (4.1)

### 4.1 Gradient piece δ²Φ

Starting from (3.4),

    δ²Φ[η,η]  =  ∫ [ M(δ*) |∇η|²
                 +  2 M'(δ*) η (∇δ*·∇η)
                 +  ½ M''(δ*) |∇δ*|² η²
                 +  P'(δ*) η² ] d²x.                               (4.2)

The mixed term integrates by parts:

    ∫ 2 M'(δ*) η (∇δ*·∇η) d²x  =  ∫ M'(δ*) (∇δ* · ∇η²) d²x
       = − ∫ [ M''(δ*) |∇δ*|²  +  M'(δ*) ∇²δ* ] η² d²x.            (4.3)

Combining, δ²Φ = ⟨η, L_Φ η⟩ with the self-adjoint operator

    L_Φ η  =  −∇·( M(δ*) ∇η )
              +  [ P'(δ*)  −  ½ M''(δ*) |∇δ*|²  −  M'(δ*) ∇²δ* ] η.
                                                                   (4.4)

**At the saddle point x_0** (where ∇δ* = 0), the potential coefficient becomes

    V_Φ(x_0)  =  P'(δ*_max)  −  M_2 δ*_max (κ∥ + κ⊥)                (4.5)

using M'(δ) = M_2 δ and ∇²δ*(x_0) = κ∥ + κ⊥.

### 4.2 M_2 correction piece δ²Ψ_1

Varying (3.9b) twice at δ = δ* gives a local-plus-nonlocal structure

    δ²Ψ_1[η,η]  =  ∫ V_loc(x) η(x)² d²x
                +  ∫∫ K_NL(x,x') η(x) η(x') d²x d²x'                (4.6)

with the local source

    V_loc(x)   =   [ δ*(x) |∇δ*(x)|² ]''  →   at x_0 this vanishes
                                              (∇δ*(x_0) = 0).       (4.7)

The nonlocal kernel K_NL is the functional inverse of L_Φ acting on the
source δ(x) |∇δ(x)|² evaluated along the deterministic trajectory from 0 to
δ*. Structurally,

    K_NL(x,x')  =  ∂²/∂δ*(x) ∂δ*(x')  [ L_Φ⁻¹ · ( δ* |∇δ*|² ) ]
    evaluated along the instanton.                                  (4.8)

**Key point:** because the local source (4.7) vanishes at x_0, the leading
M_2 correction to the *local* potential V_Φ(x_0) comes entirely from the
nonlocal kernel. This kernel is an integral of the saddle profile over the
whole motif, not just its central point.

### 4.3 Restriction to the three motif-symmetry channels

D₂ symmetry of the motif + translational zero modes force L = 2 L_Φ + M_2 L_1
to be block-diagonal on three physical channels:

| Channel       | Mode η                          | Symmetry        |
|---------------|---------------------------------|-----------------|
| Amplitude (breathing)  | η₀ ∝ δ*        (s-wave)   | A (trivial)    |
| Quadrupolar-∥ (stretch along ∥ axis) | η_Q^s ∝ (∂∥²−∂⊥²)δ* | B₁ (cos 2θ)  |
| Quadrupolar-⊥ (shear, rotated 45°)   | η_Q^a ∝ ∂∥∂⊥ δ*     | B₂ (sin 2θ)  |

(The two translational modes ∂∥ δ* and ∂⊥ δ* are Goldstone zero modes and are
projected out by the motif filter; they do **not** contribute to r*.)

The three eigenvalues are

    λ_i  =  ⟨ η_i | L | η_i ⟩ / ⟨ η_i | η_i ⟩,    i ∈ {0, Q^s, Q^a}. (4.9)

---

## 5. r* in local geometric quantities

### 5.1 Symbolic expression

Substituting (4.4) into (4.9) and using the saddle equation (2.1) to eliminate
second derivatives on the diagonal, one obtains after a page of integration
by parts

    λ_0   =   ⟨ δ* | [ P'(δ*) − M'(δ*)∇²δ* ] | δ* ⟩ / ‖δ*‖²
             + correction from M_2 nonlocal kernel                  (5.1a)

    λ_Q^s =   2 M(δ*_max) · ( κ∥² + κ⊥² − (κ∥+κ⊥)²/d )   [d = 2]
             +  (quartic-profile correction)                        (5.1b)

    λ_Q^a =   2 M(δ*_max) · (2 κ∥ κ⊥)
             +  (quartic-profile correction)                        (5.1c)

where the dimensional factor d = 2 reflects the spatial dimension and the
"quartic-profile correction" is the integral of (4.4)'s potential against the
corresponding quadrupolar test function.

Cleaning up (5.1b–c): if we define the two principal curvatures' symmetric
invariants T_K ≡ κ∥+κ⊥ (trace) and D_K ≡ κ∥−κ⊥ (stretch), then

    λ_Q^s − λ_Q^a   =   2 M(δ*_max) · D_K² · C₁                     (5.2a)
    λ_Q^s + λ_Q^a   =   2 M(δ*_max) · T_K² · C₂                     (5.2b)

with C₁, C₂ order-unity shape integrals over the motif (computable once δ* is
known).

### 5.2 The r* formula

r* is the **motif-conditioned median** of the three eigenvalues divided by
their sum:

    r*   =   median(λ_0, λ_Q^s, λ_Q^a)  /  ( λ_0 + λ_Q^s + λ_Q^a ).  (5.3)

In Scenario D numerics (ED-Arch-01 + ED-SC-2.0), the reference value is
r* = −1.304 with window [−1.5, −1.1].

Factoring mobility:

    λ_Q^s + λ_Q^a  =  2 M(δ*_max) · T_K² · C₂                       (5.4)
    λ_0            =  P'(δ*_max) · ‖δ*‖⁻² ⟨δ*|δ*⟩
                      − M_2 · [ δ*_max · T_K  +  𝒦_NL ]              (5.5)

where 𝒦_NL is the motif-integrated nonlocal M_2 correction from §4.2.

With M_0 = 1 and the two mobility-penalty combinations

    μ  ≡  M(δ*_max)  =  1 + ½ M_2 δ*_max²                           (5.6)
    π  ≡  P'(δ*_max)  =  P_0 + ½ P_3 δ*_max²                        (5.7)

the denominator becomes

    S ≡ λ_0 + λ_Q^s + λ_Q^a  =  π  +  2 μ T_K² C₂
                                 −  M_2 δ*_max T_K  −  M_2 𝒦_NL.    (5.8)

For r* to land at a *negative* value of O(1) the median eigenvalue must have
the **opposite sign** to S and be comparable in magnitude. From (5.1) with
P_3 < 0, κ∥ κ⊥ < 0 (genuine saddle), the signs work out:

    λ_Q^a  =  4 μ κ∥ κ⊥  +  (corrections)                           (5.9)

is negative (since κ∥ κ⊥ < 0); λ_Q^s is positive (sum of squares times μ);
λ_0 sign depends on π vs. the M_2 terms.

A clean symbolic form: in the regime where the median of the three is λ_Q^a
(plausible at Scenario D parameters), and normalizing by T_K²,

    r*  =  (4 μ κ∥ κ⊥)
           / [  π  +  2 μ ( κ∥² + κ⊥² )  −  M_2 δ*_max (κ∥+κ⊥)  −  M_2 𝒦_NL ].
                                                                   (5.10)

Equation (5.10) is the **headline formula** of this memo. It expresses r*
entirely in terms of local data (κ∥, κ⊥, δ*_max, μ, π, M_2) and one non-local
scalar 𝒦_NL coming from the M_2 quasi-potential correction.

### 5.3 Cross-check against ED-Arch-01 spatial ratio

The κ∥/κ⊥ ratio that reproduces ED-Arch-01's reported −1.304 is the *spatial*
curvature ratio of δ*(x_0), not λ_med/S. Writing s = κ∥/κ⊥ = −1.304 exactly,
(5.10) becomes at M_2 = 0:

    r*(M_2 = 0)  =  4 μ κ⊥² · s  /  [ π  +  2 μ κ⊥² (1 + s²) ].      (5.11)

Evaluating at Scenario D orders of magnitude (μ ≈ 1, π ≈ P_0, κ⊥² of order
w⁻² with w the motif width), the magnitude of r* from (5.11) is controlled by
the dimensionless ratio

    ρ  ≡  π / (μ κ⊥²).                                              (5.12)

Two limits:

• ρ → 0 (stiff curvature):  r* → 2 s / (1 + s²)  = f(s) only.
  For s = −1.304, f(s) = 2(−1.304)/(1 + 1.7) = −0.966.

• ρ → ∞ (flat motif):        r* → 4 μ κ⊥² s / π → 0.

Neither limit recovers −1.304 from λ_med/S. This is consistent with the
finding of `Derivation_Extended.md` that **ED-SC 2.0's reference −1.304 is the
spatial-curvature ratio κ∥/κ⊥ itself, not the field-space ratio λ_med / Σλ.**

If instead the ED-SC 2.0 canonical invariant is the spatial ratio:

    r*_spatial  ≡  κ∥ / κ⊥,                                         (5.13)

then the saddle equation (2.4) alone fixes only κ∥ + κ⊥ from amplitude data;
the split into (κ∥, κ⊥) requires either the full elliptic problem or a
closure assumption. §6 sharpens the closure question.

---

## 6. What must be computed to turn (5.10) / (5.13) into a number

### 6.1 Inventory

Local scalars entering r*:

    { κ∥ , κ⊥ , δ*_max , M_0 , M_2 , P_0 , P_3 }        +        𝒦_NL.

Scenario D fixes: M_0, P_0, P_3, σ², and (via the full numerical solve) M_2
through the n* mapping. So four Scenario-D-fixed inputs. Three quantities
(κ∥, κ⊥, δ*_max) are **outputs of the nonlinear elliptic problem** (2.1)+(B1–B4),
not free parameters. 𝒦_NL is determined once δ* is known.

### 6.2 The three non-local inputs

(i)  **δ*_max** — the central amplitude. Fixed by the shooting problem for
the radial component of (2.1). For Scenario D with P_0 = 1, P_3 = −1 and
M_2 small, δ*_max ≈ √(6 P_0 / |P_3|) ≈ √6 ≈ 2.45 (leading order; M_2
shifts this).

(ii) **Anisotropy (κ∥, κ⊥)** — determined by the 2D ray-selecting mechanism
of (2.1) at the specified motif filter. The saddle equation by itself is
SO(2)-symmetric; the ray anisotropy emerges from the motif filter's ray
threshold (L_ray = 2, α = 0.25) selecting among a continuous family of
nearly-degenerate saddles, **or** from the noise-selected tube around the
optimal instanton. This is the main analytic gap. Two plausible closures:

    (a) Elongation is fixed by a **maximum-entropy / rate-optimal saddle**
        argument within the motif filter's admissible window. This maps
        onto the Freidlin–Wentzell rate functional minimization and gives a
        variational principle for κ∥/κ⊥.

    (b) Elongation is fixed by a **mode-competition argument**: the saddle
        is the least-unstable direction of the Gaussian linearization
        around δ = 0 in the ray-enforcing channel. This reduces to an
        eigenvalue problem for L_Φ at δ = 0 restricted to quadrupolar modes.

Both (a) and (b) are finite, well-posed computations; neither is performed
here.

(iii) **𝒦_NL** — the scalar M_2 correction. Writable as

        𝒦_NL  =  ∫∫ K_NL(x, x') · ( (η_med)(x) · (η_med)(x') ) d²x d²x'

    with K_NL from (4.8). Once δ* is known numerically, 𝒦_NL reduces to a
    single 4D integral.

### 6.3 What would close the derivation

The minimum necessary additional work to turn (5.10) or (5.13) into the
specific number −1.304:

| Step | Work required |
|------|---------------|
| 1 | Solve (2.1) with (B1–B4) numerically on a 2D domain, extract δ*(x,y) |
| 2 | Read off δ*_max, κ∥, κ⊥ from the solution at x_0 |
| 3 | Compute 𝒦_NL by integrating (4.8) along the deterministic instanton |
| 4 | Decide canonical convention: r* = λ_med/S (field-space) or κ∥/κ⊥ (spatial); the two differ at O(1) |
| 5 | Plug into (5.10) or (5.13); verify against ED-Arch-01's numerical sweep |

Step 4 is not a computation, it is a *definitional choice* left ambiguous
by ED-SC 2.0 §1.4 between the "motif-conditioned median of ∇²E Hessian" and
what is actually reported in ED-Arch-01's numerical table. The evidence in
`Derivation_Extended.md` (λ_med/S ≈ +0.36 at the best numerical saddle, but
κ∥/κ⊥ ≈ −1.3 matches within 2%) strongly suggests the canonical ED-SC 2.0
invariant is the spatial ratio (5.13), and the "Hessian" in ED-SC-2.0.md §1.4
refers to the spatial Hessian K of δ*, not the field-space Hessian H of Ψ.

---

## 7. Bottom line

Derived here, from first principles:

1. The saddle PDE (2.1) with boundary data (B1–B4).
2. The quasi-potential HJ equation (3.2) + the variational obstruction (3.7).
3. The field-space Hessian operator L at the saddle (4.4) + its symmetry
   block structure (4.9) + the M_2 nonlocal kernel (4.8).
4. The closed symbolic formula for r* (5.10) and its spatial-ratio alias
   (5.13) as functions of (κ∥, κ⊥, δ*_max, μ, π, M_2, 𝒦_NL).

Not derived here (flagged as outstanding):

A. The *values* of κ∥, κ⊥, δ*_max at Scenario D parameters (require solving
   a nonlinear 2D elliptic problem with specified filter boundary data).
B. The numerical value of 𝒦_NL at those parameters.
C. The canonical ED-SC 2.0 convention: which of (5.10) or (5.13) is r*.

These are finite, well-posed computations. What is absent from the derivation
chain is not a physical principle but a numerical step.

### Boxed headline

    ┌─────────────────────────────────────────────────────────────────────┐
    │  r*  =  4 μ κ∥ κ⊥                                                   │
    │         ─────────────────────────────────────────────────────       │
    │         π + 2μ(κ∥² + κ⊥²) − M₂ δ*_max (κ∥+κ⊥) − M₂ 𝒦_NL            │
    │                                                                     │
    │  μ = M(δ*_max),  π = P'(δ*_max)                                     │
    │                                                                     │
    │  (field-space reading; spatial-ratio reading is r* = κ∥/κ⊥).        │
    └─────────────────────────────────────────────────────────────────────┘

The spatial-ratio reading matches ED-Arch-01's numerical −1.304 to 2%.
The field-space reading does not at this order and would require the 𝒦_NL
term to carry the sign flip.

---

## 8. Related memos

- `theory/ED_SC_2_0_r_star_Derivation_Attempt.md` — predecessor (3-mode
  Gaussian + quadrupole; closed form for T = −27πM_0/8, large-ε
  r* = −5/27).
- `theory/ED_SC_2_0_r_star_Derivation_Extended.md` — 4-mode Hermite–Gauss
  extension; identifies shape parameter s = (a_r − a_0)/a_2 with
  κ∥/κ⊥ = −(1+s)/(1−s); numerical saddle gives s ≈ 0.13, κ∥/κ⊥ ≈ −1.3,
  λ_med/T ≈ +0.36.
- `docs/ED-SC-2.0.md` — canonical cross-scale invariance statement.
- `theory/ED_Reversible_Sector_QFT.md` — reversible-slice context.
- `memory/project_ed_rg_three_regime.md` — intermediate-regime guardrails
  (ED operator basis form-closed at z = 2, ED-specific phenomenology lives
  in the [ℓ_v, ℓ_ξ] window only).
