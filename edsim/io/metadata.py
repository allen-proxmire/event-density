"""
edsim.io.metadata — Run metadata generation.

Captures parameter set, software version, platform info, and timestamps
for reproducibility tracking.
"""

from __future__ import annotations

import platform
import sys
from datetime import datetime, timezone
from typing import Optional

import numpy as np

from ..core.parameters import EDParameters


def build_metadata(
    params: EDParameters,
    extra: Optional[dict] = None,
) -> dict:
    """Build a metadata dictionary for a simulation run.

    Parameters
    ----------
    params : EDParameters
        Simulation parameters.
    extra : dict, optional
        Additional metadata entries.

    Returns
    -------
    dict
        Metadata with keys: ``params``, ``timestamp``, ``platform``,
        ``python_version``, ``numpy_version``, ``edsim_version``, ...
    """
    # TODO: assemble metadata dict
    # - params.to_dict()
    # - datetime.now(timezone.utc).isoformat()
    # - platform.platform()
    # - sys.version
    # - np.__version__
    # - edsim.__version__
    pass
