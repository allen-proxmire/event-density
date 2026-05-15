# Arc E — Memo 2: Generic Non-Factorizability and Density of Entangled States

**Status:** Articulation memo conditional on E-1 (tensor-product composition FORM-FORCED). No new primitives. Identification-not-derivation discipline observed. Acyclicity audit at §6.

**Date:** 2026-05-08

---

## 1. The CANDIDATE Statement

> **CANDIDATE (E2).** *In the joint Hilbert space $\mathcal{H}_A \otimes \mathcal{H}_B$ derived as FORM-FORCED in E-1, non-factorizable (entangled) states form a dense, full-measure subset of the joint state space (equivalently: of the projective state space $\mathbb{P}(\mathcal{H}_A \otimes \mathcal{H}_B)$). Their existence and density are structurally inevitable mathematical consequences of E-1 + U2 + T10, and ED-I-02's "single undeveloped participation rule" framing imposes no substrate-level superselection that would restrict the joint state space.*

E-2 is expected to be an articulation memo: the mathematical content is standard, and the substrate-level work consists in confirming that no hidden substrate restriction interferes with the standard result.

The CANDIDATE has two distinct claims:

- **(D1) Density / generic-non-factorizability claim.** The set of product (factorizable) states is measure-zero and nowhere-dense in $\mathbb{P}(\mathcal{H}_A \otimes \mathcal{H}_B)$ for $d_A, d_B \geq 2$.
- **(D2) Substrate-consistency claim.** ED-I-02 + ED-I-06 + the closed-arc primitive set impose no superselection rule that excludes generic entangled states from the substrate-realizable joint state space.

---

## 2. Substrate Inputs (Inheritance)

| Input | Status | Role |
|---|---|---|
| **E-1** (tensor-product composition FORM-FORCED) | Closed (this arc) | Joint Hilbert space is $\mathcal{H}_A \otimes \mathcal{H}_B$ with bilinearly-induced inner product |
| **U2** (single-endpoint Hilbert-space structure / T11–T12) | FORCED-unconditional | Linear closure on each side; complex inner-product structure |
| **T10** (Born rule) | FORCED-unconditional | State-space normalization; physical states are unit rays in $\mathbb{P}(\mathcal{H}_A \otimes \mathcal{H}_B)$ |
| **Standard finite-dim Hilbert-space mathematics** | Free (mathematical) | SVD, dimension counting, Lebesgue / Fubini-Study measure, algebraic geometry of Segre varieties |
| **ED-I-02** (single undeveloped participation rule) | Conceptual ground | Substrate-level reading; (SP) and (IP) configuration distinction from E-1 §3.1 |
| **ED-I-06** (no fundamental fields) | Canonical guardrail | Forbids field-sourced superselection rules |

**No new primitives.** **No use of E-3 (Schmidt), E-4 (monogamy), E-5 (no-signaling), E-6 (entropy), or E-7 (synthesis) content.**

---

## 3. Derivation of (D1): Density via the Segre Variety

### 3.1 The set of product states is the Segre variety

Let $d_A = \dim \mathcal{H}_A$ and $d_B = \dim \mathcal{H}_B$, both finite for the moment (continuum extension treated in §3.5). The full joint space $\mathcal{H}_A \otimes \mathcal{H}_B$ has $\dim = d_A d_B$, and the projective space of physical pure states is $\mathbb{P}(\mathcal{H}_A \otimes \mathcal{H}_B)$ with $\dim_{\mathbb{C}} = d_A d_B - 1$.

The set of product (factorizable, separable pure) states is the image of the *Segre embedding*

$$\mathrm{Seg}: \mathbb{P}(\mathcal{H}_A) \times \mathbb{P}(\mathcal{H}_B) \to \mathbb{P}(\mathcal{H}_A \otimes \mathcal{H}_B), \qquad ([\psi_A], [\psi_B]) \mapsto [\psi_A \otimes \psi_B].$$

