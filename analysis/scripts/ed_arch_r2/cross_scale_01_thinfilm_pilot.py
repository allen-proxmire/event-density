"""
ED-SC 2.0 Cross-Scale Test #1 — Thin-Film Dewetting (PILOT)
===========================================================

Pilot run of the ED-SC 2.0 motif-conditioned median invariant on a pseudo-
height field h(x, y) derived from an AFM-like thin-film dewetting image.

Canonical filter parameters (from docs/ED-SC-2.0.md §1.4):
    alpha      = 0.25        (threshold factor for motif admission)
    L_ray      = 2           (ray length in pixels, with periodic wrap)
    delta      = 0.10        (Hessian-eigenvalue non-degeneracy tolerance)

Pass window (docs/ED-SC-2.0.md §4): median(R_motif) in [-1.50, -1.10].

Usage
-----
    python cross_scale_01_thinfilm_pilot.py --image <path_to_png_or_jpg>
    python cross_scale_01_thinfilm_pilot.py --synthetic
    python cross_scale_01_thinfilm_pilot.py            (auto: try default path
                                                        C:/Users/allen/GitHub/
                                                        Event Density/outputs/
                                                        thinfilm_pilot_input.png
                                                        else --synthetic)

Caveats
-------
This is a PILOT test, not a canonical one.  Pixel brightness is treated as
relative height — the absolute magnitude of h is meaningless, but the
Hessian eigenvalue *ratio* is invariant under constant scaling so the
motif-conditioned median is still a well-defined quantity on the pseudo-
field.  The sampling grid is whatever the image resolution gives; no
check is made that Delta x <= L_coh/8 per ED-SC 2.0 §3.
"""

from __future__ import annotations

import argparse
import os
import sys
import numpy as np
from scipy import ndimage

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


# ----------------------------------------------------------------------------
#  Canonical ED-SC 2.0 filter parameters (DO NOT CHANGE; pre-registered)
# ----------------------------------------------------------------------------

ALPHA_FILT   = 0.25    # motif threshold factor
L_RAY        = 2       # pixels (periodic wrap)
DEG_TOL      = 0.10    # |lambda_min|/|lambda_max| >= DEG_TOL

PASS_WINDOW  = (-1.50, -1.10)
WINDOW_NEAR1 = (-1.17, -0.83)

# ----------------------------------------------------------------------------
#  Image loading
# ----------------------------------------------------------------------------

DEFAULT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))),
    "outputs", "thinfilm_pilot_input.png",
)


def load_image_as_h(path: str) -> np.ndarray:
    if not HAS_PIL:
        raise RuntimeError("PIL not installed; cannot load image.")
    img = Image.open(path).convert("L")  # grayscale
    arr = np.asarray(img, dtype=np.float64)
    return arr


def synth_thinfilm_h(N: int = 128, n_holes: int = 3, seed: int = 770) -> np.ndarray:
    """
    Synthetic pseudo-thin-film field matching the visual morphology of the
    uploaded inline image (mottled background + a few dark circular holes).
    For PILOT use only.
    """
    rng = np.random.default_rng(seed)
    # Mottled background: low-pass random field centered at 0.55 brightness
    base = rng.normal(0.0, 1.0, (N, N))
    base = ndimage.gaussian_filter(base, sigma=N / 24.0)
    base = 0.5 + 0.10 * (base / base.std())
    # A few dark "holes" (dewetting nuclei)
    xs = np.arange(N)
    XX, YY = np.meshgrid(xs, xs, indexing="xy")
    hole_sigma = N / 18.0
    hole_depth = 0.30
    # Positions roughly matching the three holes visible in the inline frame:
    # one upper-center, one mid-left, one center-right-below
    hole_sites = [
        (int(0.38 * N), int(0.18 * N)),
        (int(0.20 * N), int(0.42 * N)),
        (int(0.48 * N), int(0.50 * N)),
    ][:n_holes]
    for (cy, cx) in hole_sites:
        base -= hole_depth * np.exp(
            -((XX - cx) ** 2 + (YY - cy) ** 2) / (2.0 * hole_sigma ** 2)
        )
    # Mild ambient noise on top
    base += rng.normal(0.0, 0.015, (N, N))
    return base


