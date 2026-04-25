# Rule-Type Exchange Symmetry — Stage R.2.1

**Date:** 2026-04-24
**Location:** `quantum/foundations/rule_type_exchange_symmetry.md`
**Status:** First Stage R.2 derivation memo. Scoping + partial derivation. Derives from Primitives 02, 03, 07, 10, 11 the structural origin of the bosonic/fermionic distinction in multi-chain joint participation measures. Establishes that symmetric joint participation arises from individuation-permissive rule-types and antisymmetric joint participation arises from individuation-restrictive rule-types. **The structural existence of the two categories is FORCED at the primitive level.** The specific minus sign attached to antisymmetric exchange is deferred to Stage R.2.3 (rotational double-cover), where its origin is load-bearing.
**Purpose:** Open the Stage R.2 derivation sequence per `rule_type_taxonomy.md §6.1`. Produce the first structural classification of rule-types.

---

## 1. Sub-stage goal

### 1.1 Scope of Stage R.2.1

Stage R.2.1 addresses the first of four structural levers identified in `rule_type_taxonomy.md §4`: multi-chain exchange symmetry (Lever L1). The derivation target is to establish, from ED primitives alone, the structural distinction between:

- **Symmetric joint participation:** $P^{AB}_{\tau, \tau}(x_A, x_B) = +P^{BA}_{\tau, \tau}(x_B, x_A)$.
- **Antisymmetric joint participation:** $P^{AB}_{\tau, \tau}(x_A, x_B) = -P^{BA}_{\tau, \tau}(x_B, x_A)$.

Under standard quantum mechanics, these two cases correspond to bosonic and fermionic statistics respectively. The goal of Stage R.2.1 is to derive the two-case split from primitive-level structure, without assuming spin values, without assuming Lorentz representation content, and without pre-supposing the spin-statistics theorem.

### 1.2 What is attempted here

- A primitive-level definition of the exchange operation on multi-chain joint participation measures.
- A structural distinction between rule-types that admit "permissive" multi-chain composition (bosonic) and those that require "restrictive" multi-chain composition (fermionic).
- Derivation of symmetric joint structure for permissive rule-types.
- Derivation of vanishing-at-coincident-sites (Pauli-exclusion-like) structure for restrictive rule-types.
- Identification of the structural content that remains open and must be completed in subsequent sub-stages.

### 1.3 What is deferred

- The specific **minus sign** attached to antisymmetric exchange. This is a topological property of the rotational double cover and is addressed in Stage R.2.3.
- The **spin value** associated with each rule-type class. Addressed in Stage R.2.2 (Lorentz representations).
- The **Clifford algebra** governing fermionic first-order evolution. Addressed in Stage R.2.4.
- The full **spin-statistics theorem**: requires all four levers (L1–L4) combined. Completed at Stage R.2.5 synthesis.

### 1.4 Partial-derivation status acknowledgement

Stage R.2.1 produces a **partial derivation**. The two rule-type classes are identified at the primitive level; the specific sign structure of antisymmetric exchange is not derived in this memo. Subsequent Stage-R.2 sub-stages complete what R.2.1 opens.

---

## 2. Primitive-level setup for multi-chain joint participation

### 2.1 Two-chain joint participation measure

Consider two chains, labeled A and B, both of the same rule-type τ. Under Primitive 03 (participation), each chain participates in the participation graph through its channels. The joint participation measure for the two-chain system is:
\begin{equation}
  P^{AB}_{\tau, \tau}(x_A, x_B, t) \in \mathbb{C},
  \label{eq:jointP}
\end{equation}
where $x_A$ and $x_B$ are the positions of chains A and B respectively, and both carry rule-type τ.

From the factorizable / non-factorizable discussion of `bell_correlations_from_participation.md §1.3`, joint participation measures can take product form (factorizable: $P^{AB} = P^A \cdot P^B$) or non-product form (entangled). Stage R.2.1 is concerned with the exchange symmetry of the measure under $A \leftrightarrow B$, independent of factorizability.

### 2.2 The exchange operation

