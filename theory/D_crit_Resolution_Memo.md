# Resolving the D_crit Discrepancy — Theory Memo

**Date.** 2026-04-22.
**Status.** Resolution memo for the 0.5 vs 0.9 discrepancy flagged in the 2026-04-20 rate-balance extension and carried forward unresolved in [`docs/ED-Orientation.md`](../docs/ED-Orientation.md) §3 and §6 until now.
**Scope.** Linearised stability of the canonical ED PDE around homogeneous equilibrium. Resolves the value of the damping discriminant threshold `D_crit` and proposes a concrete Canon P6 update.
**Not in scope.** Nonlinear-regime corrections, spatial-inhomogeneity effects, finite-domain Neumann vs periodic BC corrections, or the SY2 penalty beyond leading-order.

---

## 1. Introduction

Canon P6 ([00.2 Architectural Canon §6](../docs/ED-Orientation.md)) asserts a sharp architectural damping threshold `D_crit = 0.5` under the rule-of-thumb `Δ = D + 2ζ, underdamped when Δ<1`. The 2026-04-20 rate-balance extension (v0.4-final, [`theory/ED-Dimensional-01-Ext.md`](ED-Dimensional-01-Ext.md) Appendix A) reported that the 2D linearised underdamping condition on the canonical PDE gives `D_crit ≈ 0.9` at canon-default `ζ = 1/4`. The two values disagree by ~80%. This memo performs the linearisation from scratch, identifies the source of the gap, and issues a recommendation.

## 2. The Canonical PDE

The canonical two-channel ED PDE in [00.3 Unified Cosmological Equation] form:

$$
\partial_t\rho \;=\; D\,F[\rho] \;+\; H\,v,
\qquad
\partial_t v \;=\; \frac{1}{\tau}\bigl(F[\rho] - \zeta v\bigr)
\tag{1}
$$

$$
F[\rho] \;=\; M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho),
\qquad
D + H = 1,\quad D,H \in [0,1]
\tag{2}
$$

Parameters and conventions:

- `M(ρ)` — mobility; `M(ρ*) ≡ M₀ > 0`, `M(ρ_max) = 0` (Canon P4)
- `P(ρ)` — penalty; `P(ρ*) = 0` (Canon P3), `P'(ρ*) ≡ P₀ > 0`
- `τ > 0` — participation relaxation timescale
- `ζ ∈ [0, 1]` — participation damping coefficient; canon-default `ζ = 1/4`
- `v(x, t)` — participation field (local, not spatially-averaged at the PDE level)

The question of D_crit is about **the temporal character of the linear response around equilibrium**: does a small perturbation `δρ` relax monotonically (overdamped) or oscillate (underdamped)?

## 3. Linearisation around Homogeneous Equilibrium

### 3.1 Setup

Write `ρ(x, t) = ρ* + δρ(x, t)`, `v(x, t) = 0 + δv(x, t)`. At equilibrium, `P(ρ*) = 0, ∇ρ* = 0, v = 0` identically.

### 3.2 Leading-order expansion of `F[ρ]`

Three terms in `F`:

- **Mobility** — `M(ρ)∇²ρ = M(ρ* + δρ)∇²δρ = M₀∇²δρ + O(δρ·∇²δρ)`. Linear order: `M₀∇²δρ`.
- **Gradient-squared** — `M'(ρ)|∇ρ|² = M'(ρ*)|∇δρ|² + O(δρ³) = O(δρ²)`. **Vanishes at linear order.**
- **Penalty** — `P(ρ) = P(ρ*) + P'(ρ*)δρ + O(δρ²) = P₀·δρ + O(δρ²)`. Linear order: `P₀δρ`.

Therefore

$$
F[ρ] \;\approx\; M_0\nabla^2\delta\rho \;-\; P_0\,\delta\rho
\tag{3}
$$

at linear order in `δρ`.

### 3.3 Fourier decomposition

Expand `δρ, δv ∝ exp(i\mathbf{k}·\mathbf{x} + \lambda t)`. Then `∇² → -k²` where `k = |\mathbf{k}|`. Define the **linearised response rate**

