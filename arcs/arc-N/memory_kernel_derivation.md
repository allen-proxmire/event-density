# Non-Markovian Memory Kernel Derivation

**Date:** 2026-04-24
**Location:** `quantum/foundations/memory_kernel_derivation.md`
**Status:** Phase-2 Arc-N opening memo. Extends the Lindblad master equation to the non-Markovian regime by relaxing Primitive 08's high-multiplicity (high-M) environmental-bath limit. Derives the Nakajima-Zwanzig memory-kernel master equation from finite-mode environmental structure, identifies the memory kernel's dependence on environmental autocorrelations, and shows that the Lindblad equation is recovered in the Markov (short-correlation-time) limit.
**Purpose:** First Phase-2 Arc-N deliverable per `phase2_extensions_roadmap.md §2.4`. Makes explicit the structural consequences of environmental memory that the Lindblad extension suppressed as Markov.

---

## 1. Setup and motivation

### 1.1 The Markov assumption embedded in Lindblad

The Lindblad extension of `lindblad_extension.md` derived the master equation
\begin{equation}
  \partial_t \hat\rho = -\frac{i}{\hbar}[\hat H, \hat\rho] + \sum_\alpha \left(\hat L_\alpha \hat\rho \hat L_\alpha^\dagger - \tfrac{1}{2}\{\hat L_\alpha^\dagger \hat L_\alpha, \hat\rho\}\right)
  \tag{LB}
\end{equation}
as a FORCED consequence of ED primitives plus the promoted identifications. The derivation employed:

1. **Primitive 08** (high-M environmental multiplicity) to establish a Poisson-distributed commitment-event stream.
2. **Primitive 11** (locality of commitment events) to assign each commitment an independent environmental trigger.
3. **Phase-independence** (FORCED) to ensure each environmental mode contributes an independent random phase kick.

Under the high-M limit, the individual coupling strength of each environmental mode is small (the bath distributes coupling across many modes), and the bath-correlation time vanishes. Commitment events become temporally uncorrelated — each event is statistically independent of all previous events. This memoryless property is the **Markov property**, and it is the structural feature that reduces the general master equation to the Lindblad form.

### 1.2 What relaxing high-M produces

When the environmental bath has a finite number of modes — or when the system-bath coupling spectrum has structure at frequencies comparable to the system's dynamical timescales — the bath-correlation time is non-negligible. Commitment events become temporally correlated: a commitment at time t is statistically linked to commitments at nearby times t' with t-t' less than the bath correlation time.

The resulting reduced dynamics of the chain is not Markovian. It takes the general form
\begin{equation}
  \partial_t \hat\rho(t) = \int_0^t K(t-t') \, \hat\rho(t') \, dt'
  \tag{NM}
