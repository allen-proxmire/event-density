# Rule-Type Taxonomy — Stage R.2 Opening Scoping Memo

**Date:** 2026-04-24
**Location:** `quantum/foundations/rule_type_taxonomy.md`
**Status:** Stage R.2 opening scoping memo. Defines the rule-type taxonomy problem as the derivation of chain rule-type classification from ED primitives. Identifies candidate structural levers for the bosonic/fermionic distinction, outlines the derivation path toward spinor index structure and Clifford algebra, and maps the sub-program's scope. **The memo is scoping only; no classification is derived. Full derivation is multi-session frontier research.** Rule-type taxonomy is the critical shared prerequisite for Arc R Stage R.3 (Dirac) and Arc M (chain-mass); closing this sub-program unlocks both arcs.
**Purpose:** Open Stage R.2 of Arc R per `arc_r_stage1_synthesis.md §5` and `phase2_extensions_roadmap.md §5.3`. Provide the structural scaffold on which subsequent Stage-R.2 derivation memos will build.

---

## 1. Problem statement

### 1.1 Where the taxonomy gap lies

Primitive 07 (Channel) introduces the concept of a rule-type τ as a label indexing "the kind of chain rule" — the structural classification of chains by the type of update rule they carry. Primitive 07 §1 treats rule-type as a discrete label drawn from a finite (structurally-determined) set. Primitive 07 §7.4 flags this as an open item: *"Rule-type taxonomy — what is the complete structural classification of channel-compatible rule-types? This is the ED analog of the particle-species inventory. Bottom-up: derive from participation-graph structure. Not yet done."*

At the primitive level, the ED framework specifies that rule-types exist and that they index a discrete classification, but does not derive which specific rule-types are structurally permitted or what structurally distinguishes one rule-type from another. **Stage R.2's purpose is to close that gap.**

### 1.2 Why it matters

Two Phase-2 arcs block on the rule-type taxonomy:

- **Arc R Stage R.3 (Dirac emergence):** the Dirac equation describes fermionic chains with spinor-valued participation measures. Without a primitive-level rule-type classification that distinguishes fermions from bosons, Dirac cannot be derived from ED structure.

- **Arc M (Chain-mass derivation):** the candidate identification `m_τ = σ_τ / c²` assigns mass to each rule-type τ via a rule-type-specific bandwidth signature σ_τ. Without a classification specifying what τ can be, the mass spectrum cannot be derived.

Additionally, Arc Q (QFT extension) ultimately depends on the rule-type taxonomy for its species content, so Stage R.2 is a prerequisite for multiple long-term arcs.

### 1.3 What this memo does

This memo is scoping-level. It:

- Defines what a rule-type is at the primitive level (§2).
- Catalogs the observed rule-type content in standard physics that a complete taxonomy must reproduce (§3).
- Identifies four candidate structural levers for the bosonic/fermionic distinction (§4).
- Scopes the spin-statistics-theorem content (§5).
- Outlines a multi-stage derivation path (§6).
- Lists FORCED vs. open items honestly (§7).
- Maps the relationship to Arc M (§8).

**It does not derive the taxonomy.** All candidate structural levers are labeled SPECULATIVE until a dedicated derivation memo promotes them. The memo's purpose is to make the sub-program tractable, not to solve it.

---

## 2. What a rule-type is at the primitive level

### 2.1 Primitive 02 + 07 content

From Primitive 02 (Chain): a chain is a sequence of micro-events held together by a consistent update rule. The update rule specifies how the chain's next micro-event follows from its current state. Primitive 02 does not classify chains; it establishes the concept of an update rule.

From Primitive 07 (Channel): a channel is a stable rule-type-selective pathway through the participation graph. Channels support chains with rule-types compatible with the channel's structure. A rule-type is therefore a classification of update rules by which channel structures they can traverse.

### 2.2 Operational definition

A **rule-type** τ is a primitive-level structural label such that two chains share the same rule-type if and only if their update rules are mutually interchangeable — one chain's rule can be applied to another chain's state without rule-incompatibility.

**Equivalently:** rule-types are equivalence classes of update rules under the relation of mutual-substitutability. Chains of the same rule-type follow the same structural update law; chains of different rule-types follow different laws.

### 2.3 What rule-type does NOT specify