# ----------------------------------------------------------------------------
#  Preprocessing: normalize, detrend, light smoothing
# ----------------------------------------------------------------------------

def preprocess(h_raw: np.ndarray,
               smooth_sigma: float = 0.8,
               detrend_order: int = 2) -> np.ndarray:
    """Normalize to [0, 1], remove low-order polynomial background, lightly smooth."""
    # Normalize
    h = h_raw.astype(np.float64).copy()
    h = (h - h.min()) / max(h.max() - h.min(), 1e-12)

    # Detrend via 2D polynomial fit of degree `detrend_order`
    Ny, Nx = h.shape
    y, x = np.mgrid[0:Ny, 0:Nx].astype(np.float64)
    y /= Ny; x /= Nx
    # Build design matrix up to detrend_order
    terms = []
    for i in range(detrend_order + 1):
        for j in range(detrend_order + 1 - i):
            terms.append((x ** i) * (y ** j))
    A = np.stack([t.ravel() for t in terms], axis=1)
    coef, *_ = np.linalg.lstsq(A, h.ravel(), rcond=None)
    bg = (A @ coef).reshape(h.shape)
    h -= bg
    h = (h - h.min()) / max(h.max() - h.min(), 1e-12)

    # Light Gaussian smoothing to stabilise derivatives
    if smooth_sigma > 0:
        h = ndimage.gaussian_filter(h, sigma=smooth_sigma, mode="wrap")

    return h


# ----------------------------------------------------------------------------
#  Saddle detection and Hessian
# ----------------------------------------------------------------------------

def central_gradient(h: np.ndarray):
    dpdx = 0.5 * (np.roll(h, -1, axis=0) - np.roll(h, 1, axis=0))
    dpdy = 0.5 * (np.roll(h, -1, axis=1) - np.roll(h, 1, axis=1))
    return dpdx, dpdy


def hessian_at(h: np.ndarray, i: int, j: int) -> np.ndarray:
    d2x = h[i + 1, j] - 2.0 * h[i, j] + h[i - 1, j]
    d2y = h[i, j + 1] - 2.0 * h[i, j] + h[i, j - 1]
    dxy = 0.25 * (
        h[i + 1, j + 1] - h[i + 1, j - 1]
      - h[i - 1, j + 1] + h[i - 1, j - 1]
    )
    return np.array([[d2x, dxy], [dxy, d2y]])


def find_morse_saddles(h: np.ndarray, deg_tol: float):
    """Return a list of saddle dicts with Hessian eigenstructure."""
    dpdx, dpdy = central_gradient(h)
    sx_pos = dpdx > 0; sx_neg = dpdx < 0
    sy_pos = dpdy > 0; sy_neg = dpdy < 0
    x_flip = (
        (sx_pos & np.roll(sx_neg, -1, axis=0)) |
        (sx_neg & np.roll(sx_pos, -1, axis=0))
    )
    y_flip = (
        (sy_pos & np.roll(sy_neg, -1, axis=1)) |
        (sy_neg & np.roll(sy_pos, -1, axis=1))
    )
    cand = x_flip & y_flip
    interior = np.zeros_like(cand)
    interior[4:-4, 4:-4] = True
    cand &= interior
    ij = np.argwhere(cand)

    saddles = []
    for (i, j) in ij:
        i, j = int(i), int(j)
        H = hessian_at(h, i, j)
        det = H[0, 0] * H[1, 1] - H[0, 1] * H[1, 0]
        if det >= 0:
            continue
        w, V = np.linalg.eigh(H)
        if not (w[0] < 0 < w[1]):
            continue
        if min(abs(w[0]), abs(w[1])) / max(abs(w[0]), abs(w[1])) < deg_tol:
            continue
        saddles.append({
            "i": i, "j": j, "H": H,
            "lambda_neg": float(w[0]), "lambda_pos": float(w[1]),
            "e_neg": V[:, 0], "e_pos": V[:, 1],
            "E_at": float(h[i, j]),
        })
    return saddles


