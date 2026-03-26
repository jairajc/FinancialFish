"""
Scenario packager -- expands a market question into a MiroFish-ready
simulation seed: requirement text, context documents, and metadata.

Implemented in Phase 1.2.
"""


class ScenarioPackager:
    def package(self, market: dict) -> dict:
        raise NotImplementedError("Phase 1.2")
