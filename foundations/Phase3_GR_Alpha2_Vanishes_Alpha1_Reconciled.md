# Phase-3 GR — α₂ Vanishes Identically, and the Two α₁ Strands Reconcile: the Preferred-Frame Front Collapses to One Looser-Bounded Number

**Foundations computation — does the keystone residual flagged in the 2026-06-23 frontier review: (1) actually COMPUTE `α₂` on ED's luminal family (it was previously asserted-by-extension as `O(c₁₄)`), and (2) reconcile the corpus's two conflicting α₁ strands ("c₁₄ genuinely undetermined" vs "safe by ≥70 orders via sparsity"). Not a corpus edit, not a new primitive. Result: `α₂ = 0` identically on ED's family (the same `c_s=c` condition that fixes the kinetic coupling exactly nulls the α₂ numerator), and the two strands were never in conflict — the `c_s=c` family relation ties Route-A's `c₁₄` to LambdaOfRho's derived `c₂ = sparsity`, so `c₁₄ ≈ sparsity`: nonzero (khronon propagates) but tiny (≈10⁻⁹³). The front collapses from two numbers to one (`α₁ = −4c₁₄`), against the LOOSER bound, and the conservative sector is safe without needing the dissipative escape.**

**Crank rail — maximal.** This is a favorable result on a front the corpus has flagged for over-reading three times. I compute `α₂` from the CITED Blas–Sibiryakov formula (not invented), flag the clean cancellation as likely-structural-but-worth-cross-checking, mark the band-fraction prefactor and `ρ_event^vac` magnitude as still inherited/unpinned, and state plainly what is computed vs reconciled vs still owed. No number is fabricated; the surviving open piece is named.

---

## 1. The setup (ED's luminal family — established, cited)

Khronometric couplings (Blas–Sibiryakov arXiv:1412.4828; transcribed in `Phase3_GR_PPN_RouteA_Mapping.md`): `λ ≡ c₂`, `β ≡ c₁+c₃`, `α ≡ c₁+c₄` (≡ `c₁₄`). The verified PPN formulas:

- `α₁ = 4(α − 2β)/(β − 1)`
- `α₂ = (α − 2β)·[ −β(3+β+3λ) − λ + α(1+β+2λ) ] / [ (α−2)(β−1)(β+λ) ]`
- Bounds: `|α₁| ≲ 10⁻⁴` (lunar laser ranging), `|α₂| ≲ 10⁻⁷` (solar-spin), `~10⁻⁹` (pulsars).

ED's two derived luminal conditions cut this to a one-parameter family:
- `c_T = c ⟹ β = 0` (single P05 cone, GR-II).
- `c_s = c ⟹ λ = α/(1−2α)` (the `ε=0` khronon, `DerivingEpsilon`; Route-A §3 step 2).

So ED lives on `{ β = 0, λ = α/(1−2α) }`, coordinatized by `α = c₁₄`.

## 2. Result 1 — `α₂ = 0` identically on ED's family (computed; corrects Route-A)

Route-A asserted "`α₂`, carrying the same `(α−2β)` factor, is likewise `O(α)`, vanishing iff `α=0`." **That is wrong** — the *other* factor (the numerator bracket) also vanishes on ED's family. Set `β = 0`:

- `(α − 2β) = α`
- bracket `N = −β(3+β+3λ) − λ + α(1+β+2λ) →[β=0]→ −λ + α + 2αλ`
- denominator `D = (α−2)(β−1)(β+λ) →[β=0]→ (α−2)(−1)(λ) = (2−α)λ`

Now substitute the `c_s=c` relation `λ = α/(1−2α)` into the bracket:

> `N = −λ + α + 2αλ = [ −α + α(1−2α) + 2α² ] / (1−2α) = [ −α + α − 2α² + 2α² ] / (1−2α) = 0.`

So `N = 0` for **every** `α` on the family. Therefore

> **`α₂ = α · N / [(2−α)λ] = 0`  identically on ED's luminal family** (for `α ≠ 0`; `α = 0` is the GR point where all preferred-frame parameters vanish anyway).

**The mechanism is not a coincidence:** the `c_s=c` condition is `λ(1−2α) = α`, and that is *exactly* the relation that makes `N = α − λ(1−2α) = 0`. Putting the khronon at light speed is what kills `α₂`.

