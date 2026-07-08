"""T4 emergent-spinor gate: build the minimal Weyl spinor + run the SQ1g discriminator.

Goal (SQ1g steps 1-3): build the two-component (Weyl) mode that HAS a helicity, apply
P05's transport one step along the arrow, and compute advance(L) - advance(R) = the
P09-charge difference between the two helicities. Zero => VECTOR (parity-conserving,
EM-like). Nonzero => CHIRAL (gamma5, parity-violating, weak-like).

FAITHFUL SETUP (not rigged):
- Arrow = +z (the retarded transport / momentum direction; P11/T18 fixes it).
- Weyl 2-spinor psi in C^2. Helicity eigenstates = spin along +/- arrow:
    |L> = spin +z (aligned),  |R> = spin -z (anti-aligned).  (labels are convention)
- P05 transport one step = a U(2) link variable (Gauge_02): U = e^{i phi} * V,
    V in SU(2) = the spin-frame re-routing, phi = the P09 U(1) phase advance.
  The SU(2) part is a frame rotation by angle theta about some axis n-hat. WHICH axis
  is set by the channel-topology geometry, and is EXACTLY what the canonical primitives
  leave open -- so we scan it rather than assume it.
- P09 charge / phase-advance of a mode |h>: arg< h | U | h > (the phase the mode's own
  P09 component advances by under one transport step -- SQ1g sec2's definition).

We DO NOT put chirality in by hand. We compute advance(L)-advance(R) for a general
frame-rotation and read off which geometry (if any) makes it nonzero.
"""
import numpy as np

I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)

ARROW = np.array([0.0, 0.0, 1.0])           # retarded transport direction = +z
L = np.array([1, 0], complex)               # spin +arrow (helicity +)
R = np.array([0, 1], complex)               # spin -arrow (helicity -)


def su2_rotation(theta, axis):
    axis = np.array(axis, float); axis = axis / np.linalg.norm(axis)
    n_s = axis[0] * sx + axis[1] * sy + axis[2] * sz
    return np.cos(theta / 2) * I2 - 1j * np.sin(theta / 2) * n_s   # exp(-i theta/2 n.sigma)


def transport(phi, theta, axis):
    """P05 U(2) link = U(1) P09 phase (phi) times SU(2) frame re-routing (theta about axis)."""
    return np.exp(1j * phi) * su2_rotation(theta, axis)


def advance(state, U):
    return np.angle(state.conj() @ (U @ state))   # P09 phase-advance of this mode


def discriminator(phi, theta, axis):
    U = transport(phi, theta, axis)
    aL, aR = advance(L, U), advance(R, U)
    # helicity conserved by transport iff [U, sigma_z] = 0 (up to numerical noise)
    comm = np.max(np.abs(U @ sz - sz @ U))
    return aL, aR, aL - aR, comm


def main():
    print("T4 emergent-spinor discriminator: advance(L) - advance(R) under P05 transport.")
    print("Arrow = +z. Helicity eigenstates |L>=spin+z, |R>=spin-z. Default prior: VECTOR.\n")
    phi = 0.7                          # arbitrary P09 U(1) advance (the vector/common part)
    theta = 0.9                        # arbitrary frame-rotation angle

    print(f"P09 U(1) advance phi = {phi} (common to both helicities by construction)\n")
    print(f"{'frame rotation axis':28s}{'adv(L)':>9}{'adv(R)':>9}{'DISCRIM':>10}{'[U,sz]':>9}  verdict")
    print("-" * 92)
    cases = [
        ("none (pure translation)", 0.0, [0, 0, 1]),
        ("transverse x (no screw)", theta, [1, 0, 0]),
        ("transverse y (no screw)", theta, [0, 1, 0]),
        ("tilted 45deg (partial)", theta, [1, 0, 1]),
        ("ABOUT ARROW z (screw)", theta, [0, 0, 1]),
    ]
    for lab, th, ax in cases:
        aL, aR, disc, comm = discriminator(phi, th, ax)
        verdict = "CHIRAL (gamma5)" if abs(disc) > 1e-9 else "vector"
        print(f"{lab:28s}{aL:>9.3f}{aR:>9.3f}{disc:>10.3f}{comm:>9.3f}  {verdict}")

    # General law: scan the arrow-component n_z of the rotation axis; show DISCRIM depends
    # ONLY on n_z (the screw component), independent of the transverse part.
    print("\nGeneral law: discriminator vs arrow-component n_z of the frame-rotation axis")
    print(f"(theta={theta} fixed; transverse part varied but irrelevant):")
    print(f"{'n_z':>8}{'DISCRIM':>12}{'-2*atan2(sin(t/2)nz,cos(t/2))':>34}")
    for nz in [0.0, 0.25, 0.5, 0.75, 1.0]:
        nt = np.sqrt(max(0.0, 1 - nz**2))
        _, _, disc, _ = discriminator(phi, theta, [nt, 0, nz])
        closed = -2 * np.arctan2(np.sin(theta/2) * nz, np.cos(theta/2))
        print(f"{nz:>8.2f}{disc:>12.4f}{closed:>34.4f}")

    print("\n" + "=" * 92)
    print("RESULT: advance(L)-advance(R) = -2 atan2(sin(theta/2) n_z, cos(theta/2)),")
    print("i.e. it depends ONLY on n_z, the component of the frame-rotation ABOUT THE ARROW.")
    print("  * pure translation or transverse rotation (n_z=0) -> discriminator 0 -> VECTOR")
    print("    (and helicity is NOT conserved for transverse rotation: [U,sz]!=0).")
    print("  * rotation about the arrow (n_z!=0, a SCREW) -> nonzero -> CHIRAL, and helicity")
    print("    IS conserved ([U,sz]=0): |L>,|R> are transport eigenstates with different")
    print("    P09 eigen-charges. The screw pitch IS gamma5.")
    print("So chirality <=> P05 transport SCREWS the spin-frame about the arrow it advances")
    print("along. The canonical U(N) transport (Gauge_02: isometry from P04+P07+P11) does")
    print("NOT force a screw (n_z is unfixed; the spin-frame bundle is deferred, Gauge_02")
    print("sec6.4) => DEFAULT VECTOR. Chiral must be earned by a handed channel-topology")
    print("(the tether screw, T4_03) supplying n_z!=0 -- not present in the minimal primitives.")
    print("=" * 92)


if __name__ == "__main__":
    main()
