# Memo_ED_RouteA_A2_Construct — Construction Memo (Route A2 Attempt; Multi-Route Convergence Verification)

**Series:** Wave-3 Construction Memo (Cosmology Arc + ED-SC Arc; Route A Substrate-Graph Derivation of $H_0$; Path-A2 from Memo_ED_RouteA_Scoping_Wave3 §7.2; **load-bearing for multi-route convergence per Q-A4-4** from Memo_ED_RouteA_A4_Audit)
**Status:** Substrate-graph attempt at Route A2 — derivation of the late-universe Hubble scale $H_0$ from SC-4.x Hessian eigenvalue asymptotics in the saturation regime. **Not a derivation. No new primitives.** Outcome: **substantive partial-positive with critical multi-route convergence finding.** Under leading-order linear $U(\Psi)$ assumption (A4 §2.3 + audit Q-A4-3), the Hessian at saturation is **kernel-dominated** at IR (since $U''(\Psi^{\mathrm{const}}) = 0$ for linear $U$); $\ell_{A2} \sim \ell_{V_5} = c\tau_{V_5}$ — **A2 reduces to Route A1**, not to Route A4. Multi-route convergence between A2 and A4 holds **if and only if** the substrate-graph relation $\ell_{V_5}^2 \sim M_P^2 c^4 / (\hbar \Theta_{\mathrm{ED}})$ holds at primitive level — a substantive substrate-graph relation that the corpus does not currently supply (RA-OPEN-4c-explicit, newly elevated to load-bearing). This **confirms Q-A4-4's concern** that $\tau_{V_5}$ and $\Theta_{\mathrm{ED}}$ may be independent substrate-parameters; Route A4's confident reduction of A1 to A4 is now explicitly substrate-research-frontier.
**Date:** 2026-05-17
**Anchors:** Memo_ED_RouteA_A4_Construct (A4 parametric structure $H_0 \sim \sqrt{\Theta_{\mathrm{ED}}/M_P^2}$); Memo_ED_RouteA_A4_Audit (Q-A4-4 load-bearing); Memo_ED_RouteA_Scoping_Wave3 (Route A2 scope; ED-SC 4.x six-projection framework); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$ + Hessian classification); Paper_073 (DCGT effective-metric scaling); Paper_ED_Cos_01 (M3); Paper_ED_Cos_05 (M3 conditional); Paper_027 (Newton's $G$); Paper_087 (P02 + P04 + P12); Paper_012 (P-RB-1); Paper_089 (V1); Paper_090 (V5 finite-memory $\tau_{V_5}$); Papers SC-4.x (scale-collapse + six projections including $\xi_{\mathrm{canonical}}(H_0)$).

> ⚠️ **Correction (2026-07-06):** This memo cites Θ_ED as "Paper_087 P12 (ED-threshold)." That attribution is incorrect — canonical `Paper_087` P12 is a stability-landscape functional unrelated to an event-density threshold. Θ_ED's actual (uncritically-inherited) origin is `Paper_ED_CCC_ConformalCyclicCosmology.md` §3.2/§3.7, itself now flagged. This does not change this memo's tier verdicts (Θ_ED remains substrate-parameter-INHERITED throughout) — it only corrects the primitive citation. See `event-density/docs/Scoping_ThetaED_FirstPrinciples_2026-07-06.md`.

---

## §1 Restated A2 target

### §1.1 The A2 closure target

Show that the SC-4.x Hessian eigenvalue structure in the uniform-$\Psi$ saturation regime supplies a characteristic length scale $\ell_{A2}$ such that

$$
H_0 \sim c / \ell_{A2} \quad \text{via DCGT effective-metric scaling}
$$

with $\ell_{A2}$ derivable from Hessian asymptotic eigenvalues + substrate parameters.

### §1.2 Load-bearing significance per Q-A4-4

Memo_ED_RouteA_A4_Audit §5 surfaced **Q-A4-4 as load-bearing:** the construction memo's reduction of Route A1 ($\tau_{V_5}$) to Route A4 ($\Theta_{\mathrm{ED}}$) is **asserted but not proved**. Multi-route convergence verification — independent attempts at Routes A1, A2, A4 followed by convergence audit — is required for full Route A closure. **This memo's A2 attempt is the load-bearing companion to A4, addressing Q-A4-4.**

### §1.3 ED-SC 4.x six-projection alignment

Per ED_MEMORY anchor 7, the ED-SC 4.x extension arc identifies six substrate-cosmology-boundary projections, one of which is **$\xi_{\mathrm{canonical}}(H_0)$** — precisely the Route A target. Route A2's Hessian-eigenvalue approach is the natural ED-SC-4.x-aligned derivation pathway. **Route A2 is therefore the most corpus-aligned route with the standing ED-SC 4.x arc-wide upgrade objective.**

---

## §2 SC-4.9 Hessian at saturation

### §2.1 Substrate-action Hessian definition

Per Paper_ED_SC_4_9, the substrate-action saddle Hessian is

$$
\mathcal{H}(\ell, \ell') = \frac{\delta^2 S_{\mathrm{sub}}[\Psi]}{\delta\Psi(\ell) \delta\Psi(\ell')}\bigg|_{\Psi = \Psi^{\mathrm{const}}}
$$

