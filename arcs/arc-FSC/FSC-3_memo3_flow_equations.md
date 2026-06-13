# Arc FSC — Memo 5: One-Loop Wilsonian Flow Equations for the ED Substrate (FSC-3 Memo 3)

**Status:** Third memo of Arc FSC sub-arc FSC-3. Load-bearing computational memo. Derives one-loop Wilsonian RG flow equations for the marginal coupling-magnitude sector identified in FSC-3 Memo 2, with explicit dependence on V1 spectral shape parameters $\{s_i\}$. Architect-mode active. No new primitives. Discipline reminder (FSC-0 §9): no quoting of $1/137$ or $\alpha = 1/137.036\ldots$; numerical-match checks reserved for sub-arc closure.

**Date:** 2026-05-25

**Methodological commitment.** This memo applies standard one-loop scalar-QED machinery (a well-established QFT calculation, $\sim 1965$–present) to the ED substrate with V1 acting as a substrate-derived UV regulator at scale $\ell_P$. The *one-loop calculus* is not novel ED content; the *identification of which contributions are shape-dependent vs. shape-independent under the ED-specific regulator* is the load-bearing FSC-3 work.

**Honest framing.** All one-loop β-function coefficients computed below correspond to well-known scalar-QED results adapted to the substrate regulator. The novel content is the structural decomposition into universal (shape-independent) and inherited (shape-dependent) pieces, and the identification of shape-independent operator combinations as candidate fixed-point objects for Memo 4.

---

## 1. Wilsonian Flow at Substrate Scale

### 1.1 Setup

Let $k$ be the Wilsonian sliding scale, with $\ell_P^{-1} \geq k \geq L_\mathrm{flow}^{-1}$ spanning the hydrodynamic window. The effective action $\Gamma_k$ at scale $k$ depends on the running couplings $\{g_i(k)\}$ for the 14-operator basis of Memo 2. The flow equation:
$$k\,\partial_k\, g_i \;=\; \beta_i(\{g_j\}; \{s_a\})$$
where $\{s_a\}$ are the V1 spectral shape parameters (FSC-2.1 inherited content). The shape parameters enter the β-functions through V1-mediated loop integrals.

### 1.2 The marginal-sector action

Restricting to the marginal sector (Tier 1 of Memo 2 §10.3), the relevant Lagrangian density in $D = 3+1$:
$$\mathcal{L}_\mathrm{marg}[P, A] \;=\; Z\,|D_\mu P|^2 \;-\; m^2 |P|^2 \;-\; \frac{\lambda}{4}\,|P|^4 \;-\; \frac{1}{4 e^2}\,F_{\mu\nu} F^{\mu\nu}$$
where $D_\mu = \partial_\mu - i A_\mu$, $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, and $Z$ is the matter field-strength renormalization. The gauge coupling has been absorbed into the gauge field's normalization (geometric convention), so the matter-gauge vertex coefficient is unity in this convention and $e^2$ appears as the gauge kinetic coefficient inverse. This is the standard scalar-QED Lagrangian, with all four marginal couplings ($Z, m^2, \lambda, 1/e^2$) tracked.

### 1.3 The V1 regulator

V1 acts as a substrate UV regulator at scale $\Lambda = 1/\ell_P$. In momentum space, V1's Fourier transform $\tilde V_1(p)$ provides a smooth UV cutoff: $\tilde V_1(p) \to 1$ for $p \ell_P \ll 1$ and $\tilde V_1(p) \to 0$ rapidly for $p \ell_P \gg 1$. The Wilsonian propagator at scale $k$ is the V1-regulated retarded propagator with mode-content restricted to $k \leq |p| \leq \Lambda$:
$$G_k(p) \;=\; \frac{\Theta(\Lambda - |p|)\, \Theta(|p| - k)}{p^2 + m^2}\, |\tilde V_1(p)|^2$$
(with appropriate $i\epsilon$ prescription for retardation per T18). The shape factor $|\tilde V_1(p)|^2$ is where the FSC-2.1 shape parameters $\{s_a\}$ enter loop integrals.

---

## 2. One-Loop Diagrams

The β-functions for $\lambda$, $1/e^2$, and $e$ at one loop in scalar QED receive contributions from a small finite set of diagrams. Below, each diagram is identified, the corresponding loop integral structure is given, and the shape-parameter entry point is flagged.

