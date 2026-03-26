"""
Market scanner -- fetches active prediction markets from Polymarket
and applies the hard doctrine filter before any simulation work begins.

Implemented in Phase 1.1.
"""


class MarketScanner:
    def scan(self) -> list[dict]:
        raise NotImplementedError("Phase 1.1")