- The specific value of the chain's internal state at any moment (that is chain-history, not rule-type).
- The chain's current position in the participation graph (that is state, not rule-type).
- The chain's accumulated commitment history (that is chain-aging, not rule-type).

Rule-type is the invariant structural property of the update rule itself, independent of the chain's history and current state.

### 2.4 What rule-type does specify

Rule-type should specify:

- The **internal index structure** of the participation measure $P_{K, \alpha}(x^\mu)$ for that rule-type (scalar, spinor, vector, tensor, etc.).
- The **spin** of the chain (integer or half-integer value).
- The **statistics** (bosonic or fermionic) under multi-chain exchange.
- The **intrinsic quantum numbers** (charge, baryon number, lepton number, flavor, color — for the various conservation laws).
- The **mass** of the chain (via the chain-mass derivation in Arc M, using the rule-type bandwidth signature σ_τ).

All of these should be structural consequences of the rule-type classification, derivable from primitive-level properties of the update rule.

---

## 3. Rule-type content that must be reproduced

The complete taxonomy must reproduce the empirically observed rule-type content of elementary particle physics. A scoping memo should catalog what that content is.

### 3.1 Elementary particle rule-types (Standard Model)

**Fermions (half-integer spin, Fermi-Dirac statistics):**

- **Quarks** (spin 1/2, three color charges, six flavors: up, down, charm, strange, top, bottom).
- **Leptons** (spin 1/2, electric charge, three generations):
  - Charged leptons: electron, muon, tau.
  - Neutral leptons (neutrinos): electron-neutrino, muon-neutrino, tau-neutrino.

**Bosons (integer spin, Bose-Einstein statistics):**

- **Gauge bosons** (spin 1, mediate interactions):
  - Photon (electromagnetism, massless).
  - W⁺, W⁻, Z⁰ (weak interaction, massive).
  - Gluon (strong interaction, eight colors, massless).
- **Higgs boson** (spin 0, scalar, massive; responsible for electroweak symmetry breaking).
- **(Hypothetical) graviton** (spin 2, mediates gravity).

**Composite particles** (mesons, baryons, atoms, nuclei) are built from the above elementary rule-types via participation-graph composition. The taxonomy must also support this composition structurally.

### 3.2 Structural features to reproduce

- **Discreteness** — only specific rule-types exist; the spectrum is discrete.
- **Spin values** — integer or half-integer; the range is restricted.
- **Internal symmetries** — gauge groups U(1) × SU(2) × SU(3) for the Standard Model.
- **Generations** — three generations of fermions with increasing mass.
- **Mass ratios** — m_e : m_μ : m_τ ≈ 1 : 207 : 3477, m_e : m_p ≈ 1 : 1836, etc.
- **Conservation laws** — electric charge, baryon number, lepton number, etc.

A complete taxonomy must derive each of these from ED primitive-level structure. Arc M (chain-mass) is specifically the derivation of the mass ratios; the rest of the rule-type content falls in Stage R.2.

### 3.3 Scope honesty

**Stage R.2 is not expected to derive the entire Standard Model from primitives.** A realistic near-term target is:

- Structural distinction between bosonic and fermionic chains.
- Derivation of the spin-statistics connection.
- Derivation of the spinor index structure for fermions.
- Derivation of the Clifford algebra for spinor chains.

These four targets unlock Dirac (Stage R.3) and provide the framework on which the full Standard Model content can be built via Arc Q (QFT extension) and Arc M (chain-mass) in multi-year subsequent work.

**The Standard Model's species content, gauge-group structure, and mass spectrum are long-term frontier targets, not Stage R.2 deliverables.**

---

## 4. Candidate structural levers for the bosonic/fermionic distinction

Four candidate primitive-level structural properties could distinguish fermionic from bosonic chains. Each is SPECULATIVE at the scoping level; closing the taxonomy sub-program requires selecting or deriving one (or a combination) as the structural commitment.

### 4.1 Candidate L1 — Exchange symmetry of the joint participation measure

**Proposal.** For two chains of the same rule-type τ, the joint participation measure $P^{AB}_{\tau, \tau}(x_A, x_B)$ has specific symmetry under exchange $A \leftrightarrow B$:

- **Bosonic rule-types:** $P^{AB}_{\tau,\tau}(x_A, x_B) = +P^{BA}_{\tau,\tau}(x_B, x_A)$ (symmetric).
- **Fermionic rule-types:** $P^{AB}_{\tau,\tau}(x_A, x_B) = -P^{BA}_{\tau,\tau}(x_B, x_A)$ (antisymmetric).