**Independently verified (2026-06-23).** The α₁/α₂/c_T²/c_s² formulas were cross-checked against the *published* literature, not just the Route-A transcription: the Hořava-gravity PPN derivation **arXiv:1105.5149 eq. (31)** gives `α₁ = 4(α−2β)/(β−1)` and `α₂ = (α−2β)[−β(3+β+3λ)−λ+α(1+β+2λ)]/[(α−2)(β−1)(β+λ)]`, with `c_T²=1/(1−β)`, `c_s²=(α−2)(β+λ)/[α(β−1)(2+β+3λ)]` — **identical** to the formulas used here; **Blas–Sibiryakov arXiv:1412.4828 eq. (27)** confirms the same in the aether parametrization. The α₂=0 cancellation also checks numerically (e.g. `c₁₄=0.1 ⟹ λ=0.125`, `c_s²=1`, bracket `=−0.125+0.125=0`, `α₂=0`, `α₁=−0.4=−4c₁₄`). So **α₂=0 on the luminal family is not a transcription artifact** — it is a real, and apparently *general*, feature: **any khronometric/Hořava-IR theory with both cones at `c` has α₂=0 and α₁=−4c₁₄≠0.** (A loose web claim that "c_T=c alone gives α₁=α₂=0" is wrong: c_T=c gives only β=0, leaving α₁=−4α; it takes c_s=c too, and even then only α₂ vanishes.)

**Consequence:** the *tighter* preferred-frame bound (`|α₂| ≲ 10⁻⁷` to `10⁻⁹`) — which the structural notes correctly flagged as the binding constraint — **is satisfied exactly, for free.** The falsification front loses its tighter half. Only `α₁ = −4c₁₄` survives, against the *looser* LLR bound `|α₁| ≲ 10⁻⁴` (i.e. `|c₁₄| ≲ 2.5×10⁻⁵`).

## 3. Result 2 — the two α₁ strands reconcile (no contradiction)

The corpus carried two readings of `α₁ = −4c₁₄` that looked opposed:

- **"undetermined coupling"** (`ComputingC14`, `ProtectionHunt`): `c₁₄` is a bare PPN coupling with no symmetry protection; naturalness → `O(1)` (tension); `c₁₄ = 0` exact is **refuted** (a propagating khronon at `c_s=c` forces `c₁₄ ≠ 0`); value undetermined.
- **"safe via sparsity"** (`LambdaOfRho`, `Alpha1_Magnitude`, `SparseCommitment_Constitutive`): `α₁ = −4λ`, `λ = c₂ = ρ_event/ρ_Planck` derived as the commitment sparsity → `≈ 10⁻⁹³`, safe by ≥70 orders on the forced-sparse branch.

**They are the same statement, tied by the `c_s=c` family relation.** Route-A's `c₁₄ = α` and LambdaOfRho's `λ = c₂` are *different* khronometric couplings (acceleration `c₁+c₄` vs kinetic/twist `c₂`), but on ED's family they are locked together:

> `λ = α/(1−2α)`  ⟺  `α = λ/(1+2λ)`,  i.e.  **`c₁₄ = c₂/(1+2c₂) ≈ c₂`  for small couplings.**

LambdaOfRho **derives** `c₂ = (k₁₁/s₀₂)·ρ_event/ρ_Planck` (the sparsity, because metric stiffness is always-on P02 sharing while khronon stiffness is sparse P11 pinning). Feeding that through the family relation:

> **`c₁₄ ≈ c₂ = sparsity`** — so `c₁₄` is **nonzero** (commitment is sparse but not zero ⟹ the khronon propagates ⟹ ProtectionHunt's "exact zero refuted" holds) **and tiny** (`≈ ρ_event/ρ_Planck ≈ 10⁻⁹³` in the Solar System).

So `α₁ = −4c₁₄ ≈ −4·sparsity ≈ 10⁻⁹³`. The "undetermined" reading treated `c₁₄` as free because it predated the `c₂`-derivation; once `c₂` is derived, the `c_s=c` condition *pins* `c₁₄` to the sparsity. **No contradiction: c₁₄ ≠ 0 and c₁₄ tiny are simultaneously true, and both are required** (nonzero for a propagating khronon, tiny because commitment is sparse).

## 4. Result 3 — the conservative sector is safe (Route-A's pessimism dissolved)

Route-A's honest, non-flattering correction was: the luminal cones are *necessary not sufficient*; "a conservative reading of ED's propagating khronon sits at `c₁₄ ≠ 0 ⟹ α₁ ≠ 0`; ED's only escape is the non-conservative dissipative near-field." That pessimism assumed `c₁₄` could be `O(1)`. But `c₂` (the conservative kinetic/twist coupling — LambdaOfRho's `f²/M_P²`) is **derived** to be the sparsity, and the family relation makes `c₁₄ ≈ c₂` tiny. So:

