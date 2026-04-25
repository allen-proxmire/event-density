# RG Flow Geometry of the Canonical ED PDE

**Date.** 2026-04-22 (eighth pass).
**Scope.** Mathematical: full flow-geometry extension of the tree-level RG analysis in [`ED_RG_Flow_Analysis.md`](ED_RG_Flow_Analysis.md). Identifies fixed points, computes stability, classifies directions, places the physical ED theory in the flow.

---

## 1. Theory space

Coordinates: `g = (P_0, ζ, τ, P_3, M_2) ∈ ℝ⁵`. Normalisation `M_0 ≡ 1` (diffusive) and `D + H = 1` already imposed.

Flow parameter: `ℓ = ln b`, `b > 1` (IR direction as `ℓ ↑`).

Beta functions (from tree-level analysis, `z = 2`):

$$\beta_{P_0} = 2\,P_0, \quad \beta_\zeta = 2\,\zeta, \quad \beta_\tau = -2\,\tau, \quad \beta_{P_3} = (2-2\chi)\,P_3, \quad \beta_{M_2} = -2\chi\,M_2.$$

Field scaling exponent `χ` is a free parameter in the deterministic theory; its value selects which nonlinear coupling is marginal. The two canonical choices are `χ = 0` and `χ = 1`.

---

## 2. Fixed points

Solving `β_i(g^*) = 0` for all `i`:

- `P_0^* = 0`, `ζ^* = 0`, `τ^* = 0` in every case (β-functions linear with non-zero slope).
- `P_3^* = 0` *or* `χ = 1` (marginal direction).
- `M_2^* = 0` *or* `χ = 0` (marginal direction).

### 2.1 Fixed-point catalog

| Label | Coordinates `(P_0, ζ, τ, P_3, M_2)` | `χ` | Type |
|:---|:---|:---:|:---|
| **G** | `(0, 0, 0, 0, 0)` | arbitrary | Gaussian fixed **point** |
| **WF** | `(0, 0, 0, P_3^* \in ℝ, 0)` | `1` | Fixed **line** (cubic-marginal) |
| **NM** | `(0, 0, 0, 0, M_2^* \in ℝ)` | `0` | Fixed **line** (nonlinear-mobility-marginal) |

At tree level, WF and NM are one-parameter families of fixed points along the marginal direction. Loop corrections (in the stochastic theory) would promote the marginal direction to a logarithmic flow with a single non-trivial Wilson-Fisher-type zero.

The Gaussian FP G is a genuine *point* in all basis choices; it is the intersection of the WF and NM fixed lines.

### 2.2 What is *not* a fixed point

- The physical ED theory `(P_0 > 0, ζ > 0, τ > 0, P_3 ≠ 0, M_2 ≠ 0)`.
- Any theory with `P_0 ≠ 0` or `ζ ≠ 0`.
- The `τ = ∞` limit (frozen-participation) — formally `β_τ · τ = −2τ²` diverges, but the asymptotic direction is a sink only for `τ = 0`.

---

## 3. Stability analysis

### 3.1 Stability matrix

Because each β is linear in the single coupling it involves (no cross-coupling at tree level), the Jacobian `J_{ij} = ∂β_i/∂g_j` is **diagonal at every fixed point** in this basis:

$$J \;=\; \text{diag}\bigl(\,2,\;\; 2,\;\; -2,\;\; 2-2\chi,\;\; -2\chi\,\bigr).$$

### 3.2 Eigenvalues and eigenvectors

Eigenvectors are the coordinate axes:

| Direction | Eigenvalue `λ` | Sign | Behaviour under IR flow |
|:---|:---:|:---:|:---|
| `P_0`-axis | `+2` | `>0` | relevant — grows as `b²` |
| `ζ`-axis | `+2` | `>0` | relevant — grows as `b²` |
| `τ`-axis | `−2` | `<0` | irrelevant — decays as `b^{-2}` |
| `P_3`-axis | `2 − 2χ` | χ-dep. | relevant (`χ<1`), marginal (`χ=1`), irrelevant (`χ>1`) |
| `M_2`-axis | `−2χ` | χ-dep. | relevant (`χ<0`), marginal (`χ=0`), irrelevant (`χ>0`) |