The distinction is a primitive-level structural property of the rule-type itself: whether the rule supports symmetric or antisymmetric multi-chain composition under exchange.

**Implications.**
- Pauli exclusion follows for fermions: antisymmetric wavefunctions vanish when two chains occupy the same state.
- Bose-Einstein statistics follows for bosons: symmetric joint participation permits multiple chains in the same state.

**Status: CANDIDATE.** The proposal gives a clean primitive-level bosonic/fermionic distinction but does not by itself derive spin values or the Clifford algebra. It is consistent with standard QFT's spin-statistics result but requires additional structure for the spin-side of the connection.

### 4.2 Candidate L2 — Internal index structure of the participation measure

**Proposal.** Different rule-types correspond to different internal index structures on $P_K$:

- **Scalar rule-types (spin 0):** $P_K(x^\mu) \in \mathbb{C}$ (no additional index).
- **Spinor rule-types (spin 1/2):** $P_{K, \alpha}(x^\mu) \in \mathbb{C}^4$ (Dirac spinor index $\alpha = 1, 2, 3, 4$).
- **Vector rule-types (spin 1):** $P_K^\nu(x^\mu) \in \mathbb{C}^4$ (Lorentz vector index $\nu$).
- **Tensor rule-types (spin 2):** $P_K^{\nu\rho}(x^\mu) \in \mathbb{C}^{4 \times 4}$ (symmetric traceless tensor).

The spin value is determined by the structure of the Lorentz-group representation carried by the internal index.

**Implications.**
- Integer-spin representations carry tensor (scalar, vector, tensor) indices → bosonic.
- Half-integer-spin representations carry spinor indices → fermionic.
- The spin-statistics connection arises from the rotational double-cover of half-integer-spin representations.

**Status: CANDIDATE.** This proposal is aligned with standard QFT's identification of particle species with irreducible representations of the Poincaré group. It provides a direct path to the spinor content needed for Dirac but does not by itself derive which representations are realized (which the Standard Model does empirically).

### 4.3 Candidate L3 — Clifford-algebra origin from participation-graph local structure

**Proposal.** The Clifford algebra $\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu}$ arises from a primitive-level anti-commutation structure in the participation graph's local geometry.

**Mechanism candidate.** The four-gradient $\partial_\mu$ has four independent components; a spinor-valued object transforming under Lorentz rotations requires a representation of the rotation group that intertwines the four $\partial_\mu$'s in a way consistent with a square-root-of-d'Alembertian structure. The Dirac equation's first-order form $(i\hbar\gamma^\mu\partial_\mu - mc)\psi = 0$ can be seen as the "square root" of Klein-Gordon, and the Clifford algebra is what makes this square root work:
\begin{equation}
  (i\hbar\gamma^\mu\partial_\mu)(i\hbar\gamma^\nu\partial_\nu) = -\hbar^2 \gamma^\mu\gamma^\nu \partial_\mu\partial_\nu = -\hbar^2 \cdot \tfrac{1}{2}\{\gamma^\mu, \gamma^\nu\}\partial_\mu\partial_\nu = -\hbar^2 g^{\mu\nu}\partial_\mu\partial_\nu = -\hbar^2 \Box,
\end{equation}
so $(i\hbar\gamma^\mu\partial_\mu)^2 = -\hbar^2\Box$, and combining with the mass-shell gives Klein-Gordon.

The Clifford algebra is the unique algebraic structure that permits this square-root factoring of the d'Alembertian. A primitive-level derivation would show that the participation-graph's local anti-commutation structure forces this algebra for fermionic rule-types.

**Status: CANDIDATE-SPECULATIVE.** The Clifford-algebra origin from primitive-level participation-graph anti-commutation is a deep structural claim. Standard QFT takes the algebra as given; deriving it from more primitive structure is frontier research.

### 4.4 Candidate L4 — Rotational double-cover structure

**Proposal.** Fermionic rule-types transform under the double cover of the rotation group (SU(2) for SO(3), or more generally the spin group Spin(n) for SO(n)). A 2π rotation of a fermionic chain introduces a minus sign in its participation measure; a 4π rotation returns it to itself.

