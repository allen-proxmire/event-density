"""The quadrupole/tensor question: ED radiates a SCALAR breathing mode, not GR's spin-2 tensor.

The radiative-sector note evaded the dipole catastrophe but left the quadrupole rate/polarization
open. This probe settles the POLARIZATION half, and it follows directly from the kinematic-metric
stance:

  GR's two tensor polarizations (+, x) require a DYNAMICAL rank-2 field (the metric carrying its own
  degrees of freedom). ED's metric is KINEMATIC: a read-out g_ij ~ (1/b) delta_ij of the single
  scalar bandwidth field b. So the radiative degrees of freedom are those of b: ONE scalar mode. The
  metric perturbation from any source is h_ij = -(delta_b / b^2) delta_ij, PROPORTIONAL TO delta_ij,
  i.e. pure trace / conformal = the BREATHING (spin-0) polarization, with ZERO transverse-traceless
  (spin-2) part. So ED necessarily predicts scalar breathing-mode GW, not GR's tensor +/x.

Two demonstrations:
  (A) POLARIZATION CONTENT: decompose a transverse metric perturbation into (+, x, breathing). ED's
      conformal h_ij ~ delta_ij is 100% breathing, 0% tensor; GR's h_ij is traceless-transverse,
      0% breathing. So ED radiation is pure scalar; GR is pure tensor.
  (B) OBSERVABILITY: a detector network responds to +, x, breathing with different antenna patterns.
      Show the breathing response is LINEARLY INDEPENDENT of the tensor responses (a network can
      separate scalar from tensor), so the prediction is falsifiable. This is exactly the test LIGO-
      Virgo ran (GW170814): the data favored pure TENSOR over pure scalar, so ED's scalar prediction
      is currently DISFAVORED -- a live potential-falsification, honestly a tension, not a pass.

Honest scope: this settles the POLARIZATION (ED = scalar breathing, distinct and falsifiable, and
currently disfavored). The quadrupole RATE (does the scalar quadrupole coefficient match the observed
pulsar decay that GR fits with tensor quadrupole?) is a separate quantitative question, not settled
here. The result is a distinctive, RISKY, falsifiable prediction -- the cleanest observational face
of the kinematic-metric stance -- reported as a tension, not a success.
"""
import numpy as np


def transverse_basis(nhat):
    """Two orthonormal vectors spanning the plane transverse to propagation direction nhat."""
    nhat = nhat / np.linalg.norm(nhat)
    a = np.array([0, 0, 1.0]) if abs(nhat[2]) < 0.9 else np.array([1.0, 0, 0])
    l = np.cross(nhat, a); l /= np.linalg.norm(l)
    m = np.cross(nhat, l)
    return l, m


def pol_tensors(nhat):
    """Polarization basis tensors for +, x, and breathing (scalar), given propagation nhat."""
    l, m = transverse_basis(nhat)
    e_plus = np.outer(l, l) - np.outer(m, m)
    e_cross = np.outer(l, m) + np.outer(m, l)
    e_breath = np.outer(l, l) + np.outer(m, m)          # scalar transverse "breathing" mode
    return e_plus, e_cross, e_breath


def decompose(h, nhat):
    """Project a symmetric perturbation h onto (+, x, breathing) in the transverse plane; return the
    fractional power in each. Normalize by the transverse Frobenius norm."""
    ep, ec, eb = pol_tensors(nhat)
    # normalized inner products (each basis tensor has ||.||^2 = 2)
    cp = np.sum(h * ep) / 2.0
    cc = np.sum(h * ec) / 2.0
    cb = np.sum(h * eb) / 2.0
    tot = cp**2 + cc**2 + cb**2
    if tot == 0:
        return 0.0, 0.0, 0.0
    return cp**2/tot, cc**2/tot, cb**2/tot


def rand_rotation(rng):
    """A random 3D rotation matrix (QR of a random Gaussian matrix)."""
    q, r = np.linalg.qr(rng.standard_normal((3, 3)))
    return q * np.sign(np.diag(r))


