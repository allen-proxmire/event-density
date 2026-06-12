# Khronon–MOND — Round 2: The Static Weak-Field Reduction and the Lensing Verdict

**Foundations derivation round. Not a rule proposal, not a corpus edit, not a new primitive. Form-level reduction: structures and limits are derived; exact numerical coefficients are convention/normalization-dependent and flagged as such.**
**Crank rails (held):** no reverse-engineering of the kinetic function; no attempt to derive the MOND exponent from primitives; all failures and costs flagged; GR-I must come out untouched. One deviation from the Round-2 prompt is made and justified in §1: the kinetic invariant is corrected from `(∂T)²` to the khronon **acceleration** — the prompt's k-essence form fails structurally, and the correction is what the established khronometric-MOND class actually uses.

---

## 1. A correction before the derivation: the invariant is the acceleration, not `(∂T)²`

The prompt proposes `W(X)` with `X = g^{μν}∂_μT∂_νT`. Two independent reasons this cannot be the MOND carrier:

1. **Wrong argument.** In the static weak field (§2), `X ≈ 1 − 2Φ − |∇τ|²`: it depends on the *potential* `Φ`, not its *gradient*. A function of `X` therefore builds a screening/mass-type modification, never `μ(|∇Φ|/a₀)`.
2. **The lensing graveyard.** A `(∂T)²`-scalar can only source MOND if matter couples to it directly (conformally) — and that is precisely the RAQUAL/AQUAL relativistic-MOND construction that **fails lensing**, because conformal factors are invisible to null geodesics (the same conformal-blindness fact GR-I §6 used to exclude Nordström). TeVeS's added vector field was the historical patch for exactly this failure.

The correct invariant — the one the khronometric-MOND class (Blanchet–Marsat 2011) is actually built on — is the **acceleration of the khronon congruence**:

> `u_μ = ∂_μT / √X`, `a_μ = u^ν∇_νu_μ = ⊥_μ^ν ∇_ν \ln√X` (the projected gradient of the normalization),

with the MOND sector carried by a function of `A² = a_μa^μ/a₀²`. Importantly, this stays inside the khronometric EFT: the general foliation-sector action is built from the congruence's expansion `θ`, shear `σ`, and acceleration `a` — the quadratic theory is `λθ² + βσ_{μν}σ^{μν} + α\,a_μa^μ` — and the MOND extension promotes **only the acceleration term** to a function:

$$
S_T = \frac{1}{16\pi G}\int d^4x\,\sqrt{-g}\;\Big[\,R \;+\; \lambda\,\theta^2 + \beta\,\sigma_{μν}σ^{μν} \;+\; a_0^2\,W\!\big(A^2\big)\Big],
\qquad A^2 = \frac{a_μa^μ}{a_0^2}.
$$

`W` is carried as a **general function** throughout (the rails); matter couples to `g_{μν}` **only** (universal coupling — in ED matter *is* substrate content; there is no conformal matter frame to mis-couple). This correction is not cosmetic: §5's lensing verdict turns on it.

---

## 2. The static weak-field reduction

**Metric and khronon.** `g_{00} = -(1+2Φ)`, `g_{ij} = (1-2Ψ)δ_{ij}` (signature `(−,+,+,+)`, `c=1`); khronon `T = t + τ(\mathbf{x})`.

**The khronon aligns.** For a static, time-reversal-symmetric source, the aligned configuration `T = t` (`τ = 0`) is the symmetric solution of the `T`-equation: the misalignment `τ` enters `u_i ∝ ∂_iτ`, which is odd under the staticity symmetry, so the symmetric solution has `τ = 0`. (Time-dependent and rotating systems excite `τ`; deferred, §7.) With `T = t`, the khronon congruence is the **static-observer congruence**, for which the kinematics are textbook:

> `θ = 0`, `σ_{μν} = 0`, `a_i = ∂_i \ln N = ∂_iΦ + O(Φ²)`,

where `N = √(1+2Φ)` is the lapse. **Two structural consequences fall out immediately:**

