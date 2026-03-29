"""
edsim.manuscript — Automated manuscript generation for ED-SIM-02.

Provides modular section generators, figure builders, and a
build script that assembles a publication-ready Markdown draft.
"""

from .build import build_manuscript

__all__ = ["build_manuscript"]
