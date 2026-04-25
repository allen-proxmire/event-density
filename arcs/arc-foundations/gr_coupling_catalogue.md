# Catalogue of Admissible Curvature-Coupling Structures

**Phase-3 Stage GR.1 — Catalogue Memo**
**Status:** Catalogue only. Enumerates every curvature-coupling structure consistent with ED Primitives 01–13, Phase-2 theorems, and Arc N's Theorem N1, across four sectors: GR-1 bandwidth-curvature (5 items), GR-2 vacuum-curvature (5 items, **primary target**), GR-3 worldline-curvature (5 items), GR-4 curvature-dynamics (5 items). Each item characterised by primitive dependencies and potential constraint-violation flags (C1 Lorentz / general covariance, C2 spin-statistics, C3 UV-FIN, locality from Primitive 11). **No FORCED / REFUTED evaluation in this memo** — those are Stage GR.2 and GR.3 deliverables. The catalogue's purpose is to ensure no admissible curvature-coupling structure is missed before evaluation begins.

---

## 1. Framing

### 1.1 Phase-3 inputs (recap)

The Phase-3 opening memo [1] established:

- ED-Phys-10 [2] supplies the **kinematic acoustic metric** for bandwidth-mode perturbations on a smooth bandwidth background. **No Einstein equations, no Schwarzschild, no Newtonian-gravity emergence at long-wavelength** are produced by ED-Phys-10. This is a structural ceiling Phase-3 must respect or explicitly relax with justification.
- Arc N [3] supplies **Theorem N1** (V1 finite-width vacuum memory kernel FORCED) and the cascading FORCED-conditional items (N1-E, N2-E, N3-D, V5 existence). V1 in flat Minkowski space depends on Lorentz invariants of $(x - x')^2$; in curved spacetime, the natural generalisation replaces this with Synge's world function $\sigma(x, x')$ (one-half squared geodesic distance) — supplying the substrate for vacuum-curvature coupling.
- The Phase-2 + Arc N FORCED structural inventory is **eight theorems** (R.2.5 spin-statistics, R.2.4 Cl(3,1), R.2.3 anyon prohibition, R.3 Dirac, Q.1+Q.8 GRH unconditional, Q.7 canonical commutation, Q.8 UV-FIN, N.5 V1 finite-width vacuum kernel).

### 1.2 Four central questions (recap)

Per Phase-3 opening §3:

- **(Q-GR1)** Does ED force a specific curvature-vacuum coupling?
- **(Q-GR2)** Does ED force a finite cosmological constant?
- **(Q-GR3)** Does ED admit a dynamical curvature equation?
- **(Q-GR4)** Are ED worldlines geodesic in emergent geometry?

Stage GR.1 catalogues structures relevant to all four; subsequent stages evaluate FORCED / REFUTED status against the four constraints.

### 1.3 Four constraints

- **C1** Lorentz covariance (flat-spacetime limit) and general covariance (curved-spacetime extension).
- **C2** Spin-statistics preservation.
- **C3** UV-FIN preservation.
- **Locality** (Primitive 11): commitment events are point-events; couplings respect locality.

Plus the structural ceiling from ED-Phys-10: Einstein equations not produced from primitives; only kinematic acoustic-metric content available.

### 1.4 Scope of this memo

Stage GR.1 catalogues. Stage GR.2 evaluates FORCED. Stage GR.3 evaluates REFUTED. The catalogue is intentionally inclusive — it lists structures that *may* later be REFUTED at Stage GR.3, alongside structures that survive constraint-checking. Premature filtering would risk omitting forms that pass constraints under refined analysis.

### 1.5 Notation

Throughout this memo:

- $g_{\mu\nu}(x)$ denotes a general spacetime metric (could be the acoustic effective metric or a proposed dynamical metric).
- $g^\mathrm{ac}_{\mu\nu}$ specifically denotes the ED-Phys-10 acoustic effective metric.
- $R_{\mu\nu}$, $R$, $R^\rho_{\;\;\sigma\mu\nu}$ denote Ricci tensor, Ricci scalar, Riemann tensor of $g_{\mu\nu}$.
- $\sigma(x, x')$ denotes Synge's world function (one-half squared geodesic distance) — defined in any spacetime where the geodesic between $x$ and $x'$ is unique.
- $\nabla_\mu$ denotes the Levi-Civita connection of $g_{\mu\nu}$.
- $\ell_\mathrm{ED}$ denotes the primitive event-discreteness scale (Primitive 01).

---

## 2. GR-1 — Bandwidth-Curvature Coupling

How the four-band bandwidth content $b_K^X$ couples to spacetime curvature. Five structurally distinct candidates.

### 2.1 GR-1A — Curvature-dependent bandwidth evolution

**Description.** The Phase-2 dynamical equation for $b_K^X(x^\mu)$ (the bandwidth content of band $X$ for chain $K$ at event $x^\mu$) gains an explicit curvature-coupling term:
$$
\Box b_K^X + \xi_X \cdot R(x) \cdot b_K^X + \cdots = J^X(x; b, \pi),
$$
with $\xi_X$ a band-specific dimensionless coupling and $R(x)$ the Ricci scalar at $x$. The $\Box$ becomes covariant ($\nabla^\mu \nabla_\mu$) and the coupling is to the Ricci scalar. This is structurally analogous to non-minimal scalar-curvature coupling in QFT-on-curved-spacetime.

**Primitive dependencies.** Primitive 04 (bandwidth fields); Primitive 06 (four-gradient generalised to covariant derivative); ED-Phys-10 acoustic metric (or a proposed dynamical $g_{\mu\nu}$).

**Potential constraint violations.** C1 satisfied if coupling is generally covariant (Ricci scalar is). C3 must be checked — explicit curvature couplings could in principle introduce new short-distance behaviour that interacts with UV-FIN.

**Notes.** Coupling parameter $\xi_X$ would be rule-type / band data (INHERITED) if introduced; the *form* of the coupling is the catalogue claim.

### 2.2 GR-1B — Curvature-modified σ_τ structure

**Description.** Arc M's σ_τ master formula, $\sigma_\tau = \hbar \sqrt{\Sigma_X w_\tau^X \langle (\partial_\mu \ln b_\tau^X)(\partial^\mu \ln b_\tau^X) \rangle_\tau}$, gains curvature-dependent corrections in curved spacetime. The proper-time average $\langle \cdot \rangle_\tau$ is taken along the chain's worldline; in curved spacetime the worldline samples curvature, and $\langle (\nabla \ln b)^2 \rangle_\tau$ acquires curvature-dependent contributions:
$$
\sigma_\tau^\mathrm{curved}(x) = \sigma_\tau^\mathrm{flat} + \zeta_\tau \cdot R(x) \cdot \sigma_\tau^\mathrm{flat} + \cdots
$$
where $\zeta_\tau$ is a rule-type curvature-coupling coefficient.

**Primitive dependencies.** Arc M Theorem M1 ($\sigma_\tau$ master formula); Primitive 06 (covariant derivative); ED-Phys-10.

**Potential constraint violations.** C1 must be respected — curvature corrections must be Lorentz-scalar (Ricci scalar is). C3 if the curvature-correction kernel is unbounded.

**Notes.** Effectively a curvature-dependent mass shift. Specific values of $\zeta_\tau$ INHERITED (rule-type data). Connects to Arc M's H1-dominant verdict — additional INHERITED content but no new FORCED ratio constraint.

### 2.3 GR-1C — Curvature-dependent bandweights

**Description.** The rule-type bandweight pattern $w_\tau^X$ (Lever L1 from Primitive 07) becomes spacetime-dependent in curved spacetime:
$$
w_\tau^X(x) = w_\tau^X|_\mathrm{flat} + \beta_\tau^X \cdot R(x) + \cdots
$$
At constant Ricci scalar (e.g., flat space, de Sitter, or AdS background), the bandweights reduce to constants; in non-trivial curvature, they vary with position.

**Primitive dependencies.** Primitive 07 L1; Primitive 04; ED-Phys-10.

**Potential constraint violations.** C1 if $\beta_\tau^X$ are not Lorentz-scalar (must be functions of curvature invariants only). Normalisation $\Sigma_X w_\tau^X = 1$ must be preserved at every event.

**Notes.** Most plausibly a phenomenologically-motivated structure (e.g., cosmological-scale bandweight modulation). Specific values INHERITED.

### 2.4 GR-1D — Curvature-dependent Fierz-class effects

**Description.** For Case-R rule-types, the L3 Fierz-class element $\Gamma_\tau$ (Dirac-mass $\mathbb{1}$ vs Majorana C-matrix vs pseudoscalar $\gamma^5$ vs etc.) becomes curvature-dependent — the rule-type's interface content is modulated by local curvature:
$$
\Gamma_\tau^\mathrm{curved}(x) = \Gamma_\tau^\mathrm{flat} + \gamma_\tau \cdot R(x) \cdot \mathbb{1} + \cdots
$$
or analogous combinations involving Riemann-tensor contractions with γ-matrix bilinears.

**Primitive dependencies.** Stage R.2.4 Cl(3,1) frame; Primitive 07 L3; ED-Phys-10.

**Potential constraint violations.** C2 must be checked — curvature-induced Fierz-class shifts might mix Dirac / Majorana / pseudoscalar TYPES at finite curvature. Stage R.2.5 spin-statistics preservation requires that the rule-type's $\eta = (-1)^{2s}$ is unchanged by curvature. Specific TYPE classification (Arc M Theorem M3 §6 partial result, Fierz as TYPE classifier) might be modified.

**Notes.** Catalogue includes; constraint analysis at GR.3.

### 2.5 GR-1E — Curvature-dependent Case-P/R distinctions

**Description.** The exchange-statistics dichotomy $\eta(\tau) \in \{+1, -1\}$ from Stage R.2.1 is preserved at flat-space primitive level by Stage R.2.5's spin-statistics theorem. In curved spacetime, one might ask whether curvature modifies the exchange-statistics relation — e.g., effective $\eta_\mathrm{eff}(x) = \pm 1 + \delta_\eta(R(x))$.

**Primitive dependencies.** Stage R.2.5 spin-statistics; Stage R.2.3 π_1 = ℤ_2 topology; ED-Phys-10.

**Potential constraint violations.** **C2 is the central concern.** Stage R.2.5's spin-statistics theorem is an unconditional FORCED theorem at primitive level; any curvature-induced Case-P/R modification would violate this theorem. Additionally, Stage R.2.3's π_1(Q_2) = ℤ_2 topological theorem forbids exchange phases beyond {±1} in 3+1D — and if the underlying spacetime topology in curved cases preserves 3+1D, this prohibition extends.

**Notes.** Catalogue for completeness; expected to be heavily REFUTED at Stage GR.3 (likely all sub-cases REFUTED by C2). Surviving forms (if any) would require non-trivial spacetime topology that might modify π_1.

---

## 3. GR-2 — Vacuum-Curvature Coupling (Primary Target)

How the V1 finite-width vacuum kernel from Theorem N1 generalises to curved spacetime. **The cleanest Phase-3 FORCED candidate per the Phase-3 opening expected verdict.**

### 3.1 GR-2A — V1 generalised to Synge world function $\sigma(x, x')$

**Description.** In flat Minkowski space, V1's vacuum-response kernel depends on the Lorentz invariant $(x - x')^2$. In curved spacetime, the natural generalisation is
$$
K_\mathrm{vac}^\mathrm{curved}(x, x') = K_\mathrm{vac}\bigl(\sigma(x, x')\bigr),
$$
with $\sigma(x, x')$ Synge's world function — one-half the squared geodesic distance between $x$ and $x'$ along the unique geodesic connecting them. In flat space, $\sigma(x, x') = \tfrac{1}{2} (x - x')^2$, recovering the flat-space V1.

**Primitive dependencies.** Theorem N1 (V1 forced); Primitive 06 (covariant derivative / geodesic structure); ED-Phys-10 (acoustic metric supplies the geodesic structure if no proposed dynamical metric); Primitive 13 (proper time generalises to affine parameter on curved-spacetime geodesics).

**Potential constraint violations.** None obvious. C1 satisfied (Synge's world function is generally covariant). C3 satisfied (V1's flat-space short-time behaviour is preserved by the geodesic-distance generalisation in the small-curvature expansion). C2 not affected (vacuum response is per-rule-type scalar quantity).

**Notes.** **The cleanest Phase-3 FORCED candidate.** If V1's flat-space forcing argument (UV-FIN + Primitive 01 + Primitive 13) extends to curved spacetime via the natural geodesic-distance generalisation, GR-2A is FORCED at Stage GR.2. Standard analogue from QFT-on-curved-spacetime (Hadamard parametrix structure uses Synge's world function in this exact role).

### 3.2 GR-2B — Curvature-dependent kernel width

**Description.** The V1 kernel's characteristic width $\tau_\mathrm{vac}$ becomes curvature-dependent:
$$
\tau_\mathrm{vac}(x) = \tau_\mathrm{vac}|_\mathrm{flat} \cdot f(R(x), R^{\mu\nu}R_{\mu\nu}, \ldots),
$$
with $f$ a function of curvature invariants. Higher curvature regions could in principle have shorter or longer kernel widths.

**Primitive dependencies.** Theorem N1; Primitive 01 (event-discreteness scale possibly curvature-dependent); ED-Phys-10.

**Potential constraint violations.** C1 satisfied (curvature invariants are generally covariant). C3 must be checked — kernel width must remain non-zero (V1-δ refutation from Stage N.3 §3.1) and finite (V1-∞ refutation from Stage N.3 §3.2) at all curvature values.

**Notes.** Specific curvature-dependence form is INHERITED. Existence of *some* curvature-dependence may be FORCED if event-discreteness scale itself depends on curvature; this is a Phase-3 evaluation question.

### 3.3 GR-2C — Curvature-dependent kernel amplitude

**Description.** The V1 kernel's overall amplitude $A_\mathrm{vac}$ becomes curvature-dependent:
$$
K_\mathrm{vac}^\mathrm{curved}(x, x') = A_\mathrm{vac}(R(x)) \cdot K_\mathrm{vac}^\mathrm{flat}(\sigma(x, x')).
$$
The kernel shape is preserved; only its overall strength varies with local curvature.