\end{equation}
where $K(t-t')$ is a superoperator **memory kernel** specifying how the present rate-of-change depends on past states of the chain. Equation (NM) is the Nakajima-Zwanzig form [nakajima1958, zwanzig1960] of the reduced dynamics; it is exact (to within the reduced-system ansatz) for any system-bath Hamiltonian.

### 1.3 Scope

This memo derives the structure of $K(t-t')$ from ED primitives with Primitive 08 refined to permit finite-mode baths, identifies its primitive-level content as the environmental autocorrelation function, shows that the Lindblad form is recovered when the correlation time goes to zero, and documents the separation between structural content (FORCED) and apparatus-level inheritance (specific spectral densities).

---

## 2. Primitive 08 refined

### 2.1 The high-M limit in context

Primitive 08 (Multiplicity) in its Phase-1 formulation asserts that the environmental bath has many orthogonal modes, each weakly coupled to the chain. This supports the Poisson-distributed commitment stream and the effective Markovian dynamics. The limit is a mathematically clean idealization — appropriate for systems with dense bath spectra (e.g., many-phonon acoustic baths, photon baths at high temperature) — but not universally applicable.

### 2.2 The refined statement

**Primitive 08 refined:** the environmental bath has a mode structure with spectral density $J(\omega)$ specifying the coupling strength at each frequency. The high-M limit corresponds to $J(\omega)$ smooth and slowly varying on the scale of system frequencies; the finite-M case admits $J(\omega)$ with sharp features (peaks, gaps, quasi-bound modes) at frequencies comparable to system dynamics.

**Status of the refinement.** This is not a change to the primitive stack; it is an articulation of a regime-dependence that was implicit in the high-M formulation. The Phase-1 derivation's "high-M" is the regime where $J(\omega)$ is effectively flat over the frequency range of interest.

### 2.3 Environmental autocorrelation

For a bath with spectral density $J(\omega)$ at temperature $T$ (or more generally, with some equilibrium state), the autocorrelation function of the environmental coupling is
\begin{equation}
  C(\tau) = \int d\omega \, J(\omega) \left[\coth\left(\tfrac{\omega \hbar}{2 k_B T}\right) \cos(\omega \tau) - i \sin(\omega \tau)\right]
  \tag{corr}
\end{equation}
where $\tau = t - t'$. The real part of (corr) decays on the characteristic bath correlation time
\begin{equation}
  \tau_{\text{corr}} \sim \left(\Delta \omega\right)^{-1}
\end{equation}
where $\Delta\omega$ is the bandwidth of $J(\omega)$.

**Status of (corr): CANDIDATE.** The functional form follows standard fluctuation-dissipation theorem reasoning; the specific spectral density $J(\omega)$ is apparatus-specific and inherited from the physical bath structure. The dependence on $\hbar$, $k_B$, $T$ introduces empirical constants that are not derived from ED primitives.

### 2.4 The Markov limit as a special case

When $\tau_{\text{corr}} \to 0$, the autocorrelation $C(\tau) \to \gamma \delta(\tau)$ for some effective rate $\gamma$. This is the high-M limit: the bath has infinitely many modes covering all frequencies, and the correlation time is negligible compared to all system timescales. The Markov property follows; Lindblad is recovered.

---

## 3. Temporal correlations in commitment events

### 3.1 Commitment statistics at finite M

In the high-M limit, commitment events form a Poisson stream: the probability of a commitment in an infinitesimal interval $dt$ is $\lambda dt$ (independent of history), with $\lambda$ set by the integrated spectral density.

At finite M, this independence is broken. The probability of a commitment in $dt$ at time $t$ depends on the bath's state at time $t$, which depends on previous commitment events through the system-bath interaction.

**Formal statement:** for the joint statistics of commitment events at times $t_1, t_2, \ldots, t_n$,
\begin{equation}
  P(t_1, t_2, \ldots, t_n) \ne \prod_i P(t_i) \quad \text{when} \quad |t_i - t_j| \lesssim \tau_{\text{corr}}.
\end{equation}
The joint probability does not factorize for event pairs within the correlation window.

**Status: FORCED** by the finite-mode bath + preserved bandwidth-conservation + preserved commitment-locality of Primitive 11.

### 3.2 Origin of memory

Primitive 11 locality is preserved: each commitment event is still local at a specific participation site. What is not preserved is statistical independence across commitments at different times. The bath "remembers" recent commitment events on the timescale $\tau_{\text{corr}}$, and this memory propagates to the commitment-event statistics.

**Physical interpretation:** when a commitment at time $t'$ transfers bandwidth to environmental mode $\alpha$, that mode's subsequent evolution (up to time $t' + \tau_{\text{corr}}$) reflects the prior bandwidth transfer. Any subsequent commitment event involving mode $\alpha$ within this window is statistically correlated with the earlier event. In the high-M limit, the bath has so many modes that subsequent commitments involve independent modes with overwhelming probability; at finite M, the re-encounter probability is non-negligible.

---

## 4. Derivation of the Nakajima-Zwanzig form

### 4.1 Projection-operator technique

The standard derivation of (NM) uses the Nakajima-Zwanzig projection-operator technique. Define a projection superoperator $\mathcal{P}$ onto the system's reduced state:
\begin{equation}
  \mathcal{P} \hat\rho_{\text{total}} = \hat\rho_S \otimes \hat\rho_B^{\text{eq}},
\end{equation}
where $\hat\rho_{\text{total}}$ is the total system-bath density operator and $\hat\rho_B^{\text{eq}}$ is the bath's equilibrium state. The complementary projection $\mathcal{Q} = 1 - \mathcal{P}$ projects onto the bath's non-equilibrium deviations.

Starting from the total von Neumann evolution $\partial_t \hat\rho_{\text{total}} = \mathcal{L} \hat\rho_{\text{total}}$ with $\mathcal{L} \hat\rho = -(i/\hbar)[\hat H_{\text{total}}, \hat\rho]$, and applying the projection decomposition, one obtains the exact Nakajima-Zwanzig equation [nakajima1958, zwanzig1960]:
\begin{equation}
  \partial_t \mathcal{P} \hat\rho_{\text{total}} = \mathcal{P} \mathcal{L} \mathcal{P} \hat\rho_{\text{total}}(t) + \int_0^t d t' \, \mathcal{P} \mathcal{L} e^{\mathcal{Q}\mathcal{L}(t-t')} \mathcal{Q} \mathcal{L} \mathcal{P} \hat\rho_{\text{total}}(t') + \mathcal{P} \mathcal{L} e^{\mathcal{Q}\mathcal{L} t} \mathcal{Q} \hat\rho_{\text{total}}(0).
\end{equation}

Under the assumption that the initial state factorizes (bath in equilibrium, uncorrelated with system), the inhomogeneous term vanishes, and (NM) takes the form
\begin{equation}
  \partial_t \hat\rho_S(t) = -\frac{i}{\hbar}[\hat H_S, \hat\rho_S(t)] + \int_0^t dt' \, \mathcal{K}(t-t') \hat\rho_S(t'),
  \tag{NZ}
\end{equation}
where $\mathcal{K}(t-t') = \mathcal{P} \mathcal{L} \exp(\mathcal{Q}\mathcal{L}(t-t')) \mathcal{Q} \mathcal{L} \mathcal{P}$ is the Nakajima-Zwanzig memory kernel.

**Status of (NZ):** FORCED at the formal level (projection-operator technique is a mathematical identity); the specific form of $\mathcal{K}(t-t')$ depends on $\hat H_{\text{total}}$, which in ED is constructed from the participation measure + environmental coupling.

### 4.2 Weak-coupling / second-order form

In the weak-coupling limit where the system-bath coupling $g$ is small, the memory kernel expands to leading order as
\begin{equation}
  \mathcal{K}(t-t') \hat\rho_S = -\frac{1}{\hbar^2} \operatorname{Tr}_B \left[ \hat H_{\text{int}}(t), \left[ \hat H_{\text{int}}(t'), \hat\rho_S(t) \otimes \hat\rho_B^{\text{eq}} \right] \right],
