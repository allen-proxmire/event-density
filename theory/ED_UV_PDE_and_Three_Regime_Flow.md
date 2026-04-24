# UV Effective PDE of ED and the Three-Regime Flow

**Date.** 2026-04-22 (tenth pass).
**Scope.** Derivation of the UV effective PDE of canonical ED and assembly of the full three-regime flow diagram, consolidating [`ED_RG_Flow_Analysis.md`](ED_RG_Flow_Analysis.md), [`ED_RG_Flow_Geometry.md`](ED_RG_Flow_Geometry.md), and [`ED_IR_Effective_PDE.md`](ED_IR_Effective_PDE.md).

---

## 1. Starting system

$$\partial_t \delta \;=\; D\,F[\delta] \;+\; H\,v, \qquad \tau\,\dot v \;=\; F[\delta] \;-\; \zeta\,v, \qquad D + H = 1.$$

$$F[\delta] \;=\; M_0\,\nabla^2\delta \;+\; \tfrac{1}{2}M_2\,\delta^2\,\nabla^2\delta \;+\; M_2\,\delta\,|\nabla\delta|^2 \;-\; P_0\,\delta \;-\; \tfrac{1}{6}P_3\,\delta^3 \;+\; \cdots$$

---

## 2. UV limit

The RG flow integrals (`ℓ = ln b`, `ℓ → −∞`) give:

$$P_0(\ell) = P_0\,e^{2\ell} \to 0, \quad \zeta(\ell) = \zeta\,e^{2\ell} \to 0, \quad \tau(\ell) = \tau\,e^{-2\ell} \to \infty.$$

Non-linear couplings for the natural `χ \le 0` choice (Gaussian branch):

$$P_3(\ell) = P_3\,e^{(2-2\chi)\ell} \to 0 \quad (\chi < 1), \qquad M_2(\ell) = M_2\,e^{-2\chi\ell} \to 0 \quad (\chi < 0).$$

Field `δ` is unsuppressed (no IR mass gap yet).

### 2.1 Participation-ODE limit

$$\tau\,\dot v \;=\; F[\delta] - \zeta\,v.$$

With `\zeta \to 0`:

$$\tau\,\dot v \;=\; F[\delta].$$

With `\tau \to \infty`:

$$\dot v \;=\; \frac{F[\delta]}{\tau} \;\xrightarrow[\tau \to \infty]{}\; 0 \quad\Longrightarrow\quad v(t) \;=\; v_0 \;+\; \mathcal{O}(1/\tau).$$

**`v` is frozen at its initial value** on any finite δ-timescale. The v-ODE does not decouple (as in the IR) but it *freezes*: `v` becomes a static, uniform background source.

Formally to leading order in small `1/τ`:

$$v(t) \;=\; v_0 \;+\; \frac{1}{\tau}\int_0^t F[\delta(s)]\,ds \;+\; \mathcal{O}(1/\tau^2).$$

### 2.2 δ-equation limit

$$\partial_t\delta \;=\; D\,F[\delta] + H\,v.$$

Drop vanishing couplings:

$$\partial_t\delta \;=\; D\Bigl[\,M_0\,\nabla^2\delta \;+\; \underbrace{\tfrac{1}{2}M_2\,\delta^2\,\nabla^2\delta + M_2\,\delta\,|\nabla\delta|^2}_{\to 0 \text{ for } \chi < 0} \;-\; \underbrace{\tfrac{1}{6}P_3\,\delta^3}_{\to 0 \text{ for } \chi < 1}\,\Bigr] + H\,v_0.$$

---

## 3. UV effective PDE

### 3.1 Canonical UV limit (Gaussian branch, `χ ≤ 0`)

All nonlinear couplings vanish; mass and damping vanish; `v` frozen:

$$\boxed{\;\partial_t\delta \;=\; D\,M_0\,\nabla^2\delta \;+\; H\,v_0, \qquad v(t) = v_0 = \text{const}.\;}$$

With `H v_0` re-absorbed into a shift of `δ → δ − H v_0 t` (a linear-in-time drift of the equilibrium), the UV-effective PDE for the fluctuation field is:

$$\partial_t\delta \;=\; D\,M_0\,\nabla^2\delta.$$

This is **pure linear diffusion**, the Gaussian fixed-point theory.

### 3.2 UV limit retaining leading `1/τ` correction (two-channel structure)

Without taking `\tau \to \infty` strictly, at large-but-finite `τ` with `P_0 = \zeta = 0` and nonlinear couplings dropped:

$$\boxed{\;\partial_t\delta \;=\; D\,M_0\,\nabla^2\delta \;+\; H\,v, \qquad \tau\,\dot v \;=\; M_0\,\nabla^2\delta.\;}$$

