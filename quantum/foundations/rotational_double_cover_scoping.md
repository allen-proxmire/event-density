# Rotational Double-Cover — Scoping and Partial Derivation

**Stage R.2.3 — Rule-Type Taxonomy Sub-Program, Lever L4**
**Status:** Scoping memo with partial derivation. Configuration-space π_1 = ℤ_2 result FORCED from primitives + 3+1D spatial topology. Frame-rotation ↔ exchange-path identification FORCED modulo one CANDIDATE (frame-availability at the rule-type interface). Admissibility of SL(2,ℂ) for Case-R rule-types FORCED conditional on the frame-availability CANDIDATE. Full spin-statistics closure deferred to Stage R.2.5.

---

## 1. Problem framing

### 1.1 Why Stage R.2.3 is the critical bridge

Stages R.2.1 and R.2.2 produced two independent ℤ_2 dichotomies:

- **R.2.1 (exchange):** Case P (η = +1, symmetric) vs. Case R (η = −1, antisymmetric), determined by how the rule-type's bandwidth content interacts with the individuation threshold under two-chain exchange.
- **R.2.2 (Lorentz):** Integer class (j_L + j_R ∈ ℤ) vs. half-integer class (j_L + j_R ∈ ℤ + 1/2), determined by whether the internal-index representation descends from SL(2,ℂ) to SO⁺(3,1).

Each dichotomy is ℤ_2 and each is primitive-level well-defined. But R.2.2 left open whether the half-integer class is **structurally admissible** — i.e., whether SL(2,ℂ) is the correct covariance group, or merely SO⁺(3,1). Empirically the half-integer class is occupied (fermions exist); structurally R.2.2 flagged this as CANDIDATE C1.

Stage R.2.3 attacks C1. Its objective is to answer, at primitive level:

(Q1) Is SL(2,ℂ) the structurally admissible covariance group?
(Q2) If yes, what is the primitive origin of the 2π-rotation sign (−1)^{2(j_L+j_R)}?
(Q3) Can (Q2) be tied — still at primitive level — to the exchange-sign η of Stage R.2.1, so that the Case P ↔ integer / Case R ↔ half-integer map is FORCED rather than CANDIDATE?

(Q3) is the spin-statistics content; full closure is Stage R.2.5. Stage R.2.3's responsibility is (Q1), (Q2), and the structural setup enabling (Q3).

### 1.2 Operational meaning of "double-cover" for participation measures

Operationally, a double-cover obstruction for a participation measure P_K^a(x^μ) means the following. Let R(θ) be a continuous rotation of the spatial frame by angle θ about a fixed axis. Consider the path θ: 0 → 2π. Under the Stage R.2.2 representation law (Eq. 1 of R.2.2),

  P_K^a(x) ⟶ D(R(θ))^a_b · P_K^b(R(θ)^{-1} x).

For the **physical** configuration, R(2π) = 1 ∈ SO(3), so the point R(2π)^{-1} x = x. The question is whether D(R(2π)) = 1 on the internal index space.

- **Integer class:** D(R(2π)) = +1. P returns to itself; the path is closed in (state space) × (rotation space).
- **Half-integer class:** D(R(2π)) = −1. P returns with a global sign; the path closes only after θ: 0 → 4π.

Whether the half-integer case is **structurally admissible** depends on whether the primitive-level state space of a participation measure is topologically sensitive to the distinction between R(0) and R(2π). If the primitive content sees only SO(3) (simply identifying these rotations), the half-integer class is forbidden. If the primitive content sees the SU(2) double cover (distinguishing them), the half-integer class is permitted.

This is the geometric content of (Q1).

---

## 2. Primitive-level candidates for the double-cover origin

Three candidate primitive-level sources for the 2π → −1 behaviour are worth evaluating independently, since each would produce the double cover through a different mechanism.

### 2.1 Candidate (i) — Worldline-framing at the rule-type interface (Primitives 02 + 07)

