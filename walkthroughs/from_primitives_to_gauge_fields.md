# From Primitives to Gauge Fields

## A Walkthrough of the Event Density Derivation (Theorem 17)

**Allen Proxmire** · May 2026

---

## 1. The Question

In 1954, Chen Ning Yang and Robert Mills extended the trick that had worked for electromagnetism — local phase invariance, plus a vector field that absorbs the phase derivative — to non-Abelian groups. The result was the structure that, after two decades of further development, became the Standard Model: a single mathematical recipe that, when applied to $U(1)$, gives electromagnetism; applied to $SU(2)$, gives the weak interaction; applied to $SU(3)$, gives the strong interaction. Every interaction in the Standard Model is a gauge interaction. Every gauge interaction is forced by the same structural argument: demand that a local symmetry hold, and a vector field — the gauge field — must appear with a specific transformation law to make it hold.

Standard physics tells the story this way: the requirement of local gauge invariance is the *principle* that produces the gauge fields. The physicist *demands* that the symmetry be local, and the mathematics produces $A_\mu$ to compensate. This is presented as a deep insight — the *gauge principle* — and it is not wrong. The mathematics works perfectly; the predictions are extraordinarily accurate; the Standard Model has stood for fifty years.

But the gauge principle is a postulate. Why must local symmetry hold? Standard physics has no answer. The deeper question — *why are interactions gauge interactions?* — is treated as not-the-physicist's-problem. The mathematics is what it is.

The Event Density framework provides an answer. The substrate's rule-type primitive — the structural feature that distinguishes one chain's update rule from another's — is what gauge fields *are*, after coarse-graining. The physical content is this: rule-type relabeling is a substrate symmetry, locality requires that the relabeling can be done independently at every point, and demanding that this *substrate-level* symmetry survive the substrate-to-continuum coarse-graining forces the appearance of a connection field that carries the relabeling information across spacetime. That connection field is the gauge field. Minimal coupling is forced by what the connection has to be in order to make local rule-type relabeling a continuum symmetry.

This is the content of Theorem 17 (T17), the structural-foundation result that closed the framework's gauge arc in 2026. The Klein-Gordon and Dirac walkthroughs invoke local $U(1)$ gauge invariance as "a structural commitment at the participation-phase level" without explaining where the commitment comes from. T17 explains where the commitment comes from. It also extends the structure to the non-Abelian case, where the gauge group is no longer the abelian $U(1)$ of electromagnetism but a non-commutative group like $SU(2)$ or $SU(3)$, and the gauge field becomes a Lie-algebra-valued connection.

The honest framing is that T17 is upstream-grounding for an argument standard physics already runs. The mathematics of fiber bundles, connections, and minimal coupling is unchanged. What changes is that the argument now starts from substrate primitives — rule-type as a primitive, locality as a primitive — rather than from the postulated gauge principle. The gauge field is no longer a piece of structure introduced to make a postulated symmetry work; it is what the substrate's rule-type infrastructure looks like in the continuum limit.

The chain has six structural moves:

1. The substrate has a primitive *rule-type* assignment to each chain. Different rule-types are physically distinct kinds of participation, but rule-type *labels* are not — relabeling rule-types preserves the substrate's physical content.

2. Globally, rule-type relabeling forms a symmetry group $G$. For the case of a single complex phase carried by the participation measure (the QM-emergence sector), $G$ is the abelian group $U(1)$. For richer rule-type structures, $G$ is a non-Abelian compact Lie group such as $SU(2)$ or $SU(3)$.

3. Locality — the substrate primitive that participation contributions live at chain steps and combine via local interactions — requires that rule-type relabeling at one substrate region cannot reach into a distant region. Relabelings must be performable independently at every point.

4. Demanding that local rule-type relabeling remain a substrate symmetry forces the appearance of a *connection*: a substrate object that carries the rule-type relabeling information from point to point. Without it, local relabelings would change the substrate's physical content. With it, they don't.

5. The connection's transformation law under local relabeling is forced by the requirement that the rule-type symmetry close. The minimal first-order modification of the substrate dynamics — replacing $\partial_\mu$ by $D_\mu= \partial_\mu + iqA_\mu/\hbar$ for $U(1)$, or $D_\mu= \partial_\mu + igA_\mu^a T^a$ for non-Abelian $G$ — is forced.

