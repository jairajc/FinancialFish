"""
Journal -- append-only JSONL log of every simulation run, baseline
computation, resolution, and bet.  Single source of truth for the
evaluator.

Implemented in Phase 1.7.
"""


class Journal:
    def append(self, entry: dict) -> None:
        raise NotImplementedError("Phase 1.7")

    def read_all(self) -> list[dict]:
        raise NotImplementedError("Phase 1.7")
