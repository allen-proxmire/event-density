# Q.3 Memo 01 — V1 + V2 + V4 (Partial): Vertex Taxonomy, Minimal Coupling as Structural Vertex, Vertex-Anchored Commitment Setup

**Stage:** Arc Q · Q.3 · Memo 01 (load-bearing V1 + V2 derivation; V4 partial)
**Date:** 2026-04-26
**Location:** `arcs/arc-Q/`
**Goal:** Derive V1 (vertex taxonomy under GRH) and V2 (minimal coupling as structural vertex) at CANDIDATE-FORCED. Begin V4 (vertex-anchored commitment for $\tau_g$) at the partial-closure level admitted by Q.3-internal inputs alone — full V4 closure with R-3 deferred to Memo 02 once V3 (vertex-level gauge-quotient, R-2 completion) is established. State R-3 partial closure verdict.
**Predecessors:** [`grh_evaluation.md`](grh_evaluation.md) (Q.1) · [`00_grh_closure_roadmap.md`](00_grh_closure_roadmap.md) · [`01_Q2_memo_00_outline.md`](01_Q2_memo_00_outline.md) · [`02_Q2_memo_01_non_abelian.md`](02_Q2_memo_01_non_abelian.md) · [`03_Q2_memo_02_gauge_quotient.md`](03_Q2_memo_02_gauge_quotient.md) · [`04_Q2_memo_03_verdict.md`](04_Q2_memo_03_verdict.md) (Q.2 substage CLOSED CANDIDATE-FORCED) · [`05_Q3_memo_00_outline.md`](05_Q3_memo_00_outline.md) (Q.3 Memo 00 — V1 / V2 designated forced-via-derivation; V3 / V4 load-bearing)
**Status:** Technical derivation memo. Operates under strict forbidden-input discipline (per Q.3 Memo 00 §5): no R-1 (lightlike worldline), no R-5 (vacuum / particle status), no Q.7 / Q.8 results, no SM specifics, no Higgs / generations / coupling constants, no F-M8 cascade target, no Yang-Mills or BRST as derivation premise. Inherits Q.2's CLOSED CANDIDATE-FORCED commitments (non-Abelian admissibility, kinematic gauge-quotient individuation, L3-interface gauge-invariance structure) as background.
**Purpose:** Discharge V1, V2, and V4 (partial) so Memo 02 can target V3 (vertex-level gauge-quotient, R-2 completion) and V4 completion (R-3 final closure) directly.

---

## 1. The V1, V2, V4 (Partial) Questions Restated

### 1.1 V1 question

**What is the structural vertex taxonomy under GRH?** Specifically: which vertex types are admissible for interactions involving $\tau_g$ (the gauge rule-type) and charged rule-types — emission, absorption, self-coupling, higher-order combinations — and which vertex types are structurally excluded?

The answer must be **finite and complete**: a precise list of admissible vertex types, derived from primitive-level inputs plus inherited GRH content, with explicit exclusion of any vertex types not on the list. The taxonomy must reduce to standard QFT vertex content (QED emission/absorption, Yang-Mills 3-gauge and 4-gauge self-coupling) in the appropriate limit, but must be *derived* rather than imported.

### 1.2 V2 question

**What does it mean for minimal coupling to be a structural vertex in ED terms?** Specifically: is the minimal-coupling form $D_\mu = \partial_\mu + (iq/\hbar) A_\mu$ (and its non-Abelian generalisation) a *structural commitment* of the GRH framework — derivable from L3-interface gauge-invariance plus rule-type properties — or a *postulated rule* that the framework imposes on top of its primitive ontology?

The Q.1 evaluation memo §4.4 noted this as F-GRH-D ("Minimal coupling as a structural interaction"). Q.3 V2 promotes F-GRH-D from CANDIDATE-conditional to CANDIDATE-FORCED at the vertex level. The substantive content: minimal coupling is the *unique* structural vertex form for charged-rule-type / $\tau_g$ interactions, with non-minimal alternatives (magnetic-moment couplings $\psī \sigma^{\mu\nu} \psi F_{\mu\nu}$, non-minimal scalar couplings, derivative couplings beyond minimal) structurally excluded.

### 1.3 V4 (partial) question

**What can be said about τ_g's vertex-anchored commitment using only Q.3-internal inputs (no worldline reformulation from Q.7, no vacuum content from Q.8)?**

R-3 (vertex-anchored commitment) has both a Q.3-side and a Q.7-side. The Q.3-side establishes:
- $\tau_g$'s commitment events are sourced at interaction vertices (not at worldline-intrinsic points)
- Primitive 11 admits this as a structural extension of its commitment-dynamics specification
- Vertex types (V1) supply the commitment-event candidates
- Minimal coupling (V2) supplies the structural vertex form

The Q.7-side (deferred) establishes:
- The lightlike-worldline reformulation (R-1) for $\tau_g$ propagation between vertices
- The affine-parameter machinery for per-worldline accounting
- The full reconciliation of Primitive 11 with $\tau_g$'s lightlike worldline structure

V4 partial closes the Q.3-side; full V4 closure with R-3 awaits Memo 02 (which integrates V3 vertex-level gauge-quotient closure).

### 1.4 Outcome criteria

For V1:
- **FORCED:** unique vertex taxonomy derived from primitives + GRH inheritance with no admissible alternatives.
- **CANDIDATE-FORCED:** unique taxonomy derived, with the CANDIDATE qualifier reflecting Q.2's conditional-forcing structure (specific gauge group inherited).
- **CANDIDATE-admissible:** taxonomy admissible but not uniquely forced.

For V2:
- **CANDIDATE-FORCED:** minimal coupling derived as the structural vertex form, with uniqueness verified against non-minimal alternatives. Anticipated default.
- **CANDIDATE-admissible:** minimal coupling is one admissible form among several.

For V4 (partial):
- **CANDIDATE-FORCED (Q.3-side):** vertex-anchored commitment for $\tau_g$ established from Q.3 inputs alone; full closure pending Memo 02 + Q.7.
- **CANDIDATE-admissible (Q.3-side):** the Q.3-side establishes admissibility but not forcing.

---

## 2. Structural Commitments for V1 (Vertex Taxonomy)

### 2.1 Admissible vertex types

The structural vertex taxonomy under GRH consists of the following vertex types:

#### 2.1.1 (T1) Emission vertex

