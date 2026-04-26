# Memo 01 — U3 Decomposition, Circularity Audit, and U5 → U3 Transfer

**Date:** 2026-04-26
**Arc:** `arcs/U3/`
**Predecessor:** [`00_arc_outline.md`](00_arc_outline.md)
**Status:** Structural inventory + circularity audit + transfer audit memo. Pins down the conceptual terrain so Memo 02 can derive F1, F2, F3, F4 directly (the four template-transfer items) and Memo 03 can focus on the load-bearing F5 (compatibility with U4) question. Analogous in scope to U5 Memo 01, U4 Memo 01, and U1 Memo 01, with the additional explicit circularity audit and U5 → U3 transfer audit demanded by the structural sensitivity of the F5 question.
**Purpose:** Determine, before any derivation work, which sub-features are forced-via-derivation, which are automatic, which are load-bearing, and what specifically must be proven downstream. Settle the acyclicity discipline that protects F5 from inheriting U4's Framing-1 conditionality circularly.

---

## 1. Sub-Feature Decomposition (Restated Cleanly)

### 1.1 The five sub-features in minimal falsifiable form

The U3 commitment decomposes into five structurally distinct sub-claims. Each must be settled independently for the U3 verdict to close.

- **(F1) Existence of a strongly continuous time-translation representation.** The set $\{U_t : t \in \mathbb{R}\}$ acting on the U2 Hilbert space by $U_t P_K(x, s) := P_K(x, s - t)$ is a strongly continuous one-parameter unitary group. *Falsifier handle:* any structural argument that the time-translation operators are non-unitary, non-continuous, or fail to satisfy the group property.