**Statement.** Each chain K carries not only a worldline γ_K (Primitive 02) but, at the rule-type interface (Primitive 07), a local frame f_K(τ) — an orthonormal triad in the spatial slice normal to γ_K's tangent. Rule-type interactions between K and adjacent chains K' are mediated by the relative orientation of f_K and f_{K'}. The frame transforms under spatial rotations via the defining SO(3) representation on triads, but the rule-type interface couples to f_K **through its lifted SU(2) representative** whenever the rule-type's bandwidth structure is orientation-sensitive at sub-rotation resolution.

**Primitive-level plausibility.**
- Primitive 02 gives γ_K but does not, by itself, specify a frame along γ_K. Adding a frame is a non-trivial structural claim.
- Primitive 07 (rule-type) does permit orientation-sensitive interactions: the rule-type can discriminate angular structure in how bandwidths are partitioned (cf. §7.4 adjacency sub-channels).
- If a rule-type is **orientation-insensitive** (isotropic at the interface), no frame is needed — only the worldline. This is the Case P limit.
- If a rule-type is **orientation-sensitive** at the rotation-doubling scale, the frame becomes structurally required — this is the hypothesis that singles out Case R.

**Evaluation.** Candidate (i) is attractive because it produces the Case P / Case R split **automatically** from whether the rule-type is orientation-sensitive at the sub-rotation scale. But it depends on a structural assumption — **frame availability at the rule-type interface** — that is not derivable from Primitives 02 + 07 alone; it must be added as a CANDIDATE. Call this CANDIDATE FA (frame-availability). Under FA, candidate (i) delivers the double cover cleanly.

**Status of candidate (i):** Structurally coherent, FORCED conditional on FA. FA itself is the residual CANDIDATE and is the subject of Stage R.2.4 (Clifford algebra, which provides the natural algebraic realisation of a frame).

### 2.2 Candidate (ii) — Local adjacency-graph topology (Primitive 10)

**Statement.** The individuation threshold (Primitive 10) produces a local adjacency graph around each chain. Non-trivial ℤ_2 cycles in this graph could carry the double-cover obstruction.

**Primitive-level plausibility.**
- Primitive 10 produces adjacency structure but does **not** in general produce ℤ_2-non-trivial loops at the chain-local scale. Adjacency is a **connectivity** relation, not a framing.
- A graph's ℤ_2 cohomology is a global topological feature, not a pointwise property of a chain.
- To derive a rotation-specific sign, one would need adjacency loops that close under 2π rotation but not under π rotation. Primitive 10 does not supply such structure; it is agnostic about the rotational embedding of the adjacency graph.

**Evaluation.** Candidate (ii) does not deliver the double cover from primitives. Adjacency topology can carry global ℤ_2 obstructions in principle, but nothing in Primitive 10 ties those obstructions to spatial rotation angle. **Candidate (ii) is rejected as a primitive-level source.**

(It may survive as a contributing structure at the rule-type taxonomy level if adjacency is **combined** with framing, but then the framing does the actual work — see candidate (i).)

### 2.3 Candidate (iii) — Exchange-braiding homotopy class in 3+1D (Primitive 11)

**Statement.** Primitive 11 (commitment dynamics) determines how two same-type chains exchange configurations. The exchange path τ ↦ τ' in the configuration space Q_2 of two identical chains lives in a homotopy class; in 3+1D this class is ℤ_2 (see §3). The ℤ_2 homotopy content is precisely the double cover of SO(3), because Q_2 = (ℝ^3 × ℝ^3 \ Δ) / ℤ_2, whose π_1 is ℤ_2 exactly when the ambient spatial dimension is ≥ 3 (in 2+1D it would be ℤ, yielding anyons).

**Primitive-level plausibility.**
- Primitive 11 produces continuous exchange paths under commitment evolution. This is built-in; no extra structure needed.
- Primitive 02 supplies the ambient 3+1D manifold. Spatial dimension 3 is inherited.
- The configuration-space topology is then a **theorem** about Q_2, not a further CANDIDATE.
- The resulting ℤ_2 matches, by construction, the rotational double cover SU(2) → SO(3), because a π-rotation of the relative coordinate between two identical particles **is** one generator of the ℤ_2.

**Evaluation.** Candidate (iii) delivers the double-cover obstruction **from primitives alone** (Primitives 02 + 11 + spatial dimension 3). It does so through the configuration-space topology route, which is geometric and assumption-minimal. It is the cleanest primitive-level source.

**Status of candidate (iii):** FORCED.

### 2.4 Relation between candidates (i) and (iii)

Candidates (i) and (iii) are not alternatives — they are **complementary facets** of the same structure. Candidate (iii) derives the double-cover obstruction from exchange topology; candidate (i) realises the obstruction as a local framing at the rule-type interface. The first answers "why does the double-cover exist structurally?"; the second answers "how does a specific rule-type couple to it?".

The working assumption for the rest of this memo: candidate (iii) is the primitive-level origin of the double cover; candidate (i) is the rule-type-level realisation, requiring CANDIDATE FA to couple a specific rule-type to half-integer behaviour.

---

## 3. Configuration-space topology

### 3.1 Setup

Two identical (same-type) chains in 3+1D occupy positions x_1, x_2 ∈ ℝ^3 on a constant-time slice (the spatial embedding is Lorentz-frame-dependent but the topological content is not, so we may work on a slice). Their classical configuration space, **with identity of the chains forgotten** (as required by "identical" meaning interchangeable under the rule-type), is

  Q_2 = (ℝ^3 × ℝ^3 \ Δ) / S_2,                                                   (1)

where Δ = {(x, x) : x ∈ ℝ^3} is the coincidence diagonal (excluded because Primitive 10's individuation threshold forbids same-type coincidence in Case R; in Case P the coincidence is permitted but the topology argument is cleaner if we exclude it and check the answer is the same).

### 3.2 Computation of π_1(Q_2)

Introduce centre-of-mass R = (x_1 + x_2)/2 and relative coordinate r = x_1 − x_2 ∈ ℝ^3 \ {0}. The S_2 action is R ↦ R, r ↦ −r. So

  Q_2 ≃ ℝ^3 × (ℝ^3 \ {0}) / ℤ_2,

where ℤ_2 acts antipodally on r. The ℝ^3 factor is contractible. The quotient (ℝ^3 \ {0})/ℤ_2 deformation-retracts to ℝP^2 (since ℝ^3 \ {0} ≃ S^2, and S^2 / antipodal = ℝP^2). Therefore

  π_1(Q_2) = π_1(ℝP^2) = ℤ_2.                                                   (2)

**This is a theorem.** The inputs were:
- Ambient spatial dimension 3 (Primitive 02).
- Exchange symmetry of identical chains (Primitive 11 + rule-type sameness).
- Exclusion of coincidence (Primitive 10, Case R; Case P argument see §3.4).

No further structure is needed. Equation (2) is FORCED.

### 3.3 Why ℤ_2 forbids anyonic phases in 3+1D

A one-dimensional unitary representation of ℤ_2 is a homomorphism ℤ_2 → U(1). There are exactly two: the trivial one (generator ↦ +1, "bosonic") and the sign one (generator ↦ −1, "fermionic"). No phase e^{iθ} with θ ≠ 0, π is a valid representation of ℤ_2.

Contrast with 2+1D: π_1 of the two-particle configuration space is ℤ (the braid group B_2 for 2 strands), whose U(1) representations form a full circle — anyons. 3+1D's higher connectivity (ℝ^3 \ {0} being simply connected, unlike ℝ^2 \ {0}) is what collapses ℤ to ℤ_2.

**Consequence:** In 3+1D, the only admissible exchange phases are η = ±1. This matches Stage R.2.1's dichotomy exactly. The η ∈ {±1} result of R.2.1 is **upgraded from a classification to a topological theorem** by this argument.

### 3.4 Case P and coincidence

For Case P, Primitive 10 **permits** same-type coincidence; the diagonal Δ is not excluded. One might worry that this changes the π_1 computation. It does not: including Δ, the configuration space is Sym²(ℝ^3) = (ℝ^3 × ℝ^3)/S_2, which is contractible (ℝ^3 × ℝ^3 is contractible and the S_2 quotient of a contractible space with a fixed-point set is still contractible). π_1 = 0 in that case, meaning only the trivial exchange class — equivalently, only η = +1.

So:
- Case R (coincidence excluded) → π_1 = ℤ_2 → η ∈ {+1, −1}.
- Case P (coincidence allowed) → π_1 = 0 → η ∈ {+1}.

Both reductions are consistent with R.2.1. Case P is stuck at +1 because the configuration space is contractible; Case R gets both choices because excluding the diagonal opens up the ℤ_2 loop.

**This is an independent derivation of the Stage R.2.1 dichotomy** from configuration-space topology, and it deepens R.2.1: the reason Case P cannot be −1 is topological, not just convention-matching.

---

## 4. Frame-rotation argument

### 4.1 Exchange path ↔ 2π rotation

Consider two identical chains at positions ±r_0 on the x-axis. The exchange path is a continuous trajectory x_1(s), x_2(s) (s ∈ [0,1]) with x_1(0) = −r_0, x_2(0) = +r_0, x_1(1) = +r_0, x_2(1) = −r_0, avoiding coincidence. The canonical such path rotates the line segment joining x_1 and x_2 by π about an axis perpendicular to the segment.

**Key geometric fact (Dirac, Feynman, many expositions):** this π-rotation of the segment corresponds to a 2π rotation of the relative-coordinate frame, because the segment (a line without orientation) returns to itself after π, but a **framed** segment (with a marked end) returns only after 2π.

More precisely: the exchange path represents the non-trivial class of π_1(Q_2) = ℤ_2. Under the natural identification of π_1(Q_2) with π_1(SO(3)) = ℤ_2 (which arises from the SO(3)-equivariant structure of the relative coordinate), the exchange-class generator maps to the 2π-rotation generator.

Thus:

  **Exchange generator in π_1(Q_2)   =   2π-rotation generator in π_1(SO(3)).**  (3)

Both are the non-trivial element of ℤ_2. (3) is a geometric theorem.

### 4.2 Case-R rule-types must couple to the double cover

If a rule-type's participation-measure representation D(Λ) assigns D(R(2π)) = +1, then under (3) its exchange factor η = +1 — i.e., it is Case P.

Contrapositively, if a rule-type is Case R (η = −1), then D(R(2π)) = −1 on its internal index space. By R.2.2 §3.4, D(R(2π)) = −1 requires D to be a representation of SL(2,ℂ) that does **not** descend to SO⁺(3,1) — i.e., a half-integer representation.

**Conclusion (conditional).** Case R rule-types couple to half-integer representations; Case P rule-types couple to integer representations. This is the Case P ↔ integer / Case R ↔ half-integer map of R.2.2 §5, now derived rather than asserted.

### 4.3 Where the frame-availability CANDIDATE enters

The argument of §4.1–4.2 requires that D(R(2π)) be **well-defined as a local transformation on the rule-type's internal index space**. For this, the rule-type interface must carry enough structure to see the difference between 0 and 2π rotations — i.e., it must carry a local frame (or equivalently, an SU(2)-representation-valued attachment, not just an SO(3)-valued one).

CANDIDATE FA (frame-availability): every rule-type carries, at its interface, a local frame f_K in a representation space where 0 and 2π rotations are distinguishable.

Under FA, §4.1–4.2 delivers the map. Without FA, the argument establishes only that **some** rule-types can couple to half-integer representations, not that any **particular** rule-type does.

FA is not derivable from primitives 02, 06, 07, 10, 11 as written. It is the content of Stage R.2.4 (Clifford algebra), where the frame gets an explicit algebraic realisation via γ-matrices and the Dirac bilinears. Stage R.2.3 records FA as the residual CANDIDATE blocking full primitive-level closure.

---

## 5. Structural consequences

### 5.1 SL(2,ℂ) as admissible covariance group (Case R)

For any rule-type carrying a frame (CANDIDATE FA), the primitive-level covariance group is SL(2,ℂ), because the 2π-rotation class of the frame is distinguishable from the identity. The Lorentz-representation content of Stage R.2.2 opens to all (j_L, j_R) with j_L, j_R half-integer.

For any rule-type **not** carrying a frame — e.g., any rule-type whose interface is fully isotropic at the sub-rotation scale — the covariance group collapses to SO⁺(3,1), and only integer representations are admissible.

### 5.2 Half-integer representations are structurally permitted

FORCED: Under FA, half-integer representations are structurally admissible. Combined with R.2.2's ladder, this confirms the full spin spectrum s ∈ {0, 1/2, 1, 3/2, 2, …} at the structural level.

### 5.3 Case P remains single-cover

FORCED: Case P rule-types have η = +1, which by (3) means D(R(2π)) = +1, which means D descends to SO⁺(3,1). Case P is single-cover. This is consistent and expected.

### 5.4 Upgrade of R.2.1 and R.2.2 closure statuses

- R.2.1's η ∈ {+1, −1} result is upgraded: from "exchange-symmetry primitive classification" to "π_1-theorem-forced from 3+1D topology". Same conclusion, stronger derivation.
- R.2.2's CANDIDATE C1 (admissibility of SL(2,ℂ)) is upgraded to FORCED conditional on FA.
- R.2.2's CANDIDATE C2 (Case P ↔ integer, Case R ↔ half-integer) is upgraded to FORCED conditional on FA, via the frame-rotation argument §4.1–4.2.

Post-Stage-R.2.3 summary of the spin-statistics bridge:

  Case P (η = +1, π_1-trivial exchange) ⟺ D(R(2π)) = +1 ⟺ integer spin.
  Case R (η = −1, π_1-nontrivial exchange) ⟺ D(R(2π)) = −1 ⟺ half-integer spin.

Both directions FORCED under FA. This is the spin-statistics correspondence at the primitive level.

---

## 6. FORCED / CANDIDATE / SPECULATIVE

### 6.1 FORCED by primitives

- **F1.** π_1(Q_2) = ℤ_2 in 3+1D from Primitives 02 + 11 + rule-type sameness; inputs are spatial dimension 3 and exchange of identical chains. (§3.2)
- **F2.** Exchange phases are restricted to η ∈ {±1}; anyonic phases forbidden in 3+1D. (§3.3)
- **F3.** Case P configuration space is contractible; η = +1 is forced independently of any dynamical argument. (§3.4)
- **F4.** Exchange-path generator equals 2π-rotation generator in π_1 (geometric theorem). (§4.1)
- **F5.** Case P rule-types couple to integer representations (single-cover). (§5.3)
- **F6.** Candidate (ii) (adjacency-graph ℤ_2 cohomology alone) does not deliver the double cover. (§2.2)

### 6.2 FORCED conditional on CANDIDATE FA

- **F-FA-1.** Case R rule-types couple to half-integer representations (half-cover). (§4.2, §5.1)
- **F-FA-2.** SL(2,ℂ) is the admissible covariance group for Case R. (§5.1)
- **F-FA-3.** The spin-statistics map Case P ↔ integer, Case R ↔ half-integer is established. (§5.4)

### 6.3 CANDIDATE

- **CANDIDATE FA (frame-availability).** Every Case R rule-type carries at its interface a local frame f_K in a representation space where 0 and 2π rotations are distinguishable. Not derivable from Primitives 02, 06, 07, 10, 11 as written. Deferred to Stage R.2.4 for algebraic realisation (Clifford algebra / γ-matrix structure).

### 6.4 SPECULATIVE

- **S1.** Specific assignment of a given ED rule-type to Case P vs. Case R — equivalently to integer vs. half-integer spin — is empirical per rule-type. Structure constrains the taxonomy, not the occupancy.
- **S2.** Higher-spin (s ≥ 3/2) interacting theories and their consistency (Weinberg-Witten, Vasiliev) are outside scope.
- **S3.** Non-Abelian anyons, parastatistics, and other exotic exchange structures are excluded by §3.3 in 3+1D at primitive level; whether they can appear in restricted lower-dimensional subsystems of ED is a separate question.

---

## 7. What remains open

### 7.1 Stage R.2.4 — Clifford algebra derivation

Stage R.2.4 will attack CANDIDATE FA by deriving the frame structure algebraically. The Clifford algebra Cl(3,1) with generators γ^μ satisfying {γ^μ, γ^ν} = 2η^{μν} provides the natural realisation of the frame: its spin bilinears σ^{μν} = (i/2)[γ^μ, γ^ν] generate the SL(2,ℂ) action, and 2π rotations automatically produce the −1 sign on spinor indices.

The primitive-level question for R.2.4 is: **does the rule-type interface structure (Primitive 07 §7.4 levers L1–L4) force a Clifford algebra as the algebraic frame?** The answer is expected to be "yes for Case R rule-types with orientation-sensitive interfaces," making FA FORCED at the R.2.4 level.

### 7.2 Stage R.2.5 — Spin-statistics theorem synthesis

With R.2.3 and R.2.4 in place, Stage R.2.5 will synthesise the full spin-statistics correspondence:

  η = (−1)^{2s}.

The derivation combines:
- R.2.1 (exchange η = ±1 from rule-type structure),
- R.2.2 (spin ladder from Lorentz representations),
- R.2.3 (π_1 = ℤ_2 + frame-rotation identification),
- R.2.4 (FA established via Clifford algebra).

Locality / microcausality arguments (from Primitives 02 + 10 + 11) close the final step by connecting the exchange-path sign to the rotation-representation sign.

### 7.3 Assignment of specific rule-types

The structural derivation of R.2.3–R.2.5 fixes the **ladder** and the **two-category classification**, but not the **occupancy**. Which ED rule-types are Case P and which are Case R — equivalently, which correspond to photon-like / graviton-like / Higgs-like structures and which to electron-like / quark-like / neutrino-like structures — is an empirical mapping, not a structural derivation. Mass, spin, and charge assignments enter as per-rule-type inheritance in the Dimensional Atlas, not as primitive consequences.

---

## 8. Summary

Stage R.2.3 establishes:

1. **π_1 = ℤ_2 is FORCED** in 3+1D from spatial-dimension-3 + exchange of identicals (§3.2). This upgrades R.2.1's ±1 classification from a primitive-level observation to a topological theorem.
2. **Anyons are forbidden** in 3+1D at primitive level (§3.3).
3. **Candidate (ii)** (adjacency-graph topology alone) does not deliver the double cover.
4. **Candidate (iii)** (exchange-braiding π_1) delivers the double-cover obstruction directly from primitives.
5. **Candidate (i)** (worldline-framing at the rule-type interface) realises the obstruction locally, but requires CANDIDATE FA — frame-availability — which is not derivable from the currently-articulated primitive stack.
6. **Under FA**, the Case P ↔ integer / Case R ↔ half-integer spin-statistics map is FORCED; SL(2,ℂ) is the admissible covariance group for Case R; R.2.2's CANDIDATE C1 and C2 are upgraded to FORCED conditional on FA.
7. **FA is deferred** to Stage R.2.4, where the Clifford algebra is expected to provide its algebraic realisation.

Stage R.2.3 closes its scoping responsibility. The partial derivation is as tight as primitive-level content permits pre-R.2.4. The residual opening — CANDIDATE FA — is clearly localised and has an expected closure route.