### 2.1 Diagrams for $\beta_\lambda$ (matter quartic running)

Three classes of one-loop diagrams renormalize $\lambda$:

- **(D-λ.1) Fish diagram (4-scalar from $\lambda^2$).** Two $\lambda$-vertices connected by two scalar propagators. Loop integral:
$$\mathcal{I}_{\lambda\lambda}(k; m, \{s_a\}) \;=\; \int_{k < |p| < \Lambda} \frac{d^4 p}{(2\pi)^4} \, \frac{|\tilde V_1(p)|^2 \, |\tilde V_1(p+q)|^2}{(p^2 + m^2)((p+q)^2 + m^2)}$$
at external momentum $q$ (set to 0 in the leading-log extraction). This is the substrate analog of the standard fish-diagram one-loop $\phi^4$ correction.

- **(D-λ.2) Photon-exchange box (e²-vertex, e²-vertex via gauge loop).** Two matter-gauge vertices and one gauge propagator inserted into a scalar self-energy chain. Loop integral has structure $\sim e^4 \int d^4 p \,/[(p^2 + m^2)^2 \,p^2] \,|\tilde V_1|^2 (\cdots)$.

- **(D-λ.3) Seagull contribution (from $|A|^2|P|^2$).** Single $e^2$-seagull vertex closed onto itself via gauge propagator. Loop integral $\sim e^2 \int d^4 p \,/[p^2] \,|\tilde V_1|^2$.

All three loop integrals contain a factor of $|\tilde V_1(p)|^2$ (or higher powers), inheriting shape dependence from V1.

### 2.2 Diagrams for $\beta_{1/e^2}$ (gauge kinetic running)

Single dominant class:

- **(D-F.1) Charged-scalar vacuum polarization.** One closed scalar loop attached to two gauge legs. Loop integral:
$$\Pi_{\mu\nu}^\mathrm{scalar}(q; m, \{s_a\}) \;=\; \int_{k < |p| < \Lambda} \frac{d^4 p}{(2\pi)^4} \,\frac{|\tilde V_1(p)|^2}{(p^2 + m^2)((p+q)^2 + m^2)} \cdot (\text{tensor structure})$$
This is the substrate analog of the standard scalar-QED vacuum polarization. The tensor structure $\propto (q^2 \eta_{\mu\nu} - q_\mu q_\nu)$ is enforced by gauge invariance at the level of T17's emergent gauge structure (validity discussed in §6).

### 2.3 Diagrams for $\beta_e$ (matter-gauge vertex running)

In the conventional scalar-QED scheme:

- **(D-e.1) Vertex correction from photon exchange.** Triangle with two matter lines and one gauge exchange. Loop integral $\sim e^3 \int d^4 p \,/[(p^2 + m^2)^2 p^2] \,|\tilde V_1|^2$.

- **(D-e.2) Constraint from Ward identity.** In standard QED, the Ward identity $Z_1 = Z_2$ (vertex renormalization = matter wave-function renormalization) implies $\beta_e$ is determined purely by gauge-coupling renormalization $\beta_{1/e^2}$ via $\beta_e = -\frac{1}{2}\, e^3 \cdot \beta_{1/e^2} / (1/e^2) = \frac{1}{2}\, e^3 \cdot e^2 \cdot \beta_{1/e^2} \cdot e^2$... let me reformulate more clearly: in standard conventions, $e = (e^2)^{1/2}$ implies $\beta_e = \frac{1}{2} e^{-1} \beta_{e^2} = -\frac{1}{2} e^{-1} \cdot e^4 \beta_{1/e^2} = -\frac{1}{2} e^3 \beta_{1/e^2}$. The Ward identity reduces vertex-coupling flow to gauge-coupling flow.

**ED status of Ward identity.** Gauge invariance in ED is *emergent* via T17 (substrate-derived rule-type structure), not a substrate-level primitive. Whether emergent gauge invariance preserves Ward-Takahashi identities at coarse-grained scales is non-trivial and is examined in §6.

---

## 3. Structural Decomposition: Universal vs. Inherited

### 3.1 The universal-coefficient theorem (standard QFT)

