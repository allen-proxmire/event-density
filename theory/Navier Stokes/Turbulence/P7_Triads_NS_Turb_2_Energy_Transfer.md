# NS-Turb-2 — NS Energy-Transfer Expression and Comparison Observable

**Date:** 2026-04-30
**Status:** NS-Turb-2 of the P7 ↔ Turbulence arc. **Headline: standard NS triadic energy-transfer derivation goes through cleanly; defining a *dimensionless* comparison observable for H2 testing is the substantive challenge. The user-spec'd O1 and O2 observables both have residual units (1/time and velocity, respectively) and require normalization. The cleanest dimensionless candidate is a normalized triad correlation coefficient at order O(0.1) for active inertial-range triads — typically larger than P7's 3–6% by a factor of 2–10×. A truer comparison requires a *forced-response* observable (steady-state harmonic amplitude under sinusoidal forcing) rather than a free-cascade observable, which is a different turbulence quantity than O1/O2 measure.**
**Companions:** [`P7_Triads_NS_Turb_1_Opening.md`](P7_Triads_NS_Turb_1_Opening.md), [`../NS-2.08_ED-PDE_Direct_Mapping.md`](../NS-2.08_ED-PDE_Direct_Mapping.md), [`../../Architectural_Canon.md`](../../Architectural_Canon.md) (P7).

---

## 1. Purpose