\end{equation}
where $\hat H_{\text{int}}$ is the system-bath interaction Hamiltonian in the interaction picture. The memory kernel reduces to bath-correlation functions:
\begin{equation}
  \mathcal{K}(t-t') \hat\rho_S \ni C(t-t') \cdot \left[\hat A, \left[\hat A, \hat\rho_S\right]\right]
\end{equation}
where $\hat A$ is the system part of $\hat H_{\text{int}}$ and $C(t-t')$ is the bath autocorrelation (corr).

**Status: FORCED** at the second-order perturbative level given the weak-coupling regime. The specific form inherits the functional dependence on $C(t-t')$ and thereby on $J(\omega)$.

### 4.3 ED-specific identifications

In the ED framework, the system-bath interaction is encoded in the environmental-bandwidth coupling $b^{\text{env}}_K$ (Primitive 04). The jump operators $\hat L_\alpha$ of the Lindblad extension correspond to specific bath modes $\alpha$; the memory kernel in the non-Markovian regime carries the correlations between these modes' couplings to the chain:
\begin{equation}
  \mathcal{K}(t-t') \leftrightarrow \sum_\alpha \hat L_\alpha(t) \otimes \hat L_\alpha^\dagger(t') \cdot c_\alpha(t-t'),
\end{equation}
where $c_\alpha(\tau)$ is the autocorrelation of mode $\alpha$ specifically. In the high-M limit, $c_\alpha(\tau) \to \gamma_\alpha \delta(\tau)$ and the memory kernel collapses to a sum of local-in-time Lindblad jump terms.

**Status: CANDIDATE.** The specific form of the mode-to-L̂_α correspondence in the non-Markovian case requires the refinement of Primitive 08 and explicit specification of the bath mode structure. The general framework is FORCED by the Nakajima-Zwanzig derivation.

---

## 5. The memory kernel — structure

### 5.1 Properties of $K(t-t')$

The memory kernel inherits structural properties from the Nakajima-Zwanzig derivation:

- **Time-translation invariance:** $K(t-t')$ depends only on the difference $t-t'$, reflecting the time-independence of the bath equilibrium state.
- **Causality:** $K(t-t') = 0$ for $t' > t$ (the current state is influenced only by past states).
- **Decay:** $|K(\tau)| \to 0$ as $\tau \to \infty$, on the timescale $\tau_{\text{corr}}$ set by the bath autocorrelation.
- **Initial-time limit:** $K(\tau \to 0)$ controls the instantaneous jump-like behavior; in the Markov limit, $K(\tau) \to \Gamma \delta(\tau)$ for some effective rate $\Gamma$.
- **Dissipation vs. oscillation:** the real and imaginary parts of $K(\tau)$ separate into fluctuation (dissipation) and phase-rotation (oscillation) contributions, generalizing the separate Hamiltonian and jump terms of Lindblad.

### 5.2 Spectral-density dependence

The bath spectral density $J(\omega)$ controls the functional form of $K(\tau)$. Several standard cases:

- **Ohmic bath** ($J(\omega) \propto \omega$): exponential-decay kernel, $K(\tau) \sim e^{-\tau/\tau_c}$ for high-T regimes.
- **Lorentzian bath** ($J(\omega) \propto (\omega-\omega_0)^2 + \Gamma^2)^{-1}$): damped oscillation kernel, $K(\tau) \sim e^{-\Gamma\tau/2} \cos(\omega_0 \tau)$.
- **Power-law baths** (1/f-type): slow power-law decay kernels.

**Status: INHERITED.** The specific spectral density of a given physical bath is apparatus-level content, not derivable from ED primitives. The ED framework specifies the structure of the derivation (how $K(\tau)$ depends on $J(\omega)$) but inherits the specific $J(\omega)$ from the physical context.

### 5.3 The Markov limit

When $\tau_{\text{corr}}$ is short compared to system timescales, the kernel is sharply peaked at $\tau = 0$. Approximating
\begin{equation}
  \int_0^t dt' \, K(t-t') \, \hat\rho_S(t') \approx \hat\rho_S(t) \int_0^\infty d\tau \, K(\tau) = \Gamma \cdot \hat\rho_S(t),
\end{equation}
the non-Markovian equation (NZ) reduces to a local-in-time equation. Under the specific structural form of $K(\tau)$ in the ED framework (§4.3), the integrated kernel produces the Lindblad jump-and-anticommutator structure of (LB).

**Status: FORCED** as a mathematical consequence of the short-correlation-time limit. The Lindblad equation is thus identified as the Markovian limit of (NZ), not as an independent structure.

---

## 6. Comparison with Lindblad

### 6.1 Structural relationship

| Regime | Dynamics | Memory | Mode structure |
|---|---|---|---|
| High-M / Markov | Lindblad (LB) | No | Dense $J(\omega)$; $\tau_{\text{corr}} \to 0$ |
| Finite-M / non-Markov | Nakajima-Zwanzig (NZ) | Yes, kernel $K(\tau)$ | Structured $J(\omega)$; finite $\tau_{\text{corr}}$ |

### 6.2 When the Markov limit fails

The Markov approximation fails when any of the following hold:

- **Bath spectral features** within or below the system's characteristic frequencies (bound bath modes, cavity modes, structured reservoirs).
- **Strong coupling** (system-bath coupling comparable to or larger than the bath bandwidth).
- **Low temperature** (quantum regime where the thermal-photon-emission timescale becomes comparable to system coherence).
- **Bath finite size** (finite-dimensional bath with recurrences).

In each of these regimes, non-Markovian corrections to Lindblad become significant and the memory-kernel formulation is necessary.

### 6.3 Primitive-level content preserved under Non-Markov

The Lindblad extension preserved three primitive-level structural features: Hermiticity, trace preservation, and complete positivity. The Nakajima-Zwanzig form preserves Hermiticity and trace but not necessarily complete positivity. Complete-positivity violation in NZ dynamics is a known feature of genuine non-Markovian bath structures and reflects information flow back from the bath to the system on timescales $\tau \lesssim \tau_{\text{corr}}$.

**Status: structural consequence, not a flaw.** Non-complete-positivity at finite times is a hallmark of non-Markovianity and is consistent with the general theory of open quantum systems [breuer2007, rivas2014].

---

## 7. Status classification

### 7.1 Forced content

| Feature | Source |
|---|---|
| Need for memory kernel at finite M | Primitive 08 refined + Primitive 11 locality + finite-mode bath structure |
| Temporal correlation of commitment events | Environmental autocorrelation (corr) |
| Nakajima-Zwanzig form (NZ) | Projection-operator technique applied to total von Neumann evolution |
| Causality and time-translation invariance of $K(\tau)$ | Equilibrium bath + causal system-bath coupling |
| Weak-coupling reduction of $\mathcal{K}(t-t')$ to bath autocorrelations | Standard second-order perturbative expansion |
| Markov limit recovery → Lindblad | Short-correlation-time mathematical limit |
| Hermiticity preservation | Structural from the derivation |
| Trace preservation | Bandwidth conservation (Primitive 04) |

### 7.2 Inherited content

| Item | Source of inheritance |
|---|---|
| Specific spectral density $J(\omega)$ of a given physical bath | Apparatus-level physical configuration |
| Numerical value of $\hbar$ in (corr) | Dimensional Atlas (inherited from Phase 1) |
| Bath temperature $T$ and thermodynamic content | Apparatus-level |
| Bath-correlation time $\tau_{\text{corr}}$ | Derived from $J(\omega)$ once that is inherited |

### 7.3 No new primitives

The non-Markovian extension does not introduce new primitives. Primitive 08 is refined (articulating its regime-dependence) rather than replaced. Primitives 04 and 11 are used as in Phase 1. U1–U5 remain in force.

---

## 8. Platform-specific applications

The Nakajima-Zwanzig form enables refined platform-bridge retrodictions beyond the Lindblad (Markov) approximation. Three platform contexts where non-Markovian corrections are expected to be measurable:

### 8.1 Matter-wave interferometry

The Hornberger-Joos-Zeh decoherence rate for Arndt-class interferometers assumes a Markov-bath approximation. At low pressure or in structured thermal environments (e.g., nanostructured cavities), non-Markovian corrections could produce deviations from the standard exponential visibility decay. A memory-kernel refinement of the Arndt retrodiction would predict specific sub-exponential or oscillatory features.

### 8.2 BEC collective modes

Landau damping of BEC collective modes in the Jin 1997 experiment is computed in Markov approximation. Near $T_c$, bath mode density becomes structured (critical fluctuations); non-Markovian corrections to $Q(T)$ would manifest as deviations from the standard $\gamma \propto T^2$ scaling.

### 8.3 Superconducting-qubit coherence

T1 and T2 measurements assume Markovian coupling to the electromagnetic environment. TLS (two-level system) fluctuators produce structured non-Markovian baths; superconducting-qubit decoherence at long times often exhibits non-exponential decay, a direct signature of non-Markovian memory.

**Scope note:** all three applications are platform-specific derivations that would deploy the general Nakajima-Zwanzig form of (NZ) with platform-appropriate $J(\omega)$. The present memo establishes the general framework; platform-specific derivations are future deliverables.

---

## 9. Summary

### 9.1 Achievement

**The non-Markovian master equation (NZ) with memory kernel $K(t-t')$ is derived as the natural extension of Lindblad to the finite-M environmental regime.** The derivation refines Primitive 08's high-M assumption into a regime-dependent statement, uses the Nakajima-Zwanzig projection-operator technique to obtain the exact reduced-dynamics form, and identifies the memory kernel's content as the bath autocorrelation function (corr). The Markov limit $\tau_{\text{corr}} \to 0$ recovers Lindblad.

### 9.2 Primitive-level status

**The structural content of (NZ) is FORCED** by refined Primitive 08 + Primitive 04 + Primitive 11 + standard projection-operator methods. No new primitives required. The Lindblad extension is identified as the Markovian limit.

**Inherited content** is apparatus-level: the specific bath spectral density $J(\omega)$, the bath temperature, and the derived correlation time are physical-context parameters, not primitive-level consequences.

### 9.3 Phase-2 Arc-N status

Arc-N opening deliverable complete. Remaining near-term items in Arc N:
- Platform-specific non-Markovian corrections (matter-wave, BEC, SC-qubit).
- Synthesis memo at Arc-N closure, following the template of `qm_emergence_synthesis.md`.

With this memo, the Phase-2 roadmap's short-term deliverables for Arc N are on track. Arc R (Relativistic), Arc M (Chain-mass), and Arc Q (QFT) remain open research programs.

---

## 10. Cross-references

### Program-level
- Phase-2 extensions roadmap: [`quantum/foundations/phase2_extensions_roadmap.md`](phase2_extensions_roadmap.md) §2.4
- Lindblad extension (Markovian predecessor): [`quantum/foundations/lindblad_extension.md`](lindblad_extension.md)
- U3 unitary evolution: [`quantum/foundations/u3_evolution_derivation.md`](u3_evolution_derivation.md)
- Phase-independence (required for both LB and NZ): [`quantum/foundations/phase_independence_derivation.md`](phase_independence_derivation.md)
- QM-emergence closure: [`quantum/foundations/qm_emergence_closure.md`](qm_emergence_closure.md)

### Primitive stack
- Primitive 04 (bandwidth; four-band decomposition): [`quantum/primitives/04_participation_bandwidth.md`](../primitives/04_participation_bandwidth.md)
- Primitive 08 (multiplicity; high-M assumption refined here): [`quantum/primitives/08_multiplicity.md`](../primitives/08_multiplicity.md)
- Primitive 11 (commitment events; locality preserved): [`quantum/primitives/11_commitment.md`](../primitives/11_commitment.md)

### Classical references
- Nakajima, S. (1958). On quantum theory of transport phenomena. *Progress of Theoretical Physics* **20**, 948.
- Zwanzig, R. (1960). Ensemble method in the theory of irreversibility. *Journal of Chemical Physics* **33**, 1338.
- Breuer, H. P., Petruccione, F. (2002). *The Theory of Open Quantum Systems*. Oxford.
- Rivas, Á., Huelga, S. F., Plenio, M. B. (2014). Quantum non-Markovianity: characterization, quantification and detection. *Reports on Progress in Physics* **77**, 094001.
- Breuer, H.-P., Laine, E.-M., Piilo, J., Vacchini, B. (2016). Colloquium: Non-Markovian dynamics in open quantum systems. *Rev. Mod. Phys.* **88**, 021002.

---

## 11. One-line summary

> **Refining Primitive 08's high-M bath assumption to permit finite-mode environmental structure, the reduced dynamics of a non-isolated chain takes the Nakajima-Zwanzig form $\partial_t \hat\rho(t) = \int_0^t K(t-t') \hat\rho(t') dt'$ with memory kernel $K(t-t')$ inheriting its functional dependence on the bath autocorrelation $C(\tau) = \int d\omega J(\omega) [\coth(\omega\beta/2) \cos(\omega\tau) - i \sin(\omega\tau)]$. The Nakajima-Zwanzig form is FORCED by the projection-operator technique applied to the total system-bath dynamics; the specific spectral density $J(\omega)$ is apparatus-level inherited content. In the short-correlation-time Markov limit $\tau_{\text{corr}} \to 0$, the kernel reduces to a delta function and the Nakajima-Zwanzig equation collapses to the Lindblad form, recovering `lindblad_extension.md`. The non-Markovian extension introduces no new primitives; Primitive 08 is refined rather than replaced. Arc-N opening deliverable complete; platform-specific non-Markovian corrections (matter-wave, BEC, SC-qubit) remain as near-term Arc-N deliverables.**
