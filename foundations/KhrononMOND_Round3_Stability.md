# Khronon–MOND — Round 3: Stability at the Cancellation, Screening, and the τ-Mode

**Foundations viability round — the first full kill-check of the unified theory. Not a rule proposal, not a corpus edit, not a new primitive. Form-level: structural results are derived; class-level results from the literature are labeled I; what is *not* settled here is said to be not settled.**
**Crank rails (held):** stability is a *test*, not a target — `W` is not adjusted to pass; no MOND exponent derived from primitives; GR-I untouched at high accelerations; clusters/CMB remain inherited shortfalls. One deviation from the prompt: the "full quadratic stability analysis" around anisotropic deep-MOND backgrounds is **not** fully closed here — what closes structurally is closed, what the class literature reports is cited as such, and the genuinely open piece is named rather than faked.

---

## 1. Inputs (fixed, from Round 2)

Invariant `A² = a_μa^μ/a₀²` with `a_μ = ⊥∇_μ\ln√X`; statics align the khronon (`a_i = ∂_iΦ = ½∂_i\ln b`); modified Poisson `∇·[μ_{\rm tot}∇Φ] = 4πGρ` with `μ_{\rm tot} = 1 + c_1W'`; deep IR forced-given-030: `W' → -1/c_1 + x/c_1` (the Einstein-term cancellation); lensing slip `O(Φ)`-suppressed.

---

## 2. (A) Stability at the IR cancellation point

### 2.1 The structural no-ghost result (clean)

In unitary gauge (`T = t`; the khronon eaten, the scalar mode living in the metric), the acceleration is `a_i = ∂_i \ln N` — **spatial gradients of the lapse only**. The `W(A²)` sector therefore contributes **no time derivatives** to the action, at any order in `W`: the time-kinetic structure of the scalar mode is carried entirely by the extrinsic-curvature sector (the `λθ² + βσ²` terms plus Einstein–Hilbert), which Round 2 showed is **untouched by the MOND generalization**. Consequence:

> **The `W`-generalization adds no new ghost by direct counting.** The no-ghost condition of the unified theory is the no-ghost condition of the *linear* khronometric theory (a parameter-range condition on the `λ, β` sector), unchanged. [Derived; the round's cleanest result.]

The caveat that keeps this honest: in constrained systems the `W`-sector can still enter the *effective* kinetic matrix through elimination of the non-dynamical lapse (the `a²`-type term stiffens `δN` spatially, and solving the constraints feeds that back). That feedback is exactly what the §2.3 degeneracy tracks; it does not introduce time derivatives, but it can degenerate the normalization.

### 2.2 The static sector: the classic AQUAL conditions (clean pass)

Perturbing the static equation around a background `∇Φ₀` gives the anisotropic elliptic operator with coefficients `μ_{\rm tot}` transverse to `∇Φ₀` and `d(x\,μ_{\rm tot})/dx` along it. The classical Bekenstein–Milgrom well-posedness conditions are

> `μ_{\rm tot}(x) > 0` and `d(x\,μ_{\rm tot})/dx > 0`.

Deep IR (`μ_{\rm tot} = x`): both hold (`x > 0`, `d(x²)/dx = 2x > 0`). High-`A` (`μ_{\rm tot} → 1`): both hold trivially. **The static operator is elliptic and well-posed across the whole interpolation provided `μ_{\rm tot}` is monotone-compatible — the same condition the AQUAL literature has always imposed, here inherited rather than invented.** Note what this buys: even though `W'` itself is *negative* in the deep IR (the cancellation), the **total** operator — Einstein term included — is healthy. The cancellation does not destabilize statics. ✓

### 2.3 The genuine soft spot: the `A → 0` vacuum degeneracy (named, not hidden)

Toward exact vacuum (`A → 0`: no acceleration anywhere), `μ_{\rm tot} → 0`: the static operator **degenerates**, the scalar's gradient stiffness vanishes, and the propagation speed of scalar perturbations falls as `c_s² ∝ A`-type toward zero — with the strong-coupling scale dropping alongside. This is the **known deep-vacuum degeneracy of MOND-class field theories** (the non-analytic `|∇Φ|³`-type action has a vanishing quadratic term around the zero-field background); it is not specific to the khronon embedding, and the class's own analyses (Blanchet–Marsat and the generalized-aether literature) report viable parameter corners on nontrivial backgrounds — **we have not independently re-derived those analyses here**, and say so. [I — class literature, cited at the level of "reported viable," not verified.]

Three honest remarks:

1. **Physical backgrounds sit off the degenerate point.** Everywhere in and around galaxies `A > 0`; the degenerate configuration is the exactly-unaccelerated vacuum.
2. **The ED-structural hint (flagged, deliberately not implemented).** On the cosmological background the khronon congruence has `a = 0` but `θ ∼ H ≠ 0` — the expansion. A deep-IR sector regulated by the cosmic expansion (the invariant acquiring `θ`-dependence near `A → 0`) would lift the degeneracy *and* is structurally suggested by ED's own anchoring (the khronon's background **is** the Hubble flow; `a₀ ∼ cH₀` already says the two scales meet there). Implementing this now would be reverse-engineering a cure; it is **named as Round 4's question**, with the note that it is also exactly where the cosmology/SCBU tie-in lives.
3. **Slow modes and Čerenkov.** A slow scalar in deep-MOND regions raises a potential gravitational-Čerenkov concern for high-energy cosmic rays traversing galactic outskirts; whether the mode's matter coupling makes this binding is a model-detail check — **open, Round 4.** (At high `A` the scalar is superluminal, the khronometric class character — allowed given the foliation, and the Paper_033/034 reframe stands.)

