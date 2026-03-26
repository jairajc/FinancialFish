"""
Simulation runner -- drives MiroFish's REST API end-to-end for a
single scenario, with support for running N independent times to
produce an ensemble.

Implemented in Phase 1.3.
"""


class SimulationRunner:
    def run_once(self, scenario: dict) -> dict:
        raise NotImplementedError("Phase 1.3")

    def run_n_times(self, scenario: dict, n: int = 3) -> list[dict]:
        raise NotImplementedError("Phase 1.3")
