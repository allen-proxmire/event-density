"""GR-SC 1.0a Weyl-Ratio Sensitivity Sweep.

Pre-registered in theory/GR_SC_1_0a_WeylRatio_Sensitivity.md.

Pure arithmetic: no simulator call. Computes the Weyl-like bounded
Ratio-class invariant ℛ_W(S1), its closed-form derivative, and the
relative condition number κ across a 26-point S1 sweep. Classifies
the empirical operating point as quantitative / near-singular /
borderline.

Definitions:
  ℛ_W(S1)    = -(2·S1 + 1) / (S1 + 2)
  dℛ_W/dS1   = -3 / (S1 + 2)²     (closed form; always ≤ 0)
  κ(S1)      = |(S1 / ℛ_W) · (dℛ_W/dS1)|

Empirical anchors from ED-SC 3.4 execution:
  S1_eff  = -1.95   (effectively constant across r_diag=1 window)
  S1_mean = -1.953  (arithmetic mean of 9-point scan S1 values)
  S1_lo   = -2.209  (widest 16 % CI lower edge across scan, clipped)
  S1_hi   = -1.733  (widest 84 % CI upper edge across scan)

Classification (per memo §1):
  quantitative_prediction  — max κ in empirical band < 10
                              AND max |dℛ_W/dS1| in band ≤ 10²
  near_singular_artifact   — max κ in band ≥ 100
                              OR max |dℛ_W/dS1| in band > 10³
  borderline               — otherwise

Writes:
  outputs/gr_sc_1_0a/wy_sensitivity_table.csv
  outputs/gr_sc_1_0a/wy_sensitivity_summary.json
"""
import csv
import json
import math
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "..", "..", "outputs", "gr_sc_1_0a")

# ---------------------------------------------------------------------------
# Sweep configuration
# ---------------------------------------------------------------------------
S1_MIN = -2.00
S1_MAX = -1.75
S1_STEP = 0.01

# Empirical anchors (from outputs/ed_sc_3_4/xi_calibration_summary.json)
S1_EFF = -1.95
S1_MEAN = -1.953  # arithmetic mean of 9 per-point S1 values
S1_BAND_LO_REPORTED = -2.209  # raw; clipped to sweep range below
S1_BAND_HI_REPORTED = -1.733

# Classification thresholds (per memo §1)
KAPPA_QUANT_MAX = 10.0
KAPPA_SINGULAR_MIN = 100.0
DERIV_SINGULAR_MAX = 1000.0

POLE = -2.00


# ---------------------------------------------------------------------------
# Core arithmetic
# ---------------------------------------------------------------------------
def r_w(s1):
    if s1 == POLE:
        return None
    return -(2 * s1 + 1) / (s1 + 2)


def dr_w_ds1(s1):
    if s1 == POLE:
        return None
    return -3.0 / (s1 + 2) ** 2


def kappa(s1):
    rw = r_w(s1)
    drw = dr_w_ds1(s1)
    if rw is None or drw is None or rw == 0:
        return None
    return abs((s1 / rw) * drw)


def approximately_equal(a, b, tol=1e-9):
    return abs(a - b) < tol


# ---------------------------------------------------------------------------
# Sweep
# ---------------------------------------------------------------------------
def build_sweep():
    """Generate 26 S1 values (-2.00 to -1.75 step 0.01) with rounding to
    2 decimal places to avoid float drift."""
    vals = []
    k = 0
    while True:
        v = round(S1_MIN + k * S1_STEP, 2)
        if v > S1_MAX + 1e-9:
            break
        vals.append(v)
        k += 1
    return vals


def band_clipped(s1_lo_reported, s1_hi_reported, sweep):
    """Clip the empirical band to the sweep range."""
    s1_lo = max(s1_lo_reported, sweep[0])
    s1_hi = min(s1_hi_reported, sweep[-1])
    return s1_lo, s1_hi


def within_band(s1, s1_lo, s1_hi):
    return s1_lo <= s1 <= s1_hi


