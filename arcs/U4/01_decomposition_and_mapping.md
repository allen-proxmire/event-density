# Memo 01 — U4 Decomposition, Circularity Audit, and Transfer Audit

**Date:** 2026-04-26
**Arc:** `arcs/U4/`
**Predecessor:** [`00_arc_outline.md`](00_arc_outline.md)
**Status:** Structural inventory memo with circularity audit and transfer audit. Decomposes U4 into five sub-features, performs an explicit circularity audit (with U3 as sibling CANDIDATE handled per Framing 1), audits the 2026-04-24 tightening-program memo for which arguments transfer cleanly under the 2026-04-26 methodology, classifies each sub-feature by structural status, recasts the seven falsifiers in light of the audits, and recommends a structure for Memo 02.
**Purpose:** Pin down the conceptual terrain so Memo 02 can derive F1 + F2 + F5 directly and Memo 03 can focus on the load-bearing F3 (quadratic-in-$k$ kinetic structure) and F4 (specific coefficient $1/(2m)$) questions, with explicit handling of the Galilean-invariance question.

---

## 1. Sub-Feature Decomposition

The five sub-features of U4, restated in their minimal falsifiable form:

### 1.1 F1 — Channel-momentum identification

**Claim.** In the thin/continuum limit, the channel index $K$ admits a continuous momentum-space coordinate $k$. The basis change between channel-representation and momentum-representation is the standard Fourier transform on the U2 Hilbert space, with the translation generator $\hat{p}$ identified as a self-adjoint operator via Stone's theorem.

**Status: forced-via-derivation.** Direct transfer of U5 Memo 03 §1's machinery to the channel-basis question; no new structural commitment beyond what U5 already established.

### 1.2 F2 — Plane-wave eigenfunctions

**Claim.** The eigenfunctions of $\hat{p}$ in the position representation are plane waves $\langle x | k \rangle = (2\pi\hbar)^{-d/2} \cdot e^{i k \cdot x / \hbar}$.

**Status: automatic given F1.** Mathematical consequence of $\hat{p} = -i\hbar \nabla$ applied to position-representation wavefunctions; no structural commitment beyond F1.

### 1.3 F3 — Quadratic-in-momentum kinetic energy

**Claim.** The free-kinetic-energy operator $T(\hat{p})$ is quadratic in momentum: $T(\hat{p}) \propto |\hat{p}|^2$. Linear-in-$|\hat{p}|$ terms are absent. Higher-even-power terms ($|\hat{p}|^4, |\hat{p}|^6, \ldots$) are absent in the strict non-relativistic limit.

**Status: load-bearing.** Requires translation invariance + spatial rotation invariance + parity (or time-reversal) + non-relativistic-limit scope condition + analyticity-in-$\hat{p}$ to force quadratic-leading behaviour. The argument structure exists in the prior tightening memo (transfers cleanly per §3 below) but warrants re-examination under the 2026-04-26 methodology.

### 1.4 F4 — Specific coefficient form $1/(2m)$

**Claim.** The proportionality constant in $T(\hat{p}) = c \cdot |\hat{p}|^2$ takes the specific form $c = 1/(2m)$ with $m$ a mass parameter. The kinetic energy is $T(\hat{p}) = \hbar^2 |\hat{p}|^2 / (2m)$ in standard units.

**Status: split into form-FORCED + value-INHERITED.**
- *Form FORCED.* The dimensional structure of the coefficient — inverse-twice-mass, with $\hbar^2$ supplying the dimensional bridge — is structural, derivable from dimensional analysis combined with Galilean invariance (or equivalent argument). **The factor of 2 in $1/(2m)$ specifically is the load-bearing question.**
- *Value INHERITED.* The mass $m$ itself is a per-rule-type parameter inherited per Arc M's "form FORCED, values INHERITED" methodology. The U4 arc does not attempt to derive the value of $m$.
- *Value INHERITED.* The $\hbar^2$ factor is inherited from the dimensional-atlas Madelung anchoring and from $\hbar$'s appearance in $\hat{p} = -i\hbar \nabla$ (which itself comes from Stone's theorem applied with the standard ED-program convention).

**Status: load-bearing for the form (specifically the factor of 2); inherited for $m$ and $\hbar$.**

### 1.5 F5 — Kinetic + potential decomposition

