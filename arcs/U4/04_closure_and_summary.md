# Memo 04 — U4 Arc Closure and Canonical Summary

**Date:** 2026-04-26
**Arc:** `arcs/U4/`
**Predecessors:** Memos [00](00_arc_outline.md), [01](01_decomposition_and_mapping.md), [02](02_F1_F2_F5_derivations.md), [03](03_F3_F4_and_verdict.md)
**Status:** Closure memo. Provides the canonical summary of the U4 arc and its public-facing explanation. Integrates the result into the QM-emergence program, with the active upstream-CANDIDATE inventory now reduced to a single item (U3) plus the description-level continuum gauge.
**Purpose:** Close the U4 arc with a single document that serves both as internal entry-point and as a self-contained external narrative.

---

## 1. Canonical Summary

The U4 arc asked whether the specific Hamiltonian form $\hat{H} = \hbar^2 |\hat{p}|^2 / (2m) + V(\hat{x})$ — the structural backbone of Schrödinger emergence at the dynamical level — is forced by the participation-measure framework's primitive structure, or whether it remains an inherited postulate from standard QM. The arc adopted **Framing 1**: U4 is derived *conditional on* the existence of a Hermitian Hamiltonian generator (which is sibling CANDIDATE U3's content). Within this framing, the arc decomposed U4 into five sub-features:

- **F1** Channel-momentum identification
- **F2** Plane-wave eigenfunctions
- **F3** Quadratic-in-$|\hat{p}|^2$ kinetic structure
- **F4** Specific coefficient $1/(2m)$
- **F5** Kinetic + potential decomposition $\hat{H} = T(\hat{p}) + V(\hat{x})$

Memo 01 performed the circularity audit (handling U3 as sibling CANDIDATE under Framing 1) and the transfer audit of the 2026-04-24 tightening-program memo, identifying that §§2.1–2.4 + §3 + §4 of the existing memo transferred cleanly while §2.5 (the silent adoption of the factor of 2 in $1/(2m)$) was the precise structural gap requiring sharpening. Memo 02 closed F1 (via direct transfer of U5 Memo 03 §1's Stone's-theorem argument), F2 (mathematical consequence), and F5 (translation invariance + locality) cleanly, and prepared the structural ground for F3 + F4 with the four-constraint setup C1+C2+C3+C4 plus the G1/G2/G3 framing decision for the Galilean-invariance question. Memo 03 executed the load-bearing derivations: F3 closed via the four-constraint argument with all candidate alternatives (linear-in-$|\hat{p}|$, higher-even-power, anisotropic, relativistic dispersion) explicitly dismissed; F4 closed under G1 via the Galilean-from-primitives derivation, with **the factor of 2 in $1/(2m)$ shown to emerge from integrating the Galilean commutator condition $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ against the boost generator $\hat{K} = m\hat{x} - t\hat{p}$ — not as a convention borrowed from classical mechanics, but as the integration Jacobian of the Galilean Lie algebra structure within the non-relativistic scope.**

The verdict: **U4 is FORCED**, with form-FORCED-value-INHERITED framing. The kinetic-energy operator's *form* is uniquely determined by primitive-level inputs plus the Galilean Lie algebra (within the non-relativistic-single-particle gauge-coupling-free scope of Phase-1 Step 2). The mass parameter $m$ is inherited per Arc M's "form FORCED, values INHERITED" methodology; the $\hbar$ factor is inherited via the dimensional-atlas Madelung anchoring. The arc introduces no new structural CANDIDATEs; the conditionalities are all inherited (U3 sibling, non-rel scope, gauge-coupling-free scope, mass values, $\hbar$ value). All seven falsifiers are dispatched within the stated scope conditions. The active upstream-CANDIDATE inventory of the QM-emergence Phase-1 program reduces from {U3, U4} + gauge to **{U3} + continuum gauge** — a single remaining item to close the entire Phase-1 structural-foundations program.

---

## 2. Sub-Feature Verdict Table