**Primitive-level origin candidate.** The rotational structure of the participation graph could admit a double-cover structure at the primitive level, with fermionic rule-types being those that couple to the double-cover representation rather than the single-cover.

**Implications.**
- Half-integer spin value derives from the double-cover structure.
- The minus sign under 2π rotation propagates through the antisymmetry-under-exchange content of L1.
- Connects spin and statistics at the primitive level.

**Status: SPECULATIVE.** The double-cover structure is a well-known feature of standard QFT but has no obvious primitive-level derivation in the current ED stack. Finding a primitive-level origin for the double cover is a major sub-problem.

### 4.5 Combinations and interactions

The four candidate levers are not mutually exclusive. A successful rule-type taxonomy derivation likely combines several of them:

- **L2 + L4:** spinor index structure derives from rotational double-cover representation theory; half-integer spin follows automatically.
- **L1 + L2 + L4 (spin-statistics):** antisymmetric exchange, spinor indexing, and double-cover content together produce the spin-statistics connection (fermions have half-integer spin, anticommute under exchange, satisfy Pauli exclusion).
- **L3 as a derived consequence:** once L2 + L4 specify the spinor structure, the Clifford algebra $\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu}$ may follow as the unique spinor-valued Lorentz-covariant first-order operator.

**The most defensible near-term target:** derive L1, L2, L4 from primitive-level participation-graph structure; obtain L3 as a consequence of the spinor structure.

---

## 5. The spin-statistics connection

### 5.1 The content to derive

The spin-statistics theorem states that particles with integer spin are bosons (commute under exchange) and particles with half-integer spin are fermions (anticommute under exchange). In standard QFT, this theorem is derived from Lorentz invariance + causality (spacelike-separated fields commute or anticommute appropriately) + positive-energy spectrum condition.

At the ED primitive level, the theorem should emerge from whatever structural features produce both spin and statistics simultaneously.

### 5.2 ED scoping

Under the combined Candidates L1 + L2 + L4:

- Spin value derives from the internal-index representation of the Lorentz group (L2).
- Exchange symmetry derives from the rule-type's symmetric or antisymmetric composition under multi-chain exchange (L1).
- The double-cover structure (L4) links the two: rule-types carrying double-cover (spinor) representations necessarily have antisymmetric exchange, while rule-types carrying single-cover (tensor) representations have symmetric exchange.

The ED-level spin-statistics statement would be: **"A chain rule-type carries a double-cover (half-integer spin) representation if and only if its multi-chain participation composition is antisymmetric under exchange."** This would be a primitive-level structural claim, derivable from the participation-graph's rotational + multi-chain-composition structure.

### 5.3 Status

**CANDIDATE.** Combining L1 + L2 + L4 points to the derivation, but the primitive-level argument that ties them together has not been given. This is one of the main derivation targets of the full Stage R.2 program.

---

## 6. Derivation path

The full Stage R.2 derivation is expected to unfold across multiple memos. A scoping-level sequence:

### 6.1 Stage R.2.1 — Multi-chain exchange structure (Candidate L1)

**Content.** Derive from Primitive 03 (shared participation) + Primitive 07 (channel rule-type structure) + Primitive 10 (individuation threshold) + Primitive 11 (commitment) the structural conditions under which a multi-chain joint participation measure takes a specific symmetric or antisymmetric form under exchange.

**Output.** A primitive-level classification of rule-types into exchange-symmetric (bosonic) and exchange-antisymmetric (fermionic) categories.

**Expected memo.** `rule_type_exchange_symmetry.md`.

**Estimated scope.** 1–2 sessions.

### 6.2 Stage R.2.2 — Rotational representation theory (Candidate L2)

**Content.** Derive the Lorentz-group representation content of the participation measure from the covariant structure of Primitives 02, 06, 13. Show that only specific representations (scalar, spinor, vector, tensor) are structurally consistent with Lorentz covariance + local U(1) (and higher gauge) invariance.

**Output.** A primitive-level derivation of the spin-value content: 0, 1/2, 1, 3/2, 2, ... with structural explanation of why these specific values appear.

**Expected memo.** `lorentz_representations_from_primitives.md`.

**Estimated scope.** 2–3 sessions.

### 6.3 Stage R.2.3 — Double-cover structure (Candidate L4)

**Content.** Derive the rotational double-cover structure from primitive-level participation-graph geometry. Show that half-integer-spin rule-types couple to the double-cover representation; this is the primitive-level origin of the minus-sign-under-2π-rotation of fermions.

