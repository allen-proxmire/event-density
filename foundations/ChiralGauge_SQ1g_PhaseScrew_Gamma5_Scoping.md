# #2b · SQ1g — The Phase-Screw → γ⁵ Step: Pinning the Discriminator (step 1 of the real derivation)

**Foundations — first step of the actual T4-with-chirality derivation (not a deferral). Goal: turn "does the committed-phase screw become relativistic handedness?" into a single, computable yes/no condition on ED's primitives. Result: the chiral-vs-vector question reduces exactly to — *under P05 transport along the arrow, is the P09 phase-advance helicity-dependent?* If yes → chiral (γ⁵) coupling, parity violation. If no → vector (EM-like), parity-conserving, and the screw route fails. This doc derives that discriminator, locates the one substrate ingredient it hinges on, and lays out the derivation steps we run next. Honest prior: the default (standard minimal coupling) is *vector*; the chiral outcome requires a specific helicity–phase correlation that is not yet shown — it could go either way, and that is exactly why it is worth computing.**

**Crank rail.** This pins the question; it does not answer it. The discriminator is derived from standard chiral-gauge structure; whether ED satisfies it is the open computation. I flag the default-vector prior explicitly so a chiral result has to be *earned*, not assumed.

---

## 1. The target, stated as an action

The emergent fermion couples to the P09 U(1) field `A` (the coarse-grained phase). Two possibilities, and everything rides on which:

- **Vector** (electromagnetism-like, parity-conserving): `L ⊃ ψ̄ γ^μ(∂_μ + i g A_μ) ψ` — the covariant derivative is the *same* for `ψ_L` and `ψ_R`. Both handednesses carry the same P09 charge.
- **Chiral** (weak-force-like, parity-violating): `A` couples to `ψ_L` and `ψ_R` with *different* charges (e.g. `+1` and `0`): `L ⊃ ψ̄_L γ^μ(∂_μ + i g A_μ)ψ_L + ψ̄_R γ^μ ∂_μ ψ_R`.

The discriminator between them is a single number: **the P09 charge of `ψ_L` minus the P09 charge of `ψ_R`.** Zero ⇒ vector. Nonzero ⇒ chiral. Nothing else matters for parity violation.

## 2. The discriminator, in ED's own variables

A fermion component's "P09 charge" *is* the rate at which its P09 phase advances under transport (P05) along the arrow. So the action-level discriminator translates exactly into a substrate question:

> **Does a left-handed mode and a right-handed mode acquire the *same* P09 phase-advance when transported one commitment-step along the arrow (⇒ vector), or *different* advances (⇒ chiral)?**

This is the whole step, reduced to one computable comparison. It is clean because it removes every red herring:

- It is **not** about whether the phase sits on timelike links. A phase on timelike links alone gives `ψ̄γ⁰A₀ψ` — the *temporal component of a vector* coupling (charge density). Still vector. (This is the honest limit of the earlier "γ⁵ contains γ⁰, the arrow is timelike" hope: time-singling-out is necessary but *not* sufficient — it gives a temporal vector coupling unless it is also **helicity-dependent**.)
- It is **not** about whether the transport fermion is doubled. SQ1f already settled that the transport survivor is vector-like; the chirality, if any, lives in the *phase coupling*, and §2's comparison is the only thing that decides it.

## 3. The one ingredient it hinges on

Helicity is `spin · momentum / |momentum|`. The arrow fixes a one-way direction of motion (retarded V1; modes propagate *along* the arrow). So a forward-propagating mode's helicity is the sign of `spin · (arrow-direction)`. The discriminator becomes:

> **Does P05's phase-transport rule depend on `spin · (arrow-direction)` — i.e. on whether the mode's spin aligns or anti-aligns with the arrow it is forced to move along?**

- If P05 advances the phase **independently of spin orientation** → both helicities get the same advance → **vector**. (This is the default; standard minimal coupling is spin-blind.)
- If P05's phase-advance **couples to the spin–arrow alignment** → aligned and anti-aligned modes advance oppositely → **chiral**, and the screw is real: the helix's pitch-sign *is* the helicity, and the P09 coupling *is* axial (γ⁵).