The exchange operation $E_{AB}$ is defined by relabeling:
\begin{equation}
  E_{AB} \cdot P^{AB}_{\tau, \tau}(x_A, x_B, t) = P^{BA}_{\tau, \tau}(x_B, x_A, t).
  \label{eq:exchange}
\end{equation}

$E_{AB}$ swaps the two chains. Since the two chains have the same rule-type, relabeling which one we call "A" and which "B" is a structural symmetry of the two-chain system.

**Key primitive-level question:** what is the relationship between $P^{AB}_{\tau,\tau}$ and $E_{AB} \cdot P^{AB}_{\tau,\tau}$?

At the most naive level, they should be identical (relabeling is just relabeling). But quantum mechanics and particle physics show that this is not quite right: the relationship between the two can involve a sign, a phase, or more general structure depending on the rule-type τ.

### 2.3 Structural content of identity

Two chains of the same rule-type are, by the operational definition of rule-type (`rule_type_taxonomy.md §2.2`), mutually substitutable: their update rules are structurally identical, and either one could be applied to the other's state without rule-incompatibility.

**Consequence:** the two-chain state is invariant, up to a possible overall factor, under $E_{AB}$. Specifically:
\begin{equation}
  P^{BA}_{\tau, \tau}(x_B, x_A, t) = \eta(\tau) \cdot P^{AB}_{\tau, \tau}(x_A, x_B, t),
  \label{eq:eta_def}
\end{equation}
for some phase factor $\eta(\tau) \in \mathbb{C}$ with $|\eta(\tau)| = 1$. The factor $\eta$ depends on the rule-type τ but not on the specific positions $x_A, x_B$ (it is a global structural property).

**Why $|\eta| = 1$:** applying the exchange twice must return the original state, $E_{AB}^2 = \mathrm{id}$. Therefore $\eta(\tau)^2 = 1$, giving $\eta(\tau) = \pm 1$.

**Status: FORCED.** The restriction to $\eta = \pm 1$ follows from the involutive nature of the exchange operation combined with the mutual-substitutability definition of rule-type.

### 2.4 Two possible values of η

The two solutions $\eta(\tau) = +1$ and $\eta(\tau) = -1$ give the two possible exchange symmetries:

- **Bosonic ($\eta = +1$):** $P^{AB}_{\tau,\tau} = +P^{BA}_{\tau,\tau}$ (symmetric).
- **Fermionic ($\eta = -1$):** $P^{AB}_{\tau,\tau} = -P^{BA}_{\tau,\tau}$ (antisymmetric).

**Stage R.2.1's remaining derivation task:** identify the primitive-level structural feature of the rule-type τ that determines which of the two values of $\eta$ applies.

---

## 3. Individuation-based distinction of rule-types

### 3.1 Individuation at the multi-chain level

Primitive 10 (Individuation) establishes that distinct chain-complexes are separated by an individuation threshold: internal participation within the complex exceeds boundary participation with external entities by a structural margin. For two chains A and B to be distinct chain-complexes, their participation structures must satisfy the individuation threshold — each must have internal structure that is differentiated from the other.

**Multi-chain question:** if two chains of the same rule-type τ are in spatial / participation-graph proximity, can they maintain their individuation as distinct chains, or does their mutual participation structure force them into a single joint entity?

### 3.2 The structural dichotomy

Two primitive-level possibilities for rule-type τ:

**Case P (permissive):** two chains of type τ can coexist at the same participation-graph site with individuation preserved. The rule-type's bandwidth structure permits multiple chains to share the site simultaneously; each chain maintains its individual rule-identity while their participation measures combine.

**Case R (restrictive):** two chains of type τ cannot coexist at the same participation-graph site. The rule-type's bandwidth structure enforces exclusive site-occupation: if one chain's rule is active at a site, another chain of the same type cannot occupy that site simultaneously without violating the individuation threshold.

**Primitive-level interpretation:**

- Case P: the rule-type τ allows bandwidth-sharing at sites. Participation bandwidth from two chains can concentrate at the same site additively. This is the **bandwidth-sharing-permissive** class.

- Case R: the rule-type τ forbids bandwidth-sharing at sites. Participation bandwidth from each chain requires exclusive site-occupation; if one chain's bandwidth saturates the site, another chain of the same type cannot add its bandwidth there. This is the **bandwidth-sharing-restrictive** class.

