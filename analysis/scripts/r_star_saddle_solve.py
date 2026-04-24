"""
Numerical 2D saddle solve for ED-SC 2.0 r* analytic chain closure.

Solves the Scenario-D saddle PDE (M2=0 leading order):
  d'' + d'/r = d - d^3/6    (radial ODE at M0=P0=1, P3=-1)

Looking for localized bounce: d(0)=d_max, d'(0)=0, d(r->inf)=0.

In 2D the Derrick constraint is int V d^2x = 0 with V = d^2/2 - d^4/24.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

M0, P0, P3, M2 = 1.0, 1.0, -1.0, 0.0

def rhs(r, y):
    d, dp = y
    if r < 1e-12:
        ddp = 0.5 * (d - d**3/6.0)
    else:
        ddp = -dp / r + d - d**3/6.0
    return [dp, ddp]

def end_value(d0, r_max=60.0):
    """Integrate, stop if d crosses 0 (overshoot) or d diverges."""
    def event_zero(r, y): return y[0]
    event_zero.terminal = True
    event_zero.direction = -1
    def event_blowup(r, y): return np.abs(y[0]) - 50
    event_blowup.terminal = True

    try:
        sol = solve_ivp(rhs, [1e-10, r_max], [d0, 0.0], method='RK45',
                        rtol=1e-11, atol=1e-13, max_step=0.02,
                        events=[event_zero, event_blowup])
    except Exception:
        return np.nan, None
    return sol.y[0, -1], sol

# Scan d_max over wide range to find bounce
print("Wide scan for 2D bounce d_max:")
d0_scan = np.linspace(2.5, 12.0, 60)
for d0 in d0_scan:
    end, sol = end_value(d0)
    final_r = sol.t[-1] if sol else 0
    tag = ""
    if sol and sol.t_events[0].size > 0: tag = "CROSSED_0"
    elif sol and sol.t_events[1].size > 0: tag = "BLOWUP"
    print(f"  d0={d0:6.3f}  d(r={final_r:6.2f})={end:10.4g}  {tag}")

# Look for the critical d0 where d just reaches 0 as r->inf.
# Scan finer in the physically relevant band.
def has_zero_crossing(d0):
    end, sol = end_value(d0, r_max=80.0)
    if sol is None: return False
    return sol.t_events[0].size > 0

# Binary search for smallest d0 that causes crossing.
lo, hi = 2.5, 12.0
# First, does lo cross and hi cross?
cl = has_zero_crossing(lo)
ch = has_zero_crossing(hi)
print(f"\nlo={lo} crosses={cl},  hi={hi} crosses={ch}")

d_max_crit = np.nan
if cl != ch:
    # bisect
    a, b = lo, hi
    for _ in range(50):
        m = 0.5*(a+b)
        cm = has_zero_crossing(m)
        if cm == cl:
            a = m
        else:
            b = m
        if abs(b-a) < 1e-8:
            break
    d_max_crit = 0.5*(a+b)
    print(f"\nCritical bounce amplitude d_max ~ {d_max_crit:.8f}")

# Fall back: just find d0 that gives a specific decay profile.
# For reporting: compute geometry at the "best" d0 found.
if np.isnan(d_max_crit):
    # Use Derrick's 2D constraint: int V(d(r)) 2 pi r dr = 0
    # Scan and evaluate integral.
    def derrick_int(d0):
        end, sol = end_value(d0, r_max=40.0)
        if sol is None or sol.t.size < 10: return np.nan
        r = sol.t
        d = sol.y[0]
        V = d**2/2 - d**4/24
        # Integrate V * 2*pi*r over r
        integrand = V * 2 * np.pi * r
        I = np.trapz(integrand, r)
        return I

    print("\nDerrick-integral scan:")
    d0_scan2 = np.linspace(2.5, 5.5, 30)
    derrick_vals = []
    for d0 in d0_scan2:
        I = derrick_int(d0)
        derrick_vals.append(I)
        print(f"  d0={d0:.3f}  int V dA = {I:.4g}")

    derrick_vals = np.array(derrick_vals)
    sign_changes = []
    for i in range(len(derrick_vals)-1):
        if np.isfinite(derrick_vals[i]) and np.isfinite(derrick_vals[i+1]):
            if derrick_vals[i] * derrick_vals[i+1] < 0:
                sign_changes.append((d0_scan2[i], d0_scan2[i+1]))
    print(f"Derrick sign-changes: {sign_changes}")
    if sign_changes:
        d_max_crit = brentq(derrick_int, sign_changes[0][0], sign_changes[0][1], xtol=1e-6)
        print(f"Derrick-critical d_max = {d_max_crit:.6f}")

# Extract geometry
if not np.isnan(d_max_crit):
    delta_max = d_max_crit
    # kappa_rad = d''(0) from radial PDE: 2*d''(0) = V'(d_max) = d_max - d_max^3/6
    kappa_rad = 0.5 * (delta_max - delta_max**3 / 6.0)
    epsilon = (delta_max**2 - 6.0) / 6.0
    mu = M0 + 0.5 * M2 * delta_max**2
    pi_coef = P0 + 0.5 * P3 * delta_max**2
    kappa_perp = kappa_rad
    kappa_par = kappa_rad
    chi = 2 * mu * kappa_perp**2 / P0
    r_star = -2*chi / (2*chi - 1) if abs(2*chi - 1) > 1e-9 else np.inf

    print("\n=== RADIAL BOUNCE GEOMETRY ===")
    print(f"  delta_max  = {delta_max:.6f}")
    print(f"  delta_max^2= {delta_max**2:.6f}")
    print(f"  epsilon    = {epsilon:.6f}")
    print(f"  kappa_rad  = {kappa_rad:.6f}")
    print(f"  |kappa_rad|^2 = {kappa_rad**2:.6f}")
    print(f"  mu         = {mu:.6f}")
    print(f"  pi         = {pi_coef:.6f}")
    print(f"  chi        = {chi:.6f}")
    print(f"  r* (radial)= {r_star:.6f}   (target -1.304)")

# Target inversion
target = -1.304
chi_t = target / (2 + 2*target)
k_t = np.sqrt(chi_t * P0 / (2 * M0))
print(f"\n=== TARGET INVERSION ===")
print(f"  r*=-1.304 needs chi = {chi_t:.6f}")
print(f"  kappa_perp_target^2 = {chi_t/2:.6f}   (at mu=1)")
print(f"  kappa_perp_target   = {k_t:.6f}")