> **The *conservative* `c₁₄` is itself the sparsity (`≈10⁻⁹³`), already far below `2.5×10⁻⁵`.** ED is preferred-frame-safe in the conservative sector — it does **not** need the dissipative near-field to escape. The dissipative damping (the overdamped near-field, `PreferredFrame_Alpha12 §3`) is *additional* margin on top, not the load-bearing mechanism.

This is the cleaner picture: ED is safe because its preferred-frame coupling is the sparsity (a derived, density-screened, forced-tiny number), with the dissipative near-field as belt-and-suspenders.

## 5. The front now — one number, looser bound, ≥70-order clearance

| parameter | ED value (this note) | bound | status |
|---|---|---|---|
| `α₂` | **0 identically** (§2) | `≲ 10⁻⁷`–`10⁻⁹` | satisfied exactly (tighter bound retired) |
| `α₁` | `−4c₁₄ ≈ −4·(ρ_event/ρ_Planck) ≈ 10⁻⁹³` (§3) | `≲ 10⁻⁴` | clears by ≥70 orders on the forced-sparse branch |

The preferred-frame falsification front, previously "two numbers, the tighter one binding and uncomputed," is now: **`α₂ = 0` (computed), `α₁` = the sparsity (derived, forced-sparse, ≥70-order margin) against the looser bound.** ED is khronometric, has a genuine propagating luminal khronon (`c₁₄ ≠ 0`), and is preferred-frame-safe by a derived margin.

## 6. What is still owed (crank rail)

This narrows and reconciles; it does not fabricate a final certified number. Genuinely remaining:

1. ~~`α₂ = 0` rests on the cited α₂ formula.~~ **RESOLVED 2026-06-23** — the formula is verified against published sources (arXiv:1105.5149 eq. 31; 1412.4828 eq. 27) and the cancellation checks numerically; α₂=0 is a real, general feature of luminal khronometric gravity (§2). A native Route-B `α₂` from `F` would still be a nice from-primitives cross-check, but α₂=0 is no longer transcription-dependent.
2. **The `c₁₄ ≈ c₂` identification rests on the literature family relation `λ=α/(1−2α)`,** not yet on a from-`F` derivation. Route B (direct PPN expansion of the dynamical rule) should reproduce `c₁₄ = c₂/(1+2c₂)` natively, confirming the conservative kinetic and acceleration couplings are both the sparsity.
3. **The magnitude of `ρ_event^vac`** (hence the exact `α₁`) is robustly sub-Planck (≥70-order margin holds even at a nuclear-density stress-test) but **not pinned to a single value**; and the `O(1)` band-fraction `k₁₁/s₀₂` is inherited, not derived. Neither can flip the verdict; both keep `α₁` from being a from-first-principles *exact* number.
4. **The actual numerical comparison to LLR/pulsar data** is trivial given the margin (`10⁻⁹³ ≪ 10⁻⁴`; `α₂=0`), but a literal test-suite pass (with the real ephemeris/pulsar-timing constraints) has not been "run."

## 7. Verdict

**On ED's luminal family (`β=0`, `λ=c₁₄/(1−2c₁₄)`), `α₂ = 0` identically** — computed from the cited khronometric formula; the `c_s=c` condition that fixes `λ` is exactly what nulls the `α₂` numerator, so the *tighter* preferred-frame bound is satisfied for free and the front loses half its content. **The two α₁ strands reconcile:** the `c_s=c` family relation ties Route-A's acceleration coupling `c₁₄` to LambdaOfRho's derived kinetic coupling `c₂ = sparsity`, giving `c₁₄ ≈ sparsity` — nonzero (the khronon propagates; exact-zero stays refuted) yet tiny (`≈10⁻⁹³`), so `α₁ = −4c₁₄` is safe by ≥70 orders on the forced-sparse branch. **The conservative sector is safe on its own** — Route-A's "only escape is the dissipative near-field" pessimism dissolves once `c₁₄` is pinned to the (tiny) sparsity; the dissipative damping is additional margin. The preferred-frame front collapses to a single number against the *looser* bound, with a ≥70-order derived clearance. **Still owed:** an independent re-derivation of the α₂ formula (or native Route-B `α₂`), a from-`F` confirmation of `c₁₄ = c₂/(1+2c₂)`, the (robust-but-unpinned) `ρ_event^vac` magnitude, and a literal LLR/pulsar comparison. No corpus edits, no new primitives; Einstein not derived; α₂=0 computed-not-asserted, α₁ reconciled-not-fabricated, the residual named.

---

## 8. Push 2 (2026-06-23): the Route-B/directed-flux state, and two findings