### 3.3 Classification at each FP

At the two canonical `χ`-choices:

**Gaussian FP, χ = 0:**

| Direction | `λ` | Class |
|:---|:---:|:---|
| `P_0` | +2 | relevant |
| `ζ` | +2 | relevant |
| `P_3` | +2 | relevant |
| `τ` | −2 | irrelevant |
| `M_2` | 0 | marginal |

Stability: **3 relevant, 1 irrelevant, 1 marginal.** Codimension-3 unstable manifold — must tune 3 couplings to reach G.

**Gaussian FP, χ = 1 (equivalently: WF fixed line):**

| Direction | `λ` | Class |
|:---|:---:|:---|
| `P_0` | +2 | relevant |
| `ζ` | +2 | relevant |
| `τ` | −2 | irrelevant |
| `M_2` | −2 | irrelevant |
| `P_3` | 0 | marginal |

Stability: **2 relevant, 2 irrelevant, 1 marginal.** Codimension-2 unstable manifold.

**Summary of instabilities:**

- `P_0` and `ζ` are *always* relevant: physical ED is unstable against these two directions under all choices of `χ`.
- `τ` is *always* irrelevant.
- `P_3` and `M_2` cannot be *simultaneously* non-relevant for any choice of `χ`: at `χ = 0`, `M_2` is marginal but `P_3` is relevant; at `χ = 1`, `P_3` is marginal but `M_2` is irrelevant; in between, both are neither fixed nor compatible.

---

## 4. Qualitative RG flow

### 4.1 Closed-form trajectories

Because `J` is diagonal, flow in each coordinate decouples. Exact integration of `dg_i/dℓ = λ_i g_i`:

$$P_0(\ell) = P_0(0)\,e^{2\ell}, \quad \zeta(\ell) = \zeta(0)\,e^{2\ell}, \quad \tau(\ell) = \tau(0)\,e^{-2\ell},$$

$$P_3(\ell) = P_3(0)\,e^{(2-2\chi)\ell}, \quad M_2(\ell) = M_2(0)\,e^{-2\chi\ell}.$$

### 4.2 Invariants of the flow

Ratios cancel equal-eigenvalue exponentials. Conserved quantities along any trajectory:

$$\mathcal{R}_1 \;=\; \frac{P_0}{\zeta}, \qquad \mathcal{R}_2 \;=\; P_0 \cdot \tau, \qquad \mathcal{R}_3 \;=\; \zeta \cdot \tau.$$

`R_1` is the penalty-to-damping ratio (channel-weight-independent). `R_2` and `R_3` are the products of a relevant × irrelevant coupling, which are RG-invariant. These invariants foliate the flow.

Additional invariants depending on `χ`:

- At `χ = 1`: `P_0 / P_3²` is invariant (both scale as `b²` and `b⁰` — wait, P_3 is marginal so `P_3/P_3 = 1` is trivially invariant; the useful invariant is `P_3` itself, constant along flow).
- At `χ = 0`: `P_3 / P_0` is invariant (both scale as `b²`), and `M_2` is constant.

### 4.3 Basins of attraction

**The Gaussian FP at the origin has a stable manifold of codimension 3 (χ=0) or codimension 2 (χ=1).** Initial conditions satisfying `P_0 = 0`, `ζ = 0`, plus (at χ=0) `P_3 = 0`, flow into G along the `τ`-axis (and the `M_2` marginal axis, frozen).

**For generic bare ED** (`P_0, ζ, τ, P_3, M_2` all non-zero), the trajectory leaves G along its unstable manifold. As `ℓ → ∞`:

$$P_0(\ell), \zeta(\ell) \to \infty, \qquad \tau(\ell) \to 0, \qquad P_3(\ell) \to \begin{cases} \infty & (χ<1) \\ \text{const} & (χ=1) \\ 0 & (χ>1) \end{cases}, \qquad M_2(\ell) \to \begin{cases} \infty & (χ<0) \\ \text{const} & (χ=0) \\ 0 & (χ>0) \end{cases}.$$

### 4.4 IR fate: the "fixed point at infinity"

