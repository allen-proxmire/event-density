# IR Effective PDE of ED

**Date.** 2026-04-22 (ninth pass).
**Scope.** Explicit derivation of the IR-limit PDE of canonical ED, using the RG result `τ(b) → 0, ζ(b) → ∞, P_0(b) → ∞` established in [`ED_RG_Flow_Analysis.md`](ED_RG_Flow_Analysis.md) and [`ED_RG_Flow_Geometry.md`](ED_RG_Flow_Geometry.md).

---

## 1. Starting system

$$\partial_t \delta \;=\; D\,F[\delta] \;+\; H\,v, \qquad \tau\,\dot v \;=\; F[\delta] \;-\; \zeta\,v, \qquad D + H = 1.$$

$$F[\delta] \;=\; \nabla\!\cdot\!\bigl(M(\delta)\nabla\delta\bigr) \;-\; P(\delta) \;=\; M(\delta)\,\nabla^2\delta + M'(\delta)\,|\nabla\delta|^2 - P(\delta).$$

Z₂-symmetric expansions:

$$M(\delta) \;=\; M_0 + \tfrac{1}{2}M_2\,\delta^2 + \mathcal{O}(\delta^4), \qquad P(\delta) \;=\; P_0\,\delta + \tfrac{1}{6}P_3\,\delta^3 + \mathcal{O}(\delta^5).$$

Full expanded form of `F[δ]`:

$$F[\delta] \;=\; M_0\,\nabla^2\delta \;+\; \tfrac{1}{2}M_2\,\delta^2\,\nabla^2\delta \;+\; M_2\,\delta\,|\nabla\delta|^2 \;-\; P_0\,\delta \;-\; \tfrac{1}{6}P_3\,\delta^3 \;+\; \mathcal{O}(\delta^4\nabla^2\delta).$$

---

## 2. IR limit of the participation ODE

From the RG flow:

$$\tau(b) \;=\; \tau\,b^{-2} \;\xrightarrow[b\to\infty]{}\; 0, \qquad \zeta(b) \;=\; \zeta\,b^{+2} \;\xrightarrow[b\to\infty]{}\; \infty, \qquad P_0(b) \;=\; P_0\,b^{+2} \;\xrightarrow[b\to\infty]{}\; \infty.$$

In the `τ → 0` limit of the ODE:

$$\tau\,\dot v \;=\; F[\delta] - \zeta\,v \;\;\xrightarrow[\tau\to 0]{}\;\; 0 \;=\; F[\delta] - \zeta\,v \;\;\Longrightarrow\;\; \boxed{\;v \;=\; \frac{F[\delta]}{\zeta}.\;}$$

The participation variable is **algebraically slaved** to `F[δ]`. The `v`-ODE disappears as an independent dynamical equation.

**Leading non-vanishing correction.** If one retains `τ` to first order in small `τ`, the slaving becomes

$$v \;=\; \frac{F[\delta]}{\zeta} \;-\; \frac{\tau}{\zeta^2}\,\partial_t F[\delta] \;+\; \mathcal{O}(\tau^2).$$

Both correction terms are suppressed by `\tau/\zeta^2 \sim b^{-6}` under the joint flow and are dropped in the strict IR.

---

## 3. Slaved substitution and effective mobility

Substituting the slaved `v` into the `δ`-equation:

$$\partial_t\delta \;=\; D\,F[\delta] \;+\; H\cdot\frac{F[\delta]}{\zeta} \;=\; \Bigl(D + \frac{H}{\zeta}\Bigr)F[\delta].$$

Define

$$\boxed{\;\Gamma_{\text{eff}} \;:=\; D + \frac{H}{\zeta}.\;}$$

Behaviour under RG:

$$\Gamma_{\text{eff}}(b) \;=\; D + \frac{H}{\zeta(b)} \;=\; D + \frac{H}{\zeta\,b^2} \;\xrightarrow[b\to\infty]{}\; D.$$

- **Intermediate scales** (`ℓ_v < ℓ < ℓ_ξ`, participation slaved but `ζ` finite): `Γ_eff = D + H/ζ`, enhanced above the direct channel alone.
- **Deep IR** (`ℓ → ∞`): `Γ_eff → D`. The participation channel's enhancement vanishes because `ζ` grows unboundedly. The single remaining coefficient is the bare direct-channel weight `D`.

