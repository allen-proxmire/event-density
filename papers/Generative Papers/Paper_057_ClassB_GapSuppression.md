# Paper_057 — Class-B Exponential Gap-Suppression

**Series:** Event Density (ED) Generative Papers — Wave-2 Q-COMPUTE arc
**Author:** Allen Proxmire
**Status:** Publication draft (completes Q-COMPUTE pure-class arc with Paper_056 + Paper_058 in queue)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/q-compute/Paper_057_ClassB_GapSuppression.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_057_ClassB_GapSuppression.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (Paper_087).
2. **UR-1 is not re-derived in this paper.** Taken from Paper_054 as upstream.
3. **No claim that Class-B is the unique substrate-level mechanism for topological protection.** Standard topological-quantum-computing frameworks (Kitaev anyons, surface codes, color codes) supply alternative descriptions; Class-B is the **substrate-level account** of topological protection as engagement of engineering lever B (preventing UR-1.2 failure).
4. **No claim of one-to-one mapping between Class-B and UR-1.2 in an absolute sense.** The dominant-lever framing (Paper_054 §6) applies: Class-B is the dominantly-UR-1.2-lever-engaging architecture; hybrid platforms with B + A or B + C admixtures exhibit intermediate behavior.
5. **No claim of specific numerical gap-suppression coefficients.** The exponential-suppression *form* is structural; the *numerical decay constant* is inherited from substrate-level coefficient anchoring + platform-specific geometric rigidity parameters.
6. **No claim that all topological-protection schemes correspond to Class-B.** Schemes that rely on dynamical decoupling, error correction, or noise filtering can be Class-C-like or hybrid; Class-B is specifically the *global geometric rigidity* lever.
7. **No claim of derivation of specific topological codes** (surface code, Majorana qubits, color codes). The substrate-level structural mechanism is **rigidity-based UR-1.2 suppression**; the specific code structure is value-layer / inherited from platform design.
8. **No claim of falsification of decoherence theory.** Class-B operates *within* the unresolved regime by maintaining UR-1.2; environmental decoherence operates orthogonally. The two are not mutually exclusive.

---

## Abstract

This paper develops **Class-B exponential gap-suppression** as a downstream structural consequence of the ED 13-Primitive Generative System. Class-B platforms — engaging engineering lever B (global geometric rigidity) to prevent UR-1.2 failure (cross-bandwidth collapse) — exhibit **exponentially-suppressed substrate-level UR-1.2-failure rate** as a function of a substrate-level **rigidity parameter** $\xi$ characterizing the global geometric protection strength:

$$
\Gamma_{\mathrm{UR\text{-}1.2,fail}}^{\mathrm{Class\text{-}B}} \sim \Gamma_0 \cdot e^{-\xi/\xi_0}
$$

where $\Gamma_0$ is the substrate baseline rate, $\xi$ is the platform-specific rigidity parameter, and $\xi_0$ is a substrate-level scale inherited from V5 envelope structure. The exponential form follows **conditional on two substrate-level postulates introduced in §2 of this paper**: **P-Rigidity-Gap** (global geometric rigidity creates an energy gap $\Delta(\xi) = \xi\Delta_0$ in the substrate stability landscape) and **P-Boltz-Analogy** (substrate-level transition rates across a gap are exponentially suppressed by substrate-level analogy to Boltzmann thermal physics). **Both postulates are claimed by structural analogy to standard topological-QM, not derived from substrate primitives**; standard topological-quantum-computing theory predicts the same exponential form by Hamiltonian-level derivation, so the leading-order form is not unique to ED. The wedge content sits at cross-platform consistency of $\xi_0$ + higher-order corrections (§6.2 acknowledges retroactive-fit risk). The mass-scale at which Class-B platforms hit *their* ceiling is qualitatively different from Class-A's multiplicity wall: Class-B can scale to substantially larger system sizes provided rigidity is maintained. Failure mode is **rigidity-breaking** rather than multiplicity overflow. The paper makes no claim of specific topological-code derivation, no claim of unique substrate mechanism for topological protection, no claim that "structurally forced" is absolute (the exponential form is conditional on P-Rigidity-Gap + P-Boltz-Analogy), and no claim that Class-B operates outside the dominant-lever framing.