6. The connection itself acquires dynamics through its field strength $F_{\mu\nu}$, with the Yang-Mills action $\mathcal{L} = -\frac{1}{4}F_{\mu\nu}^a F^{a\,\mu\nu}$ as the unique gauge-invariant kinetic term that's local, Lorentz-invariant, and quadratic in derivatives.

The structural payoff: gauge fields are not extra ontological furniture introduced to make a postulate work. They are the continuum-level appearance of the substrate's rule-type connection. Minimal coupling is what the dynamics of a chain looks like when its rule-type can be relabeled locally without changing physics. Yang-Mills theory is what falls out when the rule-type symmetry is non-Abelian.

---

## 2. The Substrate Ontology and the Rule-Type Primitive

The framework rests on substrate-level ontological commitments. The gauge-fields walkthrough uses the working subset that Born, Schrödinger, and Klein-Gordon used, plus one additional primitive that load-bears uniquely here.

**Micro-events.** Discrete acts of becoming, vertices in a graph spanning the event manifold.

**Participation.** The relation connecting micro-events. Participation is homogeneous — no vertex is privileged at the primitive level.

**Channels.** Stable subgraphs along which a chain can repeatedly instantiate its update rule.

**Bandwidth.** The graded measure of participation, with a four-band orthogonal decomposition.

**Polarity / U(1) phase.** The $U(1)$-valued phase relation between a chain's update rule and the local ED-flow direction.

**ED gradient.** The participation graph carries a continuous spatial axis with no preferred origin.

**Locality.** Participation contributions at one substrate region combine with those at another only via the substrate's mediating structure (chains, V1 kernel, channels). There is no instantaneous non-local action.

**Rule-type (Primitive 07).** Each chain carries a primitive label — its *rule-type* — that classifies the structural form of its update rule. Different rule-types correspond to physically distinct kinds of participation; rule-types do not mix arbitrarily. The rule-type taxonomy distinguishes (at minimum) bosonic from fermionic chains via the exchange-symmetry case distinction (η = +1 bosonic, η = −1 fermionic), and admits richer substructure for chains with internal substrate degrees of freedom.

Rule-type is the load-bearing primitive for T17. The other primitives produce the QM postulates and the relativistic extensions; rule-type is what produces gauge fields. A chain's rule-type is what *it does* at the substrate level — the structural form of its update rule. Two chains carrying the same rule-type interact in identical ways; chains carrying different rule-types interact differently.

Three forced theorems from prior walkthroughs load-bear here:

**T14 (Participation measure form).** $P_K = \sqrt{b_K} \, e^{i\pi_K}$ with the square root forced by the Cauchy functional equation on bandwidth additivity and the complex phase forced by Frobenius's theorem on real division algebras.

**U2 (Inner product on the participation-measure space).** Sesquilinear, complex, with the Hilbert-space structure forced by primitive-level aggregation arguments.

**Lorentz covariance** of the participation measure on Minkowski spacetime, established in the Klein-Gordon and Dirac walkthroughs as the relativistic extension of U2's single-frame inner product.

That's the structural setup. The gauge-fields argument runs on this.

---

## 3. Global Rule-Type Symmetry: The Phase Group $U(1)$ Forced

The first structural step is to recognize that rule-type *labels* are not physical. Two physicists studying the same chain may agree on its rule-type (its structural update form) while disagreeing on what label they attach to it. The substrate's physical content is invariant under relabeling.

### 3.1 Relabeling as a substrate symmetry

For a chain with a single complex-phased rule-type, the rule-type label can be summarized by the phase $\pi_K$ of the participation measure $P_K = \sqrt{b_K}\, e^{i\pi_K}$. Two labelings differing by a constant phase shift $\alpha/\hbar$:

$$
\pi_K \to \pi_K + \alpha /\hbar
$$

correspond to the same physical chain. The participation measure becomes:

$$
P_K \to e^{i\alpha /\hbar} P_K
$$

But the participation measure's physical content lives in *bandwidth* (the $\sqrt{b_K}$ factor) and *relative* phases between channels (through the inner product), not in the overall phase. An overall constant phase shift is unphysical.

This is the **global $U(1)$ symmetry** of the participation measure. It is not a postulate. It is the substrate-level statement that rule-type *labels* differ from rule-type *content*: the label is a coordinate the physicist chooses; the content is what the substrate provides.

### 3.2 Why $U(1)$ specifically