**Primitive dependencies.** Theorem N1; ED-Phys-10.

**Potential constraint violations.** C1 if $A_\mathrm{vac}$ is generally covariant function of curvature invariants.

**Notes.** A "weak" curvature-vacuum coupling — the kernel structure is unchanged; only the coupling strength varies. Plausibly INHERITED rather than FORCED.

### 3.4 GR-2D — Curvature-dependent cross-chain correlations

**Description.** The V5 cross-chain correlation kernel from Stage N.2 §6.5 becomes curvature-dependent in curved spacetime:
$$
K_\mathrm{cross}^\mathrm{curved}(x_1, x_2) = K_\mathrm{cross}^\mathrm{flat}(\sigma(x_1, x_2)) + (\text{curvature corrections}).
$$
Cross-chain correlations between separated chains depend not only on geodesic distance but also on local curvature at both endpoints (and possibly along the connecting geodesic).

**Primitive dependencies.** Theorem N1 cascading V5 (existence FORCED-conditional); ED-Phys-10; Primitive 10 (multi-chain content).

**Potential constraint violations.** C1 satisfied if curvature corrections involve only generally-covariant invariants. C3 must be checked. C2 not directly affected.

**Notes.** Plausibly relevant for cosmological-scale chain correlations (Phase-3 GR.4 deliverable). Specific correction form INHERITED.

