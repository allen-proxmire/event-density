# Wilsonian RG-Flow Analysis of the Canonical ED PDE

**Date.** 2026-04-22 (seventh pass).
**Scope.** Mathematical: block-averaging + rescaling applied to the canonical ED PDE. Determines whether ED is an RG fixed point.

---

## 1. Canonical ED PDE in clean form

### 1.1 Equations

The canonical ED system, with `δ := ρ − ρ*`, `d` spatial dimensions:

$$\partial_t \delta \;=\; D\,F[\delta] \;+\; H\,v, \qquad \tau\,\dot v \;=\; F[\delta] \;-\; \zeta\,v, \qquad D + H = 1.$$

$$F[\delta] \;=\; \nabla\!\cdot\!\bigl(M(\delta)\,\nabla\delta\bigr) \;-\; P(\delta) \;=\; M(\delta)\,\nabla^2\delta + M'(\delta)\,|\nabla\delta|^2 - P(\delta).$$

### 1.2 Fields and operator basis

Smooth Taylor expansions around the equilibrium `δ = 0`:

$$M(\delta) \;=\; M_0 + M_1\delta + \tfrac{1}{2}M_2\delta^2 + \cdots, \qquad P(\delta) \;=\; P_0\delta + \tfrac{1}{6}P_3\delta^3 + \cdots.$$

The saturating SY2 penalty is odd in `δ` by construction, so `P(0)=0` and even coefficients vanish. Under the Z₂ symmetry `(δ, v) → (−δ, −v)` that ED inherits from the odd penalty, mobility must be even: `M_1 = 0`. We adopt Z₂ henceforth; departures re-enter as breaking terms in §6.

**Reduced operator basis** (Z₂-symmetric, up to four derivatives, which is the truncation consistent with the tree-level scaling of §5):

| Symbol | Operator | Source in ED |
|:---|:---|:---|
| `O_0` | `δ` | linear penalty `P_0 δ` |
| `O_2` | `∇²δ` | linear mobility `M_0 ∇²δ` |
| `O_{3,0}` | `δ³` | cubic penalty `P_3 δ³/6` |
| `O_{1,2}` | `δ²∇²δ` | even mobility `½M_2 δ² ∇²δ` |
| `O_{2,2}` | `δ\|∇δ\|²` | even mobility `M_2 δ \|∇δ\|²` |
| `O_{4}` | `∇⁴δ` | higher-derivative (not in bare ED; trial) |
| `O_{v}` | `v` | participation mode |
| `O_{v,t}` | `\dot v` | participation kinetic |
| `O_{δv}` | `δv` implicit via `H v` coupling | two-channel mixing |

`O_{1,2}` and `O_{2,2}` are not independent: the divergence-form identity

$$\nabla\!\cdot\!\bigl(M(\delta)\nabla\delta\bigr) \;=\; M(\delta)\nabla^2\delta + M'(\delta)|\nabla\delta|^2$$

ties their coefficients. Under RG flow the tying is preserved *only if* `div`-form is preserved, which we test in §3–§4.

### 1.3 Symmetries and invariants

- **Translations** `(x, t) → (x+a, t+s)`: homogeneous.
- **Spatial rotations** `x → Rx`: isotropic operators only.
- **Z₂**: `(δ, v) → (−δ, −v)` — adopted.
- **Conservation**: `∫δ` is conserved by the divergence form of the mobility channel *alone*; the penalty channel breaks it. ED as a whole is **not** locally conserved; it is a **relaxational** dynamics (Model A-type) with an additional global mode `v`.
- **Gradient-flow structure**: when `H = 0`, `ζ = 0` the single-channel mobility+penalty system is a gradient descent of the Lyapunov functional `L[δ] = ∫[½M_0(∇δ)² + ½P_0 δ² + P_3 δ⁴/24 + …]` (up to nonlinear mobility corrections). This constrains the allowed operators and simplifies the RG.

---

## 2. Wilsonian coarse-graining map

### 2.1 Scale split

Momentum shell: retain `|k| < Λ/b`, integrate out `Λ/b ≤ |k| < Λ`, `b > 1`:

$$\delta(x,t) = \delta_{<}(x,t) + \delta_{>}(x,t), \qquad v(t) = v_{<}(t) + v_{>}(t).$$