The relabeling group is $U(1)$ for the QM-emergence sector because Frobenius's theorem (used in T14) selects $\mathbb{C}$ as the division algebra of substrate phases, and the phase coordinate lives in $\mathbb{R}/2\pi\mathbb{Z} \cong U(1)$.

For richer rule-type structures — chains carrying multiple substrate degrees of freedom that mix under relabeling — the relabeling group is larger. A rule-type carrying a doublet of substrate phases relabels under $SU(2)$ (the unique simply-connected compact group acting on a complex doublet preserving inner product and orientation). A rule-type carrying a triplet relabels under $SU(3)$. The general rule-type relabeling group is some compact Lie group $G$ whose specific identity is determined by the rule-type taxonomy's substructure at the substrate level. *Which* compact Lie group corresponds to *which* sector of nature is empirical input — the rule-type taxonomy of our universe is what it is, and the framework does not (currently) derive it from deeper substrate primitives.

For this section, focus on the $U(1)$ case. The non-Abelian extension is structurally identical and is treated in §7.

### 3.3 The free equation respects global $U(1)$

The free Klein-Gordon equation $(\square + m^2c^2/\hbar^2)\Psi= 0$ is invariant under a constant global phase shift: derivatives commute with multiplication by a constant phase factor. The free Dirac equation has the same property. Any free dynamics of the participation measure that respects $U(1)$ as a substrate symmetry will be invariant under constant global phase shifts.

Globally, then, $U(1)$ is a substrate symmetry of the free dynamics. This is the part standard physics already accepts. T17's content is in what happens when the symmetry is required to hold *locally*.

---

## 4. Why Local Invariance Is Forced — Locality Plus Rule-Type Symmetry

Standard physics often presents the move from global to local gauge invariance as a *demand*: "let us require that the symmetry hold locally." T17's content is that this demand is not optional. It is forced by the conjunction of two substrate primitives — the rule-type primitive (which makes the symmetry physically meaningful at the substrate level) and the locality primitive (which prohibits global, all-at-once symmetry transformations from being substrate-physically realizable).

### 4.1 The argument

Globally, rule-type relabeling means: at every spacetime point, shift the phase by the same constant $\alpha/\hbar$. But "the same constant at every spacetime point" is a *non-local* prescription. It requires coordinating the labelings at causally separated regions. The substrate has no mechanism for such coordination — by the locality primitive, substrate processes happen at chain steps and combine through the V1 kernel's forward-cone-only correlations. There is no substrate-level "global label-setter" that imposes the same $\alpha$ everywhere.

A *physically realizable* rule-type relabeling is therefore inherently local: at substrate region 1, choose $\alpha_1$; at substrate region 2, choose $\alpha_2$; these choices need not agree because the substrate has no mechanism to enforce agreement across causally disjoint regions. In the continuum limit, this becomes:

$$
\alpha(x^\mu): a function of spacetime, locally arbitrary
$$

The relabeling group, at the substrate level, is therefore not the global $U(1)$ — it is the *local* $U(1)$, with one independent phase choice at every spacetime point.

### 4.2 The naïve dynamics fails

If the participation measure $\Psi(x^\mu)$ is dynamically governed by an equation containing $\partial_\mu \Psi$, then under a local relabeling

$$
\Psi(x^\mu) \to e^{i\alpha(x^\mu}/\hbar) \Psi(x^\mu)
$$

the derivative transforms as

$$
\partial_\mu \Psi \to e^{i\alpha /\hbar} [\partial_\mu \Psi + (i/\hbar)(\partial_\mu \alpha) \Psi]
$$

The $(\partial_\mu \alpha)$ term is unwanted. It says that local relabeling — which is supposed to be unphysical, since rule-type *labels* are unphysical — *changes the dynamical equation*. That is a contradiction: a substrate-physically-meaningless relabeling cannot have substrate-physical consequences.

The resolution is one of three:

- **Option A.** Restrict the relabeling group to global $U(1)$ only, asserting that local relabeling is somehow disallowed. This contradicts the locality primitive (no mechanism for global coordination exists).
- **Option B.** Remove the derivative from the equation. This produces a non-dynamical theory and contradicts the empirical fact that participation measures evolve.
- **Option C.** Modify the equation to absorb the unwanted $(\partial_\mu \alpha)$ term by introducing a substrate object that transforms in a complementary way.

Option C is the only consistent path. The substrate object that absorbs $(\partial_\mu \alpha)$ is the gauge field.

