"""
Rep-spectrum step-1 computation: does the point-gap winding of the N-channel
commitment map FIX the chirality casting (N=2 chiral, N=3 vector)?

Follows RepSpectrum_Step1_StabilityFormalism_*.md. The casting criterion there:
chirality = point-gap winding of the (non-Hermitian, arrow-carrying) commitment
map DT; nonzero => chiral, zero => vector. This lifts chiral_winding.py's 1+1D
scalar toy to N lanes, with the ONE forced constraint the corpus supplies:

  PARITY-CLEANNESS (the substrate has no reflection primitive, T4_09) means parity
  is a symmetry. Parity = (spatial reflection k -> -k) x (lane reflection S: i->N+1-i).
  For H(k) = e^{ik} A + e^{-ik} B to be parity-symmetric we need S H(k) S^-1 = H(-k),
  which FORCES the backward hop to be the mirror of the forward hop:  B = S A S^-1.
  A (the retarded forward cross-channel hop, the U(N) link P05 + arrow P11) is the
  only free structure; B is then fixed.

We compute the point-gap winding of det H(k) around E=0 for N=1..6, for many random
forward-hops A, in two regimes:
  (B) parity-CLEAN  : B = S A S^-1        (the substrate's actual rule)
  (C) orientation-BROKEN (SSB, gate i-a): B = eps * A   (one-way arrow, S broken)
and let the numbers say whether N fixes the casting. Honest: reports "no" if so.
"""
import numpy as np
rng = np.random.default_rng(11)

def winding_det(Hk, Nk=4000, E0=1e-6j):
    """Point-gap winding of det(H(k) - E0) around 0, k: 0->2pi.
    Tiny complex E0 regularizes a real spectrum off the reference point;
    it does not change the integer topology."""
    ks = np.linspace(0, 2*np.pi, Nk, endpoint=False)
    d = []
    for k in ks:
        M = Hk(k)
        d.append(np.linalg.det(M - E0*np.eye(M.shape[0])))
    d = np.array(d)
    if np.min(np.abs(d)) < 1e-12:
        return None
    d = np.append(d, d[0])
    return np.sum(np.diff(np.unwrap(np.angle(d)))) / (2*np.pi)

def S_reflect(N):
    """Lane reflection S: i -> N+1-i (anti-diagonal permutation)."""
    return np.eye(N)[::-1].copy()

def rand_link(N):
    """A random retarded forward cross-channel hop (generic non-normal N x N)."""
    return rng.standard_normal((N, N)) + 1j*rng.standard_normal((N, N))

# --------------------------------------------------------------------------
print("=== Part A: scalar sanity (reproduce chiral_winding.py Part A) ===")
for tR, tL, lab in [(1,1,"hermitian tR=tL"),(1,0,"one-way (arrow)"),(1,0.3,"asymmetric")]:
    w = winding_det(lambda k: np.array([[tR*np.exp(1j*k)+tL*np.exp(-1j*k)]]))
    print(f"  {lab:20s} winding = {w:+.3f}")
print("  -> matches toy: hermitian 0, one-way +/-1.\n")

# --------------------------------------------------------------------------
print("=== Part B: PARITY-CLEAN N-channel map  (B = S A S^-1, the substrate rule) ===")
print(f"  {'N':>2} {'p=ceil,q=floor':>16} {'winding (10 random forward-hops A)':>40}")
for N in range(1, 7):
    S = S_reflect(N)
    ws = []
    for _ in range(10):
        A = rand_link(N)
        B = S @ A @ np.linalg.inv(S)          # forced by parity-cleanness
        w = winding_det(lambda k: np.exp(1j*k)*A + np.exp(-1j*k)*B)
        if w is not None: ws.append(round(w))
    p, q = (N+1)//2, N//2
    print(f"  {N:>2} {f'({p},{q})':>16} {str(sorted(set(ws))):>40}")
print("  -> THEOREM (proven in note): det H(k)=det H(-k) is EVEN in k => the path")
print("     retraces itself => winding is EXACTLY 0 for ALL N. Parity-clean = VECTOR.\n")

# --------------------------------------------------------------------------
print("=== Part C: ORIENTATION-BROKEN (SSB, gate i-a)  B = eps*A, S-symmetry broken ===")
print(f"  {'N':>2} {'eps=0 (max SSB)':>16} {'eps=0.3':>12}")
for N in range(1, 7):
    def ws_for(eps):
        out = []
        for _ in range(10):
            A = rand_link(N)
            w = winding_det(lambda k: np.exp(1j*k)*A + eps*np.exp(-1j*k)*A)
            if w is not None: out.append(round(w))
        return sorted(set(out))
    print(f"  {N:>2} {str(ws_for(0.0)):>16} {str(ws_for(0.3)):>12}")
print("  -> broken case: winding = N (each lane winds once). MONOTONE in N, chiral for all N>=1.\n")

# --------------------------------------------------------------------------
print("=== VERDICT ===")
print("  SM casting to reproduce:   N=1 vector,  N=2 chiral,  N=3 vector   (NON-monotone)")
print("  parity-clean substrate:    winding=0 for ALL N        -> all VECTOR")
print("  orientation-broken (SSB):  winding=N for ALL N        -> all CHIRAL, monotone")
print("  Neither matches the non-monotone SM pattern {vector, chiral, vector}.")
print("  => The point-gap winding of the transport does NOT fix the casting.")
print("     The formalism's flagged PERMISSIVE risk is realized -- informatively:")
print("     clean=trivially-vector, broken=monotone-N; the SM's 'N=2 special' is")
print("     NOT a transport-winding fact. It is the rep-theory fact (SU(2) fundamental")
print("     pseudoreal, SU(N>=3) complex) that T4_12 already isolated. Casting is")
print("     REPRESENTATION-THEORETIC (inherited), not stability-dynamical.")
