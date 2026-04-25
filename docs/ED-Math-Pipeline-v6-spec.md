# ED Math Pipeline — v6 Specification

**Status.** Text-based hierarchical spec for the v6 poster. Extends v5 (docs/figures/ED-Math-Pipeline_v5.png) with the Wilsonian RG arc closed on 2026-04-22 (sixth pass): operator form-closure, β-functions, fixed-point catalog, flow invariants, the ED window, the three effective PDEs (UV / Intermediate / IR), and the 0.6 resolution. No size constraint on the final poster; new rows and branches added freely.

**Source memos for the new material:**
- `theory/ED_RG_Flow_Analysis.md`
- `theory/ED_RG_Flow_Geometry.md`
- `theory/ED_IR_Effective_PDE.md`
- `theory/ED_UV_PDE_and_Three_Regime_Flow.md`
- `theory/The_0_6_Problem_Resolution.md`

---

## Part A — Inventory of new math objects to insert

### A.1 Operator identities

- Divergence-form identity: `∇·(M(δ)∇δ) = M(δ)∇²δ + M'(δ)|∇δ|²` — ties the two Z₂-even mobility operators `δ²∇²δ` and `δ|∇δ|²`; preserved under RG only when div-form is preserved.
- Z₂ symmetry adopted: `(δ, v) → (−δ, −v)` ⇒ `M_1 = 0`, even `P` vanish.
- Taylor expansions: `M(δ) = M_0 + ½M_2 δ² + …`, `P(δ) = P_0 δ + (1/6)P_3 δ³ + …`.
- Full expanded `F[δ]`:
  `F[δ] = M_0∇²δ + ½M_2 δ²∇²δ + M_2 δ|∇δ|² − P_0 δ − (1/6)P_3 δ³ + O(δ⁴∇²δ)`.
- Gradient-flow Lyapunov (`H = 0, ζ = 0` single-channel):
  `L[δ] = ∫[½M_0(∇δ)² + ½P_0 δ² + P_3 δ⁴/24 + …]`.

### A.2 Wilsonian coarse-graining map

- Momentum shell: keep `|k| < Λ/b`, integrate out `Λ/b ≤ |k| < Λ`, `b > 1`.
- Rescaling: `x' = x/b, t' = t/b^z, δ' = b^χ δ_<, v' = b^{χ_v} v_<`.
- Dynamic exponent `z = 2` (diffusive / Model A).
- Field exponent `χ` free in deterministic theory; two canonical choices:
  - `χ = 0` (Gaussian): `M_2` marginal, `P_3` relevant.
  - `χ = 1` (Wilson-Fisher-like): `P_3` marginal, `M_2` irrelevant.
- Coupling `χ_v = χ` forced by `P_0` cross-coupling consistency.

### A.3 Scaling dimensions at z = 2

| Operator          | Coupling | Dimension λ   | Relevant / Marginal / Irrelevant                     |
|:------------------|:---------|:--------------|:-----------------------------------------------------|
| `∇²δ`             | `M_0`    | `0`           | marginal                                             |
| `δ`               | `P_0`    | `+2`          | relevant                                             |
| `v` (ODE kinetic) | `τ`      | `−2`          | irrelevant (τ → 0 in IR)                             |
| `v` (ODE damping) | `ζ`      | `+2`          | relevant                                             |
| `δ³`              | `P_3`    | `2 − 2χ`      | rel (χ<1) / marg (χ=1) / irr (χ>1)                   |
| `δ²∇²δ`           | `M_2`    | `−2χ`         | rel (χ<0) / marg (χ=0) / irr (χ>0)                   |
| `δ\|∇δ\|²`         | `M_2`    | `−2χ`         | tied to `δ²∇²δ` by div-form identity                 |
| `∇⁴δ`             | —        | `−2`          | irrelevant (not generated at tree level)             |

### A.4 β-functions (tree level, z = 2)

```
β_{M_0} = 0                    (marginal — never flows)
β_{P_0} = +2 P_0
β_{ζ}   = +2 ζ
β_{τ}   = −2 τ
β_{P_3} = (2 − 2χ) P_3
β_{M_2} = −2χ M_2
```

Integrated trajectories (with `ℓ = ln b`):

```
M_0(ℓ) = M_0
P_0(ℓ) = P_0 · e^{+2ℓ}
ζ(ℓ)   = ζ   · e^{+2ℓ}
τ(ℓ)   = τ   · e^{−2ℓ}
P_3(ℓ) = P_3 · e^{(2−2χ)ℓ}
M_2(ℓ) = M_2 · e^{−2χℓ}
```

### A.5 Fixed points