The Segre variety $\Sigma := \mathrm{Seg}(\mathbb{P}(\mathcal{H}_A) \times \mathbb{P}(\mathcal{H}_B))$ has dimension

$$\dim_{\mathbb{C}} \Sigma = (d_A - 1) + (d_B - 1) = d_A + d_B - 2.$$

### 3.2 Dimensional comparison

The codimension of $\Sigma$ in $\mathbb{P}(\mathcal{H}_A \otimes \mathcal{H}_B)$ is

$$\mathrm{codim}_{\mathbb{C}} \Sigma = (d_A d_B - 1) - (d_A + d_B - 2) = (d_A - 1)(d_B - 1).$$

For $d_A, d_B \geq 2$, $\mathrm{codim}_{\mathbb{C}} \Sigma \geq 1$, with strict inequality unless one of the factors is one-dimensional.

### 3.3 Measure-zero and nowhere-dense

A proper algebraic subvariety of $\mathbb{P}(\mathcal{H}_A \otimes \mathcal{H}_B)$ of strictly positive codimension has:

- **Lebesgue / Fubini-Study measure zero.** Standard result: any complex algebraic subvariety of a projective space that is not the full space has measure zero in any unitarily-invariant measure. This is the Fubini-Study version of the standard real-algebraic measure-zero theorem.
- **Empty interior (nowhere-dense).** Same reasoning: an algebraic subvariety of lower dimension cannot contain an open ball of the ambient space.

So:

$$\mu_{FS}\big(\Sigma\big) = 0, \qquad \overline{\Sigma}^{\,\mathrm{int}} = \emptyset.$$

The complement $\mathbb{P}(\mathcal{H}_A \otimes \mathcal{H}_B) \setminus \Sigma$ — the set of *entangled* pure states — has full measure and is open and dense.

### 3.4 Operational reading: generic perturbations entangle

Given any product state $[\psi_A \otimes \psi_B]$, every neighborhood of $[\psi_A \otimes \psi_B]$ in $\mathbb{P}(\mathcal{H}_A \otimes \mathcal{H}_B)$ contains states *not* in $\Sigma$. Concretely, a generic infinitesimal perturbation

$$|\psi_A \otimes \psi_B\rangle + \epsilon |\phi\rangle, \qquad |\phi\rangle \in \mathcal{H}_A \otimes \mathcal{H}_B$$

is a product state only if $|\phi\rangle$ lies in the tangent space to $\Sigma$ at $[\psi_A \otimes \psi_B]$, which has codimension $(d_A - 1)(d_B - 1) \geq 1$. The set of admissible $|\phi\rangle$ that preserve product structure is a measure-zero subspace of the perturbation space. Generic perturbations entangle.

### 3.5 Continuum extension

For infinite-dimensional separable $\mathcal{H}_A$ and $\mathcal{H}_B$ (e.g., continuum field-theoretic regimes after DCGT coarse-graining): the Segre embedding extends naturally, and the set of product states is the closed image of $S(\mathcal{H}_A) \times S(\mathcal{H}_B)$ under the bilinear product map (where $S$ denotes unit sphere). Density and meagerness arguments transfer: in any standard Borel measure on the unit sphere of $\mathcal{H}_A \otimes \mathcal{H}_B$ (Gaussian, unitarily-invariant, or Fubini-Study-on-projectivization), the product set has measure zero. The argument is the standard one: countable union of finite-dim Segre varieties' closures, each measure-zero in the relevant projection.

DCGT supplies the bridge: any density / genericity result that holds at the substrate (discrete) level transfers to the continuum (coarse-grained) level via the substrate-to-continuum map, since DCGT preserves linear-algebraic structure of joint Hilbert spaces.

**(D1) is FORCED** as a mathematical consequence of E-1 (joint space is tensor product) + U2 (linear closure on each side) + standard Hilbert-space algebraic geometry. No substrate-level conditionality enters the mathematical argument.

---

## 4. Derivation of (D2): Substrate Consistency — No Hidden Superselection

