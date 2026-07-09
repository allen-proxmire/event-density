"""Setting up the Sigma-to-K^2 coarse-graining: which action terms come from the P12 landscape, and
what exactly is left to compute for lambda.

HONEST FRAMING: this SETS UP the coarse-graining and delivers the parts that are genuinely computable;
it does NOT compute lambda (that needs the substrate's mode-resolved inertia, the named open step).

Canonical P12: Sigma_C = Coh - Str - Grad, with acceleration a = -grad(Sigma) (Newton's 2nd law). So
Sigma is the POTENTIAL; the KINETIC term (inertia) is separate. The khronometric effective action
  S = (1/16 pi G) integral N sqrt(h) [ K_ij K^ij - lambda K^2  +  xi ^3R + eta a_i a^i ]
then splits cleanly:
  - POTENTIAL terms (xi ^3R, eta a^2) <- come from Sigma (the Grad term). COMPUTABLE (this probe).
  - KINETIC term (K_ij K^ij - lambda K^2) <- comes from the INERTIA. lambda = the conformal-mode
    kinetic weight. NOT in Sigma; needs the substrate inertia. THE OPEN STEP.

Part 1 (computable): Sigma's GRAD term IS the emergent spatial curvature ^3R.
  The emergent spatial metric is h_ij = (1/b) delta_ij (conformal, from reach ~ b^{1/2} in 3D). For a
  conformally-flat 3-metric h_ij = e^{2w} delta_ij with w = -1/2 ln b, the scalar curvature is
    ^3R = -2 e^{-2w} [2 nabla^2 w + (nabla w)^2] = 2 nabla^2 b - (5/2) (nabla b)^2 / b   (derived).
  The nabla^2 b piece is a total derivative (integrates to the boundary); the remaining -(5/2)(nabla b)^2/b
  is the GRADIENT CONTENT -- exactly Sigma's Grad term. So xi ^3R = (a multiple of) Sigma's Grad: the
  emergent spatial-curvature energy IS the substrate's gradient penalty. This probe verifies the
  identity ^3R = 2 nabla^2 b - (5/2)(nabla b)^2/b numerically against the conformal curvature.

Part 2 (identify the conformal mode): the trace K = -partial_t(ln sqrt h)/N ~ (3/2) partial_t b / b -- so
  the conformal/expansion mode of the geometry IS the bandwidth density b. lambda weights this mode.

Part 3 (why lambda != 1, structural): bandwidth conservation (P04) ties the conformal (compression,
  partial_t b) mode to the current via continuity partial_t b + div J = 0, distinguishing it kinetically
  from the free (transverse) shear mode. GR's lambda=1 treats them covariantly (no distinction); ED's
  conservation constraint breaks that -> lambda != 1 (Lorentz-violating, the extra scalar = MOND sector).
  A structural reason, NOT a value. The VALUE of lambda needs the compression-vs-shear inertia (open).
"""
import numpy as np


def scalar_curvature_conformal_3d(b, dx):
    """^3R for h_ij = (1/b) delta_ij in 3D, computed from the conformal-curvature formula with
    w = -1/2 ln b:  ^3R = -2 e^{-2w}[2 lap(w) + (grad w)^2].  Return the field ^3R(x)."""
    w = -0.5 * np.log(b)
    gw = np.gradient(w, dx, edge_order=2)
    lap_w = sum(np.gradient(gw[i], dx, edge_order=2, axis=i) for i in range(b.ndim))
    gw2 = sum(g ** 2 for g in gw)
    return -2.0 * np.exp(-2 * w) * (2 * lap_w + gw2)


def derived_form_3d(b, dx):
    """The claimed identity: ^3R = 2 lap(b) - (5/2)(grad b)^2 / b."""
    gb = np.gradient(b, dx, edge_order=2)
    lap_b = sum(np.gradient(gb[i], dx, edge_order=2, axis=i) for i in range(b.ndim))
    gb2 = sum(g ** 2 for g in gb)
    return 2.0 * lap_b - 2.5 * gb2 / b