This is **free two-channel diffusion**: `δ` undergoes Laplacian diffusion with mobility `D M_0`; `v` tracks the global `k=0` Laplacian integral of `δ` on the long timescale `τ`. The two channels are linearly coupled but both massless and damping-free.

Spectrum (Fourier modes `e^{i k \cdot x + \omega t}`):

$$(\omega - D M_0 k^2)\,(\tau\omega) \;-\; H\cdot(-M_0 k^2) \;=\; 0$$

$$\tau\omega^2 - \tau D M_0 k^2 \omega + H M_0 k^2 \;=\; 0$$

$$\omega \;=\; \frac{\tau D M_0 k^2 \pm \sqrt{\tau^2 D^2 M_0^2 k^4 - 4\tau H M_0 k^2}}{2\tau}.$$

At long wavelengths `k \ll k_* = 2/(D M_0^{1/2}\,\sqrt{\tau D/H})`: complex conjugate `ω` — **oscillatory two-channel modes**. At short wavelengths `k \gg k_*`: real negative `ω` — overdamped diffusion. The crossover `k_*` is set by `\sqrt{H/(τ D M_0)}`, which shrinks as `τ → ∞`: deeper UV means the oscillatory sector covers more of `k`-space.

### 3.3 Surviving operators and channels

| Operator | UV fate | Reason |
|:---|:---|:---|
| `M_0 \nabla^2 \delta` | **Survives** | marginal at `z=2` |
| `-P_0\,\delta` | Vanishes | `P_0 \to 0` |
| `-\tfrac{1}{6}P_3\,\delta^3` | Vanishes (χ<1) | `P_3 \to 0` |
| `M_2\,\delta^2\nabla^2\delta`, `M_2\,\delta\|\nabla\delta\|^2` | Vanish (χ<0) | `M_2 \to 0` |
| `H\,v` | **Survives as constant source (χ < 0, strict τ→∞) OR as dynamical two-channel coupling (finite τ)** | — |
| `-\zeta\,v` | Vanishes | `\zeta \to 0` |
| `\tau\,\dot v` | Slow / frozen | `\tau \to \infty` suppresses `\dot v` |

### 3.4 Physical meaning of UV theory

- **No mass gap**: correlation length `\xi \to \infty`; fluctuations exist at all wavelengths.
- **No damping**: participation mode has no relaxation channel.
- **Two-channel structure retained**: the v-mode exists as a slow global degree of freedom coupled to the `k=0` Laplacian of δ.
- **Oscillatory dispersion at long wavelengths**: the `\tau \dot v = M_0 \nabla^2\delta` coupling produces `\omega^2 \propto k^2` behaviour — **wave-like propagation**, in contrast to the diffusive `ω \propto k^2` of the direct channel alone. This is the kinematic acoustic-metric / free-scalar QFT regime identified in [`ED_Reversible_Sector_QFT.md`](ED_Reversible_Sector_QFT.md) and [`ED_Effective_Acoustic_Metric.md`](ED_Effective_Acoustic_Metric.md).

The UV theory is **linear, massless, undamped, and supports propagating wave modes** via the participation channel.

---

## 4. Three-regime summary

### 4.1 Regime boundaries

$$\ell_v \;=\; \tfrac{1}{2}\ln(\xi_v \Lambda) \;=\; \tfrac{1}{2}\ln\!\sqrt{M_0\,\tau/\zeta}\,\Lambda, \qquad \ell_\xi \;=\; \ln(\xi \Lambda) \;=\; \ln\!\sqrt{M_0/P_0}\,\Lambda.$$

Under generic ED parameters `\xi_v < \xi`, so `\ell_v < \ell_\xi`.

### 4.2 Effective PDE in each regime

**Regime (a) — UV** (`\ell < \ell_v`, short distances, `k > 1/\xi_v`):

$$\partial_t\delta \;=\; D\,M_0\,\nabla^2\delta \;+\; H\,v, \qquad \tau\,\dot v \;=\; M_0\,\nabla^2\delta.$$

*Free two-channel diffusion with wave-like propagating modes.*

**Regime (b) — Intermediate** (`\ell_v < \ell < \ell_\xi`, `1/\xi < k < 1/\xi_v`):

$$\partial_t\delta \;=\; \Gamma_{\text{eff}}(\ell)\,\Bigl[M_0\,\nabla^2\delta + \tfrac{1}{2}M_2\,\delta^2\nabla^2\delta + M_2\,\delta|\nabla\delta|^2 - P_0(\ell)\,\delta - \tfrac{1}{6}P_3(\ell)\,\delta^3\Bigr],$$

$$\Gamma_{\text{eff}}(\ell) \;=\; D + H/\zeta(\ell).$$

*Single-channel Model A with full ED nonlinear operator basis; participation slaved.*