E-1 §6.4 already audited and refuted hybrid superselection-sector decompositions of the joint Hilbert space at the substrate level. E-2 confirms this audit suffices for (D2).

### 4.1 ED-I-02's substrate reading endorses non-factorizability as generic

ED-I-02 distinguishes two configurations of two-endpoint substrate (E-1 §3.1):

- **(IP) Independent-preparation configurations.** Each endpoint has been individuated with its own developed participation rule, causally and structurally independent. These map to product states under E-1's bilinear $f$.
- **(SP) Single-rule shared configurations.** Both endpoints express one undeveloped participation rule (the entanglement case). These map to non-product states.

(IP) configurations require *causal and structural independence* of the two endpoints — a non-generic condition that demands deliberate preparation (separated origins, no shared substrate history, no V1-mediated cross-chain correlation since fragment formation). (SP) configurations are the substrate's *default* whenever two endpoints share even partial substrate history.

So the substrate reading of (D1) is: **generic substrate configurations of two endpoints are (SP)-class, not (IP)-class.** Product states are the exceptional case requiring deliberate independence-preparation; entangled states are the substrate-default.

This is not merely consistent with (D1); ED-I-02's substrate reading *predicts* (D1) at the qualitative level. The mathematical density theorem in §3 is the formal statement of what ED-I-02 says ontologically.

### 4.2 ED-I-06 forbids field-sourced superselection

A superselection rule restricting the joint state space to a sub-manifold containing product states would have to be sourced by an ontologically-primary structure. ED-I-06 (no fundamental fields) forbids the fundamental-field source. The substrate inventory contains no other source for a-priori joint-space sectorization.

### 4.3 Closed-arc audit confirms no inherited superselection

Each closed arc with a structural finding that touches joint Hilbert space:

- **Phase-1 (T10–T16):** all postulates derived; no joint-space superselection introduced.
- **Arc Q (T17, gauge as rule-type):** introduces continuum gauge convention as the *only* description-level CANDIDATE; gauge structure does not partition $\mathcal{H}_A \otimes \mathcal{H}_B$.
- **Arc B (T18, V1 retardation):** kernel structure on cross-chain correlations; no superselection.
- **Arc D (DCGT):** substrate-to-continuum bridge preserves joint linear structure.
- **Arc Q-COMPUTE:** multiplicity-cap function $M$ controls $\mathcal{U}$ dynamics, not joint state-space accessibility.
- **Arc BH (BH-2 through BH-7):** entanglement-straddling at decoupling surfaces; no superselection on joint state-space *structure*, only on cross-surface bandwidth $\Gamma_{\mathrm{cross}}$.
- **Arc SG / Arc ED-10:** scalar-tensor gravity content, no joint-Hilbert-space restriction.

No closed arc has produced a substrate-level superselection rule on bipartite joint Hilbert space. **(D2) is FORCED** modulo any future arc producing a substrate-derived superselection (none currently in flight).

### 4.4 Note: emergent superselection via einselection is downstream and consistent

Decoherence / einselection produces effective superselection sectors at the *coarse-grained* level (in the standard QM reading). This is a downstream emergent phenomenon and does not contradict (D2). E-2 states only that the *substrate-level* joint Hilbert space is unrestricted; emergent dynamical sectorization is consistent and lives downstream of E-1.

---

## 5. Verdict

> **VERDICT (E2): FORCED.**
>
> Density of entangled states in $\mathbb{P}(\mathcal{H}_A \otimes \mathcal{H}_B)$ — equivalently, the structural inevitability of generic non-factorizability — follows automatically from E-1 (tensor-product composition FORM-FORCED) + U2 (linear closure) + T10 (Born unit-ray normalization) + standard Hilbert-space algebraic geometry. ED-I-02 substrate-reading endorses this result at the ontological level; ED-I-06 forbids the only conceivable source of a contradicting superselection rule; closed-arc audit confirms no inherited substrate-level joint-space restriction.

**Verdict-class details:**