- **Form.** charged rule-type → charged rule-type + $\tau_g$
- **Schematic.** $\psi \to \psi + A_\mu$
- **Concrete example (background, not derivation).** electron emits photon: $e^- \to e^- + \gamma$
- **Structural conditions.** Lorentz-invariant; gauge-invariant; preserves charged-rule-type's intrinsic content (channel index, internal index); single-vertex emission of one $\tau_g$ quantum.

#### 2.1.2 (T2) Absorption vertex

- **Form.** charged rule-type + $\tau_g$ → charged rule-type
- **Schematic.** $\psi + A_\mu \to \psi$
- **Structural conditions.** Lorentz-invariant; gauge-invariant; preserves charged-rule-type's intrinsic content; single-vertex absorption of one $\tau_g$ quantum. **Reverse of T1** (CPT-related; for $\tau_g$ which is its own antiparticle, T1 and T2 are genuinely related as time-reversal partners).

#### 2.1.3 (T3) 3-gauge self-coupling vertex

- **Form.** $\tau_g + \tau_g \to \tau_g$ (and time-reversed analogs)
- **Schematic.** $A_\mu^a + A_\nu^b \to A_\rho^c$ with structure-constant factor $f^{abc}$
- **Structural conditions.** Lorentz-invariant; gauge-invariant; admissible **only for non-Abelian** gauge groups (Abelian groups have $f^{abc} = 0$). Inherits non-Abelian admissibility from Q.2 Memo 01 (R-4 closure).

#### 2.1.4 (T4) 4-gauge self-coupling vertex

- **Form.** $\tau_g + \tau_g + \tau_g + \tau_g$ (4-leg vertex)
- **Schematic.** $A_\mu^a + A_\nu^b + A_\rho^c + A_\sigma^d$ with structure-constant factor $f^{abe} f^{cde}$ (and permutations)
- **Structural conditions.** Lorentz-invariant; gauge-invariant; admissible **only for non-Abelian** gauge groups. Required for gauge invariance of the $F^a_{\mu\nu} F^{a\mu\nu}$ structure that supplies the vertex.

#### 2.1.5 Vertex-type taxonomy summary

| Vertex type | Form | Abelian? | Non-Abelian? | Inherits from |
|---|---|---|---|---|
| **T1** Emission | $\psi \to \psi + A_\mu$ | yes | yes | R.1 minimal coupling, Memo 01 |
| **T2** Absorption | $\psi + A_\mu \to \psi$ | yes | yes | R.1 minimal coupling, Memo 01 |
| **T3** 3-gauge self-coupling | $A + A \to A$ | NO | yes | Memo 01 (R-4 closure, C3 commitment) |
| **T4** 4-gauge self-coupling | $A + A + A + A$ | NO | yes | Memo 01 (R-4 closure, C3 commitment + gauge-invariance constraint) |

**Four vertex types are admissible under GRH.** All four are structurally derivable from primitive-level inputs + Q.2 inheritance + R.1 minimal-coupling background.

### 2.2 Per-vertex structural conditions

For each vertex type, the following conditions must structurally close:

| Vertex | Lorentz invariance | Gauge invariance | Charged-rule-type preservation | Primitive dependencies | Inherited theorems |
|---|---|---|---|---|---|
| T1 | Required (P-06) | Required (Q.2 + GRH-3) | Required (P-07 L1, L2) | P-02, P-04, P-06, P-07, P-11 | Theorem 1 (spin-statistics for charged rule-types); Theorem 14 (U1 participation-measure for $\tau_g$) |
| T2 | Required (P-06) | Required (Q.2 + GRH-3) | Required (P-07 L1, L2) | P-02, P-04, P-06, P-07, P-11 | Same as T1 (T2 is time-reversed T1) |
| T3 | Required (P-06) | Required (Q.2 + GRH-3); structure-constant content from compact Lie algebra structure | N/A (no charged rule-type involved) | P-04, P-06, P-07 (L2 multi-index), P-11 | Memo 01 (R-4 + non-Abelian admissibility) |
| T4 | Required (P-06) | Required (Q.2 + GRH-3); paired structure-constant contractions | N/A | P-04, P-06, P-07 (L2 multi-index), P-11 | Same as T3 |

### 2.3 Exclusion of higher-order vertices

The structural commitment to vertex types T1–T4 *excludes* higher-order vertex types. Specifically:

#### 2.3.1 (E1) 5-gauge and higher self-coupling vertices

- **Form.** $A^a + A^b + A^c + A^d + A^e \to \cdot$ (5-leg or more)
- **Why excluded.** The non-Abelian self-coupling structure originates from the field strength $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + g f^{abc} A^b_\mu A^c_\nu$ and its gauge-invariant contraction $F^a_{\mu\nu} F^{a\mu\nu}$. This contraction supplies T3 ($A^3$ from $\partial A \cdot A^2$) and T4 ($A^4$ from $A^2 \cdot A^2$) vertices, but **no higher**. There is no primitive-level mechanism to supply $A^5$, $A^6$, etc. vertices: the Lie-algebra structure provides only quadratic ($f^{abc}$) and quartic ($f^{abe} f^{cde}$) tensor combinations at the gauge-invariant level. Higher vertices would require additional primitive-level commitments not present in the GRH framework.

#### 2.3.2 (E2) Non-minimal charged-gauge couplings

