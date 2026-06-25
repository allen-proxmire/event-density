"""
#2b unitarity/sparsity bridge: is the arrow's net chirality SUPPRESSED by sparse
commitment (like alpha_1), or TOPOLOGICAL and robust (quantized, survives any nonzero
commitment)?  Model sparse commitment as a small effective one-way bias epsilon on an
otherwise hermitian (unitary) transport.  Compute the point-gap winding vs epsilon.
"""
import numpy as np

def winding(tR, tL, N=40000):
    k = np.linspace(0, 2*np.pi, N, endpoint=False)
    v = tR*np.exp(1j*k) + tL*np.exp(-1j*k)
    v = np.append(v, v[0])
    return np.sum(np.diff(np.unwrap(np.angle(v)))) / (2*np.pi)

print("=== Net chirality (point-gap winding) vs commitment sparsity epsilon ===")
print("  tR = 1+eps, tL = 1-eps ;  eps ~ effective one-way bias ~ commitment sparsity")
print(f"  {'epsilon':>10} {'winding':>10}   reading")
for eps in [0.5, 0.1, 0.01, 1e-3, 1e-4, 1e-5, 0.0]:
    w = winding(1+eps, 1-eps)
    rd = "TOPOLOGICAL: full +/-1 chirality" if abs(round(w))==1 else ("GR limit: no chirality" if eps==0 else "?")
    print(f"  {eps:>10.0e} {w:>10.3f}   {rd}")
print()
print("  Reading:")
print("  - winding = +1 for EVERY eps>0, however tiny: the chirality is QUANTIZED/topological.")
print("  - it drops to 0 ONLY at eps=0 exactly (no arrow -> GR/vector-like).")
print("  - so sparse commitment preserves the FULL chirality (a topological +/-1), it does NOT")
print("    suppress it the way it suppresses alpha_1 (a non-topological coupling ~ eps).")
print("  => maximal parity violation is COMPATIBLE with sparse commitment, precisely because")
print("     chirality is topological while alpha_1 is not.  Same sparse-commitment fact,")
print("     opposite fates: chirality stays +/-1, alpha_1 ~ eps -> tiny.")