**Claim.** The Hamiltonian admits the additive decomposition $\hat{H} = T(\hat{p}) + V(\hat{x})$, with the kinetic part depending only on momentum and the potential part depending only on position. Cross terms involving products of $\hat{p}$ and $\hat{x}$ are absent in the free-particle-plus-external-potential structure.

**Status: forced-via-derivation.** Translation invariance forbids position-dependent terms in the free-particle Hamiltonian; locality of external potentials at the participation-graph level forces $V$ to depend only on $\hat{x}$. The form of $V$ itself is inherited from external physical context, not derived from primitives.

### 1.6 Status table

| Sub-feature | Status | Conditional on |
|---|---|---|
| **F1** Channel-momentum identification | forced-via-derivation | U2 (FORCED), U5 Stone's-theorem machinery |
| **F2** Plane-wave eigenfunctions | automatic given F1 | F1 |
| **F3** Quadratic-in-$k$ kinetic structure | **load-bearing** | non-relativistic-limit scope; U3 (sibling CANDIDATE, Framing 1) |
| **F4** Coefficient $1/(2m)$ form | **load-bearing for form (factor of 2); INHERITED for $m$ and $\hbar$** | non-relativistic-limit scope; Galilean invariance (TBD whether derived or inherited); U3 (Framing 1) |
| **F5** Kinetic + potential decomposition | forced-via-derivation | translation invariance (Primitive 06), locality (primitive-level external structure) |

---

## 2. Circularity Audit

Following the discipline established in U1 Memo 01 §4, we audit each sub-feature for inputs that would be circular under U4's structural-input scope.

### 2.1 Forbidden inputs (under Framing 1)