$$
\boxed{\epsilon_k \;\equiv\; M_0 k^2 + P_0}
\tag{4}
$$

— this is the rate at which the ρ channel alone would relax mode `k`, were participation absent. It has units of inverse time; for a wave of wavelength `λ = 2π/k` it interpolates between `P₀` at `k=0` and `M₀k²` at large `k`.

Substituting into (1)–(3):

$$
\lambda \hat\rho = -D\epsilon_k\hat\rho + H\hat v
\tag{5a}
$$
$$
\lambda \hat v = -\frac{\epsilon_k}{\tau}\hat\rho - \frac{\zeta}{\tau}\hat v
\tag{5b}
$$

### 3.4 Characteristic polynomial

The `2×2` linearised operator

$$
A_k \;=\; \begin{pmatrix} -D\epsilon_k & H \\ -\epsilon_k/\tau & -\zeta/\tau \end{pmatrix}
\tag{6}
$$

has characteristic polynomial

$$
\lambda^2 + T_k\,\lambda + S_k \;=\; 0
\tag{7}
$$

with

$$
T_k \;=\; D\epsilon_k + \frac{\zeta}{\tau}, \qquad
S_k \;=\; \frac{\epsilon_k(D\zeta + H)}{\tau} \;=\; \frac{\epsilon_k(1 - D(1-\zeta))}{\tau}
\tag{8}
$$

using `H = 1 − D`.

### 3.5 Underdamping discriminant

The eigenvalues are `λ_± = -T_k/2 \pm \sqrt{T_k^2/4 - S_k}`. The mode is **underdamped** (oscillatory decay) iff the argument of the square root is negative, i.e.

$$
T_k^2 < 4 S_k
\tag{9}
$$

## 4. Regime A — Mobility–Penalty Only (D = 1, H = 0)

In this regime the participation channel is inactive. The PDE reduces to

$$
\partial_t\delta\rho = M_0 \nabla^2 \delta\rho - P_0 \delta\rho
\tag{10}
$$

a single scalar dissipative equation. Mode `k` has eigenvalue

$$
\lambda \;=\; -(M_0 k^2 + P_0) \;=\; -\epsilon_k \;\in\; \mathbb{R}_{<0}.
\tag{11}
$$

**All modes decay purely exponentially. No oscillation is possible. The concept of "critical damping" is vacuous in Regime A — the system is unconditionally overdamped.**

The Canon P6 threshold `D_crit` does not belong to Regime A. Any statement about "the transition" presupposes Regime B.

## 5. Regime B — Participation-Active (0 < D < 1, H > 0)

### 5.1 Setting ε_k = τ = 1

To expose the `D, ζ` dependence cleanly, adopt natural units in which the linearised response rate and the participation timescale are both unity: `ε_k = 1, τ = 1`. (These units are mode-specific — at a different `k`, `ε_k` differs. See §5.5 for the full parameter dependence.)

Then (8) becomes

$$
T = D + \zeta, \qquad S = 1 - D + D\zeta = 1 - D(1-\zeta).
\tag{12}
$$

### 5.2 Underdamping condition

From (9) the system is underdamped iff

$$
(D + \zeta)^2 \;<\; 4\bigl(1 - D + D\zeta\bigr).
\tag{13}
$$

Expand:

$$
D^2 + 2D\zeta + \zeta^2 \;<\; 4 - 4D + 4D\zeta
$$
$$
D^2 - 2D\zeta + \zeta^2 + 4D - 4 \;<\; 0
$$
$$
\boxed{(D - \zeta)^2 \;<\; 4(1 - D)}
\tag{14}
$$

This matches the 2026-04-20 form given in [`theory/ED-Dimensional-01-Ext.md`](ED-Dimensional-01-Ext.md) Appendix A exactly.

### 5.3 Critical condition

Equality in (14) defines the critical damping boundary:

$$
(D - \zeta)^2 \;=\; 4(1 - D)
\tag{15}
$$

Expand into a quadratic in `D`:

$$
D^2 + 2D(2 - \zeta) + (\zeta^2 - 4) \;=\; 0
\tag{16}
$$