### 3.5 GR-2E — Curvature-dependent vacuum-polarisation structure

**Description.** Arc Q.5's gauge-boson vacuum-polarisation tensor $\Pi^{\mu\nu}(q)$ acquires curvature-dependent structure in curved spacetime — modes propagate on a curved background and the polarisation tensor depends on local curvature in addition to the standard $q^\mu$ structure:
$$
\Pi^{\mu\nu}_\mathrm{curved}(x; q) = \Pi^{\mu\nu}_\mathrm{flat}(q) + (\text{curvature-coupled terms}).
$$

**Primitive dependencies.** Arc Q.5 vacuum polarisation; Theorem N1 V1; ED-Phys-10.

**Potential constraint violations.** C1 (general covariance of curvature corrections). Transversality $q_\mu \Pi^{\mu\nu} = 0$ must be preserved (FORCED by Arc Q.5 + GRH-3) — curvature corrections must respect transversality.

**Notes.** Connects to Arc Q.5 + Stage N.4 §3 cross-arc analysis. Specific corrections INHERITED.

---

## 4. GR-3 — Worldline-Curvature Coupling

How chain worldlines $\gamma_K$ interact with spacetime curvature. Five candidates.

### 4.1 GR-3A — Free chains follow geodesics of emergent metric

**Description.** A "free" chain — one with no commitment events, no individuation pairing, no gauge coupling — follows a geodesic of the emergent acoustic metric $g^\mathrm{ac}_{\mu\nu}$:
$$
u^\nu \nabla_\nu u^\mu = 0,
$$
with $u^\mu$ the chain's four-velocity along $\gamma_K$ and $\nabla_\nu$ the Levi-Civita connection of $g^\mathrm{ac}_{\mu\nu}$.