def saddle_ratio(s: dict) -> float:
    kn, kp = s["lambda_neg"], s["lambda_pos"]
    if abs(kn) >= abs(kp):
        return kn / kp
    return kp / kn


# ----------------------------------------------------------------------------
#  Motif filter
# ----------------------------------------------------------------------------

def trace_ray(h: np.ndarray, i: int, j: int,
              direction: np.ndarray, sign: int, L_ray: int) -> np.ndarray:
    Ny, Nx = h.shape
    vals = np.empty(L_ray, dtype=float)
    for step in range(1, L_ray + 1):
        di = sign * direction[0] * step
        dj = sign * direction[1] * step
        ii = int(round(i + di)) % Ny
        jj = int(round(j + dj)) % Nx
        vals[step - 1] = h[ii, jj]
    return vals


def motif_admit(s: dict, h: np.ndarray,
                alpha_filt: float, L_ray: int,
                E_hi: float, E_lo: float) -> bool:
    i, j = s["i"], s["j"]
    r_neg_pp = trace_ray(h, i, j, s["e_neg"], +1, L_ray)
    r_neg_mm = trace_ray(h, i, j, s["e_neg"], -1, L_ray)
    r_pos_pp = trace_ray(h, i, j, s["e_pos"], +1, L_ray)
    r_pos_mm = trace_ray(h, i, j, s["e_pos"], -1, L_ray)
    return (
        r_neg_pp[-1] < E_lo and r_neg_mm[-1] < E_lo and
        r_pos_pp[-1] > E_hi and r_pos_mm[-1] > E_hi
    )