**Output.** A primitive-level derivation of the double-cover as a structural feature, combined with R.2.1 and R.2.2 to give the full spin-statistics connection.

**Expected memo.** `rotational_double_cover_scoping.md`.

**Estimated scope.** 2–3 sessions. This is the hardest of the sub-stages.

### 6.4 Stage R.2.4 — Clifford algebra as consequence (Candidate L3)

**Content.** Given the spinor index structure (R.2.2) and the double-cover (R.2.3), derive the Clifford algebra $\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu}$ as the unique first-order Lorentz-covariant spinor-valued operator. The Dirac equation follows immediately as the square-root of Klein-Gordon under this algebra.

**Output.** Clifford algebra derivation + Dirac equation in the scalar electromagnetic field (minimal coupling inherited from Stage R.1).

**Expected memo.** `clifford_algebra_from_spinor_structure.md` or incorporated into the Dirac memo.

**Estimated scope.** 1–2 sessions.

### 6.5 Stage R.2.5 — Synthesis

**Content.** Consolidate R.2.1 through R.2.4 into a single synthesis memo for Stage R.2, modeled after `arc_r_stage1_synthesis.md`. Close the rule-type taxonomy sub-program at the bosonic/fermionic + spin-statistics + spinor + Clifford level, scope remaining Standard-Model species content as Arc Q + Arc M long-term frontier.

**Expected memo.** `rule_type_taxonomy_synthesis.md`.

**Estimated scope.** 1 session.

### 6.6 Total scope estimate

**Stage R.2 full derivation: approximately 7–11 memos over multiple sessions.** This is the largest sub-stage in the Phase-2 program so far (for comparison: Stage R.1 was 4 memos; Arc N memory-kernel was 1 memo).

---

## 7. FORCED versus open

### 7.1 What is FORCED at the scoping level

| Item | Source |
|---|---|
| Rule-type as equivalence class of update rules under mutual-substitutability | Primitives 02 + 07 operational definition |
| Existence of rule-type distinction at the primitive level | Primitive 07 §1 |
| Requirement that rule-types reproduce empirically observed particle content | Empirical consistency with Standard Model at the species level |
| Rule-type taxonomy is a shared prerequisite for Arc R Stage R.3 and Arc M | Cross-arc dependency analysis |
| The Clifford algebra is unique (given Lorentz covariance + spinor structure) | Standard Lorentz-representation theory |
| The spin-statistics theorem content (under standard QFT axioms) | External theorem; ED derivation is parallel target |

### 7.2 What remains CANDIDATE

All four candidate structural levers (L1–L4) are CANDIDATE at the scoping level. Selecting or deriving the correct combination is the core of the Stage R.2 sub-program.

| Lever | Role | Promotion target |
|---|---|---|
| L1 (exchange symmetry) | Bosonic/fermionic distinction via multi-chain composition | Promote in R.2.1 |
| L2 (internal index structure) | Spin-value derivation via Lorentz representations | Promote in R.2.2 |
| L3 (Clifford algebra from graph anti-commutation) | Spinor evolution structure | Derive from L2 + L4 in R.2.4 |
| L4 (rotational double-cover) | Half-integer spin + spin-statistics link | Promote in R.2.3 (hardest) |

### 7.3 What remains SPECULATIVE

- **Derivation of the specific Standard Model gauge groups** (U(1) × SU(2) × SU(3)) from primitive-level participation structure. Far beyond Stage R.2 scope.
- **Derivation of the three-generation structure** of the Standard Model fermions. Beyond scope.
- **Derivation of specific mass ratios** (Arc M; dependent on rule-type taxonomy but a separate arc).
- **Higgs mechanism origin** from primitive-level structure. Beyond scope.
- **Supersymmetry, string theory, and other beyond-Standard-Model structures** — not addressed.

### 7.4 What remains OPEN structurally

- **Why only specific rule-types exist.** The rule-type taxonomy should produce a discrete spectrum; deriving which specific entries populate the spectrum (and not others) is a frontier question.
- **Why three spatial dimensions.** The participation-graph structure that produces Lorentz representations is four-dimensional spacetime. Whether the three-spatial-dimension structure is forced or contingent is an open question; relates to anthropic considerations in standard physics.
- **Primitive-level origin of coupling constants.** Gauge-coupling strengths (electromagnetic, weak, strong) are empirically measured; their primitive-level derivation is beyond Stage R.2.