| Sub-feature | Verdict | Established in | Structural inputs |
|---|---|---|---|
| **F1** Channel-momentum identification | FORCED | Memo 02 §1 | Primitives 03 + 06 (translation symmetry, kinematic) + U2 (FORCED, prior arc) + Stone's theorem; explicitly U3-independent |
| **F2** Plane-wave eigenfunctions | FORCED (automatic given F1) | Memo 02 §2 | F1 + standard mathematical consequence ($\hat{p} = -i\hbar\nabla$ in position representation) |
| **F3** Quadratic-in-$|\hat{p}|^2$ kinetic structure | FORCED | Memo 03 §2 | C1 translation invariance + C2 rotation invariance + C3 analyticity + C4 non-relativistic-limit scope condition |
| **F4** Specific coefficient $1/(2m)$ | **FORCED form (factor of 2 derived); $m$ INHERITED per Arc M; $\hbar$ INHERITED per dimensional-atlas Madelung** | Memo 03 §3 | G1 Galilean-from-primitives: Primitive 03 (spatial translations) + Primitive 13 (time translations) + non-rel scope (uniqueness of Galilean over Lorentzian boost algebra) + U2 unitarity + Galilean Lie algebra integration |
| **F5** Kinetic + potential decomposition $\hat{H} = T(\hat{p}) + V(\hat{x})$ | FORCED (within gauge-coupling-free scope) | Memo 02 §3 | Translation invariance (free part) + locality (potential part); cross terms forbidden by either symmetry |

**Net structural content:** all five sub-features established. The Hamiltonian form $\hat{H} = \hbar^2 |\hat{p}|^2 / (2m) + V(\hat{x})$ is uniquely determined within the stated scope conditions, with no new structural CANDIDATEs introduced.

---

## 3. Falsifier-Resolution Table

| Falsifier | Target sub-feature | Dispatch argument | Memo / section |
|---|---|---|---|
| **Fal-1** No momentum-basis identification | F1 | Stone's theorem applied to translation symmetry on the U2 Hilbert space gives a unique self-adjoint $\hat{p}$; channel-momentum identification follows from the eigenstate structure of $\hat{p}$. Direct transfer of U5 Memo 03 §1. | Memo 02 §1 |
| **Fal-2** Linear-in-$|\hat{p}|$ kinetic term | F3 | Vector $\alpha \cdot \hat{p}$ excluded by C2 rotation invariance. Scalar $|\hat{p}| c$ excluded by C3 analyticity (branch-point at $\hat{p} = 0$) plus C4 non-relativistic-limit (massless dispersion incompatible with massive non-relativistic regime). | Memo 03 §2.4 |
| **Fal-3** Higher-even-power terms | F3 | C4 non-relativistic-limit suppresses all $a_n |\hat{p}|^{2n}$ terms for $n \geq 2$ by powers of $(v/c)^{2(n-1)}$; vanish in strict $c \to \infty$ limit. | Memo 03 §2.5 |
| **Fal-4** Coefficient $\neq 1/(2m)$ — wrong factor | F4 | G1 Galilean-from-primitives: integration of the Galilean commutator condition $[\hat{H}, \hat{K}] = -i\hbar \hat{p}$ against $\hat{K} = m\hat{x} - t\hat{p}$ yields $T'(|\hat{p}|^2) = 1/(2m)$; the factor of 2 emerges as the integration Jacobian, not a convention. | Memo 03 §3.7 |
| **Fal-5** Anisotropic kinetic energy | F3 | C2 rotation invariance forces $T(\hat{p}) = f(|\hat{p}|^2)$; direction-dependent terms violate isotropy. | Memo 03 §2.3 |
| **Fal-6** Position-momentum cross terms in $\hat{H}$ | F5 | Translation invariance forbids $\hat{x}$ in free-particle Hamiltonian; locality forbids $\hat{p}$ in potential. Cross terms violate one or the other. (Within gauge-coupling-free scope; magnetic vector potentials produce $T(\hat{p} - eA(\hat{x})/c)$ which is downstream content.) | Memo 02 §3 |
| **Fal-7** Relativistic dispersion in non-rel regime | F3 | C4 non-relativistic-limit scope: relativistic $E = \sqrt{|\hat{p}|^2 c^2 + m^2 c^4} - mc^2$ Taylor-expands as $|\hat{p}|^2/(2m) - |\hat{p}|^4/(8m^3 c^2) + \ldots$, with all corrections vanishing in the strict $c \to \infty$ limit. Phase-2 Arc R is the relativistic domain. | Memo 03 §2.6 |