- **Form-FORCED:** the *structural fact* that entangled states are dense and full-measure is FORCED.
- **Value-INHERITED:** the *specific dimension* of the Segre variety is INHERITED from the values of $d_A, d_B$ (which are themselves INHERITED for any specific physical system from its substrate-derived state-space dimension).
- **No CONDITIONAL caveat survived the audit.** The continuum-limit step (§3.5) was resolved as a downstream consequence of DCGT, not an auxiliary assumption.
- **No NOT-FORCED option survived.** The §4 audit failed to identify any substrate-level superselection candidate.

E-2 is therefore confirmed as an articulation memo: the substrate does what U2 + E-1 + T10 require, and the mathematical density theorem follows.

---

## 6. Circularity Audit

| Potential circularity | Audit verdict |
|---|---|
| E-3 (Schmidt) used as derivation premise? | **No.** Schmidt decomposition would in fact reach (D1) by a different route (states with Schmidt rank > 1 are entangled, and Schmidt rank > 1 is generic), but E-2's §3 derivation uses the Segre-variety dimension argument instead, avoiding any reference to Schmidt content. |
| E-4 (monogamy) used as derivation premise? | **No.** Not invoked. |
| E-5 (no-signaling) used as derivation premise? | **No.** Not invoked. |
| E-6 (entropy form) used as derivation premise? | **No.** Not invoked. |
| E-7 (synthesis) used as derivation premise? | **No.** Not invoked. |
| Self-reference of E-2 within itself? | **No.** §3 → §4 → §5 derivation chain is acyclic; §3 (D1) and §4 (D2) are independent claims joined at §5. |
| E-1 used only as input, not as conclusion? | **Confirmed.** E-1's FORM-FORCED tensor-product structure is a substrate fact at the time of writing; E-2 inherits it as input. |

**Acyclicity confirmed.**

---

## 7. Falsification

### 7.1 Falsifier for FORCED verdict (current verdict)

Either (a) a mathematical demonstration that the Segre variety is *not* of strictly lower dimension than $\mathbb{P}(\mathcal{H}_A \otimes \mathcal{H}_B)$ for some $d_A, d_B \geq 2$ (impossible — this is a theorem of complex algebraic geometry); or (b) a substrate-level superselection rule that restricts the joint Hilbert space to a sub-manifold containing the Segre variety, derived from the active primitive set without violating E-1's FORM-FORCED verdict.

(a) is mathematically excluded.
(b) was audited and excluded in §4. A future substrate finding that re-opens this audit would downgrade E-2's verdict.

### 7.2 Falsifier for CONDITIONAL verdict (rejected)

An auxiliary assumption $A^{**}$ such that: (i) the §3 derivation requires $A^{**}$ for one of its steps to go through; (ii) $A^{**}$ is not itself FORCED by E-1 + U2 + T10 + ED-I-02 + ED-I-06; (iii) without $A^{**}$, the density claim fails or is not unique.

The audit failed to identify such an $A^{**}$. The continuum-limit step (§3.5) resolves via DCGT, not auxiliary assumption.

### 7.3 Falsifier for NOT-FORCED verdict (rejected)

A substrate construction satisfying all primitives + E-1 + U2 + T10, in which the joint Hilbert space is the full $\mathcal{H}_A \otimes \mathcal{H}_B$ but a substrate-level superselection rule restricts physical states to the Segre variety (i.e., only product states are physically realizable). This would contradict E-1 §6.4 and ED-I-06.

### 7.4 Empirical-side falsifier (independent of substrate-side)

Any experimental demonstration that all observed bipartite quantum states are product states — i.e., no Bell-violation experiment produces non-product correlations. Such observations are not reported and would refute Phase-1 Bell–Tsirelson. The empirical record consistently produces non-product correlations across many platforms.

---

## 8. Consequences for the Arc

1. **E-2 closes cleanly as articulation memo.** Generic non-factorizability is FORCED. Any downstream Arc E memo may invoke "entangled states are dense / generic" as a substrate fact.

