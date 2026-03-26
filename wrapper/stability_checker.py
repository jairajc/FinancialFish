"""
Stability checker -- analyses multi-run variance and drift to classify
each market as STABLE, MARGINAL, or UNSTABLE.

UNSTABLE and DRIFT_SENSITIVE markets are excluded from all edge
calculations, Brier evaluations, and betting eligibility.

Implemented in Phase 1.6.
"""


class StabilityChecker:
    def check(self, ensemble: dict) -> dict:
        raise NotImplementedError("Phase 1.6")