# ---------------------------------------------------------------------------
# Classification logic
# ---------------------------------------------------------------------------
def classify(rows_in_band):
    """Apply the memo §1 three-way classification to rows inside the
    clipped empirical band."""
    kappas = [r["kappa"] for r in rows_in_band if r["kappa"] is not None]
    derivs = [abs(r["dR_W_dS1"]) for r in rows_in_band
              if r["dR_W_dS1"] is not None]

    if not kappas or not derivs:
        return {
            "classification": "undefined",
            "reason": "no finite kappa/derivative rows inside the band "
                      "(pole at S1 = -2 dominates)",
            "kappa_max": None, "deriv_max": None,
            "kappa_median": None,
        }

    kappa_max = max(kappas)
    kappa_min = min(kappas)
    kappa_median = sorted(kappas)[len(kappas) // 2]
    deriv_max = max(derivs)

    if kappa_max < KAPPA_QUANT_MAX and deriv_max <= 100.0:
        cls = "quantitative_prediction"
        reason = (f"max κ in band = {kappa_max:.3f} < {KAPPA_QUANT_MAX}; "
                  f"max |dℛ_W/dS1| = {deriv_max:.3f} ≤ 100")
    elif kappa_max >= KAPPA_SINGULAR_MIN or deriv_max > DERIV_SINGULAR_MAX:
        cls = "near_singular_artifact"
        reason = (f"max κ in band = {kappa_max:.3f} "
                  f"(≥ {KAPPA_SINGULAR_MIN} threshold) OR "
                  f"max |dℛ_W/dS1| = {deriv_max:.3f} "
                  f"(> {DERIV_SINGULAR_MAX} threshold)")
    else:
        cls = "borderline"
        reason = (f"max κ in band = {kappa_max:.3f}; "
                  f"max |dℛ_W/dS1| = {deriv_max:.3f}; "
                  "neither quantitative nor near-singular thresholds met")

    return {
        "classification": cls,
        "reason": reason,
        "kappa_max": kappa_max,
        "kappa_min": kappa_min,
        "kappa_median": kappa_median,
        "deriv_max": deriv_max,
    }


# ---------------------------------------------------------------------------
# Citation-form prescription (per memo §4)
# ---------------------------------------------------------------------------
def citation_form(cls, rows_in_band, anchors):
    if cls == "quantitative_prediction":
        kappa_at_eff = anchors.get("kappa_at_S1_eff")
        rw_at_eff = anchors.get("r_W_at_S1_eff")
        delta_s1_per_real = 0.15  # ED-SC 3.3.9 per-realisation envelope
        if (kappa_at_eff is not None and rw_at_eff is not None
                and S1_EFF != 0):
            rel_unc = kappa_at_eff * (delta_s1_per_real / abs(S1_EFF))
            rw_unc = abs(rw_at_eff) * rel_unc
            return {
                "form": "quantitative_point",
                "value": rw_at_eff,
                "symmetric_uncertainty": rw_unc,
                "prescription": (
                    f"Cite ℛ_W(S1_eff) = {rw_at_eff:.3f} ± "
                    f"{rw_unc:.3f} (δS1_per_real = {delta_s1_per_real})."),
            }
        return {"form": "quantitative_point",
                "prescription": "Cite ℛ_W(S1_eff) ± κ·δS1_per_real."}
    elif cls == "near_singular_artifact":
        return {
            "form": "no_numerical_citation",
            "prescription": (
                "Do not cite a numerical ℛ_W value. Cite only the "
                "bounded-Ratio-class structural claim "
                "ℛ_W ∈ (−2, −1/2) and note that the empirical S1 lies "
                "outside the bounded-subclass interior; the algebraic "
                "map's bounded-interval prediction is not empirically "
                "validated at the current operating point."),
        }
    elif cls == "borderline":
        rw_values = [r["R_W"] for r in rows_in_band if r["R_W"] is not None]
        if rw_values:
            rw_lo = min(rw_values)
            rw_hi = max(rw_values)
            return {
                "form": "range_citation",
                "range_lo": rw_lo,
                "range_hi": rw_hi,
                "prescription": (
                    f"Cite ℛ_W as a range bracketed by ℛ_W(S1_lo) = "
                    f"{rw_lo:.3f} and ℛ_W(S1_hi) = {rw_hi:.3f} across "
                    f"the empirical S1 band. Do not cite a point value."),
            }
        return {"form": "range_citation",
                "prescription": "Cite ℛ_W as a range across the S1 band."}
    else:
        return {"form": "undefined",
                "prescription": "Sensitivity sweep returned no finite "
                                "rows in the empirical band; memo §4 has "
                                "no prescription for this outcome."}


# ---------------------------------------------------------------------------
# Master driver
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    t0 = time.time()

    sweep = build_sweep()
    s1_lo_clip, s1_hi_clip = band_clipped(
        S1_BAND_LO_REPORTED, S1_BAND_HI_REPORTED, sweep)
    print(f"Sweep: {len(sweep)} points from {sweep[0]} to {sweep[-1]} "
          f"at step {S1_STEP}", file=sys.stderr)
    print(f"Empirical band (clipped): [{s1_lo_clip}, {s1_hi_clip}]",
          file=sys.stderr)
    print(f"Anchors: S1_eff={S1_EFF}, S1_mean={S1_MEAN}", file=sys.stderr)

    rows = []
    for s1 in sweep:
        rw = r_w(s1)
        drw = dr_w_ds1(s1)
        k = kappa(s1)
        row = {
            "S1": s1,
            "R_W": rw,
            "dR_W_dS1": drw,
            "kappa": k,
            "within_empirical_band": within_band(s1, s1_lo_clip, s1_hi_clip),
            "is_S1_eff": approximately_equal(s1, S1_EFF, tol=5e-3),
            "is_S1_mean": approximately_equal(s1, S1_MEAN, tol=5e-3),
            "is_pole": (s1 == POLE),
        }
        rows.append(row)

    # Locate anchor rows
    row_eff = next((r for r in rows if r["is_S1_eff"]), None)
    row_mean = next((r for r in rows if r["is_S1_mean"]), None)

    anchors = {
        "S1_eff": S1_EFF,
        "S1_mean": S1_MEAN,
        "S1_band_reported": [S1_BAND_LO_REPORTED, S1_BAND_HI_REPORTED],
        "S1_band_clipped": [s1_lo_clip, s1_hi_clip],
        "r_W_at_S1_eff": row_eff["R_W"] if row_eff else None,
        "derivative_at_S1_eff": row_eff["dR_W_dS1"] if row_eff else None,
        "kappa_at_S1_eff": row_eff["kappa"] if row_eff else None,
        "r_W_at_S1_mean": row_mean["R_W"] if row_mean else None,
        "derivative_at_S1_mean": row_mean["dR_W_dS1"] if row_mean else None,
        "kappa_at_S1_mean": row_mean["kappa"] if row_mean else None,
    }

    # Classify using rows inside the clipped empirical band
    rows_in_band = [r for r in rows if r["within_empirical_band"]]
    classification = classify(rows_in_band)

    # Citation-form prescription
    citation = citation_form(
        classification["classification"], rows_in_band, anchors)

    # Write CSV
    csv_path = os.path.join(OUT_DIR, "wy_sensitivity_table.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["S1", "R_W", "dR_W_dS1", "kappa",
                    "within_empirical_band", "is_S1_eff", "is_S1_mean",
                    "is_pole"])
        for r in rows:
            w.writerow([
                r["S1"], r["R_W"], r["dR_W_dS1"], r["kappa"],
                r["within_empirical_band"], r["is_S1_eff"], r["is_S1_mean"],
                r["is_pole"],
            ])

    # Write JSON summary
    out = {
        "method": ("GR-SC 1.0a Weyl-ratio sensitivity sweep: "
                   "closed-form ℛ_W(S1) = -(2·S1 + 1)/(S1 + 2), "
                   "dℛ_W/dS1 = -3/(S1+2)², κ = |S1·(dℛ_W/dS1)/ℛ_W|; "
                   "pure arithmetic, no simulator call"),
        "sweep": {
            "S1_min": S1_MIN, "S1_max": S1_MAX, "S1_step": S1_STEP,
            "n_points": len(sweep),
        },
        "anchors": anchors,
        "classification_thresholds": {
            "kappa_quant_max": KAPPA_QUANT_MAX,
            "kappa_singular_min": KAPPA_SINGULAR_MIN,
            "deriv_singular_max": DERIV_SINGULAR_MAX,
        },
        "classification": classification,
        "citation_form": citation,
        "rows": rows,
        "wall_seconds_total": time.time() - t0,
    }

    json_path = os.path.join(OUT_DIR, "wy_sensitivity_summary.json")
    with open(json_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"\nWrote table → {csv_path}", file=sys.stderr)
    print(f"Wrote summary → {json_path}", file=sys.stderr)
    print(json.dumps({
        "classification": classification["classification"],
        "classification_reason": classification["reason"],
        "r_W_at_S1_eff": anchors["r_W_at_S1_eff"],
        "kappa_at_S1_eff": anchors["kappa_at_S1_eff"],
        "derivative_at_S1_eff": anchors["derivative_at_S1_eff"],
        "kappa_max_in_band": classification.get("kappa_max"),
        "kappa_median_in_band": classification.get("kappa_median"),
        "deriv_max_in_band": classification.get("deriv_max"),
        "citation_form": citation.get("form"),
        "wall_seconds_total": out["wall_seconds_total"],
    }, indent=2))


if __name__ == "__main__":
    main()