**Regime (c) — IR** (`\ell > \ell_\xi`, `k < 1/\xi`):

$$\partial_t\delta \;=\; D\,M_0\,\nabla^2\delta \;-\; D\,P_0(\ell)\,\delta, \qquad P_0(\ell) \to \infty.$$

*Linear, gapped, single-channel relaxation; `δ → 0` pointwise exponentially.*

### 4.3 What turns on/off at each boundary

At **ℓ = ℓ_v** (UV → Intermediate):

| Element | UV side | Intermediate side |
|:---|:---|:---|
| Participation ODE | Slow, `v ≈ v_0 + O(1/\tau)` | Slaved, `v = F[\delta]/\zeta` |
| `H v` coupling | Constant-source or slow dynamical | Algebraic enhancement `H/\zeta` |
| `\tau \dot v` | Dominant | Negligible |
| Two-channel structure | **Retained** | **Collapsed to single-channel** |
| Propagating `ω^2 \propto k^2` modes | Exist at long wavelength | Gone — only diffusive `ω \propto k^2` |
| Nonlinear operators `M_2, P_3` | Negligible (small amplitude / suppressed couplings) | **Active** at generic δ |
| Mass term `P_0 \delta` | Negligible | **Active** (finite `P_0`) |

At **ℓ = ℓ_ξ** (Intermediate → IR):

| Element | Intermediate side | IR side |
|:---|:---|:---|
| Correlation length `\xi(\ell)` | Finite (decreasing) | Below cutoff length `\Lambda^{-1}` |
| Mass term `P_0(\ell)\delta` | Sub-dominant at small δ, active at finite δ | **Dominant**, drives `δ → 0` |
| Nonlinear operators | Present, finite-amplitude | **Field-amplitude suppressed** (δ → 0) |
| `M_0 \nabla^2\delta` | Active | Active but sub-dominant |
| `\Gamma_{\text{eff}}` | `D + H/\zeta(\ell) > D` | `\to D` |
| IC memory | Present via nonlinear flow | Lost; pointwise exponential decay |

---

## 5. Full flow diagram

```
ℓ →  -∞   ........... ℓ_v ........... ℓ_ξ ........... +∞
                      |              |
 UV (free two-ch.)    |  Intermediate |   IR (gapped)
                      |  (full ED)    |
                      |               |
                      ↓               ↓
              participation       spatial structure
                 slaves            exponentially
              (2-ch → 1-ch)         extinguished
              (waves → diffusion)  (Model A → δ≡0)

P_0(ℓ):  0 ───────────→ P_0 ───────→ ∞     [relevant, β=+2]
ζ(ℓ):    0 ───────────→ ζ ─────────→ ∞     [relevant, β=+2]
τ(ℓ):    ∞ ───────────→ τ ─────────→ 0     [irrelevant, β=−2]
P_3(ℓ):  0 or fixed ──→ P_3 ───────→ ∞ or 0 (χ-dep)
M_2(ℓ):  ∞ or 0 ──────→ M_2 ───────→ 0 or ∞ (χ-dep)
```

### 5.1 Physical meaning of each regime

| Regime | Length-scale range | Physical character | Dynamics |
|:---|:---|:---|:---|
| **UV** | `L < \xi_v` | Massless, undamped, two-channel | Wave-like + diffusive coexistent; oscillatory modes exist |
| **Intermediate** | `\xi_v < L < \xi` | Single-channel Model A with full nonlinearities | Relaxational with mass, cubic self-interaction, nonlinear mobility; the "ED window" |
| **IR** | `L > \xi` | Trivial massive phase | Linear gapped diffusion; δ → 0 exponentially |

### 5.2 Compact operator on/off table

| Operator | UV | Intermediate | IR |
|:---|:---:|:---:|:---:|
| `M_0 \nabla^2 \delta` | on | on | on |
| `-P_0 \delta` | off | on | on (dominant) |
| `P_3 \delta^3` | off (χ<1) | on | off (δ→0) |
| `M_2 \delta^2\nabla^2\delta`, `M_2 \delta\|\nabla\delta\|^2` | off (χ<0) | on | off (δ→0) |
| `H v` (source/channel) | on (frozen/slow) | on (slaved) | vanishing contribution (`H/\zeta \to 0`) |
| `\tau \dot v` | on (slow) | off (slaving) | off |
| `-\zeta v` | off | on | off (slaved to F) |

---

## 6. Final consolidated summary

### 6.1 Three effective PDEs

$$\boxed{\;\;\text{UV:}\quad \partial_t\delta = D M_0 \nabla^2\delta + H v, \qquad \tau \dot v = M_0 \nabla^2\delta.\;\;}$$