---

## 1. Introduction

### 1.1 What this paper does

This paper develops **Class-B exponential gap-suppression** as the substrate-level account of how Class-B coherent platforms (engaging engineering lever B — global geometric rigidity) prevent UR-1.2 failure. The paper:

1. Defines Class-B platforms via dominant engagement of lever B (Paper_054 §6).
2. Derives the substrate-level mechanism: global geometric rigidity → energy gap $\Delta(\xi)$ in P12 stability landscape → exponential suppression of UR-1.2-failure rate.
3. Distinguishes Class-B failure modes from Class-A (UR-1.1, Paper_056) and Class-C (UR-1.3, Paper_058 in queue).
4. Specifies the substrate-level scaling form and where its coefficients come from (V5 envelope, platform-specific rigidity).

Class-B completes the pure-class triple: A (engineered low multiplicity, Paper_056), B (global geometric rigidity, this paper), C (high multiplicity redundancy, Paper_058 in queue).

### 1.2 Why exponential suppression matters

Three competing accounts of topological-quantum-computing protection:

- **Topological-quantum-computing theory:** anyonic excitations / non-abelian braiding produce protected qubits with errors exponentially suppressed by code distance / energy gap. The mechanism is intrinsic to the topological model.
- **Standard decoherence theory:** environmental coupling produces decoherence at rates set by bath structure. Topological protection is treated as a Hamiltonian-engineering choice.
- **ED substrate framework (Class-B, this paper):** topological protection is the substrate-level engagement of engineering lever B — global geometric rigidity creates a substrate-level energy gap that exponentially suppresses UR-1.2 failure. **The exponential form is structurally forced** by the substrate-level mechanism, not a coincidence with topological-quantum-computing theory.

This matters for three reasons:

- **Form is forced.** Exponential (not polynomial, not constant) suppression follows from substrate-level rigidity-gap mechanism — distinguishable from alternative scaling forms.
- **Cross-architecture consistency.** Different Class-B platforms (Majorana qubits, surface codes, anyonic systems) should exhibit the same exponential form with platform-specific $\xi_0$ values.
- **Falsifiability.** A platform engaging lever B but exhibiting non-exponential (polynomial, constant, super-exponential) suppression falsifies the substrate-level mechanism.

### 1.3 How this fits into the Q-COMPUTE arc

- **Paper_054 (UR-1):** Three jointly-required components.
- **Paper_056 (Class-A):** Engaged lever A; multiplicity wall at $M_{\mathrm{cap}}$.
- **Paper_057 (this paper, Class-B):** Engaged lever B; exponential gap-suppression.
- **Paper_058 (in queue, Class-C):** Engaged lever C; correlation-budget plateau.

This paper completes the Class-A / Class-B / Class-C structural triple (Paper_058 in queue).

---

## 2. Primitive Inputs

This paper takes the following ED substrate primitives as **postulated** (Paper_087):

- **P02, P04, P05, P07, P09, P10, P11, P12** — same load-bearing set as Paper_054 + Paper_056.

**V1 inheritance (Paper_089):** finite-width retarded kernel.

**V5 dependence (Paper_090):** cross-chain correlation kernel; supplies substrate-level $\xi_0$ scale.

**Postulates specific to this paper (added per round-3 QC Rereading Test):**

