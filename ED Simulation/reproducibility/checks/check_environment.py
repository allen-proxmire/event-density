"""
check_environment.py
====================
Verifies that the execution environment meets ED-SIM v1 requirements.

Checks:
  - Python version (>= 3.10)
  - Required packages: numpy, scipy, matplotlib
  - Optional packages: umap-learn, scikit-learn, h5py
  - GPU availability (CuPy)

Writes a JSON summary to output/atlas/environment_check.json.

Usage:
    python reproducibility/checks/check_environment.py
"""

import os
import sys
import json
import platform
import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
ATLAS_DIR = os.path.join(SIM_DIR, "output", "atlas")

REQUIRED = {
    "numpy":      "1.24",
    "scipy":      "1.10",
    "matplotlib": "3.7",
}

OPTIONAL = {
    "umap":           ("0.5", "UMAP embedding (falls back to t-SNE)"),
    "sklearn":        ("1.2", "Silhouette score, hierarchical clustering"),
    "h5py":           ("3.8", "HDF5 output (falls back to NPZ)"),
    "cupy":           ("12.0", "GPU acceleration (optional)"),
}


def check_python_version() -> dict:
    v = sys.version_info
    ok = v >= (3, 10)
    return {
        "version": f"{v.major}.{v.minor}.{v.micro}",
        "required": ">=3.10",
        "status": "PASS" if ok else "FAIL",
    }


def check_package(name: str, min_version: str) -> dict:
    try:
        mod = __import__(name)
        ver = getattr(mod, "__version__", "unknown")
        # Simple version comparison (major.minor)
        try:
            installed = tuple(int(x) for x in ver.split(".")[:2])
            required = tuple(int(x) for x in min_version.split(".")[:2])
            ok = installed >= required
        except ValueError:
            ok = True  # Can't parse -- assume OK
        return {
            "installed": True,
            "version": ver,
            "required": f">={min_version}",
            "status": "PASS" if ok else "WARN",
        }
    except ImportError:
        return {
            "installed": False,
            "version": None,
            "required": f">={min_version}",
            "status": "MISSING",
        }


def check_gpu() -> dict:
    try:
        import cupy
        n_devices = cupy.cuda.runtime.getDeviceCount()
        return {
            "available": True,
            "devices": n_devices,
            "driver": cupy.cuda.runtime.driverGetVersion(),
        }
    except Exception:
        return {"available": False, "devices": 0, "driver": None}


def main():
    os.makedirs(ATLAS_DIR, exist_ok=True)

    report = {
        "timestamp": datetime.datetime.now().isoformat(),
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "processor": platform.processor(),
        },
        "python": check_python_version(),
        "required_packages": {},
        "optional_packages": {},
        "gpu": check_gpu(),
    }

    all_ok = True

    # Required
    print("  ED-SIM v1 Environment Check")
    print("  " + "=" * 50)
    print()
    print(f"  Python: {report['python']['version']}  "
          f"[{report['python']['status']}]")
    if report["python"]["status"] != "PASS":
        all_ok = False

    print()
    print("  Required packages:")
    for name, min_ver in REQUIRED.items():
        result = check_package(name, min_ver)
        report["required_packages"][name] = result
        status = result["status"]
        ver = result["version"] or "--"
        print(f"    {name:<15} {ver:<12} (>= {min_ver})  [{status}]")
        if status != "PASS":
            all_ok = False

    print()
    print("  Optional packages:")
    for name, (min_ver, purpose) in OPTIONAL.items():
        result = check_package(name, min_ver)
        report["optional_packages"][name] = result
        result["purpose"] = purpose
        status = result["status"]
        ver = result["version"] or "--"
        mark = "+" if result["installed"] else "-"
        print(f"    {mark} {name:<15} {ver:<12} -- {purpose}")

    gpu = report["gpu"]
    print()
    gpu_str = "Available ({} devices)".format(gpu["devices"]) if gpu["available"] else "Not available"
    print(f"  GPU: {gpu_str}")

    # Summary
    report["verdict"] = "PASS" if all_ok else "FAIL"

    print()
    print(f"  Verdict: {report['verdict']}")

    # Save
    out_path = os.path.join(ATLAS_DIR, "environment_check.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"  Report: {out_path}")

    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