The U4 arc adopts **Framing 1**: U4 is derived *given* the existence of a Hermitian Hamiltonian generator (which is U3's content). Under this framing, the following inputs are forbidden:

- **U3 invoked as a derivation input.** Specifically, any argument that derives F3 or F4 from "the form of $\hat{H}$ in U3's evolution equation" is circular. U4's job is to *specify* the form that U3's $\hat{H}$ takes; using U3 to derive that form is question-begging.
- **The Schrödinger equation in textbook form.** Would assume U3 + U4 jointly.
- **The classical Hamiltonian $H = p^2/(2m) + V(x)$ as a postulate.** Would be assuming the answer.
- **The relativistic dispersion $E = \sqrt{p^2 c^2 + m^2 c^4}$ as a postulate.** Phase-2 Arc R derived this; using it here would conflate non-relativistic Step 2 scope with relativistic Arc R scope.

### 2.2 Permitted inputs

- Primitives 03 (homogeneity → translation symmetry), 04 (bandwidth via U1), 06 (spatial axis), 07 (channel index), 09 ($U(1)$ phase via U1).
- Now-FORCED upstream items: U1, U2-Discrete, U2-Continuum, U5, Theorem 10.
- Mathematical infrastructure: Stone's theorem, Fourier transform, functional calculus on self-adjoint operators, dimensional analysis, analyticity arguments, Galilean-invariance arguments (with the load-bearing question of where Galilean invariance comes from itself audited in §2.4 below).
- Non-relativistic-limit scope condition: a regime assumption inherited from Phase-1 Step 2's scope, not derived within U4.

### 2.3 Sub-feature-level circularity audit

For each sub-feature, we identify any candidate argument that would be circular and flag it as removable, reframable, or fatal.

**F1 — Channel-momentum identification.**
- *Candidate argument:* "The translation generator on the U2 Hilbert space exists because U3 supplies time-evolution that commutes with translations, hence translation acts unitarily."
- *Audit:* Invokes U3. **REMOVABLE.** The translation symmetry is *kinematic* (Primitives 03 + 06 supply graph homogeneity), not dynamical. Translation acts unitarily on the U2 Hilbert space because U2's inner product is preserved under measure-preserving changes of variables on the position-representation, regardless of any time-evolution rule. The U5 Memo 03 §1 derivation of Stone's theorem on translation symmetry was explicitly U3-independent and transfers directly here.
- *Status:* No fatal dependency. Use U5's machinery.

**F2 — Plane-wave eigenfunctions.**
- *Candidate argument:* none load-bearing; F2 is mathematical.
- *Status:* No circularity risk.

**F3 — Quadratic-in-$k$ kinetic energy.**
- *Candidate argument 1:* "Schrödinger's equation has $H = p^2/(2m)$, so $T \propto p^2$."
- *Audit:* Assumes U3 + U4 jointly. **FATAL** as a derivation input; the goal *is* to derive the form.
- *Candidate argument 2:* "U3 supplies a Hermitian generator $\hat{H}$ of time evolution; F3 specifies its functional form on the momentum basis."
- *Audit:* The phrasing is fine under Framing 1: U4 is derived *given* the existence of $\hat{H}$. The functional-form derivation must come from primitives + symmetry + scope, not from U3's specifics. **REFRAMABLE** as: "Given that there exists a self-adjoint Hamiltonian generator, the F3 derivation specifies its functional form via translation + rotation + analyticity + non-relativistic-limit." This is the operative framing.
- *Candidate argument 3:* "The non-relativistic-limit suppresses higher-power terms because they are $O(p^4/m^3 c^2)$ relativistic corrections."
- *Audit:* Uses the relationship between non-relativistic and relativistic dispersion. The argument is structurally sound but requires Phase-2 Arc R's relativistic dispersion as the *bound being expanded around*. **REFRAMABLE** as: the non-relativistic limit is a scope condition; within that scope, higher-order terms are suppressed.
- *Status:* Two candidate arguments require reframing (Framing 1 for U3-dependence; scope condition for non-rel limit). Neither is fatal. The substantive structural derivation transfers.

**F4 — Coefficient form $1/(2m)$.**
- *Candidate argument 1:* "From the dispersion relation $E = p^2/(2m)$ for free particles."
- *Audit:* This is what we're trying to derive. **FATAL** as a derivation input.
- *Candidate argument 2:* "Galilean invariance of the non-relativistic Hamiltonian forces the $1/(2m)$ form."
- *Audit:* The argument structure is: under Galilean boost $\hat{x} \to \hat{x} + vt$, $\hat{p} \to \hat{p} + mv$, the wavefunction transforms as $\psi \to e^{i(mvx - mv^2 t/2)/\hbar} \psi$, and the Hamiltonian must transform accordingly. The unique kinetic form satisfying Galilean covariance is $T = |\hat{p}|^2 / (2m)$ — specifically the factor of 2 in the denominator comes from the $(1/2) m v^2$ term in the boost transformation. **REFRAMABLE.** The load-bearing question is where Galilean invariance comes from — addressed in §2.4 below.
- *Candidate argument 3:* "Dimensional analysis fixes the form up to a dimensionless constant."
- *Audit:* Dimensional analysis gives $T \propto |\hat{p}|^2 / m$ (up to dimensionless factors); the specific factor of 2 is *not* fixed by dimensional analysis alone. **REFRAMABLE** but insufficient on its own — the factor of 2 needs Galilean (or equivalent) argument.
- *Status:* The factor of 2 in $1/(2m)$ is the precise load-bearing target. Dimensional analysis alone does not fix it; Galilean invariance does. Memo 03 must commit to the Galilean-invariance argument and resolve where Galilean invariance enters.

**F5 — Kinetic + potential decomposition.**
- *Candidate argument 1:* "The Hamiltonian commutes with translations in free space."
- *Audit:* Uses translation invariance, which is primitive-level. **CLEAN.**
- *Candidate argument 2:* "External potentials act locally in position representation."
- *Audit:* Locality is a primitive-level structural assumption (Primitive 03's edge-locality of participation relations). **CLEAN.**
- *Status:* No circularity risk.

### 2.4 The Galilean-invariance load-bearing question

**Where does Galilean invariance come from in the U4 derivation?** Three candidate framings, to be decided in Memo 03:

- **Framing G1 — Derive Galilean invariance from primitives.** The participation graph in the non-relativistic regime supports Galilean boosts as a consistent observer-shift symmetry: given homogeneity (Primitive 03) + isotropy (Primitive 06) + non-relativistic scope, the natural boost structure is Galilean rather than Lorentzian. This would make F4 fully forced from primitives.

- **Framing G2 — Inherit Galilean invariance from the non-relativistic-limit scope.** The non-relativistic scope condition itself implies Galilean invariance, because Galilean is what "non-relativistic" *means* at the boost-symmetry level. Under this framing, F4 is FORCED *given* the non-relativistic scope, with the scope itself being a regime choice rather than a primitive derivation.

- **Framing G3 — Replace Galilean with an alternative argument.** For example: dimensional analysis + a primitive-level energy scale $E_0$ derived from bandwidth + a structural identification of $E_0 \cdot |k|^2 / k_0^2$ as the kinetic energy with $k_0$ a primitive momentum scale. Under this framing, F4 is FORCED via the primitive-level dimensional-bridge construction without invoking Galilean directly.

**Recommendation for Memo 03:** target **Framing G1** (most ambitious; most aligned with the structural-derivation methodology). If Framing G1 fails to close cleanly within Memo 03's scope, fall back to **Framing G2** as a scope-conditional verdict.

### 2.5 Permitted-vs-forbidden summary

| Input | Status |
|---|---|
| Primitives 03, 04, 06, 07, 09 in kinematic content | Permitted |
| U1 (FORCED) | Permitted |
| U2-Discrete and U2-Continuum (FORCED) | Permitted |
| U5 (FORCED) — Stone's-theorem machinery | Permitted |
| Theorem 10 (FORCED) | Permitted |
| Standard mathematical infrastructure | Permitted |
| Non-relativistic-limit scope condition | Permitted (regime input, not derivation input) |
| Galilean invariance | TBD per §2.4 (Memo 03) |
| **U3** (sibling CANDIDATE) | **Forbidden as derivation input; permitted only as conditionality (Framing 1)** |
| The classical Hamiltonian as a postulate | Forbidden (assuming the answer) |
| The Schrödinger equation in textbook form | Forbidden (assuming the answer) |

---

## 3. Transfer Audit of the 2026-04-24 Tightening Memo

The existing tightening-program memo `arcs/arc-foundations/u4_hamiltonian_form_derivation.md` claimed structural FORCED status for the $k^2$ form and produced a SPECULATIVE chain-mass derivation. We audit each section for transferability under the 2026-04-26 methodology.

### 3.1 §2.1 Translation invariance

**Existing argument.** "The participation graph in the thin-limit continuum supports translations as a structural symmetry. No position is primitively privileged. Therefore the kinetic part of $\hat{H}$ commutes with translations, which forces it to be a function of $\hat{p}$ alone."

**Transfer status: CLEAN TRANSFER.** Translation invariance is primitive-level (Primitives 03 + 06). The argument that $\hat{H}_\mathrm{kin}$ commutes with translations and therefore depends only on $\hat{p}$ uses standard functional calculus on self-adjoint operators. No U3-dependence; transfers directly.

### 3.2 §2.2 Rotation invariance

**Existing argument.** "The participation graph supports rotations as a structural symmetry. Rotation-invariant functions of $\hat{p}$ depend only on $|\hat{p}|^2$."

**Transfer status: CLEAN TRANSFER.** Rotation invariance is primitive-level (graph isotropy from Primitive 03's homogeneity + Primitive 06's spatial-axis structure with no preferred direction). Standard argument.

### 3.3 §2.3 Analyticity and Taylor expansion

**Existing argument.** "Assume $\hat{H}_\mathrm{kin}$ is analytic in $\hat{p}^2$ at $\hat{p} = 0$. Taylor expansion: $\hat{H}_\mathrm{kin} = a_0 + a_1 \hat{p}^2 + a_2 (\hat{p}^2)^2 + \ldots$"

**Transfer status: CLEAN TRANSFER (with caveat).** Analyticity in $\hat{p}^2$ at low momentum is a *regularity* assumption — physically motivated (no singularities at zero momentum) but not strictly primitive-derived. Memo 03 should flag this as a regularity input rather than a structural derivation; it is the standard assumption in non-relativistic QM and does not introduce circularity.

### 3.4 §2.4 Non-relativistic limit

**Existing argument.** "In the strict non-relativistic limit $|\hat{p}|^2 / (mc)^2 \ll 1$, higher-order terms $a_2 (\hat{p}^2)^2$ etc. are suppressed by $(v/c)^2$ and vanish in the strict limit."

**Transfer status: CLEAN TRANSFER (regime input).** The non-relativistic limit is a scope condition, not a primitive derivation. The existing memo is honest about this: §4.3 states "The non-relativistic limit is a regime assumption, not a primitive-level consequence." Transfers directly under the new methodology with the same honest framing.

### 3.5 §2.5 Coefficient identification (the factor of 2)

**Existing argument.** "$a_1$ has dimensions of inverse mass × $c^2$. Identify $a_1 = 1/(2m_\mathrm{ED})$ for some mass-like quantity $m_\mathrm{ED}$."

**Transfer status: REQUIRES REFRAMING.** Dimensional analysis fixes $a_1 \propto 1/m$ with dimensionless prefactor. The existing memo identifies the factor of 2 by *convention* (matching classical mechanics) rather than deriving it. Under the new methodology, the factor of 2 is the load-bearing question of F4 and requires a tighter argument — most plausibly Galilean invariance (per §2.4 above). **The existing memo's silent adoption of the factor of 2 is the precise gap that Memo 03 must close.**

### 3.6 §3 Linear-in-$k$ exclusion

**Existing argument.** "Vector $\alpha \cdot \hat{p}$ excluded by rotation invariance. Scalar magnitude $|\hat{p}| c$ excluded by analyticity + non-relativistic limit (massless dispersion incompatible with massive non-relativistic regime)."

**Transfer status: CLEAN TRANSFER.** The argument uses primitive-level rotation invariance + analyticity at low momentum + non-relativistic-limit scope. No U3-dependence.

### 3.7 §4 Higher-order exclusion

**Existing argument.** "Higher-order terms suppressed by $(v/c)^2$ in the strict non-relativistic limit; vanish as $c \to \infty$."

**Transfer status: CLEAN TRANSFER (with same regime caveat as §2.4).** The regime input is honest in the existing memo; transfers cleanly.

### 3.8 §6 Chain-mass derivation (SPECULATIVE)

**Existing argument.** "First-pass primitive-level identification of $m_\mathrm{ED}$ via rule-type bandwidth or σ_τ parameter, labeled SPECULATIVE."

**Transfer status: REJECTED for U4's scope.** Under Arc M's "form FORCED, values INHERITED" methodology, the U4 arc does *not* attempt to derive the value of $m$. The mass is a per-rule-type parameter inherited from Arc M's chain-mass scoping. The §6 SPECULATIVE content is research material for a future arc (Arc M extension or new chain-mass arc), not an input to the present U4 verdict.

The U4 verdict should be: "form FORCED with $m$ inherited per Arc M; chain-mass derivation deferred."

### 3.9 §6.2 Dispersion-relation approach (uses U3)

**Existing argument.** "The plane-wave participation-measure state $P_K(x, t) = e^{i(kx - \omega t)}$ evolves under U3 with $\hat{H}_\mathrm{kin} = \hat{p}^2 / (2m)$, giving the dispersion $\omega(k) = \hbar k^2 / (2m)$."

**Transfer status: REJECTED as a derivation argument; permissible as a CONSISTENCY CHECK.** The argument explicitly invokes U3 as input. Under Framing 1, U3 cannot be a derivation input. However, the dispersion relation can be cited as a consistency check after the derivation: "Given Framing 1, U4 + U3 together produce the standard non-relativistic dispersion relation."

### 3.10 §7 Potential V(x̂)

**Existing argument.** "The form of $V(\hat{x})$ (scalar function of position) is FORCED by translation-breaking external structures. The specific $V$ for a given system is inherited from experimental context."

**Transfer status: CLEAN TRANSFER.** Maps directly to F5 of the new arc.

### 3.11 Audit summary

| Existing-memo section | Transfer status | New-arc location |
|---|---|---|
| §2.1 Translation invariance | Clean transfer | Memo 02 §3 (F5), Memo 03 §1 (F3 setup) |
| §2.2 Rotation invariance | Clean transfer | Memo 03 §1 (F3 setup) |
| §2.3 Analyticity | Clean transfer (regularity caveat) | Memo 03 §1 (F3) |
| §2.4 Non-rel limit | Clean transfer (regime input) | Memo 03 §1 (F3 + scope statement) |
| §2.5 Coefficient identification | **Requires reframing** | **Memo 03 §2 (F4) — Galilean invariance load-bearing** |
| §3 Linear-in-$k$ exclusion | Clean transfer | Memo 03 §1 (F3) |
| §4 Higher-order exclusion | Clean transfer (regime caveat) | Memo 03 §1 (F3) |
| §6 Chain-mass SPECULATIVE | Rejected for U4 scope | Inherited per Arc M; deferred |
| §6.2 Dispersion via U3 | Rejected as derivation; consistency check only | Memo 03 §3 (consistency) |
| §7 Potential V | Clean transfer | Memo 02 §3 (F5) |

The substantive sharpening for Memo 03 is **F4's factor-of-2 derivation via Galilean invariance** — the precise gap the existing memo glossed over.

---

## 4. Early Eliminations and Classification

### 4.1 Sub-features that can be classified now

**Established immediately:**
- **F2** (plane-wave eigenfunctions) — *automatic given F1*; mathematical.
- **F5** (kinetic + potential decomposition) — *forced-via-derivation*; clean transfer from §2.1 + §7 of the tightening memo. No load-bearing residual.

**Established via clean transfer + Stone's-theorem machinery from U5:**
- **F1** (channel-momentum identification) — *forced-via-derivation*; the U5 Memo 03 §1 derivation transfers directly with the channel-basis as the target rather than the position-momentum basis. Memo 02 §1 will execute the transfer explicitly.

### 4.2 Sub-features remaining for Memo 03

**Load-bearing for the structural derivation:**
- **F3** (quadratic-in-$k$ kinetic structure) — derivation chain (translation + rotation + analyticity + non-rel-limit) transfers cleanly from the tightening memo, but warrants re-statement under the 2026-04-26 methodology with the scope condition explicit and the regularity-caveat noted.
- **F4 form** (factor of 2 in $1/(2m)$) — the precise gap. Requires Galilean invariance (or equivalent argument), with the where-does-Galilean-invariance-come-from question handled in Memo 03 §2 per the framing decision (G1 / G2 / G3 from §2.4 above).

**Inherited (not derived in U4):**
- **F4 value** ($m$ specific value) — inherited per Arc M's "form FORCED, values INHERITED" methodology.
- **$\hbar$ factor** — inherited from dimensional-atlas Madelung anchoring.
- **Specific $V(\hat{x})$ for a given system** — inherited from external physical context (Memo 02 §3 will state this explicitly).

### 4.3 What remains to be proven

| Sub-feature | What Memo 02 must show | What Memo 03 must show |
|---|---|---|
| F1 | Stone's-theorem transfer from U5 to channel-basis | — |
| F2 | Mathematical consequence of F1 | — |
| F3 | — | Quadratic structure via translation + rotation + analyticity + non-rel-limit |
| F4 form | — | **Factor of 2 via Galilean invariance (Framing G1/G2/G3 commit)** |
| F4 value | — | (inherited; not derived) |
| F5 | Translation invariance + locality decomposition | — |

### 4.4 Conditionality at arc closure

Anticipated U4 arc verdict: **FORCED form, INHERITED values, CONDITIONAL on U3 (sibling CANDIDATE per Framing 1)** and (depending on Memo 03's G1/G2 commitment) potentially conditional on Galilean invariance if it cannot be derived from primitives.

If Memo 03 closes G1 (Galilean from primitives): U4 FORCED with one conditional (U3).
If Memo 03 closes G2 (Galilean from non-rel scope): U4 FORCED with two conditionals (U3 + non-rel scope's Galilean content).
If Memo 03 fails both: U4 partially FORCED with the factor-of-2 unresolved.

---

## 5. Updated Falsifier Map

The seven falsifiers from Memo 00 §4.1, recast in light of the audits above:

| Falsifier | Sub-feature | Type | Memo-01 status | Memo-2/3 dispatch path |
|---|---|---|---|---|
| **Fal-1** No momentum-basis identification | F1 | Primitive-level (translation symmetry) | **Anticipated dispatched in Memo 02** | U5 Stone's-theorem transfer |
| **Fal-2** Linear-in-$k$ kinetic term | F3 | Primitive-level (rotation + analyticity + non-rel) | Active for Memo 03 | Existing tightening §3 transfers |
| **Fal-3** Higher-even-power terms | F3 | Primitive-level (non-rel-limit scope) | Active for Memo 03 | Existing tightening §4 transfers; regime-caveat noted |
| **Fal-4** Coefficient $\neq 1/(2m)$ — wrong factor | **F4 (factor of 2)** | **Galilean invariance — load-bearing** | **Active for Memo 03; the load-bearing item** | Galilean argument per Framing G1 (target) |
| **Fal-5** Anisotropic kinetic energy | F3 | Primitive-level (rotation invariance) | Active for Memo 03 | Existing tightening §2.2 transfers |
| **Fal-6** Position-momentum cross terms | F5 | Primitive-level (translation + locality) | **Anticipated dispatched in Memo 02** | Translation invariance |
| **Fal-7** Relativistic dispersion in non-rel regime | F3 | Scope condition | Active for Memo 03 | Non-rel-limit scope; Phase-2 Arc R is the relativistic domain |

**The substantive load-bearing falsifier is Fal-4** (the factor of 2 in $1/(2m)$). The other F3-attached falsifiers (Fal-2, Fal-3, Fal-5, Fal-7) all dispatch via straightforward primitive-level + scope arguments transferring from the existing tightening memo. Fal-1 and Fal-6 dispatch in Memo 02. Memo 03's substantive derivation is the F3 quadratic-structure argument (clean transfer, low risk) plus the F4 Galilean-invariance argument (the precise sharpening gap).

---

## 6. Recommended Structure for Memo 02

Based on the audits above, Memo 02 should derive F1, F2, F5 cleanly with the load-bearing items deferred to Memo 03.

### Recommended Memo 02 structure

**Title:** `02_F1_F2_F5_derivations.md`

**§1. F1 — Channel-momentum identification.**
- Restate the claim: the channel index $K$ in the thin/continuum limit admits a continuous momentum coordinate $k$ via Stone's theorem.
- Transfer the U5 Memo 03 §1 argument: translation symmetry on the participation graph (Primitives 03 + 06, kinematic) → strongly continuous unitary translation group on the U2 Hilbert space → Stone's theorem → unique self-adjoint translation generator $\hat{p}$ → eigenstates index a momentum-basis.
- Note explicit U3-independence (the argument uses only U2's Hilbert space structure plus translation symmetry; no time-evolution or Hamiltonian generator is invoked).
- Verdict: F1 forced-via-derivation.

**§2. F2 — Plane-wave eigenfunctions.**
- Standard mathematical consequence: eigenfunctions of $\hat{p} = -i\hbar \nabla$ in the position representation are plane waves $\langle x | k \rangle = (2\pi\hbar)^{-d/2} e^{ikx/\hbar}$.
- Note: this is the basis-change between position and momentum representations on the U2 Hilbert space. It is not a new structural commitment.
- Verdict: F2 automatic given F1.

**§3. F5 — Kinetic + potential decomposition.**
- Translation invariance argument (transfer from existing tightening §2.1): a free-particle Hamiltonian commutes with translations, hence depends only on $\hat{p}$ and not on $\hat{x}$.
- Locality argument: external potentials act locally in position representation (Primitive 03's edge-locality of participation relations); $V$ depends only on $\hat{x}$, not on $\hat{p}$.
- Cross terms forbidden: $\hat{p} \hat{x}$ products would mix kinetic and potential structure, violating either translation invariance (free part) or locality (potential part).
- Note that the *form* of $V$ is structural-level forced (scalar function of $\hat{x}$); the *specific* $V$ for a given system is inherited from external physical context.
- Verdict: F5 forced-via-derivation.

**§4. Falsifier audit for F1, F2, F5.**
- Dispatch Fal-1 (no momentum-basis identification) via §1.
- Dispatch Fal-6 (position-momentum cross terms) via §3.
- Note that Fal-2 through Fal-5 and Fal-7 remain active for Memo 03.

**§5. Joint status; load-bearing items deferred to Memo 03.**
- Three sub-features established; two remain (F3, F4 form).
- Memo 03 will execute the load-bearing derivations.

**Anticipated length:** moderate. The derivations are clean transfers from established machinery (U5 Stone's theorem, existing tightening memo §2.1); no substantively new arguments. Comparable to U2 Memo 02 or U5 Memo 02.

---

## 7. Recommended Next Steps

**(a) Begin Memo 02 (F1, F2, F5 derivations).** Natural next session step. The arguments are clean transfers from established machinery; Memo 02 should be the cleaner of the two derivation memos. Expected outcome: three sub-features established with no surprises.

**(b) Pre-Memo-03 preparation: commit to the Galilean-invariance framing.** Memo 03's load-bearing question is the factor of 2 in $1/(2m)$, which requires Galilean invariance (or equivalent). The three framings (G1 derive from primitives; G2 inherit from non-rel scope; G3 alternative argument) need to be evaluated explicitly. *Recommended:* sketch the Galilean-from-primitives argument before drafting Memo 03 to test whether G1 closes; if not, fall back to G2.

The G1 sketch should attempt: (i) the participation graph in the non-relativistic regime supports observer-shift transformations; (ii) consistency of the observer-shift with translation invariance + non-relativistic-limit forces the boost-symmetry to be Galilean rather than Lorentzian; (iii) Galilean covariance of the Hamiltonian forces the kinetic-energy form $T = |\hat{p}|^2 / (2m)$ with the factor of 2 fixed by the boost-transformation algebra.

**(c) Document the form-FORCED-value-INHERITED methodology in the closure memo.** When the arc closes (Memo 04, optional), the closure should be explicit about Arc M's framing: the U4 verdict includes inherited values for $m$ and $\hbar$, with the corresponding sensitivity flags (Arc M's chain-mass status; the dimensional-atlas Madelung anchoring's $\hbar$ status). This methodological transparency is consistent with the discipline established across the prior arcs.

---

## 8. Cross-references

- Arc outline: [`arcs/U4/00_arc_outline.md`](00_arc_outline.md)
- Predecessor tightening memo (audit target): [`arcs/arc-foundations/u4_hamiltonian_form_derivation.md`](../arc-foundations/u4_hamiltonian_form_derivation.md)
- U5 Memo 03 (Stone's-theorem template for F1): [`arcs/U5/03_F3_F5_and_verdict.md`](../U5/03_F3_F5_and_verdict.md)
- U1 Memo 01 (circularity-audit template): [`arcs/U1/01_decomposition_and_mapping.md`](../U1/01_decomposition_and_mapping.md)
- U5 Memo 01 (decomposition template): [`arcs/U5/01_decomposition_and_mapping.md`](../U5/01_decomposition_and_mapping.md)
- Arc M (mass parameter inheritance): `papers/Arc_M/paper_arc_m.md`

**Source primitives:**
- Primitive 03 (Participation, supplies graph homogeneity): `quantum/primitives/03_participation.md`
- Primitive 04 (Bandwidth): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 06 (ED Gradient, supplies spatial axis): `quantum/primitives/06_ed_gradient.md`
- Primitive 09 (Tension Polarity): `quantum/primitives/09_tension_polarity.md`

---

## 9. One-line memo summary

> **U4 decomposes into five sub-features: F1 (channel-momentum identification, forced-via-derivation via Stone's-theorem transfer from U5), F2 (plane-wave eigenfunctions, automatic given F1), F3 (quadratic-in-$k$ kinetic structure, load-bearing, derivation cleanly transfers from 2026-04-24 tightening memo's §§2.1–2.4 + §3 + §4 with regime-caveat for non-relativistic-limit), F4 (coefficient $1/(2m)$, load-bearing for *form FORCED-factor-of-2 via Galilean invariance* with $m$ INHERITED per Arc M and $\hbar^2$ INHERITED from dimensional-atlas Madelung anchoring; the load-bearing question is **where Galilean invariance comes from** — three framings G1/G2/G3 to be decided in Memo 03), F5 (kinetic + potential decomposition, forced-via-derivation via translation invariance + locality). Circularity audit under Framing 1 (U4 conditional on sibling CANDIDATE U3): all candidate U3-invoking arguments are reframable as "given existence of Hermitian generator, F3 + F4 specify its functional form" with no fatal dependencies. Transfer audit of 2026-04-24 tightening memo: §§2.1–2.4 + §3 + §4 + §7 transfer cleanly; §2.5 coefficient identification *requires reframing* (silently adopted factor of 2 needs Galilean argument); §6 chain-mass content rejected for U4 scope (deferred per Arc M). Updated falsifier map: Fal-1 + Fal-6 dispatched in Memo 02; Fal-2/3/5/7 dispatched in Memo 03 via clean transfers; **Fal-4 (factor of 2 in $1/(2m)$) is the substantive load-bearing falsifier requiring Galilean argument**. Memo 02 structure: §1 F1 (Stone's-theorem transfer), §2 F2 (mathematical), §3 F5 (translation + locality), §4 falsifier dispatch for F1/F6, §5 joint status. Memo 03 will tackle F3 + F4 with Galilean-invariance commitment.**
