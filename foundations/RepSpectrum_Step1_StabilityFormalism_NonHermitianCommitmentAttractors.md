# Rep-Spectrum · Step 1 — The Stability Formalism: a Rule-Type Is an Attractor Fixed Point of the Irreversible Commitment Map, and the Chirality Casting Lives in That Map's *Non-Hermitian* (Arrow) Spectrum — the One Place the Permissive Hermitian Stability (Gauge_09) Cannot See

**Foundations — scope step 1 (`RepSpectrum_Program_Scope_*`). Writes the stability-condition formalism the whole matter sector funnels into, after `T4_13` proved the casting has no geometric shortcut and is a *dynamical selection* problem. Built ON the corpus, not around it: it is the *third* ED stability notion, distinct from MS-II §6 (Welch-distinguishability → force families {1,…,d}, done) and from Gauge_09 (Hermitian coherence-Hessian → permissive, refuted for selection). Its one real move: because the commitment map is *irreversible* (P11), its linearization is *non-Hermitian*, and non-Hermitian spectra carry chirality (MS-II §4.2 point-gap winding) — so this stability notion can discriminate the L/R casting exactly where the Hermitian one is flat. Crank-rail ON: this DEFINES the formalism and LOCATES the mechanism; it does not compute the spectrum, and it names the live risk that this notion, too, could turn out permissive.**

## 1. What step 1 must deliver, and the two landmines
The rep-spectrum needs "which patterns of commitment are stable" made precise. Two existing corpus results are *not* this, and must not be reinvented:
- **MS-II §6 (Welch / distinguishability-stability):** `N` same-rule-type channels coexist stably iff mutually distinguishable in `ℂ^d` → stable **force families** are `{1,…,d}`, so `{1,2,3} ⟺ d=3`. This is a *static structural* bound on **gauge-family size** — done, and about forces, not matter patterns.
- **Gauge_09 (Hermitian coherence-Hessian):** extremize the parity-even landscape `F = −Coh + λ·Str`, check the Hessian → the symmetric `SU(N)` multiplet is stable **for all `N`** (coherence-binding even *grows* with `N`). Permissive; refuted as a *selector*.

The rep-spectrum stability is a **third, distinct notion**: dynamical stability of a **matter rule-type** (a tethered-spinor + lane pattern, T4_03/T4_13) — *which fermion patterns persist*, and *in which `γ⁵` eigenspace*. This is the frontier MS-II §8 names, and it is what AP's steer points at: **"not a stage — the happening,"** i.e. a particle is a *stable pattern of the process*, not a static shape.

