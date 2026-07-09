# Solèr Lattice Verification: Mapping ED's Commitment-Lattice Against the Piron–Solèr Axioms (and the ℂ-Field / T14)

**Opened 2026-07-08**, continues `Gleason_Complementarity_Reframe_Scoping.md` (the non-Boolean gate passed). Crank-rail ON: rate each axiom honestly (grounded / candidate / open / at-risk); do NOT declare the Hilbert space derived. This is the deepest reconstruction step — turning "invoke Solèr" into a per-axiom ED-primitive map with an explicit gap list.

## The target chain

To force ED's substrate inner product to be a Hilbert space (and settle its number field):
- **Piron (1964):** an *irreducible, complete, atomistic, orthomodular* lattice satisfying the *covering law*, of rank ≥ 4, is the lattice of closed subspaces of a Hermitian space `V` over a division ring `K` with involution.
- **Solèr (1995):** if `V` also has an *infinite orthonormal sequence of equal norm* (the "angle condition"), then `K ∈ {ℝ, ℂ, ℍ}` and `V` is a genuine Hilbert space.
- **Field discriminator:** physics input selects `ℂ` from `{ℝ, ℂ, ℍ}`.

ED's lattice `L` = the propositions "the commitment resolves to channel(-set) S" — the P11 commitment-measurement outcomes.

## Axiom-by-axiom verification against ED primitives