- **(F2) Uniqueness of the self-adjoint generator (Stone's theorem).** There exists a unique self-adjoint operator $\hat{H}$ on the U2 Hilbert space such that $U_t = \exp(-i\hat{H}t/\hbar)$. *Falsifier handle:* any structural argument that produces two inequivalent generators, or a generator that is symmetric but not self-adjoint.

- **(F3) Linearity of the evolution equation.** The induced equation $i\hbar \, \partial_t P_K = \hat{H} P_K$ is linear in $P_K$. *Falsifier handle:* any structural argument showing the time-translation action is non-linear (e.g., a Gross-Pitaevskii-like nonlinearity arising structurally from the participation-measure components).

- **(F4) First-order-in-time structure.** The evolution equation is first-order in $\partial_t$, not second-order or higher. *Falsifier handle:* any structural argument that the operator-exponential differentiation produces a higher-order equation, or that Stone's theorem's first-order character does not transfer.

- **(F5) Hamiltonian form of the generator (compatibility with U4).** The unique self-adjoint generator $\hat{H}$ produced by F2 coincides as an operator with $\hat{H}_{U4} = \hbar^2|\hat{p}|^2/(2m) + V(\hat{x})$ derived in U4. *Falsifier handle:* any structural argument that the time-translation Stone construction and the U4 Galilean-integration construction produce inequivalent operators on the U2 Hilbert space.

### 1.2 Status classification

| Sub-feature | Classification | Comment |
|---|---|---|
| **F1** | **forced-via-derivation** | Stone's-theorem-precondition derivation transferred from U5; new primitive (P-13) plus inherited U2 structure. |
| **F2** | **forced-via-derivation** | Stone's theorem applied to F1's group. Direct temporal analog of U5's F2. |
| **F3** | **automatic given F1 + F2** | A linear unitary representation induces a linear evolution equation; no separate structural commitment. |
| **F4** | **automatic given F2** | $U_t = \exp(-i\hat{H}t/\hbar)$ differentiated once gives $i\hbar\,\partial_t U_t = \hat{H} U_t$; first-order is built into the operator-exponential form. |
| **F5** | **load-bearing** | The only genuinely substantive structural question of the arc. Requires identifying two independently constructed self-adjoint operators (U3 time-translation generator vs. U4 Galilean-integrated kinetic-plus-potential operator) on the U2 Hilbert space. |

### 1.3 Arc shape implied by the classification

Two forced-via-derivation items (F1, F2), two automatic items (F3, F4), one load-bearing item (F5). The arc is methodologically a *Stone's-theorem application* arc parallel to U5, with F5 as the additional substantive question that has no analog in U5. Anticipated memo split:

- **Memo 02:** F1, F2, F3, F4 (the template-transfer items) — closes routinely.
- **Memo 03:** F5 (compatibility) + arc verdict — load-bearing.
- **Memo 04 (optional):** closure + canonical summary.

The arc is anticipated to be 3 derivation memos plus optional closure, parallel to U5.

---

## 2. Circularity Audit

The U3 arc inhabits a structurally delicate position: U4 was derived under Framing 1 (conditional on U3's existence-of-Hermitian-generator content), and U3 must now be derived without inverting that conditionality. The temptation to use U4's operator form as a derivation input is high but must be resisted everywhere except in F5 (where U4 is the *identification target*, not a derivation premise).

### 2.1 Per-sub-feature audit

#### F1 (existence of time-translation representation)

| Forbidden input | If invoked | Classification |
|---|---|---|
| U4 as derivation input | Would assume the existence of the Hermitian generator U4's Framing 1 conditionalized on — circular with U3's content | **fatal**; not invoked |
| U1 in a way that assumes linearity | The complex structure $e^{i\pi_K}$ is invoked as a *structural property of the carrier*, not as a linearity premise. F1's linearity is not at stake; F1 is about existence + continuity + unitarity of $U_t$ | **removable** by careful framing; reframe as "U1 supplies the carrier on which $U_t$ acts" rather than "U1 supplies linearity" |
| U3 itself (question-begging) | Would assume the time-evolution equation to derive its own time-translation representation | **fatal**; not invoked |
| PDE-level Schrödinger assumptions | Would assume $i\hbar\partial_t\psi = \hat{H}\psi$ to derive the existence of $U_t$ | **fatal**; not invoked |
| Downstream gauge-coupling structure | Magnetic vector potentials would deform $U_t$ via $\hat{p} - eA(\hat{x})/c$. F1 is in the gauge-coupling-free scope | **removable** by scope condition |

**F1 audit verdict:** Clean. The derivation invokes Primitive 13 (time-translation symmetry) + Primitive 03 (homogeneity) + U2 (Hilbert-space arena) only. No fatal circularities; the U1-linearity ambiguity is resolved by framing (U1 supplies the carrier, not the linearity).

#### F2 (Stone-uniqueness)

| Forbidden input | If invoked | Classification |
|---|---|---|
| U4 as derivation input | Stone's theorem itself produces uniqueness; U4 is not needed as a derivation input | **removable**; not invoked |
| U1 in a way that assumes linearity | Stone's theorem operates on the Hilbert-space structure; linearity of the unitary group is built into the definition of "unitary group on a Hilbert space" — not a U1-imported assumption | **removable** by framing |
| U3 itself | Stone's theorem is mathematical; does not require the conclusion as input | **removable**; not invoked |

**F2 audit verdict:** Clean. Stone's theorem is mathematical infrastructure, applied to F1's group.

#### F3 (linearity)

| Forbidden input | If invoked | Classification |
|---|---|---|
| U1 to import linearity directly | F3's linearity is *derived from* the linearity of $U_t$ acting on Hilbert-space elements, which is automatic given F1. No separate import from U1 needed | **removable**; not invoked |
| U4 as derivation input | Not needed | **removable**; not invoked |

**F3 audit verdict:** Clean and automatic. The classification "automatic given F1 + F2" reflects the absence of any need to import linearity separately.

#### F4 (first-order-in-time)

| Forbidden input | If invoked | Classification |
|---|---|---|
| PDE-level Schrödinger assumptions | The first-order character is derived from $U_t = \exp(-i\hat{H}t/\hbar)$ (F2), not assumed from the textbook Schrödinger equation | **removable**; not invoked |
| U4-dependent assumptions about non-relativistic scope | The non-relativistic scope condition is inherited from Phase-1 Step 2's framing, not from U4's specific operator form. The first-order character is a consequence of Stone's theorem's operator-exponential structure, with the non-relativistic scope condition selecting the abelian $\mathbb{R}_t$ time-translation group rather than a Lorentz-boost group | **reframable** by sourcing the scope condition to Phase-1 Step 2 rather than U4 |
| Higher-derivative Klein-Gordon-like structure | Would require a *second* time-translation generator paired with the first, which Stone's theorem does not produce on the U2 Hilbert space under the non-relativistic scope | **removable** by scope condition |

**F4 audit verdict:** Clean. The first-order character is automatic given F2 + the non-relativistic scope condition; both are kosher inputs.

#### F5 (compatibility with U4)

This is where the audit matters most. F5's content is the identification of two independently constructed operators. The discipline is to treat U4's operator only as a *target* of identification, not as a *premise* of derivation.

| Forbidden input | If invoked | Classification |
|---|---|---|
| U4 as derivation input for F1–F4 | F5 is the *only* sub-feature in which U4 appears, and U4's role there is as the identification target (the operator the U3-derived generator must equal), not as a derivation premise | **removable** by F5-only restriction |
| U4's Framing-1 conditionality "U3 exists" | Would close the circular loop: U3 derivation conditional on U4 conditional on U3 | **fatal** if invoked; the discipline forbids using *U4's own existence-assumption-of-U3* as input. Reframed: F5 takes U4's operator form as a mathematical object on the U2 Hilbert space, not as a derivation conditional on U3 |
| Galilean Lie algebra | Used in U4's derivation. May be re-invoked in F5 as a structural infrastructure (the Galilean group is a feature of the non-relativistic scope, not a U4-specific input) | **reframable** as primitive-level (Galilean group is the unique consistent boost-translation algebra in the non-relativistic scope, established in U4's §2.3 but available to U3 independently) |

**F5 audit verdict:** Reframable but delicate. The discipline:

1. F5 derives $\hat{H}_{U3}$ from F1 + F2 only (Stone's theorem on time-translation symmetry).
2. F5 derives $\hat{H}_{U4}$ from U4's operator form, treating U4's derivation as background (not as a U3-input).
3. F5 identifies the two via Galilean Lie algebra structure (or Stone-theorem uniqueness applied to the Galilean group's representation).
4. The identification is *not* a derivation of $\hat{H}_{U3}$ from U4's content; it is an *identification* of the two as the same operator.

Acyclicity preserved: U3 is derived from primitives + Stone's theorem; the identification step closes the U3 ↔ U4 loop *consistently* without making either arc a derivation input to the other.

### 2.2 Summary classification

| Dependency | Where it could appear | Removable / Reframable / Fatal | Resolution |
|---|---|---|---|
| U4 as derivation input for F1–F4 | F1–F4 derivations | **Fatal** | Discipline: U4 forbidden in F1–F4. |
| U4 as identification target in F5 | F5 derivation | **Reframable** | F5 protocol: identify, do not derive-from. |
| U4's Framing-1 "U3 exists" assumption | F5 if mishandled | **Fatal** | Treat U4's operator form as a mathematical object on the U2 Hilbert space, not as a conditional construct. |
| U1 to import linearity | F1, F3 | **Removable** | Linearity comes from Hilbert-space-operator definitions, not from U1 import. |
| U3 itself (question-begging) | Anywhere | **Fatal** | Standard discipline; not invoked. |
| PDE-level Schrödinger assumptions | F4 if mishandled | **Removable** | First-order character derived from Stone's theorem, not imported. |
| Downstream gauge-coupling structure | F1, F5 if mishandled | **Removable** | Scope condition: gauge-coupling-free, inherited from U4. |
| Galilean Lie algebra | F5 | **Reframable** | Treat as primitive-level structure of non-relativistic scope, not as U4-specific input. |

**Overall audit verdict:** No fatal circularities are required by the planned derivations. The two reframable items (F4 non-rel scope sourcing; F5 Galilean structure sourcing) are addressed by careful framing in Memos 02 and 03. The discipline is identical in shape to U5's "U3 forbidden" discipline applied to spatial translations; here the analog is "U4 forbidden as derivation input outside F5."

---

## 3. Transfer Audit (U5 → U3)

The U5 arc closed FORCED via Stone's theorem applied to spatial translation symmetry on the U2 Hilbert space. The U3 arc proposes to apply the same machinery to time translation symmetry. This section evaluates which components of the U5 derivation transfer cleanly.

### 3.1 Per-component transfer

| U5 component | Transfer quality | Adaptation required |
|---|---|---|
| **Stone's theorem structure** | **Clean transfer** | Stone's theorem is mathematical and applies to any strongly continuous one-parameter unitary group on a Hilbert space. The time-translation group on the U2 Hilbert space qualifies, just as the spatial-translation group did. No adaptation required. |
| **Representation theory of unitary translation groups** | **Clean transfer** | The representation theory is identical: abelian one-parameter group, generated by a single self-adjoint operator, exponential parameterization. The temporal axis $\mathbb{R}_t$ behaves identically to a spatial axis $\mathbb{R}^d$ for representation-theoretic purposes (in fact simpler: one-dimensional rather than $d$-dimensional). |
| **Generator uniqueness (Stone's-theorem conclusion)** | **Clean transfer** | Stone's theorem's uniqueness applies on any Hilbert space and any continuous unitary group. Direct application yields uniqueness of $\hat{H}$ as the time-translation generator. |
| **Strong-continuity arguments** | **Clean transfer** | The U5 strong-continuity argument relied on $L^2$-translation continuity, a standard property. The temporal analog uses $L^2$-translation continuity in time, equally standard. The U2 Hilbert space's direct-integral / direct-sum structure across the channel index $K$ inherits continuity in both space and time arguments. |
| **Unitarity arguments** | **Clean transfer** | The U5 unitarity argument used translation-invariance of the U2 measure on the spatial axis. The temporal analog uses translation-invariance of the U2 measure on the time axis — equally supplied by Primitive 13's homogeneity of the time axis and Primitive 03's homogeneity of the participation relation in time. The U2 inner product does not weight by time-dependent factors (no explicit $t$-dependence in the U2 measure construction). |
| **Linearity of the translation action** | **Clean transfer** | $T_a$ acted linearly on participation-measure components; $U_t$ acts linearly on the same components by the same argument (shift of an argument is a linear operation). |
| **Group structure ($T_a T_b = T_{a+b}$)** | **Clean transfer** | Identical: $U_t U_s = U_{t+s}$, $U_0 = I$, $U_{-t} = U_t^{-1}$. Abelian one-parameter group. |
| **Position-representation form derivation ($\hat{p} = -i\hbar\nabla$)** | **Requires reframing** | The U5 step that compared $T_a = \exp(i\hat{p}\cdot a/\hbar)$ with $T_a\psi(x) = \exp(-a\cdot\nabla)\psi(x)$ to derive the position-representation form does not have a direct U3 analog. The time-translation operator $U_t$ also has a similar form ($U_t\psi(t) = \psi(t-s)|_{s=t}$), but the resulting "time-derivative form" $\hat{H} \sim i\hbar\partial_t$ is *exactly the Schrödinger form* — and identifying $\hat{H}$ as such requires either (a) acceptance of the operator-exponential identity as a tautology of Stone's theorem (which it is) or (b) the F5 compatibility identification with U4. For F2, the operator-exponential identity suffices; the *content* of $\hat{H}$ (i.e., what operator it is, not just that it satisfies $U_t = \exp(-i\hat{H}t/\hbar)$) is F5's question. |
| **Plane-wave eigenfunction derivation** | **Rejected** | U5 derived plane waves as eigenfunctions of $\hat{p}$ via the position-representation form. The U3 analog — eigenfunctions of $\hat{H}$ — depends on the *specific* form of $\hat{H}$, which is F5's content. There are no "free" $\hat{H}$-eigenfunctions in the way there are free $\hat{p}$-eigenfunctions; the eigenvalue spectrum and eigenfunctions of $\hat{H}$ depend on the potential $V(\hat{x})$. F2 produces $\hat{H}$ as a self-adjoint operator with *some* spectrum; the spectrum's specifics are post-F5 content and not part of this arc. |
| **Thin-limit / continuum-identification arguments ($K \leftrightarrow k$)** | **Rejected as not directly applicable** | U5's thin-limit identification connected the channel index $K$ to the momentum eigenvalue $k$ via the polarity-phase factor. There is no analogous channel-energy identification here; energy eigenvalues label states, not channels. The thin-limit machinery is a U5-specific feature of the spatial-translation arc that does not carry over. |
| **Dismissal of alternative conjugacies (fractional-Fourier, wavelet, Mellin)** | **Not applicable** | U5 needed to dismiss alternative position-momentum intertwiners. U3 has no analogous question — there is no "alternative time-energy intertwiner" to dismiss; energy is the spectral parameter of $\hat{H}$, not a Fourier-conjugate of time in a representation-theoretic sense. (The energy-time uncertainty relation is *not* a Fourier-conjugacy in the same operator-theoretic sense; this is a well-known subtlety and is not part of the U3 arc.) |
| **Gauge-compatibility check (U2-Continuum conformal redundancy)** | **Clean transfer with simplification** | U5 verified that the U2-Continuum gauge acts trivially on the spatial-translation generator. The temporal analog: the U2-Continuum gauge is a *spatial* conformal rescaling (acting on the spatial measure $d\mu$), which leaves the time-translation generator invariant. The check is simpler than U5's because the gauge does not even act on the relevant axis. |

### 3.2 Transfer summary

| Component class | U5 → U3 status |
|---|---|
| Mathematical infrastructure (Stone, representation theory, $L^2$ continuity) | **Clean transfer** |
| Structural arguments (unitarity, group structure, linearity) | **Clean transfer** |
| Operator identification (position-rep form, eigenfunctions) | **Requires reframing or rejected** — F2 produces $\hat{H}$ abstractly; F5 supplies the content |
| Derivative content (channel-momentum identification, alternative-conjugacy dismissal) | **Not applicable** — no temporal analog |
| Gauge-compatibility check | **Clean transfer with simplification** |

**Transfer audit verdict:** The Stone's-theorem skeleton transfers cleanly. The operator-content questions (what is $\hat{H}$ specifically?) require new structural work — and that work is exactly F5's content. The U3 arc therefore divides naturally into:

- *U5-template content:* F1, F2, F3, F4 — closes by template transfer.
- *Genuinely new content:* F5 — requires the Galilean-Lie-algebra-closure or Stone-theorem-uniqueness compatibility argument.

This is the same conclusion the Memo 00 §6.3 prior anticipated. The transfer audit confirms it explicitly.

---

## 4. Early Eliminations and Classification

### 4.1 What can be classified now

Following §1.2's status classifications and §§2–3's audits, the following early classifications are firm:

- **F1: forced-via-derivation.** The derivation is U5-template-transfer (Stone's-theorem-precondition argument applied to time translations), with Primitive 13 supplying the new time-axis input and Primitives 03 + U2 supplying the rest. The audit confirms no fatal circularities. **Memo 02 will execute the derivation.**

- **F2: forced-via-derivation.** Stone's theorem applied to F1's group. The transfer audit classifies this as clean. **Memo 02 will execute the derivation.**

- **F3: automatic given F1 + F2.** Linearity of the unitary group induces linearity of the evolution equation; no additional structural content. **Memo 02 will state the automatic argument and dispatch Fal-3.**

- **F4: automatic given F2 + non-relativistic scope.** The operator-exponential form $U_t = \exp(-i\hat{H}t/\hbar)$ differentiated once yields a first-order equation. The non-relativistic scope condition (inherited from Phase-1 Step 2) selects the abelian time-translation group rather than a Lorentz boost group. **Memo 02 will state the automatic argument and dispatch Fal-4.**

- **F5: load-bearing.** The compatibility identification between $\hat{H}_{U3}$ (Stone's theorem on time translations) and $\hat{H}_{U4}$ (Galilean Lie algebra integration). The audit identifies the discipline (treat U4 as identification target, not derivation premise) and the candidate arguments (Galilean-algebra-closure, Stone-theorem-uniqueness). **Memo 03 will execute the derivation.**

### 4.2 What remains to be proven

**For Memo 02:**

- **F1:** Prove $\{U_t : t \in \mathbb{R}\}$ is a strongly continuous one-parameter unitary group on the U2 Hilbert space, by direct adaptation of U5's F1 argument to the time axis. Specifically:
  - Show $U_t$ is well-defined componentwise on participation-measure components.
  - Show linearity (componentwise shift is linear).
  - Show unitarity (translation-invariance of U2 measure on time axis).
  - Show group structure ($U_t U_s = U_{t+s}$, $U_0 = I$, $U_{-t} = U_t^{-1}$).
  - Show strong continuity (standard $L^2$-translation continuity in time).
- **F2:** Apply Stone's theorem to F1's group. Conclude existence of unique self-adjoint $\hat{H}$ with $U_t = \exp(-i\hat{H}t/\hbar)$.
- **F3:** State the automatic argument: linear $U_t$ + Stone-theorem identification → linear evolution equation $i\hbar\partial_t P_K = \hat{H} P_K$. Dispatch Fal-3.
- **F4:** State the automatic argument: $U_t = \exp(-i\hat{H}t/\hbar)$ differentiated once → first-order. Dispatch Fal-4.
- **Gauge-compatibility check:** Confirm U2-Continuum gauge acts trivially on $\hat{H}$ (the gauge is spatial-only).
- **Falsifier dispatches in Memo 02:** Fal-1 (non-unitary), Fal-3 (non-linear), Fal-4 (higher-order), Fal-6 (non-self-adjoint), Fal-7 (non-continuous time, conditional on Primitive 13 audit).

**For Memo 03:**

- **F5:** Prove $\hat{H}_{U3} = \hat{H}_{U4}$ on the U2 Hilbert space, using either (a) the Galilean-Lie-algebra-closure argument or (b) the Stone-theorem-uniqueness applied to the Galilean group's representation. Specifically:
  - Identify the Galilean Lie algebra's structure: $\hat{H}$, $\hat{p}$, $\hat{x}$, $\hat{K}$, $\hat{J}$ as generators with the standard commutator structure.
  - Show that $\hat{H}_{U3}$ (the time-translation generator) and $\hat{H}_{U4}$ (the Galilean-integrated kinetic-plus-potential operator) are both representations of the same Lie algebra element — the time-translation generator of the Galilean group.
  - Conclude by Stone-theorem uniqueness (or Galilean-algebra-closure) that the two operators coincide.
- **Falsifier dispatch in Memo 03:** Fal-2 (multiple inequivalent generators), Fal-5 (incompatible with U4).
- **Verdict statement:** FORCED, PARTIAL, or FREE based on F5's outcome.
- **Downstream cascade:** if FORCED, U4 promotes from FORCED-conditional to FORCED-unconditional retroactively; Schrödinger evolution promotes to FORCED-unconditional; Phase-1 closes except for continuum gauge.

---

## 5. Updated Falsifier Map

The seven falsifiers from Memo 00 §3 are recast in light of the Memo 01 audits.

| Falsifier | Targets | Source layer | Memo-01 status | Memo-02/03 dispatch |
|---|---|---|---|---|
| **Fal-1** (non-unitary time) | F1 | Primitive-level (P-13 + U2) | Anticipated dispatched by F1 derivation (U2-measure translation-invariance in time) | Memo 02, F1 §unitarity |
| **Fal-2** (multiple inequivalent generators) | F2 | Primitive-level (mathematically dispatched by Stone's theorem) | **Already dispatched by Stone's theorem itself** (mathematical fact) | Memo 02, F2 §uniqueness — restated for completeness |
| **Fal-3** (non-linear evolution) | F3 | U2-dependent (Hilbert-space linearity) | **Already dispatched by Hilbert-space-operator-definition** | Memo 02, F3 §automatic |
| **Fal-4** (higher-order in time) | F4 | U4-dependent (non-relativistic scope) → reframed to Phase-1 Step 2 scope | **Already dispatched by Stone-theorem operator-exponential differentiation** + non-rel scope | Memo 02, F4 §automatic |
| **Fal-5** (incompatible generator) | F5 | U4-dependent (load-bearing compatibility) | **Open**; the substantive falsifier of the arc | Memo 03, F5 §compatibility |
| **Fal-6** (non-self-adjoint generator) | F2 | Primitive-level (Stone-theorem hypotheses) | **Already dispatched by Stone's theorem** (self-adjointness is automatic) | Memo 02, F2 §self-adjointness |
| **Fal-7** (non-continuous time) | F1 | Primitive-level (Primitive 13 interpretation) | **Conditionally dispatched** — depends on Primitive 13 supplying continuous time. **Pre-Memo-02 audit recommended** (per Memo 00 §7(b)) | Memo 02, F1 §strong-continuity (after Primitive 13 audit) |

### 5.1 Falsifier-status taxonomy after Memo 01

- **Already dispatched (by Memo 01 audits / mathematical theorems):** Fal-2, Fal-3, Fal-4, Fal-6.
- **Anticipated dispatched in Memo 02 (template-transfer derivations):** Fal-1, Fal-7 (conditional on Primitive 13 audit).
- **Open / load-bearing (Memo 03):** Fal-5.

**Six of seven falsifiers are dispatched or anticipated dispatched without substantive new structural work.** Fal-5 is the lone load-bearing falsifier — exactly the pattern the Memo 00 anticipated.

### 5.2 The dispatched-by-mathematical-theorem cluster

Fal-2, Fal-3, Fal-4, Fal-6 are dispatched by mathematical theorems independent of any U3-arc-specific structural content:

- Stone's theorem produces a *unique* self-adjoint generator from a strongly continuous unitary group → dispatches Fal-2 and Fal-6.
- Operators on Hilbert spaces are linear by definition → dispatches Fal-3.
- The operator-exponential form $U_t = \exp(-i\hat{H}t/\hbar)$ differentiated once gives a first-order equation → dispatches Fal-4.

These four falsifiers are listed for inventory completeness but do not require substantive structural arguments in Memos 02 or 03.

---

## 6. Recommended Structure for Memo 02

### 6.1 Proposed memo title

**Memo 02 — U3 F1, F2, F3, F4 Derivations and Falsifier Dispatches**

### 6.2 Proposed section outline

- **§1. Pre-derivation setup.**
  - §1.1 Recap of sub-feature classification from Memo 01.
  - §1.2 Explicit forbidden-input list (U4 forbidden as derivation input; U3 itself forbidden; PDE-Schrödinger forbidden; etc.).
  - §1.3 Inputs declared (Primitive 13, Primitive 03, U2, standard $L^2$ continuity, Stone's theorem).
  - §1.4 Pre-derivation Primitive 13 audit: confirm continuous-time interpretation (per Memo 00 §7(b) recommendation).

- **§2. Derivation of F1 (existence of time-translation representation).**
  - §2.1 The claim.
  - §2.2 Time-translation symmetry as a kinematic feature (Primitives 13 + 03).
  - §2.3 Linearity of $U_t$ on participation-measure components.
  - §2.4 Unitarity (U2-measure translation-invariance in time).
  - §2.5 Group structure.
  - §2.6 Strong continuity.
  - §2.7 Theorem F1 statement.
  - §2.8 Falsifiers Fal-1 and Fal-7 dispatched.

- **§3. Derivation of F2 (uniqueness of self-adjoint generator).**
  - §3.1 Stone's theorem statement.
  - §3.2 Application to F1's group.
  - §3.3 Self-adjointness automatic from Stone's theorem.
  - §3.4 Theorem F2 statement.
  - §3.5 Falsifiers Fal-2 and Fal-6 dispatched.

- **§4. Derivation of F3 (linearity, automatic).**
  - §4.1 The argument: linear $U_t$ + F2 → linear evolution equation.
  - §4.2 The induced equation $i\hbar\partial_t P_K = \hat{H} P_K$.
  - §4.3 Theorem F3 statement.
  - §4.4 Falsifier Fal-3 dispatched.

- **§5. Derivation of F4 (first-order-in-time, automatic).**
  - §5.1 The argument: differentiating $U_t = \exp(-i\hat{H}t/\hbar)$ once yields first-order.
  - §5.2 Non-relativistic scope condition: selects abelian $\mathbb{R}_t$ over Lorentz boosts.
  - §5.3 Theorem F4 statement.
  - §5.4 Falsifier Fal-4 dispatched.

- **§6. Continuum-regime gauge-compatibility check.**
  - §6.1 The U2-Continuum conformal gauge is spatial-only.
  - §6.2 The time-translation generator $\hat{H}$ is gauge-invariant.
  - §6.3 Statement and verification.

- **§7. Joint status and outlook.**
  - §7.1 F1, F2, F3, F4 closed.
  - §7.2 F5 deferred to Memo 03.
  - §7.3 Six of seven falsifiers dispatched; Fal-5 remains.

### 6.3 Memo 02 substantive content overview

#### F1 derivation strategy

Direct adaptation of U5 Memo 03 §1 (or U5 publication paper §6) to the time axis. Define $U_t P_K(x, s) := P_K(x, s - t)$. Verify:

1. **Linearity:** $U_t(\alpha P + \beta Q) = \alpha U_t P + \beta U_t Q$ by componentwise shift linearity.
2. **Unitarity:** $\langle U_t P | U_t Q \rangle = \langle P | Q \rangle$ via change of variables in time integration; U2-measure $d\mu(x) \, dt$ is translation-invariant in $t$ (Primitive 13 supplies translation-invariant time axis; Primitive 03 supplies the homogeneity that makes the U2 measure carry no $t$-weighting).
3. **Group structure:** $U_t U_s = U_{t+s}$, $U_0 = I$, $U_{-t} = U_t^{-1}$.
4. **Strong continuity:** standard $L^2(\mathbb{R}_t)$ translation continuity, lifted to the U2 Hilbert space's direct-integral structure across $K$ and $x$.

Theorem F1: $\{U_t : t \in \mathbb{R}\}$ is a strongly continuous one-parameter unitary group on the U2 Hilbert space.

#### F2 derivation strategy

Direct application of Stone's theorem to F1's group:

> Every strongly continuous one-parameter unitary group $\{V(t) : t \in \mathbb{R}\}$ on a Hilbert space has a unique self-adjoint generator $A$ such that $V(t) = \exp(itA)$.

Apply to $\{U_t\}$: there exists a unique self-adjoint operator $\hat{H}$ on the U2 Hilbert space such that $U_t = \exp(-i\hat{H}t/\hbar)$. (The sign and $\hbar$ factor are conventions; the substantive content is uniqueness and self-adjointness.)

Theorem F2: $\hat{H}$ exists, is unique, is self-adjoint.

#### F3 automatic argument

A linear unitary representation induces a linear evolution equation. Differentiating $U_t P = \exp(-i\hat{H}t/\hbar) P$ at $t = 0$:
$$
\frac{d}{dt}\bigg|_{t=0} U_t P = -\frac{i}{\hbar} \hat{H} P,
$$
so $i\hbar \partial_t P = \hat{H} P$ where $P$ here denotes the time-evolved participation measure, with $\hat{H}$ acting linearly. No nonlinearity arises. **Falsifier Fal-3 dispatched.**

#### F4 automatic argument

The same differentiation produces a first-order equation in $t$. Higher-order ($\partial_t^2$, etc.) would require differentiating $U_t = \exp(-i\hat{H}t/\hbar)$ multiple times, which produces $\hat{H}^n$-actions on $P$ — these are downstream consequences of the first-order equation, not independent equations. The non-relativistic scope condition (inherited from Phase-1 Step 2) selects the abelian $\mathbb{R}_t$ time-translation group; the Lorentz-boost group of relativistic kinematics would mix space and time and produce a different (Klein–Gordon-like) equation, but is out of scope. **Falsifier Fal-4 dispatched.**

#### F5 setup (deferred to Memo 03)

Memo 02 §7 will state F5's framing without deriving it:

- $\hat{H}_{U3}$: produced by F2 as a unique self-adjoint operator on the U2 Hilbert space, with no specified content beyond "the time-translation generator."
- $\hat{H}_{U4}$: derived in U4 paper §F4 as $\hbar^2|\hat{p}|^2/(2m) + V(\hat{x})$ via Galilean Lie algebra integration on the U5 momentum operator.
- F5 question: is $\hat{H}_{U3} = \hat{H}_{U4}$ as an operator on the U2 Hilbert space?
- F5 candidate arguments: Galilean-Lie-algebra-closure or Stone-theorem-uniqueness on the Galilean group's representation.
- F5 anticipated outcome: FORCED via uniqueness of the time-translation generator within the Galilean Lie algebra structure.

Memo 03 will execute F5 in full.

---

## 7. Recommended Next Steps

**(a) Begin Memo 02 (F1, F2, F3, F4 derivations + Fal-1, Fal-3, Fal-4, Fal-6, Fal-7 dispatches).** The natural next step. Following the section outline in §6.2 above, Memo 02 should produce four theorem-grade derivations (F1, F2, F3, F4), four falsifier dispatches (Fal-1, Fal-3, Fal-4, Fal-6), one conditional dispatch (Fal-7, after Primitive 13 audit confirms continuous-time interpretation), and the gauge-compatibility check. The substantive content is template transfer from U5; the derivation should be brisk and disciplined, with explicit acyclicity audits at each step. Anticipated length: comparable to U5 Memo 02 (5 sub-features, ~moderate density). The Memo 02 conclusion will leave only F5 (compatibility with U4) and Fal-5 open for Memo 03.

**(b) Pre-Memo-02 Primitive 13 audit (15–30 minutes).** Confirm the continuous-time interpretation of Primitive 13 and document any discrete-vs-continuous interpretive ambiguities. Specifically: (i) does Primitive 13 supply a continuous time axis $\mathbb{R}_t$ directly, or a discrete time-step structure with continuous-limit lift? (ii) does Primitive 13 carry any explicit time-translation-invariance commitment, or is this implicit via Primitive 03's homogeneity? (iii) is there any structural feature of Primitive 13 that bears on the strong-continuity question of F1? The audit should produce a one-paragraph summary suitable for inclusion as Memo 02 §1.4. If the audit reveals a discrete-time interpretation, F1 acquires a thin-limit step parallel to U5's continuum-regime treatment — manageable but worth knowing in advance.

**(c) Defer memory-record update until Memo 03 closure (per Memo 00 §7(c) discipline).** No memory churn during the arc. After Memo 03 produces the verdict and Memo 04 (closure) integrates the results, a single bundled update to `project_qm_emergence_arc.md` will capture the post-arc state. This memo (Memo 01) does not warrant a separate memory update; its content is recorded in the arc directory and will be summarized in the Memo 04 closure.