| FP                    | `P_0` | `ζ` | `τ` | `P_3` | `M_2` | `χ`     | Role                                             |
|:----------------------|:------|:----|:----|:------|:------|:--------|:-------------------------------------------------|
| Gaussian `G`          | 0     | 0   | ∞*  | 0     | 0     | any     | UV-stable; codim-3 (χ=0) or codim-2 (χ=1)       |
| Wilson–Fisher line WF | 0     | 0   | ∞*  | any   | 0     | `χ = 1` | cubic marginal; φ⁴-like relaxational            |
| Nonlinear-mob line NM | 0     | 0   | ∞*  | 0     | any   | `χ = 0` | `M_2` marginal; Gaussian field, nonlinear mobility |
| "Point at infinity"   | ∞     | ∞   | 0   | —     | —     | —       | universal IR sink; trivial massive phase (δ≡0)   |

\*`τ → ∞` is the asymptotic IR-irrelevant limit but is a sink only as `τ → 0`; at FPs the τ axis sits at its trivial fixed direction.

Stability matrix `J_{ij} = ∂β_i/∂g_j` is **diagonal** at every FP in this basis.

At `G`: eigenvalues `(2, 2, −2, 2−2χ, −2χ)` for `(P_0, ζ, τ, P_3, M_2)`.
- `χ = 0`: 3 relevant, 1 irrelevant, 1 marginal (codim-3 unstable manifold).
- `χ = 1`: 2 relevant, 2 irrelevant, 1 marginal (codim-2 unstable manifold).

### A.6 Flow invariants

Exactly conserved along any trajectory (ratios with cancelling scaling dimensions):

```
R_1 = P_0 / ζ           (penalty-to-damping; channel-weight-independent)
R_2 = P_0 · τ
R_3 = ζ  · τ
```

χ-dependent additional invariants:

```
χ = 0:   P_3 / P_0 invariant;   M_2 constant.
χ = 1:   P_3 constant;          P_0 · M_2^{1/0}  (see memo §4).
```

### A.7 Crossover scales — the ED window

```
ℓ_v  = ½ ln(ξ_v Λ)       participation-slaving onset (τ(ℓ_v) ≈ 1/ζ)
ℓ_ξ  = ln(ξ Λ)           gap scale (correlation length ξ = √(M_0/P_0))
```

- `ℓ < ℓ_v`              UV regime (participation free, wave-like).
- `ℓ_v < ℓ < ℓ_ξ`        Intermediate regime (the "ED window").
- `ℓ > ℓ_ξ`              IR regime (gapped, linear, trivial).

### A.8 Participation-channel limit rules

- **IR slaving (τ → 0):** `v = F[δ]/ζ` (algebraic; v-ODE disappears).
  Leading correction: `v = F[δ]/ζ − (τ/ζ²) ∂_t F[δ] + O(τ²)`.
- **UV freezing (τ → ∞):** `v̇ ≈ F[δ]/τ → 0`, so `v(t) = v_0 + O(1/τ)` static.
- **Intermediate:** slaving holds but `ζ` finite, giving `Γ_eff = D + H/ζ`.

### A.9 Three effective PDEs (boxed)

```
UV            ∂_t δ = D M_0 ∇²δ + H v,        τ v̇ = M_0 ∇²δ
              (free two-channel diffusion; v frozen; wave-like dispersion)

Intermediate  ∂_t δ = Γ_eff [ M_0 ∇²δ + ½M_2 δ²∇²δ + M_2 δ|∇δ|²
                              − P_0 δ − (1/6)P_3 δ³ ]
              with  Γ_eff = D + H/ζ   (Model A universality class)

IR            ∂_t δ = D M_0 ∇²δ − D P_0(ℓ) δ,   P_0(ℓ) → ∞,  δ → 0
              Equivalent: ∂_t δ = D M_0 (∇² − m²(ℓ)) δ,  m² = P_0/M_0
              Solution:   δ(x,t) = e^{−D M_0 m² t}[e^{D M_0 t ∇²} δ(x,0)]
```

### A.10 Operator on/off map across regimes

| Operator              | UV       | Intermediate            | IR                    |
|:----------------------|:---------|:------------------------|:----------------------|
| `M_0 ∇²δ`             | ON       | ON (coeff `Γ_eff M_0`)  | ON (coeff `D M_0`)    |
| `P_0 δ`               | off      | ON (coeff `−Γ_eff P_0`) | ON, dominant (grows)  |
| `δ²∇²δ`, `δ\|∇δ\|²`   | off      | ON (χ-dependent)        | off (amp. suppression)|
| `P_3 δ³`              | off      | ON (χ-dependent)        | off (amp. suppression)|
| `H v` (independent)   | ON       | slaved ⇒ `H/ζ · F[δ]`   | slaved, → 0 (ζ→∞)     |
| `τ v̇`                | ON (frozen) | slaved (drops out)    | slaved (drops out)    |

### A.11 Structural closure statements