**Primitive dependencies.** Primitive 02 (chain worldlines); Primitive 13 (proper time / affine parameter); ED-Phys-10 (acoustic metric); Phase-2 free-chain conditions.

**Potential constraint violations.** None obvious at flat-space level (in flat space, geodesics are straight lines, matching free-Phase-2 chains). In curved spacetime, the equivalence between Phase-2 "free chain" and geodesic on $g^\mathrm{ac}_{\mu\nu}$ is the structural question.

**Notes.** **Likely FORCED-conditional Phase-3 candidate.** If the Phase-2 free-chain condition translates structurally into the geodesic equation on the emergent acoustic metric, GR-3A is FORCED. The equivalence-principle analogue (rule-type-independence of free worldlines) is a sub-question.

### 4.2 GR-3B — Curvature-dependent commitment thresholds

**Description.** Primitive 10's individuation threshold $\Theta_K(x)$ becomes curvature-dependent:
$$
\Theta_K(x) = \Theta_K|_\mathrm{flat} \cdot h(R(x)),
$$
with $h$ a function of curvature invariants. High-curvature regions have modified thresholds — potentially making individuation easier or harder depending on $h$'s sign.

**Primitive dependencies.** Primitive 10 (individuation); Primitive 11 (commitment); ED-Phys-10.

**Potential constraint violations.** C2 in Case-R sectors — curvature-modulated thresholds could affect Pauli exclusion if not carefully restricted (similar to Stage N.3 §2.2 N2-B Case-R refutation). C1 satisfied if $h$ is generally covariant function of curvature invariants.

**Notes.** Distinction from N2-A density-dependent thresholds: N2-A is *event-history* dependent; GR-3B is *spacetime-curvature* dependent. Both modify the threshold quantitatively.

### 4.3 GR-3C — Curvature-dependent adjacency graphs

**Description.** Primitive 10 multi-chain adjacency graphs depend on local spacetime curvature in addition to chain-pairwise distinguishability. Two chains in a high-curvature region may be adjacent under different criteria than two chains in a low-curvature region.