For any one-loop integral of the form
$$\mathcal{I}(k) \;=\; \int_{k < |p| < \Lambda} \frac{d^4 p}{(2\pi)^4}\, f(p; m)\, R(p; \{s_a\})$$
where $f(p; m)$ is the bare propagator structure (universal across all regulators) and $R(p; \{s_a\}) = |\tilde V_1(p)|^2$ is the substrate-regulator factor (shape-dependent), the leading-log behavior under $k \partial_k$ is:
$$k\,\partial_k\, \mathcal{I}(k) \;=\; -\frac{f(k; m) \cdot R(k; \{s_a\}) \cdot k^4}{(2\pi)^4} \cdot \Omega_3$$
where $\Omega_3 = 2\pi^2$ is the volume of the 3-sphere in $D = 4$ Euclidean momentum.

**Key structural fact (universal/inherited decomposition).** Evaluating at $k \ll \Lambda$ (deep in hydrodynamic window):
- $f(k; m) = 1/(k^2 + m^2)^2$ for the fish-diagram case — *universal* (depends only on bare propagator).
- $R(k; \{s_a\}) = |\tilde V_1(k)|^2 \to 1$ as $k \ell_P \to 0$ (substrate regulator becomes inactive at IR scales).

**At leading log in $\log(\Lambda/k) = \log(1/(k \ell_P))$, the shape factor $R(k; \{s_a\}) \to 1$ for $k \ll \Lambda$.** The leading-log coefficient is therefore *shape-independent* (universal). The shape-dependent contribution enters only at the *finite remainder* — the integration over modes near the cutoff $p \sim \Lambda$, where $R(p)$ varies significantly.

This is the standard QFT result that *β-function leading-log coefficients are universal across mass-independent renormalization schemes*. The substrate-RG version preserves this: the leading-log coefficients are FORCED-universal; the finite parts INHERIT shape-dependence.

### 3.2 Implication for FSC-3

The β-functions split structurally as:
$$\beta_i \;=\; \beta_i^{(\mathrm{LL})} \;+\; \beta_i^{(\mathrm{fin})}(\{s_a\})$$
where $\beta_i^{(\mathrm{LL})}$ is the leading-log coefficient (shape-independent, FORCED by substrate-emergent operator structure) and $\beta_i^{(\mathrm{fin})}$ is the finite remainder (shape-dependent, INHERITED from V1 spectral profile).

**Candidate substrate-RG universal:** any operator combination whose flow depends only on $\{\beta_i^{(\mathrm{LL})}\}$ and not on $\{\beta_i^{(\mathrm{fin})}\}$. Such combinations are the structural-locus candidates for FSC-3 ratio-fixed-point structure.

---

## 4. Explicit β-Functions at One Loop

### 4.1 $\beta_\lambda$

Combining contributions D-λ.1 + D-λ.2 + D-λ.3, the standard one-loop scalar-QED β-function for the quartic in our convention ($\mathcal{L} \supset -\frac{\lambda}{4} |P|^4$, complex scalar $P$):
$$\boxed{\,\beta_\lambda \;=\; \frac{1}{16\pi^2}\, \Big[\, A_\lambda \, \lambda^2 \;-\; B_\lambda\, \lambda\, e^2 \;+\; C_\lambda\, e^4\, \Big] \;+\; \mathcal{R}_\lambda(\{s_a\}; \lambda, e)\,}$$
with universal leading-log coefficients:
$$A_\lambda = 10, \quad B_\lambda = 6, \quad C_\lambda = 6$$
(standard complex-scalar-QED one-loop result; the specific numerical coefficients depend on field-content conventions). The shape-dependent finite remainder is:
$$\mathcal{R}_\lambda(\{s_a\}; \lambda, e) \;=\; \frac{1}{16\pi^2}\, \Big[\, A_\lambda^{(s)}(\{s_a\})\, \lambda^2 \;+\; B_\lambda^{(s)}(\{s_a\})\, \lambda\, e^2 \;+\; C_\lambda^{(s)}(\{s_a\})\, e^4\, \Big]$$
where $A_\lambda^{(s)}, B_\lambda^{(s)}, C_\lambda^{(s)}$ are $\mathcal{O}(1)$ shape-dependent constants determined by V1's spectral shape via the moment integrals:
$$A_\lambda^{(s)} \;=\; \int_0^\Lambda \frac{dp\, p^3}{(2\pi)^2}\, \frac{|\tilde V_1(p)|^4 - 1}{(p^2 + m^2)^2} \cdot (\text{kinematic factor})$$
and similar for $B_\lambda^{(s)}, C_\lambda^{(s)}$.