The block-average operator is `B_b = \mathbb{P}_{|k|<Λ/b}`. Working in Fourier for the split, real-space for the rescaling.

### 2.2 Rescaling

$$x' = x/b, \qquad t' = t/b^{z}, \qquad \delta'(x', t') = b^{\chi}\,\delta_{<}(bx', b^z t'), \qquad v'(t') = b^{\chi_v}\,v_{<}(b^z t').$$

Here `z` is the dynamic exponent and `(χ, χ_v)` are the field scaling dimensions, all symbolic.

### 2.3 Operator scaling table

Elementary pieces scale as powers of `b`:

| Quantity | Scaling factor |
|:---|:---|
| `∂_t` | `b^{−z}` |
| `∇` | `b^{−1}` |
| `δ` | `b^{−χ}` |
| `v` | `b^{−χ_v}` |
| `d^d x` | `b^{d}` |

An operator `O = δ^k (∇^{2m} δ)` contributes `b^{−kχ − χ − 2m}` per spacetime point.

---

## 3. Effective PDE for the coarse-grained field

### 3.1 Tree-level contribution

Substitute the split into `F[δ]` and collect terms by number of `δ_>` factors:

$$F[\delta_{<} + \delta_{>}] \;=\; F[\delta_{<}] \;+\; \partial F[\delta_{<}]\cdot\delta_{>} \;+\; \tfrac{1}{2}\partial^2 F[\delta_{<}]\cdot\delta_{>}^2 \;+\; \cdots$$

Taking `B_b`-average (block-average in real space, equivalent to retention of `|k|<Λ/b`):

$$\langle F[\delta_{<} + \delta_{>}]\rangle_{>} \;=\; F[\delta_{<}] \;+\; \tfrac{1}{2}\partial^2 F[\delta_{<}]\cdot\langle\delta_{>}^2\rangle_{>} \;+\; \tfrac{1}{6}\partial^3 F[\delta_{<}]\cdot\langle\delta_{>}^3\rangle_{>} \;+\; \cdots$$

The linear term `∂ F \cdot δ_{>}` vanishes because `⟨δ_{>}⟩_{>} = 0` by the projector.

**Deterministic case (no noise).** In the absence of a stochastic forcing, the PDE has a single deterministic trajectory per initial condition; `⟨δ_{>}^n⟩` reduces to products of deterministic `δ_{>}(x,t)` values, not statistical correlators. For a field with no high-wavenumber content (which is the `B_b`-projected case by construction), `δ_{>} = 0` identically at tree level, and

$$F_b[\delta_{<}] \;=\; F[\delta_{<}] \;\text{(tree level, exact)}.$$

**Structural consequence.** At tree level the coarse-grained PDE is the *same* PDE with `δ → δ_{<}`:

$$\partial_t \delta_{<} \;=\; D\,F[\delta_{<}] \;+\; H\,v_{<}, \qquad \tau\,\dot v_{<} \;=\; F[\delta_{<}]\big|_{k=0} \;-\; \zeta\,v_{<}.$$

**No new operators are generated at tree level.** This is a genuine property of the ED operator basis: the divergence-form mobility, the odd penalty, and the global participation ODE form an operator algebra closed under restriction to `|k|<Λ/b`.

### 3.2 One-loop contribution (stochastic case)

If one augments ED with additive noise `ξ(x,t)` of amplitude `ε` satisfying `⟨ξ⟩ = 0`, `⟨ξ(x,t)ξ(x',t')⟩ = 2ε δ(x−x')δ(t−t')`, the fast modes acquire a nontrivial correlator `⟨δ_{>}^2⟩ ≠ 0` and one-loop corrections appear:

$$\delta F_{\text{1-loop}} \;=\; \tfrac{1}{2}\partial^2 F[\delta_{<}]\,G_{>>}(x,x;t,t)$$

where `G_{>>}` is the high-shell propagator. The second functional derivative of `F` gives:

$$\tfrac{1}{2}\partial^2 F[\delta_{<}]\cdot\delta_{>}^2 \;=\; \tfrac{1}{2}M_2\,\delta_{>}^2\,\nabla^2\delta_{<} + M_2\,\delta_{<}(\nabla\delta_{>})^2 + \tfrac{1}{2}P_3\,\delta_{<}\,\delta_{>}^2 + \cdots$$