Since `D + H = 1` with `D, H ∈ [0, 1]`, `Γ_eff` ranges from `D` (deep IR) to `D + H = 1` (marginal IR, `ζ = H`). In both cases `Γ_eff ∈ [D, 1] \subset (0, 1]` and non-zero.

---

## 4. Operator expansion under IR scaling

The slaved-substitution PDE:

$$\partial_t\delta \;=\; \Gamma_{\text{eff}}\Bigl[\,M_0\,\nabla^2\delta \;+\; \tfrac{1}{2}M_2\,\delta^2\,\nabla^2\delta \;+\; M_2\,\delta\,|\nabla\delta|^2 \;-\; P_0\,\delta \;-\; \tfrac{1}{6}P_3\,\delta^3 \;+\; \cdots\,\Bigr].$$

Apply the tree-level scaling dimensions at `z = 2` (see [`ED_RG_Flow_Analysis.md`](ED_RG_Flow_Analysis.md) §5):

| Operator | Coupling | Dimension `λ` | Scaling under `b → ∞` |
|:---|:---|:---:|:---|
| `M_0\nabla^2\delta` | `M_0` | 0 | **marginal** — survives |
| `-P_0\delta` | `P_0` | +2 | **relevant** — grows |
| `-\tfrac{1}{6}P_3\delta^3` | `P_3` | `2−2χ` | rel. (χ<1), marg. (χ=1), irrel. (χ>1) |
| `\tfrac{1}{2}M_2\delta^2\nabla^2\delta` | `M_2` | `−2χ` | rel. (χ<0), marg. (χ=0), irrel. (χ>0) |
| `M_2\delta|\nabla\delta|^2` | `M_2` | `−2χ` | rel. (χ<0), marg. (χ=0), irrel. (χ>0) |

### 4.1 Field-amplitude suppression in deep IR

Independent of the RG scaling eigenvalues, the physical amplitude `δ(x, t)` itself decays in the IR:

At `ℓ > ℓ_ξ = \ln(\xi\Lambda)`: the linear-penalty term `-Γ_eff P_0(\ell)\delta` drives `δ → 0` pointwise exponentially, at rate `Γ_eff P_0(\ell) \to \infty`. Therefore

$$|\delta| \;\xrightarrow[\ell \to \infty]{}\; 0,$$

and all operators `\mathcal{O}(\delta^k)` with `k \ge 2` become subdominant to the linear operator `\mathcal{O}(\delta)`. Specifically:

$$\frac{|P_3\,\delta^3|}{|P_0\,\delta|} \;=\; \frac{P_3}{P_0}\,\delta^2 \;\xrightarrow{\delta\to 0}\; 0, \qquad \frac{|M_2\,\delta^2\,\nabla^2\delta|}{|M_0\,\nabla^2\delta|} \;=\; \frac{M_2}{M_0}\,\delta^2 \;\xrightarrow{\delta\to 0}\; 0, \qquad \frac{|M_2\,\delta|\nabla\delta|^2|}{|M_0\,\nabla^2\delta|} \;\xrightarrow{\delta\to 0}\; 0.$$

All Z₂-even `M_2` terms and the cubic `P_3` term drop out in the IR asymptotic, *regardless of the χ-choice for their RG eigenvalue*.

### 4.2 Surviving operators

After both (i) RG scaling and (ii) amplitude suppression:

- `\nabla^2\delta` with coefficient `Γ_eff M_0 \to D M_0` — marginal, field-linear, survives.
- `\delta` with coefficient `-Γ_eff P_0(\ell) \to \text{blowing up}` — relevant, field-linear, dominates.

Everything else is eliminated — either by RG irrelevance, by χ-dependent suppression, or by field-amplitude vanishing.

---

## 5. The IR effective PDE

### 5.1 Closed form

$$\boxed{\;\partial_t\delta \;=\; D\,M_0\,\nabla^2\delta \;-\; D\,P_0(\ell)\,\delta \;\;\bigl(\ell \gg \ell_v,\; \delta\to 0\bigr), \qquad P_0(\ell) \to \infty.\;}$$

