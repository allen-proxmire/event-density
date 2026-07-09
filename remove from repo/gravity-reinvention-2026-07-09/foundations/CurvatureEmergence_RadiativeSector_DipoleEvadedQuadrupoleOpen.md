# ED's Radiative Sector: the Bandwidth Field Radiates, the Dipole Catastrophe Is Structurally Evaded (Universal Coupling = the Equivalence Principle), and the Quadrupole Rate/Polarization Is the Sharpened Open Tension

**Foundations, gravity / curvature-emergence arc, the radiative sector. Paper E (`Paper_RelationalGravity_HolographicMetric`) flagged the sharpest open tension: ED's metric is kinematic (a read-out of the bandwidth field `b`), and binary-pulsar decay + LIGO inspirals are weak-field confirmations of dynamical, energy-carrying, spin-2 radiation that an acoustic metric does not obviously produce. This note takes it on. Probe: `evaluation/CurvatureEmergence/radiative_sector_dipole_probe.py`. Result, three parts. (1) ED DOES radiate: "an acoustic metric does not radiate" is too quick, the UNDERLYING bandwidth field radiates (it propagates retarded via the V1 kernel + the arrow's finite substrate speed, so `□b = source` has radiative solutions), like density waves in the fluid analogy. The radiation is SCALAR (`b` is a scalar; the kinematic metric is its read-out). (2) The DIPOLE catastrophe (the strongest pulsar killer of scalar gravity) is STRUCTURALLY EVADED: a mass is a universal bandwidth-influence `Q ∝ M`, so the scalar dipole moment `D = Σ Q_i x_i` equals `(Q/M)` times the mass dipole, whose second derivative is `d(momentum)/dt = 0` for an isolated binary, so `D̈ = 0` and radiation starts at QUADRUPOLE, like GR. Probe confirms: universal coupling gives dipole/quadrupole power `~ 6e-23` (machine zero), non-universal coupling brings it back (`~ 3e-3 ~ (Δ(Q/m))²`, the scalar-tensor dipole pulsars exclude). The universality that does this is the SAME universality as ED's kinematic metric (all matter reads the same `g~1/b`), i.e. the equivalence principle, so the dipole suppression is structural, not assumed. (3) The SHARPENED remaining tension: the scalar QUADRUPOLE rate and POLARIZATION vs GR's TENSOR quadrupole (pulsar 0.1% match + LIGO polarization), which is open. So Paper E's radiative tension is partially resolved and narrowed: ED radiates, evades the dipole catastrophe structurally, and the honest open question is the quadrupole rate/polarization.**

---

## 1. Does ED radiate at all? Yes: the bandwidth field radiates