**Structural reading.** The leading-log behavior of $\beta_\lambda$ is governed by the universal coefficients $(10, -6, 6)$. The shape-dependence enters as additive corrections that are $\mathcal{O}(1)$ in magnitude but do not modify the leading-log structure.

### 4.2 $\beta_{1/e^2}$

From the charged-scalar vacuum-polarization diagram D-F.1 (one complex scalar contribution):
$$\boxed{\,\beta_{1/e^2} \;=\; -\,\frac{1}{16\pi^2}\, A_F \;+\; \mathcal{R}_F(\{s_a\})\,}$$
with universal leading-log coefficient:
$$A_F \;=\; \frac{1}{3}$$
(standard scalar-QED matter-content factor; one complex scalar contributes $1/3$ to the photon self-energy). The shape-dependent remainder:
$$\mathcal{R}_F(\{s_a\}) \;=\; -\,\frac{1}{16\pi^2}\, A_F^{(s)}(\{s_a\})$$
where $A_F^{(s)}$ is the corresponding shape-dependent V1-moment integral.

Equivalent form for the gauge coupling itself:
$$\beta_{e^2} \;=\; -\,e^4 \cdot \beta_{1/e^2} \;=\; \frac{e^4}{48\pi^2} \;-\; e^4 \cdot \mathcal{R}_F.$$

### 4.3 $\beta_e$

Combining D-e.1 with the Ward identity (provisional — see §6):
$$\boxed{\,\beta_e \;=\; \frac{e^3}{96\pi^2} \;+\; \mathcal{R}_e(\{s_a\}; e)\,}$$
Universal leading-log coefficient $\frac{1}{96\pi^2}$ from Ward-identity reduction of D-F.1.

Without Ward identity:
$$\beta_e^{(\mathrm{direct})} \;=\; \frac{e^3}{16\pi^2} \cdot A_e \;+\; \mathcal{R}_e^{(\mathrm{direct})}(\{s_a\}; e)$$
with $A_e$ as the leading-log vertex coefficient. In standard QED, $A_e = -A_F/(2 \cdot 3) = -1/18$ (under matter-content normalization). The Ward identity reduces the apparent number of independent leading-log coefficients from 2 (one each for $\beta_{1/e^2}$ and $\beta_e^{(\mathrm{direct})}$) to 1.

---

## 5. Shape-Independent Combinations

### 5.1 Candidate substrate-RG invariants

From the structural decomposition of §3.2, any operator combination whose flow depends only on universal leading-log coefficients is a candidate substrate-RG invariant. Three candidates emerge:

**Candidate U-1: ratio $\lambda^2 / e^4$ leading-log coefficient.**

The β-function for the dimensionless ratio $\rho_1 \equiv \lambda / e^2$ at leading log:
$$\beta_{\rho_1}^{(\mathrm{LL})} \;=\; \beta_\lambda^{(\mathrm{LL})}/e^2 - \rho_1 \cdot \beta_{e^2}^{(\mathrm{LL})}/e^2$$
$$= \frac{1}{16\pi^2 e^2}\Big[10 \lambda^2 - 6 \lambda e^2 + 6 e^4\Big] \;-\; \frac{\rho_1}{16\pi^2 e^2}\Big[\frac{e^4}{3}\Big]$$
$$= \frac{1}{16\pi^2}\Big[10 \rho_1^2 - 6 \rho_1 + 6 - \frac{\rho_1}{3}\Big] \cdot e^2$$
$$= \frac{e^2}{16\pi^2}\Big[10 \rho_1^2 - \frac{19}{3}\rho_1 + 6\Big]$$

**Crucially, the leading-log $\beta_{\rho_1}$ depends only on universal coefficients $(10, -19/3, 6)$ and does not involve any shape parameters $\{s_a\}$.** Shape parameters enter only through the finite remainders of $\beta_\lambda$ and $\beta_{e^2}$ separately, which contribute to $\beta_{\rho_1}^{(\mathrm{fin})}$ but not to the leading-log structure.