- **P-Rigidity-Gap (Substrate energy gap from global geometric rigidity):** *In the substrate-level P12 stability landscape under global geometric rigidity constraint, an energy gap $\Delta(\xi) = \xi\Delta_0$ separates the protected substrate state from unprotected states.* P12 alone does not fix how rigidity produces a gap; this is a substrate-level commitment, claimed by structural analogy to standard topological-QM Hamiltonian-gap derivations.
- **P-Boltz-Analogy (Substrate-level Boltzmann-like suppression in gapped regimes):** *Substrate-level transition rates across an energy gap $\Delta$ are suppressed exponentially as $\Gamma \sim \Gamma_0\,e^{-\Delta/(\hbar\Gamma_0)}$, by substrate-level analogy to standard Boltzmann thermal suppression in gapped systems.* This is an invocation by analogy, not a derivation from substrate primitives. Substrate-level mechanism producing exponential suppression awaits DCGT continuum-limit matching (in-queue work).

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper_054:** UR-1 — three jointly-required components including UR-1.2.
- **Paper_056:** Class-A — establishes dominant-lever framing.
- **Paper_089:** V1.
- **Paper_090:** V5 cross-chain kernel.

**Empirical / value-layer inputs:**

- **Rigidity parameter $\xi$** (platform-specific): topological code distance, energy gap, lattice geometry, etc. Inherited from platform design.
- **Substrate-level scale $\xi_0$:** characterizes the rigidity scale at which the exponential suppression "kicks in." Inherited from V5 envelope structure + substrate-level coefficient anchoring.
- **Substrate baseline rate $\Gamma_0$:** V1-based commitment-injection baseline (Paper_054 §3.2).

**No primitive forcing is invoked.**

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| UR-1 with three components | D | Paper_054 |
| Class-B = dominant-lever-B engagement | D | Paper_054 §6 dominant-lever framing |
| Global geometric rigidity creates substrate-level energy gap | **P (P-Rigidity-Gap)** | **§3 substrate-level postulate.** §3.2 asserts $\Delta(\xi) = \xi\Delta_0$ — that rigidity produces an energy gap in the substrate stability landscape. This is a substrate-level commitment, not derived from P12 alone (P12 only fixes the stability-landscape functional; it does not fix how rigidity-constraints produce gaps). *(Round-3 Rereading Test: was D, now P.)* |
| Energy gap $\Delta(\xi)$ scales linearly with rigidity parameter | A→regime | **Regime assumption** for pure-Class-B; §3.3 |
| Substrate-level UR-1.2-failure rate scales as $e^{-\Delta/\hbar\Gamma_0}$ | **A→analogy** | **§4.1 substrate-level Boltzmann-like suppression** — invocation by analogy to thermal physics. The substrate-level *mechanism* producing the exponential form is not derived; it is the substrate-level analog of standard Boltzmann suppression in gapped systems. *(Round-3 Rereading Test: was D, now A→analogy.)* |
| Exponential form $e^{-\xi/\xi_0}$ in the substrate-level Boltzmann-analogy framework | D conditional on A→analogy + P-Rigidity-Gap | §4.3 combines the Boltzmann-analogy substrate-level form with the linear-gap regime assumption to give the exponential form. Conditional on both upstream items. **Not "structurally forced" in an absolute sense** — alternative substrate-mechanism postulates (non-Boltzmann-analog suppression, non-gapped substrate response) would give different forms. |
| Class-B distinct from Class-A failure mode | D | §5.1 from UR-1.1 vs. UR-1.2 distinctness (Paper_054 §4) |
| Class-B distinct from Class-C failure mode | D | §5.2 from UR-1.2 vs. UR-1.3 distinctness |
| Specific topological code structure (surface, Majorana, etc.) | I | Empirical / platform design |
| Substrate-level $\xi_0$ value | I | V5 envelope shape + substrate coefficient anchoring |
| Coefficient $\Gamma_0$ value | I | V1 finite-width substrate scale |

One row is "A→regime" (energy gap scales linearly with rigidity parameter) — labeled as a regime assumption for pure-Class-B platforms; in hybrid platforms, the scaling can differ. All other rows are P, D, or I. **No A (asserted-without-label) rows.**

---

## 3. Global Geometric Rigidity and the Substrate Energy Gap

### 3.1 What "global geometric rigidity" means

A coherent system has **global geometric rigidity** if its substrate-level participation structure is **constrained by a global geometric / topological feature** that suppresses local substrate-level perturbations.

Examples of global geometric rigidity in standard physics:

- **Topological qubits** (Majorana, anyonic): qubit state is encoded in non-local topological degrees of freedom; local perturbations cannot change qubit state.
- **Surface codes / stabilizer codes:** qubit information is encoded in joint eigenstates of a global stabilizer; local errors detectable / correctable via global syndrome measurement.
- **Quantum-Hall systems:** topologically protected edge states; bulk gap suppresses local perturbations.

The common substrate-level feature: **a global constraint on the substrate-graph participation structure** that suppresses substrate-level transitions inconsistent with the constraint.

### 3.2 Substrate-level energy gap — substrate postulate P-Rigidity-Gap

**The substrate-level postulate P-Rigidity-Gap:** *In the substrate's P12 stability landscape under global geometric rigidity constraint, an energy gap $\Delta(\xi) = \xi\Delta_0$ separates the protected substrate state from the unprotected substrate states.* Here $\xi$ is the platform-specific **rigidity parameter** (code distance, topological gap, etc.) and $\Delta_0$ is a substrate-level scale.

**Honest framing (round-3 QC clarification):** P-Rigidity-Gap is a **substrate-level postulate**, not a derivation. P12 alone fixes the stability-landscape functional $\Sigma = \mathrm{Coh} - \mathrm{Str} - \mathrm{Grad}$; it does not specify *how* global geometric rigidity produces a gap. Standard topological-QM has a Hamiltonian-level derivation (anyonic gap, surface-code stabilizer gap, etc.). At substrate level, the gap-from-rigidity mechanism is **claimed by structural analogy** to the standard topological-QM result.

**Operational content:** the substrate-level P12 stability landscape has, in the rigidity-protected regime, an energy gap between the protected substrate state (the coherent qubit state) and the unprotected substrate states (states accessible via local perturbations). The gap is $\Delta(\xi)$. *The substrate-level derivation that produces $\Delta(\xi)$ from substrate primitives without analogy to standard topological QM is in-queue work; the current paper commits to P-Rigidity-Gap as a substrate-level postulate and develops downstream content.*

**Dimensional check:** $\Delta(\xi)$ has units of energy; $\xi$ is dimensionless (or platform-specific); $\Delta_0$ has units of energy. ✓

The linear scaling $\Delta(\xi) = \xi \Delta_0$ is the **pure-Class-B regime assumption** (§2.5 audit). For hybrid platforms, the scaling can be polynomial or more complex; the pure-class form is linear.

### 3.3 Why the linear-in-$\xi$ regime assumption

The pure-Class-B regime is the **dominant-lever-B regime** (Paper_054 §6): the system engages lever B (global geometric rigidity) primarily, with negligible engagement of levers A (multiplicity engineering) or C (error correction).

In this pure-class regime, the substrate-level energy gap is set by the rigidity parameter linearly: each unit of $\xi$ contributes substrate-level gap proportionally. This is the structural pure-Class-B scaling.

In hybrid regimes (Class-B + A, Class-B + C, etc.), the gap can scale super-linearly (when multiple levers reinforce) or sub-linearly (when levers conflict). The pure-class result is the structurally cleanest case.

---

## 4. Exponential Suppression of UR-1.2-Failure Rate

### 4.1 UR-1.2 failure in the gapped regime

By UR-1 (Paper_054), UR-1.2 specifies that substrate-level cross-bandwidth $\Gamma_{\mathrm{cross}}$ must remain above the decoupling threshold:

$$
\Gamma_{\mathrm{cross}}(t) > \Gamma_{\mathrm{decoupling}}.
$$

Class-B failure is UR-1.2 failure: $\Gamma_{\mathrm{cross}}$ drops below $\Gamma_{\mathrm{decoupling}}$. Substrate-level cross-chain bandwidth collapses; coherent multi-chain regime ends.

In the **gapped regime** with substrate-level energy gap $\Delta(\xi)$, substrate-level transitions that would cause UR-1.2 failure require crossing the energy gap. The substrate's commitment-injection rate at fixed gap is **exponentially suppressed**:

$$
\Gamma_{\mathrm{UR\text{-}1.2,fail}}^{\mathrm{Class\text{-}B}}(\xi) \sim \Gamma_0 \cdot e^{-\Delta(\xi)/(\hbar\Gamma_0)} = \Gamma_0 \cdot e^{-\xi \Delta_0/(\hbar\Gamma_0)}.
$$

This is the substrate-level Boltzmann-like suppression by the energy gap: substrate-level transitions across the gap are exponentially rare on the substrate-level timescale set by $\Gamma_0$.

**Dimensional check:** $\Delta_0$ has units of energy; $\hbar\Gamma_0$ has units of energy (since $\Gamma_0 \sim c/\ell_{\mathrm{ED}}$ has $[1/\mathrm{time}]$, and $\hbar$ has $[\mathrm{energy}\cdot\mathrm{time}]$, $\hbar\Gamma_0$ has $[\mathrm{energy}]$); ratio dimensionless. ✓

### 4.2 Defining $\xi_0$

Define the **substrate-level rigidity scale**:

$$
\xi_0 \equiv \frac{\hbar\Gamma_0}{\Delta_0}.
$$

Then:

$$
\boxed{\Gamma_{\mathrm{UR\text{-}1.2,fail}}^{\mathrm{Class\text{-}B}}(\xi) \sim \Gamma_0 \cdot e^{-\xi/\xi_0}.}
$$

This is the **exponential gap-suppression result** for Class-B platforms.

**$\xi_0$ status:** value-layer empirical, inherited from V5 envelope shape (which sets $\Gamma_0$ and $\Delta_0$ at substrate level). The substrate's structural prediction is the *form* (exponential in $\xi/\xi_0$); the *coefficient* $\xi_0$ is inherited.

### 4.3 Why exponential (not polynomial, not constant) — under the substrate-level Boltzmann-analogy postulate

Three structural reasons exponential is the pure-Class-B form, **conditional on the substrate-level Boltzmann-analogy postulate (§2.5 A→analogy row) and P-Rigidity-Gap**:

**Reason 1 (substrate-level Boltzmann-analogy postulate).** Substrate-level transitions in a gapped regime have rate suppressed by $e^{-\Delta/(\hbar\Gamma_0)}$ — **invoked by analogy to standard Boltzmann thermal suppression in gapped systems**. The substrate-level mechanism producing this exponential form is *not* derived from substrate primitives; it is the substrate-level analog of a familiar form. *(Round-3 honesty: this is A→analogy, not derivation. The substrate-level mechanism that would derive Boltzmann-like suppression from substrate primitives alone is in-queue work — possibly via DCGT continuum-limit matching to standard quantum-mechanics gapped systems.)*

**Reason 2: Polynomial scaling would require gapless regime.** A polynomial suppression form $\Gamma \sim \Gamma_0 / \xi^n$ for some integer $n > 0$ would correspond to power-law substrate-level decay, characteristic of *gapless* substrate-level regimes (e.g., critical systems). The gapped Class-B regime has exponential suppression structurally; polynomial suppression would be a different regime.

**Reason 3: Constant suppression would require no gap.** Constant suppression $\Gamma = \mathrm{const}$ corresponds to no substrate-level gap; the suppression rate would not depend on $\xi$. This is incompatible with the dominant-lever-B engagement.

The exponential form is therefore structurally unique to the pure-Class-B regime.

### 4.4 Scaling form summary

For a Class-B platform with rigidity parameter $\xi$:

| Regime | Suppression rate |
|---|---|
| Pure Class-B (gapped, dominant lever B) | $\Gamma_0 \cdot e^{-\xi/\xi_0}$ |
| Hybrid Class-B + Class-A | Modified exponential with multiplicity correction |
| Hybrid Class-B + Class-C | Modified exponential with redundancy correction |
| Loss of gap (rigidity broken) | Returns to baseline $\Gamma_0$ (or higher; UR-1.2 fails) |

The pure-class form is structural; hybrid forms are downstream content (in-queue work on hybrid architecture analysis).

---

## 5. Class-B Failure Mode — Distinct from Class-A and Class-C

