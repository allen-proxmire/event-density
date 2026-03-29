"""
edsim.ci.config — CI/CD configuration constants and diagnostics.

Provides version constraints, backend availability checks, and
a diagnostic printer for CI environments.
"""

from __future__ import annotations

import platform
import sys

# Python versions tested in CI
CI_PYTHON_VERSIONS = ["3.10", "3.11", "3.12"]

# Minimum required versions
MIN_NUMPY_VERSION = "1.22"
MIN_SCIPY_VERSION = "1.8"


def print_ci_info() -> None:
    """Print version and backend availability information.

    Useful in CI logs for diagnosing environment issues.
    """
    from ..version import VERSION, CODENAME
    import numpy as np
    import scipy

    print(f"{'Package:':<16s} {CODENAME} v{VERSION}")
    print(f"{'Python:':<16s} {sys.version}")
    print(f"{'Platform:':<16s} {platform.platform()}")
    print(f"{'NumPy:':<16s} {np.__version__}")
    print(f"{'SciPy:':<16s} {scipy.__version__}")

    # Backend availability
    try:
        import matplotlib
        mpl_ver = matplotlib.__version__
    except ImportError:
        mpl_ver = "not installed"
    print(f"{'Matplotlib:':<16s} {mpl_ver}")

    try:
        from ..performance.numba_backend import NUMBA_AVAILABLE
        if NUMBA_AVAILABLE:
            import numba
            print(f"{'Numba:':<16s} {numba.__version__}")
        else:
            print(f"{'Numba:':<16s} not installed")
    except ImportError:
        print(f"{'Numba:':<16s} not installed")

    try:
        from ..performance.jax_backend import JAX_AVAILABLE
        if JAX_AVAILABLE:
            import jax
            print(f"{'JAX:':<16s} {jax.__version__}")
        else:
            print(f"{'JAX:':<16s} not installed")
    except ImportError:
        print(f"{'JAX:':<16s} not installed")

    # Test suite info
    try:
        import pytest
        print(f"{'pytest:':<16s} {pytest.__version__}")
    except ImportError:
        print(f"{'pytest:':<16s} not installed")


def _version_tuple(v: str) -> tuple:
    """Parse a version string like '1.22.3' into a comparable tuple (1, 22, 3)."""
    parts = []
    for p in v.split(".")[:3]:
        digits = ""
        for ch in p:
            if ch.isdigit():
                digits += ch
            else:
                break
        parts.append(int(digits) if digits else 0)
    return tuple(parts)


def check_environment() -> dict:
    """Check that the CI environment meets minimum requirements.

    Returns
    -------
    dict
        {"ok": bool, "issues": list[str]}
    """
    issues = []

    # Python version
    py_ver = f"{sys.version_info.major}.{sys.version_info.minor}"
    if sys.version_info < (3, 10):
        issues.append(f"Python {py_ver} < 3.10 (minimum required)")

    # NumPy
    try:
        import numpy as np
        if _version_tuple(np.__version__) < _version_tuple(MIN_NUMPY_VERSION):
            issues.append(f"NumPy {np.__version__} < {MIN_NUMPY_VERSION}")
    except ImportError:
        issues.append("NumPy not installed")

    # SciPy
    try:
        import scipy
        if _version_tuple(scipy.__version__) < _version_tuple(MIN_SCIPY_VERSION):
            issues.append(f"SciPy {scipy.__version__} < {MIN_SCIPY_VERSION}")
    except ImportError:
        issues.append("SciPy not installed")

    return {"ok": len(issues) == 0, "issues": issues}
