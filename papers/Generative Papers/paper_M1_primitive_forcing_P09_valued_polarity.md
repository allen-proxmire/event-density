> **⚠️ ARCHIVED — 2026-05-13.** This paper is frozen as a historical artifact. See `ARCHIVED_M_SERIES_NOTICE.md` for context. External review identified circularity in Routes E (Coecke-Kissinger presupposes complex Hilbert space) and A.2 (explicit Paper #1 invocation in §7.2, violating the §3.1 acyclicity claim). The displaced-postulate critique is not eliminated by this paper — it is displaced one level up into the meta-substrate's C*4 empirical-recovery commitment. ED is now framed as an **axiomatic substrate ontology** (13 postulated primitives + cross-domain reach), not a forcing-from-nothing program. Do not cite this paper as "forcing" P09; do not build new work on its framework.

---

# Primitive P09 — $U(1)$-Valued Polarity — is FORCED

**Paper M-1 of the Event Density Primitive-Forcing Series**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-13
**Series:** Event Density (ED) Primitive-Forcing M-Series — Paper M-1
**Position:** First primitive-forcing paper. Downstream of Meta-Paper M0. Upstream of Forcing Papers #1–#19.
**Genre:** Primitive-level forcing paper. Standalone. Cold-reader accessible. 10-section template.

---

## Abstract

The Event Density (ED) substrate is committed at the primitive level to a **$U(1)$-valued polarity** (Primitive P09): each channel $K$ at each substrate locus $u$ carries an angular variable $\pi_K(u) \in U(1) \cong S^1$, and this is the *unique* angular primitive in the substrate. In the standard Forcing Series, P09 is named as a load-bearing input to Papers #1, #2, #3, #5, #16, and #17 — the displaced-postulate critique applies at full strength, specifically targeting P09 as "the postulate that already contains the answer" (a substrate committed to $U(1)$ angular content at the primitive level is, in some readings, structurally pre-committed to complex Hilbert space downstream). This paper shows that, given the meta-substrate framework $\{C^*\}$ of Meta-Paper M0 and standard background mathematics (Frobenius classification of finite-dim associative real division algebras, classification of compact connected abelian Lie groups, Coecke-Kissinger categorical-QM framework, max-entropy principle on continuous-classical-structures), P09's $U(1)$-valued angular structure is forced as the unique substrate-level angular primitive satisfying joint constraints from **continuity (Route A.1)**, **compactness (Route A.2 + Frobenius classification)**, **abelian-ness (Route A.3)**, **1-dimensionality (Route A.4 + compositional closure)**, and **categorical-QM necessity (Route E via Coecke-Kissinger Frobenius algebra classification)** — with operational-adequacy (Route B) as cross-check. Discrete-cyclic ($\mathbb{Z}_n$), real-line non-compact ($\mathbb{R}$), integer-winding ($\mathbb{Z}$), non-abelian ($SO(3)$, $SU(2)$), multi-dimensional torus ($T^n$ for $n \geq 2$), hybrid continuous-discrete, non-Lie ($p$-adic, fractal), and no-angular-primitive alternatives are each excluded by explicit structural argument. The $U(1)$ form is FORCED. The numerical period / scale (i.e., $\pi_K \in [0, 2\pi)$ vs. $\pi_K \in [0, 1)$) is INHERITED as a labeling convention. With M-1 closure, six downstream papers (#1, #2, #3, #5, #16, #17) shift their §3.0 status for P09 from "load-bearing input" to "forced upstream by M-1"; the displaced-postulate critique no longer applies to P09 across these papers.

---

## 1. Framing

### 1.1 What the displaced-postulate critique says about P09 specifically

The reviewer critique that catalyzed the entire ED Primitive-Forcing Series targeted P09 directly. Verbatim from the critique: *"the postulate 'the substrate has a U(1)-valued angular primitive' already contains the answer. Once you've committed to that, the rest of the paper is doing legitimate algebra — $\mathbb{C}$ falls out because $\mathbb{C}$ is the algebra with a faithful $U(1)$ action of the right dimension."*

The critique is structurally correct: Paper #1's derivation of the complex participation measure $P_K = \sqrt{b_K} \cdot e^{i\pi_K}$ rests on the substrate's $U(1)$-valued angular primitive. The Frobenius classification argument (any finite-dim associative real division algebra is $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{H}$) singles out $\mathbb{C}$ as the unique algebra carrying a faithful $U(1)$ action of the right structural character; the polar form $r e^{i\theta}$ with $r \geq 0$ and $\theta \in U(1)$ then falls out as the unique amplitude carrier. *Given* $U(1)$, the complex-Hilbert-space arena is forced. The question is: *why $U(1)$, and not some other angular structure?*

Standard QM postulates the complex Hilbert space at the outset and derives $U(1)$ downstream as a gauge group of the wavefunction. ED postulates $U(1)$-polarity at the substrate level and derives the complex Hilbert space downstream as the amplitude-carrier algebra. Both frameworks move the postulate, but neither (until M-1) actually derives $U(1)$ from a deeper structural layer. The present paper attempts to do precisely that.

### 1.2 The puzzle

Why $U(1)$ at the substrate level? Candidate angular structures the substrate could in principle adopt:

- $\mathbb{Z}_n$ for finite $n$ (discrete cyclic angular content);
- $\mathbb{R}$ (real-valued non-compact angular content);
- $\mathbb{Z}$ (integer-winding non-compact discrete);
- $U(1)^n = T^n$ for $n \geq 2$ (multi-dimensional torus);
- $SO(3)$ or $SU(2)$ (non-abelian compact angular);
- $p$-adic angular content (non-Lie-group structure);
- no angular primitive at all (substrate carries only bandwidth, no phase content).

Each is structurally distinct. Each would, if adopted at the substrate level, produce a different downstream physics. ED's commitment to $U(1)$ — specifically, to a compact continuous abelian 1-dimensional Lie group — is therefore one structural choice among many. To call it forced, we must exclude all alternatives by structural argument.

### 1.3 What this paper does

The Event Density (ED) framework supplies a pre-quantum substrate (per Meta-Paper M0). This paper attempts the upstream-forcing of P09's $U(1)$-valued structure under five convergent constructive routes:

1. **Continuity (§7.1).** The substrate's angular primitive must be a continuous topological group with a 1-parameter continuous action on channel participation. Discrete-cyclic alternatives ($\mathbb{Z}_n$) fail to support the empirically observed continuous-phase interference (Mach-Zehnder gradual phase tuning, Aharonov-Bohm continuous flux variation, atomic interference at continuous wavelength).

2. **Compactness (§7.2 + Frobenius classification).** The substrate's angular primitive must act on a *bounded* algebra of admissible carriers. Frobenius classification of finite-dim associative real division algebras restricts admissible substrate-level division-algebra carriers to $\{\mathbb{R}, \mathbb{C}, \mathbb{H}\}$; for the angular primitive to act *faithfully* (distinguishing different angular values) and *compactly* (bounded angular domain), the primitive must be a compact continuous Lie group.

3. **Abelian-ness (§7.3).** The substrate's angular primitive is *intrinsic to each channel* — it does not couple channels at the primitive level (channel-channel coupling at the primitive level is the gauge-field structure of Paper #5, downstream). Therefore the angular primitive must act *commutatively* on each channel.

4. **1-dimensionality (§7.4 + compositional closure).** Multiple independent angular primitives ($T^n$ for $n \geq 2$) would correspond to multiple substrate-level phase content per channel. The empirically observed character of phase — chain participation has *one* phase per channel per locus, not multiple — combined with M-2's four-band partition's structural constraint of single-bandwidth-per-channel, forces $n = 1$.

5. **Categorical-QM necessity (§7.5 + Coecke-Kissinger framework).** The Coecke-Kissinger framework classifies continuous-classical-structures on dagger-symmetric-monoidal categories via dagger-Frobenius algebras. The unique 1-dimensional continuous self-dual abelian Frobenius algebra (modulo isomorphism) is the one corresponding to $U(1)$. This provides an independent route via category-theoretic necessity.

Convergent forcing: any one of routes A.1, A.2, A.3, A.4, E alone narrows the candidate space substantially; the joint application of all five (plus operational-adequacy Route B as sanity check) uniquely selects $U(1)$ as the substrate's angular primitive. Discrete-cyclic, non-compact, non-abelian, multi-dimensional, hybrid, and non-Lie alternatives are each excluded by at least one of the five routes (§8 details per-alternative exclusion).

**Series context.** This is Paper M-1 of the ED Primitive-Forcing M-series. M-1 is the first primitive-forcing paper, opening the program-level response to the displaced-postulate critique. It precedes M-2 (P04 four-band partition + bandwidth additivity), M-3 (P11 commitment irreversibility + uniform-$U(1)$ phase-randomization), M-4 (joint symmetry cluster P03 + P13 + GAL + POI), and subsequent M-papers in the series. With M-1 closed, the displaced-postulate critique no longer applies to P09 across the six downstream papers that named P09 as load-bearing input.

---

## 2. Claim

> **Forcing Theorem M-1 (P09 is FORCED).** Let any meta-substrate satisfy the conditions $\{C^*\}$ of Meta-Paper M0 §5. Then the substrate's unique angular primitive — the polarity $\pi_K$ on each channel and locus — is forced to be $U(1)$-valued. Discrete-cyclic ($\mathbb{Z}_n$), real-line non-compact ($\mathbb{R}$), integer-winding ($\mathbb{Z}$), non-abelian ($SO(3)$, $SU(2)$), multi-dimensional torus ($T^n$ for $n \geq 2$), hybrid continuous-discrete, non-Lie-group, and no-angular-primitive alternatives are each excluded by joint application of five convergent forcing routes — continuity (A.1), compactness via Frobenius classification (A.2), abelian-ness (A.3), 1-dimensionality + compositional closure (A.4), and Coecke-Kissinger categorical-QM necessity (E) — with operational-adequacy (B) as cross-check. The $U(1)$ form is FORCED. The numerical period / scale (labeling convention) is INHERITED.

---

## 3. Primitive Inputs and Upstream Dependencies

### 3.0 Meta-Substrate Inputs (load-bearing, not derived in this paper)

This paper's forcing argument invokes:

- **Meta-substrate framework $\{C^*\}$ (Meta-Paper M0 §5).** Specifically: existence of substrate framework supporting primitive specification, mathematical infrastructure access, structural-normative goal of empirical-physics recovery.
- **Background mathematics.** Frobenius classification of finite-dim associative real division algebras (Frobenius 1878); classification of compact connected Lie groups (Cartan-Killing); Coecke-Kissinger categorical-QM framework (Coecke & Kissinger 2017); Haar measure on compact Lie groups; max-entropy principle.
- **The structural-normative goal of empirical-physics recovery (C*4).** Specifically: the substrate must support empirically observed continuous-phase interference (Mach-Zehnder, Aharonov-Bohm, atomic / molecular interference at continuous wavelength) and the empirically observed character of phase as a *single* continuous variable per channel.

### 3.1 No downstream input — circularity audit

This paper does NOT invoke any result from Forcing Papers #1–#19. Specifically:

- **Paper #1 (Participation Measure).** Downstream — invokes P09 as input to derive the complex-Hilbert-space arena.
- **Paper #2 (Born Rule).** Downstream.
- **Paper #3 (Inner Product + Tsirelson).** Downstream.
- **Paper #5 (Gauge T17).** Downstream — invokes P09 as the substrate-level source of the $U(1)$ gauge group.
- **Paper #16 (Phase-Independence).** Downstream.
- **Paper #17 (Four Postulates Unified).** Downstream synthesis.

M-1 is the first M-paper in the series; it has no prior M-paper closures to invoke. Its only inputs are $\{C^*\}$ + standard mathematics + the structural-normative empirical-recovery goal. The DAG is acyclic.

### 3.2 What is FORCED

- **The substrate's angular primitive is $U(1)$-valued.** $\pi_K(u) \in U(1) \cong S^1$ for each channel $K$ at each locus $u$.
- **The angular primitive is continuous, compact, abelian, 1-dimensional, and Lie-group-structured.** All five structural properties forced jointly.
- **The angular primitive is unique.** No other substrate-level angular primitive exists; P09 is the substrate's *only* angular variable.
- **The angular primitive is independent of bandwidth.** P09 is structurally distinct from P04 (bandwidth) — bandwidth is real-valued non-negative; polarity is $U(1)$-valued angular. This independence is part of the four-band-partition vs. polarity structural distinction (which M-2 makes explicit; here we establish polarity's character independently).

### 3.3 What is INHERITED

- **The numerical period / scale of $U(1)$.** Whether $\pi_K \in [0, 2\pi)$ or $\pi_K \in [0, 1)$ or $\pi_K \in [0, \tau)$ is a labeling convention. The forcing argument fixes the $U(1)$ group structure; the choice of period is a unit choice.
- **The specific identification of substrate polarity with empirical phase observables** (e.g., electromagnetic gauge phase, wavefunction phase). Empirical correspondence at the value layer.
- **Mathematical infrastructure** (Frobenius classification, Lie group theory, Coecke-Kissinger framework). Inherited as background mathematics.

### 3.4 What is OUT OF SCOPE

- This paper does NOT derive any Forcing Paper #1–#19 result. M-1 is strictly upstream.
- This paper does NOT derive bandwidth additivity (P04 core); that is M-2.
- This paper does NOT derive the four-band partition (P04 §1.5); that is M-2.
- This paper does NOT derive commitment irreversibility (P11); that is M-3.
- This paper does NOT derive any symmetry primitive (P03, P13, GAL, POI); those are M-4.
- This paper does NOT address why the substrate has *any* angular primitive at all. The substrate's commitment to *some* angular primitive is part of the meta-substrate's structural-normative goal (recovering empirically observed continuous-phase interference requires some continuous angular content). Why interference must be continuous — rather than, say, classical-statistical — is a deeper question not addressed here.

---

## 4. Key Vocabulary

- **Polarity $\pi_K(u)$.** The substrate's primitive angular variable, attached to each channel $K$ at each substrate locus $u$.
- **Angular primitive.** A substrate-level structural commitment to an angle-like (i.e., periodic or quasi-periodic) primitive variable.
- **$U(1)$ (circle group).** The unique compact continuous 1-dimensional abelian Lie group. Topologically $S^1$. The standard model of phase in electromagnetism and quantum mechanics.
- **$\mathbb{Z}_n$ (discrete cyclic group of order $n$).** A discrete angular structure with $n$ values, $\{0, 1, \ldots, n-1\}$ under addition modulo $n$.
- **$\mathbb{R}$ (real line).** Non-compact continuous abelian Lie group.
- **$\mathbb{Z}$ (integers).** Discrete non-compact group; corresponds to integer-winding angular structure.
- **$SO(3), SU(2)$.** Compact non-abelian Lie groups; rotations of 3-space (and its double cover).
- **$T^n = U(1)^n$.** The $n$-dimensional torus, an abelian compact Lie group of rank $n$.
- **Continuous-phase interference.** Empirically observed phenomenon — interference patterns whose phase content varies continuously (e.g., gradual Aharonov-Bohm phase shifts, continuous Mach-Zehnder phase tuning).
- **Frobenius classification (1878).** The classification of finite-dim associative real division algebras: only $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$ (the quaternions). A foundational result of algebra.
- **Coecke-Kissinger framework.** Categorical-QM framework (Coecke & Kissinger 2017) treating quantum mechanics as a dagger-symmetric-monoidal category, with classical structures (Frobenius algebras) corresponding to observables. Used in Route E.
- **Continuous-classical-structure.** In Coecke-Kissinger: a dagger-Frobenius algebra on a dagger-symmetric-monoidal category, corresponding to a continuous classical observable.
- **Faithful action.** A group action with trivial kernel — distinct group elements produce distinct transformations.
- **Compact (topological group).** A topological group whose underlying space is compact (bounded + closed in any embedding into a Lie algebra). $U(1)$ is compact; $\mathbb{R}$ is not.
- **Compositional closure.** Per Meta-Paper M0 §5 C*5: substrate's primitive structural commitments must compose consistently — the substrate's operations chain together without producing structures outside the substrate's primitive operational class.
- **Meta-substrate $\{C^*\}$.** Framework within which M-series forcing arguments operate (Meta-Paper M0 §5).

---

## 5. Substrate Class $\{C^*\}$

The forcing theorem applies to any meta-substrate satisfying:

### C*1. Meta-substrate framework

Per Meta-Paper M0 §5. The meta-substrate supplies a framework for specifying substrate-level structural commitments; specific substrate-models are obtained by selecting primitives within the framework. The present paper analyzes what angular-primitive structure the substrate must adopt.

### C*2. Existence of an angular primitive

The substrate is committed at the primitive level to *some* angular variable $\pi_K$ on each channel $K$ at each locus $u$. The structural-normative goal C*4 (empirical-recovery) requires this: continuous-phase interference is empirically observed at all scales (matter-wave interference, light interference, atomic-clock interferometry); the substrate must support these phenomena with some continuous angular content.

Why interference must be continuous — rather than classical-statistical or fundamentally discrete — is part of the meta-substrate's structural-normative empirical-recovery goal, not derived here. We invoke it as given.

### C*3. Standard mathematical infrastructure

The meta-substrate has access to: Frobenius classification (1878); Cartan-Killing classification of compact Lie groups; Coecke-Kissinger categorical-QM framework (2017); Haar measure on compact Lie groups; max-entropy principle.

### C*4. Empirical-recovery structural-normative goal

The substrate must support empirically observed continuous-phase interference phenomena (per M0 §5 C*4). This load-bearing structural-normative commitment is used in Routes A.1 (continuity necessity) and B (operational-adequacy cross-check).

### C*5. Compositional closure

The substrate's primitive structural commitments must compose consistently. Used in Route A.4 (single-phase-per-channel argument relating to single-bandwidth-per-channel structure).

### C*6. No prior M-paper closures invoked

M-1 is the first M-paper in the series. The forcing argument uses only $\{C^*\}$ + background mathematics + the empirical-recovery goal. No earlier M-paper closures exist.

---

## 6. Alternative Encodings $\{A1-A6\}$ and $\{B1-B6\}$

### 6.A. A-series — Structural alternatives within the substrate-ontology framework

**A1. $\mathbb{Z}_n$ (discrete cyclic group of finite order $n$).**
A discrete angular structure with $n$ values. Substrate's polarity primitive takes values $\pi_K \in \{0, 1, \ldots, n-1\}$ mod $n$.

**A2. $T^n = U(1)^n$ for $n \geq 2$.**
The $n$-dimensional torus. Substrate's polarity primitive takes values in an $n$-dimensional compact abelian Lie group; equivalently, $n$ independent $U(1)$ phases per channel.

**A3. $U(1) \times \mathbb{Z}_n$ for $n \geq 2$ (hybrid continuous-discrete).**
A continuous $U(1)$ component combined with a discrete $\mathbb{Z}_n$ component. Polarity takes values $\pi_K \in U(1) \times \mathbb{Z}_n$.

**A4. $\mathbb{Z}$ (integer-winding non-compact discrete).**
Polarity takes integer values: $\pi_K \in \mathbb{Z}$. Quantized angular structure with no upper bound.

**A5. $SO(3)$ or $SU(2)$ (compact non-abelian).**
Polarity takes values in a compact connected non-abelian Lie group. Multiple non-commuting components.

**A6. No angular primitive at all.**
The substrate has bandwidth (P04 in M-2) but no polarity primitive. Phase content is structurally absent at the substrate level; any phase-like effects in downstream phenomena would be downstream emergent content rather than substrate primitive.

### 6.B. B-series — Mainstream alternatives from physics frameworks

**B1. $\mathbb{R}$ (real-line non-compact continuous).**
Polarity takes real-valued non-compact values: $\pi_K \in \mathbb{R}$. Equivalent to lifting $U(1) \to \mathbb{R}$ via covering map; angular structure unbounded.

**B2. $SU(2)$ (compact non-abelian, structurally equivalent to A5 but considered as the QM-spin Lie group).**
Distinct from A5 in the physics-framework context: $SU(2)$ specifically as the spin-1/2 covering group of $SO(3)$, treated as a substrate-level angular structure.

**B3. $p$-adic angular content.**
Polarity takes values in a $p$-adic group $\mathbb{Q}_p / \mathbb{Z}_p$ or similar non-Archimedean structure. Non-Lie-group angular structure.

**B4. Fractal-valued angular content.**
Polarity takes values in a Cantor-like or other fractal subset of $S^1$ or $\mathbb{R}$.

**B5. Higher-dimensional Lie group with $U(1)$ as a subgroup** (e.g., $U(n)$ for $n \geq 2$ treated as the substrate-level angular structure rather than as a downstream gauge group).
Polarity takes values in a larger compact Lie group that contains $U(1)$ as a proper subgroup.

**B6. Categorically-trivial structure** (e.g., the substrate has only $\mathbb{Z}_2$ phase content, treating phase as a sign flip).
Polarity takes values in $\mathbb{Z}_2 = \{0, 1\}$. The minimal-discrete angular structure.

---

## 7. Constructive Necessity

This section derives $U(1)$ from $\{C^*\}$ + background mathematics + the empirical-recovery goal via five convergent routes.

### 7.1 Route A.1: Continuity necessary

The substrate's structural-normative goal C*4 requires support for empirically observed continuous-phase interference. Concrete examples:

- **Mach-Zehnder interferometry.** Gradual tuning of a phase shifter produces a continuous-tuning fringe pattern: as $\theta$ varies continuously from $0$ to $2\pi$, the output intensity varies continuously as $\cos^2(\theta/2)$.
- **Aharonov-Bohm experiment.** Continuous variation of magnetic flux through a solenoid produces continuous variation of the interference pattern. At any flux value, the substrate must support a corresponding continuous phase content.
- **Atomic / molecular interferometry.** Continuous wavelength variation in matter-wave interferometers (Bose-Einstein condensates, molecular interferometers up to Eibenberger-Fein scales) produces continuous fringe variation.

Any substrate-level angular primitive must support these continuous-phase phenomena. The substrate's angular primitive must therefore be a *continuous* topological group.

**Excluded by Route A.1:**
- **A1 ($\mathbb{Z}_n$):** Discrete cyclic groups support only $n$ distinct angular values. Substrate-derived phase content would inherit this discreteness; the substrate could not produce continuous-tuning fringes — only $n$-discrete-stepped fringes. Empirically refuted at all observed precision.
- **A4 ($\mathbb{Z}$):** Same continuity issue.
- **B3 ($p$-adic):** $p$-adic groups are not continuous in the standard topological sense; their natural topology is totally disconnected. Substrate-derived phase content would not vary continuously in the empirical sense.
- **B4 (fractal):** Fractal subsets of $S^1$ are totally disconnected; same continuity issue.
- **B6 ($\mathbb{Z}_2$):** Only two angular values; trivially fails continuity.

**Conclusion of Route A.1.** Angular primitive must be a continuous topological group. Surviving candidates: $U(1)$, $T^n$ ($n \geq 2$), $\mathbb{R}$, $SO(3)$, $SU(2)$, $U(n)$, $U(1) \times \mathbb{Z}_n$ (partial continuity in the $U(1)$ component, but $\mathbb{Z}_n$ component still discrete — addressed in §7.2).

### 7.2 Route A.2: Compactness necessary via Frobenius classification

The substrate's angular primitive must act on substrate carriers (bandwidth, channels, locus structure). For this action to be *bounded* and produce a closed substrate-level operational structure, the angular primitive must be *compact*.

**Frobenius classification (1878).** Any finite-dimensional associative real division algebra is isomorphic to $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{H}$. The substrate's downstream amplitude-carrier algebra (forced in Paper #1 to be $\mathbb{C}$) is the algebra carrying a faithful action of the angular primitive. For the action to be faithful and the algebra to be one of the Frobenius-classified options:

- **$\mathbb{R}$ as carrier algebra:** $\mathbb{R}$ has no continuous compact non-trivial group action (only $\mathbb{Z}_2$ for $\pm 1$ and the trivial group). The substrate's continuous-phase requirement would not be supported.
- **$\mathbb{C}$ as carrier algebra:** $\mathbb{C}$ has a natural $U(1)$ action: $z \mapsto e^{i\theta} z$. Compact, continuous, abelian. Matches the standard QM phase structure.
- **$\mathbb{H}$ as carrier algebra:** $\mathbb{H}$ has $SU(2) \cong S^3$ as its group of unit quaternions; the $SU(2)$ action is compact and continuous but *non-abelian*. Quaternionic-Hilbert-space QM frameworks (Adler 1995; Finkelstein et al. 1962) exist mathematically but fail empirically: quaternionic QM produces additional structural predictions (e.g., higher-dimensional spin content, additional symmetries) that are not observed empirically.

For the substrate-level angular primitive's action on the carrier algebra to be admissible under Frobenius classification + compactness + empirical adequacy, the carrier must be $\mathbb{C}$ and the angular primitive must be $U(1)$.

**Excluded by Route A.2:**
- **B1 ($\mathbb{R}$):** Non-compact. The substrate-level angular primitive acting on a Frobenius-classified algebra cannot be non-compact and produce closed substrate-level operations. $\mathbb{R}$ acting on $\mathbb{C}$ produces $e^{i\theta}$ for $\theta \in \mathbb{R}$, but this factors through $U(1)$ (since $e^{i\theta + 2\pi i k} = e^{i\theta}$ for integer $k$); the $\mathbb{R}$-structure adds unbounded winding-number content that the substrate has no mechanism to track or distinguish from the $U(1)$-content. The natural substrate-level structure is $U(1) = \mathbb{R} / 2\pi\mathbb{Z}$.

**Conclusion of Route A.2.** Angular primitive must be compact. Surviving continuous + compact candidates: $U(1)$, $T^n$ ($n \geq 2$), $SO(3)$, $SU(2)$, $U(n)$.

### 7.3 Route A.3: Abelian-ness necessary

The substrate's angular primitive is *intrinsic to each channel* at each locus — it is a per-channel local quantity, not a channel-coupling structure. Channel-channel coupling at the substrate level is a separate structural commitment, addressed by the gauge-field structure of Paper #5 (downstream) and ultimately by P10 (rule-type primitive, pending M-11).

For an angular primitive intrinsic to each channel:

- The primitive must act *commutatively* on the channel's amplitude content: the order of multiple phase rotations within a single channel must not matter. If $\pi_K \in G$ for some group $G$, then for two angular values $g_1, g_2 \in G$, the substrate must satisfy $g_1 \cdot g_2 = g_2 \cdot g_1$ (acting on the channel's amplitude).
- Non-abelian primitive structure would imply that phase rotations within a single channel fail to commute, contradicting the per-channel-intrinsic character.

**Excluded by Route A.3:**
- **A5 ($SO(3)$):** Non-abelian compact connected Lie group. $SO(3)$ acting per-channel would require channel content carrying a 3-dimensional rotation structure, which contradicts P09's character as a *single* angular variable per channel.
- **B2 ($SU(2)$):** Non-abelian, same issue. Note: $SU(2)$ in standard QM is the *gauge group of spin-1/2*, which is a downstream rule-type primitive (P10's content, addressed in Paper #5's T17 and Paper #7's Dirac equation); it is not the substrate-level angular primitive of P09.
- **B5 ($U(n)$ for $n \geq 2$):** Non-abelian for $n \geq 2$. Same issue.

**Conclusion of Route A.3.** Angular primitive must be an abelian Lie group. Surviving compact connected abelian Lie groups: $U(1)$ (rank 1) and $T^n = U(1)^n$ for $n \geq 2$ (rank $n$).

### 7.4 Route A.4: 1-dimensionality necessary + compositional closure

Multiple independent angular primitives ($T^n$ for $n \geq 2$) would correspond to *multiple independent phases* per channel. The substrate's structural-normative empirical-recovery goal requires polarity to be a *single* angular variable per channel — chains in physical reality carry a single phase, not multiple independent phases.

Additionally, M-2's four-band partition (forced upstream by M-2, downstream of M-1 but cross-referenced for compositional consistency) gives each channel a *single* bandwidth $b_K$ per channel per locus (with internal further partition into the four bands, but bandwidth itself is one quantity per channel). The single-phase-per-channel structure aligns with the single-bandwidth-per-channel structure: each channel carries one $(b_K, \pi_K)$ pair, not one $b_K$ with multiple $\pi_K^{(1)}, \pi_K^{(2)}, \ldots, \pi_K^{(n)}$ independent angular components.

**Compositional closure** (per $\{C^*\}$ C*5) requires the substrate's primitive operational categories to compose consistently. Multi-phase-per-channel content would either:
- Force a multi-bandwidth-per-channel companion structure (contradicting M-2's single-bandwidth identification), or
- Leave the multiple phases incommensurate with the single bandwidth (compositional inconsistency).

Either failure mode violates compositional closure.

**Excluded by Route A.4:**
- **A2 ($T^n$ for $n \geq 2$):** Multiple independent angular primitives per channel. Violates single-phase-per-channel + compositional closure with M-2.
- **A3 ($U(1) \times \mathbb{Z}_n$ for $n \geq 2$):** Hybrid continuous-discrete. The $\mathbb{Z}_n$ component is a second independent discrete angular variable; same single-phase violation as A2.
- **B5 ($U(n)$ for $n \geq 2$):** Already excluded by A.3 (non-abelian); but even the abelian rank of $U(n)$ at the maximal-torus level (which is $T^n$) is excluded by A.4.

**Conclusion of Route A.4.** Angular primitive must be 1-dimensional abelian compact Lie group. The unique survivor is $U(1)$.

### 7.5 Route E: Coecke-Kissinger categorical-QM necessity

The Coecke-Kissinger framework (Coecke & Kissinger 2017) classifies *continuous-classical-structures* on dagger-symmetric-monoidal categories (the categorical-QM analog of "observables in QM") via dagger-Frobenius algebras. A continuous-classical-structure is the categorical structure corresponding to a continuous classical observable; in standard QM, it corresponds to a maximal commuting set of self-adjoint operators.

For a continuous-classical-structure of dimension 1 (single continuous observable) on a dagger-symmetric-monoidal category modeling substrate-level participation content:

- The unique 1-dimensional continuous self-dual abelian dagger-Frobenius algebra (modulo isomorphism) corresponds to the $L^2(S^1)$ Frobenius algebra, which is the Coecke-Kissinger categorical encoding of $U(1)$.
- Discrete alternatives ($\mathbb{Z}_n$) correspond to discrete dagger-Frobenius algebras of finite dimension; these are not continuous-classical-structures.
- Non-self-dual or non-abelian alternatives fail the dagger-Frobenius classification for continuous-classical-structures.

**Independent route confirmation:** Route E independently arrives at $U(1)$ from a different starting point (category theory rather than algebraic-Lie-group analysis). The convergence with Routes A.1–A.4 provides over-determined forcing.

**Conclusion of Route E.** Categorically, the unique 1-dimensional continuous-classical-structure on a dagger-symmetric-monoidal category is the one corresponding to $U(1)$.

### 7.6 Route B: Operational-adequacy cross-check

Beyond the constructive routes A.1–A.4 + E, operational adequacy provides a cross-check:

- Empirical physics requires the substrate to support continuous-phase interference (Mach-Zehnder, Aharonov-Bohm, atomic interferometry — already invoked in Route A.1).
- Empirical physics requires the substrate to support the $U(1)$ gauge group of electromagnetism (downstream content of Paper #5).
- Empirical physics requires the substrate to support the $U(1)$ phase factor in standard QM wavefunctions.

Each of these empirical observations is consistent with the substrate having $U(1)$ as its angular primitive. None of the excluded alternatives ($\mathbb{Z}_n$, $\mathbb{R}$, $\mathbb{Z}$, $SO(3)$, $SU(2)$, $T^n$, hybrid, $p$-adic, fractal, $\mathbb{Z}_2$, no-angular-primitive) is consistent with the joint empirical observations.

**Conclusion of Route B.** Operational adequacy confirms $U(1)$ as the unique angular primitive consistent with empirical physics.

### 7.7 Convergent forcing

Five independent routes (A.1, A.2, A.3, A.4, E) plus operational-adequacy cross-check (B) all converge on $U(1)$:

- A.1 continuity excludes discrete and totally-disconnected alternatives.
- A.2 compactness via Frobenius excludes non-compact alternatives.
- A.3 abelian-ness excludes non-abelian alternatives.
- A.4 1-dimensionality excludes multi-dimensional torus alternatives.
- E Coecke-Kissinger excludes non-self-dual / non-abelian dagger-Frobenius structures.
- B operational adequacy cross-checks empirically.

Any one route alone substantially narrows the candidate space; the joint application uniquely selects $U(1)$. The forcing is **over-determined** — robust against single-route failure or single-objection counterargument.

**Conclusion of §7.** P09's $U(1)$-valued structure is forced by joint Routes A.1 + A.2 + A.3 + A.4 + E (with Route B cross-check) under $\{C^*\}$ + background mathematics + the structural-normative empirical-recovery goal.

---

## 8. Exclusion Arguments

Each A-series and B-series alternative is excluded by one or more of the convergent forcing routes.

### 8.A. A-series exclusions

**A1. $\mathbb{Z}_n$ (discrete cyclic).**
- Violates Route A.1: discrete angular content cannot support empirically observed continuous-phase interference (Mach-Zehnder, Aharonov-Bohm continuous tuning).
- Violates Route E: discrete dagger-Frobenius algebras are not continuous-classical-structures.
*Excluded by Routes A.1 and E.*

**A2. $T^n$ for $n \geq 2$ (multi-dimensional torus).**
- Violates Route A.4 + compositional closure: multiple independent angular primitives per channel contradict single-phase-per-channel empirical observation and conflict with M-2's single-bandwidth structure.
*Excluded by Route A.4.*

**A3. $U(1) \times \mathbb{Z}_n$ (hybrid continuous-discrete).**
- Violates Route A.1 (in the $\mathbb{Z}_n$ component): discrete content cannot support continuous interference.
- Violates Route A.4: multiple independent angular primitives per channel.
*Excluded by Routes A.1 and A.4.*

**A4. $\mathbb{Z}$ (integer-winding non-compact discrete).**
- Violates Route A.1: discrete content.
- Violates Route A.2: non-compact.
*Excluded by Routes A.1 and A.2.*

**A5. $SO(3)$ or $SU(2)$ (compact connected non-abelian).**
- Violates Route A.3: non-abelian content cannot serve as a per-channel intrinsic primitive without inducing channel coupling at the primitive level.
*Excluded by Route A.3.*

**A6. No angular primitive at all.**
- Violates Route B operational adequacy: empirically observed continuous-phase interference requires some continuous angular substrate content. Without P09, the substrate cannot support the empirical interference phenomenology.
- Equivalently: the participation measure of Paper #1, the Born rule, and all downstream QM content cannot be derived without an angular primitive.
*Excluded by Route B (operational adequacy).*

### 8.B. B-series exclusions

**B1. $\mathbb{R}$ (real-line non-compact).**
- Violates Route A.2 (compactness via Frobenius): non-compact angular primitive cannot act on Frobenius-classified algebras to produce closed substrate operations. $\mathbb{R}$ acting on $\mathbb{C}$ factors through $U(1)$; the substrate-level natural structure is $U(1)$ itself, not the covering $\mathbb{R}$.
*Excluded by Route A.2.*

**B2. $SU(2)$ (compact non-abelian — distinct treatment from A5).**
- Same exclusion as A5: Violates Route A.3 abelian-ness.
- Additional note: $SU(2)$ in standard QM is the spin-1/2 gauge group, downstream content of Paper #5's T17 and Paper #7's Dirac equation. Its appearance there is via the rule-type primitive (P10, pending M-11), not via P09. Conflating P09 with $SU(2)$ confuses substrate-level intrinsic phase with downstream gauge structure.
*Excluded by Route A.3.*

**B3. $p$-adic angular content.**
- Violates Route A.1: $p$-adic groups are totally disconnected (their natural topology has no continuous-tuning structure).
- Violates Route E: $p$-adic groups do not produce standard continuous-classical-structure dagger-Frobenius algebras in the Coecke-Kissinger framework.
*Excluded by Routes A.1 and E.*

**B4. Fractal-valued angular content.**
- Violates Route A.1: fractal subsets of $S^1$ or $\mathbb{R}$ are totally disconnected; cannot support continuous interference.
*Excluded by Route A.1.*

**B5. $U(n)$ for $n \geq 2$.**
- Violates Route A.3: non-abelian for $n \geq 2$.
- Violates Route A.4: maximal-torus rank $n \geq 2$ would correspond to multiple independent phases.
- Note: $U(n)$ as a *downstream gauge group* (e.g., for combined $U(1) \times SU(N-1)$ Standard-Model structure) is downstream content of Paper #5's T17 + Paper #8's DCGT, not substrate-level angular primitive.
*Excluded by Routes A.3 and A.4.*

**B6. $\mathbb{Z}_2$ (sign-flip only).**
- Same exclusion as A1: discrete cyclic, fails continuity (Route A.1).
- Empirically refuted: $\mathbb{Z}_2$ would support only $\pm 1$ phase content, contradicting all continuous-tuning observations.
*Excluded by Route A.1.*

### 8. Summary

| Alternative | Violates | Excluded by |
|---|---|---|
| A1 $\mathbb{Z}_n$ | Continuity + categorical | Routes A.1, E |
| A2 $T^n$ ($n \geq 2$) | Single-phase-per-channel + compositional closure | Route A.4 |
| A3 $U(1) \times \mathbb{Z}_n$ | Continuity (discrete component) + single-phase | Routes A.1, A.4 |
| A4 $\mathbb{Z}$ | Continuity + compactness | Routes A.1, A.2 |
| A5 $SO(3)$ / $SU(2)$ | Abelian-ness | Route A.3 |
| A6 No angular primitive | Empirical adequacy | Route B |
| B1 $\mathbb{R}$ | Compactness via Frobenius | Route A.2 |
| B2 $SU(2)$ (gauge-spin) | Abelian-ness | Route A.3 |
| B3 $p$-adic | Continuity + categorical | Routes A.1, E |
| B4 Fractal | Continuity | Route A.1 |
| B5 $U(n)$ ($n \geq 2$) | Abelian-ness + single-phase | Routes A.3, A.4 |
| B6 $\mathbb{Z}_2$ | Continuity | Route A.1 |

**Unique survivor: $U(1)$.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifiers

**F1. Empirical observation of genuinely $\mathbb{Z}_n$-valued angular content.**
Discovery of a physical phenomenon requiring the substrate's primitive angular content to be discrete (not merely effectively discrete via coarse-graining of a $U(1)$ structure). Would falsify Route A.1.

*Honest assessment.* All empirically observed phase content is continuous at observed precision. Even discrete-spectrum quantum systems (atoms, qubits) have continuous Rabi-oscillation phase between discrete eigenstates. No known phenomenon requires fundamentally discrete substrate-level phase.

**F2. Empirical observation of non-$U(1)$ abelian phase structure.**
Discovery of a fundamental phenomenon requiring a $T^n$ ($n \geq 2$) phase structure per channel — i.e., multiple independent continuous phases per substrate channel. Would falsify Route A.4.

*Honest assessment.* Multi-mode quantum optics (orbital-angular-momentum modes, frequency-comb modes) involves multiple channels with $U(1)$ phases each; this is the substrate's *multi-channel* structure, not a multi-phase-per-channel structure. No empirical phenomenon requires the latter.

**F3. Empirical observation of non-abelian per-channel phase.**
Discovery of a fundamental phenomenon requiring non-abelian phase structure intrinsic to a single channel. Would falsify Route A.3.

*Honest assessment.* Non-abelian gauge structures (electroweak, QCD, spin) are *gauge-field rule-types* with non-abelian phase transport across channels (P10 / Paper #5's T17 / Paper #7's spinors); the per-channel matter-field phases remain $U(1)$. No empirical phenomenon contradicts this.

**F4. Empirical observation of preferred-frame phase structure.**
Discovery that the substrate-level angular primitive has a preferred frame or origin. Would suggest $\mathbb{R}$ rather than $U(1)$ (since $\mathbb{R}$ has a preferred origin point). Would falsify Route A.2.

*Honest assessment.* All empirical phase observations are independent of an absolute phase origin (the global $U(1)$ gauge symmetry — substrate-level statement of which is Paper #16's phase-independence-of-bandwidth result).

**F5. Failure of Frobenius classification.**
Discovery that finite-dim associative real division algebras exist beyond $\{\mathbb{R}, \mathbb{C}, \mathbb{H}\}$. Would weaken Route A.2.

*Honest assessment.* Frobenius classification is one of the most thoroughly verified results in algebra (over 140 years since Frobenius 1878). Falsifying it is extraordinarily unlikely.

### 9.2 Structural falsifiers

**F6. Coecke-Kissinger framework inconsistency.**
Discovery that the Coecke-Kissinger classification of continuous-classical-structures via dagger-Frobenius algebras is flawed or incomplete. Would weaken Route E.

*Honest assessment.* Coecke-Kissinger 2017 is established categorical-QM mathematics; the classification of continuous-classical-structures via Frobenius algebras is robust.

**F7. Alternative compact 1-dim abelian Lie group.**
Discovery of a compact connected 1-dim abelian Lie group distinct from $U(1)$. Would refute the uniqueness of $U(1)$.

*Honest assessment.* The classification theorem (Cartan-Killing) is settled mathematics: the unique compact connected 1-dim abelian Lie group is $U(1)$ (up to isomorphism). Falsifying this is mathematically impossible.

### 9.3 Empirical exposure downstream

Closing P09 upstream of Forcing Papers #1–#19 exposes the following downstream-level structures to empirical test:

- **Paper #1 (Participation Measure).** The complex Hilbert space arena's derivation now operates on substrate-level forced $U(1)$ polarity. Empirical confirmation of complex-amplitude QM (interference, Bell-Tsirelson, double-slit, quantum-eraser experiments) confirms M-1's forcing.
- **Paper #5 (Gauge T17).** The $U(1)$ gauge group of electromagnetism now inherits from M-1's $U(1)$ polarity. Empirical confirmation of $U(1)$ gauge invariance in QED at all observed precision confirms M-1.
- **Paper #16 (Phase-Independence).** The global $U(1)$ gauge redundancy of QM observable predictions now inherits from M-1. Empirical confirmation that global phases are unobservable confirms M-1.
- **Walkthroughs on Aharonov-Bohm, Berry phase, photonic Chern channels.** All involve continuous $U(1)$ phase content; all consistent with M-1's $U(1)$ forcing.

---

## 10. Appendix: Derivation Chain + Glossary + Status

### 10.1 Derivation chain summary

```
Meta-Substrate Framework {C*}
       │
       ▼
M-1 INPUT: Existence of an angular primitive (under C*4 empirical-recovery goal)
       │
       ▼
M-1 Five-route convergent forcing:
   ├─── Route A.1: Continuity ──────────► excludes discrete (A1, A4, B3, B4, B6)
   ├─── Route A.2: Compactness via Frobenius ──► excludes non-compact (B1)
   ├─── Route A.3: Abelian-ness ─────────► excludes non-abelian (A5, B2, B5)
   ├─── Route A.4: 1-dimensionality + compositional closure ──► excludes T^n (A2, A3)
   ├─── Route E: Coecke-Kissinger ────────► excludes non-categorical-classical (B3)
   └─── Route B: Operational-adequacy ────► cross-check (excludes A6)
       │
       ▼
M-1 OUTPUT: P09 ($U(1)$ polarity) FORCED
       │
       ▼
Downstream Updates:
   ├─── Paper #1 (Participation Measure: $\mathbb{C}$ as carrier algebra)
   ├─── Paper #2 (Born Rule: uniform-$U(1)$ phase-randomization inherits)
   ├─── Paper #3 (Inner Product + Tsirelson)
   ├─── Paper #5 (Gauge T17: $U(1)$ gauge group)
   ├─── Paper #16 (Phase-Independence)
   └─── Paper #17 (Four Postulates Unified)
```

### 10.2 Cross-references

**Meta-Paper M0** (`paper_M0_primitive_forcing_meta_paper_UPDATED.md`):
- §5 Meta-substrate framework $\{C^*\}$.
- §5.1 Primitive Centrality Analysis — P09 listed as HIGH-centrality.
- §5.2 Forcing Priority Order — M-1 = P09 first closure.
- §6.1 Roadmap sketch for P09 forcing.

**Dependency Graph** (`DEPENDENCY_GRAPH_ED.md`):
- §1.1 P09 primitive definition.
- §2 Master Dependency Table — P09 load-bearing in Papers #1, #2, #3, #5, #16, #17.
- §4.1 HIGH-centrality classification.
- §5 Downstream Update Map — P09 closure updates 6 papers.

**M-2 Paper, M-3 Paper, M-4 Paper.** Downstream of M-1. Use M-1's $U(1)$ closure for:
- M-2: structural consistency with bandwidth (P04) vs. polarity (P09) primitive distinction.
- M-3: uniform-$U(1)$ phase-randomization at commitment inherits from M-1 + Haar measure.
- M-4: $U(1)$ representations of symmetry generators (Stone's theorem on Hilbert spaces with $U(1)$-valued unitary group).

**Phase-1 Revisions** (`REVISIONS_PHASE1_abstracts_claims_scope.md`):
- Papers #1, #2, #3, #5, #16, #17 §3.0 entries explicitly name P09 as load-bearing input.

**Update Plan after M-1** (`UPDATE_PLAN_after_M1.md`): per-paper surgical §3.0 update specifications, applied 2026.

### 10.3 Glossary extensions (beyond §4)

- **Maximum-entropy principle on $U(1)$.** Under no-additional-information about a distribution on $U(1)$, the maximum-entropy distribution is the Haar measure (uniform on $S^1$). Used in M-3's argument for uniform-$U(1)$ phase-randomization at commitment.
- **Inönü-Wigner contraction.** Group-theoretic limit procedure used in M-4 to relate Poincaré to Galilean. Independent of M-1.
- **Dagger-symmetric-monoidal category.** A symmetric monoidal category equipped with a dagger functor (involutive contravariant identity-on-objects functor). The categorical encoding of quantum mechanics in Coecke-Kissinger.
- **Frobenius algebra.** An associative algebra equipped with a non-degenerate bilinear pairing satisfying the Frobenius condition. In Coecke-Kissinger, dagger-Frobenius algebras correspond to classical structures (continuous-classical-structures correspond to continuous observables).
- **Haar measure.** The unique (up to normalization) left-invariant measure on a locally compact topological group. For $U(1)$, the Haar measure is the standard uniform measure on $S^1$.

### 10.4 Status

This is Paper M-1 of the ED Primitive-Forcing M-series. With M-1 closed:

- **P09 ($U(1)$-valued polarity) is FORCED** under joint Routes A.1 + A.2 + A.3 + A.4 + E (with Route B cross-check) from meta-substrate $\{C^*\}$ + background mathematics + the structural-normative empirical-recovery goal.
- **6 downstream papers** (#1, #2, #3, #5, #16, #17) have their §3.0 entries for P09 converted from "load-bearing input" to "forced upstream by M-1 (2026)."

### 10.5 Series Context

Cumulative status across the ED Primitive-Forcing M-series after M-1 closure:

- **M-1 (this paper, 2026):** P09 $U(1)$ polarity — FORCED.
- **M-2 (subsequent):** P04 four-band partition + bandwidth additivity — FORCED.
- **M-3 (subsequent):** P11 commitment irreversibility + uniform-$U(1)$ phase-randomization — FORCED; commitment-existence residue.
- **M-4 (subsequent):** Joint symmetry cluster P03 + P13 + GAL + POI — FORCED; cosmological-curvature residue.
- **M-5 onward:** P07, V1 + V5 existence, HYD, residue closures.

After M-1, the displaced-postulate critique no longer applies to P09 specifically. Other primitives' critique applicability remains pending their respective M-papers.

### 10.6 Honest closing

This paper does not eliminate all unforced roots. The meta-substrate framework $\{C^*\}$ itself remains the recursion-stopping commitment. The substrate's commitment to *some* angular primitive (rather than no angular primitive at all) is part of the meta-substrate's structural-normative goal of recovering empirically observed continuous-phase interference, invoked here as given.

What M-1 achieves: the conversion of P09 from a displaced postulate (assumed at the substrate level to produce the complex-Hilbert-space arena downstream) to an explicitly named structural consequence (forced by joint Routes A.1–A.4 + E from $\{C^*\}$ + background mathematics). The reviewer's critique — *"the postulate 'the substrate has a U(1)-valued angular primitive' already contains the answer"* — is structurally correct *as applied to the pre-M-1 program*, but no longer applies after M-1: P09 is now upstream-forced, not postulated.

The kernel-level structural coherence of the ED program advances its first step. M-2 onward addresses the remaining load-bearing primitives.

---

**End of Paper M-1.**