- **Forms.** Magnetic-moment vertex $\psī \sigma^{\mu\nu} \psi F_{\mu\nu}$; anomalous-charge-radius vertex $\psī \gamma^\mu \psi \partial_\nu F^{\mu\nu}$; derivative vertices $\partial^n \psī \cdot A^m \cdot \partial^k \psi$ for $n + k > 0$.
- **Why excluded.** L3-interface specifies the *minimal* structural form for gauge-invariant interactions (V2; §3 below). Non-minimal couplings require additional structural commitments (e.g., explicit field-strength factor at the vertex, additional derivative content) not present in the GRH framework. They are admissible as *effective* vertex content (e.g., the electron's anomalous magnetic moment is generated by loop corrections in standard QED, derivable from the minimal-coupling vertex), but not as *structural* vertex content at the primitive level.

#### 2.3.3 (E3) Multi-charged-rule-type vertices

- **Form.** $\psi_1 + \psi_2 \to \psi_3$ (without $\tau_g$ involvement); 4-fermion contact vertices; etc.
- **Why excluded.** GRH is specifically about gauge-rule-type / charged-rule-type interactions. Direct charged-rule-type / charged-rule-type vertices (without gauge-rule-type mediation) would require additional structural commitments beyond GRH (e.g., explicit 4-fermion terms in a Fermi-style theory, or Higgs-Yukawa couplings for SSB-related multi-fermion structure). Such vertices are out of GRH scope; they are Q.4-content (Higgs sector, SSB) or Q.6-content (generation structure, flavor) at most.

### 2.4 V1 conclusion

**The vertex taxonomy under GRH consists of exactly four vertex types: T1 (emission), T2 (absorption), T3 (3-gauge self-coupling, non-Abelian only), T4 (4-gauge self-coupling, non-Abelian only). Higher-order and non-minimal vertices are structurally excluded by primitive-level constraints.**

This taxonomy reduces to standard QFT vertex content in the appropriate limit (QED for U(1), Yang-Mills for non-Abelian) without invoking the standard QFT Lagrangian as a derivation premise.

---

## 3. Structural Commitments for V2 (Minimal Coupling as Structural Vertex)

### 3.1 The minimal-coupling form

For the U(1) case (Stage R.1 background), the minimal-coupling vertex is:
$$
D_\mu = \partial_\mu + \frac{iq}{\hbar} A_\mu
$$
The vertex factor for the emission vertex T1 is $-iq/\hbar \cdot \gamma^\mu$ (for spin-½ charged fermions; analogous for other charged-rule-type structures).

For the non-Abelian generalisation (Memo 01 inheritance), the minimal-coupling vertex is:
$$
D_\mu = \partial_\mu + \frac{ig}{\hbar} A^a_\mu T^a
$$
where $T^a$ are the generators of the gauge group $G$ in the representation of the charged rule-type. The vertex factor for T1 is $-ig/\hbar \cdot \gamma^\mu T^a$.

### 3.2 Derivation as structural vertex (not postulated rule)

V2 establishes that the minimal-coupling form is **derivable** from the GRH framework, not postulated. The derivation chain:

#### 3.2.1 Step 1: L3 interface enforces gauge invariance

From GRH-3 (Q.2 generalisation): the L3 interface for $\tau_g$ enforces local gauge invariance. The interaction between a charged rule-type $\psi$ and $\tau_g$ — i.e., the L3-interface content — must be gauge-invariant under the joint transformation:
- $A_\mu \to U A_\mu U^{-1} + (i/g) U \partial_\mu U^{-1}$
- $\psi \to \rho(U) \psi$, where $\rho$ is the representation of $G$ in which $\psi$ lives

#### 3.2.2 Step 2: Lowest-order gauge-invariant interaction

The lowest-order Lorentz-covariant + gauge-invariant interaction term involving $\psi$, $\bar{\psi}$, and $A_\mu$ (with Lorentz indices contracted) is:
$$
\mathcal{L}_{\mathrm{int}} \propto \bar{\psi} \gamma^\mu (\partial_\mu + \tfrac{ig}{\hbar} A^a_\mu T^a) \psi - \bar{\psi} \gamma^\mu \partial_\mu \psi = \bar{\psi} \gamma^\mu \tfrac{ig}{\hbar} A^a_\mu T^a \psi
$$

This is the **unique** lowest-order gauge-invariant Lorentz-scalar combination of $\psi$, $\bar{\psi}$, and $A_\mu$ at the vertex level. Higher-order terms (with additional $A_\mu$ factors, additional derivatives, or non-minimal index contractions) require additional structural commitments not present in the GRH framework (per V1 §2.3).

#### 3.2.3 Step 3: Minimal coupling inherits

Combining steps 1 and 2: the L3-interface gauge-invariance (forced by GRH-3) plus Lorentz covariance (Primitive 06) plus the lowest-order constraint (no additional structural content beyond GRH) **uniquely determines the minimal-coupling vertex form**.

#### 3.2.4 Step 4: Promotion to structural vertex

R.1's `kg_minimal_coupling_and_current.md` derived the minimal-coupling form for U(1) from local-phase invariance applied to charged-rule-type wavefunctions. R.1 established the form *as a consequence of local-phase invariance*. V2 promotes this from "consequence of local-phase invariance" to "structural vertex content of the GRH framework" by identifying the local-phase-invariance constraint as a *special case* of GRH-3's L3-interface gauge invariance (with U(1) being the Abelian case).

The promotion is bidirectional: GRH-3 generalises R.1's local-phase invariance to non-Abelian; V2 promotes R.1's vertex form to the structural vertex of GRH.

### 3.3 What's FORCED, what's empirical

**FORCED at the vertex form (V2):**
- The **operator structure** $D_\mu = \partial_\mu + (ig/\hbar) A^a_\mu T^a$ as the unique lowest-order gauge-invariant covariant derivative
- The **vertex content** $-ig/\hbar \cdot \gamma^\mu T^a$ for spin-½ charged rule-types (with analogous structure for other spins)
- The **uniqueness** of this form (no admissible non-minimal alternatives at the structural level)
- The **non-Abelian extension** to general compact Lie groups (per Memo 01 R-4 closure)

**Empirical / inherited (NOT forced by V2):**
- The **value** of the coupling constant $g$ — empirical inheritance via the Dimensional Atlas
- The **specific gauge group** $G$ (whether U(1), SU(2), SU(3), or product groups) — empirical inheritance per Q.2 F4 closure
- The **representation $\rho$** in which a specific charged rule-type lives — empirical / Q.4-onward
- The **specific charge assignments** for individual particle species — empirical
- The **value** of $\hbar$ — inherited per the dimensional-atlas Madelung anchoring

This pattern parallels Arc M's "form FORCED, value INHERITED" methodology.

### 3.4 V2 conclusion

**Minimal coupling is the structural vertex form of GRH at the primitive-vertex level.** It is not a postulated rule, not a Lagrangian add-on, not a quantization prescription — it is the unique lowest-order gauge-invariant Lorentz-covariant interaction admissible under the GRH framework's L3-interface specification.

F-GRH-D ("Minimal coupling as a structural interaction") promotes from CANDIDATE-conditional (Q.1) to **CANDIDATE-FORCED at the vertex level** at this memo.

---

## 4. Primitive-Level Audit for V1 and V2

Each primitive is tested against V1 (vertex taxonomy) and V2 (minimal coupling). Classifications: **supports**, **neutral**, **constrains**, **forbids**.

### 4.1 Primitive 02 — worldline + ambient 3+1D manifold

- **V1 test.** Does the spacetime structure admit point-like interaction vertices?
- **Analysis.** Vertices are point-like events on the manifold; multiple worldlines (charged-rule-type worldlines + $\tau_g$'s lightlike trajectory) intersect at vertex points. Standard manifold structure admits this. The lightlike-worldline reformulation question (R-1) is deferred to Q.7 — Primitive 02's spacetime structure does not restrict the vertex-type extension at Q.3's level.
- **V2 test.** Does the manifold admit the four-gradient $\partial_\mu$ that appears in $D_\mu$?
- **Analysis.** Yes — Primitive 06 supplies the four-gradient, and the spacetime manifold (Primitive 02) is the domain. No conflict.
- **Tension.** None at Q.3 level.
- **Falsifiers triggered.** None.
- **Classification:** **neutral** for V1 (does not actively support or constrain); **supports** for V2 via the manifold-structure background.

### 4.2 Primitive 04 — bandwidth fields

- **V1 test.** Do the four-band bandwidth contents accommodate vertex events?
- **Analysis.** Vertex events involve bandwidth-flow exchanges between rule-types: at an emission vertex T1, charged-rule-type bandwidth content shifts (some bandwidth allocated to the emitted $\tau_g$ quantum); at absorption T2, the reverse. Primitive 04's four-band decomposition admits such exchanges naturally — the bands are by-rule-type and by-event, so vertex-mediated exchanges are admissible.
- **V2 test.** Does the minimal-coupling vertex form respect Primitive 04's bandwidth structure?
- **Analysis.** Yes — minimal coupling specifies the vertex factor at the L3-interface level; bandwidth content adjustments at the vertex are consistent with the four-band orthogonality (Primitive 04 §1.5).
- **Tension.** None.
- **Falsifiers triggered.** None.
- **Classification:** **supports** for both V1 and V2.

### 4.3 Primitive 06 — four-gradient + Lorentz covariance

- **V1 test.** Does Lorentz covariance admit the vertex types T1–T4?
- **Analysis.** All four vertex types are Lorentz-invariant by construction:
  - T1 / T2: $\bar{\psi} \gamma^\mu \psi A_\mu$ (Lorentz scalar, contracting $\mu$)
  - T3: $f^{abc} \partial_\mu A^a_\nu A^{b\mu} A^{c\nu}$ (Lorentz scalar)
  - T4: $f^{abe} f^{cde} A^a_\mu A^{b\mu} A^c_\nu A^{d\nu}$ (Lorentz scalar)
- **V2 test.** Does Lorentz covariance admit the minimal-coupling form?
- **Analysis.** Yes — $D_\mu = \partial_\mu + (ig/\hbar) A^a_\mu T^a$ is Lorentz-covariant (transforms as a four-vector under Lorentz; $T^a$ acts on internal index, independent of Lorentz). The vertex factor $-ig/\hbar \cdot \gamma^\mu T^a$ is Lorentz-covariant.
- **Tension.** None.
- **Falsifiers triggered.** None.
- **Classification:** **supports** for both V1 and V2.

### 4.4 Primitive 07 — rule-type taxonomy (load-bearing)

- **L1 (bandwidth partition).** Vertex events shift bandwidth content between rule-types and bands; the partition adjusts at vertices but the structural content of L1 (a partition exists) is unchanged. **Supports** for V1.
- **L2 (internal index).** Vertex factors involve internal-index contractions ($T^a$ for charged rule-type's internal index; $f^{abc}$ for non-Abelian gauge index). L2's general internal-index structure (per Memo 01) admits these. **Supports** for V1 + V2.
- **L3 (interface).** **The load-bearing lever.** L3 specifies how rule-types interact at vertices; GRH-3 (per Q.2 generalisation) supplies the gauge-invariance constraint at the L3 level. V2 derives the minimal-coupling vertex form as the unique lowest-order gauge-invariant L3 interface content. **Supports** V2 directly; supplies the structural foundation for V1's vertex types.
- **L4 (statistics class).** Vertex types are consistent with $\tau_g$'s Case-P statistics (η = +1, integer spin) and with charged rule-types' Case-R statistics (η = −1, half-integer spin) per Theorem 1. **Supports** for V1.
- **Classification (overall):** **supports** — L3 is the load-bearing lever and admits both V1 and V2.

### 4.5 Primitive 10 — individuation threshold

- **V1 test.** Does Primitive 10 admit vertex-level individuation?
- **Analysis.** Vertex events count as commitment events (V4 content); individuation at vertex level is V3 (Memo 02 deferred). At V1's level, Primitive 10 does not interact directly — vertex types are admissible structural objects, not individuation-threshold content.
- **V2 test.** Does Primitive 10 admit minimal-coupling vertex factors?
- **Analysis.** Same — minimal coupling specifies the L3-interface vertex content, not Primitive 10 individuation directly. Q.2 Memo 02 established the kinematic gauge-quotient individuation; vertex-level individuation is V3.
- **Tension.** None at Q.3 Memo 01 level.
- **Falsifiers triggered.** None.
- **Classification:** **neutral** for V1 + V2 (not directly engaged at this memo; engaged at V3 / Memo 02).

### 4.6 Primitive 11 — commitment dynamics (load-bearing for V4 partial)

- **V1 test.** Do vertex types T1–T4 count as commitment events under Primitive 11?
- **Analysis.** This is the V4 partial question (§5). Primitive 11 specifies commitment events as a primitive-level dynamical content; vertex events for $\tau_g$ are commitment events sourced at interaction vertices (R-3 content). For V1's purpose (vertex taxonomy), the question reduces to: do the four vertex types admit being commitment events under Primitive 11's general specification? Anticipated yes (verified in §5 below).
- **V2 test.** Does the minimal-coupling vertex form admit being a commitment-event source under Primitive 11?
- **Analysis.** Same — V2 specifies the structural vertex form; Primitive 11 admits commitment events at vertex points with this form.
- **Tension.** Primitive 11's specification was originally designed for worldline-anchored commitment events (Phase-1 single-rule-type framework). Vertex-anchored commitment for $\tau_g$ is a structural extension; whether Primitive 11 admits this extension natively or requires a refinement is V4's substantive question (§5).
- **Falsifiers triggered.** None at V1 + V2 level. VFal-8 (P-11 incompatibility with vertex commitment) is the V4 question; addressed in §5.
- **Classification:** **supports** for V1 + V2 conditional on Primitive 11 admitting vertex-anchored commitment (V4 partial closure in §5).

### 4.7 Primitive-level audit summary

| Primitive | V1 (vertex taxonomy) | V2 (minimal coupling) | Note |
|---|---|---|---|
| **P-02** | neutral | supports | Manifold structure background |
| **P-04** | supports | supports | Bandwidth content admits vertex exchanges |
| **P-06** | supports | supports | Lorentz covariance verifies all four vertex types and minimal coupling |
| **P-07** | supports | supports | L3 lever load-bearing — admits gauge-invariance constraint and minimal-coupling derivation |
| **P-10** | neutral | neutral | Vertex-level individuation is V3 (Memo 02); not directly engaged here |
| **P-11** | supports (conditional on V4) | supports (conditional on V4) | Primitive 11 admits vertex-anchored commitment subject to V4's closure |

**No primitive forbids V1 or V2.** Four primitives (P-04, P-06, P-07, P-11) actively support; two (P-02, P-10) are neutral or background. No falsifier (VFal-1 vertex primitive incompat., VFal-3 vertex breaks GRH-1/2/4) triggered.

---

## 5. Partial V4: Vertex-Anchored Commitment Without Q.7/Q.8

### 5.1 When τ_g must appear at a vertex

For $\tau_g$ (massless Case-P rule-type with lightlike worldline per GRH-4), commitment events cannot be at intrinsic worldline points: lightlike worldlines have no rest frame, so the proper-time parametrisation that Phase-1's commitment-rate construction assumes (Primitive 11 + Primitive 13) is not available for $\tau_g$.

**The structural alternative:** $\tau_g$'s commitment events are sourced at interaction vertices with charged rule-types. The vertex types T1 and T2 (emission and absorption) are the loci at which commitment events for $\tau_g$ are realised. The non-Abelian self-coupling vertices T3 and T4 also contribute commitment events for $\tau_g$ (involving multiple $\tau_g$ quanta).

Concretely:
- **At every emission vertex T1**, one $\tau_g$ quantum is created — this is a commitment event for $\tau_g$
- **At every absorption vertex T2**, one $\tau_g$ quantum is destroyed — this is a commitment event for $\tau_g$
- **At every 3-gauge vertex T3**, three $\tau_g$ quanta participate (one created and two destroyed, or similar combinations) — three commitment events for $\tau_g$
- **At every 4-gauge vertex T4**, four $\tau_g$ quanta participate — four commitment events for $\tau_g$

The commitment events for $\tau_g$ are **completely vertex-sourced** — there is no admissible alternative locus at the Q.3 level.

### 5.2 When τ_g is forbidden at a vertex

Vertex types **not** in V1's taxonomy (T1–T4) are structurally forbidden, and hence cannot supply commitment events for $\tau_g$. This means:

- **No 5-gauge or higher self-coupling vertices** (per V1 §2.3.1) — $\tau_g$ does not contribute commitment events at non-existent vertex types.
- **No non-minimal charged-gauge vertices** (per V1 §2.3.2) — $\tau_g$ does not contribute commitment events at structurally-excluded magnetic-moment, anomalous-charge-radius, or higher-derivative vertices.
- **No non-physical vertices** (vertices that violate Lorentz covariance or gauge invariance) — $\tau_g$ cannot contribute commitment events at structurally-illegal configurations.

Additionally, $\tau_g$ is forbidden from contributing commitment events at vertex configurations where:
- **Gauge invariance fails** — e.g., a vertex configuration involving $\tau_g$ and charged rule-types that violates the L3-interface gauge-invariance constraint
- **Lorentz covariance fails** — vertex factors must transform as Lorentz scalars (or appropriate covariant tensors); $\tau_g$ cannot contribute at vertex configurations that fail this requirement

### 5.3 How vertex structure constrains τ_g's status

The vertex-anchored commitment specification for $\tau_g$ implies several structural constraints on $\tau_g$'s status as a rule-type:

#### 5.3.1 (C5.1) τ_g participates in physics only through vertices

$\tau_g$'s entire physical content — every commitment event, every observable contribution to physics — is sourced at interaction vertices with charged rule-types (or at non-Abelian self-coupling vertices). Off-vertex, $\tau_g$ propagates between vertices (this is Q.7 content; here we only commit that off-vertex propagation exists, not its specific form).

#### 5.3.2 (C5.2) τ_g's commitment-rate is vertex-density-dependent

Primitive 11's commitment-dynamics specification involves a commitment rate per worldline. For $\tau_g$, this rate is determined by the local vertex density along $\tau_g$'s lightlike trajectory: where the vertex density is high (regions of intense charged-rule-type / $\tau_g$ interaction), the commitment-event rate is high; where vertex density is zero (free-propagation regions), the commitment-event rate is zero.

This is a structural extension of Primitive 11's specification — replacing "commitment rate per proper time along the worldline" with "commitment rate per vertex density along the (lightlike) worldline." The extension does not require new primitive-level content; it adapts the existing specification to $\tau_g$'s lightlike trajectory.

#### 5.3.3 (C5.3) τ_g's individuation respects vertex equivalence

V3 (Memo 02 deferred) will establish that vertex-level individuation respects gauge equivalence. The Q.3 Memo 01 partial commitment is: $\tau_g$'s individuation as a rule-type instance is *vertex-mediated* — two $\tau_g$ quanta sourced at gauge-equivalent vertex configurations count as one rule-type instance, not two. (Full closure pending V3 / Memo 02.)

### 5.4 What's deferred to Q.7 / Q.8

The following V4 content is deferred to downstream substages, not addressable at Q.3 Memo 01:

- **R-1: lightlike-worldline reformulation** — the affine-parameter machinery for $\tau_g$'s propagation between vertices (Q.7 content). At Q.3 Memo 01, we commit that off-vertex propagation exists; we do not specify its parametrisation.
- **R-5: vacuum-vs-particle status of $\tau_g$** — whether $\tau_g$'s vertex events occur in vacuum-state configurations (vacuum polarisation, virtual vertex pairs) is Q.7 / Q.8 content. At Q.3 Memo 01, we commit that vertex events exist at the interaction level; vacuum-state vertex content is downstream.
- **Per-worldline accounting of vertex-anchored commitment events** — Q.7 will reformulate Primitive 11's per-worldline commitment-rate accounting in the affine-parameter framework, integrating the vertex-density-dependent rate of §5.3.2.

### 5.5 V4 partial summary

**The Q.3-side of R-3 closes at Memo 01:** $\tau_g$'s commitment events are sourced at interaction vertices (V1 types T1–T4), with vertex-density-dependent commitment rates (C5.2), and vertex-mediated individuation (C5.3, pending V3 / Memo 02). The Q.7-side (R-1 lightlike worldline + R-5 vacuum status) is deferred.

R-3 partial closure: **CANDIDATE-FORCED at the Q.3 level**, with full R-3 closure pending Q.3 Memo 02 (V4 completion via V3 vertex-level gauge-quotient) and Q.7 (R-1 + R-5 partial).

---

## 6. Falsifier Analysis (VFal-5, VFal-6, VFal-8)

### 6.1 VFal-5 — Vertex-classification inconsistency

- **Statement.** The vertex taxonomy admits structurally inconsistent or redundant vertex types — distinct vertex types that are gauge-equivalent at the kinematic level but counted separately, or vertex types that violate Lorentz covariance.
- **Audit (per §2 + §4).** The four vertex types T1–T4 are pairwise structurally distinct: T1 (1 charged rule-type + 1 gauge boson incoming, 1 charged rule-type outgoing), T2 (reverse of T1), T3 (3 gauge bosons), T4 (4 gauge bosons). They differ in the count and rule-type identity of their participants. None is gauge-equivalent to any other (gauge transformations preserve vertex-type counts of charged + gauge bosons). All four are Lorentz-invariant (per §4.3). Higher-order vertices and non-minimal couplings are structurally excluded (§2.3).
- **Verdict on VFal-5: NOT triggered.** The taxonomy is internally consistent.

### 6.2 VFal-6 — Minimal coupling not unique as structural vertex

- **Statement.** Multiple non-equivalent vertex structures are admissible at the L3 interface level, with no primitive-level discriminator selecting minimal coupling as the unique form.
- **Audit (per §3 + §4).** The derivation in §3.2 establishes that minimal coupling is the unique lowest-order gauge-invariant Lorentz-covariant vertex involving $\bar{\psi}$, $\psi$, and $A^a_\mu$. Higher-order alternatives (magnetic-moment $\sigma^{\mu\nu}$ vertex, derivative couplings, anomalous-charge-radius couplings) require additional primitive-level commitments not present in the GRH framework. The "lowest-order" criterion is itself structurally forced: at higher orders, additional structural commitments would be needed, which are forbidden inputs for Q.3 (per Q.3 Memo 00 §5 — no additional vertex-level Lagrangian content as derivation premise).
- **Verdict on VFal-6: NOT triggered.** Minimal coupling is the unique structural vertex form at the GRH framework level.

### 6.3 VFal-8 — Primitive 11 incompatibility with vertex-anchored commitment for τ_g

- **Statement.** Primitive 11's commitment-dynamics specification requires worldline-intrinsic commitment events that lightlike $\gamma_{\tau_g}$ cannot supply, with no admissible vertex-anchored alternative.
- **Audit (per §5).** Primitive 11's general specification is for commitment events as primitive-level dynamical content; the *worldline-intrinsic* aspect is a Phase-1 single-rule-type framing where commitment rate is per-proper-time along a timelike worldline. For $\tau_g$ (lightlike worldline, no rest frame), the worldline-intrinsic specification does not apply directly — but the *general* commitment-event structure (commitment events as primitive-level dynamical content) is preserved. The vertex-anchored commitment specification (§5) is a structural extension of Primitive 11 to the gauge-rule-type case, replacing "per proper time" with "per vertex density."
  
  This extension is admissible because Primitive 11 specifies *commitment events* at the primitive level, not specifically *worldline-intrinsic commitment events*. The worldline-intrinsic framing was a Phase-1 specialisation, not a Primitive 11 general commitment.
  
  The full reconciliation with Primitive 11 (i.e., showing that the vertex-density commitment rate is consistent with Primitive 11's general specification) requires Q.7's lightlike-worldline reformulation. At Q.3 Memo 01, the Q.3-side of the reconciliation is established: vertex-anchored commitment is a structurally admissible alternative to worldline-anchored commitment for $\tau_g$.

- **Verdict on VFal-8: NOT triggered at Q.3-side level.** The reconciliation is structurally admissible; full reconciliation pending Q.7.

### 6.4 Cumulative falsifier status for V1 + V2 + V4 partial

| Falsifier | Status | Where dispatched |
|---|---|---|
| **VFal-1** (vertex primitive incompat.) | not triggered | §4 (P-02 through P-11 audit) |
| **VFal-2** (vertex L3 incompat.) | not triggered for V1 + V2; deferred to Memo 02 for V3 | §4.4 + §5 |
| **VFal-3** (vertex breaks GRH-1/2/4) | not triggered | §2.2 (GRH preserved per Memo 01 §4.4) |
| **VFal-4** (cross-substage individ. failure) | not triggered for V1 + V2; deferred to Memo 02 for V3 | §5.4 |
| **VFal-5** (vertex taxonomy inconsistent) | **NOT triggered** | §6.1 |
| **VFal-6** (minimal coupling not unique) | **NOT triggered** | §6.2 |
| **VFal-7** (vertex-counting fails gauge) | deferred to Memo 02 (V3) | — |
| **VFal-8** (P-11 incompat with vertex commit.) | **NOT triggered at Q.3-side; full reconciliation Q.7** | §6.3 |
| **VFal-9** (Q.3 ⟷ Q.7 circular) | not triggered for V1 + V2 + V4 partial; full check Memo 03 | §5.4 |

**No falsifier triggered for V1, V2, or V4 partial.** Four falsifiers (VFal-2, VFal-4, VFal-7, VFal-9) deferred to Memo 02 / Memo 03 for full V3 + V4 + V5 dispatch.

---

## 7. Provisional Verdicts for V1, V2, and Partial V4

### 7.1 V1 verdict

**V1 (vertex taxonomy under GRH): CANDIDATE-FORCED.**

Specifically: the vertex taxonomy under GRH consists of exactly four vertex types — T1 (emission), T2 (absorption), T3 (3-gauge self-coupling, non-Abelian only), T4 (4-gauge self-coupling, non-Abelian only). Higher-order vertices (5-gauge and above) and non-minimal couplings (magnetic-moment, anomalous-charge-radius, derivative couplings beyond minimal) are structurally excluded by primitive-level constraints.

The verdict is **CANDIDATE-FORCED** rather than FORCED unconditionally because:
- Specific gauge-group choice remains empirical inheritance per Q.2 F4 closure (T3 and T4 vertices exist *if* the gauge group is non-Abelian, with the choice of $G$ being empirical)
- Specific charged-rule-type representations remain empirical (T1 and T2 vertex factors involve representation matrices $T^a$ in specific representations $\rho$, with the representation choice being empirical)

The conditional-forcing structure parallels Q.2's verdict pattern.

### 7.2 V2 verdict

**V2 (minimal coupling as structural vertex): CANDIDATE-FORCED.**

Specifically: the minimal-coupling form $D_\mu = \partial_\mu + (ig/\hbar) A^a_\mu T^a$ is the unique lowest-order gauge-invariant Lorentz-covariant vertex content for charged-rule-type / $\tau_g$ interactions, derivable from the L3-interface gauge-invariance constraint (GRH-3) plus Lorentz covariance (P-06) plus the lowest-order structural commitment.

F-GRH-D ("Minimal coupling as a structural interaction") promotes from CANDIDATE-conditional (Q.1) to **CANDIDATE-FORCED at the vertex level** at Memo 01.

The verdict is CANDIDATE-FORCED rather than FORCED unconditionally because:
- The coupling constant $g$ value is empirical inheritance via Dimensional Atlas
- The gauge group $G$ (and hence the generator algebra $T^a$) is empirical inheritance per Q.2 F4 closure
- The charged-rule-type representations $\rho$ are empirical / Q.4-onward content
- The value of $\hbar$ is inherited per dimensional-atlas Madelung anchoring

### 7.3 V4 partial verdict

**V4 (vertex-anchored commitment for τ_g, partial Q.3-side): CANDIDATE-FORCED.**

Specifically: $\tau_g$'s commitment events are sourced at interaction vertices (V1 types T1–T4), with vertex-density-dependent commitment rates and vertex-mediated individuation. Primitive 11 admits this vertex-anchored commitment specification as a structural extension to the gauge-rule-type case.

The "partial" qualifier reflects:
- V4's full closure depends on V3's vertex-level gauge-quotient closure (Memo 02 deferred)
- R-3's full closure depends on Q.7's lightlike-worldline reformulation (R-1, deferred to Q.7) for the affine-parameter machinery and the per-worldline accounting
- R-3's full closure also depends on Q.7 / Q.8's vacuum-vs-particle status resolution (R-5)

R-3 partial closure: **CANDIDATE-FORCED at Q.3 Memo 01**; full R-3 closure trajectory: Memo 02 (V4 completion via V3) + Q.7 (R-1 + R-5 partial) + Q.8 (R-5 completion).

### 7.4 Justification

The three verdicts rest on:

- **Primitive-level audit (§4).** No primitive forbids V1, V2, or V4 partial. Four primitives actively support; two are neutral. No VFal-1 trigger.
- **GRH + Q.2 inheritance.** The four-vertex taxonomy inherits from R-4 (Memo 01); the minimal-coupling form inherits from R.1 background promoted to vertex-level structural commitment via GRH-3 + Q.2 generalisation; the vertex-anchored commitment for $\tau_g$ inherits from M.1.2's massless-rule-type framework as background.
- **Falsifier status (§6).** No falsifier triggered for V1, V2, or V4 partial. VFal-5 (taxonomy inconsistent), VFal-6 (minimal coupling not unique), VFal-8 (P-11 incompat) all NOT triggered.
- **Cross-cutting consistency.** V1 vertex types support V2 minimal-coupling derivation; V2 minimal-coupling form supplies V1 vertex factor content; V4 partial vertex-anchored commitment is compatible with both V1 vertex types (as commitment-event candidates) and V2 minimal-coupling form (as the structural vertex content).

---

## 8. Implications for R-3 and R-2 Completion

### 8.1 R-3 status update

**R-3 (vertex-anchored commitment for $\tau_g$) advances to PARTIAL CLOSURE at Memo 01.**

The Q.3-side of R-3 is established: vertex-anchored commitment for $\tau_g$ is a structurally admissible alternative to worldline-anchored commitment, sourced at V1 vertex types T1–T4, with vertex-density-dependent commitment rates and vertex-mediated individuation.

R-3's full closure requires:
- **Memo 02 (V4 completion).** Integration with V3's vertex-level gauge-quotient closure: vertex-mediated individuation of $\tau_g$ as a rule-type instance must respect gauge equivalence at the vertex level.
- **Q.7 (R-1 lightlike worldline reformulation).** The affine-parameter machinery for $\tau_g$ propagation between vertices, with per-worldline accounting of vertex-anchored commitment events.
- **Q.8 (R-5 vacuum vs particle status).** Vacuum-state vertex events (virtual vertex pairs, vacuum polarisation) and their reconciliation with the vertex-anchored commitment specification.

R-3 status: **CANDIDATE-FORCED partial at Q.3 Memo 01; full closure trajectory Memo 02 → Q.7 → Q.8.**

### 8.2 R-2 completion status update

**R-2 completion (vertex-level gauge-quotient individuation) is unchanged at Memo 01.**

V3 is reserved for Memo 02. Memo 01 establishes the vertex taxonomy (V1) and minimal-coupling vertex form (V2) that V3 will use as inputs. The vertex-mediated individuation aspect of V4 partial (§5.3.3) is committed conditional on V3's closure.

R-2 completion status: **outstanding; closure expected at Q.3 Memo 02**.

### 8.3 What remains for Q.3 Memo 02

Q.3 Memo 02 must:

- **Derive V3 (vertex-level gauge-quotient individuation, R-2 completion).** Establish that vertex-level individuation respects gauge equivalence — gauge-equivalent vertex configurations count as one commitment event. Dispatch VFal-7 (vertex-counting fails gauge equivalence).
- **Complete V4 (vertex-anchored commitment, R-3 final).** Integrate V3's closure with the V4 partial specification from Memo 01; close the vertex-mediated individuation aspect explicitly.
- **Dispatch remaining falsifiers** (VFal-2 vertex L3 incompat at V3 level; VFal-4 cross-substage individ. failure; VFal-9 Q.3 ⟷ Q.7 circular at V5 level).
- **State R-3 final closure verdict.**

Anticipated length: comparable to this Memo 01 (substantive primitive-level vertex-derivation work for V3; integration work for V4 completion).

### 8.4 What remains for Q.3 Memo 03

Q.3 Memo 03 must:

- **Verify F1-equivalent items if any** (no Q.3-equivalent of Q.2's F1; possibly bookkeeping integration).
- **Close V5 (downstream dependency map for Q.7 + Q.8).**
- **Issue the Q.3 substage verdict.** Anticipated: CLOSED — CANDIDATE-FORCED, with R-2 completion + R-3 both closed.
- **Dispatch falsifier audits and methodological items.**

---

## 9. Honest Scope Limits

Memo 01 addresses V1, V2, and V4 partial only. The following are explicitly out of scope:

### 9.1 Deferred to Q.3 Memo 02

- **V3 (vertex-level gauge-quotient individuation, R-2 completion).** Memo 02 substantive content.
- **V4 completion (R-3 final closure).** Memo 02 integration with V3.
- **VFal-7, VFal-2 (V3 level), VFal-4, VFal-9** dispatch — Memo 02 work.

### 9.2 Deferred to Q.3 Memo 03

- **V5 (downstream dependency map for Q.7 / Q.8).**
- **Q.3 substage verdict.**

### 9.3 Deferred to Q.7

- **R-1 (lightlike-worldline reformulation for $\tau_g$).** Affine-parameter machinery; per-worldline accounting in lightlike framework.
- **R-5 partial (vacuum-field aspect of $\tau_g$).** Background field interpretation.
- **Vertex-level renormalisation procedures.** Counter-term content.

### 9.4 Deferred to Q.8

- **R-5 completion (zero-point aspect).** Vacuum-state vertex content; virtual vertex pairs.
- **Vacuum polarisation contributions.**
- **Λ from vacuum-vertex content** (already partially established via Theorem 9 Phase-3 background).

### 9.5 Outside the GRH closure trajectory

- **Specific gauge group choice.** Empirical inheritance per Q.2 F4.
- **Coupling constant values** ($q$, $g_s$, $g_w$). Empirical via Dimensional Atlas.
- **Charged-rule-type representations** (which fermions in which representations of $G$). Empirical / Q.4-onward.
- **Higgs sector / SSB vertex content.** Q.4; SPECULATIVE.
- **Generation structure / flavor-changing vertices.** Q.6 / empirical.
- **Charge quantization pattern.** Possibly Q.2 / Q.3 partial sub-memo or empirical.
- **Standard QFT amplitude / scattering content.** Q.7 second-quantisation.
- **Anomalous magnetic moment of the electron.** Standard QED loop-correction content; *derivable* in standard QED from the minimal-coupling vertex; ED's analog is Q.7 work.

---

## 10. One-Line Summary

> Q.3 Memo 01 establishes V1 (vertex taxonomy under GRH = exactly four vertex types T1 emission, T2 absorption, T3 3-gauge self-coupling non-Abelian-only, T4 4-gauge self-coupling non-Abelian-only — with higher-order and non-minimal vertices structurally excluded by primitive-level constraints) and V2 (minimal coupling $D_\mu = \partial_\mu + (ig/\hbar) A^a_\mu T^a$ as the unique lowest-order gauge-invariant Lorentz-covariant structural vertex content, with F-GRH-D promoted from CANDIDATE-conditional to CANDIDATE-FORCED at the vertex level) at **CANDIDATE-FORCED**, plus V4 partial (vertex-anchored commitment for $\tau_g$ with commitment events sourced at V1 vertex types T1–T4, vertex-density-dependent commitment rates, vertex-mediated individuation pending V3 / Memo 02, full R-3 closure pending Q.7 / Q.8) at **CANDIDATE-FORCED Q.3-side** with R-3 advancing to PARTIAL CLOSURE — across a clean primitive-level audit (P-04, P-06, P-07 actively support, P-02 and P-10 neutral, P-11 supports conditional on V4 closure with VFal-8 not triggered), no falsifier triggered for V1 + V2 + V4 partial (VFal-5, VFal-6, VFal-8 all NOT triggered; VFal-2/4/7/9 deferred to Memo 02), with the conditional-forcing characterisation reflecting that specific gauge-group choice + coupling values + charged-rule-type representations remain empirical inheritance per Arc M's "form FORCED, value INHERITED" methodology, advancing the GRH closure trajectory toward Q.3 Memo 02 (V3 vertex-level gauge-quotient + V4 completion = R-2 completion + R-3 final) and ultimately Q.7 (R-1 + R-5 partial) + Q.8 (R-5 completion).

---

## Recommended Next Steps

**(a) Begin Q.3 Memo 02 (V3 + V4 completion; R-2 completion + R-3 final closure).** The natural next deliverable. Memo 02 should: (i) derive V3 (vertex-level gauge-quotient individuation) — establish that vertex-level individuation respects gauge equivalence; the vertex-level analog of Q.2 Memo 02's Q3-A automatic outcome; (ii) integrate V4 completion — close vertex-mediated individuation of $\tau_g$ explicitly; (iii) dispatch VFal-2 (vertex L3 at V3 level), VFal-4 (cross-substage individ. failure), VFal-7 (vertex-counting fails gauge), VFal-9 (Q.3 ⟷ Q.7 circular); (iv) state R-2 completion + R-3 final closure verdicts. Anticipated length: comparable to Memo 01.

**(b) Pre-Memo-02 audit of Wilson-loop / gauge-invariant vertex observable construction.** A short audit (15–30 minutes) confirming that gauge-invariant vertex observables are well-defined for both Abelian and non-Abelian cases. Wilson loops (path-ordered exponentials of $A_\mu$ around closed loops) supply the standard construction; verify that Primitive 04's bandwidth structure and Primitive 10's individuation threshold admit Wilson-loop observables as physical content. Important for V3 closure.

**(c) Verify the vertex-density commitment-rate construction noted in §5.3.2.** A short derivation (2–3 paragraphs) confirming that the structural extension "commitment rate per vertex density" is consistent with Primitive 11's general specification of commitment events as primitive-level dynamical content. This verification belongs in Memo 02 as part of V4 completion but is worth pre-checking now.

**(d) Defer memory-record update until Q.3 closure (Memo 03).** Per the discipline established in U3 / U4 / U5 arcs and the GRH closure roadmap §10. The bundled memory update will capture R-2 completion closure (CANDIDATE-FORCED) plus R-3 closure (CANDIDATE-FORCED) plus Q.3 substage verdict plus downstream handoffs to Q.7 / Q.8.

**(e) (Optional) Sketch the V3 derivation strategy now.** Memo 02's V3 work parallels Q.2 Memo 02's Q3-A derivation (Primitive 10 individuation respects gauge equivalence by consulting gauge-invariant observables). The vertex-level analog: Primitive 10 vertex-individuation respects gauge equivalence by consulting gauge-invariant vertex observables (Wilson loops, gauge-invariant vertex factors). Pre-sketching this now would let Memo 02 land into a known structure. Optional but useful.
