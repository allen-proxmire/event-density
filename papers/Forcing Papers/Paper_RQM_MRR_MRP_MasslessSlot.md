# Paper RQM-MRR-MRP — Conditional Massless Slot via MR-R Chiral + MR-P Gauge

**Series:** Wave-3 Relativistic-QM Bridge — Arc-M Stage MR
**Status:** Wave-3 generative paper; M3 verdict at write-time
**Companions:** Paper_RQM_ArcM_H1, Paper_RQM_GRH_D1, Paper_RQM_T1, Paper_RQM_T7, Paper_087.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the two-branch mutually-exclusive massless-slot characterization (MR-R chiral / MR-P gauge) from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates.
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** derive a substrate-level no-third-mass-removal-mechanism claim. Per audit row 14, the paper observes that the Standard Model uses two mechanisms but does **not** structurally derive that a third mechanism is impossible; that exhaustiveness claim is OPEN. It also does not derive which specific rule-types occupy the MR-R slot (neutrino-mass case is INHERITED / empirical).
5. The **two-branch mutually-exclusive structure** (fermion-class MR-R vs gauge-class MR-P, disjoint per T7 Lorentz-rep classification) is FORM-FORCED conditional on T7 + chiral-symmetry / gauge-invariance machinery; **specific masses, symmetry-breaking parameters, and the no-third-mechanism exhaustiveness** are INHERITED / OPEN.

## Abstract

This paper supplies the substrate-level fine-grained characterization of the massless sector within Arc-M H1: a rule-type can be massless ($\sigma=0$) via one of two **mutually exclusive** mechanisms — **MR-R** (Mass-Removal via R-chiral: fermion-class with unbroken chiral symmetry, forbidding the Dirac mass term) or **MR-P** (Mass-Removal via P-gauge: gauge-class with unbroken gauge symmetry, forbidding the gauge-boson mass term). Mutual exclusivity is FORM-FORCED by the T7 Lorentz-representation classification (fermion-class and gauge-class are disjoint). The slot is **conditional**: occupied only if the protecting symmetry is unbroken. MR-P branch is populated by GRH-D1 (photon). Verdict per Paper_095: **M3** at write-time. Key falsifier line: **F4** (discovery of a third mass-removal mechanism orthogonal to MR-R and MR-P would refute exhaustiveness — but per audit row 14, structural exhaustiveness is itself OPEN).

---

## §1 Statement of Result

**Claim.** The ED Arc-M framework supports a **conditional massless slot**: a substrate-level rule-type can be massless ($\sigma = 0$) via one of two **mutually-exclusive** mechanisms:

- **MR-R (Mass-Removal via R-chiral):** A fermion-class rule-type with conserved chirality (chiral symmetry unbroken). Mass is forbidden by the chiral-symmetry conservation; the rule-type is massless.
- **MR-P (Mass-Removal via P-gauge):** A gauge-class rule-type with unbroken gauge symmetry. Mass is forbidden by gauge-symmetry conservation (no Higgs-like mechanism active); the rule-type is massless.

The two mechanisms are **mutually exclusive**: a given rule-type is either fermion-class (potential MR-R candidate) or gauge-class (potential MR-P candidate), but not both. The mutual exclusivity is FORM-FORCED by the rule-type-class dichotomy (T7 Lorentz-rep classification).

The **conditional** qualifier: a rule-type is in the massless slot **only if** its symmetry-mechanism is unbroken. Symmetry breaking (Higgs mechanism, chiral-symmetry breaking) moves the rule-type out of the massless slot.

Verdict: **M3**. No new postulates.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P05 (Polarity-transport)** — supplies gauge connection content.
- **P09 ($U(1)$-valued polarity)** — supplies gauge group structure.
- **P10 (Rule-type primitive)** — supplies fermion-class and gauge-class rule-types.

> **Substrate-c anchor (footnote).** The propagation rate of $\sigma=0$ substrate excitations is **substrate-c**; substrate-c constancy is postulated (P-RB-1, Paper_012) and INHERITED at numerical value. MR-R and MR-P rule-types in this paper both propagate at substrate-c per this anchor.

### 2.2 Upstream Dependencies

- **I-RQM-T1:** Spin–statistics dichotomy.
- **I-RQM-T7:** Lorentz representations classification.
- **I-RQM-T2:** Cl(3,1) and chirality structure.
- **I-RQM-T4:** Dirac equation (mass term coupling chiralities).
- **I-RQM-GRH-D1:** Existence of at least one massless Case-P gauge rule-type.
- **I-RQM-ArcM-H1:** Mass structural form.
- **I-Chiral:** Standard chiral-symmetry-breaking machinery.
- **I-Higgs:** Standard Higgs-mechanism machinery.