Because `P_0 → ∞` and `ζ → ∞` at any nonzero bare value, the IR fate of every generic trajectory is the **trivial massive phase**:

$$\text{IR}(\ell \to \infty) \;\longmapsto\; \bigl(P_0 \to \infty,\; \zeta \to \infty,\; \tau \to 0,\; \langle\delta\rangle \to 0\bigr).$$

No non-trivial IR fixed point exists in finite theory space. This "fixed point at infinity" represents a gapped, fully-relaxed system — correlations decay exponentially with length scale `ξ(\ell) = \sqrt{M_0/P_0(\ell)} \propto e^{-\ell}`, i.e. vanishing correlation length at long wavelengths.

### 4.5 Critical manifolds

- **Gaussian critical manifold** (codim 3 at χ=0; codim 2 at χ=1): `{P_0 = 0, ζ = 0, P_3 = 0 (at χ=0)}`. All initial conditions on this manifold flow into G along the irrelevant directions (`τ`, `M_2` at χ=0).
- **WF critical manifold** (χ = 1; codim 2): `{P_0 = 0, ζ = 0}` — the theory is a 1-parameter family along `P_3`, flowing into the WF fixed line along irrelevant `τ, M_2`.
- **NM critical manifold** (χ = 0; codim 2): `{P_0 = 0, ζ = 0, P_3 = 0}` — flows into the NM fixed line along irrelevant `τ`.

### 4.6 UV limit

As `ℓ → −∞` (`b → 0`, short distances), the flow reverses:

$$P_0(\ell) \to 0, \quad \zeta(\ell) \to 0, \quad \tau(\ell) \to \infty, \quad \langle \delta \rangle \text{ free}.$$

ED approaches the Gaussian FP in the UV along its unstable manifold (run backwards). In this sense G is **UV-attractive** for the marginal and irrelevant directions and **UV-repulsive** along the relevant `P_0, ζ`. The UV behaviour of bare ED is Gaussian to leading order — a *massless, damping-free, frozen-participation* free theory.

---

## 5. Physical ED in the flow

### 5.1 Position at the microscopic scale

Bare ED at `ℓ = 0`:

$$g_0 \;=\; (P_0, \zeta, \tau, P_3, M_2), \qquad \text{all components non-zero.}$$

No component lies on any critical manifold. Therefore `g_0` has non-trivial projection onto every unstable direction of every fixed point.

### 5.2 Trajectory

Define the correlation length and the participation length:

$$\xi \;:=\; \sqrt{M_0/P_0}, \qquad \xi_v \;:=\; \sqrt{M_0\,\tau/\zeta}.$$

In units `M_0 = 1`:

- `ξ(\ell) = \xi\,e^{-\ell}` — shrinks under IR flow.
- `ξ_v(\ell) = \xi_v\,e^{-2\ell}` (from `τ e^{-2ℓ}/ ζ e^{2ℓ} = (τ/ζ) e^{-4ℓ}`, `ξ_v ∝ e^{-2ℓ}`).

Three characteristic flow scales:

| Scale (in ℓ) | Event |
|:---|:---|
| `\ell_v = \tfrac{1}{2}\ln(\xi_v \Lambda)` | participation channel becomes irrelevant (`v` slaves to `F/ζ`) |
| `\ell_\xi = \ln(\xi \Lambda)` | correlation length reached, system gapped below this |
| `\ell \gg \ell_\xi` | deep IR, trivial massive phase |

For physical ED, `ξ_v < ξ` is the generic ordering (participation channel is usually faster than the mass scale). `ℓ_v < ℓ_ξ`.

### 5.3 Flow away from / toward fixed points

Relative to each FP:

| FP | Does ED flow toward it? | How? |
|:---|:---|:---|
| G (UV end) | Yes, in the limit `ℓ → −∞` | Along unstable manifold run backwards |
| G (IR end) | No — ED leaves G along relevant `P_0, ζ` | — |
| WF (χ=1) | No — WF unstable along `P_0, ζ`; physical ED generically not on its critical manifold | — |
| NM (χ=0) | No — NM unstable along `P_0, ζ, P_3`; same | — |
| "FP at infinity" (massive phase) | Yes, in the limit `ℓ → +∞` | Generic IR flow of any initial condition with `P_0 ≠ 0` |

