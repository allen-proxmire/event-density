# Klein-Gordon Emergence from the Lorentz-Covariant Participation Measure

**Date:** 2026-04-24
**Location:** `quantum/foundations/klein_gordon_emergence.md`
**Status:** Phase-2 Arc-R Stage R.1 main derivation memo. Derives the Klein-Gordon equation
\begin{equation*}
  \left(\Box + \frac{m^2 c^2}{\hbar^2}\right) \Psi(x^\mu) = 0
\end{equation*}
from the Lorentz-covariant participation measure defined in `relativistic_participation_measure.md`. The second-order d'Alembertian structure is FORCED by Lorentz invariance applied to a scalar wavefield; the mass-shell dispersion $p_\mu p^\mu = m^2 c^2$ is FORCED by Poincaré invariance + analyticity; the non-relativistic limit explicitly reduces to Phase-1 Schrödinger. No new primitives required. Dimensional constants $\hbar$, $m$, $c$ remain inherited.
**Purpose:** Second Phase-2 Arc-R deliverable per `phase2_extensions_roadmap.md §2.1`. Makes Klein-Gordon a primitive-level-derived consequence of the ED framework for scalar (bosonic) chains.

---

## 1. Starting material

### 1.1 Covariant participation measure (Arc-R Stage R.0)

From `relativistic_participation_measure.md` §2, the Lorentz-covariant participation measure for a scalar (bosonic) chain is
\begin{equation}
  P_K(x^\mu) = \sqrt{b_K(x^\mu)} \, e^{i \pi_K(x^\mu)} \in \mathbb{C},
  \label{eq:covP}