## 2. The definition — a rule-type is an attractor of the commitment *map*
The process is P11: a chain **commits**, multiplicity drops (`multiplicity.md`), a channel is selected. This is a **discrete update map** `T` on pattern-space, and — decisively — it is **non-invertible** (commitment is irreversible; the facts-paper's "non-invertibility = the irreducible core"). So the ED-native object is not a gradient flow and not a static Hessian, but an **iterated non-invertible map**:

> **A stable rule-type = an attracting fixed point `x*` of the commitment map `T`:** `T(x*) = x*` (the pattern reproduces itself each commitment), and nearby patterns converge to it under iteration. **The particle spectrum = the attractor set of `T`.**

This is exactly "a stable pattern of the happening": `x*` is a shape the *process* keeps re-making, not a shape sitting still.

## 3. The criterion — a spectral gap of the (non-Hermitian) linearization
Linearize at the fixed point: `DT|_{x*}`. Discrete-time asymptotic stability is standard:

> **`x*` is stable ⟺ spectral radius `ρ(DT) < 1`** — every perturbation eigen-mode decays. The **spectral gap** `1 − ρ(DT) > 0` is the ED stability margin; a mode at `|λ|=1` is marginal (a would-be massless/flat direction), `|λ|>1` unstable (the pattern is not a particle).

Because `T` is **non-invertible** (P11), `DT` is **non-normal / non-Hermitian** — the arrow makes transport retarded, hence non-Hermitian (MS-II §3). This is not a nuisance; it is the whole mechanism (§4). *(Contrast: Gauge_09's `F`-Hessian is symmetric/Hermitian by construction — it threw away the arrow, which is why it could only ever be parity-even and permissive.)*

## 4. The key move — the casting lives in the non-Hermitian spectrum, which Hermitian stability cannot see
Parity acts on a matter pattern as `(spinor swap) ⊗ (lane reflection S)` (T4_13). The question "vector vs chiral" is whether the stable attractor treats the two `γ⁵` eigenspaces the same (vector) or differently (chiral). Now the two stability notions diverge sharply:

- **A Hermitian / parity-even `DT`** (Gauge_09's world) has its L and R sectors **degenerate** — `[DT, γ⁵]`-symmetric — so it is *flat* in the casting direction. It **cannot** select a chirality. This is *why* Gauge_09 was permissive, and `T4_13` found the geometry permissive: both are parity-even, and parity-even objects are blind to the casting. (Consistent, not a coincidence.)
- **A non-Hermitian `DT`** (the actual commitment map, carrying the arrow) has a **point-gap spectrum**: `det(DT − z)` can *wind* as `z` circles a point in the complex plane, and nonzero winding is a **net-chirality invariant** (MS-II §4.2; the retarded-vs-Hermitian toy `evaluation/ChiralGauge/chiral_winding.py` already exhibits exactly this — nonzero winding, skin effect, spectral flow, all zero in the Hermitian control). Nonzero point-gap winding ⟹ the L and R attractors are **inequivalent** ⟹ **chiral casting**; zero winding ⟹ **vector**.

> **So the casting criterion is concrete and computable:** for a candidate matter pattern of channel-count `N`, form its commitment-map linearization `DT` and compute the **point-gap winding** of `DT`. **Nonzero ⟹ chiral** (one `γ⁵` eigenspace is the attractor); **zero ⟹ vector** (both). The `T4_12` question "is N=2 chiral, N=3 vector?" becomes "does the N-channel commitment map's `DT` carry point-gap winding?" — a definite non-Hermitian spectral computation, the relativistic-scale successor to the 1+1D toy.

This is the payoff of `T4_13`: it proved the casting is *dynamical selection*; step 1 now says the selection is the **point-gap winding of the irreversible commitment map**, the one arrow-carrying object the permissive parity-even notions structurally cannot access.

## 5. Where discreteness comes from — not from stability (avoiding the Gauge_09 error)
Gauge_09's deeper lesson: *do not ask stability to supply discreteness.* It doesn't. The **discrete candidate set** comes from **topology/quantization**, already in hand:
- spin from `π₁(SO(3))=ℤ₂` (T4_03, MS-II §4.1),
- charge/winding `∈ ℤ` (B4),
- family size `{1,…,d}` from Welch distinguishability (MS-II §6),
- the `γ⁵` split from `arrow × orientation` (T4_10).

**Stability is the *filter*, not the *source*.** The spectrum = (topologically quantized candidates) ∩ (attractors of `T`), with the point-gap winding of `DT` deciding each survivor's chirality. This division is the corpus-consistent one: it keeps the enumeration where it belongs (topology) and puts the arrow-flow where the *selection* (which candidates persist, in which chirality) belongs.

## 6. Honest tier, the live risk, and the concrete next computation
- **Tier: formalism DEFINED + mechanism LOCATED, spectrum NOT computed.** What is delivered: (a) the ED-native definition (rule-type = attractor of the irreversible commitment map), (b) the criterion (spectral gap `ρ(DT)<1`), (c) the correct placement of discreteness (topology) vs selection (stability), and (d) the identification that the **casting = point-gap winding of the non-Hermitian `DT`**, the precise reason the permissive Hermitian notions (Gauge_09, T4_13) could not see it. All tied to standing corpus results (MS-II §3/§4.2/§6, Gauge_09, B4, T4_03/10/13), reinventing none.
- **The live risk, held to the positive bar:** the non-Hermitian `DT` might *also* come out permissive — nonzero winding for *both* N=2 and N=3, or a `DT` whose winding is not fixed by channel-count. If so, ED **underdetermines** the matter chirality (the honest parallel to Gauge_09's gauge-multiplicity verdict), and that would be a real result, not a failure to hide. This formalism's value is that it is the **first correctly-posed test** of whether ED fixes the casting at all — with a definite yes/no computation rather than a metaphor.
- **Concrete next brick:** lift `chiral_winding.py` from the 1+1D toy to the **N-channel commitment map** — build `DT` for a candidate tethered-spinor + `N`-lane pattern and compute its point-gap winding as a function of `N`. That single computation either delivers the casting (winding≠0 at N=2, =0 at N=3) or shows the arrow-map is permissive too. Either way it converts the last open matter-sector question from prose to a number.
