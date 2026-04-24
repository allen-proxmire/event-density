"""ED-SC 3.4-σ₁ F3-verify driver (MLE Student-t fit on raw T_motif).

Pre-registered in theory/GR_SC_1_3_RayleighClass_ModelCorrection_Verify.md.

Regenerates the F2 multi-seed `T_motif` pool deterministically by
re-running the ED-SC 3.4-σ₁ Multi-Seed evolution pipeline (the F2
summary JSON did not persist raw T_motif values), then performs
maximum-likelihood Student-t fitting on the pooled ~850-motif
sample. Emits refined ν estimate with Hessian-based uncertainty,
K-S goodness-of-fit test, and updated κ correction factor /
model band.

Simulator of record:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility

This driver performs NO new lattice physics — it regenerates the
F2 fields under identical canonical parameters and canonical
seeds, re-extracts T_motif, then runs MLE + K-S on the pooled
sample. Student-t fitting via scipy.stats.t.fit; Hessian via
numerical differentiation of the negative log-likelihood; K-S
test via scipy.stats.kstest.

Writes:
  outputs/ed_sc_3_4_sigma1/sigma1_model_verify_table.csv
  outputs/ed_sc_3_4_sigma1/sigma1_model_verify_summary.json

No simulator constants are mutated. Deterministic given seeds.
"""
import csv
import json
import math
import os
import sys
import time
import numpy as np
from numpy.fft import fft2, ifft2, fftshift
from scipy import stats, optimize

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "ed_arch_r2"))
import r2_grf_falsifier_tests as fr  # noqa: E402

from ED_Update_Rule import ed_step_mobility  # noqa: E402

# ---------------------------------------------------------------------------
# Canonical constants (inherited from F2 driver verbatim)
# ---------------------------------------------------------------------------
XI_CANONICAL = 1.7575325729470939
XI_BURN_IN = 100
XI_SNAP_EVERY = 10

ALPHA_FILT = 0.25
N_REQ = 4
DIMLESS_HINGE = 1.08
DIAG_COS = 0.707

WINDOW_A = (2.50, 2.80)
WINDOW_B = (3.50, 3.90)

XI_TARGET = 1.7575
SEEDS = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

CALIBRATION_W_GRID = [0.05, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35]
CALIBRATION_TOL = 0.01

# F3 comparison constants
NU_F3_SUMMARY = 30
NU_F3_ENVELOPE = [20, 50]
MODEL_BAND_F3_REL = 0.0161
KAPPA_CENTRAL_PREF3 = 0.001828  # Gaussian Rayleigh central

# K-S pass threshold
KS_PASS_PVALUE = 0.05

OUT_DIR = os.path.join(HERE, "..", "..", "outputs", "ed_sc_3_4_sigma1")