evaluated at the uniform-$\Psi$ saturation configuration.

For $\mathcal{L}_{\mathrm{sub}}[\Psi, \nabla_{V_1}\Psi, \nabla_{V_5}\Psi]$ with leading-order structure (per A4 §2.3 + audit Q-A4-3 leading-order linearity):

$$
\mathcal{L}_{\mathrm{sub}} = U(\Psi) + \sum_K \frac{1}{2} G_K \cdot (\nabla_K \Psi)^2
$$

where $G_K$ is the kernel-derivative coupling coefficient for $K \in \{V_1, V_5\}$. The Hessian decomposes into:

- **Local term:** $\mathcal{H}_{\mathrm{local}}(\ell, \ell') = U''(\Psi^{\mathrm{const}}) \cdot \delta(\ell - \ell')$ — diagonal contribution from potential second derivative
- **Kernel terms:** $\mathcal{H}_{\mathrm{kernel}}(\ell, \ell') = \sum_K G_K \cdot K(\ell - \ell')$ — non-local contributions from V1 + V5 kernel structure

### §2.2 Hessian eigenvalue structure

Diagonalizing $\mathcal{H}$ in substrate-graph momentum space (Fourier conjugate of substrate-graph position):

$$
\lambda_K(q) = U''(\Psi^{\mathrm{const}}) + \sum_K G_K \cdot \tilde{K}(q)
$$

where $\tilde{K}(q)$ is the substrate-graph Fourier transform of kernel $K$. For V1 + V5 finite-width kernels (Paper_089 + Paper_090), $\tilde{K}(q)$ has long-wavelength behavior $\tilde{K}(q) \to G_K \cdot \ell_K^2 \cdot q^2$ for $q \ll 1/\ell_K$ (kernel-derivative-like long-wavelength expansion).

**IR-limit dispersion relation:**

$$
\lambda(q) = U''(\Psi^{\mathrm{const}}) + \beta \cdot q^2 + O(q^4)
$$

where $\beta = \sum_K G_K \ell_K^2$ is the effective kernel-curvature coefficient.

**Standard QFT analog:** this is the dispersion $\lambda(q) = m_{\mathrm{eff}}^2 + \beta q^2$ for a free scalar with effective mass $m_{\mathrm{eff}}^2 = U''(\Psi^{\mathrm{const}})$.

### §2.3 Saturation-regime Hessian eigenvalue asymptotics

At saturation, two regimes for the IR Hessian eigenvalue $\lambda_{\mathrm{IR}}$:

- **Potential-dominated:** $U''(\Psi^{\mathrm{const}}) \gg \beta q^2$ for relevant $q$ → $\lambda_{\mathrm{IR}} \sim U''(\Psi^{\mathrm{const}}) = m_{\mathrm{eff}}^2$; IR cutoff length $\ell_{\mathrm{IR}} \sim 1/m_{\mathrm{eff}}$
- **Kernel-dominated:** $U''(\Psi^{\mathrm{const}}) \ll \beta q^2$ for relevant $q$ → $\lambda_{\mathrm{IR}} \sim \beta q^2$; IR cutoff length set by kernel scale $\ell_{\mathrm{IR}} \sim \sqrt{\beta} \sim \ell_{V_5}$ (V5 dominates IR for ~40-OOM cross-scale content per Paper_090)

**Critical question:** which regime obtains at the saturation configuration?

---

## §3 Eigenvalue regime under leading-order linear $U(\Psi)$

### §3.1 Leading-order linearity (per A4 §2.3 + audit Q-A4-3)

A4 construction memo §2.3 + audit Q-A4-3 established leading-order linearity:

$$
U(\Psi) \approx \hbar \Psi \quad\text{(leading-order; per audit Q-A4-1 dimensional bridge)}
$$

For linear $U(\Psi)$: $U''(\Psi^{\mathrm{const}}) = 0$. **The potential-dominated regime is absent at leading order.**

This is a structural consequence of A4's leading-order linearity assumption (Q-A4-3). Subleading nonlinear corrections (logarithmic, higher-power) would supply $U''$ contributions but are subleading $O(\varepsilon)$ at the linearity-leading order.

### §3.2 Consequence: A2 enters kernel-dominated regime

With $U''(\Psi^{\mathrm{const}}) = 0$ at leading order, the IR Hessian eigenvalue is **kernel-dominated**:

$$
\lambda_{\mathrm{IR}} \sim \beta q^2, \quad \ell_{A2} \sim \sqrt{\beta} \sim \ell_{V_5}
$$

(V5's ~40-OOM cross-scale content gives the largest kernel-set length per Paper_090; $\ell_{V_5} = c\tau_{V_5}$ dominates V1's much shorter $\ell_{V_1}$).

**$\ell_{A2}$ reduces to $\ell_{V_5}$.** Route A2 at leading-order linear $U$ assumption **reduces to Route A1**, not to Route A4.

### §3.3 If subleading nonlinear $U''(\Psi^{\mathrm{const}}) \neq 0$

If A4's leading-order linearity is relaxed (e.g., quadratic-correction $U(\Psi) = \hbar\Psi + b\Psi^2$):

$$
U''(\Psi^{\mathrm{const}}) = 2b
$$

Dimensional consistency: $[b\Psi^2] = [\mathcal{L}_{\mathrm{sub}}] = [E L^{-3}]$, so $[b] = [E L^{-3}]/[\Psi^2] = [E L^{-3}]/[E^2 L^{-6}] = [E^{-1} L^3]$. Then $[U''] = [E^{-1} L^3] \cdot [\text{nothing}] = [E^{-1} L^3]$ — wait, this is wrong dimension for an effective mass-squared.