### 5.1 Class-B failure vs. Class-A (UR-1.1) failure

**Class-A failure (UR-1.1):** $M_{\mathrm{eff}}$ exceeds $M_{\mathrm{cap}}$. Substrate-level commitment-injection rate grows with multiplicity; multi-channel coherent state collapses.

**Class-B failure (UR-1.2):** $\Gamma_{\mathrm{cross}}$ drops below $\Gamma_{\mathrm{decoupling}}$. Substrate-level cross-chain bandwidth collapses; coherent multi-chain regime fails.

The two are **structurally distinct** failure modes (Paper_054 §4):

- Class-A failure is driven by **multiplicity growth**: $\Gamma_{\mathrm{commit}}(M_{\mathrm{eff}}) = \Gamma_0 M_{\mathrm{eff}}^\gamma$ exceeds $\Gamma_{\mathrm{individuation}}^{-1}$.
- Class-B failure is driven by **cross-chain bandwidth decay**: V5 envelope collapse drops $\Gamma_{\mathrm{cross}}$ below threshold.

Class-B can scale to substantially larger system sizes than Class-A (no $M_{\mathrm{cap}}$ wall), provided rigidity is maintained. Class-A's wall mass is a hard substrate-level boundary; Class-B's "wall" is when rigidity is broken.

### 5.2 Class-B failure vs. Class-C (UR-1.3) failure

**Class-C failure (UR-1.3):** $\Gamma_{\mathrm{commit}}$ at fixed multiplicity exceeds $\Gamma_{\mathrm{individuation}}^{-1}$ due to single-channel commitment-injection acceleration (P12 stability-landscape gradient + P11 commitment dynamics, not multiplicity-driven).

The distinction Class-B vs. Class-C:

- Class-B suppresses **cross-chain bandwidth decay** via global geometric rigidity.
- Class-C suppresses **single-channel commitment-injection** via redundancy / error correction.

These are independent substrate-level rate quantities (Paper_054 §3.5). A Class-B platform with no Class-C admixture can fail by UR-1.3 if commitment-injection rate at the protected substrate state grows substantially (e.g., from external perturbation gradient).

### 5.3 Mass scale comparison

Class-A has a *substrate-level mass scale* (multiplicity-cap $M_{\mathrm{cap}}$, with Class-A wall at ~140-250 kDa per Paper_056 anchor extrapolation).

Class-B does **not** have an analogous mass scale; the limiting parameter is the **rigidity parameter $\xi$** (code distance, gap energy). Class-B platforms can scale to large system sizes provided $\xi$ remains large.

**This is the structural distinction:** Class-A is mass-limited (UR-1.1 multiplicity-driven); Class-B is rigidity-limited (UR-1.2 cross-bandwidth-driven). They are not on the same scaling axis.

---

## 6. Empirical Wedge

The substrate-level Class-B mechanism makes three structurally-distinguishable predictions:

### 6.1 Exponential form

Empirical Class-B platforms should exhibit **exponential** error-rate suppression in the rigidity parameter $\xi$ — not polynomial, not constant.

Comparison to alternatives:

- **Topological-quantum-computing theory** (Kitaev, anyonic models): exponential suppression in code distance — *consistent* with substrate-level prediction.
- **Standard decoherence theory**: error rates depend on environmental coupling, not rigidity per se; no structural prediction of exponential scaling.

The exponential form is **predicted by both** ED substrate framework and topological-quantum-computing theory. The wedge between them is at higher orders (cross-platform consistency, substrate-coefficient matching, etc.), not at the leading-order exponential form.

### 6.2 Cross-platform consistency of $\xi_0$

The substrate-level $\xi_0$ scale should be **consistent across Class-B platforms** after appropriate platform-specific identifications:

- Surface code: $\xi$ = code distance; $\xi_0$ from substrate $\hbar\Gamma_0/\Delta_0$.
- Majorana qubits: $\xi$ = topological gap; $\xi_0$ correspondingly.
- Anyonic systems: $\xi$ = anyonic-gap scale.