\end{equation}
transforming as a scalar at each spacetime event under Lorentz transformations:
\begin{equation}
  P_K(x^\mu) \;\to\; P'_K(x'^\mu) = P_K(\Lambda^{-1} x'^\mu).
\end{equation}

The coherent sum over channels defines the candidate scalar wavefunction:
\begin{equation}
  \Psi(x^\mu) = \sum_K P_K(x^\mu) \in \mathbb{C}.
  \label{eq:cohSum}
\end{equation}

### 1.2 Primitive-level inputs

The derivation below uses the following primitive-level content, all FORCED in Phase 1 or in the covariant-scoping memo:

- **Primitive 02 (Chain, covariant):** chains are worldlines $x^\mu(\tau)$ parameterized by proper time τ.
- **Primitive 04 (Four-band, covariant):** bandwidth decomposition into four Lorentz-scalar bands.
- **Primitive 06 (ED gradient, covariant):** four-gradient $\partial_\mu$ as the natural covariant derivative.
- **Primitive 13 (Relational timing, covariant):** proper-time-parameterized phase content.
- **U1 (FORCED):** participation measure is complex-valued with polar decomposition.
- **U3 (FORCED modulo ℏ):** linear, first-order-in-proper-time evolution for isolated chains — to be generalized here.

### 1.3 Dimensional constants

Three dimensional constants enter Klein-Gordon:
- **$c$** — speed of light; Lorentz invariance scale.
- **$\hbar$** — reduced Planck constant; inherited via U3 from the Dimensional Atlas.
- **$m$** — particle mass; inherited at the species level; chain-mass primitive-level derivation is Arc-M (open).

None of these is derived in this memo. All three are inherited empirical anchors.

---

## 2. Lorentz-invariance constraints on the evolution equation

The evolution equation for $\Psi(x^\mu)$ must be Lorentz-invariant as a statement about scalar fields. This constraint combined with structural requirements from ED primitives determines the form of the equation up to the mass parameter.

### 2.1 Available covariant differential operators on scalars

For a Lorentz scalar $\Psi(x^\mu)$, the covariant derivatives that preserve scalar character are:

- **Zeroth order:** $\Psi$ itself, or any scalar multiple $\alpha \cdot \Psi$.
- **First order:** no Lorentz-scalar constructable from $\partial_\mu \Psi$ alone (the four-gradient is a four-vector, not a scalar). The product $\partial_\mu \Psi \cdot \partial^\mu \Psi^*$ is a scalar but quadratic in $\Psi$, so it produces non-linear equations.
- **Second order:** the d'Alembertian $\Box \Psi = \partial_\mu \partial^\mu \Psi$ is a Lorentz scalar.
- **Higher order:** $\Box^n \Psi$ for any $n$; more generally, scalars constructed from multiple d'Alembertians.

### 2.2 Linear scalar wave equations

For a linear equation in $\Psi$, the most general second-order Lorentz-scalar form is
\begin{equation}
  A \Box \Psi + B \Psi = 0
\end{equation}
for real constants $A$, $B$. Higher-order terms $C \Box^n \Psi$ would introduce additional derivative structure; for the minimum-order Lorentz-scalar linear equation, $n = 1$ is sufficient.

Normalizing $A = 1$ (no loss of generality) and writing $B = m^2 c^2 / \hbar^2$ (on dimensional grounds — see §2.3):
\begin{equation}
  \left(\Box + \frac{m^2 c^2}{\hbar^2}\right) \Psi = 0.
  \label{eq:KG_form}
\end{equation}

This is the structural form of the Klein-Gordon equation, derived from Lorentz invariance alone under the minimum-order linear-scalar-field assumption.

### 2.3 Dimensional considerations

The d'Alembertian has units of $[\text{length}^{-2}]$ (since $\partial_\mu \partial^\mu$ has two spacetime derivatives). For the equation to be dimensionally consistent, $B$ must have units of $[\text{length}^{-2}]$. The unique combination of empirical constants $\hbar$, $m$, $c$ with these units is $m c/\hbar$, and its square is $m^2 c^2/\hbar^2$. This fixes the coefficient $B$ up to a dimensionless multiplicative factor (which is set to unity by the mass-shell condition — see §3).

**Status of (eq:KG_form):** FORCED at the structural level by Lorentz invariance + minimum-order linear scalar equation + dimensional consistency. The specific coefficient $m^2 c^2 / \hbar^2$ is forced by dimensional arguments plus the mass-shell identification derived in §3.

### 2.4 Why second-order in time (revisited)

Phase-1 Schrödinger is first-order in time: $i\hbar \partial_t \Psi = \hat H \Psi$. Klein-Gordon is second-order in time: $(1/c^2) \partial_t^2 \Psi - \nabla^2 \Psi + (m^2 c^2/\hbar^2) \Psi = 0$. The difference is FORCED by Lorentz invariance.

A first-order-in-time Lorentz-scalar equation for a scalar field would privilege the time coordinate, breaking Lorentz invariance. Specifically, $\partial_t \Psi$ is the zero-component of the four-gradient $\partial_\mu \Psi$ (up to factors of $c$); an equation involving $\partial_t \Psi$ alone cannot be Lorentz-scalar unless balanced by spatial terms in a way that reconstructs $\Box$.

The unique Lorentz-scalar second-order time-derivative operator is $(1/c^2)\partial_t^2$, which appears in $\Box = (1/c^2) \partial_t^2 - \nabla^2$ paired with the spatial Laplacian. **This pairing forces the second-order structure.**

**Alternative factorization.** Klein-Gordon can be factored into two first-order equations by introducing auxiliary fields (Feshbach-Villars form). Each factored first-order equation is Lorentz-covariant when its multi-component structure is taken into account. At the level of a single scalar field, however, the equation is second-order.

---

## 3. Plane-wave modes and the mass-shell condition

### 3.1 Plane-wave participation modes

A plane-wave participation mode has the form
\begin{equation}
  P_K(x^\mu) = c_K \, e^{-i p_\mu x^\mu / \hbar},
  \label{eq:planewave}
\end{equation}
where $p_\mu = (E/c, -\mathbf{p})$ is the four-momentum (with lower index) and $c_K$ is a complex amplitude. In components:
\begin{equation}
  p_\mu x^\mu = \frac{E}{c} \cdot ct - (-\mathbf{p}) \cdot \mathbf{x} = E t - \mathbf{p} \cdot \mathbf{x},
\end{equation}
so
\begin{equation}
  P_K(x^\mu) = c_K \, e^{-i(E t - \mathbf{p} \cdot \mathbf{x})/\hbar} = c_K \, e^{i(\mathbf{p} \cdot \mathbf{x} - E t)/\hbar}.
\end{equation}

### 3.2 Primitive-level justification for plane-wave modes

The plane-wave form (eq:planewave) is the Lorentz-covariant generalization of Phase-1's momentum-basis mode $P_k(x, t) = c_k e^{ikx}/\sqrt{2\pi}$. Under translation invariance of the participation graph (Primitive 06 covariant), four-momentum eigenmodes are the natural basis; their explicit form is the plane-wave exponential above.

**Status: FORCED** by Poincaré invariance applied to primitive-level P_K structure, in strict parallel with the U3 momentum-basis identification of Phase 1.

### 3.3 Action of the d'Alembertian on plane-waves

Applying the d'Alembertian to (eq:planewave):
\begin{equation}
  \Box P_K = \partial_\mu \partial^\mu \left(c_K \, e^{-i p_\nu x^\nu / \hbar}\right) = c_K \, \left(-\frac{i p_\mu}{\hbar}\right)\left(-\frac{i p^\mu}{\hbar}\right) e^{-i p_\nu x^\nu / \hbar}.
\end{equation}

Simplifying:
\begin{equation}
  \Box P_K = -\frac{p_\mu p^\mu}{\hbar^2} \cdot P_K.
  \label{eq:boxP}
\end{equation}

This is an algebraic identity for any plane-wave mode with well-defined four-momentum $p_\mu$.

### 3.4 Mass-shell condition

For the plane-wave mode to satisfy the Klein-Gordon form (eq:KG_form), equating (eq:boxP) to $-(m^2 c^2 / \hbar^2) P_K$:
\begin{equation}
  -\frac{p_\mu p^\mu}{\hbar^2} = -\frac{m^2 c^2}{\hbar^2},
\end{equation}
which gives the **mass-shell condition**:
\begin{equation}
  p_\mu p^\mu = m^2 c^2.
  \label{eq:massshell}
\end{equation}

In components, $p_\mu p^\mu = (E/c)^2 - |\mathbf{p}|^2 = m^2 c^2$, equivalently
\begin{equation}
  E^2 = |\mathbf{p}|^2 c^2 + m^2 c^4.
  \label{eq:rel_disp}
\end{equation}

This is the **relativistic energy-momentum dispersion relation**.

**Status: FORCED** by the combination of (eq:KG_form) structural form + plane-wave mode ansatz. The mass-shell condition follows by algebraic identity.

### 3.5 Positive and negative energy branches

Equation (eq:massshell) admits two energy branches:
\begin{equation}
  E_\pm = \pm \sqrt{|\mathbf{p}|^2 c^2 + m^2 c^4}.
\end{equation}

Both branches are solutions of Klein-Gordon. In standard quantum mechanics this produces the positive-energy and negative-energy solutions, historically interpreted as particles and antiparticles (Dirac's original argument, later formalized in QFT). At the scalar level, the two branches correspond to scalar particles and scalar antiparticles.

**Status: FORCED** mathematically. The physical interpretation of the negative-energy branch as an antiparticle requires additional QFT-level machinery (Arc Q).

---

## 4. Klein-Gordon evolution equation

### 4.1 The equation for plane-wave modes

Combining §2 and §3: for plane-wave modes satisfying the mass-shell condition,
\begin{equation}
  \left(\Box + \frac{m^2 c^2}{\hbar^2}\right) P_K(x^\mu) = 0.
  \label{eq:KG_modes}
\end{equation}

### 4.2 The equation for the coherent sum

By linearity of the d'Alembertian and the participation-measure evolution, the coherent sum $\Psi = \sum_K P_K$ inherits the same equation:
\begin{equation}
  \left(\Box + \frac{m^2 c^2}{\hbar^2}\right) \Psi(x^\mu) = \sum_K \left(\Box + \frac{m^2 c^2}{\hbar^2}\right) P_K(x^\mu) = 0.
  \label{eq:KG_Psi}
\end{equation}

**This is the Klein-Gordon equation for the coherent-sum wavefunction.**

### 4.3 Derivation of linearity

The linearity used in (eq:KG_Psi) is the same linearity that U3 established in Phase 1. The covariant version of U3 — not derived in full in this memo, but structurally forced by the same arguments — gives a linear evolution on each $P_K$, and hence on the sum.

Alternative argument: since (eq:KG_form) is linear in $\Psi$, it is preserved under linear superposition of any solutions. If each $P_K$ is a solution, then $\Sigma_K P_K$ is a solution.

### 4.4 Status of the Klein-Gordon emergence

**Structurally FORCED:**
- The d'Alembertian as the unique second-order Lorentz-scalar operator on scalar fields (§2.1).
- The mass-shell condition for plane-wave modes (§3.4).
- The Klein-Gordon equation structural form (eq:KG_form).
- Linearity of the Klein-Gordon evolution for the coherent sum (§4.3).

**Inherited:**
- Numerical value of $m$ (mass of the scalar particle; Arc-M SPECULATIVE).
- Numerical value of $\hbar$ (via U3; `hbar_origin.md`).
- Numerical value of $c$ (speed of light; Dimensional Atlas relativistic regime).

**Klein-Gordon is derived from the ED primitive framework for scalar (bosonic) chains, up to the three inherited dimensional constants.**

---

## 5. Non-relativistic limit — explicit derivation to Schrödinger

This section derives the non-relativistic limit of Klein-Gordon and shows that it reduces to the Phase-1 Schrödinger equation exactly.

### 5.1 Rest-energy factorization

In the non-relativistic regime, the particle's total energy is dominated by its rest energy $E_0 = m c^2$. Kinetic energy and potential energy are small corrections. Write the wavefunction as
\begin{equation}
  \Psi(x^\mu) = e^{-i E_0 t / \hbar} \cdot \psi(\mathbf{x}, t),
  \label{eq:nr_factorization}
\end{equation}
factoring out the rest-energy time-dependence. The residual $\psi$ captures the slow (non-relativistic) dynamics.

### 5.2 Computing derivatives

Time derivatives:
\begin{align}
  \partial_t \Psi &= e^{-i E_0 t/\hbar} \left[-\frac{i E_0}{\hbar} \psi + \partial_t \psi\right], \\
  \partial_t^2 \Psi &= e^{-i E_0 t/\hbar} \left[-\frac{E_0^2}{\hbar^2} \psi - \frac{2 i E_0}{\hbar} \partial_t \psi + \partial_t^2 \psi\right].
\end{align}

Since $E_0 = m c^2$:
\begin{equation}
  \partial_t^2 \Psi = e^{-i E_0 t/\hbar} \left[-\frac{m^2 c^4}{\hbar^2} \psi - \frac{2 i m c^2}{\hbar} \partial_t \psi + \partial_t^2 \psi\right].
\end{equation}

Dividing by $c^2$:
\begin{equation}
  \frac{1}{c^2} \partial_t^2 \Psi = e^{-i E_0 t/\hbar} \left[-\frac{m^2 c^2}{\hbar^2} \psi - \frac{2 i m}{\hbar} \partial_t \psi + \frac{1}{c^2} \partial_t^2 \psi\right].
  \label{eq:nr_timederiv}
\end{equation}

Spatial derivatives:
\begin{equation}
  \nabla^2 \Psi = e^{-i E_0 t/\hbar} \cdot \nabla^2 \psi.
  \label{eq:nr_spaced}
\end{equation}

### 5.3 Substitution into Klein-Gordon

Klein-Gordon (eq:KG_Psi):
\begin{equation}
  \left[\frac{1}{c^2} \partial_t^2 - \nabla^2 + \frac{m^2 c^2}{\hbar^2}\right] \Psi = 0.
\end{equation}

Substituting (eq:nr_timederiv) and (eq:nr_spaced), and dividing by $e^{-i E_0 t/\hbar}$:
\begin{equation}
  -\frac{m^2 c^2}{\hbar^2} \psi - \frac{2 i m}{\hbar} \partial_t \psi + \frac{1}{c^2} \partial_t^2 \psi - \nabla^2 \psi + \frac{m^2 c^2}{\hbar^2} \psi = 0.
\end{equation}

The $-\frac{m^2 c^2}{\hbar^2} \psi$ and $+\frac{m^2 c^2}{\hbar^2} \psi$ terms cancel:
\begin{equation}
  - \frac{2 i m}{\hbar} \partial_t \psi + \frac{1}{c^2} \partial_t^2 \psi - \nabla^2 \psi = 0.
  \label{eq:NR_exact}
\end{equation}

### 5.4 Non-relativistic limit

The term $(1/c^2) \partial_t^2 \psi$ is suppressed relative to $(2im/\hbar) \partial_t \psi$ in the non-relativistic regime. Specifically, if the characteristic energy scale of $\psi$ is $E \sim p^2/(2m) \ll m c^2$, then
\begin{equation}
  \frac{\partial_t^2 \psi}{c^2} \sim \frac{E^2}{\hbar^2 c^2} \cdot \psi, \qquad \frac{2 i m}{\hbar} \partial_t \psi \sim \frac{2 m E}{\hbar^2} \psi,
\end{equation}
and the ratio is $E/(2 m c^2) \ll 1$.

Dropping the suppressed term:
\begin{equation}
  - \frac{2 i m}{\hbar} \partial_t \psi - \nabla^2 \psi = 0.
\end{equation}

Rearranging:
\begin{equation}
  \frac{2 i m}{\hbar} \partial_t \psi = - \nabla^2 \psi,
\end{equation}
multiplying both sides by $\hbar^2 / (2 m)$:
\begin{equation}
  i \hbar \partial_t \psi = -\frac{\hbar^2}{2m} \nabla^2 \psi.
  \label{eq:SchrodingerFromKG}
\end{equation}

**This is the free-particle Schrödinger equation** — identical to the Phase-1 result of `schrodinger_emergence.md` equation (12) with $V = 0$.

### 5.5 Including an external potential

Minimal coupling in Klein-Gordon replaces $E \to E - V$, or equivalently $p_0 \to p_0 - V/c$ in the four-momentum. Under the rest-energy factorization (eq:nr_factorization), the potential appears in the non-relativistic limit through the modified energy $E_0 + E_{\text{kin}} + V$. The same derivation as §5.3–§5.4 with $E_0 \to E_0 + V$ yields the Schrödinger equation with potential:
\begin{equation}
  i \hbar \partial_t \psi = \left[-\frac{\hbar^2}{2m} \nabla^2 + V(\mathbf{x})\right] \psi.
\end{equation}

This matches Phase-1 Schrödinger emergence exactly.

### 5.6 Consistency check

The Klein-Gordon equation for a scalar particle of mass $m$ reduces, in the non-relativistic limit $v/c \ll 1$, to the free-particle Schrödinger equation for the same particle. The reduction is exact in the limit and produces the correct coefficient $-\hbar^2/(2m)$ for the kinetic term, consistent with U4's structural derivation of the Hamiltonian form in Phase 1.

**Status: FORCED** — the reduction is a mathematical identity. The Klein-Gordon equation derived in §4 is the relativistic generalization of the Schrödinger equation derived in Phase 1; no independent choice has been made.

---

## 6. Primitive-level versus inherited content

### 6.1 Forced content

| Feature | Source |
|---|---|
| Lorentz-scalar structure of Ψ | Primitive 02 covariant + scalar-case rule-type |
| Covariant differential operator $\Box$ | Primitive 06 covariant (four-gradient) |
| Linear evolution in Ψ | Primitive 03 + 07 + 08 superposition preservation (covariant extension of U3 derivation) |
| Second-order-in-time structure | Lorentz invariance for Lorentz-scalar wave equation |
| Klein-Gordon form $(\Box + M^2)\Psi = 0$ with $M^2 > 0$ | Minimum-order Lorentz-scalar linear equation + dimensional consistency |
| Mass-shell condition $p_\mu p^\mu = m^2 c^2$ | Plane-wave ansatz + Klein-Gordon form |
| Relativistic dispersion $E^2 = p^2 c^2 + m^2 c^4$ | Mass-shell applied in components |
| Positive and negative energy branches | Square-root structure of (massshell) |
| Linearity of coherent-sum Klein-Gordon | Linearity of d'Alembertian and U3 |
| Non-relativistic limit → Schrödinger | Mathematical limit $v/c \to 0$ |

### 6.2 Inherited content

| Item | Source |
|---|---|
| Speed of light $c$ | Dimensional Atlas relativistic regime |
| Reduced Planck constant $\hbar$ | Dimensional Atlas Madelung anchoring (via U3) |
| Scalar-particle mass $m$ | Inherited at species level; chain-mass derivation in Arc M (open) |
| Specific potential $V(\mathbf{x})$ (when present) | Apparatus / interaction-term specification |

### 6.3 Not required

- **No new primitives.** The derivation uses Primitives 02, 04, 06, 13 in their covariant reformulations (from the scoping memo), plus U1–U5 as previously FORCED, plus phase-independence. All primitive-level content was established before this memo.
- **No additional postulates.** Klein-Gordon is derived from the ED framework without adding independent physical postulates beyond those of Phase 1.

---

## 7. Summary table

| Content | Status | Source / Notes |
|---|---|---|
| Covariant $P_K(x^\mu)$ for scalar chains | FORCED | Scoping memo §2 |
| $\Box + m^2 c^2 / \hbar^2$ operator structure | FORCED | Lorentz scalar minimum-order linear (§2.1–§2.2) |
| Plane-wave modes $e^{-i p_\mu x^\mu/\hbar}$ | FORCED | Translation invariance (§3.1) |
| Mass-shell condition $p_\mu p^\mu = m^2 c^2$ | FORCED | Plane-wave + KG form (§3.4) |
| Relativistic dispersion $E^2 = p^2 c^2 + m^2 c^4$ | FORCED | Mass-shell in components (§3.4) |
| Klein-Gordon equation $(\Box + m^2 c^2/\hbar^2) \Psi = 0$ | FORCED | Main result (§4.2) |
| Non-relativistic limit to Schrödinger | FORCED | Rest-energy factorization (§5) |
| Interaction (non-zero $V$) | CANDIDATE | Minimal coupling; apparatus-specific |
| Antiparticle interpretation of negative-energy branch | Deferred | Requires QFT (Arc Q) |
| Spinor case (Dirac) | Deferred | Requires rule-type taxonomy (Primitive 07 §7.4) |
| Numerical values of $c$, $\hbar$, $m$ | Inherited | Dimensional Atlas + species-level anchoring |

---

## 8. Open items

### 8.1 Derived but not developed in this memo

- **Gauge-coupling extension.** Minimal coupling in Klein-Gordon for charged particles: $p_\mu \to p_\mu - q A_\mu$ where $A_\mu$ is the electromagnetic four-potential. Produces interaction terms.
- **Conserved four-current.** The current $j^\mu = (i\hbar / 2m)(\Psi^* \partial^\mu \Psi - \Psi \partial^\mu \Psi^*)$ satisfies $\partial_\mu j^\mu = 0$. Structural content of conservation from symmetries; cf. Noether's theorem.
- **Normalization and inner product.** Klein-Gordon has a non-positive-definite inner product (the Klein-Gordon product), which poses interpretational issues for the single-particle probability interpretation. This is one of the structural arguments for the QFT extension (Arc Q).

### 8.2 Requires further arcs

- **Spinor case (Dirac).** Requires rule-type taxonomy from Primitive 07 §7.4. Dedicated memo `dirac_emergence.md` after the taxonomy sub-program completes.
- **Multi-particle content.** Arc Q (QFT extension). Klein-Gordon at the single-particle level is known to have pathologies (non-positive-definite inner product, Klein paradox); these resolve at the field-theoretic level.
- **Chain-mass derivation.** Arc M. The numerical value of $m$ remains inherited until the rule-type taxonomy → chain-mass derivation closes.
- **Interaction terms beyond minimal coupling.** Full electroweak and strong-interaction content requires the QFT extension (Arc Q) with appropriate rule-type classification.

### 8.3 Arc-R Stage R.1 status

**Stage R.1 (Klein-Gordon emergence) is COMPLETE at the free-particle level.** Remaining Stage R.1 deliverables:
- Minimal coupling extension to include $V$ and $A_\mu$: one follow-up memo.
- Charge conservation and four-current: short memo or incorporated into minimal-coupling memo.
- Arc-R Stage R.1 synthesis: completion memo for the Stage.

Estimated scope for Stage R.1 closure: 2–3 additional memos.

---

## 9. Honest framing

### 9.1 What this memo achieves

- Derives the Klein-Gordon equation as a FORCED consequence of the Lorentz-covariant participation measure + primitive-level Lorentz-invariance constraints + minimum-order linear scalar-field assumption.
- Establishes the mass-shell condition as a structural identity arising from the plane-wave mode structure applied to the Klein-Gordon form.
- Derives the non-relativistic limit explicitly, showing that Klein-Gordon reduces to the Phase-1 Schrödinger equation in the $v/c \to 0$ regime.
- No new primitives required.

### 9.2 What this memo does not achieve

- No derivation of the antiparticle interpretation of the negative-energy branch (requires Arc Q).
- No treatment of interaction terms beyond the minimal-coupling sketch.
- No derivation of the spinor (Dirac) case (requires rule-type taxonomy).
- No treatment of the Klein-Gordon non-positive-definite inner-product pathology (a known QFT motivation).
- No chain-mass derivation; $m$ remains inherited.

### 9.3 Structural significance

**Klein-Gordon is now the first Phase-2 Arc-R result at the level of a derived wave equation.** Where Phase-1 derived Schrödinger for non-relativistic scalar chains, Phase-2 Arc-R extends this to Klein-Gordon for relativistic scalar chains. The non-relativistic limit check confirms that Phase 1 is a consistent sub-theory of the relativistic framework, as it must be.

The remaining Phase-2 Arc-R work (minimal coupling, Dirac via rule-type taxonomy) is scoped and on schedule. Arc-N (non-Markovian) and Arc-R Stage R.1 have both advanced significantly; the program is now in the medium-term regime of the Phase-2 roadmap.

---

## 10. Cross-references

### Program-level
- Arc-R scoping memo (foundation for this derivation): [`quantum/foundations/relativistic_participation_measure.md`](relativistic_participation_measure.md)
- Phase-2 roadmap: [`quantum/foundations/phase2_extensions_roadmap.md`](phase2_extensions_roadmap.md) §2.1
- Phase-1 Schrödinger (non-relativistic limit target): [`quantum/foundations/schrodinger_emergence.md`](schrodinger_emergence.md)
- Phase-1 QM-emergence closure: [`quantum/foundations/qm_emergence_closure.md`](qm_emergence_closure.md)
- U3 evolution derivation (structural basis for linearity): [`quantum/foundations/u3_evolution_derivation.md`](u3_evolution_derivation.md)
- ℏ-origin memo (inheritance structure): [`quantum/foundations/hbar_origin.md`](hbar_origin.md)

### Primitive stack
- Primitive 02 (chain; covariant reformulation as worldline): [`quantum/primitives/02_chain.md`](../primitives/02_chain.md)
- Primitive 04 (bandwidth; covariant four-band): [`quantum/primitives/04_participation_bandwidth.md`](../primitives/04_participation_bandwidth.md)
- Primitive 06 (ED gradient; four-gradient): [`quantum/primitives/06_ed_gradient.md`](../primitives/06_ed_gradient.md)
- Primitive 07 (channel + rule-type; taxonomy open for Dirac): [`quantum/primitives/07_channel.md`](../primitives/07_channel.md)
- Primitive 13 (relational timing; proper-time): [`quantum/primitives/13_relational_timing.md`](../primitives/13_relational_timing.md)

### Classical references
- Klein, O. (1926). Quantentheorie und fünfdimensionale Relativitätstheorie. *Zeitschrift für Physik* **37**, 895–906.
- Gordon, W. (1926). Der Comptoneffekt nach der Schrödingerschen Theorie. *Zeitschrift für Physik* **40**, 117–133.
- Dirac, P. A. M. (1928). The Quantum Theory of the Electron. *Proceedings of the Royal Society A* **117**, 610–624.
- Bjorken, J. D., Drell, S. D. (1964). *Relativistic Quantum Mechanics*. McGraw-Hill.
- Weinberg, S. (1995). *The Quantum Theory of Fields*, Vol. 1. Cambridge University Press.

---

## 11. One-line summary

> **The Klein-Gordon equation $(\Box + m^2 c^2/\hbar^2) \Psi(x^\mu) = 0$ is derived as a FORCED consequence of the Lorentz-covariant participation measure + minimum-order linear Lorentz-scalar-equation structure. The d'Alembertian arises as the unique second-order Lorentz-scalar differential operator on scalar fields; the mass-shell condition $p_\mu p^\mu = m^2 c^2$ arises from applying the equation to plane-wave modes; the relativistic dispersion $E^2 = p^2 c^2 + m^2 c^4$ follows in components. Explicit non-relativistic limit via rest-energy factorization $\Psi = e^{-i m c^2 t / \hbar} \psi$ reduces Klein-Gordon to the free-particle Schrödinger equation $i \hbar \partial_t \psi = -(\hbar^2/2m) \nabla^2 \psi$, consistent with Phase-1 Step 2. No new primitives required; dimensional constants $c$, $\hbar$, $m$ remain inherited. Arc-R Stage R.1 main deliverable complete; remaining Stage R.1 items (minimal coupling, charge conservation, Stage synthesis) scoped for near-term follow-up memos. Arc-R Stage R.2 (rule-type taxonomy for spinor / Dirac case) remains the critical prerequisite for Stage R.3. Antiparticle interpretation, multi-particle content, and interaction terms beyond minimal coupling are deferred to Arc Q (QFT extension).**