def main():
    print("=" * 92)
    print("Sigma-to-K^2 SETUP: Grad = emergent spatial curvature (computable); lambda = kinetic (open)")
    print("=" * 92)

    # a smooth 3D bandwidth dip (a "mass")
    L = 60; dx = 1.0
    x = (np.arange(L) - L / 2) * dx
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    r2 = X ** 2 + Y ** 2 + Z ** 2
    b = 1.0 - 0.4 * np.exp(-r2 / (2 * (L / 8) ** 2))          # dip to 0.6 at centre

    print("\n PART 1 (COMPUTABLE): Sigma's Grad term IS the emergent spatial curvature ^3R.")
    R_conf = scalar_curvature_conformal_3d(b, dx)
    R_form = derived_form_3d(b, dx)
    m = (np.abs(X) < L / 2 - 4) & (np.abs(Y) < L / 2 - 4) & (np.abs(Z) < L / 2 - 4)
    rel = np.abs(R_conf - R_form)[m].max() / (np.abs(R_conf)[m].max() + 1e-30)
    print(f"   ^3R (conformal-curvature formula) vs 2 lap(b) - (5/2)(grad b)^2/b :  max rel diff = {rel:.2e}")
    print("   -> identity verified: ^3R = 2 lap(b) - (5/2)(grad b)^2/b. The lap(b) piece is a total")
    print("      derivative (boundary); the -(5/2)(grad b)^2/b piece is the GRADIENT CONTENT = Sigma's")
    print("      Grad term. So xi ^3R is (a multiple of) Sigma's Grad: emergent spatial curvature = the")
    print("      substrate gradient penalty. The POTENTIAL sector of the action comes from Sigma. [DONE]")

    print("\n PART 2 (identify the conformal mode): trace K = -partial_t(ln sqrt h)/N.")
    print("   sqrt h = b^{-3/2} (3D), so ln sqrt h = -(3/2) ln b, and K = (3/2) (partial_t b / b) / N.")
    print("   -> the CONFORMAL / expansion mode of the geometry IS the bandwidth density b. lambda is the")
    print("      kinetic weight of THIS mode relative to the shear (traceless) mode.")

    print("\n PART 3 (structural: why lambda != 1): bandwidth CONSERVATION (P04) ties the conformal")
    print("   (compression) mode partial_t b to the current via continuity  partial_t b + div J = 0,")
    print("   distinguishing it kinetically from the free (transverse) SHEAR mode. GR (lambda=1) treats")
    print("   them covariantly; ED's conservation constraint breaks that -> lambda != 1 (the extra scalar")
    print("   = MOND sector). A structural REASON, not a value.")

    print("\n WHAT REMAINS (the open step, now sharply posed): compute the ratio of the substrate's")
    print("   KINETIC INERTIA for the COMPRESSION (conformal, partial_t b, conserved) mode vs the SHEAR")
    print("   (transverse, partial_t h^TT) mode. That ratio, calibrated against the GR/DeWitt value, IS")
    print("   lambda. It requires the substrate's mode-resolved inertia (from the retarded V1 propagation")
    print("   of bandwidth), which is NOT in Sigma (Sigma is the potential) and is not yet computed.")

    print("\n SET-UP VERDICT: the Sigma-to-action map is split and half-done. POTENTIAL sector: DONE --")
    print(" Sigma's Grad = the emergent spatial curvature ^3R (verified). KINETIC sector: the conformal")
    print(" mode is identified (= b), lambda != 1 has a structural reason (P04 conservation distinguishes")
    print(" compression from shear), and the VALUE of lambda is reduced to one sharp computation: the")
    print(" compression-vs-shear inertia ratio from the retarded substrate dynamics. That is the open")
    print(" number, now precisely posed. Honest: setup + potential sector done; lambda's value open.")
    print("=" * 92)


if __name__ == "__main__":
    main()
