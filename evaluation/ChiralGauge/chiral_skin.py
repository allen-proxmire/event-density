"""
Pursuing the point-gap winding route (#2b).
Q: does the arrow's nonzero point-gap winding actually mean 'only one pattern/direction
allowed' -- a net chirality hermitian lattices forbid? Test the directional signature
(non-Hermitian skin effect + spectral flow) on finite chains. Could-say-no.
"""
import numpy as np

def chain_H(N, tR, tL):
    H = np.zeros((N, N), dtype=complex)
    for i in range(N-1):
        H[i+1, i] = tR      # hop to the right
        H[i, i+1] = tL      # hop to the left
    return H

print("=== Part C: does the arrow pick ONE direction? (open-chain eigenstate localization) ===")
print("  center-of-mass of |psi|^2 averaged over all modes; N=80, mid=39.5")
for tR, tL, lab in [(1.0,1.0,"hermitian  (tR=tL)"),(1.0,0.5,"retarded-biased"),(1.0,0.0,"one-way (full arrow)")]:
    N=80; H=chain_H(N,tR,tL); w,v=np.linalg.eig(H)
    coms=[np.sum(np.arange(N)*np.abs(vec)**2)/np.sum(np.abs(vec)**2) for vec in v.T]
    print(f"  {lab:22s} mean COM = {np.mean(coms):5.1f}   spread = {np.std(coms):4.1f}")
print("  -> hermitian: COM ~ mid, states extended (no preferred direction; L/R symmetric).")
print("  -> retarded:  COM -> one edge (skin effect): the arrow makes ALL modes pile one way.\n")

print("=== Part D: spectral flow under flux twist 0->2pi (the chiral-anomaly signature) ===")
print("  winding of the spectrum around E0=0 as a U(1) flux threads the ring (PBC):")
def ring_Hk(k, tR, tL):  # single-band ring dispersion with flux k
    return tR*np.exp(1j*k) + tL*np.exp(-1j*k)
def spectral_winding(tR, tL, N=8000):
    ks=np.linspace(0,2*np.pi,N,endpoint=False); v=ring_Hk(ks,tR,tL)
    v=np.append(v,v[0]); return np.sum(np.diff(np.unwrap(np.angle(v))))/(2*np.pi)
for tR,tL,lab in [(1,1,"hermitian"),(1,0,"one-way (arrow)"),(1,0.5,"retarded-biased")]:
    print(f"  {lab:18s} net spectral flow / winding = {spectral_winding(tR,tL):+.2f}")
print("  -> hermitian: 0 (anomaly-free, vector-like: states that flow up = states that flow down).")
print("  -> arrow:    +/-1 (net spectral flow = a chiral-anomaly signature = ONE net chirality).")