### 5.2 Equivalent form: linear gapped diffusion

Introduce the running mass `m^2(\ell) := P_0(\ell)/M_0 = (1/\xi^2(\ell)) \to \infty`:

$$\partial_t\delta \;=\; D\,M_0\bigl(\nabla^2 - m^2(\ell)\bigr)\,\delta.$$

This is the **linear, gapped, single-channel diffusion equation** with mass gap `m^2(\ell) \to \infty`.

### 5.3 Solution

For any bounded initial condition `δ(x, 0)`:

$$\delta(x, t) \;=\; e^{-D M_0 m^2(\ell)\,t}\,\bigl[\,e^{D M_0\,t\,\nabla^2}\,\delta(x, 0)\,\bigr].$$

At asymptotic IR times `t \gg 1/(D M_0 m^2)`:

$$\delta(x, t) \;\xrightarrow{t\to\infty}\; 0 \quad\text{pointwise, exponentially.}$$

### 5.4 Operator content

Exactly two operators in the final IR PDE:

1. `\nabla^2\delta` — dissipative Laplacian (linear mobility).
2. `-\delta` — linear relaxation to equilibrium (linear penalty).

Zero nonlinearities. Zero participation. Zero higher-derivative. Zero cross-coupling.

### 5.5 Physical meaning

Every fluctuation of `δ` around the equilibrium `ρ*` decays to zero exponentially in the IR. The correlation length `\xi(\ell) = 1/m(\ell) \to 0` means **no spatial structure survives at sufficiently long wavelengths**: ED at `ℓ \gg ℓ_ξ` is in the **disordered / trivial / gapped phase** of the Model-A universality class.

---

## 6. Summary

### 6.1 What ED becomes in the IR

$$\text{Full ED (UV)} \;\;\xrightarrow{\ell = \ell_v}\;\; \text{Single-channel Model A} \;\;\xrightarrow{\ell = \ell_\xi}\;\; \text{Linear gapped diffusion} \;\;\xrightarrow{\ell \to \infty}\;\; \delta \equiv 0.$$

### 6.2 Operators that survive to the deep IR

- `M_0 \nabla^2\delta` (linear mobility, marginal)
- `P_0 \delta` (linear penalty, relevant and dominant)

### 6.3 Operators / channels that disappear

| Eliminated by | Operator |
|:---|:---|
| Participation slaving (`τ → 0`) | `\dot v`, `Hv` as independent dynamics |
| `\zeta \to \infty` | Participation enhancement `H/\zeta \to 0`; `\Gamma_{\text{eff}} \to D` |
| RG irrelevance (`χ > 0`) | `M_2 \delta^2 \nabla^2\delta`, `M_2 \delta|\nabla\delta|^2` |
| RG irrelevance (`χ > 1`) | `P_3\delta^3` |
| Field-amplitude suppression (`\delta \to 0`) | **all** `\mathcal{O}(\delta^k \ge 2)` terms, regardless of RG eigenvalue |
| Higher-derivative suppression (`λ < 0`) | `\nabla^4\delta`, `(\nabla^2\delta)^2`, etc. |

### 6.4 Match to RG flow geometry

This derivation realises the "fixed point at infinity" of [`ED_RG_Flow_Geometry.md`](ED_RG_Flow_Geometry.md) §4.4:

$$\text{IR sink:}\;\; \bigl(P_0 \to \infty,\; \zeta \to \infty,\; \tau \to 0,\; \Gamma_{\text{eff}} \to D,\; \delta \to 0\bigr).$$

The PDE equivalent of this trajectory-endpoint is exactly the two-operator linear-gapped-diffusion equation of §5.1. The RG flow geometry and the explicit IR PDE are consistent.

### 6.5 Closed-form final statement

$$\boxed{\;\;\partial_t\delta_{\text{IR}} \;=\; D\,M_0\,\nabla^2\delta_{\text{IR}} \;-\; D\,P_0(\ell)\,\delta_{\text{IR}}, \qquad P_0(\ell) \to \infty, \qquad \delta_{\text{IR}} \to 0.\;\;}$$

This is the exact IR effective PDE of canonical ED.