After averaging, these shift the running couplings `M_0(b)`, `P_0(b)` by loop integrals, without producing operators outside the ED basis *to the Z₂ truncation order* — because `∂² F[δ]` only contains operators already in the basis. **One-loop form-closure holds in the same sense as tree-level.**

Operators that could in principle be generated but are *not* at one loop by this basis closure:

- `(∇²δ)²`, `(∇δ·∇∇²δ)`: would arise from cross terms of two ∇²; they require `∂^2 F` contain `∇⁴`, which it does not. Absent.
- `δ⁵`, `δ⁷`: would arise from higher `∂^n F`; at one loop only `∂² F` enters. Absent at one loop, potentially present at two loops.

The ED operator basis is therefore **one-loop form-closed** under this RG.

---

## 4. Operator basis expansion of `F_b` and coupling flow

Collecting the flow of each coupling at tree level with the scaling of §2:

$$\partial_{t'}\delta' \;=\; D\bigl[M_0 b^{z-2}\nabla'^2\delta' - P_0 b^{z}\delta' + \tfrac{P_3}{6} b^{z-2\chi}\delta'^3 + \tfrac{M_2}{2} b^{z-2\chi-2}\delta'^2\nabla'^2\delta' + M_2 b^{z-2\chi-2}\delta'|\nabla'\delta'|^2\bigr] + H\,b^{z-\chi+\chi_v}\,v'.$$

$$\tau\,b^{-z}\,\dot{v}' \;=\; \bigl[M_0 b^{-2}\nabla'^2\delta' - P_0\,\delta'\bigr]\big|_{k=0}\cdot b^{-\chi+\chi_v} - \zeta\,v'.$$

Impose the **diffusive normalisation** `M_0` marginal:

$$\boxed{z = 2.}$$

This is the generic Model-A choice; no other choice keeps both `∂_t` and `M_0 ∇²` at the same order without noise. Then the flow of each coupling under `b → b(1+dℓ)` with `ℓ = ln b` is:

| Coupling | Scaling factor | Tree-level `β_i = dg_i/dℓ` | Classification |
|:---|:---|:---|:---|
| `M_0` | `b^{z-2} = 1` | `0` | **Marginal** |
| `P_0` | `b^{z} = b^2` | `2 P_0` | **Relevant** |
| `ζ` | `b^{z} = b^2` | `2 ζ` | **Relevant** |
| `P_3` | `b^{z-2χ} = b^{2-2χ}` | `(2 − 2χ) P_3` | Marginal iff `χ = 1` |
| `M_2` | `b^{z-2χ-2} = b^{-2χ}` | `−2χ M_2` | Marginal iff `χ = 0`; irrelevant for `χ > 0` |
| `τ` | `b^{-z} = b^{-2}` | `−2 τ` | **Irrelevant** (flows to 0) |
| `H` | fixed by `D + H = 1` (tied to D) | `0` | constrained |
| `D` | tied to H | `0` | constrained |
| `χ_v = χ` forced | matching `P_0` cross-coupling | — | — |

**Field exponent `χ` is a free parameter** in the deterministic theory (no noise-fluctuation normalisation to pin it). Two natural choices split the operator content:

- **Gaussian choice** `χ = 0`: `δ` is dimensionless. `M_2` marginal; `P_3` relevant (`β = 2P_3`). Nonlinear mobility preserved at leading order; cubic penalty grows.
- **Wilson-Fisher-like choice** `χ = 1`: cubic penalty `P_3` marginal; `M_2` irrelevant (`β = −2M_2`). Nonlinear mobility flows away, leaving a pure `φ⁴`-like relaxational theory.

The ED bare theory has *both* `M_2` and `P_3` nonzero generically, so it does not sit at either fixed point: at least one of the two nonlinear couplings is relevant/irrelevant and therefore flows.

---

## 5. Beta functions (summary)

At tree level, with `z = 2`:

$$\begin{aligned}
\beta_{M_0} &= 0 \\
\beta_{P_0} &= 2\,P_0 \\
\beta_{\zeta} &= 2\,\zeta \\
\beta_{\tau} &= -2\,\tau \\
\beta_{P_3} &= (2 - 2\chi)\,P_3 \\
\beta_{M_2} &= -2\chi\,M_2 \\
\beta_{H} &= 0 \quad \text{(constrained by }D + H = 1\text{)} \\
\beta_{D} &= 0 \quad \text{(ditto)}
\end{aligned}$$