1. **The static sector isolates the MOND carrier.** With `θ = σ = 0`, the `λ` and `β` terms are *inert* in statics — the **only** active foliation term is the acceleration function `W(A²)`. The `λ`-sector governs cosmology and the `β`-sector the tensor waves (`c_T` — GR-II's structural pass, untouched by `W`). The MOND modification and the static modification are *the same term*. No tuning makes this so; it is the kinematics of static congruences.
2. **The ED reading (an identity, not a new derivation).** GR-I derived the lapse from the substrate: `N² ∼ b`. Therefore
   `a_i = ∂_i \ln N = \tfrac{1}{2}\,∂_i \ln b` —
   **the khronon's acceleration is the logarithmic bandwidth gradient.** The MOND function is a function of `|∇\ln b|` measured against `a₀`: the deep-IR regime is, in substrate terms, *the regime where bandwidth gradients fall below the cosmic rate*. This ties the invariant directly to the GR-I metric sector with no new structure.

**The field equations.** With `T = t` imposed by symmetry, the `T`-equation is identically satisfied in statics; the modification enters through the metric variation of `W`. Since `A² = |∇Φ|²/a_0^2 + O(Φ³)`, varying the action with respect to `Φ` gives, at leading order (schematic constants `c₁, c₂` of order unity, convention-dependent and flagged):

$$
\nabla\cdot\Big[\big(1 + c_1\,W'(A^2)\big)\,\nabla\Phi\Big] \;=\; 4\pi G\,\rho ,
$$

— **the modified Poisson equation**, with effective interpolation

$$
\mu_{\rm tot}(x) \;=\; 1 + c_1\,W'(x^2), \qquad x = \frac{|\nabla\Phi|}{a_0}.
$$

The `Ψ`-equation receives the khronon's stress; its *anisotropic* part is `∼ W'\,a_{\langle i}a_{j\rangle}`, which is **second order in the potentials** (§5). At leading order the system closes on `Φ` alone, in exactly the AQUAL/Bekenstein–Milgrom form — but crucially **in the metric potential itself**, not in an auxiliary scalar.

---

## 3. GR-limit verification — with a second correction to the prompt

The prompt's "GR recovery ⟺ `W(X) = X` (canonical)" is replaced by the correct statement:

> **GR recovery at high accelerations ⟺ `W'(A² ≫ 1) → α`, a small constant** — the standard *quadratic* khronometric acceleration coupling, PPN-bounded (`α₁, α₂` constraints ⟹ `α` small).

Then `μ_tot → 1 + c_1α ≈ 1`, the Poisson equation reduces to `∇²Φ = 4πGρ`, `Φ = Ψ` at leading order, and **GR-I's weak-field Schwarzschild sector is untouched** — including the factor-of-two bending and redshift. The residual `O(α)` preferred-frame effects are *exactly* GR-II §8's standing `α₁, α₂` falsification front: nothing new is introduced and nothing is hidden. ✓ (Rail held: GR-I untouched.)

---

## 4. The deep-IR embedding — and an honest cost surfaced

Insert the forced-given-030 requirement: the deep-IR law must be the Combination Rule, i.e. `μ_tot(x) → x` as `x → 0`. From `μ_tot = 1 + c_1W'`:

$$
W'(A^2) \;\xrightarrow{\,A\to 0\,}\; -\frac{1}{c_1}\;+\;\frac{A}{c_1} + \ldots
$$

Two pieces, and they have different statuses:

- **The non-analytic linear piece** (`∝ A`, i.e. `W ⊃ A³`-type, the `X^{3/2}` of Round 1): this is the MOND carrier, uniquely fixed by matching Paper_030. Forced-given-030, as before.
- **The constant `−1/c₁`** — **the IR cancellation, and this round's honestly-surfaced cost.** In the convention where the Einstein–Hilbert term keeps its standard normalization, the khronon function must approach a *constant negative slope* in the deep IR that **exactly cancels the Einstein gradient term** in the static constraint, leaving the non-analytic piece as the leading survivor. Physically: *below `a₀`, the khronon sector takes over the static constraint from the Einstein term.* This cancellation is a **known structural feature of the class** (the negative-branch kinetic function of generalized-aether MOND, Zlosnik–Ferreira–Starkman), so it is standard-in-class — but it is the single most delicate requirement of the unification, and Round 1's summary ("`W = (2/3)X^{3/2}`") was **incomplete without it**. Status: still forced-given-030 (the *total* `μ_tot → x` is one matching condition; both pieces follow from it), but the cancellation is flagged as the structure Round 3 must stress-test (its perturbative stability is precisely where ghost/gradient pathologies arise in this class).

With it in place, spherical symmetry gives Gauss-law integration `μ_tot(x)\,|\nabla\Phi| = a_N ≡ GM/r²`, and the deep-IR limit `μ_tot = x` yields

$$
\frac{|\nabla\Phi|^2}{a_0} = a_N \;\Longrightarrow\; |\nabla\Phi| = \sqrt{a_N\,a_0},
$$

**the Combination Rule (Paper_030), embedded relativistically** — and with it BTFR slope-4 (`v⁴ = GMa₀`, Paper_031) — with `a₀ = cH₀/2π` carried by the khronon's cosmological background (Round 1 §3.2). The interpolation between the two fixed asymptotics remains an honest family (unchanged status). ✓

---

## 5. The lensing verdict (the kill-or-confirm check)

**Setup.** Photons follow null geodesics of `g_{μν}`; weak-field deflection `∝ ∫ ∇_⊥(Φ + Ψ)`. The check: does light see the *same* MONDified potential that stars do — i.e. is the slip `Φ − Ψ` negligible, with both potentials MONDified?

**The structural answer — and why this construction is on the right side of history.** The MOND modification here lives **in the gravitational constraint itself**: §2's equation MONDifies the *metric potential* `Φ`. Matter (and light) couple universally to `g_{μν}`; there is no conformal scalar sector for photons to be blind to. The historical lensing failure of relativistic MOND (RAQUAL) was precisely that its scalar coupled *conformally* to matter — and conformal factors do not deflect light (GR-I §6's own Nordström argument). TeVeS's vector field was a patch for that failure. **The khronon never has the disease the patch was for**: it is part of the gravity sector, not a conformally-coupled matter scalar.

**The slip computation (leading order).** The khronon's contribution to `Φ − Ψ` comes from its anisotropic stress, `σ_{ij} ∼ (8πG)^{-1} W' a_{\langle i}a_{j\rangle}`. With `a_i = ∂_iΦ` this is `O(|∇Φ|²)` — **second order in the potentials**. Even in the deep-MOND regime (`W' ∼ A`), its ratio to the leading constraint terms is `O(Φ) ∼ v²/c² ∼ 10^{-6}` for galaxies. Hence:

> `Φ = Ψ\,[1 + O(Φ)]` — **no gravitational slip at leading order** — and both potentials are the *MONDified* potential of §2. The deflection angle is `α_{\rm def} ∝ ∫∇_⊥(Φ+Ψ) = 2∫∇_⊥Φ_{\rm MOND}`: **galactic lensing tracks the MOND potential, with no added vector field.**

**Verdict: the kill-check PASSES at leading order in the static weak field.** This is consistent with the published khronometric-MOND analyses (Blanchet–Marsat advertise correct light bending) and — the ED-flavored point — it passes *for the same structural reason ED's gravity got the factor of two in GR-I*: the modification is metric-borne, so space and time potentials move together.

**Caveats (named, not hidden).** (i) Leading-order, static, quasi-spherical; the interpolation-regime and time-dependent lensing details are open. (ii) **Cluster-scale lensing remains the standing MOND-class shortfall**: lensing *tracks* the MOND potential, but the MOND potential itself under-predicts clusters — that problem is inherited intact and lands on the SCBU/cosmology sector (Round 1 §6.5). (iii) The slip suppression assumed the `W'`-sector's perturbations are healthy; that is Round 3's stability question, not established here.

---

## 6. Round-2 Summary — forced / inherited / open

| Item | Status |
|---|---|
| Invariant = khronon acceleration `a_μ = ⊥∇_μ\ln√X` (not `(∂T)²`) | **corrected** — required by structure; the `(∂T)²` route is either inert or lensing-dead |
| Static sector isolates the `W(A²)` term (`θ = σ = 0`) | **derived** (kinematics of static congruences) |
| `a_i = \tfrac12∂_i\ln b` — acceleration = bandwidth gradient | **identity** via GR-I's `N² ∼ b` (ED reading; no new structure) |
| Modified Poisson `∇·[μ_{\rm tot}∇Φ] = 4πGρ`, `μ_{\rm tot} = 1 + c_1W'` | **derived** (form-level; constants convention-dependent) |
| GR limit: `W' → α` small ⟹ `μ→1`, GR-I untouched | **verified**; residual = the standing `α₁, α₂` front (GR-II §8) |
| Deep IR: `μ_{\rm tot} → x` ⟹ Combination Rule + BTFR embedded | **forced-given-030** (inherited law; relativistic embedding) |
| **The IR cancellation** (`W' → -1/c_1 + x/c_1`): khronon takes over the static constraint below `a₀` | **surfaced cost** — standard-in-class (ZFS negative branch) but the delicate piece; Round-3 stress test |
| Interpolation between asymptotics | **family** (unchanged honest status) |
| `a₀ = cH₀/2π` | **inherited** (Paper_029) via the khronon background (Round 1) |
| **Lensing: tracks the MOND potential, no vector needed** | **PASSES at leading order** — metric-borne modification; slip `O(Φ)`-suppressed |
| `c_T = c` (GW170817) | **untouched** — `W` modifies the acceleration sector; tensor speed governed by `β` |
| Clusters / CMB | **inherited shortfall, flagged** — not addressed |

## 7. Round-3 agenda

1. **Stability of the deep-IR branch (now the sharpest open item).** Perturbations around deep-MOND backgrounds where the khronon sector dominates the constraint (the `−1/c₁` cancellation): ghost-freedom, gradient stability, Čerenkov — mapped onto Paper_033/035's (C1)–(C3), now as conditions on `W` near `A → 0`. This is where theories of this class typically get hurt; it is the natural next kill-check.
2. **The interpolation family vs solar-system screening:** how fast `W' → α` must saturate; whether any family member is excluded by planetary ephemerides.
3. **The misalignment mode `τ`** in time-dependent/rotating systems (excited beyond statics) — and whether it feeds the PPN preferred-frame sector.
4. **Cosmology tie-in:** the `λθ²` sector on FRW backgrounds (the khronon's cosmological face) → connection to SCBU and the standing cluster/CMB debt.
5. **Deferred on purpose:** the primitives-level origin of the deep-IR exponent and of the IR cancellation (the substrate question "*why* does the khronon take over below the cosmic rate?") — the reverse-engineering guard stays up.

---

*Round-2 static weak-field reduction. The kinetic invariant is corrected to the khronon acceleration (the `(∂T)²` form is structurally inert or lensing-dead); statics isolate the acceleration sector (`θ=σ=0`), whose ED reading is `a_i = \tfrac12∂_i\ln b`; the modified Poisson equation emerges in the metric potential with `μ_{\rm tot} = 1 + c_1W'`; the GR limit is `W'→α` small (GR-I untouched; `α₁,α₂` front unchanged); the deep IR embeds the Combination Rule and BTFR (forced-given-030) at the cost of a surfaced **IR cancellation** — the khronon taking over the static constraint below `a₀`, standard-in-class but delicate, now Round 3's stress test. **The lensing kill-check passes at leading order**: the modification is metric-borne, slip is `O(Φ)`-suppressed, and galactic lensing tracks the MOND potential with no added vector. Clusters/CMB remain inherited shortfalls, flagged. Form-level throughout; exact coefficients convention-dependent; no new primitives; no MOND exponent derived from primitives.*