### 4.3 The gauge principle is not a postulate — it is forced

What standard physics calls the *gauge principle* — "demand local invariance" — is, in the framework, the conclusion of an argument: locality plus rule-type symmetry plus dynamics forces local invariance. The physicist is not free to demand or not-demand. The substrate either has a connection field that compensates for local relabeling, or it has a contradiction between rule-type meaninglessness and dynamical consequence.

This is the load-bearing T17 contribution. The gauge field is not introduced to make a postulate work; it is forced by the conjunction of substrate primitives, with no postulate involved.

---

## 5. The Gauge Field as Rule-Type Connection

With local invariance forced, the next question is *what* the connection field looks like. The mathematics is the standard fiber-bundle / connection apparatus, applied to the substrate's rule-type structure.

### 5.1 The connection field

Introduce a real four-vector field $A_\mu(x^\mu)$ on spacetime, transforming under local $U(1)$ as:

$$
A_\mu(x^\mu) \to A'_\mu(x^\mu) = A_\mu(x^\mu) − \partial_\mu \alpha(x^\mu)/q
$$

(The factor of $q$ — the chain's rule-type-coupling charge — is conventional. Without it, $A_\mu$ would carry inverse-charge units; with it, $A_\mu$ has standard electromagnetic-potential units.)

This $A_\mu$ is the **gauge field** or, in the substrate reading, the **rule-type connection** — the substrate object that carries rule-type label information from point to point.

### 5.2 Substrate-level interpretation

The gauge field $A_\mu$ is what the substrate's rule-type infrastructure looks like in the continuum limit. At the substrate level, the rule-type assignment to a chain is a primitive structural label. Locally, the label can be relabeled. Globally, no fact-of-the-matter forces the labels at distant regions to match. The connection $A_\mu$ encodes the *parallel transport* of rule-type labels: given a label choice at point $x$, $A_\mu(x)$ tells you what label corresponds to it at the infinitesimally-displaced point $x + dx$.

In the language of fiber bundles, the substrate's rule-type assignment is a $G$-bundle over the spacetime base, where $G$ is the rule-type relabeling group. The gauge field $A_\mu$ is a connection on this bundle. Local gauge transformations are vertical bundle automorphisms — they change the trivialization without changing the bundle itself.

### 5.3 The substrate provides the connection; physics finds it as $A_\mu$

What standard physics calls "the electromagnetic four-potential" is, in the framework, the continuum-limit appearance of the substrate's rule-type connection for the $U(1)$ rule-type relabeling group. It is not introduced as new ontological content. It is the coarse-grained reading of substrate machinery that was already there.

This is what T17's "subsumes T5" means in the framework's theorem ledger: the older T5 result (which posited the gauge field as primitive) is replaced by T17, which derives it as the substrate's rule-type connection. No new primitive is introduced.

---

## 6. Minimal Coupling, Forced

With the connection in hand, the modification of the dynamical equation is direct.

### 6.1 The gauge-covariant derivative

Replace $\partial_\mu$ by

$$
D_\mu \equiv \partial_\mu + (iq/\hbar) A_\mu
$$

Under a local $U(1)$ transformation parameterized by $\alpha(x^\mu)$:

$$
\Psi \to e^{i\alpha /\hbar} \Psi
A_\mu \to A_\mu − \partial_\mu \alpha /q
$$

direct computation gives:

$$
D'_\mu \Psi' = (\partial_\mu + (iq/\hbar)(A_\mu − \partial_\mu \alpha /q))(e^{i\alpha /\hbar} \Psi)
= e^{i\alpha /\hbar} [\partial_\mu \Psi + (i/\hbar)(\partial_\mu \alpha) \Psi + (iq/\hbar) A_\mu \Psi − (i/\hbar)(\partial_\mu \alpha) \Psi]
= e^{i\alpha /\hbar} [\partial_\mu \Psi + (iq/\hbar) A_\mu \Psi]
= e^{i\alpha /\hbar} D_\mu \Psi
$$

The unwanted $(\partial_\mu \alpha)$ term cancels. $D_\mu \Psi$ transforms with the same phase factor as $\Psi$ — the same way an ordinary $\partial_\mu$ would have transformed under a *global* relabeling. This is the defining property of a gauge-covariant derivative.

### 6.2 Why this form is unique

The replacement $\partial_\mu \to D_\mu= \partial_\mu + (iq/\hbar) A_\mu$ is the *unique* first-order modification that restores local invariance. Any other modification — adding terms quadratic in $A_\mu$, or terms involving $\partial_\mu A_\nu$, or non-linear combinations — either fails to cancel the $(\partial_\mu \alpha)$ term or introduces additional structure not forced by local invariance alone.

Higher-order terms (such as Pauli's anomalous magnetic moment coupling $\sigma^{\mu\nu} F_{\mu\nu}$) are gauge-invariant on their own but introduce structure beyond the minimal requirement. They are *consistent* with gauge invariance, not *forced by* it. The minimal-coupling prescription $\partial_\mu \to D_\mu$ is what's forced; everything else is additional structure.

### 6.3 The interacting equation

For a charged scalar field satisfying Klein-Gordon, replacing $\partial_\mu$ by $D_\mu$ gives:

$$
(D_\mu D^\mu + m^{2}c^{2}/\hbar^{2}) \Psi= 0
$$

For a charged spinor field satisfying Dirac, replacing $\partial_\mu$ by $D_\mu$ gives:

$$
(i\hbar \gamma^\mu D_\mu − mc) \Psi= 0
$$

In both cases, the free equation is recovered when $A_\mu= 0$. The interacting equation is the unique gauge-covariant first-order extension of the free equation.

This is what the Klein-Gordon and Dirac walkthroughs invoke without justification. T17 supplies the justification.

---

## 7. The Non-Abelian Extension

For rule-types whose relabeling group is a non-Abelian compact Lie group $G$ (such as $SU(2)$ or $SU(3)$), the same structural argument runs with one modification: the participation measure carries an internal index, and the gauge field becomes Lie-algebra-valued.

### 7.1 The participation measure with internal index

Let $T^a$ ($a = 1, \ldots, \dim G$) be a basis for the Lie algebra $\mathfrak{g}$ of $G$, with structure constants $f^{abc}$ satisfying

$$
[T^a, T^b] = i f^{abc} T^c
$$

The participation measure carries an internal index $i$:

$$
\Psi_i(x^\mu), i = 1, ..., dim(rep)
$$

Under a local $G$-transformation parameterized by $\alpha^a(x^\mu)$:

$$
\Psi \to U(\alpha) \Psi, U(\alpha) = \exp(i \alpha^a T^a / \hbar)
$$

with $T^a$ in some representation of $\mathfrak{g}$ acting on the index $i$.

### 7.2 The connection becomes Lie-algebra-valued

The gauge field becomes a Lie-algebra-valued one-form on spacetime:

$$
A_\mu(x^\mu) = A_\mu^a(x^\mu) T^a
$$

with one real-valued component $A_\mu^a$ for each generator. Under local $G$-transformation, $A_\mu$ transforms as:

$$
A_\mu \to U A_\mu U^{-1} − (i\hbar /g) U \partial_\mu U^{-1}
$$

(The coupling constant $g$ replaces the abelian $q$. Different generators may carry different couplings, but for a simple gauge group all components share the same coupling.)

### 7.3 The non-Abelian gauge-covariant derivative

The covariant derivative becomes:

$$
D_\mu \equiv \partial_\mu + (ig/\hbar) A_\mu^a T^a
$$

Under local $G$-transformation, $D_\mu \Psi$ transforms as $U(\alpha) D_\mu \Psi$ — the same way $\Psi$ transforms — by the same algebraic argument as in §6.1, now applied with the matrix $U(\alpha)$ instead of the scalar phase.

This is non-Abelian minimal coupling. Substituting it into the relativistic field equations gives the corresponding interacting equations for the charged sector.

### 7.4 Self-interaction

In the $U(1)$ case, the gauge field interacts with charged matter but not with itself: the photon is electrically neutral. In the non-Abelian case, the gauge field interacts with itself because the structure constants $f^{abc}$ produce non-vanishing commutators $[A_\mu, A_\nu]$. This *self-interaction* is the structural content that distinguishes Yang-Mills theory from electromagnetism.

The self-interaction is forced. It is not added by hand. The non-commutativity of $G$ forces the connection's transformation law to involve $[A_\mu, A_\nu]$, which forces the kinetic term to include terms cubic and quartic in $A_\mu$. This is the source of gluon-gluon coupling in QCD and W-boson self-coupling in the electroweak sector.

---

## 8. Field Strength and Self-Interaction

The connection is now in place. The remaining structural step is the connection's own dynamics — the field strength and the gauge-invariant action.

### 8.1 The field strength

The substrate-level definition of the field strength comes from the commutator of two covariant derivatives applied to $\Psi$:

$$
[D_\mu, D_\nu] \Psi= (ig/\hbar) F_{\mu \nu} \Psi
$$

Direct computation gives:

$$
F_{\mu \nu} = \partial_\mu A_\nu − \partial_\nu A_\mu + (ig/\hbar) [A_\mu, A_\nu]
$$

For the abelian $U(1)$ case, the commutator $[A_\mu, A_\nu]$ vanishes and $F_{\mu\nu}$ reduces to the standard electromagnetic field strength:

$$
F_{\mu \nu} = \partial_\mu A_\nu − \partial_\nu A_\mu(abelian case)
$$

For the non-Abelian case, $F_{\mu\nu}$ becomes Lie-algebra-valued:

$$
F_{\mu \nu} = F_{\mu \nu}^a T^a, F_{\mu \nu}^a = \partial_\mu A_\nu^a − \partial_\nu A_\mu^a − (g/\hbar) f^{abc} A_\mu^b A_\nu^c
$$

The $f^{abc} A_\mu^b A_\nu^c$ term is the non-Abelian self-interaction at the field-strength level.

### 8.2 The Yang-Mills action

The unique gauge-invariant, Lorentz-invariant, local, quadratic-in-derivatives kinetic term for $A_\mu$ is:

$$
\mathcal{L}_{YM} = −(1/4) F_{\mu \nu}^a F^{a \mu \nu}
$$

The trace structure $F_{\mu\nu}^a F^{a\,\mu\nu}$ contracts the Lie-algebra index $a$ via the Killing form of $\mathfrak{g}$ (which reduces to $\delta^{ab}$ for compact simple groups in the standard normalization). The Lorentz-index contraction reproduces the $E^2 - B^2$ form of electromagnetism in the abelian case.

The factor of $-1/4$ is conventional — it sets the coefficient of the kinetic term to its standard form so that $A_\mu^a$ has canonical mass dimension and the equations of motion reduce to the standard Maxwell-Yang-Mills form.

### 8.3 Why this action is unique

The kinetic term must satisfy three conditions: gauge invariance, Lorentz invariance, and locality. The lowest-order (quadratic in derivatives, dimensionless coupling) gauge-invariant Lorentz scalar built from $A_\mu^a$ is $F_{\mu\nu}^a F^{a\,\mu\nu}$. Higher-order terms (such as $F^4$ or $F\square F$) are gauge-invariant but introduce non-renormalizable structure not forced by the basic principles. The quadratic action is what's forced; higher-order terms are additional structure.

### 8.4 The Yang-Mills equation

Varying the Yang-Mills action with respect to $A_\mu^a$ gives the Yang-Mills equation:

$$
D_\mu F^{\mu \nu} = J^\nu
$$

where $J^\nu$ is the matter current sourced by the charged fields. In the abelian case, this is Maxwell's equations. In the non-Abelian case, this is the Yang-Mills equation that drives the strong and weak interactions.

This is the equation that the Yang-Mills walkthrough analyzes for mass-gap behavior and substrate-to-continuum closure. T17 supplies its derivational origin.

---

## 9. What's Forced, What's Inherited, What's Open

It is worth being precise about what changes when the framework is in place versus when it isn't.

### 9.1 What's forced

The existence of a gauge field $A_\mu$ as the substrate's rule-type connection is forced. It is not introduced as new ontological content. Rule-type is a substrate primitive; locality is a substrate primitive; the conjunction forces a connection.

The transformation law $A_\mu \to A_\mu - \partial_\mu \alpha / q$ (abelian) or $A_\mu \to U A_\mu U^{-1} - (i\hbar/g) U \partial_\mu U^{-1}$ (non-abelian) is forced by the requirement that local rule-type relabeling close as a substrate symmetry.

Minimal coupling — the replacement $\partial_\mu \to D_\mu= \partial_\mu + (ig/\hbar) A_\mu^a T^a$ — is the unique first-order modification of the free dynamics that restores local invariance. The form is forced; alternatives either fail to restore invariance or introduce additional structure.

The field strength $F_{\mu\nu}$ via $[D_\mu, D_\nu] = (ig/\hbar) F_{\mu\nu}$ is forced. The Yang-Mills kinetic term $-\frac{1}{4} F_{\mu\nu}^a F^{a\,\mu\nu}$ is the unique gauge-invariant, Lorentz-invariant, local, lowest-order kinetic term.

The Yang-Mills equation $D_\mu F^{\mu\nu} = J^\nu$ is forced as the variational equation of motion.

### 9.2 What's inherited

The specific gauge group $G$ — $U(1)$ for electromagnetism, $SU(2)$ for the weak interaction, $SU(3)$ for the strong interaction, or some larger group at higher unification — is inherited from the rule-type taxonomy of our universe. The framework establishes that *some* compact Lie group plays the relabeling role; *which* compact Lie group is empirical input. The Standard Model's $U(1) \times SU(2) \times SU(3)$ is read off from the taxonomy of observed rule-types (electron, neutrino, quark colors, weak doublets) rather than derived from deeper substrate primitives.

The coupling constants $q, g, g_s$ — the strengths of the gauge interactions — are inherited from the substrate-coupling rate at which rule-type relabelings transmit through the V1 kernel. The framework does not (currently) derive numerical values for these; they are read off the dimensional atlas.

The matter content — which rule-types exist with what gauge charges — is inherited from observed particle physics. The three generations of fermions, the specific charge assignments, the fact that quarks come in three colors — these are taxonomic facts about rule-types in our universe, not derivations from substrate primitives.

The factor of $-1/4$ in the kinetic term is conventional — it sets the canonical normalization of $A_\mu$ and is not substrate-derived.

### 9.3 What's open

The deepest open question is the rule-type taxonomy itself. Why does our universe have the specific rule-types it has? Why $U(1) \times SU(2) \times SU(3)$ and not some other gauge structure? Why three generations? Why the specific charge assignments? These are questions about the *shape* of the substrate's rule-type taxonomy, which the framework treats as empirical input. The structural-foundations program closes the question of *what gauge fields are* (rule-type connections) but leaves open *which gauge fields actually exist* (taxonomic data about our specific universe).

A second open question is the relationship between rule-type relabeling and chiral structure. The Standard Model's gauge interactions are *chiral* — the weak force couples differently to left-handed and right-handed fermions. The framework's rule-type primitive does distinguish left-handed from right-handed via the spinor representation (Dirac walkthrough §3-§5), so chirality is substrate-grounded, but the specific chiral coupling pattern of the weak interaction is taxonomic input.

A third open question is the Higgs mechanism — how rule-types acquire mass via spontaneous breaking of a symmetry that is otherwise gauge-protected. This is `arcs/arc-Q/higgs_mechanism_scoping.md` in the framework's repository, and the derivation is partial. The structural connection between rule-type taxonomy, gauge symmetry, and mass-generation through symmetry breaking is open.

T17 closes the structural foundations of gauge fields. It does not close the empirical content of which gauge fields nature happens to have. That distinction is honest framing, not a concession.

---

## 10. What This Argument Establishes

The chain runs:

Substrate primitives (micro-events, participation, channels, bandwidth, polarity, ED gradient, locality, rule-type) → T14 (participation measure form forced) → U2 (inner product on participation-measure space forced) → Lorentz covariance (participation measure on Minkowski spacetime forced via Klein-Gordon and Dirac walkthroughs) → rule-type as primitive label-content distinction (§3) → locality + rule-type symmetry forces local relabeling as the substrate-realizable form of the symmetry (§4) → connection field $A_\mu$ as rule-type connection (§5) → minimal coupling $D_\mu= \partial_\mu + (ig/\hbar) A_\mu^a T^a$ as unique first-order modification (§6) → non-Abelian extension via Lie-algebra-valued connection (§7) → field strength $F_{\mu\nu}$ and Yang-Mills action (§8) → Yang-Mills equation $D_\mu F^{\mu\nu} = J^\nu$.

Gauge fields are now derived consequences of substrate ontology rather than postulates introduced to make a postulated gauge principle work. The mathematical content of the standard fiber-bundle / connection / minimal-coupling apparatus is unchanged. What changes is the foundational status: $A_\mu$ is no longer extra ontological furniture; it is the continuum-limit appearance of the substrate's rule-type infrastructure.

The framework reproduces the Standard Model's gauge structure exactly. Quantum electrodynamics is the $U(1)$ projection of T17. Weak interactions are the $SU(2)$ projection. Quantum chromodynamics is the $SU(3)$ projection. The minimal-coupling prescription that the Klein-Gordon and Dirac walkthroughs invoke is forced rather than postulated. The Yang-Mills equation that the Yang-Mills walkthrough analyzes is derived rather than written down.

For empirically tested gauge phenomena — Coulomb's law, the Aharonov-Bohm effect, the running of the strong coupling, $W$ and $Z$ boson production, gluon jets, electroweak precision tests — the framework predicts the same as standard physics. T17 is upstream-grounding for an argument standard physics already runs successfully.

What's new is the answer to "why are interactions gauge interactions?" In standard physics, this is the gauge principle, accepted without derivation. In ED, it is the conclusion of an argument: rule-type is a substrate primitive, locality forbids global coordination of label choices, dynamics forbids local label changes from having consequences, and the only way to reconcile these is for the substrate to provide a connection field that compensates for local relabeling. That field, in the continuum limit, is what physics calls the gauge field.

The factor that's worth emphasizing: T17 does not introduce any new substrate primitive. The rule-type primitive was already in the framework's inventory, used in the spin-statistics walkthrough to distinguish bosonic from fermionic chains, used in the Dirac walkthrough to motivate the spinor-valued participation measure, used in the mass walkthrough to anchor the $\sigma_\tau$ form. T17 reads off the gauge structure from the same primitive that was already doing other work. The substrate inventory is unchanged; the structural-foundations theorem inventory grows by one.

Whether the substrate primitives themselves are right is the load-bearing empirical question, as in every walkthrough. The framework stands or falls on whether participation, bandwidth, channels, polarity, locality, and rule-type are the correct foundational concepts. The empirical exposure of the framework lives in its predictions across other sectors — soft-matter mobility, substrate-derived gravity transitions, quantum-computational ceilings — not in gauge-field structure, where the framework reproduces the empirically validated standard-model results without modification.

For gauge fields specifically, the structural case is closed. Minimal coupling is forced. Yang-Mills theory is what falls out when the rule-type relabeling group is non-Abelian. The gauge field is not a postulated piece of ontology; it is what the substrate's rule-type connection looks like at the continuum scale. The gauge principle is not a principle but a theorem.

---

## 11. References

- Yang, C. N., Mills, R. L. "Conservation of Isotopic Spin and Isotopic Gauge Invariance." *Physical Review* 96, 191–195 (1954).
- Weyl, H. "Elektron und Gravitation." *Zeitschrift für Physik* 56, 330–352 (1929).
- Glashow, S. L. "Partial-Symmetries of Weak Interactions." *Nuclear Physics* 22, 579–588 (1961).
- Salam, A. "Weak and Electromagnetic Interactions." *Proceedings of the 8th Nobel Symposium* (1968).
- Weinberg, S. "A Model of Leptons." *Physical Review Letters* 19, 1264–1266 (1967).
- 't Hooft, G. "Renormalizable Lagrangians for Massive Yang-Mills Fields." *Nuclear Physics B* 35, 167–188 (1971).
- Atiyah, M. F., Singer, I. M. "The Index of Elliptic Operators on Compact Manifolds." *Bulletin of the American Mathematical Society* 69, 422–433 (1963).
- Kobayashi, S., Nomizu, K. *Foundations of Differential Geometry, Vol. 1.* Wiley-Interscience, 1963.
- Proxmire, A. *The Born Rule as a Forced Theorem of Event Density: A Gleason–Busch Reconstruction from First Principles.* April 2026.
- Proxmire, A. *The Inner Product as Forced Structure in Event Density: Discrete Derivation, Continuum Lift, and Gauge-Invariant Completion.* April 2026.
- Proxmire, A. *U5: The Forced Structure of Translation Symmetry and the Momentum Operator.* April 2026.
- Proxmire, A. *Theorem 17: Gauge-Field-as-Rule-Type — The Substrate Origin of Gauge Fields and Minimal Coupling.* April 2026.
- Proxmire, A. *Event Density: One Substrate, Three Domains.* April 2026.
- Proxmire, A. *ED-QFT Unified Overview.* April 2026.
- Peskin, M. E., Schroeder, D. V. *An Introduction to Quantum Field Theory.* Westview Press, 1995.
- Weinberg, S. *The Quantum Theory of Fields, Volume II: Modern Applications.* Cambridge University Press, 1996.
- The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.