After verifying α₂=0, I read the native Route-B docs (`Phase3_GR_PPN_RouteB_DirectExpansion.md`, `Phase3_GR_DirectedFluxSector.md`) to attempt the from-`F` confirmation of `c₁₄ = c₂`. State found: the vector sector `D∇²A^i = κ_J ρ w^i` is **built and run** (`directed_flux.py`); it produces the long-range `g_{0i} = λ_J w_i U` at machine precision; the cross-check `λ_J = c₁₄ = −η` holds; the dissipative reserve gives a measured Yukawa screening `𝒮(Γ)` reaching `<10⁻⁴`. The open α₁ is written there as `α₁ = −4 λ_J 𝒮(Γ)`, two band-fractions (`λ_J`, `Γ`). Two genuine findings:

**Finding 1 — a latent `c₂` ↔ `λ_J` magnitude tension, and the from-`F` closure made concrete.** The corpus has *two* ED-internal derivations of the α₁ coupling that disagree on mechanism while agreeing on safety: `LambdaOfRho` gives `c₂` (a stiffness ratio) `= sparsity ≈ 10⁻⁹³` (**intrinsically tiny**); `DirectedFlux` gives `λ_J = c₁₄` (a source-coupling ratio) framed as possibly **O(1), saved by `𝒮(Γ)`**. These are different khronometric couplings (`c₂` vs `c₁₄`) tied by the `c_s=c` family relation `c₂ = c₁₄/(1−2c₁₄)`. So if `c₂=sparsity`, the relation **forces** `λ_J=c₁₄≈sparsity` — the coupling is intrinsically tiny and `𝒮(Γ)` is *redundant extra margin*, not load-bearing. **The from-`F` closure is now a concrete band-partition check:** pin `λ_J` and `c₂` from the P04 band fractions and verify `c₂ = c₁₄/(1−2c₁₄)`, both `→ sparsity`. That decides "tiny coupling (sparsity)" vs "O(1) screened by `Γ`" — same verdict, different physics — and is the genuine remaining computation. (My §3–§4 reconciliation took the first reading; this names what would prove it from `F`.)

**Finding 2 — a likely α₂-matching inconsistency in Route-B §7 (caught by the verified formula).** Route-B §7 writes `α₂ = 2η 𝒮₂(Γ)`, whose *conservative* limit (`𝒮₂→1`) is `α₂ = 2η = −2c₁₄ ≠ 0`. But §2 here (literature-verified) gives `α₂ = 0` identically on the luminal family — and since ED conservatively *is* a luminal khronometric theory (the α₁ cross-check `η=−c₁₄` held in the *same* expansion), its conservative α₂ **must** be 0. So Route-B §7's α₂ prefactor matching (which that doc explicitly flagged as "to verify against source, not fabricated") is **inconsistent with the verified khronometric formula** — the conservative α₂ should vanish, not equal `−2c₁₄`. The §7 α₂ matching needs correcting with `α₂ → 0` conservatively as the constraint; the α₁ matching (`α₁ = −4c₁₄` conservatively) is fine.

**Net of Push 2:** the residual is sharpened, not closed. The keystone now rests on one band-partition computation (pin `λ_J`, `c₂`; check the `c_s=c` relation, expect both `→ sparsity`), plus fixing the Route-B §7 α₂ prefactor (the answer it must reproduce — `α₂=0` conservatively — is now known). Neither requires a new primitive; both are well-posed.

## 9. Push 3 (2026-06-23): Findings 1 & 2 RECTIFIED, anchored on the verified Will PPN form

The authoritative PPN `g_{0i}` (Will, *Living Reviews in Relativity* / TEGP; preferred-frame part):

> `g_{0i} = −½(4γ+3+α₁−α₂+ζ₁−2ξ)V_i − ½(1+α₂−ζ₁+2ξ)W_i − ½(α₁−2α₂)\,w_iU − α₂\,w^jU_{ij}`

Coefficient of `w_iU` is `−½(α₁−2α₂)`; coefficient of `w^jU_{ij}` is `−α₂`. Feeding ED's verified conservative values (`α₁=−4c₁₄`, `α₂=0`, §2):

> **ED's conservative preferred-frame metric is `g_{0i}^{PF} = 2c₁₄\,w_iU` — the `w_iU` term ONLY (coefficient `2c₁₄`), and ZERO `w^jU_{ij}`.** This is the target any correct ED expansion must hit.