**All seven falsifiers dispatched.** No physical-distinction alternative survives within U4's stated scope conditions.

---

## 4. Conditionality Ledger

The U4 verdict is FORCED, conditional on the following — *all of which are inherited from prior structural commitments, not introduced by U4*:

### 4.1 U3 (sibling CANDIDATE; Framing 1)

U3 supplies the existence of a Hermitian Hamiltonian generator $\hat{H}$ in the participation-measure evolution equation $i\hbar \partial_t P_K = \hat{H} P_K + \sum V_{KK'} P_{K'}$. U4 specifies the *form* of $\hat{H}$ given that $\hat{H}$ exists. Promoting U3 in a subsequent arc would make U4 fully unconditional.

This is the natural sibling-CANDIDATE conditionality — methodologically novel for the structural-foundations cycle (U4 is the first arc whose verdict is naturally framed as conditional on a sibling CANDIDATE), but not a *new* upstream item: U3 was already in the active CANDIDATE inventory before U4 closed.

### 4.2 Non-relativistic-single-particle scope

Phase-1 Step 2's scope condition. Conditions:
- F3: suppresses higher-even-power terms ($a_n |\hat{p}|^{2n}$ for $n \geq 2$); rules out massless $|\hat{p}| c$ dispersion; rules out full relativistic $\sqrt{|\hat{p}|^2 c^2 + m^2 c^4}$.
- F4: selects Galilean boost structure over Lorentzian (absolute time preserved in the non-rel regime).

The non-rel scope is itself a regime choice, inherited from Phase-1 Step 2's framing, not derived within U4.

### 4.3 Gauge-coupling-free scope

F5's kinetic + potential decomposition $\hat{H} = T(\hat{p}) + V(\hat{x})$ holds in the absence of magnetic vector potentials. With gauge couplings, the kinetic operator becomes $T(\hat{p} - eA(\hat{x})/c)$ — coupling position and momentum via the gauge field $A$. Gauge field theory is downstream content (Phase-2 Arc R, QFT extension), not within Phase-1 Step 2's scope.

### 4.4 Inherited values

- **Mass $m$:** per Arc M's "form FORCED, values INHERITED" methodology. Arc M established that ED forces the *form* of mass structure but inherits all numerical mass values, ratios, and hierarchies. U4 inherits this framing for the mass parameter in the Hamiltonian.
- **$\hbar$:** inherited via the dimensional-atlas Madelung anchoring. The numerical value of $\hbar$ is not derived from primitives; it is the structural constant that emerges via the Madelung-form correspondence between the participation-measure evolution and standard quantum mechanics.

### 4.5 No new conditionalities introduced

**U4 introduces no new structural CANDIDATEs.** All four conditionalities listed above are inherited from prior structural commitments:
- U3 was in the active inventory before U4 opened.
- Non-rel scope was inherited from Phase-1 Step 2.
- Gauge-coupling-free scope was inherited from the same.
- Inherited values follow Arc M's and the dimensional atlas's prior commitments.

The methodological discipline of the structural-foundations cycle — *introduce zero new CANDIDATEs* — is preserved by U4.

---

## 5. Integration into the Structural-Foundations Program

### 5.1 The Phase-1 chain

With U4 closed, the Phase-1 Schrödinger-emergence chain reads:

```
Primitives 03, 04, 06, 07, 09, 13
                          |
                          v
                    U1 (FORCED) → P_K = √b · e^{iπ}
                          |
                          v
                    U2 (FORCED) → ⟨P|Q⟩ inner product
                          |
                          v
                    U5 (FORCED) → adjacency partition b = b_x + b_p
                          |
                          v
                    U4 (FORCED, this arc) → Ĥ = ℏ²|p|²/(2m) + V(x)
                          |
                          v
                    U3 (CANDIDATE, sole remaining) → iℏ ∂_t P = Ĥ P
                          |
                          v
                  Schrödinger emergence (Step 2)
                          |
                          v
            Born / Bell / Heisenberg / Schrödinger
                  (all four foundational postulates)
```

Schrödinger evolution is now FORCED *conditional on U3 alone*. All other structural inputs are in place: the participation-measure carrier (U1), the Hilbert-space structure (U2), the kinetic + potential Hamiltonian form (U4), the Fourier-conjugate adjacency partition supporting Heisenberg (U5), the Born rule (Theorem 10).

### 5.2 Updated active CANDIDATE inventory

| Pre-U4 | Post-U4 |
|---|---|
| {U3, U4} + continuum gauge | **{U3} + continuum gauge** |

**One upstream CANDIDATE remains.** Promoting U3 would close the entire QM-emergence Phase-1 structural-foundations program except for the description-level continuum gauge convention.

### 5.3 Updated FORCED theorem count

The structural-foundations cycle theorem inventory:

| # | Theorem | Arc | Status |
|---|---|---|---|
| 10 | Born rule (Gleason–Busch path) | born_gleason | FORCED |
| 11 | U2-Discrete (sesquilinear inner product on participation graph) | U2 | FORCED |
| 12 | U2-Continuum (continuum inner product, gauge-invariant form) | U2_continuum | FORCED |
| 13 | U5 (adjacency-band Fourier-conjugate partition) | U5 | FORCED |
| 14 | U1 (participation-measure construction) | U1 | FORCED |
| **15** | **U4 (specific Hamiltonian form, this arc)** | **U4** | **FORCED (form; values inherited)** |

**Six theorems in the structural-foundations cycle.** Combined with the nine forced theorems from the 2026-04-24 closure (spin-statistics, Cl(3,1), anyon prohibition, Dirac, GRH, canonical commutation, UV-FIN, V1 finite-width vacuum kernel, V1 with Synge world function), the total FORCED theorem inventory is now **15**.

### 5.4 Methodological observation

The structural-derivation methodology is now validated across **six substantively different structural questions**:

1. *born_gleason:* non-contextuality + Gleason–Busch admissibility.
2. *U2-Discrete:* linearity + sesquilinearity + specific aggregation form.
3. *U2-Continuum:* discrete-to-continuum lift with explicit conformal gauge.
4. *U5:* adjacency-band partition with negative-existence audit + Stone's-theorem-driven Fourier conjugacy.
5. *U1:* algebraic-structure question (Frobenius) + magnitude-exponent question (Cauchy).
6. *U4 (this arc):* specific Hamiltonian form via Galilean-Lie-algebra integration.

The pattern — **decompose CANDIDATE → identify automatic / forced-via-derivation / load-bearing sub-features → close load-bearing items via primitive-level + symmetry + scope arguments → introduce zero new CANDIDATEs → produce theorem-grade results** — has demonstrated robustness across the full diversity of Phase-1 structural questions. The remaining U3 arc is anticipated to follow the same pattern.

---

## 6. Public Explainer

*This section is intended for a scientifically literate but non-expert audience and is not part of the formal derivation.*

The Schrödinger equation is one of the most famous equations in physics. In its standard textbook form, it reads $i\hbar \partial_t \psi = \hat{H} \psi$, where $\hat{H}$ — the Hamiltonian operator — has the specific form $\hat{H} = -\hbar^2 \nabla^2 / (2m) + V(x)$. The first term, the *kinetic energy*, is proportional to the second derivative of the wavefunction with respect to position; the second term, the *potential energy*, depends on the position $x$ of the particle. Every quantum-mechanical calculation in every laboratory experiment for nearly a century has used this Hamiltonian form (or its relativistic and many-particle generalizations).