---

## §3 Derivation

### 3.1 MR-R: Mass-Removal via R-chiral

For fermionic rule-types in $D = 3+1$, the Dirac equation couples left-handed and right-handed chiral components through the mass term:
$$\mathcal{L}_{\mathrm{mass}} = -m \bar\Psi \Psi = -m(\bar\Psi_L \Psi_R + \bar\Psi_R \Psi_L) .$$

If the substrate-level chiral symmetry $\Psi_L \to e^{i\alpha_L}\Psi_L$, $\Psi_R \to e^{i\alpha_R}\Psi_R$ (with independent $\alpha_L, \alpha_R$) is unbroken, the mass term is forbidden: it explicitly mixes $L$ and $R$ sectors, violating the chiral symmetry.

A fermion with unbroken chiral symmetry is therefore **massless**. The mechanism is **MR-R (Mass-Removal via R-chiral)**.

**Examples:**
- **Weyl fermions** (purely left-handed or purely right-handed): massless by construction; chiral symmetry is trivially preserved because only one chirality exists.
- **Massless Dirac fermions** in chirally-symmetric theories (rare in nature; standard model breaks chiral symmetry via Higgs).

**Conditional:** MR-R applies only if chiral symmetry is unbroken. Standard-model fermions have masses because Higgs VEV breaks the chiral symmetry, coupling $L$ and $R$ chiralities and generating Dirac mass.

### 3.2 MR-P: Mass-Removal via P-gauge

For gauge-class rule-types (Case-P per Arc-Q), the gauge invariance forbids a mass term unless a Higgs-like mechanism breaks the gauge symmetry. Specifically, a mass term for gauge boson $A_\mu$:
$$\mathcal{L}_{\mathrm{mass}} = \frac{1}{2} m^2 A_\mu A^\mu$$
explicitly breaks $U(1)$ gauge invariance: under $A_\mu \to A_\mu - \partial_\mu \alpha$, the mass term changes.

If gauge invariance is **unbroken** (no Higgs-like mechanism), the mass term cannot appear. The gauge boson is therefore **massless**. The mechanism is **MR-P (Mass-Removal via P-gauge)**.

**Examples:**
- Photon ($U(1)_{EM}$ unbroken): massless.
- Gluon ($SU(3)_C$ unbroken): massless.
- Hypothetical graviton (diffeomorphism invariance): massless.

**Conditional:** MR-P applies only if gauge symmetry is unbroken. Standard-model W and Z bosons have masses because electroweak Higgs VEV breaks $SU(2)_L \times U(1)_Y$ down to $U(1)_{EM}$.

### 3.3 Mutual exclusivity of MR-R and MR-P

By the Lorentz-representation classification (T7, Paper_RQM_T7):
- **Fermion-class** rule-types live in spinor representations $(j_1, j_2)$ with $j_1 + j_2$ half-integer (e.g., Weyl $(1/2, 0)$, Dirac $(1/2, 0) \oplus (0, 1/2)$).
- **Gauge-class** rule-types live in vector representations $(j_1, j_2)$ with $j_1 + j_2$ integer (e.g., vector $(1/2, 1/2)$, tensor $(1, 1)$).

A rule-type's representation determines its class; the classes are disjoint by definition (different total spin).

**MR-R** acts on fermion-class only; **MR-P** acts on gauge-class only. Therefore the two mechanisms are mutually exclusive: a rule-type is in the MR-R massless slot or the MR-P massless slot, but not both.

### 3.4 The conditional massless slot

A rule-type occupies the massless slot iff:
- **(MR-R branch)** it is fermion-class with unbroken chiral symmetry, OR
- **(MR-P branch)** it is gauge-class with unbroken gauge symmetry.

By GRH unconditional D1 (Paper_RQM_GRH_D1), at least one gauge-class rule-type with unbroken gauge symmetry exists (MR-P branch populated by photon-class).

By empirical particle physics, the MR-R branch in nature has either:
- No representatives (if all fermions have masses via Higgs-broken chiral symmetry), OR
- Neutrinos as approximate / candidate occupants (if neutrinos are exactly massless or have very small Majorana-type masses).

The MR-R slot is therefore **conditionally** populated: it exists structurally, but its empirical realization depends on whether nature breaks all chiral symmetries.

### 3.5 Why mutual exclusivity matters