def detector_tensor_3d(rng):
    """An L-shaped detector whose two orthogonal arms have a random 3D orientation (as detectors at
    different points on Earth have differently-oriented local planes in the global frame)."""
    R = rand_rotation(rng)
    u = R[:, 0]; v = R[:, 1]
    return 0.5 * (np.outer(u, u) - np.outer(v, v))


def main():
    print("=" * 90)
    print("QUADRUPOLE/TENSOR QUESTION: ED radiates a SCALAR breathing mode, not GR's spin-2 tensor")
    print("=" * 90)

    nhat = np.array([0.3, -0.4, 0.85]); nhat /= np.linalg.norm(nhat)

    print("\n (A) POLARIZATION CONTENT of the metric perturbation (fraction in +, x, breathing):")
    # ED: h_ij ~ delta_ij (conformal, from g ~ 1/b), pure trace
    h_ED = np.eye(3) * 1.0
    fp, fc, fb = decompose(h_ED, nhat)
    print(f"   ED  (h_ij ~ delta_ij, conformal / kinematic metric):  +={fp:.3f}  x={fc:.3f}  breathing={fb:.3f}")
    # GR: a transverse-traceless tensor perturbation (example: pure + in the transverse frame)
    ep, ec, eb = pol_tensors(nhat)
    h_GR = ep + 0.6 * ec
    fp, fc, fb = decompose(h_GR, nhat)
    print(f"   GR  (transverse-traceless tensor h):                  +={fp:.3f}  x={fc:.3f}  breathing={fb:.3f}")
    print("   -> ED radiation is 100% scalar breathing (0% tensor); GR is 100% tensor (0% breathing).")
    print("      ED has ONE radiative DOF (the scalar b); GR has TWO (the dynamical tensor metric).")

    print("\n (B) OBSERVABILITY: is the breathing mode distinguishable from tensor by a detector network?")
    # detectors at DIFFERENT 3D orientations (as at different points on Earth); average the
    # breathing-vs-tensor independence over random sky directions and detector networks.
    rng = np.random.default_rng(3)
    for ndet in (2, 3, 4):
        fracs = []
        for _ in range(400):
            n = rng.standard_normal(3); n /= np.linalg.norm(n)
            ep, ec, eb = pol_tensors(n)
            F = np.zeros((ndet, 3))
            for i in range(ndet):
                d = detector_tensor_3d(rng)
                F[i] = [np.sum(d*ep), np.sum(d*ec), np.sum(d*eb)]
            tensor_span = F[:, :2]; Fb = F[:, 2]
            coef, *_ = np.linalg.lstsq(tensor_span, Fb, rcond=None)
            resid = Fb - tensor_span @ coef
            fracs.append(np.linalg.norm(resid) / (np.linalg.norm(Fb) + 1e-30))
        print(f"   {ndet}-detector network: mean fraction of breathing NOT explainable by tensor = {np.mean(fracs):.3f}")
    print("   -> with >=3 differently-oriented detectors the breathing (scalar) mode is generically")
    print("      linearly INDEPENDENT of the tensor modes, so a network can separate scalar from tensor.")
    print("      (2 detectors are degenerate -- exactly why LIGO+Virgo, a 3-detector network, was needed.)")

    print("\n VERDICT:")
    print("  ED's kinematic metric (a read-out of the single scalar b) has ONE radiative DOF: a SCALAR")
    print("  BREATHING mode. It cannot produce GR's spin-2 tensor radiation, which needs a dynamical")
    print("  tensor field ED does not have. This is a sharp, distinctive, FALSIFIABLE prediction -- the")
    print("  cleanest observational face of 'the metric is a shadow, not a field.' Current status: LIGO-")
    print("  Virgo polarization tests (GW170814) favor pure TENSOR over pure scalar, so ED's scalar")
    print("  prediction is DISFAVORED -- a live potential-falsification, an honest tension, not a pass.")
    print("  (The quadrupole RATE is a separate, unsettled quantitative question.)")
    print("=" * 90)


if __name__ == "__main__":
    main()