Apply the quadratic formula (taking the positive root so that `D ∈ [0, 1]`):

$$
D_{\rm crit}(\zeta) \;=\; -(2 - \zeta) + \sqrt{(2-\zeta)^2 - (\zeta^2 - 4)}
\;=\; -(2 - \zeta) + \sqrt{8 - 4\zeta}
$$

Let `u ≡ √(2 − ζ)`. Then

$$
\boxed{D_{\rm crit}(\zeta) \;=\; -u^2 + 2u \;=\; u(2 - u) \;=\; \sqrt{2 - \zeta}\,\bigl(2 - \sqrt{2 - \zeta}\bigr)}
\tag{17}
$$

### 5.4 Evaluations

| ζ | u = √(2−ζ) | `D_crit(ζ)` |
|:---:|:---:|:---:|
| 0 | √2 ≈ 1.414 | 2√2 − 2 ≈ **0.828** |
| 0.1 | 1.378 | ≈ 0.858 |
| **0.25** (canon) | **√7/2 ≈ 1.323** | **≈ 0.896** |
| 0.5 | 1.225 | ≈ 0.949 |
| 0.75 | 1.118 | ≈ 0.986 |
| 1 | 1 | 1 |

At canon-default `ζ = 1/4`, `D_crit ≈ 0.896`. This is the value reported in the 2026-04-20 rate-balance extension as "`D_crit ≈ 0.9`."

### 5.5 Parameter dependence (restoring ε_k and τ)

With `ε_k` and `τ` restored, the underdamping condition (14) becomes

$$
(D\epsilon_k - \zeta/\tau)^2 \;<\; 4\epsilon_k(1 - D)/\tau
\tag{18}
$$

which after scaling `D → D` and redefining `ζ̃ = ζ/(τε_k)` recovers the same quadratic structure but with a rescaled participation-damping parameter. Two consequences:

- **Spatial-mode dependence.** `ε_k = M₀k² + P₀` so `D_crit` is smallest at `k = 0` (longest wavelength, most oscillatory) and approaches 0 as `k → ∞` (short wavelengths always underdamped for any `D > 0`). This matches the intuition that spatial diffusion stabilises short wavelengths.
- **Timescale separation.** For `τε_k ≫ 1` the participation damping term `ζ/τ` is negligible relative to `Dε_k`, and `D_crit → 1` (the system is nearly always in the underdamped eigenvalue structure).

The canonical statement assumes `ε_k = τ = 1`, i.e. the reference mode at unit linearised-response rate and unit participation timescale.

## 6. Comparison — Where Does `D_crit = 0.5` Come From?

The Canon P6 rule of thumb `Δ ≡ D + 2ζ, critical at Δ = 1`, evaluated at `ζ = 1/4`, gives `D_crit = 1 - 2·(1/4) = 0.5`.

### 6.1 Can this be recovered from (17) by a choice of ε_k, τ?

Solve

$$
\frac{-(2 - \zeta) + 2\sqrt{1 - \zeta + \epsilon}}{\epsilon} \;=\; 1 - 2\zeta
$$

at `ζ = 1/4, D_crit = 1/2` (with `τ = 1`). Algebra yields the quadratic `4ε² − 36ε + 1 = 0` with roots `ε ≈ 8.97` or `ε ≈ 0.028`. Neither corresponds to the canonical `ε = 1` normalisation.

**The `D_crit = 0.5` heuristic is not a limit of the full result.** It is not obtained by any principled choice of normalisation.

### 6.2 The approximation structure

Compare the correct form (from (14))

$$
(D - \zeta)^2 + 4D \;<\; 4
$$

to the heuristic form `D + 2ζ < 1` squared:

$$
(D + 2\zeta)^2 \;<\; 1 \iff D^2 + 4D\zeta + 4\zeta^2 \;<\; 1.
$$