---

## 6. Fixed-point determination

### 6.1 Solving `β_i = 0` for all `i`

From §5, simultaneous vanishing requires:

1. `P_0 = 0` (no mass / penalty stiffness)
2. `ζ = 0` (no participation damping) — i.e., **reversible slice**
3. `τ` either 0 (v instantly slaved) or ∞ (v frozen) — the operator is marginal only at these endpoints
4. `P_3 = 0` OR `χ = 1`
5. `M_2 = 0` OR `χ = 0`

Conditions (4) and (5) together force either `(P_3 = 0, M_2 = 0, χ \text{ arbitrary})` — fully Gaussian — or a fixed point for one single nonlinear coupling with the other set to zero by hand.

### 6.2 Fixed-point structure

Three tree-level fixed points:

| FP | `P_0` | `ζ` | `P_3` | `M_2` | `χ` | Physical meaning |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **G** (Gaussian) | 0 | 0 | 0 | 0 | free | Free massless relaxation, `M_0 ∇²` only |
| **WF** (cubic) | 0 | 0 | `≠0` (marginal) | 0 | 1 | `φ⁴`-type critical theory; canonical Model A |
| **NM** (nonlinear mobility) | 0 | 0 | 0 | `≠0` (marginal) | 0 | Pure PME-type mobility, no penalty |

**None of these is the bare ED theory**, which has `P_0 ≠ 0`, `ζ ≠ 0`, *and* generically `P_3, M_2 ≠ 0`.

### 6.3 Flow away from the bare theory

Starting from bare ED at a microscopic scale `b = 1`:

$$P_0(b) = P_0\,b^2, \qquad \zeta(b) = \zeta\,b^2, \qquad \tau(b) = \tau\,b^{-2}.$$

At any fixed `M_0` and coarse-graining scale `b`:

- `P_0(b)/M_0 = b²/L_0²`. At `b = L_0·√(M_0/P_0) = ξ` (the correlation length), `P_0(b) M_0^{-1} = 1`: penalty dominates, system is gapped at that scale. Beyond `b ≫ ξ`, flow drives the system into the massive phase where `δ → 0` exponentially. Below `b ≪ ξ`, the theory is approximately Gaussian.
- `τ(b) → 0`: participation timescale vanishes relative to the coarse-grained time. The ODE `τ \dot v = F − ζ v` reduces at long wavelengths to `v = F[δ]/ζ`, **slaving v to δ**.
- Slaved-v substitution: `∂_t δ = (D + H/ζ) F[δ]` — at long wavelengths ED collapses to a **single-channel relaxational PDE with effective mobility `D + H/ζ`** times the bare `F`. The two-channel structure is IR-irrelevant.

### 6.4 Operator-closure vs coupling-closure

Two distinct statements:

- **Form closure (operator-basis closure).** Under tree- *and* one-loop RG, the ED basis `{O_0, O_2, O_{3,0}, O_{1,2}, O_{2,2}, O_v, O_{\dot v}, O_{δv}}` is closed: no new operator types are generated. **Holds.**
- **Coupling closure (fixed-point property).** For ED to be an RG fixed point, all β functions must vanish at the physical couplings. **Fails**: `β_{P_0}, β_{\zeta}, β_{\tau}` are non-zero at the ED values.

### 6.5 Minimal extension for RG closure of bare ED

No extension of the operator basis makes the *physical* ED couplings stationary, because relevance/irrelevance is determined by power-counting, not by operator content. The physical ED theory cannot be a fixed point; it can at most sit *near* the Gaussian/WF fixed point in the UV, flowing massive in the IR.

What *can* be made stationary by a minimal extension is the effective **form** of the PDE under coarse-graining, which is already closed in §6.4. No new operators are needed.

---

## 7. Final summary

**7.1 Does ED flow to itself?** At tree level and one loop, the **form** of the ED PDE is preserved: coarse-graining generates only operators already in the ED basis (penalty + divergence-form mobility + global participation mode). No new operators arise.

**7.2 Is ED closed under RG?** **In the operator-basis sense, yes.** **In the fixed-point sense, no.** The running couplings `P_0(b) = P_0 b^2`, `ζ(b) = ζ b^2`, `τ(b) = τ b^{-2}` are non-stationary. The participation channel is IR-irrelevant: at scales `b ≫ ξ_v = √(M_0 τ/ζ)`, `v` slaves to `F[δ]/ζ` and the two-channel structure collapses to a single-channel relaxational PDE.

