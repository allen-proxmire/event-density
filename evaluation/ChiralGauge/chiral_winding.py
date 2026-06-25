"""
#2b continuum-limit chirality — toy-model computation (follow-on to SQ1).

Honest scope: the full substrate-V1 -> Dirac coarse-graining is OPEN (T4), and ED has
no global Brillouin torus, so this does NOT compute a relativistic net chirality. It
isolates the one mechanism SQ1's hypothesis turns on: does ED's RETARDED (one-way, arrow)
transport do what hermitian lattices cannot -- carry unpaired chirality / lift the
Nielsen-Ninomiya doublers? We test two 1D toy models and let them answer, including no.
"""
import numpy as np

def winding(Hk, E0=0.0, N=6000):
    """Point-gap winding number of the complex curve H(k) around reference E0."""
    ks = np.linspace(0, 2*np.pi, N, endpoint=False)
    v = np.array([Hk(k) for k in ks]) - E0
    v = np.append(v, v[0])                       # close the loop
    return np.sum(np.diff(np.unwrap(np.angle(v)))) / (2*np.pi)

# ---------- Part A: scalar Hatano-Nelson, point-gap winding around E=0 ----------
# H(k) = tR e^{ik} + tL e^{-ik}.  Hermitian iff tR = tL.
def Hk_scalar(k, tR, tL): return tR*np.exp(1j*k) + tL*np.exp(-1j*k)
print("=== Part A: scalar point-gap winding around E=0 (non-hermitian topology) ===")
for tR, tL, lab in [(1,1,"hermitian  tR=tL"),(1,0,"one-way R (retarded)"),
                    (0,1,"one-way L"),(1,0.3,"asymmetric")]:
    w = winding(lambda k: Hk_scalar(k, tR, tL))
    print(f"  {lab:22s}  winding = {w:+.3f}   (rounded {int(round(w))})")
print("  -> hermitian: real spectrum, winding 0 (doublers must pair).")
print("  -> one-way (arrow-like): winding +/-1  => non-hermitian topology is nonzero.\n")

# ---------- Part B: 1D lattice 'Dirac' dispersion, doubler count ----------
# Massless gap-closings ('Weyl points') = real-axis zeros of the 1-component dispersion d(k).
#   naive central difference (HERMITIAN):  d(k) = i*sin(k)        |d|^2 = sin^2 k
#   retarded forward difference          :  d(k) = e^{ik} - 1      |d|^2 = 2(1-cos k)
def d_central(k):  return 1j*np.sin(k)
def d_forward(k):  return np.exp(1j*k) - 1.0
def count_real_zeros(d, N=200000, tol=1e-4):
    ks = np.linspace(0, 2*np.pi, N, endpoint=False)
    a = np.abs(np.array([d(k) for k in ks]))**2
    # local minima below tol
    zeros = [ks[i] for i in range(N) if a[i] < tol and a[i] <= a[i-1] and a[i] <= a[(i+1)%N]]
    # cluster nearby hits
    out=[]
    for z in zeros:
        if not out or min(abs(z-o) for o in out) > 0.1: out.append(round(z,3))
    return out
print("=== Part B: lattice-Dirac doublers (real-axis gap closings) ===")
zc = count_real_zeros(d_central);  zf = count_real_zeros(d_forward)
print(f"  central (hermitian) zeros at k = {zc}   -> {len(zc)} modes  (k=0 and k=pi: the DOUBLER)")
print(f"  forward (retarded)  zeros at k = {zf}   -> {len(zf)} mode   (pi-doubler LIFTED off real axis)")
# show the retarded difference = central + Wilson term
wilson = lambda k: (np.exp(1j*k)-1) - 1j*np.sin(k)   # = cos k - 1
print(f"  forward = central + (cos k - 1):  Wilson term at k=pi = {wilson(np.pi).real:+.1f}  (the doubler mass)")
print("  -> the arrow's retarded transport IS a Wilson term: it lifts the doubler for free.")
print("  -> BUT Wilson-style lifting breaks chiral symmetry -> a single VECTOR-LIKE fermion,")
print("     not a chiral one. Undoubling != handedness.")