**Finding 2 — RECTIFIED.** Route-B §5–§7 sourced `g_{0i}` from the *scalar* bandwidth current and got `g_{0i} ⊃ −2η(w_iU + w^jU_{ij})` (both terms), matching to `α₁=4η(𝒮₁+𝒮₂)`, `α₂=2η𝒮₂` → conservative `α₁=−8c₁₄`, `α₂=−2c₁₄`, **both wrong**. The fix is supplied by ED's own machine-precision result: `DirectedFlux` test [1] found the **scalar current is curl-free → pure gauge → sources no physical `g_{0i}`**. So the §5 scalar-current `g_{0i}` (including its `w^jU_{ij}` piece) is a *gauge artifact*; the physical cross-term is the **vector sector** `D∇²A^i=κ_J ρ w^i ⟹ g_{0i}=λ_J w_iU` — the `w_iU` structure **only**. Therefore the gauge-invariant result is `α₂=0` (no physical `w^jU_{ij}` — exactly the verified khronometric value) and `α₁=−4c₁₄\,𝒮(Γ)` (the `w_iU` vector term, screened). **Route-B §7's α₁/α₂ formulas are superseded by DirectedFlux + the verified formula; the §7 nonzero α₂ was the pure-gauge scalar-current artifact.** One residual bookkeeping item: DirectedFlux normalizes `g_{0i}=λ_J w_iU` with `λ_J=c₁₄`, while the Will form wants the `w_iU` coefficient `=2c₁₄` — a factor-of-2 in the `η`/`λ_J` metric-assembly normalization to nail; it does not touch `α₂=0` or the `α₁∝c₁₄` conclusion.

**Finding 1 — RECTIFIED.** The "is `λ_J` intrinsically tiny (sparsity) or O(1)-saved-by-screening?" tension is resolved by the *established* `c_s=c` relation: `λ_J=c₁₄` and LambdaOfRho's `c₂` are tied by `c₂=c₁₄/(1−2c₁₄)`, i.e. `c₁₄=c₂/(1+2c₂)`. With LambdaOfRho's derived `c₂=sparsity`, this **forces** `λ_J=c₁₄≈sparsity` — intrinsically tiny. DirectedFlux's framing that `λ_J` "could be O(1), saved by `𝒮(Γ)`" is **superseded**: once `c_s=c` (derived, `ε=0`) and `c₂=sparsity` (LambdaOfRho) hold, `λ_J` is not a free O(1) band-fraction — it is the sparsity, and `𝒮(Γ)` is **redundant extra margin, not load-bearing.** (Conditional on `c₂=sparsity`, a derived result resting on the four-band stiffness-origin argument; the band-partition computation would confirm it independently — but the corpus's *internal consistency* is now restored: both docs describe one intrinsically-tiny coupling.)

**Net of Push 3:** the two strands and the two routes now tell *one consistent story* — `α₂=0` (verified, and gauge-invariant: no physical `w^jU_{ij}`), `α₁=−4c₁₄\,𝒮(Γ)` with `c₁₄≈sparsity` intrinsically tiny (safe even at `𝒮=1`; screening is backup). The corpus inconsistencies (Route-B §7 vs the verified formula; LambdaOfRho vs DirectedFlux) are removed. What genuinely remains is the band-partition *confirmation* of `c₂=sparsity` and the `λ_J` factor-of-2 normalization — **a precision/consistency check, not a safety question.**

---

*α₂ vanishes identically on ED's luminal family (β=0, λ=α/(1−2α)): the β=0 α₂ numerator `−λ+α+2αλ` becomes `[−α+α(1−2α)+2α²]/(1−2α)=0` under the c_s=c relation — the same condition that fixes λ nulls α₂. So the tighter preferred-frame bound (|α₂|≲10⁻⁷–10⁻⁹) is satisfied for free; only α₁=−4c₁₄ survives, against the looser LLR bound |α₁|≲10⁻⁴. The two α₁ strands reconcile via the family relation c₁₄=c₂/(1+2c₂)≈c₂: LambdaOfRho derives c₂=sparsity=ρ_event/ρ_Planck, so c₁₄≈sparsity — NONZERO (propagating khronon; ProtectionHunt exact-zero refutation holds) and TINY (≈10⁻⁹³, ≥70-order safe on the forced-sparse branch). The conservative c₁₄ is itself the sparsity, so the conservative sector is safe WITHOUT the dissipative near-field (Route-A's pessimism dissolved; dissipation = extra margin). Front collapses two→one number, looser bound, ≥70-order clearance. Owed: independent α₂-formula re-derivation / native Route-B α₂; from-F confirmation of c₁₄=c₂/(1+2c₂); robust-but-unpinned ρ_event^vac magnitude + inherited O(1) band-fraction; literal LLR/pulsar comparison. Crank-rail maximal; no number fabricated.*