**Primitive dependencies.** Primitive 10; ED-Phys-10.

**Potential constraint violations.** C2 (multi-chain spin-statistics preservation across curvature variation). C1 (curvature-dependence must be generally covariant).

**Notes.** Connects to N3-A time-lagged adjacency catalogue from Arc N (additional non-Markovian structure now combined with curvature dependence).

### 4.4 GR-3D — Curvature-dependent memory kernels

**Description.** Arc N memory kernels $K_X(\Delta\tau)$ for bandwidth memory (N1-A), commitment memory (N2-A/C), and adjacency memory (N3-A/B) become curvature-dependent:
$$
K_X^\mathrm{curved}(\Delta\tau, x) = K_X|_\mathrm{flat}(\Delta\tau) \cdot k_X(R(x)).
$$
Memory kernels' decay timescales or amplitudes vary with local curvature.

**Primitive dependencies.** Arc N catalogue items (N1-A, N2-A/C, N3-A/B); ED-Phys-10.

**Potential constraint violations.** C1 (general covariance), C3 (must preserve UV-FIN under curvature-dependent kernel modifications).

**Notes.** A subset of GR-2B (curvature-dependent V1 width) extended to other Arc N kernel sectors. Specific dependence INHERITED.

### 4.5 GR-3E — Curvature-dependent null-cone deformation

**Description.** The acoustic-metric null cones at each event $x$ depend on local bandwidth-flow structure, which in turn depends on local spacetime curvature. The chain-propagation null-cone structure is therefore curvature-dependent. Specifically, mode-propagation speeds $c_s(x)$ of the acoustic metric depend on $R(x)$:
$$
c_s(x) = c_s|_\mathrm{flat} \cdot c_R(R(x), R^{\mu\nu}R_{\mu\nu}, \ldots).
$$

**Primitive dependencies.** ED-Phys-10 acoustic metric; Primitive 06 (Lorentz / general covariance).

**Potential constraint violations.** C1 satisfied if $c_R$ depends only on curvature invariants. Causal structure must be preserved (no superluminal propagation in any frame).

**Notes.** Direct extension of ED-Phys-10's analogue-metric content to curvature-dependent settings. Plausibly admissible as a refinement of ED-Phys-10 rather than a new structural mechanism.

---

## 5. GR-4 — Curvature-Dynamics Candidates

Whether ED admits a dynamical equation for curvature itself — i.e., whether the bandwidth-field equations, when re-expressed in terms of the emergent acoustic metric, yield Einstein-like dynamics. **Most speculative Phase-3 sector.**

### 5.1 GR-4A — Einstein-like equations with kernel-weighted source

**Description.** The bandwidth-field equation, in the long-wavelength limit and in terms of the emergent acoustic metric $g^\mathrm{ac}_{\mu\nu}$, takes a form analogous to Einstein's:
$$
R_{\mu\nu} - \tfrac{1}{2} R g_{\mu\nu} + \Lambda_\mathrm{eff} g_{\mu\nu} = 8\pi G_\mathrm{eff} \cdot T^\mathrm{kernel}_{\mu\nu},
$$
with $T^\mathrm{kernel}_{\mu\nu}$ a stress-energy-like tensor whose source is the V1 vacuum-response-kernel-weighted bandwidth content.

**Primitive dependencies.** Phase-1 + Arc R bandwidth-field equations; ED-Phys-10 acoustic metric; Theorem N1 V1; Arc Q.8 cosmological-Λ structure.

**Potential constraint violations.** C1 (generally covariant by construction). C3 (UV-FIN preservation in source $T^\mathrm{kernel}_{\mu\nu}$). Whether such an equation actually emerges from primitives is the central GR.2 evaluation question.

**Notes.** Most aggressive Phase-3 catalogue claim. Likely SPECULATIVE outcome at Stage GR.2 — full Einstein-equation emergence is unlikely from current primitive content. ED-Phys-10's prior closure (no Einstein) constitutes the structural baseline against which GR-4A is evaluated.

### 5.2 GR-4B — Nonlocal curvature equations from V1