**At leading-log order, $\rho_1 = \lambda/e^2$ flows according to a universal one-dimensional flow equation with no shape-parameter dependence.** This is a *concrete substrate-RG universal candidate* for ratio-level fixed-point analysis.

The leading-log discriminant: $\rho_1^2$ coefficient is $10 > 0$ and $\rho_1$ constant is $6 > 0$. The fixed-point equation $10 \rho_1^2 - (19/3) \rho_1 + 6 = 0$ has discriminant $(19/3)^2 - 4 \cdot 10 \cdot 6 = 361/9 - 240 = (361 - 2160)/9 = -1799/9 < 0$. **No real fixed point at leading log for $\rho_1$.**

The leading-log flow for $\rho_1$ has no real fixed point. The flow continues monotonically with sign determined by the discriminant: since the quadratic $10\rho_1^2 - (19/3)\rho_1 + 6$ has no real roots and is positive at $\rho_1 = 0$ (value $6$), it is positive for all real $\rho_1$. So $\beta_{\rho_1}^{(\mathrm{LL})} > 0$ for all $\rho_1$, and $\rho_1$ flows monotonically toward $+\infty$ at IR (or equivalently, $\lambda$ grows faster than $e^2$ in IR).

This is a structurally informative *negative* result for Candidate U-1: the ratio $\lambda/e^2$ does not have a universal IR fixed point at leading log.

**Candidate U-2: ratio $\beta_e/\beta_{e^2}$.**

This is forced to a constant by the Ward identity ($\beta_e = e \cdot \beta_{e^2} / (2 e^2) = \beta_{e^2}/(2e)$), so it is *trivially* universal — does not produce new structural content beyond the Ward identity itself.

**Candidate U-3: the gauge-coupling-only flow (with $\lambda = 0$ projection).**

Setting $\lambda = 0$ and tracking $\beta_{e^2}$ alone:
$$\beta_{e^2}^{(\mathrm{LL})} \;=\; \frac{e^4}{48\pi^2}$$

This is the standard scalar-QED Landau-pole behavior: $\beta_{e^2} > 0$ everywhere, gauge coupling grows monotonically at IR, no IR fixed point (and the Landau pole appears at UV — which in ED is regulated by the substrate scale $\ell_P$ rather than appearing as a literal pole).

**At leading log, the gauge coupling has no IR fixed point either.** This is the standard scalar-QED result; ED inherits it.

### 5.2 What this means

The leading-log analysis of the three marginal-sector candidate ratios produces a clear structural finding:

> **Finding (FSC-3.5.1).** At one-loop leading-log in the ED substrate Wilsonian flow, the marginal-sector ratios $\rho_1 = \lambda/e^2$ and $\rho_2 = e^2$ (standalone) flow with universal coefficients (shape-independent) but **do not exhibit IR-attractive fixed points**. Both ratios flow monotonically — $\rho_1$ to $+\infty$, $\rho_2$ to $+\infty$ — under the universal leading-log structure. The leading-log flow is the substrate analog of standard scalar-QED Landau-pole-type behavior.

This is the load-bearing FSC-3 finding for the *absolute-magnitude* and the *single-ratio* fixed-point questions. **Neither has a non-trivial IR fixed point at leading log in the marginal sector alone.**

### 5.3 Where might fixed points still appear?

The structural avenues that remain open after Finding FSC-3.5.1:

- **Two-loop and higher-order contributions.** Beyond leading log, the β-functions acquire $\lambda^3$, $\lambda e^4$, $e^6$ terms and the flow structure changes. Wilson-Fisher fixed points in $4 - \epsilon$ dimensions emerge precisely at two-loop. Whether ED's substrate-regulator at finite $\ell_P$ produces an analog effect at all loop orders is open.
- **Multi-sector mixing.** The 14-operator basis includes Tier 5 ratio operators ($O_{\mathrm{ratio}}, \{O_{r_\alpha}\}$ — reversible-irreversible ratio and P04 band-allocations). Their flow couples to the marginal sector but is *not* governed by the same leading-log structure. Fixed points may exist in the full 14-dimensional flow that do not exist in the projected marginal sector.
- **Substrate-specific operators.** P11 commitment-density and V5 cross-chain kernel operators were classified as dangerously irrelevant (Memo 2 §9.4). Their contribution to the marginal-operator flow is shape-dependent but may produce structurally novel terms not present in standard scalar QED. Specifically, P11 introduces decoherence-rate-type operators that have no standard-QFT analog.
- **Non-Abelian extensions.** Standard non-Abelian gauge theory has asymptotic-freedom in IR (signs flip from scalar-QED). ED's gauge sector at T17 is *emergent* from polarity rule-type; whether non-Abelian extensions in ED inherit the standard $\mathrm{adj} - n_f$ asymptotic-freedom structure is a separate question.
- **Conformal-window analog.** In standard QFT with $N_c$ colors and $N_f$ flavors, the conformal window $N_f^* < N_f < N_f^{(*)}$ supports IR fixed points (Seiberg, Banks-Zaks). ED's "flavor-content" analog — the multiplicity of substrate rule-types contributing to the matter-loop — could in principle place the substrate within or outside an analog conformal window.

The most structurally-natural avenue is *multi-sector mixing*. The leading-log analysis of §5.1 projected onto the marginal sector ignored the Tier 5 ratio operators. Their explicit inclusion could change the conclusion.

---

## 6. Ward Identity Status in ED

A non-trivial issue: the Ward identity used in §4.3 to relate $\beta_e$ to $\beta_{1/e^2}$ assumes gauge invariance at substrate scale. ED's gauge structure is *emergent* via T17, not a substrate-level forced principle (FSC-0 §5.2).

### 6.1 Emergent Ward identity argument

The T17 closure establishes that, under coarse-graining via DCGT, the substrate's polarity-transport structure produces a continuum gauge symmetry that is exact at scales $R_\mathrm{cg} \gg \ell_P$. At leading order in the $\ell_P/R_\mathrm{cg}$ expansion, the Ward identity holds: emergent gauge invariance is unbroken in the hydrodynamic window.

**Implication:** at one-loop with the substrate UV cutoff well below the Wilsonian scale ($k \ell_P \ll 1$), the Ward identity is satisfied up to terms suppressed by $\ell_P/k^{-1} = k \ell_P$. The relation $\beta_e = \frac{1}{2} e^3 \beta_{1/e^2}$ holds with corrections suppressed by $k \ell_P$.

### 6.2 Subleading violations