So the entire phase-screw → γ⁵ claim lives or dies on **one property of P05: is its phase-transport spin–arrow-coupled or spin-blind?** That is now a definite question about a single primitive, not a vibe about helices.

## 4. The structural case, honestly weighed

**For chiral (spin–arrow coupling):** P05 is *polarity* transport — it carries an oriented internal quantity along directed edges. If the polarity it transports includes the spin/orientation degree of freedom (P09's phase is the U(1) part; the full polarity bundle P07 carries more), then transport along the arrow naturally couples the advance to spin–arrow alignment, because the transported object and the transport direction are not independent. ED's polarity transport is *not* obviously the spin-blind scalar hopping of textbook minimal coupling — it is structured. That is the real reason this is not a foregone vector conclusion.

**For vector (the default prior):** absent a specific spin–arrow term, coarse-graining a U(1) link phase gives minimal (vector) coupling — that is the generic outcome, and it is what electromagnetism *is*. The chiral outcome is the special case and must be produced by an actual feature of P05/P07, not hoped for.

**My honest read:** default vector, with a genuine and specific channel to chiral through the structure of P05/P07 polarity transport. ~Even odds, worth computing, and the computation is well-defined.

## 5. The derivation we run next (steps, ours)

1. **Write the discrete spinor.** Build the two-component (Weyl) mode structure on the directed graph from T4's emergent-spinor construction — the minimal object that *has* a helicity (spin–arrow alignment).
2. **Apply P05 to each helicity.** Transport an aligned mode and an anti-aligned mode one commitment-step along the arrow under P05's actual rule; read off each one's P09 phase-advance.
3. **Compute the discriminator** (§2): advance(L) − advance(R). Zero ⇒ vector ⇒ screw route fails (fall back to: is parity violation then *spontaneous*, IC-selected?). Nonzero ⇒ chiral ⇒ the screw *is* γ⁵, and §3's spin–arrow coupling is the mechanism.
4. **If chiral, check the magnitude is maximal** (pure `1±γ⁵`, V−A) vs partial — SQ1d predicts maximal (topological), so a partial result would be a tension to resolve.

Step 1 is the gate: it needs T4's emergent-spinor structure made explicit enough to carry a helicity. That is the real work, and it is the same spinor structure the whole matter sector needs — so doing it here is not a detour, it is the matter-sector derivation, entered through its sharpest question.

## 6. Status

**The phase-screw → γ⁵ step is now a single computable discriminator: advance(L) − advance(R) under P05 transport along the arrow, which hinges on whether P05's phase-transport is spin–arrow-coupled (chiral) or spin-blind (vector).** This is step 1 of the real derivation, done: the question is pinned, the deciding primitive (P05/P07 polarity transport) is located, the default-vector prior is stated, and the genuine chiral channel (structured polarity transport, not scalar hopping) is identified. Next is the computation itself — build the emergent helicity (T4), transport it, compare the advances. That is ours to run, and it is the door into the matter-sector derivation, not a side quest.

---

*#2b SQ1g — pins the phase-screw → γ⁵ step. Reduces "does the screw become relativistic handedness?" to ONE computable discriminator: under P05 transport along the arrow, advance(L) − advance(R) of the P09 phase. Zero ⇒ vector (EM-like, parity-conserving, screw route fails) ⇒ fall back to spontaneous/IC parity breaking; nonzero ⇒ chiral (γ⁵, parity violation), screw is real. Hinges on ONE primitive property: is P05's phase-transport spin–arrow-coupled (⇒ chiral) or spin-blind (⇒ vector, the default)? Kills two red herrings: timelike-phase alone = temporal VECTOR coupling (γ⁰ necessary not sufficient — needs helicity-dependence); transport-doubling already settled (SQ1f vector-like; chirality lives in the coupling). Structural case: default vector, but real chiral channel via structured P05/P07 polarity transport (not scalar minimal coupling) — ~even odds, well-defined. Derivation steps (ours): build emergent helicity (T4 spinor), transport each helicity under P05, compute advance(L)−advance(R), check maximality (SQ1d predicts pure V−A). Step 1 (this doc) done; step 2+ is the real T4 matter-sector derivation entered through its sharpest question. Crank-rail: discriminator derived from standard structure; ED's answer is the open computation; default-vector prior stated so chiral must be earned.*