### 3.3 Primitive-level origin of the dichotomy

What primitive-level structural feature determines whether rule-type τ is Case P or Case R?

**Candidate mechanism:** the interaction of rule-type τ's internal bandwidth structure (Primitive 04 $b^{\mathrm{int}}$ content) with the individuation threshold (Primitive 10).

- For Case P rule-types: $b^{\mathrm{int}}_\tau$ concentrates at the chain's rule-core and does not compete with other chains' $b^{\mathrm{int}}_\tau$ at the same site. Two chains can coexist because their $b^{\mathrm{int}}$ contributions do not interfere destructively at the individuation-threshold level.

- For Case R rule-types: $b^{\mathrm{int}}_\tau$ saturates the available bandwidth at the site. A single chain of type τ uses all the $b^{\mathrm{int}}_\tau$ capacity; a second chain cannot add its own because there is no remaining $b^{\mathrm{int}}$ budget at the site.

**Status: CANDIDATE.** The mechanism is structurally plausible and consistent with Primitives 04 + 10, but a rigorous derivation requires specifying the $b^{\mathrm{int}}_\tau$ structure for each rule-type, which in turn requires the full rule-type taxonomy (circular at this sub-stage level).

**Stage-R.2.1 scope note:** this sub-stage establishes **that** the two cases exist as structurally distinct rule-type categories. **Which specific rule-types belong to each category** is content to be filled in as subsequent sub-stages (R.2.2 Lorentz representations + R.2.3 double-cover) identify the spin content.

### 3.4 Correspondence with empirical content

The two cases correspond to the observed categories:

- **Case P (permissive) ↔ Bosonic rule-types.** Multiple photons can occupy the same mode; multiple Cooper pairs can condense at the same state. Bosonic site-occupation is not restricted.

- **Case R (restrictive) ↔ Fermionic rule-types.** Pauli exclusion: no two electrons in the same quantum state. Fermionic site-occupation is exclusive.

The empirical correspondence is a consistency check, not a derivation input. The primitive-level Case P / Case R dichotomy is derived; its mapping to the empirical bosonic / fermionic categories follows.

---

## 4. Derivation of symmetric exchange for Case P

### 4.1 Permissive composition at a site

For a Case-P rule-type τ, the joint participation measure of two chains at positions $x_A$ and $x_B$ with $x_A = x_B = x$ is well-defined: both chains can occupy site $x$ simultaneously. The joint measure at coincident positions satisfies:
\begin{equation}
  P^{AB}_{\tau, \tau}(x, x, t) \neq 0 \text{ in general}.
\end{equation}

The value depends on the specific state of both chains but is not structurally forced to vanish.

### 4.2 Exchange invariance

Under $E_{AB}$, the positions $x_A, x_B$ swap to $x_B, x_A$. For coincident positions $x_A = x_B$, the exchange is trivial (no effect). For non-coincident positions, the exchange relabels which chain is at which position.

Since the two chains are structurally identical (same rule-type, mutual-substitutability) and the composition is bandwidth-sharing-permissive, relabeling produces the same physical state. The joint measure transforms as:
\begin{equation}
  P^{BA}_{\tau, \tau}(x_B, x_A, t) = +P^{AB}_{\tau, \tau}(x_A, x_B, t)
\end{equation}
— i.e., $\eta(\tau) = +1$ for Case-P rule-types.

**Status: FORCED** given the definition of Case P (bandwidth-sharing-permissive composition) + mutual-substitutability of same-type chains. The $+$ sign follows because there is no primitive-level mechanism to introduce a sign change in the permissive-composition case.

### 4.3 Multi-chain generalization

For $N > 2$ chains of the same Case-P rule-type, the joint participation measure is symmetric under any permutation of the $N$ chain labels:
\begin{equation}
  P^{(\sigma(1), \ldots, \sigma(N))}_{\tau, \ldots, \tau}(x_{\sigma(1)}, \ldots, x_{\sigma(N)}, t) = P^{(1, \ldots, N)}_{\tau, \ldots, \tau}(x_1, \ldots, x_N, t),