**Description.** Instead of a local Einstein-like equation, ED admits a non-local equation for curvature with V1 kernel content:
$$
R_{\mu\nu}(x) = \int K_\mathrm{vac}(\sigma(x, x')) \cdot S_{\mu\nu}(x') \, d^4x',
$$
with $S_{\mu\nu}$ a source built from bandwidth content. The non-locality is finite-width (consistent with V1 admissibility class) and respects causal structure.

**Primitive dependencies.** Theorem N1 V1; ED-Phys-10; Primitive 11 commitment locality (must be respected at the scale of V1's finite width).

**Potential constraint violations.** C1 satisfied (Synge's world function in $K_\mathrm{vac}$ is generally covariant). Locality must be respected at the V1 width scale — non-locality beyond V1 width is REFUTED.

**Notes.** A more conservative alternative to GR-4A: instead of a local Einstein equation, a non-local kernel-weighted relation between curvature and bandwidth source.

### 5.3 GR-4C — Acoustic-metric-only dynamics (baseline)

**Description.** ED-Phys-10's acoustic metric remains the structural ceiling: there is no dynamical equation for $g^\mathrm{ac}_{\mu\nu}$ beyond the underlying bandwidth-field equations. Curvature is a *kinematic* feature of bandwidth-mode propagation, not a *dynamical* object in its own right. This is the baseline — the structure ED is known to have, against which GR-4A and GR-4B are evaluated.

**Primitive dependencies.** ED-Phys-10 acoustic metric; Phase-2 bandwidth-field equations.

**Potential constraint violations.** None — this is the established ED-Phys-10 result.

**Notes.** Phase-3 GR.5 closure may land here if GR-4A and GR-4B both fail FORCED evaluation. Status: **default baseline**.

### 5.4 GR-4D — Curvature-induced vacuum backreaction

**Description.** The V1 vacuum-response kernel, when integrated over a curved-spacetime region, produces back-reaction on the curvature itself. Specifically, the cosmological-Λ structure (Arc Q.8 + Arc N §6) couples back to curvature at primitive level:
$$
G_{\mu\nu}^\mathrm{induced} = \kappa \cdot \int K_\mathrm{vac}(\sigma) \cdot \rho_\mathrm{vac}(x') \, d^4x' \cdot g_{\mu\nu},
$$
with $\rho_\mathrm{vac}$ the local vacuum-energy density and $\kappa$ a coupling constant.

**Primitive dependencies.** Theorem N1 V1; Arc Q.8 cosmological-Λ; ED-Phys-10.

**Potential constraint violations.** C1 (general covariance). C3 (UV-FIN of integrated source).

**Notes.** Connects directly to Arc N §6.1's "Λ as V1-kernel integral" hand-off. Specific coupling constant $\kappa$ (analogue of $G$) INHERITED.

### 5.5 GR-4E — Curvature-dependent UV-FIN constraints

**Description.** Arc Q's UV-FIN (Theorem Q3) operates with primitive event-discreteness scale $\ell_\mathrm{ED}$. In curved spacetime, the natural UV-FIN constraint may be curvature-modulated: $\ell_\mathrm{ED}^\mathrm{curved}(x) = \ell_\mathrm{ED} \cdot \ell_R(R(x))$, with the cutoff scale itself depending on local curvature. This would couple UV-FIN to curvature in a structurally non-trivial way.

**Primitive dependencies.** Arc Q.8 UV-FIN; Primitive 01 (event-discreteness); ED-Phys-10.

**Potential constraint violations.** C3 must be re-evaluated under curvature-modulated cutoff. C1 satisfied if $\ell_R$ is curvature-invariant function.

**Notes.** Most subtle Phase-3 catalogue item. Connects deeply to quantum-gravity-style concerns about Planck-scale physics. Likely SPECULATIVE at Stage GR.2.

---

## 6. Summary Table

| ID | Description | Primitive dependencies | Potential constraints to check (GR.3) |
|---|---|---|---|
| **GR-1A** | Curvature-dependent bandwidth evolution ($\xi_X R \, b$ coupling) | 04, 06, ED-Phys-10 | C1 (gen. cov.), C3 |
| **GR-1B** | Curvature-modified σ_τ ($\zeta_\tau R$ shift) | 06, M.1 + ED-Phys-10 | C1, C3 |
| **GR-1C** | Curvature-dependent bandweights $w_\tau^X(x)$ | 04, 07-L1, ED-Phys-10 | C1; normalisation $\Sigma w = 1$ |
| **GR-1D** | Curvature-dependent Fierz-class $\Gamma_\tau(x)$ | R.2.4, 07-L3, ED-Phys-10 | **C2** (Fierz TYPE preservation) |
| **GR-1E** | Curvature-dependent Case-P/R distinctions | R.2.5, R.2.3, ED-Phys-10 | **C2 (central — likely heavily REFUTED)** |
| **GR-2A** | V1 with Synge world function $\sigma(x, x')$ | N1, 06, 13, ED-Phys-10 | None obvious; **PRIMARY FORCED CANDIDATE** |
| **GR-2B** | Curvature-dependent kernel width $\tau_\mathrm{vac}(x)$ | N1, 01, ED-Phys-10 | C3 (V1-δ and V1-∞ bounds) |
| **GR-2C** | Curvature-dependent kernel amplitude $A_\mathrm{vac}(x)$ | N1, ED-Phys-10 | C1 |
| **GR-2D** | Curvature-dependent cross-chain correlations $K_\mathrm{cross}^\mathrm{curved}$ | N1 (V5), 10, ED-Phys-10 | C1, C3 |
| **GR-2E** | Curvature-dependent vacuum polarisation $\Pi^{\mu\nu}_\mathrm{curved}$ | Q.5, N1, ED-Phys-10 | C1; transversality $q_\mu \Pi^{\mu\nu} = 0$ |
| **GR-3A** | Free chains follow geodesics of $g^\mathrm{ac}_{\mu\nu}$ | 02, 13, ED-Phys-10, Phase-2 free-chain | None obvious; **likely FORCED-CONDITIONAL** |
| **GR-3B** | Curvature-dependent commitment thresholds | 10, 11, ED-Phys-10 | C2 (Case-R Pauli exclusion) |
| **GR-3C** | Curvature-dependent adjacency graphs | 10, ED-Phys-10 | C1, C2 |
| **GR-3D** | Curvature-dependent memory kernels | Arc N catalogue, ED-Phys-10 | C1, C3 |
| **GR-3E** | Curvature-dependent null-cone deformation $c_s(x; R)$ | ED-Phys-10, 06 | Causal structure |
| **GR-4A** | Einstein-like equations with kernel-weighted source | Phase-2 + ED-Phys-10 + N1 | All four constraints; **likely SPECULATIVE** |
| **GR-4B** | Nonlocal curvature equations from V1 | N1, ED-Phys-10, 11 | Locality at V1-width scale |
| **GR-4C** | Acoustic-metric-only dynamics (baseline) | ED-Phys-10, Phase-2 | None — established baseline |
| **GR-4D** | Curvature-induced vacuum backreaction | N1, Q.8, ED-Phys-10 | C1, C3 |
| **GR-4E** | Curvature-dependent UV-FIN constraints | Q.3 (UV-FIN), 01, ED-Phys-10 | C3 re-evaluated |

### 6.1 Notes on the table

- **Bold C-markers** indicate items where Stage GR.3 evaluation is expected to be most consequential — strongest REFUTED candidates.
- **GR-2A marked as PRIMARY FORCED CANDIDATE** — V1 with Synge world function is the cleanest Phase-3 forcing route per Phase-3 opening §6.3.
- **GR-3A marked as likely FORCED-CONDITIONAL** — free-chain geodesic worldlines in emergent metric, conditional on Phase-2 free-chain condition translating to geodesic equation.
- **GR-4A marked as likely SPECULATIVE** — full Einstein-like emergence is the most aggressive Phase-3 claim and unlikely to close FORCED.
- **GR-4C is the established baseline** — if GR-4A and GR-4B fail FORCED evaluation, Phase-3 closes at GR-4C with the ED-Phys-10 acoustic-metric-only result preserved.

---

## 7. Coverage Assessment

### 7.1 Sectors covered

The catalogue spans four sectors:
- **GR-1 (bandwidth-curvature):** 5 items (A–E).
- **GR-2 (vacuum-curvature):** 5 items (A–E). **Primary target.**
- **GR-3 (worldline-curvature):** 5 items (A–E).
- **GR-4 (curvature-dynamics):** 5 items (A–E).

Total: 20 catalogue items.

### 7.2 Sectors not covered (intentional)

The following curvature-coupling-adjacent structures are *not* catalogued at this stage:

- **Quantum-gravity emergent corrections** to the gravitational coupling constant $G$. Out of Phase-3 structural-derivation scope; $G$ remains INHERITED.
- **String-theory-style extra-dimensional curvature couplings.** Outside ED's primitive stack; SPECULATIVE.
- **Cosmic-inflation-specific curvature mechanisms** (e.g., slow-roll inflaton-curvature coupling). Phenomenological / model-specific; not primitive-level.
- **Dark-matter / dark-energy effective-fluid couplings.** Empirical-phenomenology layer; not Phase-3 structural.

### 7.3 Catalogue completeness

The 20 items represent the systematic enumeration of primitive-level curvature-coupling structures consistent with ED Primitives 01–13 + Phase-2 closures + Arc N Theorem N1 + ED-Phys-10. New catalogue items may be added at later stages if structural analysis surfaces additional admissible forms; current coverage is judged adequate for Stage GR.2 / GR.3 evaluation.

---

## 8. Hand-Off

### 8.1 To Stage GR.2 (FORCED evaluation)

Stage GR.2 (`gr_coupling_forced.md`) will evaluate each of the 20 catalogue items for primitive-level FORCED status. Most plausible FORCED candidates per Phase-3 opening §6.3:

- **GR-2A (V1 with Synge world function):** primary FORCED candidate. If V1's flat-space forcing argument extends to curved spacetime via the natural geodesic-distance generalisation (Hadamard-parametrix-style construction), GR-2A is FORCED.
- **GR-3A (free-chain geodesic worldlines):** likely FORCED-conditional. If Phase-2 free-chain condition translates to geodesic equation on emergent acoustic metric.

Secondary candidates:
- **GR-4D (curvature-induced vacuum backreaction):** structurally plausible via Arc N §6.1 hand-off.
- **GR-2B (curvature-dependent kernel width):** existence of *some* curvature-dependence may be FORCED if event-discreteness scale itself depends on curvature.

Expected GR.2 outcome: 1–3 items FORCED + possibly 1 item FORCED-conditional; remainder ADMISSIBLE-NOT-FORCED.

### 8.2 To Stage GR.3 (REFUTED evaluation)

Stage GR.3 (`gr_coupling_refuted.md`) will evaluate items against C1 / C2 / C3 / locality constraints. Expected REFUTED targets:

- **GR-1E (curvature-dependent Case-P/R distinctions):** likely heavily REFUTED by C2 (spin-statistics preservation theorem).
- **GR-1D (curvature-dependent Fierz-class):** REFUTED in restricted sub-cases violating C2 Fierz TYPE preservation.
- **GR-3B (curvature-dependent commitment thresholds in Case-R):** REFUTED in sub-cases violating Pauli exclusion (parallel to Stage N.3 §2.2 N2-B Case-R refutation).
- **GR-4A (Einstein-like equations with kernel-weighted source):** SPECULATIVE rather than REFUTED — depends on whether full Einstein emergence is structurally derivable; ED-Phys-10 guardrails preserve baseline.

Expected GR.3 outcome: 2–4 items REFUTED in restricted sub-cases.

### 8.3 To Stage GR.4 (cosmological implications)

Stage GR.4 (`gr_cosmological_implications.md`) will evaluate the cosmological consequences of FORCED + ADMISSIBLE Phase-3 structures: explicit V1-kernel-integral computation for closed cosmological spacetime, cosmological-Λ structure, large-scale structure implications via V5 cross-chain correlations, dispersion-relation modifications, empirical-signature framework.

### 8.4 To Stage GR.5 (synthesis)

`phase3_synthesis.md`. Will integrate GR.0 + GR.1 + GR.2 + GR.3 + GR.4 into a final Phase-3 verdict.

---

## 9. Cross-References

- Phase-3 opening: `phase3_scoping.md` (GR.0).
- Phase-2 closures: `phase2_synthesis.md`, `arc_q_synthesis.md`, `chain_mass_synthesis.md`, `dirac_emergence.md`, `rule_type_taxonomy_synthesis.md`.
- Arc N closure: `arc_n_synthesis.md`, `non_markov_implications.md`.
- ED-Phys-10 prior: `archive/research_history/ED Physics/ED-Phys-10/`, `memory/project_ed10_geometry_qft_scope.md`.
- Downstream: `gr_coupling_forced.md` (GR.2), `gr_coupling_refuted.md` (GR.3), `gr_cosmological_implications.md` (GR.4), `phase3_synthesis.md` (GR.5).

---

## 10. References

[1] A. Proxmire, *Phase-3 Scoping*, `phase3_scoping.md`, 2026.

[2] ED-Phys-10 kinematic-curvature arc, closed 2026-04-22. See `memory/project_ed10_geometry_qft_scope.md`.

[3] A. Proxmire, *Arc N Synthesis*, `arc_n_synthesis.md`, 2026.

[4] B. S. DeWitt, *The Global Approach to Quantum Field Theory*. Oxford University Press, 2003 — for Synge's world function $\sigma(x, x')$ and Hadamard-parametrix structure on curved spacetime.

[5] M. Visser, "Acoustic black holes: horizons, ergospheres, and Hawking radiation," *Class. Quantum Grav.* **15**, 1767 (1998) — for analogue-gravity acoustic-metric formalism.

---

## 11. One-Line Summary

**Stage GR.1 catalogues 20 admissible curvature-coupling structures across four sectors — GR-1 bandwidth-curvature (5 items: curvature-dependent bandwidth evolution, σ_τ shift, bandweights, Fierz-class, Case-P/R distinctions), GR-2 vacuum-curvature (5 items: V1 with Synge world function, curvature-dependent kernel width, amplitude, cross-chain correlations, vacuum-polarisation; primary target), GR-3 worldline-curvature (5 items: free-chain geodesics, curvature-dependent thresholds, adjacency, memory kernels, null-cone deformation), GR-4 curvature-dynamics (5 items: Einstein-like kernel-weighted, non-local from V1, acoustic-metric-only baseline, curvature-induced vacuum backreaction, curvature-dependent UV-FIN) — each characterised by primitive dependencies and potential constraint flags (C1 Lorentz/general covariance, C2 spin-statistics, C3 UV-FIN, locality), with GR-2A (V1 with Synge world function) flagged as the primary FORCED candidate per Phase-3 opening expected verdict, GR-3A (free-chain geodesic worldlines) flagged as likely FORCED-conditional, GR-1E (curvature-dependent Case-P/R) flagged as likely heavily REFUTED by C2, GR-4A (Einstein-like emergence) flagged as likely SPECULATIVE with GR-4C (acoustic-metric-only) as the established baseline, and the catalogue handed off to Stage GR.2 for FORCED evaluation, Stage GR.3 for REFUTED evaluation, and Stages GR.4/GR.5 for cosmological implications and synthesis.**
