"""
ED Scattering Sweep: shared-field two-core experiment.
Uses connected-component blob detection (matching original detect_cores logic).
Token-safe: one summary line per (b, v) + two tables.
"""
import sys, numpy as np

ED_PATH = r'C:\Users\allen\GitHub\Event Density\ED Simulations'
sys.path.insert(0, ED_PATH)
from ED_Update_Rule import ed_step_mobility

from scipy.ndimage import label, center_of_mass, shift as ndshift

# ── CoreType-QM1 fixed parameters ─────────────────────────────────────────────
GRID     = 100
ALPHA    = 0.001
GAMMA    = 0.50
DT       = 0.1
P_MIN    = 0.01
P_MAX    = 1.0
R_CORE   = 8.0
AMP      = 0.9
BG       = 0.10
MOB_EXP  = 1.0
BOUNDARY = 'periodic'
D0       = 40
CX, CY   = 50, 50

PART_SIG = 1.5 * R_CORE      # soft-partition sigma
THRESH   = 0.50 * P_MAX       # connected-component threshold (matches orig detect_cores)

ri, ci = np.ogrid[0:GRID, 0:GRID]

# ── Field utilities ───────────────────────────────────────────────────────────
def init_field(b_px):
    cA, cB = float(CX - D0//2), float(CX + D0//2)
    rA, rB = float(CY), float(CY + b_px)
    dA2 = (ri-rA)**2 + (ci-cA)**2
    dB2 = (ri-rB)**2 + (ci-cB)**2
    p = np.clip(BG + AMP*np.exp(-dA2/(2*R_CORE**2))
                   + AMP*np.exp(-dB2/(2*R_CORE**2)), P_MIN, P_MAX)
    return p, (rA, cA), (rB, cB)

def soft_partition(p, posA, posB):
    rA, cA = posA; rB, cB = posB
    wA = np.exp(-((ri-rA)**2+(ci-cA)**2) / (2*PART_SIG**2))
    wB = np.exp(-((ri-rB)**2+(ci-cB)**2) / (2*PART_SIG**2))
    fA = wA / (wA + wB + 1e-30)
    return p*fA, p*(1.0-fA)

def advect(p, dc):
    return np.clip(ndshift(p, [0.0, dc], mode='wrap',
                            order=1, prefilter=False), P_MIN, P_MAX)

def detect_cores(p):
    """
    Connected-component blob detection above THRESH.
    Matches original detect_cores(p, p_max) from Scenario_E_TwoCore.
    Returns list of (row, col) centroids sorted left-to-right, max 2.
    """
    mask        = p > THRESH
    labeled, n  = label(mask)
    if n == 0:
        return []
    # Weighted centroids (by density)
    blobs = []
    for k in range(1, n + 1):
        region = (labeled == k)
        w   = p[region]
        idx = np.argwhere(region)
        r_c = float((w * idx[:,0]).sum() / w.sum())
        c_c = float((w * idx[:,1]).sum() / w.sum())
        blobs.append((r_c, c_c))
    # Sort left-to-right; keep top-2 by size if more than 2 components
    if n > 2:
        sizes = [(p[labeled == k].sum(), k) for k in range(1, n+1)]
        sizes.sort(reverse=True)
        keep = {sizes[0][1], sizes[1][1]}
        blobs = [(r,c) for k,(r,c) in enumerate(blobs, 1) if k in keep]
    blobs.sort(key=lambda rc: rc[1])   # left-to-right by column
    return blobs

def track(blobs, prevA, prevB):
    """Nearest-neighbour assign to (A, B). Returns (newA, newB, n_blobs)."""
    n = len(blobs)
    if n == 0: return prevA, prevB, 0
    if n == 1: return blobs[0], blobs[0], 1
    b0, b1 = blobs[0], blobs[1]
    d_dir = (np.hypot(b0[0]-prevA[0], b0[1]-prevA[1]) +
             np.hypot(b1[0]-prevB[0], b1[1]-prevB[1]))
    d_crs = (np.hypot(b1[0]-prevA[0], b1[1]-prevA[1]) +
             np.hypot(b0[0]-prevB[0], b0[1]-prevB[1]))
    return (b0,b1,2) if d_dir <= d_crs else (b1,b0,2)

def defl_angle(traj, v_col_sign, n_valid):
    """Deflection angle over last 10% of valid (pre-merge) trajectory."""
    n = min(n_valid, len(traj))
    if n < 4: return 0.0
    tail = max(2, n//10)
    dr = traj[n-1][0] - traj[n-1-tail][0]
    dc = traj[n-1][1] - traj[n-1-tail][1]
    mag = np.hypot(dr, dc)
    if mag < 1e-6: return 0.0
    cos_a = np.clip((v_col_sign * dc) / mag, -1.0, 1.0)
    return float(np.degrees(np.arccos(cos_a)))

def classify_outcome(traj_A, traj_B, merge_step, n_steps):
    """Determine MERGE / BIND / SCATTER / PASS."""
    if merge_step is not None:
        return 'MERGE'
    # Two blobs survived: check final trajectory
    cA0, cB0 = traj_A[0][1],  traj_B[0][1]
    cAf, cBf = traj_A[-1][1], traj_B[-1][1]
    if (cA0 < cB0 and cAf > cBf) or (cA0 > cB0 and cAf < cBf):
        return 'PASS'
    tail = max(2, len(traj_A)//5)
    d0 = np.hypot(traj_A[-tail][0]-traj_B[-tail][0],
                  traj_A[-tail][1]-traj_B[-tail][1])
    d1 = np.hypot(traj_A[-1][0]-traj_B[-1][0],
                  traj_A[-1][1]-traj_B[-1][1])
    return 'SCATTER' if d1 > d0 * 1.15 else 'BIND'

# ── Single run ─────────────────────────────────────────────────────────────────
def run_one(b_px, v):
    SHIFT   = v
    t_CA    = int(D0 / (2.0 * SHIFT))
    STEPS   = min(500, max(300, t_CA * 2))

    p, posA, posB = init_field(b_px)
    cA, cB  = list(posA), list(posB)
    traj_A  = [tuple(cA)]
    traj_B  = [tuple(cB)]
    d_min   = float('inf')
    d_min_step  = 0
    merge_step  = None
    n_valid_A   = 0    # last step where both blobs were tracked

    for step in range(1, STEPS + 1):
        # 1. Shared-field ED update
        p = ed_step_mobility(p, alpha=ALPHA, gamma=GAMMA, dt=DT,
                             p_min=P_MIN, p_max=P_MAX,
                             boundary=BOUNDARY, mobility_exp=MOB_EXP)
        # 2. Soft partition → advect → recombine
        pA, pB = soft_partition(p, tuple(cA), tuple(cB))
        p = np.clip(advect(pA, +SHIFT) + advect(pB, -SHIFT), P_MIN, P_MAX)

        # 3. Detect connected-component blobs
        blobs = detect_cores(p)
        nA, nB, n_blobs = track(blobs, tuple(cA), tuple(cB))

        if n_blobs < 2:
            # Merge detected
            merge_step = step
            d_at_merge = np.hypot(cA[0]-cB[0], cA[1]-cB[1])
            if d_at_merge < d_min:
                d_min, d_min_step = d_at_merge, step
            traj_A.append(tuple(cA))   # freeze position at merge
            traj_B.append(tuple(cB))
            n_valid_A = step
            break

        cA, cB = list(nA), list(nB)
        traj_A.append(tuple(cA))
        traj_B.append(tuple(cB))
        n_valid_A = step

        d = np.hypot(cA[0]-cB[0], cA[1]-cB[1])
        if d < d_min:
            d_min, d_min_step = d, step

    outcome = classify_outcome(traj_A, traj_B, merge_step, STEPS)
    tA = defl_angle(traj_A, +1, n_valid_A)
    tB = defl_angle(traj_B, -1, n_valid_A)
    t_ev = merge_step if outcome == 'MERGE' else (d_min_step if outcome == 'BIND' else None)
    return outcome, d_min, tA, tB, t_ev

# ── Sweep ──────────────────────────────────────────────────────────────────────
b_values = [0, 5, 10, 15, 20, 25, 30]
v_values = [0.05, 0.10, 0.20, 0.30]

print('=== ED Scattering Sweep  (Shared-Field, CoreType-QM1) ===')
print('alpha=0.001  gamma=0.50  R=8px  D0=40px  grid=100x100')
print('Blob detection: connected-components above 0.50*P_MAX')
print()

results = {}
for v in v_values:
    for b in b_values:
        outcome, d_min, tA, tB, t_ev = run_one(b, v)
        results[(b, v)] = (outcome, d_min, tA, tB, t_ev)
        t_str = '%d' % t_ev if t_ev is not None else '--'
        print('(b=%2d, v=%.2f): %-7s  D_min=%5.2f  thetaA=%5.1f  thetaB=%5.1f  t_event=%s'
              % (b, v, outcome, d_min, tA, tB, t_str))
        sys.stdout.flush()

# ── Table 1: Classification grid ──────────────────────────────────────────────
print()
print('=== TABLE 1: Outcome Classification ===')
hdr = '      b\\v |' + ''.join([' v=%.2f ' % v for v in v_values])
print(hdr)
print('-' * len(hdr))
for b in b_values:
    row = '  b=%2d   |' % b
    for v in v_values:
        row += ' %-7s' % results[(b,v)][0]
    print(row)

# ── Table 2: Critical boundary b_c(v) ────────────────────────────────────────
print()
print('=== TABLE 2: Critical Capture Boundary b_c(v) ===')
print('  b_c = largest b giving MERGE; transition above')
for v in v_values:
    bc_list = [b for b in b_values if results[(b,v)][0] == 'MERGE']
    bc = max(bc_list) if bc_list else None
    if bc is not None and bc < b_values[-1]:
        nb = b_values[b_values.index(bc)+1]
        print('  v=%.2f:  b_c in [%2d, %2d) px   b_c/R in [%.2f, %.2f)'
              % (v, bc, nb, bc/R_CORE, nb/R_CORE))
    elif bc is not None:
        print('  v=%.2f:  b_c >= %d px  (all tested b give MERGE)' % (v, bc))
    else:
        print('  v=%.2f:  b_c < 0  (no MERGE found in tested range)' % v)

print()
print('Done.')