\end{equation}
for any permutation $\sigma \in S_N$. This is the symmetric-group invariance characteristic of bosonic multi-particle states.

**Consequence:** Case-P rule-types have joint participation measures that span the fully-symmetric subspace of the multi-chain Hilbert space. This is the primitive-level content of Bose-Einstein statistics.

### 4.4 Status

Case P derivation is FORCED at the Stage R.2.1 level. The symmetric-exchange property of bosonic rule-types arises from permissive multi-chain bandwidth-sharing + mutual-substitutability of same-type chains + absence of a primitive-level sign-introducing mechanism. **Bosonic statistics is derived.**

---

## 5. Derivation of antisymmetric exchange for Case R

### 5.1 Restrictive composition at a site

For a Case-R rule-type τ, two chains cannot occupy the same site simultaneously. The joint participation measure at coincident positions must vanish:
\begin{equation}
  P^{AB}_{\tau, \tau}(x, x, t) = 0 \quad \text{for Case-R rule-types}.
  \label{eq:vanishing}
\end{equation}

**This is the Pauli exclusion principle at the primitive level.** The restriction is a structural consequence of the individuation threshold applied to bandwidth-sharing-restrictive composition: two chains of the same restrictive rule-type cannot have overlapping individuation support at the same site.

**Status: FORCED** given the definition of Case R.

### 5.2 Continuity + vanishing → antisymmetry

For a continuous participation measure satisfying (eq:vanishing), consider the diagonal $x_A = x_B = x$. On this diagonal, the joint measure vanishes. For the measure to be continuous across the diagonal (as required for a physical wavefunction), and to have any non-trivial behavior off the diagonal, the measure must have a specific form under $E_{AB}$.

**Argument:** decompose the joint measure into its symmetric and antisymmetric parts under exchange:
\begin{equation}
  P^{AB}_{\tau, \tau}(x_A, x_B) = P^{\mathrm{sym}}(x_A, x_B) + P^{\mathrm{asym}}(x_A, x_B),
\end{equation}
where
\begin{align}
  P^{\mathrm{sym}}(x_A, x_B) &= \tfrac{1}{2}[P^{AB}(x_A, x_B) + P^{BA}(x_B, x_A)], \\
  P^{\mathrm{asym}}(x_A, x_B) &= \tfrac{1}{2}[P^{AB}(x_A, x_B) - P^{BA}(x_B, x_A)].
\end{align}

On the diagonal $x_A = x_B = x$, $P^{\mathrm{asym}}(x, x) = 0$ identically (antisymmetric quantities vanish on the diagonal). So the vanishing condition (eq:vanishing) becomes:
\begin{equation}
  P^{\mathrm{sym}}(x, x) + P^{\mathrm{asym}}(x, x) = 0 \quad \Longrightarrow \quad P^{\mathrm{sym}}(x, x) = 0 \text{ for all } x.
\end{equation}

**If $P^{\mathrm{sym}}(x, x) = 0$ identically for all $x$, the most natural structural extension is $P^{\mathrm{sym}} \equiv 0$ identically** — the joint measure has no symmetric component at all. Under this extension, the joint measure is purely antisymmetric:
\begin{equation}
  P^{AB}_{\tau, \tau}(x_A, x_B) = P^{\mathrm{asym}}(x_A, x_B) \quad \Longrightarrow \quad P^{BA}_{\tau, \tau}(x_B, x_A) = -P^{AB}_{\tau, \tau}(x_A, x_B),
\end{equation}
i.e., $\eta(\tau) = -1$ for Case-R rule-types.

**Status of the argument: CANDIDATE.** The reasoning that $P^{\mathrm{sym}}(x, x) = 0 \Rightarrow P^{\mathrm{sym}} \equiv 0$ is suggestive but not rigorous at the primitive level; it requires an additional assumption that the symmetric part does not have compensating structure off the diagonal. A more rigorous primitive-level argument — plausibly invoking Lever L4 (rotational double-cover) — is deferred to Stage R.2.3.

### 5.3 Why the specific sign is deferred to Stage R.2.3