**Verdict (A): the deep-IR branch is *not ruled out*.** No new ghost (structural); statics elliptic (classic conditions, pass); gradient sector healthy for `A > 0` with slowing modes toward vacuum; the `A → 0` degeneracy is the live edge, known-in-class, with a flagged ED-native candidate regulator deferred to Round 4. "Stable on physical backgrounds, degenerate at the unphysical point, full anisotropic quadratic analysis not independently closed here" — that is the honest sentence.

---

## 3. (B) Interpolation and solar-system screening

**The mechanism.** Screening here is *not* Vainshtein-type; it is the smallness of the residual: at solar accelerations `x = |∇Φ|/a₀ ∼ 10⁷–10⁸`, `W' → α_{\rm eff}` (the linear khronometric coupling) and the force correction is the tail `δμ = μ_{\rm tot} - 1 = c_1(W' - α_{\rm eff}) + c_1α_{\rm eff}`.

**Two separate constraint channels, kept distinct:**

1. **The preferred-frame channel (`α₁, α₂`)** — set by the *asymptotic constant* `α_{\rm eff}` and the `λ, β` sector: the standing GR-II front, unchanged. The linear khronometric theory has known viable corners (including the subfamily where `α₂` vanishes identically); binary-pulsar constraints on khronometric parameters (the Yagi–Blas–Yunes–Sibiryakov-type analyses) bound but do not exclude them. [I — class literature.] Nothing new is added or evaded by `W`.
2. **The interpolation-tail channel** — set by *how fast* `W'` saturates. This is a genuine, quantitative squeeze: Cassini-class ephemeris bounds on anomalous solar-system accelerations are known to **exclude the slowest-saturating MOND interpolation families** (inverse-power tails `μ ≈ 1 - 1/x` produce fractional corrections `∼ 10⁻⁸` at Saturn, at the edge of exclusion), while faster (e.g. exponentially saturating) families survive. [I — the published MOND-interpolation constraint literature.] **Status upgrade for the family:** Round 1 left the interpolation as an unconstrained honest family; it is now a **constrained family** — still not pinned, no member load-bearing for the unification, but with named members already excluded. That is falsifiable space shrinking in the right way: the theory's middle is being measured, not protected.

**Effective scalar charge.** In the screened regime a compact source's scalar charge is suppressed by the same smallness (`∝ α_{\rm eff}` plus the tail), so strong-equivalence-principle violations and dipole radiation in binaries are those of the *linear* khronometric theory — pulsar-tested, viable-corner status. In the *unscreened* (`x ≲ 1`) regime the scalar is active by design — that is the MOND phenomenology itself, and **wide-binary systems near `a₀` are the live observational frontier** where this theory and Newtonian expectations genuinely diverge (an opportunity, not only a constraint).

**Verdict (B): PPN-safe in the same corner GR-II already occupied, with the interpolation family now Cassini-constrained.** No additional structure was needed; no failure found; the family tightened.

---

## 4. (C) The longitudinal τ-mode

**Identification.** `T = t + τ(x, t)`: in unitary gauge τ is eaten and *is* the metric's scalar mode — the khronon mode is not an extra player beside the breathing polarization GR-II counted; it **is** that mode. Statics force `τ = 0` (Round 2); time-dependent and rotating systems excite it.

- **High-`A` (screened) regime:** the mode propagates as in linear khronometric theory — superluminal scalar, couplings `O(α_{\rm eff})`-suppressed, pulsar-viable corner. **Benign-as-screened.**
- **Transition and deep-IR regimes:** the mode's gradient stiffness is the §2 anisotropic operator: healthy for `A > 0`, slowing toward vacuum; its excitation in time-dependent galactic dynamics (bars, mergers, orbiting satellites) is the theory's dynamical MOND sector — *predictive territory* (this is where MOND-class theories differ observably from particle dark matter in dynamics), not yet a computed deliverable.
- **Strong coupling:** the τ-mode's interactions grow as the kinetic normalization drops — the **same** `A → 0` edge as §2.3, not a second pathology. Single named soft spot, one address.
- **Dipole radiation:** suppressed in screened binaries (above); unscreened wide systems radiate scalar — below current sensitivity but in-principle distinctive.