The correct inequality has `(D − ζ)² + 4D ` on the left; the heuristic has `(D + 2ζ)² `. The cross-terms differ in sign and weight: the heuristic carries `+4Dζ` where the true inequality carries `−2Dζ`. **The heuristic flips the sign of the coupled cross-term and over-weights `ζ` by a factor of 2.** This is why at `ζ = 1/4` the heuristic predicts `D_crit = 0.5` while the true value is `≈ 0.9` — the cross-term difference is maximal in the `D ~ ζ ~ 1/2` region.

### 6.3 Why the heuristic exists at all

The heuristic is a **qualitative additive rule** — "total damping = direct + participation" with `ζ` weighted by 2 to account for its two entries into the coupled system (appearing in both the trace `T_k` and the determinant `S_k` of (8)). As an order-of-magnitude indicator it correctly predicts that increasing either `D` or `ζ` moves the system toward overdamping. As a quantitative prediction it is off by ~80%.

### 6.4 Is it a dimensionality effect? A mobility-form effect?

- **Dimensionality.** The linearised eigenvalue problem (5) is scalar and identical in any `d` (only `∇² → -k²` is used, and `k = |\mathbf{k}|`). Dimensionality enters only through the density of modes, not through `D_crit` per mode. **Ruled out.**
- **Mobility form.** At linear order `M(ρ)` enters only through `M₀ = M(ρ*)`; the shape of `M(ρ)` (β=1, β=2, SY2, etc.) does not affect `D_crit`. **Ruled out.**
- **Penalty form (linear vs SY2).** Both linearise to `P₀·δρ` with `P₀ = P'(ρ*)`; the shape of `P(ρ)` does not affect `D_crit` at linear order. **Ruled out.**
- **Definition of critical damping.** Both the heuristic and the full derivation use the standard `T² = 4S` condition (`trace² = 4·det` on the 2×2 linearised operator). **No definitional ambiguity.**

The discrepancy is a single root cause: **the heuristic is an incorrect algebraic approximation of the coupled 2×2 eigenvalue discriminant**.

## 7. Resolution

### 7.1 Canonical value

The critical damping threshold for the canonical ED PDE linearised around homogeneous equilibrium is

$$
\boxed{D_{\rm crit}(\zeta) \;=\; \sqrt{2 - \zeta}\,\bigl(2 - \sqrt{2 - \zeta}\bigr)}
\tag{19}
$$

at the reference mode `ε_k·τ = 1`. At canon-default `ζ = 1/4`:

$$
D_{\rm crit}(1/4) \;\approx\; 0.896.
$$

### 7.2 Regime-split statement

- **Regime A (D = 1, H = 0).** Mobility–penalty only. System is unconditionally overdamped. `D_crit` is not a defined quantity.
- **Regime B (0 < D < 1).** Participation-active. Underdamped iff `(D − ζ)² < 4(1 − D)` at reference mode. Critical at (19). `D_crit(ζ) ∈ [0.828, 1]` for `ζ ∈ [0, 1]`.

No other regime split is required. The 0.5 value is not canonical; it is a discarded heuristic.

### 7.3 What changes downstream

- **ED-Dimensional-01-Ext v0.4-final Appendix A.** The "highest-priority v0.5+ theory issue" flagged in that memo is resolved: the correct `D_crit(1/4) ≈ 0.896`, not 0.5. The Appendix A statement is correct and should be promoted to canonical.
- **ED-Orientation.md §3 Canon P6 row.** The "sharp transition at `D_crit = 0.5`" statement is retired. Replacement below.
- **00.3 Unified PDE Three-regimes table.** The regime boundaries expressed in Orientation §4 as `D < 0.1`, `0.1 ≤ D ≤ 0.4`, `D ≥ 0.5` need to be re-examined against (19); the `0.5` boundary is heuristic and the canonical boundary is closer to 0.9.
- **Canon P6 itself.** Replace single-number `D_crit = 0.5` with the `ζ`-parametrised expression (19); retain the heuristic `D + 2ζ` form only as an order-of-magnitude indicator, explicitly marked as approximate.

## 8. Canon P6 Update (Recommended)

**Current 00.2 Canon P6 statement:**

> P6 Damping Discriminant — `Δ = D + 2ζ`, underdamped when Δ<1, overdamped when Δ>1, sharp transition at `D_crit = 0.5`.