# ----------------------------------------------------------------------------
#  Main
# ----------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--image", type=str, default=None,
                    help="Path to input image (PNG/JPG). If omitted, tries "
                         "DEFAULT_PATH then falls back to --synthetic.")
    ap.add_argument("--synthetic", action="store_true",
                    help="Force synthetic stand-in (for piloting without an image).")
    ap.add_argument("--size-synth", type=int, default=128,
                    help="Synthetic grid size (default 128).")
    ap.add_argument("--out-memo", type=str,
                    default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         "ThinFilm_Pilot_Memo.md"),
                    help="Memo output path.")
    args = ap.parse_args()

    # Decide input source
    use_synthetic = False
    source_label = None
    h_raw = None

    if args.synthetic:
        h_raw = synth_thinfilm_h(N=args.size_synth)
        use_synthetic = True
        source_label = "SYNTHETIC stand-in (no real image provided)"
    else:
        path = args.image or DEFAULT_PATH
        if os.path.exists(path) and HAS_PIL:
            h_raw = load_image_as_h(path)
            source_label = f"REAL image: {path}"
        else:
            print(f"[pilot] No image at {path}; falling back to SYNTHETIC.")
            h_raw = synth_thinfilm_h(N=args.size_synth)
            use_synthetic = True
            source_label = "SYNTHETIC stand-in (no real image provided)"

    print("=" * 78)
    print("  ED-SC 2.0 Cross-Scale Test #1 — Thin-Film Dewetting  [PILOT]")
    print("=" * 78)
    print(f"  source: {source_label}")
    print(f"  raw shape: {h_raw.shape}")

    # Preprocess
    h = preprocess(h_raw, smooth_sigma=0.8, detrend_order=2)
    p_hat = float(h.mean())
    p_std = float(h.std())
    E_hi = p_hat + ALPHA_FILT * p_std
    E_lo = p_hat - ALPHA_FILT * p_std
    print(f"  after preprocess: mean={p_hat:.5f}  std={p_std:.5f}  "
          f"range=[{h.min():.4f}, {h.max():.4f}]")
    print(f"  thresholds: E_lo={E_lo:.5f}  E_hi={E_hi:.5f}")

    # Coherence length estimate (autocorrelation first-zero proxy via |grad|)
    gx, gy = central_gradient(h)
    gmag_mean = float(np.mean(np.sqrt(gx ** 2 + gy ** 2)))
    L_coh = 1.0 / gmag_mean if gmag_mean > 0 else float("inf")
    print(f"  L_coh estimate (1/mean|grad h|): {L_coh:.2f} pixels")

    # Morse saddles
    saddles = find_morse_saddles(h, DEG_TOL)
    all_ratios = np.array([saddle_ratio(s) for s in saddles])
    print(f"  Morse saddles (after degeneracy filter): {len(saddles)}")
    if len(all_ratios) > 0:
        q25, q50, q75 = np.percentile(all_ratios, [25, 50, 75])
        in_arch = float(((all_ratios >= PASS_WINDOW[0]) & (all_ratios <= PASS_WINDOW[1])).mean())
        print(f"  R_all: median={q50:+.3f}  IQR=[{q25:+.3f},{q75:+.3f}]  "
              f"in_pass_window={in_arch*100:.1f}%")

    # Motif filter
    admitted = [s for s in saddles if motif_admit(s, h, ALPHA_FILT, L_RAY, E_hi, E_lo)]
    motif_r = np.array([saddle_ratio(s) for s in admitted])
    print(f"  motif-admitted saddles: {len(admitted)} / {len(saddles)}")

    verdict = None
    if len(motif_r) == 0:
        print("  R_motif is EMPTY — cannot compute invariant.")
        verdict = "undecidable_no_motif_saddles"
        med = mean = q25 = q75 = in_win = float("nan")
    else:
        med = float(np.median(motif_r))
        mean = float(motif_r.mean())
        q25, q75 = np.percentile(motif_r, [25, 75])
        in_win = float(((motif_r >= PASS_WINDOW[0]) & (motif_r <= PASS_WINDOW[1])).mean())
        print(f"  R_motif: N={len(motif_r)}  median={med:+.3f}  mean={mean:+.3f}  "
              f"IQR=[{q25:+.3f},{q75:+.3f}]  width={q75-q25:.3f}")
        print(f"  R_motif fraction in ED-SC 2.0 window {PASS_WINDOW}: {in_win*100:.1f}%")

        if PASS_WINDOW[0] <= med <= PASS_WINDOW[1]:
            verdict = "PASS"
        else:
            verdict = "FAIL"
        print(f"  VERDICT (pilot, median in window?): {verdict}")

    # Text histogram of R_motif (if we have any)
    print("")
    print("  Textual histogram of R_motif (bin width 0.25):")
    if len(motif_r) > 0:
        bins = np.arange(-6.0, -0.74, 0.25)
        hist_motif, _ = np.histogram(motif_r, bins=bins)
        for k in range(len(bins) - 1):
            lo, hi = bins[k], bins[k + 1]
            mark = " <-- ED-SC 2.0 window" if (lo >= -1.5 and hi <= -1.0) else ""
            bar = "*" * int(hist_motif[k])
            print(f"    [{lo:+.2f}, {hi:+.2f})  {hist_motif[k]:>3d}  {bar}{mark}")
    else:
        print("    (no saddles)")

    # Save NPZ of the processed field + ratios for reproducibility
    here = os.path.dirname(os.path.abspath(__file__))
    np.save(os.path.join(here, "thinfilm_pilot_h.npy"), h)
    np.save(os.path.join(here, "thinfilm_pilot_ratios_all.npy"), all_ratios)
    np.save(os.path.join(here, "thinfilm_pilot_ratios_motif.npy"), motif_r)

    # Short summary line for memo
    summary = {
        "source": source_label,
        "use_synthetic": use_synthetic,
        "shape": h.shape,
        "N_morse": len(saddles),
        "N_motif": len(motif_r),
        "median": med,
        "mean": mean,
        "q25": q25,
        "q75": q75,
        "in_window_frac": in_win,
        "L_coh_px": L_coh,
        "verdict": verdict,
    }
    print("")
    print("  artifacts saved to:", here)
    return summary


if __name__ == "__main__":
    main()