# ---------------------------------------------------------------------------
# ξ measurement (verbatim)
# ---------------------------------------------------------------------------
def xi_halfdecay(field, dx=1.0):
    N = field.shape[0]
    f = field - np.mean(field)
    F = fft2(f)
    C = fftshift(np.real(ifft2(F * np.conj(F)))) / (N * N)
    c0 = C[N // 2, N // 2]
    if c0 <= 0:
        return float('nan')
    y, x = np.indices(C.shape)
    r = np.sqrt((x - N // 2) ** 2 + (y - N // 2) ** 2).astype(int)
    rmax = N // 2
    prof = np.empty(rmax)
    for k in range(rmax):
        mask = (r == k)
        prof[k] = C[mask].mean() if mask.any() else 0.0
    prof /= c0
    for k in range(1, rmax):
        if prof[k] <= 0.5:
            if prof[k - 1] == prof[k]:
                return float(k) * dx
            return float(k - 1 + (prof[k - 1] - 0.5)
                         / (prof[k - 1] - prof[k])) * dx
    return float(rmax) * dx


def evolve_40snap(seed, w):
    rng = np.random.default_rng(seed)
    p = rng.uniform(0.5 - w, 0.5 + w, size=(fr.SIZE, fr.SIZE))
    snaps = []
    xis = []
    for step in range(fr.STEPS):
        p = ed_step_mobility(
            p, alpha=fr.ALPHA0, gamma=fr.GAMMA, dt=fr.DT,
            p_min=fr.P_MIN, p_max=fr.P_MAX, boundary=fr.BOUNDARY,
            mobility_exp=fr.MOBILITY_EXP, noise_scale=fr.NOISE0, rng=rng,
        )
        if step >= XI_BURN_IN and (step - XI_BURN_IN) % XI_SNAP_EVERY == 0:
            snaps.append(p.copy())
            xis.append(xi_halfdecay(p))
    return snaps, xis


def run_calibration_for_seed(seed):
    results = []
    for w in CALIBRATION_W_GRID:
        _, xis = evolve_40snap(seed, w)
        xi_mean = float(np.mean([x for x in xis if np.isfinite(x)]))
        results.append({"w": w, "xi": xi_mean})
    results.sort(key=lambda r: r["xi"])
    return results


def interpolate_w(calibration, xi_target):
    xs = [r["xi"] for r in calibration]
    ws = [r["w"] for r in calibration]
    if xi_target <= xs[0]:
        return ws[0]
    if xi_target >= xs[-1]:
        return ws[-1]
    for i in range(len(xs) - 1):
        if xs[i] <= xi_target <= xs[i + 1]:
            a = (xi_target - xs[i]) / (xs[i + 1] - xs[i])
            return ws[i] * (1 - a) + ws[i + 1] * a
    return ws[-1]


def in_window(L, win):
    return win[0] <= L <= win[1]


def r_diag_of(L):
    return int(round(DIAG_COS * L))


# ---------------------------------------------------------------------------
# Motif extraction with T_motif recording
# ---------------------------------------------------------------------------
def collect_T_40snap(snapshots, L_ray):
    all_T = []
    for p in snapshots:
        E = fr.smooth_field(p)
        p_hat = float(p.mean())
        p_std = float(p.std())
        sads = fr.find_morse_saddles(E)
        for s in sads:
            if not fr.motif_pass(s, E, p_hat, p_std,
                                 ALPHA_FILT, L_ray, N_REQ):
                continue
            T = float(s["lam_neg"]) + float(s["lam_pos"])
            all_T.append(T)
    return all_T


def run_seed_T_extraction(seed):
    t_seed = time.time()
    print(f"Seed {seed} — calibration + evolution...", file=sys.stderr)
    calibration = run_calibration_for_seed(seed)
    w = interpolate_w(calibration, XI_TARGET)

    snapshots, xis = evolve_40snap(seed, w)
    xi_finite = [x for x in xis if np.isfinite(x)]
    xi_measured = float(np.mean(xi_finite)) if xi_finite else float('nan')
    miss = abs(xi_measured - XI_TARGET) / XI_TARGET

    if miss > CALIBRATION_TOL and xi_finite:
        if xi_measured < XI_TARGET:
            w_new = max(min(CALIBRATION_W_GRID), w * 0.85)
        else:
            w_new = min(max(CALIBRATION_W_GRID), w * 1.15)
        snapshots_new, xis_new = evolve_40snap(seed, w_new)
        xi_finite_new = [x for x in xis_new if np.isfinite(x)]
        xi_new = (float(np.mean(xi_finite_new))
                  if xi_finite_new else xi_measured)
        miss_new = abs(xi_new - XI_TARGET) / XI_TARGET
        if miss_new < miss:
            w = w_new
            xi_measured = xi_new
            snapshots = snapshots_new
            miss = miss_new

    L_ray = DIMLESS_HINGE * xi_measured
    if in_window(L_ray, WINDOW_A) or in_window(L_ray, WINDOW_B):
        raise RuntimeError(
            f"seed {seed}: L_ray={L_ray:.4f} intersects a resonance window.")
    r_diag = r_diag_of(L_ray)
    out_of_scope = (r_diag != 1)

    T_list = collect_T_40snap(snapshots, L_ray)
    print(f"  seed={seed}  ξ_meas={xi_measured:.4f}  "
          f"L_ray={L_ray:.4f}  r_diag={r_diag}  "
          f"N_T={len(T_list)}  t={time.time()-t_seed:.1f}s",
          file=sys.stderr)
    return {
        "seed": seed,
        "xi_measured": xi_measured,
        "xi_miss_fraction": miss,
        "w_used": w,
        "L_ray": L_ray,
        "r_diag": r_diag,
        "out_of_scope": out_of_scope,
        "N_T": len(T_list),
        "T_list": T_list,
    }


# ---------------------------------------------------------------------------
# MLE Student-t fit + Hessian
# ---------------------------------------------------------------------------
def neg_log_likelihood_t(params, data):
    nu, mu, sigma = params
    if nu <= 2 or sigma <= 0:
        return np.inf
    return -np.sum(stats.t.logpdf(data, df=nu, loc=mu, scale=sigma))


def mle_fit_student_t(data):
    """Run MLE Student-t fit. Returns (nu, mu, sigma, ll_final)."""
    # scipy built-in fit (fast; uses method-of-moments initialization)
    nu_sp, mu_sp, sigma_sp = stats.t.fit(data)
    ll_sp = -neg_log_likelihood_t((nu_sp, mu_sp, sigma_sp), data)

    # Custom fit via L-BFGS-B with bounds (consistency check)
    def nll(params):
        return neg_log_likelihood_t(params, data)
    bounds = [(2.01, 500.0), (None, None), (1e-8, None)]
    result_cu = optimize.minimize(
        nll, x0=[nu_sp, mu_sp, sigma_sp], method="L-BFGS-B", bounds=bounds)
    nu_cu, mu_cu, sigma_cu = result_cu.x
    ll_cu = -result_cu.fun

    # Take the better of the two
    if ll_cu >= ll_sp:
        nu, mu, sigma, ll_final = nu_cu, mu_cu, sigma_cu, ll_cu
        optimizer_used = "L-BFGS-B"
    else:
        nu, mu, sigma, ll_final = nu_sp, mu_sp, sigma_sp, ll_sp
        optimizer_used = "scipy.stats.t.fit"
    return {
        "nu": float(nu), "mu": float(mu), "sigma": float(sigma),
        "log_likelihood": float(ll_final),
        "optimizer": optimizer_used,
        "scipy_fit": {"nu": float(nu_sp), "mu": float(mu_sp),
                      "sigma": float(sigma_sp), "ll": float(ll_sp)},
        "custom_fit": {"nu": float(nu_cu), "mu": float(mu_cu),
                       "sigma": float(sigma_cu), "ll": float(ll_cu)},
    }


def hessian_at_optimum(params, data, eps_frac=1e-4):
    """Numerical Hessian of the negative log-likelihood at params.
    Returns 3x3 matrix in (ν, μ, σ) order."""
    nu, mu, sigma = params
    eps = np.array([eps_frac * abs(nu), eps_frac * abs(mu) + 1e-8,
                    eps_frac * abs(sigma)])
    p0 = np.array(params)
    H = np.zeros((3, 3))
    f0 = neg_log_likelihood_t(p0, data)
    for i in range(3):
        for j in range(3):
            if i == j:
                pp = p0.copy(); pp[i] += eps[i]
                pm = p0.copy(); pm[i] -= eps[i]
                f_p = neg_log_likelihood_t(pp, data)
                f_m = neg_log_likelihood_t(pm, data)
                H[i, j] = (f_p - 2 * f0 + f_m) / (eps[i] ** 2)
            else:
                ppp = p0.copy(); ppp[i] += eps[i]; ppp[j] += eps[j]
                ppm = p0.copy(); ppm[i] += eps[i]; ppm[j] -= eps[j]
                pmp = p0.copy(); pmp[i] -= eps[i]; pmp[j] += eps[j]
                pmm = p0.copy(); pmm[i] -= eps[i]; pmm[j] -= eps[j]
                f_pp = neg_log_likelihood_t(ppp, data)
                f_pm = neg_log_likelihood_t(ppm, data)
                f_mp = neg_log_likelihood_t(pmp, data)
                f_mm = neg_log_likelihood_t(pmm, data)
                H[i, j] = (f_pp - f_pm - f_mp + f_mm) / (4 * eps[i] * eps[j])
    return H


def nu_sigma_from_hessian(H):
    """Invert Hessian and return sqrt of (1,1) element (ν marginal σ).
    Returns None if matrix is not positive definite."""
    try:
        cov = np.linalg.inv(H)
    except np.linalg.LinAlgError:
        return None, None
    if cov[0, 0] <= 0:
        return None, cov.tolist()
    return float(math.sqrt(cov[0, 0])), cov.tolist()


# ---------------------------------------------------------------------------
# Scale factor and model band
# ---------------------------------------------------------------------------
def scale_factor(nu):
    if nu <= 2:
        return None
    return math.sqrt((nu - 2) / nu)


def scale_factor_band(nu_fit, nu_sigma):
    if nu_sigma is None:
        return None, None
    nu_lo = max(2.01, nu_fit - nu_sigma)
    nu_hi = nu_fit + nu_sigma
    sf_lo = scale_factor(nu_lo)
    sf_hi = scale_factor(nu_hi)
    return sf_lo, sf_hi


# ---------------------------------------------------------------------------
# Kolmogorov–Smirnov goodness-of-fit
# ---------------------------------------------------------------------------
def ks_student_t(data, nu, mu, sigma):
    ks_stat, ks_p = stats.kstest(data, lambda x: stats.t.cdf(
        x, df=nu, loc=mu, scale=sigma))
    return float(ks_stat), float(ks_p)


# ---------------------------------------------------------------------------
# Master driver
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    t_master = time.time()

    if in_window(DIMLESS_HINGE * XI_TARGET, WINDOW_A) or \
            in_window(DIMLESS_HINGE * XI_TARGET, WINDOW_B):
        raise RuntimeError(
            f"Planned ξ_target={XI_TARGET} yields L_ray"
            f"={DIMLESS_HINGE * XI_TARGET} in a resonance window.")

    print(f"F3-verify: regenerating F2 T_motif pool at ξ = {XI_TARGET} lu "
          f"across {len(SEEDS)} seeds", file=sys.stderr)

    per_seed = []
    all_T = []
    for seed in SEEDS:
        r = run_seed_T_extraction(seed)
        per_seed.append({k: v for k, v in r.items() if k != "T_list"})
        all_T.extend(r["T_list"])

    T_array = np.asarray(all_T, dtype=float)
    N_pooled = len(T_array)
    print(f"\nPooled T_motif sample: N = {N_pooled}", file=sys.stderr)
    print(f"  mean = {T_array.mean():.6f}, std = {T_array.std(ddof=1):.6f}",
          file=sys.stderr)

    # MLE fit
    print("Running MLE Student-t fit...", file=sys.stderr)
    mle = mle_fit_student_t(T_array)
    print(f"  ν_fit = {mle['nu']:.3f}, μ_fit = {mle['mu']:.6f}, "
          f"σ_fit = {mle['sigma']:.6f}, log L = {mle['log_likelihood']:.3f}",
          file=sys.stderr)

    # Hessian-based σ_ν
    print("Computing Hessian at MLE optimum...", file=sys.stderr)
    H = hessian_at_optimum([mle["nu"], mle["mu"], mle["sigma"]], T_array)
    nu_sigma, cov_matrix = nu_sigma_from_hessian(H)
    print(f"  σ_ν (from Hessian) = {nu_sigma}", file=sys.stderr)

    # Scale factor central + band
    sf_central = scale_factor(mle["nu"])
    sf_lo, sf_hi = scale_factor_band(mle["nu"], nu_sigma)

    kappa_central_MLE = KAPPA_CENTRAL_PREF3 * sf_central
    if sf_lo is not None and sf_hi is not None:
        kappa_lo = KAPPA_CENTRAL_PREF3 * sf_lo
        kappa_hi = KAPPA_CENTRAL_PREF3 * sf_hi
        half_width = (kappa_hi - kappa_lo) / 2
        model_band_rel_MLE = half_width / kappa_central_MLE
    else:
        kappa_lo = kappa_hi = None
        model_band_rel_MLE = None

    # K-S goodness-of-fit
    print("Running K-S goodness-of-fit test...", file=sys.stderr)
    ks_stat, ks_p = ks_student_t(T_array, mle["nu"], mle["mu"], mle["sigma"])
    student_t_valid = (ks_p > KS_PASS_PVALUE)
    print(f"  KS stat = {ks_stat:.4f}, p-value = {ks_p:.4f}, "
          f"valid = {student_t_valid}", file=sys.stderr)

    # Comparison to F3
    tightening = (MODEL_BAND_F3_REL / model_band_rel_MLE
                  if model_band_rel_MLE is not None and model_band_rel_MLE > 0
                  else None)
    nu_in_f3_envelope = (NU_F3_ENVELOPE[0] <= mle["nu"] <= NU_F3_ENVELOPE[1])

    # Downstream updated clearance
    # GR-SC 1.8 target: σ₁/κ_M^det < 0.036 → κ_M^det > σ₁/0.036.
    # Central |N̂'| ≳ (σ₁/0.036) / (0.35355 × scale_factor).
    # σ₁_std(ξ_canonical) from fit = 0.005169.
    sigma1_std_canonical = 0.005169
    kappa_M_threshold = sigma1_std_canonical / 0.036
    N_prime_threshold_central = (kappa_M_threshold
                                 / (0.35355 * sf_central)
                                 if sf_central else None)

    # Pooled-R2 symbolic ratio
    N_prime_over_mu_1 = (0.52 / (0.35355 * sf_central)
                        if sf_central else None)

    # Write CSV
    csv_path = os.path.join(OUT_DIR, "sigma1_model_verify_table.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "nu_fit", "nu_sigma", "mu_fit", "sigma_fit", "N_pooled",
            "scale_factor_MLE", "kappa_central_MLE",
            "kappa_model_band_MLE_rel",
            "KS_stat", "KS_pvalue", "student_t_valid",
            "nu_in_F3_envelope", "tightening_vs_F3",
        ])
        w.writerow([
            mle["nu"], nu_sigma, mle["mu"], mle["sigma"], N_pooled,
            sf_central, kappa_central_MLE,
            model_band_rel_MLE,
            ks_stat, ks_p, student_t_valid,
            nu_in_f3_envelope, tightening,
        ])

    # Write summary JSON
    out = {
        "method": ("ED-SC 3.4-σ₁ F3-verify: MLE Student-t fit on raw "
                   "pooled T_motif sample regenerated from F2 evolution "
                   "pipeline; Hessian-based ν uncertainty; "
                   "K-S goodness-of-fit validation"),
        "simulator_of_record":
            "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
        "parent_artefact":
            "outputs/ed_sc_3_4_sigma1/sigma1_multiseed_summary.json (F2)",
        "xi_canonical_lattice_units": XI_CANONICAL,
        "xi_target": XI_TARGET,
        "dimensionless_hinge": DIMLESS_HINGE,
        "alpha_filt": ALPHA_FILT,
        "N_req": N_REQ,
        "snapshot_schedule": {
            "burn_in": XI_BURN_IN, "snap_every": XI_SNAP_EVERY,
            "snapshots_per_seed": 40,
        },
        "canonical_params": {
            "alpha": fr.ALPHA0, "gamma": fr.GAMMA,
            "noise_sigma": fr.NOISE0,
            "mobility_exp": fr.MOBILITY_EXP,
            "steps": fr.STEPS, "size": fr.SIZE, "dt": fr.DT,
        },
        "seeds": SEEDS,
        "resonance_windows_excluded": {
            "A": list(WINDOW_A), "B": list(WINDOW_B)},
        "per_seed_regeneration": per_seed,
        "N_pooled": N_pooled,
        "pooled_T_stats": {
            "mean": float(T_array.mean()),
            "std_ddof1": float(T_array.std(ddof=1)),
            "median": float(np.median(T_array)),
            "iqr": float(np.quantile(T_array, 0.75)
                          - np.quantile(T_array, 0.25)),
            "min": float(T_array.min()),
            "max": float(T_array.max()),
        },
        "mle_fit": {
            "nu": mle["nu"],
            "nu_sigma": nu_sigma,
            "mu": mle["mu"],
            "sigma": mle["sigma"],
            "log_likelihood": mle["log_likelihood"],
            "optimizer": mle["optimizer"],
            "scipy_fit": mle["scipy_fit"],
            "custom_fit": mle["custom_fit"],
            "hessian_matrix": H.tolist(),
            "covariance_matrix": cov_matrix,
        },
        "kappa_correction": {
            "kappa_central_preF3_Gaussian": KAPPA_CENTRAL_PREF3,
            "scale_factor_MLE": sf_central,
            "scale_factor_band": (
                [sf_lo, sf_hi] if sf_lo is not None else None),
            "kappa_central_MLE": kappa_central_MLE,
            "kappa_band_MLE": (
                [kappa_lo, kappa_hi] if kappa_lo is not None else None),
            "model_band_rel_MLE": model_band_rel_MLE,
        },
        "f3_comparison": {
            "nu_F3_summary": NU_F3_SUMMARY,
            "nu_F3_envelope": NU_F3_ENVELOPE,
            "nu_in_F3_envelope": nu_in_f3_envelope,
            "model_band_F3_rel": MODEL_BAND_F3_REL,
            "tightening_factor": tightening,
            "kappa_central_F3": 0.001766,
            "kappa_central_shift_MLE_vs_F3": (
                kappa_central_MLE - 0.001766
                if kappa_central_MLE else None),
            "kappa_central_shift_MLE_vs_F3_rel": (
                (kappa_central_MLE - 0.001766) / 0.001766
                if kappa_central_MLE else None),
        },
        "ks_test": {
            "ks_stat": ks_stat,
            "ks_pvalue": ks_p,
            "pass_threshold": KS_PASS_PVALUE,
            "student_t_valid": student_t_valid,
        },
        "downstream_updates": {
            "kappa_central_updated": kappa_central_MLE,
            "model_band_relative_updated": model_band_rel_MLE,
            "GR_SC_1_8_N_prime_threshold_central_updated":
                N_prime_threshold_central,
            "pooled_R2_N_prime_over_mu1_updated": N_prime_over_mu_1,
        },
        "wall_seconds_total": time.time() - t_master,
    }

    json_path = os.path.join(OUT_DIR, "sigma1_model_verify_summary.json")
    with open(json_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"\nWrote table → {csv_path}", file=sys.stderr)
    print(f"Wrote summary → {json_path}", file=sys.stderr)
    print(json.dumps({
        "N_pooled": N_pooled,
        "nu_fit": mle["nu"],
        "nu_sigma": nu_sigma,
        "mu_fit": mle["mu"],
        "sigma_fit": mle["sigma"],
        "scale_factor_MLE": sf_central,
        "kappa_central_MLE": kappa_central_MLE,
        "model_band_rel_MLE": model_band_rel_MLE,
        "nu_in_F3_envelope": nu_in_f3_envelope,
        "tightening_factor_vs_F3": tightening,
        "ks_stat": ks_stat,
        "ks_pvalue": ks_p,
        "student_t_valid": student_t_valid,
        "kappa_shift_MLE_vs_F3": out["f3_comparison"][
            "kappa_central_shift_MLE_vs_F3_rel"],
        "wall_seconds_total": out["wall_seconds_total"],
    }, indent=2))


if __name__ == "__main__":
    main()
