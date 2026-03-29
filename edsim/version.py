"""
edsim.version — Version information for ED-SIM-02.
"""

VERSION = "0.1.0"
VERSION_TUPLE = (0, 1, 0)
CODENAME = "ED-SIM-02"


def get_version() -> str:
    """Return the version string."""
    return VERSION


def get_version_info() -> dict:
    """Return version metadata as a dict."""
    return {
        "version": VERSION,
        "codename": CODENAME,
        "major": VERSION_TUPLE[0],
        "minor": VERSION_TUPLE[1],
        "patch": VERSION_TUPLE[2],
    }