But sit with the form for a moment. *Why* is the kinetic term proportional to $|p|^2$ — squared momentum — rather than, say, $|p|$ or $|p|^3$? *Why* is the proportionality constant exactly $1/(2m)$ — the reciprocal of *twice* the mass — rather than $1/m$ or $1/(3m)$? Standard quantum mechanics doesn't ask. The Hamiltonian form is taken from classical mechanics ($T = p^2/(2m)$ in classical kinetic energy), promoted to operator status, and used. The factor of 2 in the denominator is borrowed from the classical formula without further justification.

The U4 arc of Event Density's structural-foundations program asks: where do these specific structural choices come from? The answer comes from two pieces of mathematics applied in sequence.

First, the *form* of the kinetic term — its squared dependence on momentum — is forced by the symmetries of space combined with a regularity assumption and the non-relativistic regime. Translation invariance (no preferred origin in space) forces the kinetic energy to be a function of momentum alone, not position. Rotation invariance (no preferred direction in space) forces it to depend only on the squared magnitude $|p|^2$, not on the direction. Analyticity at low momentum forces a Taylor expansion: the first non-trivial term is $|p|^2$, and higher-power terms ($|p|^4, |p|^6, \ldots$) appear in the relativistic regime as small corrections but vanish in the strict non-relativistic limit. So the kinetic-energy form is forced to be proportional to $|p|^2$.

Second, the *factor of 2* in $1/(2m)$ is forced by Galilean invariance — the symmetry that relates inertial observers in the non-relativistic regime. Specifically, when an observer moves with velocity $v$ relative to the original frame, the momentum operator transforms as $\hat{p} \to \hat{p} - mv$ (the moving observer sees a different momentum, shifted by $mv$). The Hamiltonian must transform consistently with this momentum shift. Working out the algebra of this consistency requirement — specifically, integrating the commutator condition that the Galilean Lie algebra demands — gives a differential equation for the kinetic-energy function, with unique solution $T = |p|^2/(2m)$. The factor of 2 emerges as the integration Jacobian, not as a convention. **It's not borrowed from classical mechanics; it's forced by the structure of how observers in different inertial frames see the same physics.**

This closes the structural backbone of the Schrödinger equation's Hamiltonian. Combined with the prior structural-foundations results — the participation-measure carrier (U1), the inner-product structure (U2), the Born rule (Theorem 10), and the adjacency-band partition supporting Heisenberg's uncertainty (U5) — the entire kinematic structure of non-relativistic quantum mechanics is now derived rather than postulated. One question remains open: why does the participation measure evolve in time according to a *first-order linear* equation $i\hbar \partial_t P = \hat{H} P$ in the first place? That's the U3 question, the natural and final foundational target of the Phase-1 program. With U4 closed, the structural foundations of standard non-relativistic quantum mechanics are within one arc of complete.

---

## 7. Memo-to-Theorem Mapping