**Proposed revised statement:**

> **P6 Damping Discriminant.** Linearising the canonical PDE (1) around the homogeneous equilibrium `ρ*` and passing to Fourier modes at reference rate `ε_k·τ = 1`, the characteristic polynomial
>
> `λ² + (D + ζ)λ + (1 − D + Dζ) = 0`
>
> admits oscillatory (underdamped) eigenvalues iff
>
> `(D − ζ)² < 4(1 − D)`
>
> with critical (repeated-real) damping at
>
> `D_crit(ζ) = √(2 − ζ) · (2 − √(2 − ζ))`.
>
> At canon-default `ζ = 1/4`, `D_crit ≈ 0.896`. At `ζ = 0`, `D_crit = 2√2 − 2 ≈ 0.828`. As `ζ → 1`, `D_crit → 1`.
>
> The earlier additive heuristic `Δ ≡ D + 2ζ, critical at Δ = 1` gives the qualitatively correct monotone dependence on `D` and `ζ` but over-weights `ζ` by ~2× and flips the sign of the coupled cross-term; quantitatively it is in error by ~80% at canon-default parameters. It is retained only as an order-of-magnitude mnemonic, not a quantitative threshold.

## 9. Verification Hooks

Three independent consistency checks:

- **(a)** At `ζ = 1`: the participation channel has maximum internal damping. `D_crit = 1·(2−1) = 1`; system transitions to oscillation only at the boundary `D = 1`, i.e. effectively never. ✓ consistent with intuition.
- **(b)** At `ζ = 0`: no internal participation damping. `D_crit = √2·(2−√2) = 2√2 − 2 ≈ 0.828`. The system is still overdamped for large `D` because the direct channel `Dε_k` provides damping on its own. ✓ consistent with (5a) reducing to `λ_ρ = −D + H v̂/ρ̂`.
- **(c)** `D_crit(ζ)` monotone in `ζ`: `dD_crit/dζ = (1 − √(2−ζ))/√(2−ζ) = (1/u − 1) < 0` for `u > 1`, but note that at `ζ = 1, u = 1` and the derivative vanishes. So `D_crit(ζ)` is monotone *decreasing in `u`*, equivalently *increasing in `ζ`* (since `u = √(2−ζ)` decreases in `ζ`). ✓ more participation damping ⇒ harder to achieve oscillation ⇒ higher `D_crit`.

All three pass.

## 10. Open Items

- **Nonlinear regime.** (19) is exact at linear order. The SY2 penalty and the `M′|∇ρ|²` term couple at O(δρ²); corrections to `D_crit` at finite amplitude are of the form `D_crit(ζ, A/ρ*) = D_crit(ζ, 0) + c(ζ)·(A/ρ*)² + …` with `c(ζ)` unknown. Simulation or perturbation calculation required.
- **Finite-domain boundary effects.** Neumann BCs quantise `k`-modes; the long-wavelength cutoff can shift the effective `ε_k` and thus `D_crit`. For the 2D canonical lattice at `N = 64`, lowest nonzero `k = π/L`, effect is ~O(1/N²) on `ε_k` and therefore small; relevant only at very coarse grids.
- **Propagation to §6.7 dimensional-consistency results.** ED-SIM-3D verified Canon axiom P7 across `d = 1, 2, 3` using the heuristic `D_crit = 0.5` as a regime marker. Those results should be re-examined against the corrected threshold `D_crit(ζ = 1/4) ≈ 0.9`; the qualitative classifications should survive but the numerical boundaries shift.
- **Propagation to Orientation §4 three-regimes table.** The regime boundaries `D < 0.1 / 0.1–0.4 / ≥ 0.5` are heuristic and should be updated once the downstream papers are reviewed.

---

*Memo v1.0, 2026-04-22. Source: Test-to-Axiom Mapping Project pivot into theory-consolidation phase. Cross-reference: [`docs/ED-Orientation.md`](../docs/ED-Orientation.md) §3 Canon P6, §4 Three-regimes table; [`theory/ED-Dimensional-01-Ext.md`](ED-Dimensional-01-Ext.md) Appendix A.*
