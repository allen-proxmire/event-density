# Schrödinger Dynamics Emerges in the Thin-Participation Limit — FORCED

**Paper #13 of the Event Density Forcing Series (Wave 2, Paper 3)**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-13
**Series:** Event Density (ED) Forcing Papers — Paper #13 of the program
**Genre:** Forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

The Schrödinger equation $i\hbar\,\partial_t\Psi = \hat{H}\Psi$ was forced in Paper #4 via Stone's theorem applied to the participation-manifold Hilbert space. This paper supplies a structurally distinct route: the Schrödinger equation emerges as the **continuum limit of substrate-level discrete-channel dynamics in the thin-participation regime**. **Given the substrate primitives of Papers #1–#4 plus the thin-participation regime ($M_\mathrm{eff} \to \infty$, $b_\mathrm{env} \to 0$, $\Gamma_\mathrm{commit} \to 0$) and the substrate-level per-channel evolution rule $i\hbar\,\partial_t P_K = H_K P_K + \sum_{K'} V_{KK'} P_{K'}$**, the continuum limit produces the standard Schrödinger PDE on the coherent-sum wavefunction $\Psi(x,t) = \sum_K P_K(x,t)$. The two routes (Stone's theorem on the assumed arena, thin-limit continuum coarse-graining) converge on the same equation; together they over-determine the result. The claim is conditional on the per-channel evolution rule, which is itself a substrate-level structural commitment derived from bandwidth conservation + commitment-event timing. The thin-participation regime is empirically robust for canonical QM (single-particle Schrödinger experiments operate in this regime); outside it, the substrate's discrete-channel content is what is fundamental.

---

## 1. Framing

### 1.1 Why a second derivation of the Schrödinger equation?

