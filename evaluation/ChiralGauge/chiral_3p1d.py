"""
Relativistic bridge, first check: does the arrow's doubler-lifting survive to 3+1D?
Count massless gap-closings (zeros of |D(p)|^2) over the 4D Brillouin zone for the naive
HERMITIAN lattice Dirac vs the RETARDED forward-difference. (Necessary-not-sufficient: a
clean undoubling is required, but whether the survivor is CHIRAL vs VECTOR-LIKE is the
harder, open part this does NOT settle.)
"""
import numpy as np
import itertools

def count_zeros_4d(comp, M=24, tol=1e-3):
    # |D(p)|^2 = sum_mu |comp(p_mu)|^2 over the 4D BZ; count grid points below tol
    grid = np.linspace(0, 2*np.pi, M, endpoint=False)
    zeros = 0; locs=[]
    for p in itertools.product(grid, repeat=4):
        val = sum(abs(comp(pm))**2 for pm in p)
        if val < tol:
            zeros += 1; locs.append(tuple(round(x,2) for x in p))
    return zeros, locs

# naive hermitian:  D_mu ~ sin(p_mu)           (central difference)
# retarded forward: D_mu ~ e^{i p_mu} - 1       (one-way; contains a free Wilson term)
herm = lambda pm: np.sin(pm)
retd = lambda pm: np.exp(1j*pm) - 1.0
nz_h, _ = count_zeros_4d(herm)
nz_r, locs_r = count_zeros_4d(retd)
print("=== 3+1D doubler count (zeros of |D(p)|^2 over the 4D BZ) ===")
print(f"  hermitian naive (sin):     {nz_h:3d} zeros   (expect 16 = 2^4 doublers)")
print(f"  retarded forward (arrow):  {nz_r:3d} zero(s) at {locs_r}   (expect 1 at origin)")
print()
print("  -> the arrow undoubles in 3+1D exactly as in 1+1D: 16 -> 1.")
print("     Necessary (no mirror army), NOT sufficient: whether that single survivor is a")
print("     CHIRAL Weyl point or a VECTOR-LIKE Dirac point is the open relativistic question.")