| Memo | Sections | Structural results established |
|---|---|---|
| **Memo 00** (arc outline) | All | Arc scope, five sub-features, seven falsifiers, four-memo plan, Framing 1 (U4 conditional on U3), G1/G2/G3 framings for Galilean-invariance question |
| **Memo 01** (decomposition + circularity audit + transfer audit) | §1 | Sub-feature decomposition (F1–F5) restated in minimal falsifiable form |
| | §2 | Circularity audit per sub-feature; Framing 1 commitment; Galilean-invariance question identified as load-bearing |
| | §3 | Transfer audit of 2026-04-24 tightening memo: §§2.1–2.4 + §3 + §4 transfer cleanly; §2.5 silent factor-of-2 adoption identified as the precise gap |
| | §4 | Early classification: F1, F2, F5 forced-via-derivation/automatic; F3, F4 load-bearing |
| | §5 | Updated falsifier map; Fal-1 + Fal-6 anticipated dispatched in Memo 02; Fal-4 the substantive load-bearing falsifier |
| | §6 | Recommended Memo 02 structure |
| **Memo 02** (F1, F2, F5 derivations) | §1 | F1 established via Stone's-theorem transfer from U5 Memo 03 §1; explicitly U3-independent |
| | §2 | F2 established as automatic given F1; mathematical |
| | §3 | F5 established via translation invariance + locality, in gauge-coupling-free scope |
| | §4 | F3 setup: four constraints C1–C4 prepared for Memo 03 |
| | §5 | F4 setup: factor-of-2 question identified; G1 commitment |
| | §6 | Updated falsifier status; Fal-1 + Fal-6 dispatched, Fal-2 + Fal-5 partially dispatched |
| | §7 | Recommended Memo 03 structure |
| **Memo 03** (F3, F4, verdict) | §1 | State of arc entering Memo 03 |
| | §2 | F3 established via C1 + C2 + C3 + C4; Fal-2, Fal-3, Fal-5, Fal-7 dispatched |
| | §3 | F4 established under G1 Galilean-from-primitives via 6-step argument; **factor of 2 derived as integration Jacobian**; Fal-4 dispatched |
| | §4 | G2 fallback documented for completeness; G1 closure makes G2 unnecessary |
| | §5 | Final falsifier audit: all seven dispatched within stated scope |
| | §6 | **U4 verdict: FORCED with form-FORCED-value-INHERITED framing**; theorem statement; conditionality ledger |
| | §7 | Downstream cascade: Schrödinger emergence FORCED conditional on U3 alone; CANDIDATE inventory reduces to {U3} + gauge |

### 7.1 Final theorem-grade statement

> **Theorem 15 (U4; Specific Hamiltonian Form).** Let the ED primitive stack supply: bandwidth (Primitive 04), spatial structure (Primitive 06), participation relations (Primitive 03), channel index (Primitive 07), tension polarity (Primitive 09), and relational timing (Primitive 13), together with the now-FORCED upstream items U1, U2-Discrete, U2-Continuum, U5, and Theorem 10. Within the non-relativistic single-particle scope of Phase-1 Step 2 (gauge-coupling-free), and conditional on the existence of a Hermitian Hamiltonian generator (sibling CANDIDATE U3, Framing 1), the Hamiltonian operator on the participation-measure Hilbert space takes the unique form
>
> $$\hat{H} = \frac{\hbar^2 |\hat{p}|^2}{2m} + V(\hat{x})$$
>
> where: (1) the channel-momentum identification $K \leftrightarrow k$ in the thin/continuum limit follows from Stone's theorem on translation symmetry; (2) plane-wave eigenfunctions $\langle x | k \rangle = (2\pi\hbar)^{-d/2} e^{i k x / \hbar}$ supply the position-momentum basis change; (3) the kinetic + potential decomposition is forced by translation invariance + locality; (4) the quadratic-in-$|\hat{p}|^2$ structure is forced by C1 translation + C2 rotation + C3 analyticity + C4 non-relativistic-limit; (5) the specific coefficient $\hbar^2/(2m)$ — including the factor of 2 — is forced by integration of the Galilean commutator condition $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ against $\hat{K} = m\hat{x} - t\hat{p}$, with the factor of 2 emerging as the integration Jacobian rather than a convention; (6) the mass $m$ is inherited per Arc M, and $\hbar$ is inherited via the dimensional-atlas Madelung anchoring; (7) the form of the potential $V(\hat{x})$ is structural (scalar function of position), with the specific $V$ inherited from external physical context.

---

## 8. Recommended Next Steps