The naive worry is "an acoustic/kinematic metric cannot radiate energy as spin-2 waves." That is too quick, because it looks at the shadow, not the substance. In ED the metric `g~1/b` is a read-out of the bandwidth field `b`; the dynamics live in `b`. And `b` propagates **retarded** at a finite speed: the V1 single-chain kernel is retarded (Papers #18/#19), and the arrow makes propagation forward-causal at a finite substrate speed. So the near-zone static limit (`∇²Φ = source`, `Φ~1/r`, the Gauss result of this arc) is the instantaneous limit of a genuinely dynamical field whose far-zone behaviour is a wave equation `□b = source`. A time-varying mass (an accelerating binary) is a time-varying bandwidth source, and it radiates bandwidth waves that carry energy, exactly as the fluid analogy predicts (the acoustic metric is kinematic, but the fluid density that carries it has real wave dynamics and real radiation). **ED has a radiative sector.** Its character: the radiating field is `b`, a **scalar**, and the metric perturbation is its kinematic read-out. That scalar character is the whole story of the tension, because scalar gravity has a notorious problem.

## 2. The dipole catastrophe, and why ED structurally evades it

Scalar gravitational radiation generically has a **dipole** term, which is `O(c/v)` *louder* than quadrupole and which binary pulsars (especially compactness-asymmetric neutron-star / white-dwarf binaries) exclude to high precision. Dipole radiation is what kills most scalar-tensor theories. So the decisive question for ED is whether its scalar radiation has a dipole.

The scalar dipole moment of a set of bandwidth charges is `D = Σ_i Q_i x_i`, and dipole radiation is powered by `⟨D̈²⟩` with `D̈ = Σ_i Q_i ẍ_i`. Now use ED's own reading of mass: **a mass is its bandwidth-influence, `Q_i = α m_i` with a universal `α` (the same bandwidth-charge-to-mass ratio for every body).** Then
$$\ddot D = \sum_i Q_i \ddot x_i = \alpha \sum_i m_i \ddot x_i = \alpha \sum_i F_i^{\text{int}} = 0,$$
because for an isolated binary the internal forces cancel by Newton's third law (equivalently, `D = α \times` the mass dipole `= α M X_{\text{com}} = 0` in the COM frame). So **`D̈ = 0`: no dipole radiation, and the leading radiation is quadrupole, like GR.**

**The universality is not an extra assumption; it is ED's equivalence principle.** ED's metric is a *universal* read-out of `b`: every chain, whatever its composition, sees the same `g~1/b`, so all bodies fall the same way (the weak equivalence principle holds structurally in ED, because the metric is one universal function of `b`). That same universality is exactly `Q/M =` const for all bodies. So the property that suppresses the dipole radiation is the property ED already has: a universal kinematic metric. The dipole suppression is structural.

**Probe (`radiative_sector_dipole_probe.py`).** A mass-asymmetric two-body circular orbit (`m1=1.4, m2=1.0`), scalar dipole and mass-quadrupole moments computed and spectrally differentiated over the orbit:

| coupling | scalar dipole `|D|` | dipole / quadrupole radiated power |
|---|---|---|
| **universal** (`Q_i/m_i` equal) | `1.2e-16` (machine zero) | **`6e-23`** (no dipole radiation) |
| non-universal (`Q_i/m_i` differ 30%) | `0.12` | `2.7e-3` (`~ (Δ(Q/m))²`, dipole reappears) |

Universal bandwidth coupling gives an exactly vanishing scalar dipole moment in the COM frame, so dipole radiation is machine-zero and radiation starts at quadrupole; a non-universal coupling brings back the scalar-tensor dipole radiation that pulsars exclude. **Universal coupling (ED's equivalence principle) structurally evades the dipole catastrophe.**

## 3. The sharpened remaining tension: quadrupole rate and polarization

Evading the dipole is the strong result (it is what excludes most scalar-gravity theories), but it is not the whole test. Two things remain, and they are the honest, narrowed form of Paper E's tension:

- **Quadrupole rate.** A *scalar* quadrupole radiates at a different coefficient than GR's *tensor* quadrupole. Binary pulsars match GR's quadrupole formula to `~0.1%`. So ED's scalar quadrupole (plus any emergent tensor sector) must sum to GR's rate; a generic scalar quadrupole does not, unless the scalar coupling is weak or structured in a specific way. Not shown.
- **Polarization.** GR predicts two tensor polarizations (`+`, `×`); a scalar field radiates a breathing (scalar) mode. LIGO/Virgo multi-detector observations (e.g. GW170817) constrain the polarization content toward the two tensor modes, disfavouring a purely scalar mode. A purely-scalar-radiation ED would face this. Not shown.

So the sharpened tension: ED evades the *dipole* catastrophe structurally, but the *quadrupole rate* and the *polarization* of its scalar radiation, versus GR's tensor quadrupole, are open, and are the real remaining challenge from pulsars and LIGO.

## 4. Honest tiers and verdict

- **ED radiates (structural).** The bandwidth field is retarded (V1 kernel + finite substrate speed) and scalar; a time-varying mass radiates bandwidth waves carrying energy. "Acoustic metric does not radiate" is refuted at the level of the underlying field.
- **Dipole suppression (derived, conditional on the universal-coupling reading).** `Q ∝ M` universally ⟹ `D̈ = 0` ⟹ no dipole radiation ⟹ leading radiation is quadrupole. Analytic and probe-confirmed. Conditional on "mass = a universal bandwidth-influence `Q`," which is the reading of P04 already used in the Gauss field equation, and which is ED's equivalence principle (the universal kinematic metric). So the condition is the same universality ED already has, not a new input.
- **Quadrupole rate / polarization (open).** Scalar quadrupole vs GR tensor quadrupole; pulsar 0.1% rate match + LIGO tensor-polarization preference. The sharpened remaining tension.

**Verdict.** Paper E's radiative tension is partially resolved and sharpened. ED has a radiative sector (the scalar bandwidth field radiates), and it **structurally evades the dipole catastrophe** (the strongest pulsar killer of scalar gravity) via the universal bandwidth coupling that is its equivalence principle, a real and non-trivial pass, confirmed by the probe. The honest remaining question, narrowed from "does it radiate / dipole catastrophe" to a sharp point, is the **scalar quadrupole rate and polarization versus GR's tensor quadrupole**. That, not dipole radiation, is now the live pulsar/LIGO test for ED gravity, and it is the natural next target (does ED have, or emergently generate, a tensor radiative sector, or a scalar quadrupole that matches GR's rate?).

## 5. Status and Paper E

This upgrades Paper E's flagged tension (§6/§9/§10.4). Paper E currently states radiative gravity as an undifferentiated "live potential-falsifier"; this note refines it: the **dipole** part is structurally evaded (a pass), the **quadrupole rate/polarization** part is the sharp open tension. Paper E's §6 and §10.4 should be updated to reflect the split (dipole evaded via the equivalence-principle coupling; quadrupole rate/polarization open), which strengthens the paper (it turns a blanket worry into a specific, partially-answered, still-falsifiable claim). The falsifier sharpens to: *a scalar-quadrupole rate or polarization inconsistent with the measured pulsar decay / LIGO polarization, with no emergent tensor sector, would falsify ED gravity*, and the dipole-radiation line (which would have been the easy kill) is closed.