---

## 8. Relationship to Arc M (chain-mass)

### 8.1 Shared prerequisite structure

Stage R.2 and Arc M share the rule-type taxonomy as a prerequisite. Specifically, Arc M's candidate mass identification $m_\tau = \sigma_\tau / c^2$ assigns a rule-type-specific bandwidth signature $\sigma_\tau$ to each rule-type τ; without a classification of τ values, $\sigma_\tau$ cannot be enumerated.

### 8.2 What Arc M contributes beyond Stage R.2

Stage R.2 classifies rule-types structurally (bosonic/fermionic, spin values, Lorentz representation). Arc M takes this classification as input and derives the numerical value of each rule-type's mass via the bandwidth-signature identification.

**Arc M is downstream of Stage R.2.** Stage R.2 does not derive masses; it derives the classification that Arc M uses.

### 8.3 Dependency diagram

```
Primitives 02, 03, 06, 07, 10, 11, 13
  │
  ▼
Stage R.2 rule-type taxonomy (scoping memo = this document)
  │  ├── R.2.1 exchange symmetry
  │  ├── R.2.2 Lorentz representations
  │  ├── R.2.3 double cover
  │  ├── R.2.4 Clifford algebra
  │  └── R.2.5 synthesis
  │
  ├─────────────────────────────┬────────────────────────────┐
  │                             │                             │
  ▼                             ▼                             ▼
Stage R.3 (Dirac emergence)   Arc M (chain-mass)           Arc Q (QFT)
  │                             │                             │
  ▼                             ▼                             ▼
Fermionic relativistic QM     Mass spectrum                Multi-particle
```

---

## 9. Honest framing

### 9.1 What this memo achieves

- Clearly articulates the rule-type taxonomy problem.
- Defines rule-type at the primitive level (§2).
- Catalogs the empirical rule-type content that a complete taxonomy must reproduce (§3).
- Identifies four candidate structural levers for the bosonic/fermionic distinction (§4) and their relationships.
- Scopes the spin-statistics theorem content within the ED framework (§5).
- Outlines a five-sub-stage derivation path (§6) with estimated memo counts.
- Provides a consolidated FORCED / CANDIDATE / SPECULATIVE / OPEN status (§7).
- Maps the relationship to Arc M (§8) with explicit dependency diagram.

### 9.2 What this memo does not achieve

- No primitive-level derivation of any rule-type classification.
- No selection among the four candidate structural levers (L1–L4).
- No derivation of the spin-statistics theorem.
- No primitive-level origin of the Clifford algebra.
- No species-level predictions or Standard Model connection.

These are the core deliverables of the full Stage R.2 derivation program, spanning 7–11 memos.

### 9.3 Scope honesty

**Stage R.2 is the largest single sub-program in Phase 2 so far.** Its scope is multi-session frontier research. The scoping memo (this document) reduces the problem to a tractable sequence of four sub-stages (R.2.1 through R.2.4) plus synthesis (R.2.5), but each sub-stage is itself a non-trivial derivation.

The Standard Model's full species content (gauge groups, generations, mass spectrum) is not a Stage R.2 deliverable. Stage R.2 produces the structural classification at the bosonic/fermionic + spin-statistics + spinor + Clifford level; the rest is frontier research spanning Arc M, Arc Q, and possibly further arcs.

**Honest near-term Stage R.2 target:** unlock Dirac (Stage R.3) by deriving the fermionic spinor-index content and Clifford algebra. This alone is a multi-session achievement and would substantially advance the ED framework's claim to primitive-level foundational structure.

---

## 10. Summary

Rule-type taxonomy is the primitive-level classification of chain update rules. At the scoping level, four candidate structural levers (L1 exchange symmetry, L2 internal index structure, L3 Clifford algebra, L4 rotational double-cover) suggest a derivation path: L1 distinguishes bosonic from fermionic chains via multi-chain composition; L2 derives spin values from Lorentz-representation theory; L4 provides the double-cover structure linking spin and statistics; L3 follows as a consequence of the spinor structure. Together, the four levers scope the derivation of the bosonic/fermionic distinction, the spin-statistics theorem, the spinor index structure, and the Clifford algebra — sufficient to unlock Arc R Stage R.3 (Dirac emergence) and to provide the classificatory input needed by Arc M (chain-mass derivation).

