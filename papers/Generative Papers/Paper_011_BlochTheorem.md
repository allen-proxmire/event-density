# Paper 011 — Bloch Theorem from P10 Substrate Translation Symmetry

**Series:** Wave-2 Generative Papers (QM-Kinematics Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of band structure for specific crystalline materials; band content is INHERITED from standard solid-state matching.
2. It does **not** claim a substrate-level theory of crystal formation; the periodic substrate edge-set is declared as a postulate.
3. It does **not** claim novel empirical predictions beyond standard Bloch-Floquet theory.
4. It does **not** introduce new substrate primitives.
5. "Bloch theorem" here means: eigenstates of a Hamiltonian with discrete translation symmetry can be chosen of the form $\psi_k(x) = e^{ikx} u_k(x)$ with $u_k(x+a) = u_k(x)$, where $a$ is the lattice period.

---

## Abstract

Bloch periodicity is FORM-FORCED in ED when the substrate edge-set carrying rule-type dynamics admits a discrete translation symmetry. P10 (Rule-type primitive) supplies the rule-type carrier; P03 (Channel + locus indexing; spatial homogeneity) supplies the substrate-level translation-symmetry primitive at the locus level; the paper-specific postulate P-Discrete-Translation declares a discrete subgroup of P03's translation symmetry. The Bloch form $\psi_k(x) = e^{ikx} u_k(x)$ follows by standard representation-theoretic application of the discrete-translation symmetry to the rule-type Hilbert space.

---

## §1 Introduction

Bloch theorem is the spectral consequence of discrete translation symmetry: eigenstates of a translation-symmetric Hamiltonian decompose into Bloch-form solutions labeled by a crystal momentum $k$ in the Brillouin zone. This paper supplies the substrate-level origin: discrete translation symmetry is a structural feature of the substrate edge-set (a discrete subgroup of P03's continuous-translation primitive), and Bloch form is FORCED by standard representation theory applied to the rule-type Hilbert space.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P03 (Channel + locus indexing; spatial homogeneity)** — supplies substrate-level continuous-translation primitive at the locus level.
- **P07 (Channel structure)** — supplies the channel-level state space.
- **P10 (Rule-type primitive)** — supplies the rule-type carrier whose Hamiltonian is being analyzed.

### 2.2 Upstream dependencies

- **I-Hilbert:** Hilbert-space emergence as completion of motif algebra (Paper_007).
- **I-V1:** V1 finite-width retarded kernel (Paper_089) — supplies the propagator/Hamiltonian structure.
- **I-RepTheory:** Standard representation theory of abelian groups (standard math).
- **I-Fourier:** Standard Fourier analysis on discrete-translation groups (standard math).

### 2.3 Paper-specific postulates

- **P-Discrete-Translation:** The substrate edge-set carrying the rule-type dynamics admits a discrete translation subgroup $\mathbb{Z}^d \subset \mathbb{R}^d$ with lattice vectors $\{a_i\}$. The full continuous-translation primitive P03 is restricted to this subgroup on the relevant substrate edge-set.
- **P-Symmetric-Hamiltonian:** The coarse-grained Hamiltonian commutes with the discrete-translation subgroup.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P03 supplies continuous-translation primitive | P | Primitive (Paper_087). |
| 2 | P10 supplies rule-type carrier | P | Primitive. |
| 3 | Discrete-translation subgroup on relevant substrate edge-set | P-Discrete-Translation | Postulate. |
| 4 | Coarse-grained Hamiltonian commutes with discrete translations | P-Symmetric-Hamiltonian | Postulate. |
| 5 | Hilbert space supports rule-type-carrier states | I | Paper_007. |
| 6 | Simultaneous eigenbasis for translation generators (abelian group rep theory) | I | Standard rep theory (I-RepTheory). |
| 7 | Eigenvalues of translation operator $T_a$ are $e^{ika}$ for $k \in \mathrm{BZ}$ | I | Standard rep theory + I-Fourier. |
| 8 | Bloch form $\psi_k(x) = e^{ikx} u_k(x)$ with $u_k$ periodic | D-via-I | Application of I-RepTheory + I-Fourier to the P-Symmetric Hamiltonian on Hilbert space. |
| 9 | Band structure for specific materials | I | Empirical / standard solid-state matching. |

---

## §3 The Derivation

### 3.1 Discrete translation symmetry from P03 + postulate

P03 supplies the continuous-translation primitive on the substrate: spatial homogeneity at the locus level. P-Discrete-Translation declares that the relevant substrate edge-set retains only a discrete subgroup $\mathbb{Z}^d$ of P03's continuous translations, with lattice vectors $\{a_i\}$. P-Symmetric-Hamiltonian declares that the coarse-grained Hamiltonian $H$ commutes with this discrete subgroup.

### 3.2 Translation operators and their spectrum

The translation operators $T_{a_i}$ form a unitary representation of $\mathbb{Z}^d$ on the rule-type Hilbert space (I-Hilbert from Paper_007). $\mathbb{Z}^d$ is abelian; by standard representation theory (I-RepTheory), $\{T_{a_i}\}$ admit a simultaneous eigenbasis. The eigenvalues are characters of $\mathbb{Z}^d$, parameterized by $k \in \mathrm{BZ} := \mathbb{R}^d/(2\pi \mathbb{Z})^d$:
$$T_{a_i} |k\rangle = e^{i k \cdot a_i} |k\rangle .$$

### 3.3 Bloch form

By P-Symmetric-Hamiltonian, $[H, T_{a_i}] = 0$; eigenstates of $H$ can be chosen as simultaneous eigenstates of $\{T_{a_i}\}$. Such states have the form
$$\psi_k(x) = e^{ikx} u_k(x) , \qquad u_k(x + a_i) = u_k(x) ,$$
by standard Fourier-decomposition on $\mathbb{Z}^d$ (I-Fourier).

This is the Bloch theorem. The FORM is FORCED by I-RepTheory + I-Fourier applied to P-Symmetric-Hamiltonian on the rule-type Hilbert space.

---

## §4 What the Derivation Supplies and Does Not Supply

**Supplies:** Substrate origin of Bloch form as a representation-theoretic consequence of discrete translation symmetry on the rule-type substrate edge-set.

**Does not supply:** Band gaps, effective masses, density of states for specific materials (INHERITED). Substrate-level theory of crystal formation. Topological band invariants (OPEN; see Paper_011 follow-ups).

---

## §5 Open Structural Questions

- **O-Bloch-1:** Substrate-level theory of why specific substrate edge-sets exhibit discrete translation symmetry (crystal formation).
- **O-Bloch-2:** Topological band invariants (Chern numbers, $\mathbb{Z}_2$ invariants) via substrate-level bundle structure.
- **O-Bloch-3:** Bloch theorem for non-abelian substrate symmetries (magnetic translation group, Hofstadter problem).
- **O-Bloch-4:** Disorder corrections / Anderson localization in substrate framework.

---

## §6 Falsification Criteria

- **F1:** Empirical detection of a translation-symmetric system whose eigenstates do **not** admit Bloch form — would refute the application.
- **F2:** Substrate evidence that the relevant edge-set carries a non-abelian translation group (e.g., magnetic translation group with non-zero flux per plaquette) without modifying §3 derivation appropriately — would highlight an unaddressed regime.
- **F3:** Demonstration that the rule-type Hilbert space does NOT support a unitary representation of the discrete-translation group — would refute I-Hilbert application.

---

## §7 Position Statement

Bloch periodicity is **FORM-FORCED** in ED by P03 + P10 + paper-specific postulates declaring the discrete-translation regime. The derivation applies standard representation theory (I) to the postulated symmetric Hamiltonian on the rule-type Hilbert space. Band content is **INHERITED** from standard solid-state matching.

---

**End Paper 011 (FIXED).**