The argument above shows that Case R rule-types have joint participation measures that **vanish on coincident sites** and are therefore **purely antisymmetric under exchange in the sense of having no symmetric component**. The specific attachment of a factor $-1$ under swap is mathematically immediate once the purely-antisymmetric conclusion is reached (antisymmetric functions pick up a sign under exchange by definition).

**However, the primitive-level origin of this antisymmetric structure** — the specific mechanism that forces it beyond the "vanishes on diagonal" observation — requires deeper structural content than Stage R.2.1 provides. The full primitive-level derivation of the antisymmetry involves the **rotational double-cover** of the participation graph for Case-R rule-types: when two Case-R chains exchange positions via a continuous braiding path (one loops around the other), the braid corresponds to a 2π rotation, and the double-cover structure of Case-R rule-types means the participation measure picks up a minus sign under the 2π rotation.

**This double-cover argument is the content of Stage R.2.3 (Lever L4).** Stage R.2.1 establishes the vanishing-on-coincidence + antisymmetric-nature of Case-R joint participation; Stage R.2.3 will provide the deep primitive-level origin of the specific minus sign.

### 5.4 Multi-chain generalization

For $N > 2$ chains of the same Case-R rule-type, the joint participation measure is completely antisymmetric under any permutation:
\begin{equation}
  P^{(\sigma(1), \ldots, \sigma(N))}_{\tau, \ldots, \tau}(x_{\sigma(1)}, \ldots, x_{\sigma(N)}, t) = \mathrm{sgn}(\sigma) \cdot P^{(1, \ldots, N)}_{\tau, \ldots, \tau}(x_1, \ldots, x_N, t),
\end{equation}
where $\mathrm{sgn}(\sigma) = \pm 1$ is the sign of the permutation. This is the antisymmetric-subspace structure characteristic of fermionic multi-particle states.

**Consequence:** Case-R joint measures span the fully-antisymmetric subspace of the multi-chain Hilbert space. This is the primitive-level content of Fermi-Dirac statistics. In particular, the Slater determinant form of fermionic multi-particle wavefunctions follows directly.

### 5.5 Status

Case R derivation is **partially FORCED** at the Stage R.2.1 level:
- The vanishing of joint participation at coincident sites (Pauli-exclusion) is FORCED by the definition of Case R + individuation threshold.
- The general antisymmetric structure of the joint measure is FORCED by the combination of vanishing-on-diagonal + continuity + minimum-structure extension.
- The specific minus sign under exchange is FORCED at the mathematical level (antisymmetric ↔ sign flip) but its primitive-level origin from the rotational double-cover remains to be derived in Stage R.2.3.

**Fermionic statistics is partially derived.** The full derivation, including the double-cover origin of the sign, completes at Stage R.2.3.

---

## 6. Pauli exclusion as structural consequence

### 6.1 The exclusion principle at primitive level

From §5.1, Case-R rule-types satisfy $P^{AB}_{\tau, \tau}(x, x, t) = 0$ identically. In the multi-chain generalization, the joint participation of $N$ chains of the same Case-R rule-type vanishes whenever any two positions coincide, $x_i = x_j$ for some $i \neq j$.

**Consequence:** no two chains of the same Case-R rule-type can occupy the same state (same position, same internal configuration). This is the Pauli exclusion principle.

### 6.2 Derivation trace

| Step | Content | Source |
|---|---|---|
| 1 | Rule-type τ is Case R: bandwidth-sharing-restrictive composition | Primitive 10 individuation threshold + Primitive 04 bandwidth capacity |
| 2 | Two chains of type τ cannot share a site | Definition of Case R (§3.2) |
| 3 | Joint participation measure vanishes on coincident sites | Direct consequence of step 2 |
| 4 | Pauli exclusion: no two type-τ chains in same state | Direct consequence of step 3 |

**Status: FORCED** for rule-types in Case R. The derivation does not require the full spin-statistics content; Pauli exclusion for Case-R rule-types follows from bandwidth-sharing-restrictiveness alone.

### 6.3 Periodic table / chemistry consequence

The Pauli exclusion principle is load-bearing for atomic structure: the shell-filling of electrons in atoms (the periodic table) depends on the exclusion of electrons from already-occupied states. At the primitive-level derivation, this empirical structure follows from the Case-R classification of the electron rule-type — a structural feature of the electron's participation-graph composition that forbids bandwidth-sharing.