**(a) Open the U3 arc as the natural and final foundational target.** With U4 closed, U3 is the sole remaining active CANDIDATE in the QM-emergence Phase-1 program. U3 supplies the existence of a Hermitian Hamiltonian generator and the linear-first-order-in-time form of the participation-measure evolution equation. Anticipated arc structure: 4 memos (00 outline + 01 decomposition + 02 derivations + 03 verdict + optional 04 closure). Substantive content concentrated on (i) existence of a self-adjoint $\hat{H}$ via Stone's theorem applied to time-translation symmetry on the U2 Hilbert space (Primitive 13 supplies the time-axis kinematics; the argument parallels F1 of the present arc applied to spatial translations); (ii) linearity of the evolution equation; (iii) first-order-in-time character. Promoting U3 would close the entire QM-emergence Phase-1 structural-foundations program except for the description-level continuum gauge convention.

**(b) Draft the U4 publication paper as the fifth in the structural-foundations publication series.** With U4 closed, the structural-foundations cycle now has six theorem-grade results but only three publication papers (Born_Gleason 17pp, U2_Inner_Product 24pp, U1_Participation_Measure 20pp). U5 and U4 papers are publishable but not yet drafted. The U4 paper would document the specific-Hamiltonian-form derivation with the Galilean-invariance argument as its methodologically distinctive content (the factor-of-2 integration Jacobian story is the most distinctive structural finding of the U4 arc). Anticipated paper length: comparable to U5 / U1 papers (15–20 pages compiled). Convention work, not derivation work; can be scheduled per project priorities.

**(c) Update the structural-foundations ledger with U4 and updated CANDIDATE inventory.** The bundled memory-record update should capture: (i) Theorem 15 (U4) added to the FORCED-theorem inventory (now 15 total); (ii) active CANDIDATE inventory reduced from {U3, U4} + gauge to **{U3} + gauge**; (iii) new conditionality flags inheriting from Arc M (mass values), dimensional-atlas Madelung ($\hbar$), and the gauge-coupling-free scope; (iv) sibling-CANDIDATE conditionality methodology demonstrated (Framing 1) — a structurally novel pattern that may apply to future arcs derived in the presence of unclosed sibling CANDIDATEs. The MEMORY.md index line should be updated correspondingly. This is the same bundled-update discipline followed after prior arc closures.

**(d) Prepare the Phase-1 synthesis paper revision.** With U4 closed and only U3 remaining, the QM-emergence synthesis paper [`papers/QM_Emergence_Structural_Completion/`] is now substantively outdated (still claims "five upstream CANDIDATEs U1–U5" in §4, plus Born/Bell/Heisenberg framed as conditional). The paper's §§3.3 (Born), 3.4 (Bell/Tsirelson), 3.5 (Heisenberg), and §4 (CANDIDATE inventory) all need updating. After U3 closes, the synthesis paper should be revised in a single comprehensive editorial pass to reflect the completed Phase-1 structural-foundations program. The U4 closure is a natural moment to scope the synthesis revision but the substantive editing is best held until U3 is in hand. *Recommendation:* defer the synthesis revision until after U3 closure; document the deferred revision in the bundled memory-record update.

---

## 9. Cross-references

**Within the U4 arc:**
- [`00_arc_outline.md`](00_arc_outline.md) — arc scoping
- [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md) — sub-feature classification + circularity audit + transfer audit
- [`02_F1_F2_F5_derivations.md`](02_F1_F2_F5_derivations.md) — three forced-via-derivation sub-features
- [`03_F3_F4_and_verdict.md`](03_F3_F4_and_verdict.md) — load-bearing derivations + arc verdict

**Predecessor arcs (FORCED inputs):**
- [`arcs/born_gleason/`](../born_gleason/) — Theorem 10 (Born)
- [`arcs/U2/`](../U2/) — U2-Discrete
- [`arcs/U2_continuum/`](../U2_continuum/) — U2-Continuum
- [`arcs/U5/`](../U5/) — U5; particularly Memo 03 §1's Stone's-theorem template applied here in F1
- [`arcs/U1/`](../U1/) — U1

**Sibling CANDIDATE (the natural next foundational arc):**
- U3 (participation-measure evolution equation) — sole remaining active CANDIDATE.

