"""Braiding dig — probe 1: is an order-holding link topologically held in 3D and erasable in 4D?

The hypothesis (Braiding_3D_CommitmentOrder_Hypothesis): ED's commitment-order is held by a
topological link/braid, and that holding is 3D-special — so the arrow forces 3 spatial dims.

CRANK-RAIL / honest subtlety this probe must expose: there are TWO different 3D-special facts,
and they give DIFFERENT dimension counts.
  (a) WORLDLINE BRAIDING (anyons): strands in (s_space + 1) SPACETIME braid only when the
      spacetime is 3D, i.e. s_space = 2. => predicts TWO spatial dimensions. (This is why
      anyons live in 2+1 D.) If "commitment-order = time-ordering of worldlines," the naive
      reading, the hypothesis would predict 2D -- a problem.
  (b) SPATIAL LINKING / KNOTTING: two 1-D loops link (codim-2) only in 3D SPACE; in 4D every
      link comes apart (lift one loop in the 4th coordinate, slide it past, lower it). => this
      is the fact that gives THREE spatial dimensions.

So for "why 3 spatial D," the held structure must be SPATIAL LINKING (b), not temporal
worldline-braiding (a). This probe tests (b) directly and quantitatively: take two loops linked
in 3D and ask whether they can be UNLINKED by a continuous, self-avoiding motion
  - in 3D (w-coordinate frozen at 0), vs
  - in 4D (the w-coordinate free).
Measure the minimum loop-to-loop distance along the unlinking attempt: if it must hit 0, the
loops had to pass through each other (no continuous unlink); if it stays > 0, they unlinked
freely. Linking number (Gauss integral) confirms linked->unlinked.

Could-say-no: if 4D does NOT unlink (min-dist still forced to 0) the codim-2 picture is wrong;
if 3D DOES unlink (min-dist stays >0) linking isn't held in 3D either. Honest either way. And
the result settles whether the hypothesis-as-written (note says "worldline braid->3D") needs
correcting to "spatial linking->3D."
"""
import numpy as np


def loopA(n=400):
    """unit circle in the xy-plane: (cos, sin, 0, 0)."""
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return np.stack([np.cos(t), np.sin(t), np.zeros(n), np.zeros(n)], axis=1)


def loopB(n=400, X=0.0, W=0.0):
    """circle radius 0.6 in the xz-plane, center (1+X, 0, 0, W) -- threaded through A at X=W=0."""
    p = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return np.stack([1 + X + 0.6 * np.cos(p), np.zeros(n), 0.6 * np.sin(p), np.full(n, W)], axis=1)


def min_dist(A, B):
    d = np.linalg.norm(A[:, None, :] - B[None, :, :], axis=2)
    return d.min()


def gauss_linking(A, B):
    """Gauss linking integral on the x,y,z components (w=0 configs): Lk in {...,-1,0,1,...}."""
    A3, B3 = A[:, :3], B[:, :3]
    dA = np.roll(A3, -1, 0) - A3
    dB = np.roll(B3, -1, 0) - B3
    Am = A3 + dA / 2
    Bm = B3 + dB / 2
    r = Am[:, None, :] - Bm[None, :, :]
    rn = np.linalg.norm(r, axis=2) ** 3 + 1e-12
    cross = np.cross(dA[:, None, :], dB[None, :, :])
    num = np.sum(r * cross, axis=2)
    return np.sum(num / rn) / (4 * np.pi)


def main():
    print("=" * 72)
    print("BRAIDING probe 1 — is a link held in 3D and erasable in 4D? (spatial linking)")
    print("=" * 72)
    A = loopA()

    Lk0 = gauss_linking(A, loopB(X=0.0, W=0.0))
    Lk_far = gauss_linking(A, loopB(X=1.6, W=0.0))
    print(f"\n  linking number:  start (X=0)  Lk = {Lk0:+.2f}   |   far (X=1.6, w=0)  Lk = {Lk_far:+.2f}")
    print("  (start linked, far position unlinked — the goal is to get there continuously, self-avoiding)")

    # --- 3D attempt: translate B in x, w frozen at 0 ---
    print("\n  3D unlinking attempt (w frozen = 0): translate B out in x")
    Xs = np.linspace(0.0, 1.6, 33)
    md3 = [min_dist(A, loopB(X=x, W=0.0)) for x in Xs]
    print(f"    min loop-loop distance along the path:  min over path = {min(md3):.3f}")
    print(f"    (dips to ~0 at X~0.6 => B must pass THROUGH A => no self-avoiding unlink in 3D)")

    # --- 4D attempt: lift in w, translate in x, lower in w ---
    print("\n  4D unlinking attempt (w free): lift B (w:0->1), translate x (0->1.6), lower (w:1->0)")
    Ws = np.linspace(0.0, 1.0, 12)
    md4 = []
    for w in Ws:                                   # lift at X=0
        md4.append(min_dist(A, loopB(X=0.0, W=w)))
    for x in np.linspace(0.0, 1.6, 33):            # translate at W=1
        md4.append(min_dist(A, loopB(X=x, W=1.0)))
    for w in Ws[::-1]:                             # lower at X=1.6
        md4.append(min_dist(A, loopB(X=1.6, W=w)))
    print(f"    min loop-loop distance along the path:  min over path = {min(md4):.3f}")
    print(f"    (stays > 0 => B slides past A through the 4th dimension, self-avoiding => unlinked)")

    print("\n" + "=" * 72)
    held_3d = min(md3) < 0.05
    free_4d = min(md4) > 0.1
    print(f"  3D: unlinking forces an intersection (min-dist -> 0)?  {held_3d}  => link HELD in 3D")
    print(f"  4D: unlinking stays self-avoiding (min-dist > 0)?      {free_4d}  => link ERASABLE in 4D")
    if held_3d and free_4d:
        print("  VERDICT: spatial linking (codim-2) is held in 3D, erasable in 4D — the 3-spatial-D")
        print("           fact. The order-holding structure must be SPATIAL LINKING, not worldline")
        print("           braiding (which is a 2-spatial-D / anyon phenomenon) — corrects the note.")
    else:
        print("  VERDICT: codim-2 linking picture NOT confirmed as written — hypothesis needs rework.")
    print("=" * 72)


if __name__ == "__main__":
    main()
