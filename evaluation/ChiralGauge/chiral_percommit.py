"""
Per-commitment chirality (AP's route). The transport route gives a vector-like survivor
in 3+1D (the 1+1D chirality was dimension-special). So locate the handedness where AP
says it lives: in the commitment EVENTS. Model chirality as the winding of the P09 phase
along the commitment sequence (a helix/screw). Decisive question: does first-arrival
LOCK the sign of the phase-advance (=> net winding => handedness), or does P11
randomization wash it out (=> net 0 => vector-like)?
"""
import numpy as np
rng = np.random.default_rng(7)
N = 200000

def net_winding(locked, drift, noise):
    if locked:                       # first-arrival: every commitment advances the same way
        sign = np.ones(N)
    else:                            # unlocked: each commitment picks its own handedness
        sign = rng.choice([-1.0, 1.0], size=N)
    dphi = sign*drift + noise*rng.standard_normal(N)   # P11 randomization = the noise
    phi = np.cumsum(dphi)
    return (phi[-1]-phi[0])/N/(2*np.pi)                # net winding per commitment

print("=== Per-commitment handedness = net winding of the P09 phase along the arrow ===")
print(f"  {'case':34s}{'drift':>7}{'noise(P11)':>12}{'net winding/step':>18}")
for locked, drift, noise, lab in [
    (True , 0.30, 1.0, "LOCKED (first-arrival), strong P11 noise"),
    (True , 0.05, 1.0, "LOCKED, tiny drift, strong P11 noise"),
    (True , 0.30, 5.0, "LOCKED, huge P11 noise"),
    (False, 0.30, 1.0, "UNLOCKED (random sign per commit)"),
    (False, 0.30, 0.0, "UNLOCKED, no noise at all"),
]:
    w = net_winding(locked, drift, noise)
    print(f"  {lab:34s}{drift:>7.2f}{noise:>12.1f}{w:>18.4f}")
print()
print("  Reading:")
print("  - LOCKED: net winding ~ drift, ROBUST to P11 randomization (noise averages out of")
print("    the SUM; drift grows ~N, noise ~sqrt(N)). Even a tiny locked drift => net handedness.")
print("  - UNLOCKED: net winding ~ 0 regardless of noise -> vector-like (no handedness).")
print("  => the ONLY thing that matters is whether the sign of phase-advance is LOCKED.")
print("     First-arrival lock-in (the SAME mechanism ED baryogenesis already needs for")
print("     matter>antimatter) supplies exactly that lock. So parity violation and the")
print("     matter/antimatter asymmetry would be ONE handed-commitment lock-in. [hypothesis]")