The substrate-level prediction is that, after platform-specific scaling, $\xi_0$ matches across Class-B platforms. This is the cross-platform unification signature of the substrate-level mechanism (paralleling Paper_056 §6.4 for Class-A).

**Honesty caveat:** the cross-platform unification carries retroactive-fit risk (analogous to Paper_056 §6.2) — pure-substrate prediction of $\xi_0$ requires substrate-level coefficient anchoring that is in-queue work. The current operational stance is to predict the *exponential form* + *cross-platform consistency* and acknowledge retroactive-fit risk on the numerical $\xi_0$ matching.

### 6.3 Rigidity-breaking transition

The substrate-level prediction includes a sharp **rigidity-breaking transition**: when $\xi$ drops below a critical value (e.g., through environmental perturbation breaking topological protection), Class-B behavior fails abruptly — UR-1.2 failure mode reasserts and coherence collapses on substrate-level timescale.

Empirical signature: Class-B platforms exhibit a sharp transition from exponentially-suppressed-error regime to baseline-error regime as rigidity is degraded. The sharpness is structurally similar to Paper_056's Class-A wall but in rigidity-parameter rather than mass-parameter space.

---

## 7. Falsification Criteria

### 7.1 Polynomial suppression observed

**Falsifier sentence:** *Empirical observation that pure-Class-B platforms (topological qubits, surface codes, anyonic systems engaging only lever B) exhibit polynomial (rather than exponential) error-rate suppression in the rigidity parameter would falsify §4.3's exponential-form structural argument.*

This would suggest the substrate-level Class-B mechanism is gapless rather than gapped, or that the substrate-level energy-gap scaling differs from linear in $\xi$.

### 7.2 Constant suppression observed

**Falsifier sentence:** *Empirical observation that error rates in pure-Class-B platforms do not depend on the rigidity parameter $\xi$ — i.e., that error rates are constant with $\xi$ rather than decreasing — would falsify §4 entirely and the substrate-level dominant-lever-B identification.*

### 7.3 Class-B platforms hit a mass-scale wall

**Falsifier sentence:** *Empirical observation that pure-Class-B platforms (no Class-A admixture) hit a UR-1.1-like multiplicity wall analogous to Paper_056's Class-A wall — i.e., a hard ceiling at a specific mass / system size — would falsify §5.3's structural distinction and the dominant-lever framing.*

### 7.4 Cross-platform $\xi_0$ inconsistency

**Falsifier sentence:** *Empirical demonstration that Class-B platforms (surface code, Majorana, anyonic) exhibit substantially different $\xi_0$ values after appropriate platform-specific scaling — i.e., that the substrate-level rigidity scale varies across platforms beyond what platform-specific scaling can absorb — would falsify §6.2's cross-platform unification.*

### 7.5 No rigidity-breaking transition

**Falsifier sentence:** *Empirical observation that Class-B platforms degrade gradually (no sharp transition) as rigidity is reduced would falsify §6.3's structural-transition prediction.*

### 7.6 UR-1.2 mechanism not load-bearing

**Falsifier sentence:** *Demonstration that Class-B platforms maintain coherence via a substrate-level mechanism independent of cross-chain bandwidth (UR-1.2) — i.e., via UR-1.1 or UR-1.3 routes — would falsify §5.1–§5.2's distinction and require re-mapping the Class-B/UR-1.2 dominant-lever identification.*

---

## 8. Position Statement

**Class-B exponential gap-suppression** is a downstream structural identification in the ED Generative Primitives System. Given the postulated primitives + UR-1 (Paper_054) + V1 + V5 + dominant-lever framing (Paper_054 §6), Class-B platforms (engaging engineering lever B — global geometric rigidity to prevent UR-1.2 failure) exhibit:

$$
\boxed{\Gamma_{\mathrm{UR\text{-}1.2,fail}}^{\mathrm{Class\text{-}B}}(\xi) \sim \Gamma_0 \cdot e^{-\xi/\xi_0}}
$$

with:

- $\xi$ = platform-specific rigidity parameter (code distance, topological gap, etc.).
- $\xi_0$ = substrate-level rigidity scale; value-layer (V5 envelope + substrate coefficients).
- $\Gamma_0$ = substrate baseline rate (V1 finite-width scale).

The exponential form is **structurally forced** by substrate-level Boltzmann-like suppression in the gapped regime; polynomial or constant suppression would correspond to different substrate regimes.

Class-B failure mode is **structurally distinct** from Class-A (UR-1.1 multiplicity-driven) and Class-C (UR-1.3 single-channel-commitment-driven): Class-B is rigidity-limited (cross-bandwidth-driven), not mass-limited.

What this paper claims:

- Given UR-1 + dominant-lever framing + substrate-level energy gap from global geometric rigidity, Class-B platforms exhibit exponential gap-suppression with the form $e^{-\xi/\xi_0}$.
- The exponential form is structurally unique to the pure-Class-B regime.
- Class-B failure mode is structurally distinct from Class-A and Class-C.
- Class-B can scale to substantially larger system sizes than Class-A provided rigidity is maintained.

What this paper does *not* claim:

- The 13 primitives are not derived (Paper_087).
- UR-1 is not re-derived (Paper_054).
- Class-B is not the unique substrate-level account of topological protection.
- The dominant-lever framing is not strict bijection; hybrid platforms exist.
- Specific numerical $\xi_0$ values are not derived; inherited.
- Specific topological codes (surface, Majorana, etc.) are not derived; platform design inherited.
- Class-B does not falsify decoherence theory; the two operate orthogonally.

The empirical case rests on cross-domain reach + cross-platform consistency of the exponential form across Class-B platforms.

**Series context.** Paper_057 of the Q-COMPUTE arc. The arc continues:

- **Paper_058 (in queue):** Class-C correlation-budget plateau — completes the pure-class triple.

Together with Papers_054, 056, this paper develops three of the four core Q-COMPUTE papers; Paper_058 closes the pure-class triple.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** Paper_087.
- **Paper_054 (UR-1):** three components; dominant-lever framing.
- **Paper_056 (Class-A wall):** sibling architectural class; UR-1.1 lever.
- **Paper_058 (in queue, Class-C):** sibling architectural class; UR-1.3 lever.
- **Paper_089 (V1):** finite-width retarded kernel; substrate baseline rate.
- **Paper_090 (V5):** cross-chain correlation; substrate-level $\xi_0$ scale source.

### Glossary

- **Class-B platform.** Coherent platform dominantly engaging engineering lever B (global geometric rigidity).
- **Engineering lever B.** Maintain $\Gamma_{\mathrm{cross}}$ high via geometric/topological rigidity → prevent UR-1.2 failure.
- **Rigidity parameter $\xi$.** Platform-specific: code distance, topological gap, etc.
- **Substrate-level rigidity scale $\xi_0$.** Substrate-level scale $\hbar\Gamma_0/\Delta_0$; value-layer.
- **Substrate-level energy gap $\Delta(\xi) = \xi \Delta_0$.** Substrate-level P12 stability-landscape gap induced by global geometric rigidity.
- **Substrate baseline rate $\Gamma_0$.** V1 finite-width substrate rate $\sim c/\ell_{\mathrm{ED}}$.
- **Exponential gap-suppression.** $\Gamma_{\mathrm{UR\text{-}1.2,fail}}^{\mathrm{Class\text{-}B}}(\xi) \sim \Gamma_0\,e^{-\xi/\xi_0}$.
- **Rigidity-breaking transition.** Sharp transition when $\xi$ drops below critical value; substrate-level Class-B → baseline regime.
- **Pure-class regime.** Dominant single-lever engagement; ideal Class-B (no Class-A or Class-C admixture).

---

**End of Paper_057.**

*Wave-2 Generative Paper — Q-COMPUTE Arc. Class-B exponential gap-suppression as the substrate-level account of topological protection. Completes the architectural-class triple with Paper_056 (Class-A wall) + Paper_058 (Class-C plateau, in queue).*