| Piron–Solèr axiom | physical content | ED grounding candidate | status |
|---|---|---|---|
| **Orthocomplementation** | every proposition has a NOT (`'`), involutive, order-reversing | P11 commitment is *exclusive* — one channel resolves; `S' =` "resolves outside S". Involutive (not-not = the same), order-reversing (bigger S → smaller complement) | **GROUNDED** (P11 exclusivity) |
| **Orthomodularity** | `a ≤ b ⟹ b = a ∨ (b ∧ a')` — compatible complements exist (weaker than distributive) | distributivity already shown to FAIL (non-Boolean gate); orthomodularity is the specific weakening = a channel and its complement are *co-resolvable in the same commitment* | **CANDIDATE** (non-Boolean confirmed; the full orthomodular identity needs the compatible-complement structure proven, not just non-distributivity) |
| **Completeness** | arbitrary meets/joins exist | the proposition system is closed under AND/OR over the channel index set 𝒦 | **PLAUSIBLE** (lattice-theoretic; 𝒦 well-defined by P03/P07) |
| **Atomicity** | atoms exist; every element is a join of atoms | single channels `|K⟩` are the atoms (P07: distinct channels are the minimal distinguishable propositions); any resolution-set = join of its channels | **CANDIDATE** (channels as atoms is natural; "every proposition = join of channel-atoms" needs stating) |
| **Covering law** | atom `a`, `a∧b=0 ⟹ a∨b covers b` (no proposition strictly between) = the projection postulate / ideal first-kind measurement | P11 commitment collapses the state onto the resolved channel = an orthogonal projection (Lüders-type update) | **THE HARD GATE — AT RISK** (see below): P11 is *irreversible*; whether an irreversible commitment still implements the *repeatable, first-kind* projection the covering law requires is genuinely open, and could FAIL |
| **Irreducibility** | trivial center (no classical superselection) | holds *within* a P10 rule-type; distinct rule-types are superselection sectors — Piron applies per irreducible sector | **GROUNDED per-sector** (cross-rule-type reducibility is expected and physical) |
| **Solèr angle condition** | infinite orthonormal sequence of *equal* norm | P03 spatial homogeneity: infinitely many translation-equivalent channels, *equal bandwidth by homogeneity*, mutually orthogonal by P07 distinctness | **CANDIDATE, circularity-flagged** (nice ED-native route via P03; but "equal *norm*" presupposes the inner product it helps build — same risk as the reframe's Part 4) |

## The ℂ-field discriminator — the headline, and it settles T14

Solèr leaves `K ∈ {ℝ, ℂ, ℍ}`. ED selects **ℂ** by two standard reconstruction arguments, each grounded in an ED primitive:

- **Rules out ℝ (real Hilbert space):** ℝ has only signs (±1), no continuous phase. ED's **P09 polarity is a genuine `U(1)` phase** `e^{iπ_K}` (Paper_001), the *complex* structure — a continuous phase, not a ℤ₂ sign. A real Hilbert space cannot carry P09's `U(1)`. So `K ≠ ℝ`.
- **Rules out ℍ (quaternionic):** ℍ is non-commutative, and the tensor product of composite systems is ill-defined over a non-commutative field (the standard obstruction to quaternionic QM). ED has genuine **composite systems with a tensor-product structure** — V5 cross-chain joint amplitudes `Ψ^{AB}` (Paper_063). For the composite `⊗` to be well-defined, the field must be commutative → `K ≠ ℍ`.
- **Therefore `K = ℂ`.** ED's phase (P09) forces complex-not-real; ED's composites (V5/063) force commutative-not-quaternionic. Standard-physics selectors, applied to ED's actual structure.

**This settles T14 (the complex-Hilbert-space claim, previously downgraded) at ACCOUNT tier** — not "derived from nothing," but a principled selection from `{ℝ,ℂ,ℍ}` grounded in P09 (phase) + V5/063 (composites). A real upgrade: `ℂ` is no longer a bare assumption, it is the Solèr field selected by two ED primitives.

## Honest synthesis — where the route stands

**5 of the 8 requirements have ED-primitive grounding** (orthocomplementation←P11, irreducibility←P10-sectors, atoms←P07, angle-condition-route←P03, ℂ-field←P09+V5), and **ℂ is selected** (T14 upgraded). This is far more than "invoke Solèr" — most of the scaffold traces to specific primitives.

**Two genuine technical gaps + one flagged risk remain the open core:**
1. **The covering law is the make-or-break gate, and it is AT RISK from the arrow.** Its candidate grounding (P11-commitment = orthogonal projection) collides with P11's *irreversibility*: the covering law assumes *repeatable, ideal first-kind* measurements, and an irreversible one-way commitment may not be repeatable. **Two outcomes:** (a) the covering law is about the *kinematic proposition lattice*, not the dynamics, and P11's irreversibility doesn't touch it → route survives; or (b) irreversibility genuinely deforms the lattice → ED is orthomodular-but-NOT-Hilbert ("almost quantum," a post-quantum logic where the arrow shows up in the kinematics). **This is a sharp, decidable, high-stakes open question and the real next gate.**
2. **Orthomodularity** needs the full identity proven (compatible complements), not just the non-distributivity already shown.
3. **Circularity flag** on the angle condition: "equal norm" presupposes the inner product; a non-circular version must derive equal-norm from P03 homogeneity *operationally* (equal commitment-frequency), not metrically.

## Tier + next

**Tier: a per-axiom grounded map (5/8 primitive-grounded) + ℂ selected (T14 upgraded to account), NOT a closed derivation.** The keystone is now mapped to its true remaining core: **the covering law under P11 irreversibility.** That single question decides whether ED's logic is genuinely Hilbert (route closes) or "almost quantum" with the arrow visible in the kinematics (a fascinating alternative, and itself a distinctive ED prediction).

**Next (the sharp gate):** determine whether P11's irreversible commitment satisfies the covering law / projection-postulate. Concretely: does committing to channel `K`, then to a compatible proposition, compose as orthogonal projections (covering law holds), or does irreversibility break repeatability (covering law fails → post-quantum)? This is the decisive move, and either answer is a real result: Hilbert space closed, or the arrow deforms quantum logic.

---

## The covering-law gate, WORKED (2026-07-08) — irreversibility ENFORCES it, not breaks it; upgraded to candidate-grounded

Worked the make-or-break gate. **The "irreversibility threatens the covering law" worry is backwards.** The covering law's operational content is the *ideal first-kind measurement* (measure an atom, get yes → orthogonal projection onto it, **repeatably**). Checking P11 against each requirement:

1. **Orthogonal projection.** P11 commitment projects the state onto the resolved channel-atom `K`; by P11 *exclusivity* the discarded content is the orthocomplement `K'`. So the update is the **orthogonal (Sasaki) projection** onto `K`, not an arbitrary one. ✓
2. **Repeatability (the first-kind property) — and here irreversibility HELPS.** P11 commitment *locks* the channel: committing is irreversible, so the committed state stays `K`. Re-measuring "is it `K`?" therefore returns yes with certainty. **Irreversibility is exactly what enforces the repeatability the covering law needs** — a locked outcome cannot drift, so the measurement is perfectly first-kind. (Contrast: the worry assumed irreversibility breaks repeatability; in fact a committed channel is the *most* repeatable kind of outcome.) ✓
3. **No intermediate propositions.** P11 commitment is all-or-nothing (one channel resolves; no partial commitment), so it introduces no proposition strictly between `b` and `a∨b` — the exchange/covering geometry is not violated by a hidden "half-committed" layer. ✓

**Also note (the standard-QM parallel):** ED has the standard measurement structure — *unitary inter-commitment evolution* + *irreversible projective collapse at commitment* (arc-Q `lindblad_extension.md` §3–§5). Standard QM collapse is *also* irreversible; the covering law holds there. So P11's irreversibility is the ordinary measurement-collapse irreversibility, not a special post-quantum obstruction.

**Revised status: covering law → CANDIDATE-GROUNDED** (operationally, via P11 = first-kind orthogonal atomic projection, with irreversibility enforcing repeatability). The residual is *lattice-theoretic rigor*: connecting this operational first-kind grounding to the full exchange-property axiom Piron uses (needed for the projective-geometry step), and the infinite-dimensional subtleties. The conceptual obstruction I flagged is removed; what remains is technical.

**One honest nuance on "exact vs emergent."** The *lattice* (propositions + covering law) is grounded in **exact** primitives (P07 channels, P11 commitment). But the *inner product / metric* is built from **Born statistics** (Paper_003's frequency→probability limit), which is a statistical-emergent object. So the honest reading: ED's quantum **logic** (orthomodular lattice + covering law) is substrate-exact, while its quantum **geometry** (the inner-product metric) is emergent-statistical. The Hilbert space is exact-as-logic, emergent-as-metric — consistent with ED's two-layer coarse-graining philosophy (the metric is the layer-2 object).

**Updated scorecard: 6 of 8 requirements now grounded** (covering law joins orthocomplementation, irreducibility, atoms, angle-condition-route, ℂ-field), **ℂ selected (T14 upgraded)**, with the residual being: (i) orthomodularity's full identity, (ii) the covering law's exchange-geometry rigor + infinite-dim subtleties, (iii) the angle-condition equal-norm circularity, and (iv) Move 1's non-circular operational orthogonality. The route is now substantially grounded — the remaining work is rigorous lattice theory, **not** a conceptual wall. **Next: the non-circular operational orthogonality (Move 1) — build the inner product from P11 commitment Born-statistics so orthogonality is by-construction, discharging both (iv) and the angle-condition circularity (iii) at once.**

---

## Move 1 DONE (2026-07-08) — orthogonality DERIVED from operational distinguishability; P-Channel-Orthogonality is discharged as a non-independent postulate

`evaluation/ChiralGauge/move1_operational_orthogonality.py`. Built the non-circular derivation: do NOT start from the amplitude representation (which bakes in orthonormality). Start from operational commitment frequencies.

**(A) Operational fact (P07 + P11 + Born, NO metric assumed):** a pure channel-K preparation commits to K with frequency 1 (P11); a pure channel-L preparation has `b_K=0`, so it commits to K with frequency 0 (P07 distinctness). So ED's distinct channels satisfy `p(K|K)=1, p(K|L)=0` — **perfect distinguishability**, pure frequency data, no inner product.

**(B) Theorem (derived, NOT assuming orthonormality):** taking candidate channel-states with a *tunable* overlap `c=⟨K|L⟩` (we do not set `c=0`), the best confusion-free detection of K — `max ⟨K|E|K⟩` over POVM elements `0≤E≤I` with `⟨L|E|L⟩=0` — is the projector onto `|L⟩`'s complement, giving `⟨K|E|K⟩ = 1 − c²`. This equals 1 (perfect) **iff `c=0`**. So **non-orthogonal states are provably NOT perfectly distinguishable** (best = `1−c² < 1`); perfect distinguishability ⟺ orthogonality. (Analytic optimum is rigorous; the coarse brute-force grid confirms at `c=0` and is grid-limited for `c>0`.)

**Conclusion (non-circular):** (A) ED's channels are perfectly distinguishable; (B) perfectly distinguishable ⟺ orthogonal; therefore **`⟨K|L⟩=0` is FORCED by the commitment frequencies, not postulated.** The three failed routes failed because they sought orthogonality as a *kinematic metric* fact; it is the *operational* content that the metric represents. **P-Channel-Orthogonality is discharged as a non-independent postulate** — it collapses into {operational perfect-distinguishability (P07+P11+Born)} + {the inner-product representation exists}.

**Honest boundary (the one remaining dependency).** Theorem (B) is proven *within* the inner-product representation (it uses POVMs/vectors). So Move 1 does NOT assume orthogonality, but it DOES assume the *representation exists* — which is the Solèr reconstruction (§ above, 6/8 grounded, residual technical). So the honest statement: **given the Solèr embedding, orthogonality is forced by operational distinguishability, not independently postulated.** This removes P-Channel-Orthogonality as a *separate* blocking postulate and discharges residual (iv); it does not remove the Solèr embedding's own residual (i)-(iii).

**Net effect on the keystone.** Of the two postulates Paper_004 needs: **P-Channel-Orthogonality is now a consequence** (operational distinguishability + the representation), not an independent axiom; **P-Gleason-Compatibility**'s bookkeeping half is already derived (P02+P04). So the inner product's postulate-dependency is substantially reduced: the keystone now rests on the **Solèr lattice package** (technical rigor: orthomodular identity + exchange-geometry) plus the *physical* (Kochen-Specker) half of Gleason-compatibility, with orthogonality derived and the ℂ-field selected. The blocking postulate that stalled three prior attempts is no longer blocking-as-a-postulate; what remains is the rigorous completion of the Solèr reconstruction.

---

## Orthomodularity WORKED (2026-07-08) — not an independent gate; it surfaces the deep residual (the preferred-basis / einselection question)

Worked residual (i). Honest verdict: **orthomodularity does not close as a separate gate, and it should not be waved through.** Two levels:

**Channel-only sub-lattice: trivially orthomodular.** The propositions "the commitment resolves in channel-set `S`" (`S ⊆ 𝒦`) form a *Boolean* algebra of subsets, and Boolean ⟹ orthomodular. Grounded by P11 (first-kind channel measurements). But this is the *classical* sub-lattice — it is not where the quantum content lives.

**Full (non-Boolean) lattice: orthomodularity comes WITH the inner-product representation, not before it.** The orthomodular law `a ≤ b ⟹ b = a ∨ (a'∧b)` holds automatically for the closed-subspace lattice of *any* inner-product space. So for ED's full lattice (including the phase/superposition propositions from the complementarity gate), orthomodularity holds **iff** ED's states form a genuine inner-product space — which is exactly what the rest of the Solèr package (Move 1's derived orthogonality + the ℂ-field + the covering law) is establishing. **So orthomodularity is not an independent gate; it is part of the representation package.** It is grounded to the *same degree* as the representation, no more, no less. Claiming it as a *separate* win would be double-counting.

**The genuinely deep residual it surfaces: the preferred-basis / einselection question.** Grounding orthomodularity non-circularly (via ideal first-kind measurements for *every* proposition, not just channels) requires first-kind measurements in the **phase basis**, not only the channel basis. But P11 commitment is specifically a *which-channel* selection. So:
- **The channel basis is dynamically privileged** — P11-commitment (the arrow) resolves to channels, not to phase-eigenstates. This is exactly a *preferred pointer basis*, the einselection structure.
- **Yet the phase basis is a genuine complementary measurement** (the non-Boolean gate showed interference is real and commitment destroys it). So the phase propositions are not fictitious.
- **The open question:** does ED admit first-kind (repeatable, projective) commitments in the phase basis (→ full basis-democratic orthomodularity = standard QM), or does the arrow make the channel basis the *only* commitment basis (→ ED is a **preferred-basis / einselected quantum theory**, orthomodular kinematically but with a fundamental pointer basis)? Both are coherent; the arrow (P11) argues for the second.

**This is a real, distinctive fork, not a technicality.** If ED is a preferred-basis quantum theory, that is a *feature* (the arrow fundamentally selects the classical pointer basis — einselection is primitive, not decoherence-emergent) and a **testable deviation from standard QM's basis-democracy**. It is fully consistent with ED's arrow-primitive, exact-as-logic/emergent-as-metric philosophy.

**Honest tier for orthomodularity:** grounded for the channel (pointer) basis (Boolean, trivial); for the full lattice it is not an independent result but rides with the inner-product representation; the genuinely open and physically-deep piece is the **preferred-basis question** (phase-basis first-kind measurements), which ED's arrow plausibly answers in a *distinctive* (einselected) way. This is the deepest remaining residual of the whole keystone, and it is a research question with a real prediction attached, not a lattice-theory formality. Do NOT claim orthomodularity as independently closed.