**Predecessor tightening-program memo (audit target):**
- [`arcs/arc-foundations/u4_hamiltonian_form_derivation.md`](../arc-foundations/u4_hamiltonian_form_derivation.md) (2026-04-24) — superseded by present arc; §2.5's silent factor-of-2 adoption sharpened in Memo 03 §3 via G1 Galilean argument.

**Predecessor publication papers (templates for the U4 paper, when drafted):**
- [`papers/Born_Gleason/born_gleason_paper.md`](../../papers/Born_Gleason/born_gleason_paper.md)
- [`papers/U2_Inner_Product/paper_u2_inner_product.md`](../../papers/U2_Inner_Product/paper_u2_inner_product.md)
- [`papers/U1_Participation_Measure/paper_u1_participation_measure.md`](../../papers/U1_Participation_Measure/paper_u1_participation_measure.md)

**Source primitives (load-bearing for U4):**
- Primitive 03 (Participation, supplies homogeneity for translation symmetry): `quantum/primitives/03_participation.md`
- Primitive 04 (Bandwidth, supplies $|P|^2 = b$ via U1): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 06 (ED Gradient, supplies spatial axis): `quantum/primitives/06_ed_gradient.md`
- Primitive 09 (Tension Polarity): `quantum/primitives/09_tension_polarity.md`
- Primitive 13 (Relational Timing, supplies time-axis for Galilean argument): `quantum/primitives/13_relational_timing.md`

**Arc M (mass-parameter inheritance):**
- `papers/Arc_M/paper_arc_m.md` — "form FORCED, values INHERITED" framing.

**Mathematical references:**
- Stone's theorem: M. H. Stone, "On one-parameter unitary groups in Hilbert space," *Annals of Mathematics* **33**, 643–648 (1932).
- Galilean Lie algebra and central extension: V. Bargmann, "On unitary ray representations of continuous groups," *Annals of Mathematics* **59**, 1–46 (1954).

**Project memory:** `memory/project_qm_emergence_arc.md`

**Public-facing companions on desktop (in same explainer series):**
- `C:\Users\allen\Desktop\ED_Exponent2_Explainer.md`
- `C:\Users\allen\Desktop\ED_Born_Gleason_Explainer.md`
- `C:\Users\allen\Desktop\ED_U2_Inner_Product_Explainer.md`
- `C:\Users\allen\Desktop\ED_U1_Participation_Measure_Explainer.md`
- *(Potential)* `ED_U4_Hamiltonian_Form_Explainer.md` — natural fifth in the series, focusing on the factor-of-2 integration Jacobian story.

---

## 10. One-line memo summary

> **U4 arc closed. The specific Hamiltonian form $\hat{H} = \hbar^2 |\hat{p}|^2/(2m) + V(\hat{x})$ is FORCED at the form level, with values inherited (mass per Arc M, $\hbar$ per dimensional-atlas Madelung). All five sub-features established (F1 channel-momentum identification via Stone's theorem; F2 plane-wave eigenfunctions automatic; F3 quadratic-in-$|\hat{p}|^2$ via four constraints C1–C4; F4 coefficient $1/(2m)$ via G1 Galilean-from-primitives, with **the factor of 2 forced by integrating the Galilean commutator condition $[\hat{H}, \hat{K}] = -i\hbar \hat{p}$** rather than borrowed by convention; F5 kinetic + potential decomposition via translation invariance + locality). All seven falsifiers dispatched. Conditionalities all inherited (U3 sibling CANDIDATE, non-rel scope, gauge-coupling-free scope, mass values, $\hbar$); zero new structural CANDIDATEs introduced. Active upstream-CANDIDATE inventory reduces from {U3, U4} + gauge to **{U3} + continuum gauge** — one upstream item remains to close the entire QM-emergence Phase-1 structural-foundations program. Theorem inventory: 15 (was 14). Six-arc structural-foundations cycle (born_gleason → U2-D → U2-C → U5 → U1 → U4) demonstrates the structural-derivation methodology against six substantively different structural questions; U3 is the natural and final foundational target.**

---

**Arc Closed.**