**Verdict (C): benign-as-screened at high `A`; the dynamical deep-IR τ-sector is open predictive territory; its only pathology channel is the already-named `A → 0` degeneracy.**

---

## 5. (D) The ED translation

With `a_i = ½∂_i\ln b`, the deep-IR cancellation reads, in substrate language:

> **When the logarithmic bandwidth gradient falls below the cosmic rate (`|∇\ln b| ≲ 2a₀`), the static constraint switches branches: the Einstein (commitment-linear) response cancels and the response becomes the geometric-mean branch — sourced by `|∇\ln b|` itself measured against `a₀`.**

Three findings on naturalness:

1. **The crossover *scale* is structurally natural, not a dial.** The khronon's background has exactly one scale — the Hubble rate (it *is* cosmic time) — so a crossover, if there is one, can only sit at `∼ cH₀`. `a₀` is not tuned into `W`; it is the only scale `W`'s argument can be measured against. (The `1/2π` stays inherited from Paper_029.)
2. **The crossover *form* is forced-given-030 — and 030 is the substrate's own statement of it.** Paper_030's P14 *bilocal coupling* (the geometric mean of the local and cosmic accelerations) is, read structurally, precisely the assertion that the substrate's weak-gradient response is normalized by the cosmic rate. The khronon EFT does not add this claim; it **mirrors** the corpus's existing substrate-side mechanism in relativistic form. The two are one claim in two languages — which is what "embedding, not re-deriving" should look like.
3. **The substrate forbids nothing and enforces one thing.** Nothing in the primitives excludes the IR branch (no invariant is touched; `W` lives in the foliation sector GR-II already counted). What the substrate *does* enforce is the high-`A` branch: commitment-linearity (P-Commitment-Linear) demands `μ → 1` at strong gradients — the screening limit is not optional, it is GR-I. The primitives-level *derivation* of the IR branch (why the bilocal coupling; why the cancellation) remains the deliberately-deferred deepest question — unchanged, guard up.

**Verdict (D): natural scale, mirrored (not invented) form, nothing forbidden, the Einstein branch enforced.** No fine-tuning flag beyond the §2.3 degeneracy already named.

---

## 6. Round-3 Summary

**Survives:**
- No new ghost — the `W`-sector adds no time derivatives; the no-ghost condition is the linear khronometric one (structural, clean).
- Static well-posedness across the interpolation — the classic AQUAL ellipticity conditions hold (deep IR: `μ = x` passes both).
- The cancellation does **not** destabilize statics: the *total* operator is healthy even where `W' < 0`.
- Screening: PPN-safe in the linear-khronometric viable corner; pulsar-safe as screened; lensing verdict (R2) unaffected.
- τ-mode: identified as the breathing scalar GR-II already counted; benign-as-screened; its deep-IR dynamics are predictive territory (wide binaries the live frontier).
- ED-naturalness: the crossover scale is the khronon's only scale; the form mirrors Paper_030's own bilocal mechanism.

**Fails:** nothing outright. No kill condition triggered.

**Soft spots (named, one address):**
- **The `A → 0` vacuum degeneracy** — vanishing stiffness, slowing modes, dropping strong-coupling scale at the exactly-unaccelerated point; known-in-class; class literature reports viable corners not independently verified here.
- Čerenkov for slow modes in deep-MOND regions — open check.
- The interpolation family — now **Cassini-constrained** (slow-saturating members excluded); still a family.
- Clusters/CMB — inherited, out of scope, standing.

**Deferred to Round 4:**
1. **The cosmological regulator** — does the `θ`-sector (the khronon's Hubble expansion, `θ ∼ H` where `a = 0`) lift the `A → 0` degeneracy *without* retrofit? This is simultaneously the stability question and the SCBU/cosmology tie-in — the two open threads are one thread.
2. Čerenkov bound for the deep-IR slow mode.
3. (Standing, guarded) the primitives-level origin of the IR branch.

---

*Round-3 viability analysis. The unified theory survives its first full kill-check: no new ghost (the `W`-sector is time-derivative-free in unitary gauge — the round's cleanest structural result), classic AQUAL ellipticity holds across the interpolation, the Einstein-cancellation does not destabilize statics, screening is PPN/pulsar-safe in the linear khronometric corner, and the τ-mode is the already-counted breathing scalar, benign as screened. The one genuine soft spot is the known-in-class `A → 0` vacuum degeneracy — physical backgrounds sit off it, the class literature reports viable corners (not independently verified here), and ED's own structure points at the cosmological regulator (`θ ∼ H`) as the non-retrofit cure, deferred to Round 4 where it merges with the SCBU tie-in. The interpolation family is upgraded from unconstrained to Cassini-constrained. Nothing reverse-engineered; failures and non-verifications stated; GR-I untouched; clusters/CMB still owed.*