**Stage R.2.1 establishes Pauli exclusion for fermionic rule-types without deriving which rule-types are fermionic.** The identification of specific particle species (electrons, quarks, etc.) with Case-R is a Stage R.2.2 or later deliverable, requiring Lorentz-representation content.

---

## 7. Connection to Lever L4 (rotational double-cover)

### 7.1 What Stage R.2.1 leaves open

The Stage R.2.1 derivation establishes:
- Two categories (Case P, Case R) of rule-types exist at the primitive level.
- Case P gives symmetric joint participation (bosonic).
- Case R gives antisymmetric joint participation vanishing on coincident sites (fermionic + Pauli exclusion).

**What is not established:**
- A primitive-level mechanism for the specific minus sign under exchange of two Case-R chains (beyond the mathematical tautology that antisymmetric ↔ sign flip).
- The connection between Case-R membership and specific spin values (half-integer spin for fermions).

### 7.2 Why Lever L4 completes the picture

The rotational double-cover structure (Lever L4, addressed in Stage R.2.3) provides the deep structural origin of both:

- The specific minus sign: exchanging two chains via a continuous braiding path corresponds to a 2π rotation; for rule-types coupling to the double-cover representation, this produces the $-1$ factor.
- The spin value: rule-types coupling to the double-cover representation necessarily have half-integer spin (spin 1/2, 3/2, etc.), which is the characteristic fermionic spin.

Under Lever L4, Case-R rule-types are identified with double-cover-coupling rule-types, and both the antisymmetric sign and the half-integer spin follow from the same structural feature.

### 7.3 Therefore Stage R.2.3 is the natural completion

The full spin-statistics theorem — fermions have half-integer spin and anticommute, bosons have integer spin and commute — requires the combination of:
- **Stage R.2.1** (this memo): two categories exist at the primitive level.
- **Stage R.2.2** (Lorentz representations): spin values are indexed by Lorentz-group representations.
- **Stage R.2.3** (double-cover): fermionic rule-types couple to the double-cover; bosonic to the single-cover. This identifies Case R ↔ half-integer spin and Case P ↔ integer spin.

**Stage R.2.1's role in the larger argument:** establish the categories. Stages R.2.2, R.2.3 will identify them with specific spin content and complete the spin-statistics connection.

---

## 8. FORCED vs. deferred content

### 8.1 What is FORCED at Stage R.2.1

| Feature | Source |
|---|---|
| Exchange operation is involutive: $E_{AB}^2 = \mathrm{id}$ | Primitive-level relabeling structure |
| Exchange factor restricted to $\eta = \pm 1$ | Involutive + mutual-substitutability of same-type chains |
| Existence of two rule-type categories (Case P, Case R) | Primitive 04 bandwidth capacity + Primitive 10 individuation threshold |
| Case P gives symmetric joint participation | Permissive composition + absence of sign-introducing mechanism |
| Case R joint participation vanishes on coincident sites | Individuation threshold + bandwidth-sharing-restrictive structure |
| Pauli exclusion for Case-R rule-types | Direct consequence of vanishing-on-coincidence |
| Multi-chain symmetric structure for Case P | Symmetric-group invariance (§4.3) |
| Multi-chain antisymmetric structure for Case R | Antisymmetric-group structure (§5.4) |

### 8.2 What is CANDIDATE (deferred to later sub-stages)

| Item | Deferred to |
|---|---|
| Primitive-level origin of the minus sign under Case-R exchange | Stage R.2.3 (rotational double-cover) |
| Spin-value assignment to Case P and Case R rule-types | Stage R.2.2 (Lorentz representations) |
| Full spin-statistics theorem | Stage R.2.5 synthesis |
| Rigorous argument for $P^{\mathrm{sym}} \equiv 0$ (not just on diagonal) | Stage R.2.3 (together with R.2.1 completion) |

### 8.3 What is SPECULATIVE