Paper #4 of this series established the Schrödinger equation as a forcing theorem: given the participation-manifold Hilbert space and time-homogeneity, Stone's theorem produces a unique self-adjoint generator whose differential form is
$$
i\hbar\,\partial_t P(t) = \hat{H}\,P(t).
$$
The argument is rigorous and complete — but it operates *on the Hilbert space*. It takes the Hilbert-space arena as input (supplied by Papers #1-#3) and shows that time evolution on that arena must be unitary with a Hermitian generator.

A natural complementary question is: how does the Schrödinger PDE on the position-space wavefunction $\Psi(x, t)$ — the form physicists actually use — arise from the substrate's discrete-channel dynamics? The substrate operates on discrete channels $K$ at discrete loci $u$; the wavefunction $\Psi(x, t)$ on continuous position $x$ is an emergent continuum object. How does the discrete-to-continuum transition produce specifically the Schrödinger form?

### 1.2 The puzzle

Three sub-puzzles arise:

1. **Linearity from substrate dynamics.** Per-channel dynamics could in principle be nonlinear in the participation measure. What forces the continuum-limit equation to be linear?
2. **First-order time evolution.** Per-channel dynamics could in principle have higher time-derivatives. What forces the continuum equation to be first-order?
3. **Complex amplitude structure.** The continuum equation involves $i\hbar$ on the left-hand side. What forces this specifically?

Standard treatments answer these questions either by analogy (canonical quantization, classical-mechanics correspondence) or by postulation (Hilbert-space evolution must be unitary). Neither derives the Schrödinger form from a discrete substrate via an explicit continuum-limit mechanism.

### 1.3 What this paper does

The Event Density (ED) framework supplies the substrate. Papers #1-#3 establish the participation-measure carrier, the Born rule, and the sesquilinear inner product. Paper #4 establishes Schrödinger via Stone's theorem on time-translations. Paper #11 establishes Heisenberg from the four-band partition. Paper #12 establishes the momentum operator $\hat{p} = -i\hbar\nabla$ via Stone's theorem on spatial-translations.

The present paper supplies the **substrate-level continuum-limit route** to Schrödinger. Specifically:

1. **The thin-participation regime** is defined as the substrate-level limit $M_\mathrm{eff} \to \infty$ (many channels participating coherently, no single dominant channel) with environmental and commitment-reserve bands suppressed.
2. **The per-channel participation-measure dynamics** $i\hbar\,\partial_t P_K = H_K P_K + \sum_{K'} V_{KK'} P_{K'}$ takes a forced linear first-order form at the substrate level — a structural consequence of bandwidth conservation + commitment-event timing.
3. **The continuum limit** $K \to k$ (momentum basis in the thin regime) produces the coherent sum $\Psi(x, t) = \int dk\,P_k(x, t)$ as a complex-valued continuum field.
4. **The Schrödinger PDE** $i\hbar\,\partial_t\Psi = \hat{H}\Psi$ with $\hat{H} = -\hbar^2\nabla^2/(2m) + V(x)$ emerges as the unique continuum-limit equation when the per-channel coefficients $H_K$ and $V_{KK'}$ are identified with the momentum-space representation of the kinetic-plus-potential Hamiltonian.

The two routes — Stone's theorem (Paper #4) and thin-participation continuum limit (this paper) — produce the same equation via different machinery. Their convergence is over-determined forcing.

**Series context.** Papers #1-#3 supply the kinematic backbone; Paper #4 supplies the Stone-theorem route to Schrödinger; Papers #11-#12 supply the Heisenberg and momentum-operator sides. The present paper supplies the substrate-level continuum-limit route to Schrödinger as a complementary derivation, completing the program's pair of independent forcings of the Schrödinger dynamics.

---

## 2. Claim

> **Forcing Theorem (Schrödinger from Thin-Participation Limit, conditional).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#4 results, thin-participation regime, per-channel evolution rule*. Then the coherent-sum wavefunction satisfies the standard Schrödinger PDE.
>
> *The thin-participation regime is load-bearing; outside it (e.g., environmental decoherence, active commitment events), discrete substrate content dominates and continuum Schrödinger does not apply.*

---

## 3. Scope

### 3.0 Primitive Inputs (postulated substrate axioms)

This paper takes the following inputs as **postulated**:

- **THN (thin-participation regime):** $M_\mathrm{eff} \to \infty$, $b_\mathrm{env} \to 0$, $\Gamma_\mathrm{commit} \to 0$. Substrate-level operational limit in which continuum Schrödinger emerges. Outside this regime, substrate-level discrete dynamics dominate.
- **P04 (bandwidth conservation under per-channel evolution):** the substrate-level dynamical equation $i\hbar\,\partial_t P_K = H_K P_K + \sum_{K'} V_{KK'} P_{K'}$ preserves bandwidth (Shannon-Khinchin axiom 4 applied at the substrate level).
- **Papers #1–#4 results.**

The full 13-primitive substrate axiom set is enumerated in the ED Foundations position paper. The empirical case for the postulates rests on their downstream reach across domains. This paper's contribution: given the postulates above, the standard Schrödinger PDE on the coherent-sum wavefunction $\Psi(x,t) = \sum_K P_K(x,t)$ is the unique continuum-limit equation. The two routes to Schrödinger (Paper #4's Stone-theorem route + this paper's thin-limit continuum coarse-graining) converge on the same equation.

### 3.1 What is FORCED

- **Linearity** of the continuum-limit evolution equation.
- **First-order-in-time** structure of the evolution.
- **Complex-valued amplitude** structure: the $i\hbar$ coefficient on the left-hand side.
- **Kinetic operator** $-\hbar^2\nabla^2/(2m)$ in the position representation.
- **Potential operator** $V(\hat{x})$ as a local multiplication operator.
- **Schrödinger PDE form** $i\hbar\,\partial_t\Psi = \hat{H}\Psi$ on the coherent-sum wavefunction.
- **Equivalence with Paper #4's Stone-theorem route** — the two routes converge on the same equation.

### 3.2 What is INHERITED

- **Numerical value of $\hbar$**. Inherited via the Madelung anchoring (same as Papers #4, #6, #11, #12).
- **Inertial mass $m$**. Inherited per the H1-dominant verdict of Arc M (Paper #6 §7.5): mass appears as a Lorentz-scalar bandwidth-signature functional whose numerical value is rule-type data.
- **Specific potential $V(x)$**. Determined by the chain's environmental coupling structure; inherited from value-layer empirical content.

### 3.3 What is OUT OF SCOPE

- **Relativistic wave equations** (Dirac, Klein-Gordon). Paper #7 territory.
- **Gauge-coupled Schrödinger** $i\hbar\,\partial_t\Psi = \frac{1}{2m}(\hat{p} - eA/c)^2\Psi + qA^0\Psi$. Downstream of Paper #5.
- **Many-particle / field-theoretic Schrödinger**. Single-particle scope here.
- **Open-system / Lindblad evolution**. Non-unitary modifications belong to a separate regime.

---

## 4. Key Vocabulary

- **Substrate.** Pre-quantum primitive layer of ED.
- **Channel.** Primitive structural pathway in the participation graph, indexed by $K$.
- **Participation measure $P_K(x, t)$.** Complex amplitude carrier $\sqrt{b_K}\,e^{i\pi_K}$ on each channel (Paper #1).
- **Effective multiplicity $M_\mathrm{eff}$.** Substrate quantity counting how many channels carry comparable participation bandwidth: $M_\mathrm{eff} = (\sum_K |P_K|^2)^2 / \sum_K |P_K|^4$. Large $M_\mathrm{eff}$ = many channels active coherently; small $M_\mathrm{eff}$ = one channel dominant.
- **Thin-participation regime.** Substrate regime characterized by $M_\mathrm{eff} \to \infty$, $b_\mathrm{env} \to 0$, $\Gamma_\mathrm{commit} \to 0$. Many coherent channels, no environmental decoherence, no active commitment events.
- **Coherent sum $\Psi(x, t)$.** $\sum_K P_K(x, t)$ (discrete) or $\int dK\,P_K(x, t)$ (continuum limit). The wavefunction.
- **Continuum limit $K \to k$.** In the thin regime, the discrete channel index $K$ becomes a continuous label $k$ identified with momentum.
- **Per-channel evolution.** Substrate-level dynamical equation for each channel's participation measure: $i\hbar\,\partial_t P_K = H_K P_K + \sum_{K'} V_{KK'} P_{K'}$.
- **Hamiltonian operator $\hat{H}$.** The kinetic-plus-potential operator $-\hbar^2\nabla^2/(2m) + V(\hat{x})$ in the position representation.

---

## 5. Substrate Class $\{C\}$

### C1. Participation graph + channel structure (Primitives P03 + P07)

Discrete participation graph with channels at each locus.

### C2. Bandwidth with additivity (Primitive P04)

Four-band partition: $b_K = b_K^\mathrm{int} + b_K^\mathrm{adj} + b_K^\mathrm{env} + b_K^\mathrm{com}$ with conservation along an isolated chain.

### C3. Polarity (Primitive P09)

$U(1)$-valued angular primitive on each channel.

### C4. Time homogeneity (Primitive P13) + spatial homogeneity (P03 + P06)

Continuous time and spatial axes with substrate-level translation symmetry.

### C5. Inherited results from Papers #1-#4 and #12

- **Paper #1**: participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$.
- **Paper #2**: Born rule $\text{Prob}(K) \propto |P_K|^2$.
- **Paper #3**: sesquilinear inner product on the participation manifold.
- **Paper #4**: linear unitary time evolution at the Hilbert-space level (the Stone-theorem result the present paper provides an independent derivation of).
- **Paper #12**: momentum operator $\hat{p} = -i\hbar\nabla$ as spatial-translation generator.

### C6. Per-channel substrate dynamics

The substrate supplies a per-channel dynamical equation for each participation-measure component:
$$
i\hbar\,\partial_t P_K(x, t) = H_K\,P_K(x, t) + \sum_{K'} V_{KK'}\,P_{K'}(x, t),
$$
with diagonal coefficients $H_K$ (per-channel "free" content) and off-diagonal coefficients $V_{KK'}$ (inter-channel coupling). The substrate-level form of this equation — linear, first-order in time, complex-coefficient — is itself a substrate-level structural commitment, established in the U3 / Schrödinger emergence work of Papers #1's substrate-foundation memos.

The linearity is forced by bandwidth additivity (C2) extended to time evolution: if two channels' contributions evolve independently, their sum's evolution is the sum of individual evolutions. The first-order time-derivative is forced by the substrate's commitment-event timing structure (Primitive P11) operating on discrete time-step content; higher-order derivatives would require additional initial-condition structure that the substrate does not supply.

The complex coefficient $i\hbar$ is forced by unitarity (C5 from Paper #4 inherited): real coefficients would produce non-unitary evolution.

### C7. Thin-participation regime

The continuum-limit derivation operates in the thin-participation regime, defined by three substrate-level conditions:

- **$M_\mathrm{eff} \to \infty$**: many channels carry comparable bandwidth; the chain is delocalized across the channel space.
- **$b_\mathrm{env} \to 0$**: environmental band suppressed; no environmental phase-randomization at the evolution timescale.
- **$\Gamma_\mathrm{commit} \to 0$**: no commitment events occur during the evolution.

This is the regime in which substrate-level dynamics matches QM-level dynamics. Outside this regime — thick participation, with $M_\mathrm{eff} \sim O(1)$ — substrate dynamics deviates from Schrödinger; the deviation is the regime where Q-COMPUTE-class architectural limits (Arc Q-COMPUTE) become observable.

### C8. No Schrödinger PDE as input

The forcing argument invokes only C1-C7 plus standard Fourier analysis on $L^2(\mathbb{R}^d)$ and the operator correspondence between momentum-space and position-space representations.

---

## 6. Alternative Encodings

### 6.1 Structural alternatives

**A1. Nonlinear continuum limits.** Continuum-limit equation containing nonlinear terms in $\Psi$: $i\hbar\,\partial_t\Psi = \hat{H}\Psi + g|\Psi|^2\Psi$ (Gross-Pitaevskii-class), or other nonlinear modifications.

**A2. Higher-order time-derivative limits.** Continuum equation with $\partial_t^2$ or higher: $\partial_t^2\Psi = -\hat{H}^2\Psi/\hbar^2$ (Klein-Gordon-class on a non-relativistic carrier), or stochastic-process limits with higher time-derivatives.

**A3. Real-valued continuum limits.** Continuum equation without the imaginary $i\hbar$: real-valued evolution generators producing exponential growth / decay rather than unitary rotation.

**A4. Non-unitary continuum limits.** Equations that fail to preserve $\int|\Psi|^2dx$: dissipative or amplifying continuum dynamics.

**A5. Non-differential continuum limits.** Continuum equations involving non-local operators (integral kernels, non-differential operators) rather than the Laplacian.

**A6. Discrete-only / no-continuum-limit.** Substrate dynamics admits no continuum limit; remains discrete at all scales.

**A7. Channel-basis-dependent limits.** Continuum equations whose form depends on the choice of channel basis (energy vs. momentum vs. angular momentum), producing different PDEs for different choices.

### 6.2 Mainstream alternatives

**B1. Schrödinger as postulate.** $i\hbar\,\partial_t\Psi = \hat{H}\Psi$ adopted as a foundational axiom with no derivation.

**B2. Path-integral derivation.** Feynman's path-integral formulation produces Schrödinger as the differential form of the propagator. Path-integral measure and action principle taken as input.

**B3. Classical wave analogy.** de Broglie's wave hypothesis + Hamilton-Jacobi → Schrödinger. Classical mechanics + wave-particle duality taken as input.

**B4. Stochastic emergence (Nelson stochastic mechanics).** Schrödinger as an effective description of a stochastic Brownian-class process in configuration space. Stochastic substrate taken as input.

**B5. Schrödinger as semiclassical limit.** Schrödinger emerges as the small-$\hbar$ limit of some more-fundamental theory (e.g., string theory, geometric quantization). Different more-fundamental substrate.

**B6. Lattice-Schrödinger limit.** Continuum Schrödinger as $a \to 0$ limit of lattice Schrödinger on a discrete grid. Lattice taken as input regularization.

---

## 7. Constructive Necessity

The argument establishes Schrödinger in four steps.

### 7.1 The thin-participation regime

Define the **effective multiplicity** of a chain's participation:
$$
M_\mathrm{eff}(x, t) = \frac{\left(\sum_K |P_K(x, t)|^2\right)^2}{\sum_K |P_K(x, t)|^4}.
$$
This is the standard participation-ratio measure: $M_\mathrm{eff} = 1$ when one channel carries all bandwidth (single-channel state), $M_\mathrm{eff} = N$ when bandwidth is equally distributed across $N$ channels.

The **thin-participation regime** is the substrate condition $M_\mathrm{eff} \to \infty$ with the additional conditions $b_\mathrm{env} \to 0$ and $\Gamma_\mathrm{commit} \to 0$ from C7. In this regime, the chain participates coherently across a continuum of channels with no environmental decoherence and no active commitment events.

**Why this regime is the QM regime.** The thin-participation regime is the substrate-level condition in which the chain's behavior is governed by coherent superposition rather than by individual commitment events. Outside this regime — when $M_\mathrm{eff}$ is finite or commitment events are frequent — substrate dynamics deviates from QM toward classical-statistical or thick-participation behavior. The standard quantum-mechanical regime (atoms, molecules, mesoscopic systems with $\hbar \omega \gg k_B T$) corresponds to the thin-participation regime in ED.

### 7.2 Per-channel substrate dynamics

By C6, the substrate supplies the per-channel evolution
$$
i\hbar\,\partial_t P_K(x, t) = H_K\,P_K(x, t) + \sum_{K'} V_{KK'}\,P_{K'}(x, t).
$$
The form is **linear** in $P$ (from bandwidth additivity), **first-order** in $\partial_t$ (from commitment-event timing structure), and carries the complex coefficient $i\hbar$ (from unitarity).

In the thin-participation regime, the discrete channel index $K$ becomes a continuous label. By Paper #12 (spatial-translation symmetry produces the momentum operator), the natural continuous label is **momentum** $k$:
$$
K \to k \in \mathbb{R}^d.
$$
The momentum-basis identification is forced by Paper #12's Stone-theorem argument: the substrate's spatial-translation symmetry singles out momentum as the conjugate label to position, with plane waves as the basis.

In the momentum basis, each $P_k$ takes the form
$$
P_k(x, t) = c_k(t)\,\frac{e^{ikx}}{\sqrt{2\pi\hbar}},
$$
where $c_k(t)$ is the time-dependent amplitude of the $k$-mode. The per-channel coefficients identify with:
- **$H_k = \hbar^2 k^2/(2m)$**: the free-particle kinetic energy of a $k$-mode (diagonal in momentum basis). This identification is forced by Paper #6's Galilean Lie algebra closure, which produces the kinetic-energy form uniquely.
- **$V_{kk'} = \tilde{V}(k - k')$**: the Fourier transform of a local position-space potential $V(x)$. Local potentials in position space appear as convolution kernels in momentum space.

### 7.3 The coherent sum as the wavefunction

The thin-participation wavefunction is the coherent sum of per-channel participation measures:
$$
\Psi(x, t) = \int dk\,P_k(x, t) = \int dk\,\frac{c_k(t)}{\sqrt{2\pi\hbar}}\,e^{ikx}.
$$
This is the inverse Fourier transform of $c_k(t)$. $\Psi(x, t)$ is a complex-valued continuum field on spacetime — the QM wavefunction.

Normalization: by Plancherel's theorem on the Fourier-pair $(c_k, \Psi)$,
$$
\int dx\,|\Psi|^2 = \int dk\,|c_k|^2 = N,
$$
with $N = 1$ by convention.

### 7.4 Schrödinger PDE from the continuum-limit substitution

Apply $\int dk$ to both sides of the per-channel evolution equation:
$$
\int dk\,[i\hbar\,\partial_t P_k] = \int dk\,[H_k\,P_k + \sum_{k'} V_{kk'}\,P_{k'}].
$$

**Left-hand side:** $\int dk\,i\hbar\,\partial_t P_k = i\hbar\,\partial_t\int dk\,P_k = i\hbar\,\partial_t\Psi$.

**Right-hand side, kinetic term:** Substitute $H_k = \hbar^2 k^2/(2m)$:
$$
\int dk\,\frac{\hbar^2 k^2}{2m}\,P_k = \int dk\,\frac{\hbar^2 k^2}{2m}\,\frac{c_k(t)}{\sqrt{2\pi\hbar}}\,e^{ikx}.
$$
Using the Fourier identity $k^2 \leftrightarrow -\nabla^2$ (i.e., $-\nabla^2(e^{ikx}) = k^2 e^{ikx}$), this becomes
$$
-\frac{\hbar^2}{2m}\nabla^2\Psi(x, t).
$$

**Right-hand side, potential term:** Substitute $V_{kk'} = \tilde{V}(k - k')$:
$$
\int dk\,\int dk'\,\tilde{V}(k - k')\,P_{k'} = \int dk'\,P_{k'}\int dk\,\tilde{V}(k - k') = V(x)\,\Psi(x, t),
$$
where the last equality uses the convolution-theorem identity: a convolution in momentum space corresponds to a pointwise product in position space, with $V(x)$ the inverse Fourier transform of $\tilde{V}$.

**Combining:**
$$
\boxed{\;i\hbar\,\partial_t\Psi(x, t) = \left[-\frac{\hbar^2}{2m}\nabla^2 + V(x)\right]\Psi(x, t).\;}
$$

This is the **Schrödinger equation** on the coherent-sum wavefunction $\Psi(x, t)$. The form is forced by:
- Linearity (preserved under $\int dk$ from the per-channel linearity of C6).
- First-order time derivative (preserved under $\int dk$).
- Complex $i\hbar$ coefficient (preserved under $\int dk$).
- Kinetic operator $-\hbar^2\nabla^2/(2m)$ from the momentum-basis $H_k$ identification (Paper #6).
- Potential operator $V(x)$ from the momentum-basis-to-position-basis Fourier correspondence.

**Equivalence with Paper #4's Stone-theorem route.** Paper #4 starts from the Hilbert-space arena and produces, via Stone's theorem on time-translations, the operator-form equation $i\hbar\,\partial_t P(t) = \hat{H}P(t)$. The present paper starts from the substrate's discrete-channel dynamics and produces, via the thin-participation continuum limit, the PDE on $\Psi(x, t)$. The two routes converge: the Hilbert-space operator equation of Paper #4, applied to the position-representation wavefunction, *is* the Schrödinger PDE of the present paper. Either route alone establishes the result; together they over-determine it.

---

## 8. Exclusion Arguments

### 8.1 A1 — Nonlinear continuum limits

The per-channel substrate dynamics (C6) is linear: bandwidth additivity (C2) forces independent channels to evolve independently, with their sum's evolution equal to the sum of individual evolutions. Linearity is preserved under the continuum-limit $\int dk$ (linear operations commute with integration). A nonlinear continuum limit would require either nonlinear per-channel dynamics (violating C6) or a non-linear continuum-limit operation (violating Fourier analysis).

Empirically observed nonlinear Schrödinger-class equations (Gross-Pitaevskii for BECs) are *effective* descriptions of many-body systems where mean-field self-interaction produces a nonlinear term in the single-particle approximation. At the substrate level, the full many-body equation is linear in the multi-particle wavefunction; the nonlinearity arises from a mean-field reduction, not from substrate-level nonlinearity.

### 8.2 A2 — Higher-order time-derivative limits

Per-channel dynamics is first-order in $\partial_t$ by C6 (commitment-event timing structure). Higher-order derivatives would require additional initial-condition structure that the substrate's participation-measure framework does not supply (only $P_K(t=0)$ is specified; not $\partial_t P_K(t=0)$). The continuum-limit equation inherits the first-order time-derivative structure.

Klein-Gordon-class equations $(\Box + m^2c^2/\hbar^2)\Psi = 0$ are relativistic (Paper #7) with mixed space-time second-derivatives forced by Lorentz covariance — different scope.

### 8.3 A3 — Real-valued continuum limits

The complex coefficient $i\hbar$ in the per-channel equation (C6) is forced by unitarity (C5 inherited from Paper #4): real coefficients would produce non-unitary evolution that does not preserve $\int dx |\Psi|^2$. The complex structure is preserved under the continuum-limit $\int dk$.

### 8.4 A4 — Non-unitary continuum limits

Equivalent to A3: non-unitarity requires real generator coefficients, excluded by C5.

### 8.5 A5 — Non-differential continuum limits

The Fourier identity $k^2 \leftrightarrow -\nabla^2$ is a mathematical fact about the standard Fourier transform on $L^2(\mathbb{R}^d)$, established in Paper #12's spatial-translation-symmetry argument. A non-differential continuum limit would require either a non-Fourier basis-change (excluded by Paper #12's exclusion of fractional-Fourier, wavelet, Mellin alternatives) or a non-local kernel structure $V_{kk'}$ that does not factor through the convolution theorem (excluded by C4's spatial homogeneity, which forces local position-space potentials).

### 8.6 A6 — Discrete-only / no-continuum-limit

The thin-participation regime (C7) is a substrate-level limit empirically realized in atomic, molecular, mesoscopic, and condensed-matter systems at sub-decoherence timescales. Substrate dynamics empirically does admit a continuum limit in this regime; a discrete-only substrate would contradict observed quantum-mechanical phenomenology.

### 8.7 A7 — Channel-basis-dependent limits

Different channel-basis choices (energy, momentum, angular momentum) produce equivalent Schrödinger PDEs related by unitary basis changes. The momentum basis is the *natural* choice because Paper #12 shows that spatial-translation symmetry singles out momentum as the conjugate label to position. Other bases produce the same equation expressed in different coordinates — not different equations.

### 8.8 B1 — Schrödinger as postulate

Adopting Schrödinger as a foundational axiom is *downstream* of the substrate forcing. The present paper derives the equation from substrate primitives; treating it as a postulate is a presentation choice.

### 8.9 B2 — Path-integral derivation

Feynman's path-integral formulation produces Schrödinger as the differential form of the propagator $K(x, t; x', t') = \int \mathcal{D}x(\tau)\,e^{iS[x]/\hbar}$. The path-integral measure and the action principle are inputs. Under the substrate-conditions test, the path-integral is downstream of the substrate-level participation-measure dynamics: each channel's contribution can be reinterpreted as a path-integral history, with the per-channel sum corresponding to the path-integral measure. The path-integral and the substrate-level approach are equivalent reformulations.

### 8.10 B3 — Classical wave analogy

The de Broglie wave hypothesis + Hamilton-Jacobi route produces Schrödinger heuristically from classical-mechanics analogy. The present paper produces it from substrate primitives without invoking classical mechanics. The two routes converge on the same equation; the substrate route is upstream.

### 8.11 B4 — Stochastic emergence (Nelson)

Nelson's stochastic mechanics derives Schrödinger from a Brownian-class stochastic process in configuration space. Under the substrate-conditions test, Nelson's substrate (stochastic Brownian process) is different from ED's substrate (participation graph with discrete channels). The two are not directly comparable as substrate-level alternatives; they are different choices of pre-quantum substrate.

### 8.12 B5 — Schrödinger as semiclassical limit

Treating Schrödinger as a small-$\hbar$ limit of a more-fundamental theory (string theory, geometric quantization) is downstream of choosing that more-fundamental theory. ED's substrate is upstream of string theory (the participation graph is more primitive than worldsheet conformal field theory); the substrate-conditions test produces Schrödinger directly from the substrate, not as a limit.

### 8.13 B6 — Lattice-Schrödinger limit

Lattice Schrödinger is a regularization of the continuum Schrödinger; both arise from the substrate-level discrete-to-continuum transition in the thin-participation regime. The present paper's substrate forcing supplies the *physical* lattice (the participation graph); lattice formulations approximate this with a chosen lattice spacing.

### 8.14 Summary of exclusions

| Alternative | Violates | Reason |
|---|---|---|
| A1 nonlinear limits | C2, C6 | Bandwidth additivity forces linear per-channel dynamics; preserved under continuum limit. |
| A2 higher-order time | C6 | Commitment-event timing forces first-order; substrate provides no extra initial-condition structure. |
| A3 real-valued limits | C5 (unitarity) | Real coefficients produce non-unitary evolution; $i\hbar$ forced. |
| A4 non-unitary limits | C5 | Equivalent to A3. |
| A5 non-differential | Paper #12 + C4 | Fourier identity $k^2 \leftrightarrow -\nabla^2$ forced by spatial homogeneity. |
| A6 no continuum limit | empirical + C7 | Thin-participation regime empirically realized in QM systems. |
| A7 basis-dependent limits | Paper #12 | Momentum basis singled out by spatial-translation symmetry; other bases equivalent. |
| B1 Schrödinger as postulate | not in space | Downstream of substrate forcing. |
| B2 path-integral | reformulation | Equivalent to substrate-level summation; downstream of substrate. |
| B3 classical wave analogy | heuristic only | Substrate route is upstream and rigorous. |
| B4 Nelson stochastic | different substrate | Stochastic Brownian substrate vs. ED participation graph; not directly comparable. |
| B5 semiclassical limit | downstream | Of choosing the more-fundamental theory; substrate produces directly. |
| B6 lattice Schrödinger | regularization | Approximates substrate's physical lattice. |

**The Schrödinger PDE $i\hbar\,\partial_t\Psi = [-\hbar^2\nabla^2/(2m) + V(x)]\Psi$ is the unique substrate-derived continuum-limit equation in the thin-participation regime.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifier

Any reproducible observation of nonlinear, higher-order, non-unitary, or non-differential evolution at the kinematic level in the thin-participation regime (atomic, molecular, mesoscopic systems with $\hbar\omega \gg k_BT$) would falsify the substrate forcing along with standard Schrödinger QM. Specific constraints:

- **Weinberg-nonlinearity bounds** ($< 10^{-21}$ from atomic-spectroscopy + NMR experiments) constrain A1 alternatives. Substrate prediction: identically zero.
- **GRW/CSL collapse-rate bounds** constrain non-unitary modifications. Substrate prediction: at the kinematic level in the thin regime, the evolution is unitary; commitment-event content lives outside the thin-participation regime.
- **Atomic and molecular spectra** test the kinetic-plus-potential structure to very high precision; all observed data consistent with the substrate-derived Schrödinger PDE.

### 9.2 Structural falsifier

Construct a substrate satisfying C1-C8 (participation graph, four-band partition, polarity, time + spatial homogeneity, Papers #1-#4 + #12 inherited, per-channel linear first-order dynamics, thin-participation regime, no Schrödinger PDE as input) but supporting a non-Schrödinger continuum-limit equation that survives the exclusion arguments of §8. The author's claim is that no such substrate exists.

### 9.3 Downstream exposure

**Atomic physics.** Hydrogen energy levels follow from solving Schrödinger with the Coulomb potential. Every spectroscopy result depends on the substrate-derived PDE.

**Condensed-matter and mesoscopic systems.** Bloch-electron dynamics, quantum-dot states, semiconductor electronics — all governed by the substrate-derived Schrödinger PDE in the thin-participation regime.

**Quantum-computing kinematic content.** Qubit dynamics in the thin-participation regime (between commitment events) follows the substrate-derived Schrödinger PDE. Deviations at the Q-COMPUTE multiplicity wall (Arc Q-COMPUTE) are the substrate-level signature of leaving the thin regime.

---

## Appendix A — Derivation Chain and Glossary

### A.1 The momentum-basis identification — explicit

In the thin-participation regime, the continuous channel index $K$ becomes a continuous label. Paper #12 §7.2 establishes that spatial-translation symmetry on the participation manifold produces $\hat{p} = -i\hbar\nabla$ as the unique self-adjoint translation generator, with plane waves $e^{ipx/\hbar}$ as the eigenbasis. The momentum-basis identification $K \to k$ is the natural continuous extension of the channel index that diagonalizes the translation generator.

Plane-wave $k$-mode amplitudes:
$$
P_k(x, t) = \frac{c_k(t)}{\sqrt{2\pi\hbar}}\,e^{ikx},
$$
with $c_k(t)$ the time-dependent momentum-space amplitude. The coherent sum
$$
\Psi(x, t) = \int dk\,P_k(x, t) = \int\frac{dk}{\sqrt{2\pi\hbar}}\,c_k(t)\,e^{ikx}
$$
is the inverse Fourier transform of $c_k$, satisfying Plancherel.

### A.2 The Fourier-identity argument for $-\hbar^2\nabla^2/(2m)$ — explicit

Each $k$-mode has kinetic-energy coefficient $H_k = \hbar^2 k^2/(2m)$ (Paper #6 §7.4 forces this form via the Galilean integration Jacobian). The continuum-limit kinetic contribution:
$$
\int dk\,H_k\,P_k = \int\frac{dk}{\sqrt{2\pi\hbar}}\,\frac{\hbar^2 k^2}{2m}\,c_k(t)\,e^{ikx}.
$$
Recognizing $k^2 e^{ikx} = -\nabla^2 e^{ikx}$:
$$
\int dk\,H_k\,P_k = -\frac{\hbar^2}{2m}\nabla^2\int\frac{dk}{\sqrt{2\pi\hbar}}\,c_k(t)\,e^{ikx} = -\frac{\hbar^2}{2m}\nabla^2\Psi(x, t).
$$

### A.3 The convolution-theorem argument for $V(x)\Psi$ — explicit

Each pair of channels $(k, k')$ has off-diagonal coefficient $V_{kk'} = \tilde{V}(k - k')$, the Fourier transform of the local position-space potential $V(x)$. The continuum-limit potential contribution:
$$
\int dk\,\sum_{k'}V_{kk'}\,P_{k'}(x, t) = \int dk\,\int dk'\,\tilde{V}(k - k')\,P_{k'}(x, t).
$$
By the convolution theorem (a convolution in $k$-space is a pointwise product in $x$-space), this equals $V(x)\,\Psi(x, t)$.

### A.4 Glossary

- **Channel.** Primitive structural pathway in the participation graph.
- **Coherent sum $\Psi(x, t)$.** $\int dK\,P_K(x, t)$; the continuum wavefunction.
- **Effective multiplicity $M_\mathrm{eff}$.** $(\sum_K |P_K|^2)^2/\sum_K |P_K|^4$; participation-ratio measure.
- **FORCED.** Derived from substrate primitives + standard mathematics with no additional commitments.
- **Hamiltonian operator $\hat{H}$.** $-\hbar^2\nabla^2/(2m) + V(\hat{x})$ in position representation.
- **INHERITED.** Quantitative content ($\hbar$, $m$, specific $V(x)$) used but not derived in this paper.
- **Kinetic operator.** $-\hbar^2\nabla^2/(2m)$; momentum-space form $\hbar^2 k^2/(2m)$.
- **Momentum basis.** Channel-basis identification $K \to k$ singled out by spatial-translation symmetry (Paper #12).
- **Participation measure $P_K(x, t)$.** Complex amplitude carrier $\sqrt{b_K}\,e^{i\pi_K}$ on each channel.
- **Per-channel dynamics.** $i\hbar\,\partial_t P_K = H_K P_K + \sum_{K'} V_{KK'}P_{K'}$ (C6).
- **Plancherel theorem.** $\int dx|\Psi|^2 = \int dk|c_k|^2$ for Fourier-conjugate pairs.
- **Potential operator.** $V(\hat{x})$ acting as multiplication-by-$V(x)$ in position representation.
- **Schrödinger PDE.** $i\hbar\,\partial_t\Psi = \hat{H}\Psi$ on the coherent-sum wavefunction.
- **Substrate.** Pre-quantum primitive layer of ED.
- **Thin-participation regime.** $M_\mathrm{eff} \to \infty$, $b_\mathrm{env} \to 0$, $\Gamma_\mathrm{commit} \to 0$.

### A.5 Source-repository citations (for ED-internal readers)

- `arcs/arc-foundations/schrodinger_emergence.md` — QM Step 2 derivation memo for Schrödinger emergence in the thin-participation limit.
- `arcs/U3/04_closure_and_summary.md` — Paper #4's Stone-theorem route to the same equation.
- `arcs/U4/04_closure_and_summary.md` — Galilean Lie algebra → kinetic-energy form (Paper #6).
- `arcs/U5/04_closure_and_summary.md` — Stone's theorem on spatial translations (Paper #12).
- `walkthroughs/from_primitives_to_schrodinger_equation.md` — public-facing walkthrough.

These are *not* required reading for the present paper.

---

*End of Paper #13.*