$$\boxed{\;\;\text{Intermediate:}\quad \partial_t\delta = \Gamma_{\text{eff}}\Bigl[M_0\nabla^2\delta + \tfrac{M_2}{2}\delta^2\nabla^2\delta + M_2\delta|\nabla\delta|^2 - P_0\delta - \tfrac{P_3}{6}\delta^3\Bigr].\;\;}$$

$$\boxed{\;\;\text{IR:}\quad \partial_t\delta = D M_0 \nabla^2\delta - D P_0(\ell)\delta, \qquad P_0(\ell) \to \infty.\;\;}$$

### 6.2 Flow geometry

- **UV origin** at Gaussian fixed point G (free two-channel diffusion, propagating modes).
- **Intermediate "ED window"** between crossovers `\ell_v` and `\ell_\xi`: single-channel Model A with full ED operator basis. This is the regime to which the ED framework's nonlinear content — mobility capacity, saturating penalty, cubic self-interaction, participation slaving — applies.
- **IR sink**: trivial massive phase; `δ ≡ 0`.

### 6.3 Channel structure across regimes

- **Participation channel is a UV phenomenon.** The two-channel structure with independent `v`-dynamics lives only at `\ell < \ell_v`. In the intermediate regime `v` is algebraically slaved; in the IR `v` contribution vanishes. Coherent, oscillatory, wave-like ED signatures live strictly in the UV regime.
- **Nonlinear self-interaction is an intermediate phenomenon.** `P_3 \delta^3` and `M_2`-induced nonlinear mobility are active only in the intermediate regime. In the UV they are coupling-suppressed (χ-dependent); in the IR they are field-amplitude-suppressed (`δ → 0`).
- **Linear diffusion `M_0 \nabla^2\delta` is universal across all three regimes.** It is marginal at the Gaussian fixed point and propagates unchanged to every asymptotic region.

### 6.4 Interpretation for cross-scale invariance

The claim "ED applies across 20–60 orders of magnitude" decomposes cleanly:

- **Form-invariance of the intermediate PDE** holds across regimes (condensed matter, quantum, optomechanics, galactic, cosmological). Each regime sits at different bare `(P_0, \zeta, \tau, P_3, M_2)` → different `(\xi, \xi_v)` → different location of its "ED window" on the `ℓ`-axis, but the operator content of the intermediate PDE is the same.
- **UV** and **IR** asymptotic forms are simpler than ED itself and are not regime-specific ED content: free diffusion (UV) and linear gapped diffusion (IR) are universal for any Model-A-class theory with a participation mode.
- **The "cross-scale" claim, precisely stated:** the intermediate regime's operator structure is universal; the *location* of that window on the `ℓ`-axis and the *numerical values* of `(P_0, \zeta, \tau)` at `\ell = 0` are regime-specific, which is exactly what the Dimensional Atlas supplies. The windows in different regimes are not expected to coincide on the `\ell`-axis; they coincide only in operator content.
- **Outside the ED window**, ED's predictions reduce to standard PDE asymptotics (free diffusion UV-side, linear relaxation IR-side). ED-specific phenomenology — Q-C transition, nonlinear triad coupling, mobility capacity, saturating penalty — lives in the intermediate window and nowhere else.

---

## Appendix A — Consolidated summary card

| Question | Answer |
|:---|:---|
| UV PDE | `∂_t δ = D M_0 ∇²δ + H v`, `τ \dot v = M_0 ∇²δ` (free two-channel diffusion, wave-like at long wavelengths) |
| Intermediate PDE | Full single-channel ED with slaved v, `Γ_{\text{eff}} = D + H/ζ`, all nonlinearities active |
| IR PDE | `∂_t δ = D M_0 ∇²δ - D P_0(\ell) δ` with `P_0(\ell) \to ∞` (linear gapped diffusion; δ → 0) |
| UV → Intermediate boundary | `\ell_v = \tfrac{1}{2}\ln(\xi_v Λ)`; participation slaves, two-channel collapses |
| Intermediate → IR boundary | `\ell_\xi = \ln(\xi Λ)`; mass gap dominates, δ extinguished |
| Universal operator | `M_0 \nabla^2 δ` — survives in all three regimes |
| UV-only operator | `\tau \dot v` + `H v` as dynamical two-channel coupling |
| Intermediate-only operators | `P_3 δ³`, `M_2 δ² ∇²δ`, `M_2 δ \|\nabla δ\|^2`, `\zeta v` relaxation |
| IR-dominant operator | `P_0 δ` (drives exponential relaxation) |
| Cross-scale invariance meaning | Intermediate-regime operator form is universal across regimes; window location and coupling values are regime-specific |
| ED-specific phenomenology localised to | Intermediate window `\ell_v < \ell < \ell_\xi` only |