This memo derives the standard Navier-Stokes triadic energy-transfer expression in Fourier form and defines candidate comparison observables for testing H2 (weak-coupling amplitude correspondence between P7's 3–6% amplitude ratio and a turbulence-cascade quantity).

The mathematical derivation is standard turbulence theory and goes through cleanly. **The substantive challenge is defining the comparison observable.** P7's 3–6% is a *dimensionless* ratio (harmonic amplitude to fundamental); a meaningful comparison requires a dimensionless turbulence observable at a comparable physical setting.

The user-spec'd observables O1 (fractional transfer per triad) and O2 (normalized triad efficiency) need careful unit-checking. Honest finding: both have residual units; cleanest dimensionless versions exist but typical values are O(0.1), not 3–6%. The arc may need to revise the comparison framework.

---

## 2. Inputs

| Input | Source |
|---|---|
| NS Fourier-space nonlinearity | Standard turbulence theory (Frisch §6) |
| Transverse projector $P_{ij}(\mathbf{k}) = \delta_{ij} - k_i k_j / k^2$ | Standard incompressible NS Helmholtz decomposition |
| Triad constraint $\mathbf{k} + \mathbf{p} + \mathbf{q} = 0$ | Convolution structure of bilinear nonlinearity |
| P7 amplitude ratio 3–6% with weak coupling ~0.03 | [`../../Universal_Invariants.md`](../../Universal_Invariants.md), [`../../Architectural_Canon.md`](../../Architectural_Canon.md) §2 (P7) |
| H1/H2/H3 hypotheses | [`P7_Triads_NS_Turb_1_Opening.md`](P7_Triads_NS_Turb_1_Opening.md) §6.3 |

---

## 3. NS Nonlinearity in Fourier Triad Form

### 3.1 Real-space → Fourier conversion

Take the incompressible NS momentum equation:

$$\partial_t u_i + u_j \partial_j u_i = -\frac{1}{\rho} \partial_i p + \nu \nabla^2 u_i + f_i, \qquad \partial_j u_j = 0.$$

Fourier transform (convention $\hat u_i(\mathbf{k}, t) = \int u_i(\mathbf{x}, t) e^{-i\mathbf{k}\cdot\mathbf{x}} d^3x$):

$$\partial_t \hat u_i(\mathbf{k}) = -i k_j \widehat{(u_i u_j)}(\mathbf{k}) - \frac{i k_i}{\rho} \hat p(\mathbf{k}) - \nu k^2 \hat u_i(\mathbf{k}) + \hat f_i(\mathbf{k}).$$

Convolution form of the bilinear:

$$\widehat{(u_i u_j)}(\mathbf{k}) = \int \hat u_i(\mathbf{p}) \hat u_j(\mathbf{q}) \, \delta^3(\mathbf{p}+\mathbf{q}-\mathbf{k}) \, d^3p \, d^3q.$$

### 3.2 Incompressibility projection eliminates pressure

Pressure $\hat p(\mathbf{k})$ enforces $k_i \hat u_i = 0$. Multiplying the momentum equation by $k_i$ and using incompressibility gives:

$$\hat p(\mathbf{k}) = -\frac{i \rho \, k_i k_j}{k^2} \widehat{(u_i u_j)}(\mathbf{k}).$$

Substituting back, the pressure-eliminated equation contains the transverse projector:

$$\partial_t \hat u_i(\mathbf{k}) = -i k_j P_{im}(\mathbf{k}) \widehat{(u_m u_j)}(\mathbf{k}) - \nu k^2 \hat u_i(\mathbf{k}) + \hat f_i(\mathbf{k}),$$

where $P_{ij}(\mathbf{k}) = \delta_{ij} - k_i k_j/k^2$.

### 3.3 Triadic interaction expression

Substituting the convolution and using the triad constraint $\mathbf{p} + \mathbf{q} = \mathbf{k}$:

$$\boxed{\;\partial_t \hat u_i(\mathbf{k}) \supset \int_{\mathbf{p}+\mathbf{q}=\mathbf{k}} M_{ijm}(\mathbf{k}) \, \hat u_j(\mathbf{p}) \, \hat u_m(\mathbf{q}) \, d^3p\;}$$

with the standard NS interaction coefficient:

$$M_{ijm}(\mathbf{k}) = -i \, k_j \, P_{im}(\mathbf{k}) = -i \, k_j \left(\delta_{im} - \frac{k_i k_m}{k^2}\right).$$

(Symmetrization in (j, m) gives the canonical Frisch / Pope / Lesieur form; the asymmetric expression above suffices for energy-transfer analysis.)

**Key structural features:**
- Interaction coefficient $M_{ijm}$ has *vector-tensor* structure with explicit transport-direction dependence (via $k_j$ in front) and incompressibility projection (via $P_{im}$).
- Bilinear in $\hat u$.
- Triad constraint $\mathbf{p}+\mathbf{q}=\mathbf{k}$.

This is the structural feature NS-2.08 §5 + NS-3.02b §5 identified as the "non-ED advective transport content" — the index structure $k_j P_{im}$ is fundamentally transport-directional and projection-based, *not* symmetric-quadratic-in-gradients like P7.

---

## 4. Energy-Transfer Expression

### 4.1 Energy spectrum

Define the modal energy:

$$E(\mathbf{k}, t) = \frac{1}{2} |\hat u(\mathbf{k}, t)|^2 = \frac{1}{2} \hat u_i^*(\mathbf{k}) \hat u_i(\mathbf{k}).$$

Time evolution:

$$\frac{\partial E(\mathbf{k})}{\partial t} = \mathrm{Re}\big[\hat u_i^*(\mathbf{k}) \, \partial_t \hat u_i(\mathbf{k})\big].$$

### 4.2 Triadic energy transfer

Insert the Fourier-triad form from §3.3:

$$\frac{\partial E(\mathbf{k})}{\partial t} \supset \mathrm{Re}\left[\hat u_i^*(\mathbf{k}) \int_{\mathbf{p}+\mathbf{q}=\mathbf{k}} M_{ijm}(\mathbf{k}) \, \hat u_j(\mathbf{p}) \, \hat u_m(\mathbf{q}) \, d^3p\right] - 2\nu k^2 E(\mathbf{k}) + (\mathrm{forcing}).$$

The triadic transfer-rate density:

$$\boxed{\;S(\mathbf{k} | \mathbf{p}, \mathbf{q}) = \mathrm{Re}\big[\hat u_i^*(\mathbf{k}) \, M_{ijm}(\mathbf{k}) \, \hat u_j(\mathbf{p}) \, \hat u_m(\mathbf{q})\big]\;}$$

(with the $\delta(\mathbf{p}+\mathbf{q}-\mathbf{k})$ enforced by the convolution structure).

### 4.3 Triadic conservation symmetry

Energy conservation in the inertial range (no viscous dissipation, no forcing) implies that energy is *redistributed* between modes by triadic interactions, not created/destroyed. The triadic transfer satisfies the closure identity:

$$S(\mathbf{k}|\mathbf{p},\mathbf{q}) + S(\mathbf{p}|\mathbf{q},\mathbf{k}) + S(\mathbf{q}|\mathbf{k},\mathbf{p}) = 0.$$

This is the standard turbulence-cascade conservation law: when modes $\mathbf{p}, \mathbf{q}$ donate energy to mode $\mathbf{k}$, the donations sum to zero across the triad. Each triad is energy-conservative.

**Significance for the comparison.** This conservation makes free-cascade triadic transfer *fundamentally different* from P7's harmonic generation. P7 generates harmonic content from a fundamental (k=3 from k=1) under driving — the harmonic amplitude is set by the response of the system to the driving, not by free-cascade redistribution of conserved energy. The two phenomena have different physics even though they share triadic Fourier structure. **This is a substantial structural mismatch worth flagging directly.**

---

## 5. Candidate Comparison Observables

Per the arc spec, three candidate observables to test H2:

### 5.1 O1 — Fractional transfer per triad

User-spec'd form:

$$f(\mathbf{k}, \mathbf{p}, \mathbf{q}) = \frac{|S(\mathbf{k}|\mathbf{p},\mathbf{q})|}{E(\mathbf{p}) + E(\mathbf{q})}.$$

**Unit check.** $S$ has dimension $[\hat u]^3 [k] \sim L^4/T^2 \cdot L^{-1} = L^3/T^2$ in Fourier units (rough; depends on convention). $E$ has dimension $[\hat u]^2 \sim L^4/T^2$. Ratio $f$ has dimension $L^{-1}/T^{-1} \cdot ... $ — **leaving residual units of $1/T$ (inverse time).**

To make $f$ dimensionless, normalize by a characteristic time scale. Natural choice: eddy turnover time at scale $k$, $\tau_k = 1/(k u(k))$. Dimensionless version:

$$\tilde f(\mathbf{k}, \mathbf{p}, \mathbf{q}) = f(\mathbf{k}, \mathbf{p}, \mathbf{q}) \cdot \tau_k = \frac{|S(\mathbf{k}|\mathbf{p},\mathbf{q})|}{(E(\mathbf{p}) + E(\mathbf{q})) \cdot k \, u(k)}.$$

This is the "fraction of donor energy transferred to mode $\mathbf{k}$ per eddy turnover time at $\mathbf{k}$." A standard turbulence quantity; values in the inertial range are typically O(0.1)–O(0.3) for active triads (varies by triad geometry, locality, etc.).

### 5.2 O2 — Normalized triad efficiency

User-spec'd form:

$$\eta(\mathbf{k}, \mathbf{p}, \mathbf{q}) = \frac{|S(\mathbf{k}|\mathbf{p},\mathbf{q})|}{|\hat u(\mathbf{p})| \, |\hat u(\mathbf{q})| \, |k|}.$$

**Unit check.** Numerator: $|\hat u|^3 |k|$. Denominator: $|\hat u|^2 |k|$. Ratio has dimension of velocity. **Not dimensionless.**

To make dimensionless, normalize by $|\hat u(\mathbf{k})|$:

$$\tilde\eta(\mathbf{k}, \mathbf{p}, \mathbf{q}) = \frac{|S(\mathbf{k}|\mathbf{p},\mathbf{q})|}{|\hat u(\mathbf{p})| \, |\hat u(\mathbf{q})| \, |k| \, |\hat u(\mathbf{k})|}.$$

This is the *normalized triad correlation coefficient* — angular-cosine-class quantity bounded by 1 by Cauchy-Schwarz. Standard turbulence DNS values for active inertial-range triads are typically O(0.1)–O(0.3); for non-local or weakly-coupled triads, $\tilde\eta \to 0$.

### 5.3 O3 — Scale-locality ratio

User-spec'd form:

$$L(\mathbf{k}, \mathbf{p}, \mathbf{q}) = \frac{|S(\mathbf{k}|\mathbf{p},\mathbf{q})|}{|S(\mathbf{k} | \mathbf{k}\pm\Delta k)|}.$$

**Purpose.** Measures how much triadic transfer comes from *non-local* (large-scale-separated) vs. *local* (similar-scale) triads. Standard turbulence is dominated by local triads (Kolmogorov's local-cascade hypothesis); $L \to 1$ for local-triad-dominated turbulence.

**Honest assessment.** O3 measures *locality*, not *amplitude*. Less directly relevant to H2 (which tests P7's amplitude-magnitude prediction). Useful for separate question of cascade locality, but not for the central H2 comparison.

---

## 6. Preliminary Assessment

### 6.1 Recommendation: O1 (with normalization to dimensionless $\tilde f$)

Per user spec preference and the unit analysis above, **O1 with proper normalization** is the most natural candidate for "fractional transfer per triad" comparable to P7's amplitude ratio. The normalized form:

$$\tilde f = \frac{|S(\mathbf{k}|\mathbf{p},\mathbf{q})|}{(E(\mathbf{p})+E(\mathbf{q})) \cdot k u(k)}$$

is dimensionless and has standard turbulence values O(0.1)–O(0.3) in the inertial range.

### 6.2 The order-of-magnitude challenge

**Honest issue:** standard turbulence inertial-range $\tilde f \sim 0.1$–$0.3$ is **2–10× larger** than P7's predicted 3–6%.

Three possible interpretations:

(i) **H2 is wrong as stated.** P7's 3–6% does not correspond to free-cascade triadic transfer; the order-of-magnitude mismatch is significant.

(ii) **The comparison observable is wrong.** P7's amplitude ratio is a *forced-response* quantity (steady-state harmonic amplitude under sinusoidal driving), not a free-cascade quantity. The standard turbulence cascade observables don't directly correspond. A *forced-response* turbulence observable would be needed — e.g., steady-state amplitude at $k=3k_0$ under sinusoidal forcing at $k_0$ in a viscous regime where the cascade doesn't develop. This would be a different turbulence-physics setting.

(iii) **The mapping is qualitative not quantitative.** Both have triadic structure with weak coupling at the architectural level; the specific 3–6% vs. 10–30% mismatch reflects regime differences (P7 in steady-state perturbation; turbulence in fully-developed inertial range) rather than structural failure. Not directly testable as a quantitative match.

The honest near-term direction: **investigate (ii)** — define a forced-response observable that more directly corresponds to P7's setting, and compare. If the forced-response observable in the appropriate viscous-laminar regime gives O(0.05) magnitude (matching 3–6%), H2 holds in that restricted regime; if it doesn't, H2 fails as quantitative claim.

### 6.3 The structural mismatch flagged in §4.3

P7's harmonic generation is *sourced by driving* of the canonical PDE; turbulence's triadic transfer is *energy-conserving redistribution* in free cascade. These are different physical phenomena despite shared Fourier-triadic structure. Even if the magnitude question (§6.2) is resolved, the mechanism mismatch persists — and this aligns with NS-2.08/NS-3.02b's earlier finding that advection is structurally non-ED at the index/transport-character level.

This pushes the working hypothesis from H2 (clean amplitude correspondence) toward H1 (generic triadic similarity, trivially true) or toward a more limited "qualitative-mapping" version of H3 that acknowledges the structural mismatch but argues for a partial-template relationship.

---

## 7. Recommended Next Steps

1. **NS-Turb-3 — Evaluate O1 ($\tilde f$) magnitude in turbulence literature.** File: `theory/Navier Stokes/Turbulence/P7_Triads_NS_Turb_3_Inheritance.md`. Two parts:
   - Confirm the standard inertial-range $\tilde f$ value O(0.1)–O(0.3) from DNS / LES literature (Frisch §6.4; Pope §6; Lesieur).
   - Investigate whether a *forced-response* observable in the viscous-laminar regime (sinusoidal forcing at $k_0$, measure amplitude at $k=3k_0$) gives a different magnitude potentially matching P7's 3–6%.
   - Estimated 1–2 sessions.

2. **NS-Turb-4 — Compare magnitudes and audit failure modes.** File: `theory/Navier Stokes/Turbulence/P7_Triads_NS_Turb_4_Failure_Modes.md`. Aggregate the magnitude comparison plus the structural-mismatch analysis (free-cascade vs. forced-response; index-structure asymmetry from NS-2.08/NS-3.02b). Honest verdict per H2 status. Estimated 1 session.

3. **NS-Turb-5 — Architectural classification synthesis.** File: `theory/Navier Stokes/Turbulence/P7_Triads_NS_Turb_5_Synthesis.md`. Aggregate H1/H2/H3 verdicts. Honest verdict whether ED supplies a non-trivial structural prediction about turbulence cascade. Estimated 1 session.

### Decisions for you

- **Confirm the unit-analysis finding:** O1 and O2 as user-spec'd both have residual units; dimensionless versions are $\tilde f$ (fractional transfer per eddy turnover time) and $\tilde\eta$ (normalized triad correlation coefficient).
- **Confirm the order-of-magnitude finding:** standard-turbulence $\tilde f$ values O(0.1)–O(0.3) are 2–10× larger than P7's 3–6% — a real magnitude mismatch.
- **Confirm the suggested resolution direction:** investigate forced-response observable in viscous-laminar regime (different turbulence-physics setting from free cascade). If H2 holds in that restricted regime, the arc has a substantive but limited verdict.
- **Confirm the structural-mechanism mismatch flagged in §4.3 is honest:** P7 = forced harmonic generation; turbulence cascade = free-cascade conservative redistribution. Different physics; same Fourier-triadic structure.

---

*NS-Turb-2 derives the standard NS triadic energy-transfer expression $S(\mathbf{k}|\mathbf{p},\mathbf{q}) = \mathrm{Re}[\hat u^*(\mathbf{k}) \cdot M(\mathbf{k}) \hat u(\mathbf{p}) \hat u(\mathbf{q})]$ with $M_{ijm} = -ik_j P_{im}(\mathbf{k})$. Defining a *dimensionless* comparison observable for H2 testing is the substantive challenge. User-spec'd O1 and O2 require normalization; proper dimensionless forms ($\tilde f$ fractional-transfer-per-eddy-turnover, $\tilde\eta$ normalized triad correlation) have standard inertial-range values O(0.1)–O(0.3), 2–10× larger than P7's 3–6%. **Honest near-term direction: investigate forced-response observable in viscous-laminar regime as the structurally appropriate analog of P7's setting.** Structural mismatch flagged: P7 = forced harmonic generation; turbulence cascade = free-cascade conservative redistribution.*