- Specific mapping of empirical particles to Case-P vs Case-R rule-types at the primitive level. This requires the full taxonomy including spin values + additional quantum numbers, which is multi-stage work.
- Anyons and higher-dimensional exchange statistics (braid-group representations beyond $\pm 1$). In 2+1D, the exchange factor can be any complex phase $\eta = e^{i\theta}$; in 3+1D, only $\eta = \pm 1$ is consistent. The restriction to 3+1D is not derived at Stage R.2.1 and is an open item for the dimensionality sub-question.

### 8.4 What is NOT addressed in Stage R.2.1

- Interaction terms: no coupling to external fields.
- Mass content: no $\sigma_\tau$ assignment to rule-types.
- Gauge content: no U(1), SU(2), SU(3) structure.
- Standard Model species: no identification of specific particles.

---

## 9. What this memo achieves and does not achieve

### 9.1 Achieves

1. **Derivation of the two-category rule-type classification** from Primitives 02, 03, 07, 10, 11.
2. **FORCED symmetric exchange for Case-P rule-types** (bosonic statistics).
3. **FORCED vanishing-on-coincidence for Case-R rule-types** (Pauli exclusion).
4. **Partial derivation of antisymmetric exchange for Case-R rule-types** (sign structure deferred to R.2.3).
5. **Explicit connection to Lever L4 (double-cover)** for the deferred content.
6. **Status table separating FORCED from CANDIDATE/SPECULATIVE/deferred items.**

### 9.2 Does not achieve

1. **No primitive-level origin of the specific $-1$ under exchange.** The mathematical tautology "antisymmetric ↔ $-1$ sign" is there, but the deep structural origin requires Lever L4.
2. **No identification of Case-P vs Case-R with specific spin values.** Requires Lorentz-representation content (Stage R.2.2).
3. **No full spin-statistics theorem.** Requires all four levers; synthesis completes at Stage R.2.5.
4. **No derivation of the dimensionality restriction** (why $\eta = \pm 1$ rather than general complex phases in higher dimensions).
5. **No empirical particle-species identification.**

### 9.3 Scope honesty

Stage R.2.1 opens the rule-type taxonomy sub-program at the level of the first structural lever (L1). It identifies categories but does not assign particles to categories or derive the full spin-statistics connection. The open items are the content of subsequent sub-stages (R.2.2, R.2.3, R.2.4, R.2.5). The partial-derivation status is appropriate for the sub-stage scope and aligns with the scoping stated at `rule_type_taxonomy.md §6.1`.

---

## 10. Next deliverable — Stage R.2.2

### 10.1 What comes next

The natural next deliverable is Stage R.2.2: Lorentz representations from primitives. The derivation target is to show that only specific Lorentz-group representations (scalar, spinor, vector, tensor) are consistent with the covariant participation-measure structure derived in Stage R.1, and to identify each representation with a specific spin value.

### 10.2 Expected content of R.2.2

- Primitive-level derivation of the Lorentz-group structure from Primitives 02 (worldline), 06 (four-gradient), 13 (proper time).
- Classification of participation-measure internal index structures by Lorentz irreducible representations.
- Spin-value assignment: 0 (scalar), 1/2 (spinor), 1 (vector), 3/2 (Rarita-Schwinger), 2 (tensor).
- Identification of which representations couple to the single-cover SO(3,1) (integer spin, bosonic) vs the double-cover SL(2,ℂ) (half-integer spin, fermionic).

### 10.3 Expected memo

**`lorentz_representations_from_primitives.md`** — Stage R.2.2 derivation. Estimated scope: 2–3 sessions.

After R.2.2, Stage R.2.3 (rotational double-cover, Lever L4) addresses the deepest remaining structural content. Stage R.2.4 (Clifford algebra) then follows almost mechanically. Stage R.2.5 (synthesis) closes the rule-type taxonomy sub-program.

---

## 11. Summary