**ED's IR destination is the trivial massive phase.** ED's UV origin is the Gaussian fixed point.

### 5.4 IR effective theory

Below the participation scale `ℓ > ℓ_v`: `τ(\ell) → 0`, so

$$\tau\,\dot v = F[\delta] - \zeta\,v \;\;\xrightarrow{\tau \to 0}\;\; v = F[\delta]/\zeta.$$

Substitute into the `δ` equation:

$$\partial_t\delta \;=\; D\,F[\delta] \;+\; H\cdot\frac{F[\delta]}{\zeta} \;=\; \Bigl(D + \frac{H}{\zeta(\ell)}\Bigr)F[\delta].$$

Below the correlation scale `ℓ > ℓ_\xi`: `P_0(\ell) \gg M_0 \Lambda^2`, the penalty dominates:

$$\partial_t\delta \;\approx\; -\bigl(D + H/\zeta\bigr) P_0(\ell)\,\delta \;+\; \text{(subdominant gradients)}.$$

Solution: `δ ∝ e^{-(D+H/ζ)P_0 t} → 0` exponentially. The IR effective PDE is

$$\boxed{\;\partial_t\delta \;=\; -\Gamma(\ell)\,\delta \;+\; \mathcal{O}(\nabla^2/\xi^2)\;, \qquad \Gamma(\ell) = \bigl(D + H/\zeta(\ell)\bigr)P_0(\ell) \to \infty\;.}$$

This is *pointwise exponential relaxation* — no spatial structure survives, no dynamical modes propagate. The IR effective theory is **trivial: δ ≡ 0**.

### 5.5 UV effective theory

Above the smallest inverse length in play (ℓ < 0, b < 1):

$$P_0(\ell),\,\zeta(\ell) \to 0, \qquad \tau(\ell) \to \infty, \qquad \partial_t\delta \;\to\; D\,M_0\,\nabla^2\delta + H\,v, \qquad \tau\,\dot v = M_0\,\nabla^2\delta.$$

The UV effective PDE is **linear, massless, two-channel, undamped**. In the strict `\tau \to \infty` limit v freezes, leaving pure diffusion `\partial_t\delta = D\,M_0\,\nabla^2\delta`. The UV fixed-point theory is **free diffusion**.

### 5.6 Intermediate regime

Between `ℓ_v` and `ℓ_ξ` (participation slaved, mass not yet dominant):

$$\partial_t\delta \;=\; \bigl(D + H/\zeta(\ell)\bigr)\bigl[M_0\,\nabla^2\delta - P_0(\ell)\,\delta + \text{nonlinear}\bigr].$$

This is single-channel Model-A relaxational dynamics with a running mass. Nonlinear `P_3, M_2` contributions run according to their own eigenvalues; which dominates is `χ`-dependent.

---

## 6. Final summary

### 6.1 Fixed-point inventory

| Name | Location | Stable directions | Unstable directions | Marginal |
|:---|:---|:---:|:---:|:---:|
| **Gaussian G** (χ = 0) | origin | τ | P_0, ζ, P_3 | M_2 |
| **Gaussian G** (χ = 1) | origin | τ, M_2 | P_0, ζ | P_3 |
| **WF fixed line** (χ = 1) | `P_3` axis | τ, M_2 | P_0, ζ | along-line |
| **NM fixed line** (χ = 0) | `M_2` axis | τ | P_0, ζ, P_3 | along-line |
| **"FP at infinity"** (IR sink) | `(P_0, ζ) → ∞`, `τ → 0` | all | none | — |

### 6.2 ED's RG trajectory

$$\text{Gaussian G (UV, } \ell \to -\infty\text{)} \;\;\longrightarrow\;\; \text{Physical ED (}\ell = 0\text{)} \;\;\longrightarrow\;\; \text{Massive IR sink (}\ell \to +\infty\text{)}.$$

Two crossover scales traversed:

1. `\ell_v = \tfrac{1}{2}\ln(\xi_v \Lambda)`: two-channel → single-channel (participation slaved).
2. `\ell_\xi = \ln(\xi \Lambda)`: single-channel → trivial massive (spatial structure extinguished).

### 6.3 Effective PDEs at each regime

$$\text{UV (}\ell \ll \ell_v\text{):}\quad \partial_t\delta = D M_0 \nabla^2\delta + H v, \quad \tau\dot v = M_0 \nabla^2\delta. \qquad \text{(two-channel free diffusion)}$$

$$\text{Intermediate (}\ell_v < \ell < \ell_\xi\text{):}\quad \partial_t\delta = (D + H/\zeta)\bigl[M_0\nabla^2\delta - P_0 \delta + \tfrac{P_3}{6}\delta^3 + \tfrac{M_2}{2}\delta^2\nabla^2\delta + M_2\delta|\nabla\delta|^2\bigr]. \qquad \text{(single-channel Model A)}$$

$$\text{IR (}\ell \gg \ell_\xi\text{):}\quad \partial_t\delta = -\Gamma\,\delta, \qquad \Gamma \to \infty. \qquad \text{(trivial relaxation)}$$

### 6.4 Meaning for cross-scale invariance

- **Operator basis is RG-invariant.** No new operators appear at any scale. This is what makes the ED PDE *form* identifiable across regimes.
- **Couplings are RG-dependent.** `P_0, ζ` grow under IR flow; `τ` decays; `P_3, M_2` flow according to the `χ`-choice. The Dimensional Atlas's per-regime coupling maps are therefore *structurally forced*, not optional.
- **Two-channel structure is UV-only.** The participation channel is IR-irrelevant. At scales larger than `ξ_v`, ED is effectively single-channel Model A with slaved participation. The oscillatory / Q-coherent signatures live strictly above `ℓ_v` in UV, gone below.
- **No non-trivial IR fixed point exists.** The ED theory does not flow to any interacting fixed point; it flows to a trivial massive sink. Non-trivial physics lives at intermediate `ℓ` between the two crossover scales `ℓ_v` and `ℓ_ξ`.
- **Cross-scale reuse is the statement that the intermediate-regime PDE form (Model-A relaxational with two characteristic scales `ξ`, `ξ_v`) is universal across regimes at the level of operator content.** Each regime sits at different bare values of `(P_0, ζ, τ, P_3, M_2)` and therefore at different `(ξ, ξ_v)`, but the *form* of the effective PDE is the same. This is what §6.1 of `ED_RG_Flow_Analysis.md` called "form closure"; the present flow-geometry analysis localises it to the intermediate regime and identifies the two crossover scales as the boundaries beyond which the universality breaks down (in the UV to free diffusion, in the IR to trivial relaxation).

---

## Appendix A — Summary card

| Question | Answer |
|:---|:---|
| How many fixed points? | 1 point (G) + 2 lines (WF, NM) + 1 "point at infinity" (massive sink). |
| Is any FP IR-stable with non-trivial couplings? | **No.** |
| Does ED flow to itself? | **No.** ED flows from G (UV) to the massive sink (IR). |
| Does the ED *form* survive flow? | **Yes**, in the intermediate regime `ℓ_v < ℓ < ℓ_ξ`. |
| Which couplings are IR-growing? | `P_0, ζ` (always); `P_3, M_2` conditional on `χ`. |
| Which couplings are IR-decaying? | `τ` (always); `M_2` (χ > 0); `P_3` (χ > 1). |
| Flow invariants? | `P_0/ζ`, `P_0·τ`, `ζ·τ`; and χ-dependent ratios. |
| Critical manifold codimension at G? | 3 (χ=0) or 2 (χ=1). |
| Participation channel in IR? | Slaved to `F[δ]/ζ`; two-channel → single-channel at `ℓ_v`. |
| UV-effective theory? | Free two-channel diffusion. |
| IR-effective theory? | Trivial relaxation `∂_t δ = −Γ δ`, `Γ → ∞`. |
| Intermediate effective theory? | Single-channel Model A with full ED operator basis. |
| Cross-scale invariance localised to? | Intermediate regime `ℓ_v < ℓ < ℓ_ξ` — the "ED window". |