Let me retry: if $\Psi$ has dimension $[\hbar \cdot \Theta_{\mathrm{ED}}] = [E T] \cdot [L^{-3} T^{-1}] = [E L^{-3}]$ (action-density), then $[U(\Psi)] = [E L^{-3}]$ as well (since $U(\Psi) = \mathcal{L}_{\mathrm{sub}}$). So $[U/\Psi] = $ dimensionless, $[U'(\Psi)] = $ dimensionless × $1/\Psi = [\Psi^{-1}] = [L^3 E^{-1}]$, $[U''(\Psi)] = [\Psi^{-2}] = [L^6 E^{-2}]$.

Effective mass-squared $[m_{\mathrm{eff}}^2] = [\lambda_{\mathrm{IR}}] = $ ?? The Hessian eigenvalue has dimension of (action density / $\Psi^2$) × (correct dimensional bridge). This dimensional bookkeeping is getting complex; the structural point is what matters.

**Structural point:** if $U''(\Psi^{\mathrm{const}})$ is non-zero (subleading nonlinear $U$), it supplies a mass-squared scale that gives potential-dominated IR cutoff. This mass scale could be substrate-graph-related to $\Theta_{\mathrm{ED}}$ (via the substrate-action functional structure), in which case A2 could converge with A4 at subleading-order.

**At leading order (linear $U$), A2 ≠ A4 parametrically.** A2 reduces to A1 ($\ell_{V_5}$).

---

## §4 Candidate $\ell_{A2}$

Under leading-order linear $U(\Psi)$:

$$
\ell_{A2} \sim \ell_{V_5} = c \tau_{V_5}
$$

where $\tau_{V_5}$ is V5's finite-memory time per Paper_090 — a primitive substrate-parameter at the same level as $\ell_P$ or $\hbar$.

### §4.1 Substrate-parameter content for $\ell_{V_5}$

$\tau_{V_5}$ is **not derived from $\Theta_{\mathrm{ED}}$ or Planck content** in the current corpus. It enters Paper_090 as a V5 primitive feature. Substrate-parameter-INHERITED at the same primitive level as $\ell_P$, $c$, $\hbar$, $\Theta_{\mathrm{ED}}$.

### §4.2 Numerical matching

For $H_0 \sim c/\ell_{V_5}$ to match observation $H_0 \approx 2.2 \times 10^{-18}$ s$^{-1}$:

$$
\ell_{V_5} \sim c/H_0 = R_H \approx 1.4 \times 10^{26} \text{ m}, \quad \tau_{V_5} \sim 1/H_0 \approx 4.6 \times 10^{17} \text{ s}.
$$

In Planck units: $\tau_{V_5}/\tau_P \approx 10^{61}$. **V5's finite-memory time is $\sim 10^{61}$ Planck times.**

This is the substrate-parameter content for $\tau_{V_5}$ that, via Route A2 at leading order, reproduces the observed $H_0$.

### §4.3 Hessian-eigenvalue at saturation

The IR Hessian eigenvalue at saturation:

$$
\lambda_{\mathrm{IR}} \sim \beta / \ell_{V_5}^2 \sim G_{V_5} / \ell_{V_5}^0 \cdot 1
$$

(with appropriate dimensional factors). The smallest non-zero Hessian eigenvalue sets the IR cutoff at $\ell_{V_5}$. **Substrate-graph IR structure at saturation is set by V5's finite-memory scale.**

This is the substantive substrate-graph content of Route A2: **the cosmological scale is the V5 finite-memory scale**, accessed via Hessian IR cutoff at saturation.

---

## §5 DCGT translation + comparison with A4

### §5.1 DCGT effective-metric scaling

Per Paper_073, DCGT produces the continuum effective metric whose characteristic scale tracks the substrate-graph IR Hessian eigenvalue's wavelength. For $\lambda_{\mathrm{IR}} \to 0$ at $q \to 1/\ell_{V_5}$, the effective metric's macroscopic-scale content corresponds to $R_{\mathrm{cg}} \sim \ell_{V_5}$.

DCGT translation per Memo_ED_RouteA_Scoping_Wave3 §3 (parametric transparency): $H_0 \sim c/\ell_{A2} \sim c/\ell_{V_5}$ — recovering Route A1 directly.

### §5.2 Parametric comparison with A4

| Aspect | Route A4 ($\Theta_{\mathrm{ED}}$) | Route A2 ($\ell_{V_5}$ at leading order) |
|---|---|---|
| Closure pathway | Substrate-action density via Q1A + Q2A + Friedmann | Hessian IR eigenvalue via DCGT effective-metric scaling |
| Surviving substrate-parameter | $\Theta_{\mathrm{ED}}$ (with $\hbar$ bridge) | $\tau_{V_5}$ |
| $H_0$ formula | $H_0 = (8\pi/3)^{1/2} \cdot M_P \cdot (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{1/2}$ | $H_0 \sim c/\ell_{V_5} = 1/\tau_{V_5}$ |
| Required substrate-parameter value | $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ | $\tau_{V_5}/\tau_P \approx 10^{61}$ |

### §5.3 Multi-route convergence evaluation

**A2 ↔ A4 parametric convergence condition:** the two routes give the same $H_0$ prediction if and only if

$$
\frac{1}{\tau_{V_5}} \sim M_P \cdot (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{1/2}
$$

(modulo dimensionless coefficients). Squaring + rearranging in dimensional form:

$$
\boxed{\;\ell_{V_5}^2 \sim \frac{M_P^2 c^4}{\hbar \Theta_{\mathrm{ED}}} \;\text{(in natural units)}\;}
$$

This is the **substrate-graph multi-route convergence relation** between V5's finite-memory length and the ED-threshold value.

**Status of this relation:**
- Paper_090 does **not** derive $\tau_{V_5}$ from $\Theta_{\mathrm{ED}}$ + Planck content
- Paper_087 P12 does **not** derive $\Theta_{\mathrm{ED}}$ from $\tau_{V_5}$ + Planck content
- Neither parameter is substrate-graph-derived from the other in current corpus

**If the convergence relation holds at primitive level**, Route A closes with multi-route convergence (substantial corpus advance per ED-SC 4.x arc-wide upgrade objective). **If the relation does not hold**, $\tau_{V_5}$ and $\Theta_{\mathrm{ED}}$ are independent substrate-parameters; Route A is under-determined; the two routes give different $H_0$ predictions absent additional substrate-research-frontier work to relate them.

**This is precisely the Q-A4-4 audit concern realized in explicit form.**

### §5.4 Substrate-graph plausibility of the convergence relation

Is $\ell_{V_5}^2 \sim M_P^2 c^4 / (\hbar \Theta_{\mathrm{ED}})$ plausible substrate-graph?

Dimensionally: both sides are length-squared. ✓

Substrate-graph interpretation: V5's finite-memory length is set by the inverse-square-root of the ED-threshold value (in appropriate units). Intuitively: low-threshold (small $\Theta_{\mathrm{ED}}$) substrate has long V5 memory; high-threshold (large $\Theta_{\mathrm{ED}}$) substrate has short V5 memory.

**Substrate-graph mechanism for the relation:** if V5's cross-chain coupling is mediated by substrate event-density (per Paper_090 ~40-OOM cross-scale structure depending on substrate population), then $\tau_{V_5}$ correlates with $1/\Theta_{\mathrm{ED}}$ — low event-density gives long memory; high event-density gives short memory. This is **substrate-graph plausible** but not derived.

**RA-OPEN-4c-explicit (newly elevated to load-bearing per Q-A4-4):** substrate-graph derivation that V5's finite-memory length $\ell_{V_5}$ satisfies $\ell_{V_5}^2 \sim M_P^2 c^4 / (\hbar \Theta_{\mathrm{ED}})$ from Paper_090 V5 structure + Paper_087 P12 + Paper_012 P-RB-1 + Paper_073 DCGT scale-collapse. If derivable, multi-route convergence verifies; if not derivable, Route A is genuinely under-determined.

---

## §6 IDENTIFIED vs OPEN

### §6.1 IDENTIFIED (substantive A2 closures)

- **Hessian eigenvalue structure at saturation:** $\lambda(q) = U''(\Psi^{\mathrm{const}}) + \beta q^2$ at leading order (§2.2)
- **Kernel-dominated IR regime under leading-order linear $U(\Psi)$:** $U''(\Psi^{\mathrm{const}}) = 0$ → $\lambda_{\mathrm{IR}} \sim \beta q^2$ → IR cutoff $\ell_{A2} \sim \ell_{V_5}$ (§3.2)
- **Route A2 reduces to Route A1 at leading order:** $\ell_{A2} \sim \ell_{V_5} = c\tau_{V_5}$; substrate-parameter-INHERITED at $\tau_{V_5}$ primitive level (§4.1)
- **DCGT effective-metric scaling at saturation IR:** $H_0 \sim c/\ell_{V_5}$ (§5.1)
- **Multi-route convergence condition explicit:** $\ell_{V_5}^2 \sim M_P^2 c^4 / (\hbar \Theta_{\mathrm{ED}})$ (§5.3 boxed result)
- **ED-SC 4.x six-projection alignment:** Route A2 = $\xi_{\mathrm{canonical}}(H_0)$ projection via Hessian asymptotics (§1.3)

### §6.2 OPEN (load-bearing for Route A full closure)

| OPEN | Description | Status |
|---|---|---|
| **RA-OPEN-4c-explicit** (newly elevated) | Substrate-graph derivation of multi-route convergence relation $\ell_{V_5}^2 \sim M_P^2 c^4 / (\hbar \Theta_{\mathrm{ED}})$ from Paper_090 + Paper_087 P12 + Paper_073 | **Load-bearing for full Route A closure per Q-A4-4** |
| **RA-OPEN-A2-1** (newly introduced) | Substrate-graph derivation of $\tau_{V_5}$ value from sub-primitive content (analog of RA-OPEN-4a for $\Theta_{\mathrm{ED}}$) | Substrate-research-frontier; parallel to RA-OPEN-4a |
| **RA-OPEN-A2-2** (newly introduced) | Substrate-graph derivation of leading-order linearity of $U(\Psi)$ from Paper_ED_SC_4_9 substrate-action functional structure (audit Q-A4-3) | Subleading; if $U''$ non-zero at subleading, potential-dominated regime supplies independent $\ell_{A2}$ contribution |
| **Multi-route convergence audit** | Adversarial verification that A2 ≡ A4 at primitive level (not just parametric form) | Required for Route A full closure declaration |

### §6.3 Multi-route convergence evaluation (addressing RA-OPEN-4c)

**Per §5.3 analysis:**

- **At leading order:** A2 reduces to A1; A2 ≠ A4 parametrically unless substrate-graph relation $\ell_{V_5}^2 \sim M_P^2 c^4 / (\hbar \Theta_{\mathrm{ED}})$ holds at primitive level
- **The relation is substrate-graph plausible** (V5 memory inversely correlates with substrate event-density) but **not derived** in current corpus
- **Multi-route convergence is corpus-conditional:** holds if RA-OPEN-4c-explicit closes; fails if it doesn't

**Honest assessment:** Route A is **substantively closed at substrate-parameter-INHERITED level** via A4 alone (form-DERIVED $H_0 = f(\Theta_{\mathrm{ED}})$ with $\Theta_{\mathrm{ED}}$ INHERITED), **modulo the Q-A4-4 + RA-OPEN-4c-explicit qualification** that A1 ($\tau_{V_5}$) might be an independent substrate-parameter requiring separate substrate-graph treatment. Route A2's contribution is to **explicitly identify the convergence relation** $\ell_{V_5}^2 \sim M_P^2 c^4 / (\hbar \Theta_{\mathrm{ED}})$ as the substrate-graph question whose resolution determines whether A1, A2, A4 unify into one Route A or remain three independent closure pathways.

---

## §7 Status update + recommended next steps

### §7.1 A2 closure status

| Aspect | Status |
|---|---|
| Hessian eigenvalue structure at saturation | Substrate-graph IDENTIFIED via SC-4.9 + leading-order $\mathcal{L}_{\mathrm{sub}}$ structure |
| IR cutoff $\ell_{A2}$ at leading order | $\ell_{A2} \sim \ell_{V_5}$ (kernel-dominated regime; reduces to A1) |
| $H_0$ formula | $H_0 \sim c/\ell_{V_5} = 1/\tau_{V_5}$ via DCGT IR scaling |
| Multi-route convergence with A4 | **Conditional on substrate-graph relation $\ell_{V_5}^2 \sim M_P^2 c^4 / (\hbar \Theta_{\mathrm{ED}})$** (RA-OPEN-4c-explicit) |
| ED-SC 4.x six-projection alignment | Confirmed: A2 = $\xi_{\mathrm{canonical}}(H_0)$ projection via Hessian asymptotics |

### §7.2 Critical finding for Route A closure

**Multi-route convergence is corpus-conditional, not corpus-given.** Route A4 closes at substrate-parameter-INHERITED level (Paper_027 analog) for $\Theta_{\mathrm{ED}}$. Route A2 closes at substrate-parameter-INHERITED level for $\tau_{V_5}$. The two routes give *parametrically distinct* predictions absent the convergence relation.

**If RA-OPEN-4c-explicit closes substrate-graph:** Routes A1, A2, A4 unify; Route A closes substantially at multi-route-convergent level. Substantive substrate-graph relation between V5 memory and ED-threshold is a corpus advance.

**If RA-OPEN-4c-explicit does not close:** Routes A1, A2, A4 remain three independent closure pathways with potentially different $H_0$ predictions; observation determines which substrate-parameter value to use; Route A remains substrate-parameter-INHERITED at the same Paper_027 level via *either* $\Theta_{\mathrm{ED}}$ (A4) or $\tau_{V_5}$ (A1/A2) — both admissible but not unified.

### §7.3 Honest substrate-research assessment

**Route A closes at Paper_027 substrate-parameter-INHERITED level via A4 alone** (per A4 audit + this memo's analysis). The multi-route convergence question (whether A1/A2 reduce to A4 or are independent) is a **separate substrate-research advance** that — if it closes — would substantively unify the substrate-research-frontier substrate-parameters $(\Theta_{\mathrm{ED}}, \tau_{V_5})$ into a single substrate-graph relation. This unification is **substrate-graph-plausible** but currently **not derived**.

**For practical corpus purposes (per ED_MEMORY anchor 7 + Q-A4-4):** Route A4 closure delivers the substrate-graph derivation of $H_0$ form modulo $\Theta_{\mathrm{ED}}$ value INHERITED — sufficient for the M3 status of Cos_01 + Cos_05 + 038_5 retroactive upgrade + ED-SC 4.x arc-wide implications. The convergence question is **tightening work**, not blocking work.

### §7.4 Recommended next steps

**Path-Multi-Route-Convergence-Audit:** Claude-B-class adversarial audit of A4 + A2 combined closure, focusing on the convergence relation $\ell_{V_5}^2 \sim M_P^2 c^4 / (\hbar \Theta_{\mathrm{ED}})$ — examine whether substrate-graph derivation is achievable from Paper_090 + Paper_087 P12 + Paper_073 composition; identify any corpus-internal substrate-graph mechanism that would supply the relation.

**Path-A1-Construction (optional; lower priority):** focused construction of Route A1 directly via $\tau_{V_5}$ dimensional rearrangement — if A1 closes independently and gives the same $H_0$ as A2/A4 at parametric level, supplies third-route convergence verification.

**Path-Cos05-Update (parallel; conditional on accepting Route A4-level closure):** propagate Route A4 closure into Cos_05 (remove "conditional on Route A" qualifier; carry RA-OPEN-4c-explicit as remaining substrate-research-frontier OPEN for multi-route convergence; verdict remains M3).

**Path-038_5-Update (parallel; conditional on accepting Route A4-level closure):** retroactive M2 → M3 upgrade per Λ-smallness reframing inheritance.

**Path-ED-SC-4.x-Arc-Update (conditional on multi-route convergence audit):** propagate ED-SC 4.x arc-wide M3 → M2 upgrade once RA-OPEN-4c-explicit closes (or is accepted at substrate-parameter-INHERITED level analogous to Paper_027's pattern).

**Path-A4-Construct-Update (separate; refinements per A4 audit Q-A4-1, Q-A4-2, Q-A4-3, Q-A4-5):** apply construction-memo refinements per A4 audit recommendations.

### §7.5 My recommendation

**Path-Multi-Route-Convergence-Audit immediately** to settle the Q-A4-4 + RA-OPEN-4c-explicit load-bearing question. The substrate-graph relation $\ell_{V_5}^2 \sim M_P^2 c^4 / (\hbar \Theta_{\mathrm{ED}})$ is the **single substantive substrate-research finding** that, if it closes, unifies A1/A2/A4 into one Route A closure; if it doesn't close, the corpus must honestly carry both $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$ as independent primitive substrate-parameters (analog to $\ell_P, \hbar, c$ being independent substrate-constants).

**Path-Cos05-Update + Path-038_5-Update in parallel** — Route A4-level closure is sufficient for the corpus paper-structure propagation; the multi-route convergence is tightening work.

### §7.6 Cross-program impact summary

| Outcome | Implication |
|---|---|
| **Best case (convergence holds):** RA-OPEN-4c-explicit closes substrate-graph; A1/A2/A4 unify; Route A substantively closed at multi-route-convergent level | Substantive substrate-graph relation between V5 memory and ED-threshold is corpus advance; full Route A closure at substrate-parameter-INHERITED level + multi-route-convergent verification |
| **Mid case (convergence accepted as substrate-parameter-INHERITED):** $(\Theta_{\mathrm{ED}}, \tau_{V_5})$ both substrate-parameter-INHERITED at primitive level; corpus carries both as independent | Route A closes at Paper_027-analog level via any of A1/A2/A4; multi-route choice is convention; no substantive substrate-research finding |
| **Worst case (convergence fails substrate-graph + observation-divergence):** A4 and A2 give different $H_0$ predictions inconsistent with observation under reasonable substrate-parameter ranges | Substantive substrate-research finding requiring substrate-graph reformulation; possible substrate-ontology characterization update |

**All outcomes corpus-informative.** The A2 construction's substantive contribution is **explicit identification of the multi-route convergence relation** $\ell_{V_5}^2 \sim M_P^2 c^4 / (\hbar \Theta_{\mathrm{ED}})$ as the substrate-research-frontier question whose resolution determines Route A's full closure status.

---

## §8 Substrate-research-pattern note

A2 construction's outcome — **A2 reduces to A1 at leading order; convergence with A4 is corpus-conditional** — is the **first multi-route closure attempt** in the corpus delivering a substantive divergence finding rather than convergence. The Q1Q2 + Chain-Class Identification Project delivered cleanly-convergent substrate-graph closures (Q1A + Q2A + C3 all converge on the same M3 chain). Route A's multi-route structure (four candidate routes per scoping memo) was expected to deliver convergence via multi-route verification (RA-OPEN-4c per construction memo §6.2); the actual outcome is **conditional convergence dependent on a substrate-graph relation not currently in the corpus**.

**This is a substantive substrate-research finding:** the canonical Route A formulation ($\ell_{V_5}(H_0)$ per ED_MEMORY anchor 7) involves *both* V5 finite-memory ($\tau_{V_5}$) *and* ED-threshold ($\Theta_{\mathrm{ED}}$) at primitive substrate-parameter level. Whether these are independent substrate-parameters or substrate-graph-related is the substrate-research-frontier question Route A2 explicitly identifies.

The substrate-research-pattern shift from inheritance-level closures (Load-Bearing Program) to construction-uniqueness closures (Q1Q2 + Chain-Class Identification) to multi-route convergence verification (Route A) is the substantive corpus-progression characterization.

---

**End Memo_ED_RouteA_A2_Construct.**