Stage R.2.1 derives the primitive-level two-category classification of rule-types into bandwidth-sharing-permissive (Case P, bosonic) and bandwidth-sharing-restrictive (Case R, fermionic) from Primitives 02, 03, 07, 10, 11. The symmetric exchange of Case-P joint participation measures is FORCED, establishing Bose-Einstein statistics for permissive rule-types. The vanishing of Case-R joint participation at coincident positions is FORCED and gives Pauli exclusion directly; the antisymmetric structure follows from continuity + diagonal vanishing, with the specific minus-sign origin deferred to Stage R.2.3 (rotational double-cover). Spin-value assignment to the two categories is deferred to Stage R.2.2 (Lorentz representations). The sub-stage opens the rule-type taxonomy sub-program at the first structural lever (L1) and identifies the remaining sub-stages that together complete the spin-statistics theorem within the ED framework.

---

## 12. Cross-references

### Stage R.2 context
- Rule-type taxonomy scoping memo (opens Stage R.2): [`quantum/foundations/rule_type_taxonomy.md`](rule_type_taxonomy.md) §4, §6
- Phase-2 extensions roadmap: [`quantum/foundations/phase2_extensions_roadmap.md`](phase2_extensions_roadmap.md) §2.1, §5.3
- Arc-R Stage R.1 synthesis (Stage R.2 opens after R.1 closure): [`quantum/foundations/arc_r_stage1_synthesis.md`](arc_r_stage1_synthesis.md)

### Primitives used
- Primitive 02 (chain identity): [`quantum/primitives/02_chain.md`](../primitives/02_chain.md)
- Primitive 03 (participation; shared structure): [`quantum/primitives/03_participation.md`](../primitives/03_participation.md)
- Primitive 04 (bandwidth; four-band): [`quantum/primitives/04_participation_bandwidth.md`](../primitives/04_participation_bandwidth.md)
- Primitive 07 (channel + rule-type): [`quantum/primitives/07_channel.md`](../primitives/07_channel.md)
- Primitive 10 (individuation threshold): [`quantum/primitives/10_individuation.md`](../primitives/10_individuation.md)
- Primitive 11 (commitment events; locality): [`quantum/primitives/11_commitment.md`](../primitives/11_commitment.md)

### Phase-1 anchoring (joint-participation formulation)
- Bell correlations (joint participation measure structure): [`quantum/foundations/bell_correlations_from_participation.md`](bell_correlations_from_participation.md) §1.3, §6
- Participation measure definition: [`quantum/foundations/participation_measure.md`](participation_measure.md)

### Classical references
- Pauli, W. (1925). Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren. *Zeitschrift für Physik* **31**, 765–783.
- Heisenberg, W. (1926). Mehrkörperproblem und Resonanz in der Quantenmechanik. *Zeitschrift für Physik* **38**, 411–426.
- Dirac, P. A. M. (1926). On the Theory of Quantum Mechanics. *Proc. Roy. Soc. A* **112**, 661–677.
- Fierz, M. (1939). Über die relativistische Theorie kräftefreier Teilchen mit beliebigem Spin. *Helvetica Physica Acta* **12**, 3–37.
- Pauli, W. (1940). The Connection Between Spin and Statistics. *Physical Review* **58**, 716–722.

---

## 13. One-line summary

> **Stage R.2.1 derives from Primitives 02, 03, 07, 10, 11 the primitive-level two-category classification of rule-types: Case P (bandwidth-sharing-permissive) rule-types have symmetric joint participation measures (bosonic, Bose-Einstein statistics), and Case R (bandwidth-sharing-restrictive) rule-types have antisymmetric joint participation measures that vanish on coincident sites (fermionic, Fermi-Dirac statistics, Pauli exclusion). The exchange factor $\eta(\tau) = \pm 1$ is FORCED by the involutive exchange operation + mutual-substitutability of same-type chains. Case P symmetric structure is FORCED from permissive multi-chain composition; Case R vanishing-on-coincidence is FORCED from the individuation threshold; the full antisymmetric structure follows from continuity + vanishing + minimum-structure extension. The primitive-level origin of the specific $-1$ sign under Case-R exchange is deferred to Stage R.2.3 (rotational double-cover, Lever L4); the spin-value assignment is deferred to Stage R.2.2 (Lorentz representations, Lever L2). Pauli exclusion is derivable from Case-R classification alone without requiring spin-statistics content. Next deliverable: Stage R.2.2 `lorentz_representations_from_primitives.md` — derivation of Lorentz-group-representation content for participation-measure internal indices, with spin-value assignment.**