Full Stage R.2 derivation scope is estimated at 7–11 memos across five sub-stages, with opening memo `rule_type_exchange_symmetry.md` as the natural next deliverable. The Standard Model's full species content, gauge structure, and mass spectrum remain long-term frontier targets beyond Stage R.2; closure of Stage R.2 at the bosonic/fermionic + spin-statistics + spinor + Clifford level is the realistic near-term goal.

---

## 11. Cross-references

### Stage-R context
- Phase-2 roadmap: [`quantum/foundations/phase2_extensions_roadmap.md`](phase2_extensions_roadmap.md) §2.1, §5.3
- Arc-R scoping memo: [`quantum/foundations/relativistic_participation_measure.md`](relativistic_participation_measure.md) §6
- Arc-R Stage R.1 synthesis (Stage R.1 closure, Stage R.2 opening): [`quantum/foundations/arc_r_stage1_synthesis.md`](arc_r_stage1_synthesis.md) §5
- Free Klein-Gordon (scalar case; Stage R.1): [`quantum/foundations/klein_gordon_emergence.md`](klein_gordon_emergence.md)

### Arc-M coupling
- Arc M (chain-mass derivation; shared prerequisite): [`quantum/foundations/phase2_extensions_roadmap.md`](phase2_extensions_roadmap.md) §2.3
- U4 Hamiltonian derivation (includes chain-mass SPECULATIVE identification): [`quantum/foundations/u4_hamiltonian_form_derivation.md`](u4_hamiltonian_form_derivation.md) §6

### Primitive stack (load-bearing for Stage R.2)
- Primitive 02 (chain; rule identity): [`quantum/primitives/02_chain.md`](../primitives/02_chain.md)
- Primitive 03 (participation; shared structure for exchange symmetry): [`quantum/primitives/03_participation.md`](../primitives/03_participation.md)
- Primitive 07 (channel; rule-type taxonomy explicitly open at §7.4): [`quantum/primitives/07_channel.md`](../primitives/07_channel.md)
- Primitive 10 (individuation; multi-chain distinguishability): [`quantum/primitives/10_individuation.md`](../primitives/10_individuation.md)
- Primitive 11 (commitment; single-channel outcome): [`quantum/primitives/11_commitment.md`](../primitives/11_commitment.md)

### Classical references
- Pauli, W. (1940). The Connection Between Spin and Statistics. *Physical Review* **58**, 716–722.
- Fierz, M. (1939). Über die relativistische Theorie kräftefreier Teilchen mit beliebigem Spin. *Helvetica Physica Acta* **12**, 3–37.
- Wigner, E. P. (1939). On Unitary Representations of the Inhomogeneous Lorentz Group. *Annals of Mathematics* **40**, 149–204.
- Weinberg, S. (1995). *The Quantum Theory of Fields*, Vol. 1, Chapter 5. Cambridge University Press.
- Dirac, P. A. M. (1928). The Quantum Theory of the Electron. *Proc. Roy. Soc. A* **117**, 610–624.

---

## 12. One-line summary

> **Rule-type taxonomy is the primitive-level classification of chain update rules, defined operationally as equivalence classes of update rules under mutual-substitutability. The Stage R.2 sub-program must reproduce the bosonic/fermionic distinction, the spin-statistics theorem, the spinor index structure for fermionic chains, and the Clifford algebra $\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu}$ — sufficient to unlock Arc R Stage R.3 (Dirac) and provide input for Arc M (chain-mass). Four candidate structural levers are identified: (L1) multi-chain exchange symmetry distinguishing bosonic/fermionic composition, (L2) internal index structure carrying Lorentz-representation content for spin values, (L3) Clifford algebra as consequence of spinor structure, (L4) rotational double-cover for half-integer-spin + spin-statistics linkage. All four are CANDIDATE at the scoping level; promotion is the content of sub-stages R.2.1 through R.2.4 plus synthesis R.2.5, spanning an estimated 7–11 memos. The Standard Model's gauge-group structure, three-generation content, and specific mass spectrum are long-term frontier targets beyond Stage R.2; closure of Stage R.2 at the bosonic/fermionic + spin-statistics + spinor + Clifford level is the realistic near-term goal. Opening memo for the first sub-stage (R.2.1 multi-chain exchange symmetry) is the natural next deliverable.**
