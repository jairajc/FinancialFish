"""
Market doctrine -- hard kill-list, eligibility rules, and the
narrative-driver classifier that decides whether a market's resolution
depends on social dynamics MiroFish can actually model.

Implemented in Phase 1.1.
"""


class MarketDoctrine:
    def is_eligible(self, market: dict) -> tuple[bool, str]:
        raise NotImplementedError("Phase 1.1")

    def classify_driver(self, market: dict) -> str:
        raise NotImplementedError("Phase 1.1")