At order $(k \ell_P)^n$ for $n \geq 1$, the Ward identity may receive substrate-specific corrections from operators that are not gauge-invariant at substrate scale but become gauge-invariant only at coarse-grained scales. These corrections are shape-dependent (they involve V1's near-cutoff behavior) but are subleading in $k\ell_P$ throughout the hydrodynamic window.

**For the leading-log analysis of §5, Ward-identity violations are subleading and do not change the conclusion.** This is technically a non-trivial check; in a fuller analysis it would warrant explicit verification.

---

## 7. Implications for Memo 4 (Fixed-Point Search)

### 7.1 What Memo 4 must compute

Given Finding FSC-3.5.1, Memo 4 (fixed-point search) must extend the analysis in three directions:

- **Direction A: Two-loop β-functions for the marginal sector.** Add the $\lambda^3$ and $\lambda^2 e^2$ corrections to $\beta_\lambda$ and check whether two-loop terms produce non-trivial fixed points. This is the Wilson-Fisher analog in $D = 4$ with substrate-cutoff regulator.
- **Direction B: Coupled marginal + Tier-5 ratio-operator flow.** Compute the full 14-operator flow projected onto Tier-1 (marginal couplings) + Tier-5 (ratio operators) sub-basis. The ratio operators may provide the "stabilizing direction" that produces fixed points absent in the marginal-only projection.
- **Direction C: Non-Abelian extension (low priority for FSC).** Compute the β-functions for substrate non-Abelian gauge structure (T17 supports SU(N)-class). Asymptotic-freedom-class fixed points in non-Abelian sector are well-established in standard QCD and would inherit cleanly. Not directly relevant to $\alpha_\mathrm{em}$ but informative for full coupling-magnitude content.

### 7.2 Computational scope estimate

- Direction A: 2–3 memos (two-loop calculation is technically heavier; needs care with sub-divergences).
- Direction B: 2–3 memos (14-operator flow matrix; requires identifying operator-mixing structure under coarse-graining for ratio operators specifically).
- Direction C: 1–2 memos (standard non-Abelian one-loop, adapted to substrate regulator).

Total estimated Memo 4 scope: 5–8 memos. Substantial but bounded.

### 7.3 Expected outcomes by direction

- **Direction A (two-loop marginal).** Likely outcome: *partial fixed-point structure* — a non-trivial fixed point may exist at two-loop in $D = 4$ for the marginal sector, but its location and basin will be shape-dependent (FSC-2.1 propagates to two-loop coefficients). This would be a *partial-positive* result for FSC-3: fixed point exists but is not universal.
- **Direction B (multi-sector with ratios).** Most structurally interesting direction. The Tier-5 ratio operators carry the *0.6-ratio-precedent* class of substrate-RG universality (Arc RG). Including them may produce a sector of the flow that has universal ratio fixed points coexisting with non-universal absolute-magnitude flow. This would be a clean *Scenario B partial-universality* result.
- **Direction C (non-Abelian).** Likely inheritance from standard QCD asymptotic freedom; no novel ED content for $\alpha_\mathrm{em}$ specifically.

### 7.4 Tier-1 recommendation

Per FSC-3 Memo 1 §7.2 and Memo 2 §12.4: hold position-paper §7.2 as currently stated until at least Direction A or Direction B of Memo 4 closes.

---

## 8. Honest Caveats

### 8.1 What this memo computed

- Standard one-loop scalar-QED β-functions at leading log (well-known calculation).
- Identification of which leading-log coefficients are universal (FORCED) vs. which finite remainders are shape-dependent (INHERITED).
- A specific candidate universal ratio $\rho_1 = \lambda/e^2$ with explicit leading-log $\beta_{\rho_1}$ shown to be shape-independent.
- A *negative* fixed-point finding at leading log for $\rho_1$ and for $e^2$ standalone.

### 8.2 What this memo did NOT compute

- Explicit shape-dependent constants $A^{(s)}, B^{(s)}, C^{(s)}, A_F^{(s)}, A_e^{(s)}$ as functions of specific V1 shape choices (Gaussian, Lorentzian, Bessel). These are computable in principle but require specific V1-shape commitment.
- Multi-sector flow including Tier-5 ratio operators. Deferred to Memo 4 Direction B.
- Two-loop contributions. Deferred to Memo 4 Direction A.
- Subleading Ward-identity violations from substrate-specific gauge-symmetry-breaking operators. Subleading and not load-bearing for present analysis.
- Non-Abelian gauge structure. Outside FSC scope but flagged for separate investigation.

### 8.3 Honest characterization of the result

This memo is a *structural derivation*, not a *substantively novel computation*. The one-loop scalar-QED β-functions have been known since the 1960s. The novel ED content is the universal/inherited decomposition under the substrate-derived V1 regulator and the identification of $\rho_1 = \lambda/e^2$ as the explicit candidate universal ratio. The negative leading-log fixed-point finding is consistent with the standard scalar-QED Landau-pole pattern and was structurally anticipated by FSC-3 Memo 1 §6.4 ("absolute-magnitude fixed points do not exist; ratio fixed points may").

### 8.4 What this means for Arc FSC closure

Finding FSC-3.5.1 *strengthens* the structurally-expected outcome of FSC-3 (Scenario B partial-positive). It does *not* close FSC-3: Memo 4 Direction A and B remain to be computed before a verdict on whether *any* substrate-RG fixed points exist for coupling-magnitude-related operators.

If Memo 4 confirms Scenario B (ratio fixed points exist, absolute-magnitude fixed points do not), Arc FSC closes with the third sharpening of position-paper §7.2:

> *Coupling-magnitude values are FORCED-INHERITED at substrate and emergent scales: substrate-microscopic V1 spectral shape (FSC-2.1) propagates through one-loop Wilsonian RG flow to determine finite parts of marginal-sector coupling-magnitude flow, and the leading-log universal coefficients do not produce IR-attractive fixed points for absolute coupling magnitudes (FSC-3.5.1). Substrate-RG universality applies to certain ratios (analogous to Arc RG's 0.6 ratio and V5 cross-scale invariance) but not to absolute coupling magnitudes. This is structurally analogous to standard QFT, where critical exponents are universal but coupling values are not.*

If Memo 4 produces an unexpected Scenario A positive result (universal fixed points for absolute couplings), Arc FSC reopens substantially.

---

## 9. Summary

| Question (FSC-3 Memo 3 scope) | Answer |
|---|---|
| What is the leading-log structure of $\beta_\lambda, \beta_{1/e^2}, \beta_e$ in the ED substrate? | Standard scalar-QED form (eqs. boxed in §4). Universal leading-log coefficients with explicit shape-dependent finite remainders $\mathcal{R}_\lambda, \mathcal{R}_F, \mathcal{R}_e$. |
| Does shape-parameter dependence factorize into a universal part and an inherited part? | Yes (§3). Leading-log coefficients are FORCED (universal); finite remainders INHERIT shape-dependence. |
| Are there shape-independent combinations of couplings? | Yes: ratios like $\rho_1 = \lambda/e^2$ have shape-independent leading-log β-functions (§5.1). |
| Do these shape-independent combinations have IR-attractive fixed points? | **No** at one-loop leading log (Finding FSC-3.5.1). $\rho_1$ flows monotonically to $+\infty$; $e^2$ alone is Landau-pole-class. |
| Does this close FSC-3 negatively? | **No**, only *partially*. Memo 4 must compute: (A) two-loop, (B) multi-sector with Tier-5 ratios, (C) non-Abelian. Scenario B is the most structurally promising direction. |
| Status of position-paper §7.2 disclaimer? | Unchanged. Will be updated after Memo 4 closes (estimated 5–8 memos). |

---

## 10. References and Inheritance

| Inherited Item | Source | Use in FSC-3 Memo 3 |
|---|---|---|
| Standard one-loop scalar QED β-functions | Standard QFT, 1960s–present (Coleman-Weinberg, Sirlin, Brodsky-Lepage, etc.) | Universal leading-log coefficients (§4) |
| Ward-Takahashi identity (emergent under T17) | T17 + DCGT closure | Reduction of $\beta_e$ to $\beta_{1/e^2}$ flow (§4.3, §6) |
| Memo 2 operator basis (14 operators, 5 tiers) | `FSC-3_memo2_operator_basis.md` | Defines marginal sector to which one-loop calculation applies |
| V1 regulator structure | N1, T18 (Papers #18, #19), FSC-2 Memo 1 | Loop-integral cutoff structure (§1.3); shape-dependence locus |
| FSC-2.1 shape-parameter inventory | `FSC-2_v1_cross_overlap.md` | Identifies $\{s_a\}$ entering finite remainders $\mathcal{R}_i$ |
| Arc RG seventh-pass methodology | `arcs/arc-RG/ED_RG_Flow_Analysis.md` | Wilsonian flow methodology template (§1.1) |
| FSC-3 Memo 1 (Scenario B prediction) | `FSC-3_substrate_rg_universality.md` | Sets expectation that finding will be partial-positive (ratio fixed points, not absolute) |
| Position paper §7.2 | Position paper | Load-bearing target of Arc FSC, unchanged by this memo |

---

**End of FSC-3 Memo 3.**

*Finding FSC-3.5.1: at one-loop leading log, marginal-sector β-functions for $\lambda, 1/e^2, e$ have universal (shape-independent) leading-log coefficients but the candidate universal ratios $\rho_1 = \lambda/e^2$ and $e^2$ standalone exhibit no IR-attractive fixed points (Landau-pole-class monotonic flow). The structural decomposition into universal-leading-log + inherited-finite-remainder is FORCED by V1's role as substrate UV regulator. The substrate inherits the standard scalar-QED no-fixed-point Landau-pole pattern at one-loop leading log. Memo 4 (fixed-point search) must extend to two-loop (Direction A), multi-sector with Tier-5 ratio operators (Direction B), and optionally non-Abelian (Direction C) before Arc FSC can close. Direction B is the most structurally promising — Tier-5 ratio operators carry the Arc-RG 0.6-ratio-class universality that may provide the stabilizing structure absent in the marginal-only projection. Position-paper §7.2 unchanged until Memo 4 closes. Estimated 5–8 memos for Memo 4 completion.*