- **Form closure theorem.** Under Wilsonian coarse-graining at tree level and one loop, no operators outside the Z₂-symmetric reduced basis `{∇²δ, δ, δ³, δ²∇²δ, δ|∇δ|², v, v̇, H v}` are generated. The canonical ED ansatz is a theorem, not a guess.
- **ED is not a fixed point.** At physical couplings `(P_0, ζ, τ) ≠ 0` all three β-functions are non-zero. Cross-scale invariance is therefore structural in *form*, not in *couplings*.
- **IR is a trivial massive phase.** No interacting IR fixed point exists; flow endpoint is `δ ≡ 0` ("fixed point at infinity").
- **UV origin is Gaussian G.** All trajectories start from a neighbourhood of `G` and cross the ED window before gapping out.
- **ED window `[ℓ_v, ℓ_ξ]` is the domain of ED-specific phenomenology.** UDM β = 2, Q–C transition, C7 triad, mobility capacity, saturating penalty all live here.

### A.12 The 0.6 resolution

```
Dictionary:    T_0 = L_0^2 · D_nd / D_phys
Anchors:       L_0     = ℏ / (mc)       (reduced Compton)
               D_phys  = ℏ / (2m)       (Madelung)
               D_nd    = 0.3            (cross-regime invariant)
Identity:      T_0 = 2·D_nd · ℏ/(mc²) = 0.6 · ℏ/(mc²)
Side identity: c_0 / c = 1 / (2 D_nd)   ⇒  c_0 = c at D_nd = 1/2
```

Audit: five alternative routes fail (damping discriminant, reversible-slice QFT dispersion, acoustic-metric curvature, PME coarse-graining, ζ-interpolation). Only the algebraic dictionary route succeeds. `0.6` is structurally fixed by the choice `D_nd = 0.3`.

---

## Part B — Full hierarchical pipeline (v6)

Rows numbered top → bottom. Each row is a horizontal band in the poster. Arrows between rows labeled with the transition semantics.

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  ROW 0 — TITLE                                                               ║
║  "ED — The Math Pipeline (v6)"                                               ║
║  from ED-05 axioms → unique PDE → RG flow → three regimes → predictions      ║
╚══════════════════════════════════════════════════════════════════════════════╝
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW 1 — ED-05 PRE-PDE AXIOMS (bare event domain)                            │
│                                                                              │
│  A1: ED(A) ≥ 0               A2: ED(∅) = 0                                   │
│  A3: A ⊆ B ⇒ ED(A) ≤ ED(B)   A4: ED(A∪B) ≤ ED(A) + ED(B)                     │
│                                                                              │
│  non-negativity / null baseline / monotonicity / subadditivity               │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │ counting is structured
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW 2 — SEVEN CONSTRAINTS (the pre-architectural gate)                      │
│                                                                              │
│  C1 Locality               F[ρ](x) ← ρ(x + ε)                                │
│  C2 Isotropy               F[Rρ] = R F[ρ]                                    │
│  C3 Gradient-driven flow   J = −M(ρ)∇ρ                                       │
│  C4 Dissipative            dE/dt ≤ 0                                         │
│  C5 Single scalar field    ρ : ℝ^d × ℝ → ℝ                                   │
│  C6 Minimal coupling       ρ ↔ v  (one loop)                                 │
│  C7 Dimensional consistency [LHS] = [RHS]                                    │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │ filtered through the frame
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW 3 — COMPOSITIONAL RULE  (cosmological specialisation of A4)             │
│                                                                              │
│  p(A∪B) = p(A) + p(B)                                                        │
│         − α ∫_{A∩B} p^γ dμ                                                   │
│         − β ∫_{A∪B} |∇p|² dμ                                                 │
│         − γ ∫_{∂(A∪B)} h(|∇p|) dS                                            │
│                                                                              │
│  relational penalty  +  gradient penalty  +  boundary / horizon term         │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │ structure
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW 4 — ARCHITECTURAL CANON P1–P7  +  D.19 UNIQUENESS                       │
│                                                                              │
│  P1 operator structure    F[ρ] = M(ρ)∇²ρ + M'(ρ)|∇ρ|² − P(ρ)                 │
│  P2 channel complement.   ∂_t ρ = D·F[ρ] + H·v,  D+H=1                       │
│  P3 penalty equilibrium   P(ρ*) = 0,  P'(ρ*) > 0                             │
│  P4 mobility capacity     M(ρ_max) = 0, M(ρ) > 0 for ρ < ρ_max               │
│  P5 participation FB      τ v̇ = F̄[ρ] − ζ v                                   │
│  P6 damping discriminant  (D−ζ)² < 4(1−D); D_crit ≈ 0.896 (ζ=1/4)            │
│  P7 nonlinear triad       M'(ρ)|∇ρ|² generates k_3 = k_1 ± k_2               │
│                                                                              │
│  D.19  UNIQUENESS — no freedom to choose; the PDE is selected uniquely       │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │ forced  (Theorem D.19)
                                    ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║  ROW 5 — THE UNIFIED PDE                                                     ║