2. **E-3 (Schmidt) and E-5 (no-signaling) are now structurally unblocked and can be drafted in parallel.** Both inherit E-1 + E-2; E-3 additionally needs U2 and standard SVD; E-5 additionally needs T18 + P11.

3. **The (IP) vs. (SP) distinction is now formally articulated** as the substrate reading of "product vs. entangled." (IP) configurations require deliberate causal and structural independence; (SP) configurations are the substrate-default. This terminology will be useful in E-4 (monogamy) and E-7 (synthesis).

4. **Substrate-level reading: entanglement is the generic case.** This sharpens ED-I-02's qualitative claim ("entanglement is the persistence of undeveloped identity") to the formal mathematical claim that *most* substrate configurations of two endpoints are non-individuated, and individuation (which produces product states) is the structural exception. This reading propagates to E-7's synthesis with BH-4 entanglement-straddling.

5. **No new active CANDIDATEs.** Active CANDIDATE inventory remains {} as of arc-opening tally.

6. **No sensitivity flags introduced beyond E-1's existing P09 flag.** E-2 inherits E-1's load-bearings without adding new ones.

---

## 9. Summary

**What this memo accomplished.**

- Stated the E-2 CANDIDATE (§1) and decomposed it into (D1) density and (D2) substrate-consistency.
- Derived (D1) via Segre-variety dimensional argument: $\mathrm{codim}_{\mathbb{C}} \Sigma = (d_A - 1)(d_B - 1) \geq 1$ for $d_A, d_B \geq 2$, hence $\Sigma$ is measure-zero and nowhere-dense (§3).
- Confirmed (D1) extends to continuum dimension via DCGT (§3.5).
- Audited (D2): ED-I-02 substrate reading endorses generic non-factorizability; ED-I-06 forbids superselection-sourcing fields; closed-arc inheritance audit confirms no substrate-level joint-space restriction (§4).
- Issued the verdict: **FORCED** (§5).
- Confirmed acyclicity (§6).
- Provided substrate-level falsifiers for each verdict class (§7).
- Sharpened ED-I-02's qualitative claim into the formal "(IP) is exceptional, (SP) is generic" reading (§8).

**What this memo did not do.**

- Did not derive Schmidt decomposition (E-3 deliverable).
- Did not derive monogamy (E-4 deliverable).
- Did not derive no-signaling (E-5 deliverable).
- Did not address mixed-state separability (the more refined question of whether mixed states are generically entangled in the operator space $\mathcal{B}(\mathcal{H}_A \otimes \mathcal{H}_B)$). E-2 treats only pure states. Mixed-state separability has more nuanced density structure (separable and entangled mixed states each form full-measure-positive sets near the maximally-mixed state, by Życzkowski et al.); this is downstream content that does not affect E-2's pure-state verdict and is best addressed if and when an Arc E memo treats mixed-state structure explicitly.

**Recommended next steps.**

1. **E-3 (next memo): Schmidt decomposition — form-FORCED, values-INHERITED.** Articulate Schmidt decomposition as a theorem of inner-product algebra given E-1 + U2. Identify Schmidt coefficients as INHERITED from substrate-state-specific spectral data. Expected verdict form-FORCED, values-INHERITED. Estimated 0.5–1 session.

2. **E-5 (parallel with E-3): No-signaling from V1 retardation + P11.** Derive partial-trace independence under measurement-basis change. Substrate inputs: T18 (forward-cone-only correlations) + P11 (commitment irreversibility) + E-1 (partial trace well-defined). Expected verdict FORCED. Estimated 0.5–1 session. Can be drafted in parallel with E-3.

3. **(Defer until E-3 + E-5 close) Stage E-4 (monogamy) and E-6 (entropy form) as the substantive-derivation pair.** Both require their own primitive-level arguments (cross-chain bandwidth budgets for E-4; Shannon–Khinchin substrate counting for E-6). Each is expected to take 1–2 sessions.

---

**Pause for further instruction.**