**7.3 Is ED's cross-scale invariance structural or approximate?**

- **Structural** in the sense that the *PDE form* is preserved under coarse-graining: same operator basis at every scale.
- **Approximate** in the sense that the *numerical couplings* (`M_0, P_0, ζ, τ`, and with them the atlas scales `L_0, T_0, R_0`) are not RG-invariant; they flow with `b`. What is cross-scale invariant is the *structure*, not the *parameter values*.

**7.4 Implication for the 20–60-orders-of-magnitude reuse claim.**

The cross-scale reuse of the ED PDE across condensed matter, quantum, optomechanics, galactic, and cosmological regimes is now sharpened:

- What is invariant across scales: the **operator basis** (one divergence-form mobility + one odd-symmetric penalty + one global slaved ODE). This is what §6.4 "form closure" certifies, and it is non-trivial — most candidate operator bases fail to close under coarse-graining.
- What is *not* invariant across scales: the **numerical values** of `(M_0, P_0, ζ, τ)`. These are regime-specific and are exactly what the Dimensional Atlas maps per regime. The `β_i ≠ 0` result predicts this: the atlas's per-regime coupling maps *must* be non-trivial; a single universal coupling value is ruled out.
- What this means operationally: the cross-scale-invariance claim should be read as "the ED PDE *form* is a fixed operator family under Wilsonian coarse-graining, with regime-specific coupling maps that flow between scales," not as "the ED PDE *with its numerical values* is the same everywhere."

**7.5 Concrete predictions.**

(i) Running of `P_0 ∝ b^2` is a universal scaling, independent of regime. The Dimensional Atlas regimes should therefore satisfy `P_0(L_{\text{regime}}) \cdot L_{\text{regime}}^2 / M_0 \approx \text{const}` to leading order — i.e., the ratio `ξ/L_{\text{regime}}` is approximately regime-invariant. (Cross-check candidate.)

(ii) The participation channel becomes irrelevant at scales above `ξ_v = √(M_0 τ/ζ)`. Regimes with measured-unit-scales much larger than `ξ_v` should not show oscillatory/Hamiltonian signatures. Regimes with measured scales below `ξ_v` should show them. This predicts the oscillatory/coherent sector of ED is IR-projected out above `ξ_v`, consistent with the ED-09.5 Q-C transition at the participation-damping scale.

(iii) The cubic penalty coupling `P_3` and nonlinear mobility `M_2` are marginal for mutually exclusive choices of `χ` — which means ED's generic bare theory (both nonzero) has *exactly one* marginal and *exactly one* relevant/irrelevant nonlinear coupling. Which is which depends on the observable being normalised. This is a testable structural feature rather than a free choice: at the Wilson-Fisher choice `χ = 1`, `M_2` decays as `b^{-2}` under coarse-graining — nonlinear-mobility signatures should therefore be strong in microscopic regimes (condensed matter, FRAP) and weak in macroscopic regimes (galactic, cosmological). Qualitatively consistent with observation.

---

## Appendix A — Condensed verdict card

| Question | Answer |
|:---|:---|
| ED operator basis closed under coarse-graining? | **Yes**, at tree and one-loop. |
| All ED β-functions vanish at physical couplings? | **No**. `β_{P_0} = 2P_0 ≠ 0`, `β_\zeta = 2\zeta ≠ 0`, `β_\tau = −2\tau ≠ 0`. |
| ED is an RG fixed point? | **No**. |
| ED form survives RG? | **Yes** (form-closed). |
| Cross-scale invariance of ED: structural or approximate? | **Structural in operator form, approximate in couplings.** |
| Minimal operator extension required for coupling closure? | **None exists**: relevance is power-counted and cannot be altered by adding operators. |
| Participation channel fate under RG? | **IR-irrelevant**: `τ → 0`, `v` slaves to `F[δ]/ζ`, collapsing to single-channel Model A. |
| UV fixed points available? | **Gaussian** and **Wilson-Fisher**-like cubic; ED bare theory near neither. |
| Atlas-scale reuse reinterpretation | Per-regime coupling maps (required, since β ≠ 0) over a shared, form-closed operator basis. |
