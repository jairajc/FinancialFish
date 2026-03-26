"""
Evaluator -- computes Brier scores, calibration curves, incremental
value vs baselines, hypothetical PnL, and the economic viability
ratio.  Operates on windowed subsets of the journal.

Implemented in Phase 1.7.
"""


class Evaluator:
    def evaluate(self, journal_entries: list[dict]) -> dict:
        raise NotImplementedError("Phase 1.7")