The mutual-exclusivity claim has structural significance: it forces a **clean separation** of mass-generation mechanisms between fermionic and gauge sectors. There is no hybrid case where a rule-type is simultaneously fermion and gauge — the Lorentz-representation classification (T7) prevents this.

This separation is FORM-FORCED. It supplies the substrate-level reason why the Standard Model's mass-generation has two distinct mechanisms (Higgs for gauge bosons, Yukawa for fermions) rather than a single unified mechanism.

### 3.6 Massless slot examples

- **Photon:** MR-P branch, gauge-class, $U(1)_{EM}$ unbroken.
- **Gluon:** MR-P branch, gauge-class, $SU(3)_C$ unbroken.
- **Neutrino (massless limit):** MR-R branch, fermion-class, Weyl-spinor representation.
- **Hypothetical graviton:** MR-P branch, gauge-class (diffeomorphism), tensor representation.

Massive particles (electron, W, Z, etc.) do **not** occupy the massless slot — their respective symmetries are broken.

### 3.7 Connection to Arc-M H1

Paper_RQM_ArcM_H1 (Arc-M H1-dominant) classifies mass-generation by statistics-class-mechanism. This paper (MR-R + MR-P) is the **fine-grained classification** of the massless sector within Arc-M H1: it identifies the two mechanisms by which a rule-type can be massless, distinguishes them as mutually exclusive, and provides the conditional structure for empirical realization.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P05, P09, P10 primitives | P | Primitives. |
| 2 | Lorentz representations classification | I | Paper_RQM_T7. |
| 3 | Spin–statistics dichotomy | I | Paper_RQM_T1. |
| 4 | Dirac mass term couples chiralities | I | Paper_RQM_T4. |
| 5 | Chiral symmetry forbids Dirac mass when unbroken | I | Standard chiral theory (I-Chiral). |
| 6 | MR-R: massless fermion with unbroken chirality | D-via-I | Composition. |
| 7 | Gauge invariance forbids gauge-boson mass without Higgs | I | Standard gauge theory. |
| 8 | MR-P: massless gauge boson with unbroken gauge symmetry | D-via-I | Composition. |
| 9 | Fermion-class and gauge-class are disjoint by Lorentz rep | D-via-I | From T7. |
| 10 | MR-R ↔ MR-P mutually exclusive | D-via-I | Composition of T7 inherited classification result (step 9 is I-from-T7); mutual exclusivity follows from inherited Lorentz-rep disjointness. |
| 11 | Conditional massless slot (active only if symmetry unbroken) | D | From steps 6–10. |
| 12 | GRH D1 guarantees MR-P branch is populated | I | Paper_RQM_GRH_D1. |
| 13 | MR-R branch population: empirical (neutrino case) | I | Empirical. |
| 14 | Mutual exclusivity forces two distinct mass-generation mechanisms | OPEN | Paper observes that the Standard Model has two mechanisms; does **not** derive that a third mechanism is impossible. The substrate-level no-third-mechanism claim is OPEN. (Label could read I for the empirical observation that SM has two; the structural-necessity claim is OPEN.) |
| 15 | Verdict M3 | A→position | Per Paper_095. |

---

## §5 Falsification Criteria

- **F1: Discovery of a rule-type simultaneously fermion-class and gauge-class.** Would refute the mutual-exclusivity claim. (Supersymmetry pairs fermions with bosons but does not place them in the same rule-type — would not refute.)

- **F2: Massless gauge boson with broken gauge symmetry.** Would refute MR-P's necessity condition.

- **F3: Massive fermion with unbroken chiral symmetry.** Would refute MR-R's necessity condition.

- **F4: Discovery of a third mass-removal mechanism orthogonal to MR-R and MR-P.** Would refute exhaustiveness of the massless-slot characterization.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper supplies the substrate-level fine-grained characterization of the massless sector: two mechanisms (MR-R chiral, MR-P gauge), mutually exclusive, conditionally populated.

**Relationship to other RQM-bridge papers:**
- **T1, T7:** supply the fermion / gauge classification.
- **T4:** supplies the chiral-coupling structure of the Dirac mass term.
- **GRH D1:** guarantees MR-P branch population.
- **Arc-M H1:** supplies the broader mass structural form.

**Numerical content INHERITED.** Specific masses, specific symmetry-breaking parameters. **Form FORCED.** Two-branch mutually-exclusive massless-slot structure.

**Future work.** Substrate-level derivation of which specific rule-types occupy the MR-R slot (especially neutrino-mass case); substrate-level derivation of the Higgs mechanism for gauge bosons and Yukawa for fermions.

Verdict: **M3**.

---

**End Paper RQM-MRR-MRP.**