║                                                                              ║
║  ∂_t ρ = D · [ M(ρ)∇²ρ + M'(ρ)|∇ρ|² − P(ρ) ]  +  H · v                       ║
║  τ v̇   = F̄(ρ) − ζ v                                                          ║
║                                                                              ║
║  M(ρ) = M_0 (ρ_max − ρ)^β                                                    ║
║  P_SY2(ρ) = αγ (ρ − ρ*) / √((ρ − ρ*)² + ρ_0²)                                ║
║                                                                              ║
║  Working form (δ := ρ − ρ*, Z₂):                                             ║
║  F[δ] = M_0 ∇²δ + ½ M_2 δ²∇²δ + M_2 δ|∇δ|² − P_0 δ − (1/6)P_3 δ³ + …         ║
╚══════════════════════════════════════════════════════════════════════════════╝
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌──────────────────┐       ┌──────────────────┐       ┌──────────────────┐
│ branch A —       │       │ branch B — RG    │       │ branch C —       │
│ channels &       │       │ flow geometry    │       │ dimensional      │
│ textbook         │       │  (NEW, v6)       │       │ dictionary       │
│ reductions       │       │                  │       │  (NEW, v6)       │
│  (as in v5)      │       │                  │       │                  │
└──────────────────┘       └──────────────────┘       └──────────────────┘

════════════════════════════════════════════════════════════════════════════════
                 BRANCH B — WILSONIAN RG FLOW  (new spine, v6)
════════════════════════════════════════════════════════════════════════════════

                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW 6 — WILSONIAN COARSE-GRAINING MAP                                       │
│                                                                              │
│  Shell:      keep |k| < Λ/b,  integrate out Λ/b ≤ |k| < Λ                    │
│  Rescale:    x' = x/b,  t' = t/b^z,  δ' = b^χ δ_<,  v' = b^{χ_v} v_<         │
│  z = 2       dynamic exponent (diffusive / Model A)                          │
│  χ           field scaling exponent (free in deterministic theory)           │
│  χ_v = χ     forced by P_0 cross-coupling consistency                        │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW 7 — FORM-CLOSURE THEOREM                                                │
│                                                                              │
│  At tree level and one loop, the RG map generates no operators outside       │
│  the Z₂-symmetric reduced basis                                              │
│                                                                              │
│       { ∇²δ ,  δ ,  δ³ ,  δ²∇²δ ,  δ|∇δ|² ,  v ,  v̇ ,  H v }                 │
│                                                                              │
│  Div-form identity  ∇·(M(δ)∇δ) = M(δ)∇²δ + M'(δ)|∇δ|²                        │
│  ties δ²∇²δ and δ|∇δ|² coefficients.                                         │
│                                                                              │
│       ⇒  ED operator ansatz is a THEOREM, not a guess.                       │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW 8 — TREE-LEVEL SCALING DIMENSIONS (at z = 2)                            │
│                                                                              │
│   Operator       Coupling    λ             Relevance                         │
│   ─────────────  ────────    ──────        ────────────────────────────      │
│   ∇²δ            M_0         0             marginal                          │
│   δ              P_0         +2            relevant                          │
│   v̇              τ           −2            irrelevant                        │
│   v              ζ           +2            relevant                          │
│   δ³             P_3         2 − 2χ        rel (χ<1) / marg (χ=1)            │
│   δ²∇²δ          M_2         −2χ           marg (χ=0) / irr (χ>0)            │
│   δ|∇δ|²         M_2         −2χ           (tied to δ²∇²δ)                   │
│   ∇⁴δ            —           −2            irrelevant; not generated         │
│                                                                              │
│   Two canonical χ-choices:                                                   │
│     χ = 0  (Gaussian)          — M_2 marginal, P_3 relevant                  │
│     χ = 1  (Wilson-Fisher-like)— P_3 marginal, M_2 irrelevant                │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW 9 — β-FUNCTIONS                                                         │
│                                                                              │
│    β_{M_0} = 0                (marginal — never flows)                       │
│    β_{P_0} = +2 P_0                                                          │
│    β_{ζ}   = +2 ζ                                                            │
│    β_{τ}   = −2 τ                                                            │
│    β_{P_3} = (2 − 2χ) P_3                                                    │
│    β_{M_2} = −2χ M_2                                                         │
│                                                                              │
│  Integrated trajectories (ℓ = ln b):                                         │
│    P_0(ℓ) = P_0 · e^{+2ℓ}    ζ(ℓ)   = ζ · e^{+2ℓ}    τ(ℓ) = τ · e^{−2ℓ}      │
│    P_3(ℓ) = P_3 · e^{(2−2χ)ℓ}  M_2(ℓ) = M_2 · e^{−2χℓ}                       │
│                                                                              │
│  At physical couplings (P_0, ζ, τ) ≠ 0 → ED is NOT a fixed point.            │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW 10 — FIXED-POINT CATALOG                                                │
│                                                                              │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   │
│  │ Gaussian  G  │   │  WF line     │   │  NM line     │   │  Point at ∞  │   │
│  │              │   │  (χ = 1)     │   │  (χ = 0)     │   │              │   │
│  │ P_0=0 ζ=0    │   │ P_3 free     │   │ M_2 free     │   │ P_0→∞, ζ→∞   │   │
│  │ P_3=0 M_2=0  │   │ M_2 = 0      │   │ P_3 = 0      │   │ τ → 0         │   │
│  │ UV-stable    │   │ marginal φ⁴  │   │ marginal NM  │   │ IR sink      │   │
│  │ codim 3 (χ=0)│   │ line         │   │ line         │   │ trivial mass │   │
│  │ codim 2 (χ=1)│   │              │   │              │   │ phase (δ≡0)  │   │
│  └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   │
│                                                                              │
│  Jacobian J_{ij} = ∂β_i/∂g_j is DIAGONAL at every FP.                        │
│  Eigenvalues at G: (2, 2, −2, 2−2χ, −2χ) for (P_0, ζ, τ, P_3, M_2).          │
│                                                                              │
│  ED physical theory: UV near G → trajectory crosses ED window → IR to ∞.     │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW 11 — FLOW INVARIANTS (exactly RG-conserved on every trajectory)         │
│                                                                              │
│    R_1 = P_0 / ζ           penalty-to-damping ratio                          │
│    R_2 = P_0 · τ                                                             │
│    R_3 = ζ  · τ                                                              │
│                                                                              │
│    χ = 0:   P_3 / P_0  invariant;    M_2 constant                            │
│    χ = 1:   P_3 constant                                                     │
│                                                                              │
│  These foliate the flow — every trajectory is labelled by (R_1, R_2, R_3).   │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW 12 — CROSSOVER SCALES :: THE ED WINDOW                                  │
│                                                                              │
│        ℓ_v = ½ ln(ξ_v Λ)        participation-slaving onset                  │
│        ℓ_ξ = ln(ξ Λ)            gap scale  (ξ = √(M_0/P_0))                  │
│                                                                              │
│  ℓ → −∞  ──────── ℓ_v ──────── ℓ_ξ ──────── ℓ → +∞                           │
│                                                                              │
│    UV                 INTERMEDIATE                 IR                        │
│  v free            v = F[δ]/ζ slaved            v → 0                        │
│  wave-like         Model A universality         linear gapped                │
│  massless          nonlinearities active        δ → 0 exponentially          │
│                                                                              │
│   ◄──── ED-specific phenomenology lives ONLY in ℓ_v < ℓ < ℓ_ξ ────►          │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW 13 — PARTICIPATION-CHANNEL LIMIT RULES                                  │
│                                                                              │
│   IR slaving  (τ → 0):    v = F[δ]/ζ       (v-ODE disappears)                │
│                            + correction:  − (τ/ζ²) ∂_t F[δ] + O(τ²)          │
│                                                                              │
│   UV freezing (τ → ∞):    v̇ → 0           v(t) = v_0 + O(1/τ)  static        │
│                                                                              │
│   Intermediate:           slaved, ζ finite → Γ_eff = D + H/ζ                 │
│                                                                              │
│  (Opposite limits of the same v-ODE τ v̇ = F[δ] − ζ v.)                       │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║  ROW 14 — THREE EFFECTIVE PDEs  (one box per regime)                         ║
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │ UV     (ℓ < ℓ_v)                                                       │  ║
║  │                                                                        │  ║
║  │   ∂_t δ = D M_0 ∇²δ + H v                                              │  ║
║  │   τ v̇  = M_0 ∇²δ                                                       │  ║
║  │                                                                        │  ║
║  │   Free two-channel diffusion. v frozen at τ → ∞.                       │  ║
║  │   Long-wavelength dispersion:   ω² ∝ k²   (WAVE-LIKE).                 │  ║
║  │   Matches kinematic acoustic-metric / free-scalar QFT regime           │  ║
║  │   (ED-10 fourth-pass arc).                                             │  ║
║  │   Crossover k_* = √( H / (τ D M_0) ).                                  │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │ INTERMEDIATE   (ℓ_v < ℓ < ℓ_ξ) — THE ED WINDOW                         │  ║
║  │                                                                        │  ║
║  │   ∂_t δ = Γ_eff [  M_0 ∇²δ                                             │  ║
║  │                  + ½ M_2 δ² ∇²δ                                        │  ║
║  │                  + M_2 δ |∇δ|²                                         │  ║
║  │                  − P_0 δ                                               │  ║
║  │                  − (1/6) P_3 δ³   ]                                    │  ║
║  │                                                                        │  ║
║  │   Γ_eff = D + H/ζ                                                      │  ║
║  │                                                                        │  ║
║  │   Universality class: Model A.                                         │  ║
║  │   Home of UDM β=2, Q-C transition, C7 triad, mobility capacity,        │  ║
║  │   saturating penalty, horizon formation, ED-SC 2.0 invariants.         │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │ IR     (ℓ > ℓ_ξ)                                                       │  ║
║  │                                                                        │  ║
║  │   ∂_t δ = D M_0 ∇²δ − D P_0(ℓ) δ,        P_0(ℓ) → ∞                    │  ║
║  │   ≡      D M_0 ( ∇² − m²(ℓ) ) δ,         m² = P_0/M_0                  │  ║
║  │                                                                        │  ║
║  │   Solution:  δ(x,t) = e^{−D M_0 m² t} · [ e^{D M_0 t ∇²} δ(x,0) ]      │  ║
║  │   Endpoint:  δ → 0 pointwise, exponentially.                           │  ║
║  │                                                                        │  ║
║  │   Two-stage elimination of nonlinearities:                             │  ║
║  │     (i)  RG irrelevance (χ-dependent)                                  │  ║
║  │     (ii) Field-amplitude suppression: |δ| → 0 ⇒ O(δ^{k≥2}) → 0         │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
╚══════════════════════════════════════════════════════════════════════════════╝
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW 15 — OPERATOR ON / OFF MAP ACROSS REGIMES                               │
│                                                                              │
│  Operator          │  UV         │  Intermediate           │  IR             │
│  ─────────────────── ─────────── ───────────────────────── ────────────────  │
│  M_0 ∇²δ           │  ON         │  ON  (Γ_eff M_0)        │  ON (D M_0)     │
│  P_0 δ             │  off        │  ON  (−Γ_eff P_0)       │  ON (dominant)  │
│  δ²∇²δ, δ|∇δ|²     │  off        │  ON  (χ-dep.)           │  off (|δ|→0)    │
│  P_3 δ³            │  off        │  ON  (χ-dep.)           │  off (|δ|→0)    │
│  H v (independent) │  ON         │  slaved → (H/ζ) F[δ]    │  → 0 (ζ→∞)      │
│  τ v̇               │  ON (frozen)│  slaved (drops)         │  slaved (drops) │
│                                                                              │
│  ED window ≡ intersection of "nonlinearities on" and "v slaved, ζ finite".   │
└──────────────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════════════
     BRANCH A — CHANNELS, REDUCTIONS, PREDICTIONS  (v5 spine, preserved)
════════════════════════════════════════════════════════════════════════════════

                                    │  turn each channel on alone
                                    ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ MOBILITY         │  │ PENALTY          │  │ PARTICIPATION    │
│ channel alone    │  │ channel alone    │  │ channel alone    │
│                  │  │                  │  │                  │
│ ∂_t ρ =          │  │ ∂_t ρ =          │  │ τ v̇ + ζ v = F̄(ρ) │
│   D ∇·[M(ρ)∇ρ]   │  │   −D P_0(ρ−ρ*)   │  │                  │
└──────────────────┘  └──────────────────┘  └──────────────────┘
          │                     │                     │
          ▼                     ▼                     ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ POROUS MEDIUM    │  │ DEBYE / RC       │  │ TELEGRAPH / RLC  │
│ ∂_t δ =          │  │ ρ(t) = ρ* +      │  │ τ v̈ + ζ v̇ + v=0  │
│   D_pme ∇²(δ^m)  │  │   (ρ_0−ρ*)       │  │                  │
│ m = β + 1        │  │   e^{−D P_0 t}   │  │ ω = √(1/τ −      │
│ R(t) ∝           │  │ τ_RC = 1/(D P_0) │  │     (ζ/2τ)²)     │
│ t^{1/(d(m−1)+2)} │  │                  │  │                  │
└──────────────────┘  └──────────────────┘  └──────────────────┘
          │                     │                     │
          ▼                     ▼                     ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ UDM  (CONFIRMED) │  │ CLUSTER MERGER-  │  │ FRAP on BSA      │
│                  │  │ LAG (CONFIRMED)  │  │ (PENDING)        │
│ D(c) =           │  │ ℓ = D_T/v_curr   │  │ τ ρ̈ + ζ ρ̇ + ρ=0  │
│   D_0(1−c/c_max)^β│  │                  │  │                  │
│ 10 materials,    │  │ D_T = 2.1×10^27  │  │ Creative         │
│ 8 mechanisms,    │  │ m²/s (Mistele WL)│  │ Proteomics tech  │
│ R² > 0.986       │  │ 7 clusters +     │  │ review window    │
│                  │  │ Finner+25 (58)   │  │                  │
└──────────────────┘  └──────────────────┘  └──────────────────┘

════════════════════════════════════════════════════════════════════════════════
           BRANCH C — DIMENSIONAL DICTIONARY + 0.6 RESOLUTION  (NEW, v6)
════════════════════════════════════════════════════════════════════════════════

                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW D1 — ED DIMENSIONAL DICTIONARY                                          │
│                                                                              │
│   T_0 = L_0² · D_nd / D_phys                                                 │
│                                                                              │
│   Quantum anchors (Madelung theorem):                                        │
│     L_0     = ℏ / (mc)      reduced Compton wavelength                       │
│     D_phys  = ℏ / (2m)      Madelung diffusion coefficient                   │
│     D_nd    = 0.3           cross-regime nondimensional invariant            │
│                                                                              │
│   Universal invariant:  D_phys · T_0 / L_0² = 0.3                            │
│   verified exactly across 5 regimes (≈ 61 OOM):                              │
│     Quantum / Planck / Condensed Matter / Galactic / Cosmological            │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  ROW D2 — 0.6 RESOLUTION                                                     │
│                                                                              │
│    T_0 = 2 · D_nd · ℏ/(mc²) = 0.6 · ℏ/(mc²)                                  │
│                                                                              │
│    ⇒  "0.6" is fixed by D_nd = 0.3 — not a free constant.                    │
│                                                                              │
│    Side identity:    c_0 / c = 1 / (2 D_nd)                                  │
│                      c_0 = c  exactly at D_nd = 1/2                          │
│                                                                              │
│    Audit — five routes tested, four fail:                                    │
│       (1) damping discriminant D_crit ..... FAIL                             │
│           (2) reversible-slice QFT dispersion .. FAIL                        │
│           (3) acoustic-metric curvature ......... FAIL                       │
│           (4) PME coarse-graining coincidence ... FAIL                       │
│           (5) ζ-interpolation ................... FAIL                       │
│       ( * ) algebraic dictionary identity ....... PASS  ✓                    │
└──────────────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════════════
              ROW 16 — CROSS-SCALE INVARIANCE RESTATED  (NEW, v6)
════════════════════════════════════════════════════════════════════════════════

┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│   "ED across 20–60 OOM"  is NOT coupling-invariance.                         │
│                                                                              │
│   Couplings FLOW per β-functions. What recurs across scales is:              │
│                                                                              │
│       ├─ operator structure of the canonical PDE (form-closure)              │
│       ├─ triad  { mobility , penalty , participation }                       │
│       ├─ Model A universality inside the ED window                           │
│       └─ the ED-SC 2.0 motif-conditioned Hessian invariant  r* ≈ −1.304      │
│                                                                              │
│   What is regime-specific:                                                   │
│       ├─ window location (ℓ_v, ℓ_ξ values)                                   │
│       ├─ coupling values (P_0, ζ, τ, M_0 ...)                                │
│       └─ which empirical signatures activate (UDM / merger-lag / FRAP / …)   │
│                                                                              │
│   Cross-scale invariance is STRUCTURAL IN FORM, APPROXIMATE IN COUPLINGS.    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════════════
            ROW 17 — STRUCTURAL FORKS RIBBON  (v5 preserved + v6 extended)
════════════════════════════════════════════════════════════════════════════════

┌──────────────────────────────────────────────────────────────────────────────┐
│   …and these also fall out of the same equation, no additional assumptions:  │
│                                                                              │
│  dimensional invariant      D · T_0 / L_0² = 0.3     (5 regimes, 61 OOM)     │
│  sharp bifurcation          (D−ζ)² = 4(1−D) ⇒ D_crit ≈ 0.896 (ζ=1/4)         │
│  universal invariants       E_g = αγρ_0;  t_rel ≈ ρ_0/(αγ)                   │
│  triad coupling             C ≈ 0.03;  K = A_3/A_1^3 ≈ 0.0148                │
│                             K_2 = A_2/A_1^2 ≈ 0.279;  φ_3 − 3φ_1 = π         │
│  d-consistency              α_R = 1/(d(m−1) + 2)    (d = 1,2,3 exact)        │
│  ED-SC 2.0 invariant        r* = med R_motif(∇²E) ≈ −1.304                   │
│                                                                              │
│  ─── NEW v6 additions ─────────────────────────────────────────────────────  │
│                                                                              │
│  form closure (RG)          ED operator basis is closed under coarse-graining│
│  flow invariants            R_1 = P_0/ζ,  R_2 = P_0·τ,  R_3 = ζ·τ            │
│  fixed-point geometry       G  +  WF(χ=1) line  +  NM(χ=0) line  +  ∞ (sink) │
│  ED window                  ℓ_v = ½ln(ξ_v Λ),  ℓ_ξ = ln(ξ Λ)                 │
│  IR endpoint                δ → 0  (trivial massive phase)                   │
│  UV endpoint                Gaussian free two-channel + wave-like dispersion │
│  0.6 identity               0.6 = 2·D_nd(quantum);  c_0 = c/0.6              │
│  χ-selection                χ=0 Gaussian / χ=1 WF — selects which            │
│                              nonlinearity is marginal                        │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Part C — Implementation notes for the poster

- **Canvas.** v5 was 22.0 × 20.6. v6 needs ≈ 24.0 × 30.0 to accommodate the RG spine (rows 6–15) as a vertical column parallel to branch A. Alternatively split into a two-page poster: page 1 = rows 0–5 + branch A; page 2 = branches B (RG) + C (dictionary) + rows 16–17.
- **Colour additions beyond v5 palette.**
  - RG spine (rows 6–15): new colour family `RG_SPINE = "#dceafc"` with edge `"#2b4d7a"`.
  - Fixed-point catalog cells (row 10): four micro-palette swatches — Gaussian `"#eef5ff"`, WF `"#f5eef9"`, NM `"#eef9ef"`, Point-at-∞ `"#f9efef"`.
  - Three-regime PDE row (row 14): UV `"#eef0f9"`, Intermediate `"#f3ece1"` (same as v5 CHANNEL), IR `"#e7e2d4"`.
  - Branch C dictionary (rows D1/D2): reuse CONFIRMED `"#d3ebd6"` but with an "ID" (identity) badge rather than "CONFIRMED".
- **Arrow semantics.**
  - PDE → RG spine arrow label: "coarse-grain: b, z=2".
  - RG spine → three-regime box arrow label: "integrate β to ℓ = ℓ_v, ℓ_ξ".
  - Three-regime box → branch A reductions arrow label: "in the ED window, channel limits are textbook reductions".
  - Branch C row D2 → forks row 17 label: "structural identity, not constant".
- **Consistency with existing memos.** Every equation on the poster is sourced directly from the five authoritative memos listed at the top of this file. No new math is introduced here; the poster is a rendering of those memos.
- **Guardrails to preserve in caption text.**
  - "ED is form-closed but NOT a fixed point."
  - "Cross-scale invariance is structural in form, approximate in couplings."
  - "ED-specific phenomenology lives in ℓ_v < ℓ < ℓ_ξ only."
  - "0.6 is fixed by D_nd = 0.3, not a free constant."
  - "Participation slaving (IR, τ→0) and participation freezing (UV, τ→∞) are opposite limits of one v-ODE."

---

## Part D — Cross-reference map

| v6 row | Source memo                               | Section                             |
|:-------|:------------------------------------------|:------------------------------------|
| 6      | `ED_RG_Flow_Analysis.md`                  | §2 coarse-graining map              |
| 7      | `ED_RG_Flow_Analysis.md`                  | §1.2 operator basis; §3–§4 closure  |
| 8      | `ED_RG_Flow_Analysis.md`                  | §5 scaling dimensions               |
| 9      | `ED_RG_Flow_Geometry.md`                  | §1 β-functions                      |
| 10     | `ED_RG_Flow_Geometry.md`                  | §2 fixed points + §3 Jacobian       |
| 11     | `ED_RG_Flow_Geometry.md`                  | §4.2 invariants                     |
| 12     | `ED_UV_PDE_and_Three_Regime_Flow.md`      | §4 three-regime flow diagram        |
| 13     | `ED_IR_Effective_PDE.md` §2 (slaving);    | `ED_UV_PDE_and_Three_Regime_Flow.md` §2 (freezing) |
| 14     | `ED_IR_Effective_PDE.md` §5 (IR boxed);   | `ED_UV_PDE_and_Three_Regime_Flow.md` §3/§5 (UV + Intermediate + consolidation) |
| 15     | `ED_UV_PDE_and_Three_Regime_Flow.md`      | §5 operator on/off table            |
| 16     | `ED_RG_Flow_Geometry.md` §6;              | `ED_UV_PDE_and_Three_Regime_Flow.md` §6.2 |
| D1/D2  | `The_0_6_Problem_Resolution.md`           | dictionary identity + five-route audit |

---

**End of v6 spec.** Next step: implement as `analysis/scripts/generate_ed_math_pipeline_v6.py` (extend v5 with three new vertical columns: RG spine, three-regime PDEs, dictionary / 0.6 resolution). Output target: `docs/figures/ED-Math-Pipeline_v6.png`.
