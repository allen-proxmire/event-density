"""
edsim.reproducibility.certificate — Reproducibility certificate objects.

Lightweight, serializable data structures that capture the pass/fail
status and quantitative details of each validation phase.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass
class LawCheck:
    """Result of a single validation phase.

    Attributes
    ----------
    name : str
        Short phase identifier (e.g., "phase_1_attractor_2d").
    description : str
        Human-readable description of what was tested.
    passed : bool
        Whether all checks in this phase passed.
    details : dict[str, Any]
        Quantitative details (metric values, thresholds, etc.).
    """

    name: str
    description: str
    passed: bool
    details: dict = field(default_factory=dict)


@dataclass
class ReproducibilityCertificate:
    """Aggregate result of the full reproducibility pipeline.

    Attributes
    ----------
    version : str
        Platform version identifier.
    timestamp : str
        ISO 8601 timestamp of certificate generation.
    phases : list[LawCheck]
        Results of each validation phase.
    """

    version: str
    timestamp: str
    phases: list = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Serialize the certificate to a JSON-compatible dict."""
        return asdict(self)

    @property
    def n_passed(self) -> int:
        """Number of phases that passed."""
        return sum(1 for p in self.phases if p.passed)

    @property
    def n_failed(self) -> int:
        """Number of phases that failed."""
        return sum(1 for p in self.phases if not p.passed)

    @property
    def all_passed(self) -> bool:
        """Whether all phases passed."""
        return all(p.passed for p in self.phases)

    @property
    def failed_names(self) -> list[str]:
        """Names of failed phases."""
        return [p.name for p in self.phases if not p.passed]

    def summary(self) -> dict[str, Any]:
        """Return a compact summary.

        Returns
        -------
        dict
            version, timestamp, n_phases, n_passed, n_failed, failed_names.
        """
        return {
            "version": self.version,
            "timestamp": self.timestamp,
            "n_phases": len(self.phases),
            "n_passed": self.n_passed,
            "n_failed": self.n_failed,
            "all_passed": self.all_passed,
            "failed_names": self.failed_names,
        }
