"""
Baseline models -- the architecture justification layer.

Four cheap comparison models that every simulation must beat to prove
MiroFish adds value beyond what simpler approaches already provide:
  1. Market price (free)
  2. Market + recency (one LLM call)
  3. LLM-only (same context, no simulation)
  4. RAG-only (retrieve + summarise, no simulation)

Implemented in Phase 1.5.
"""


class Baselines:
    def compute_all(self, market: dict, context_docs: list[str]) -> dict:
        raise NotImplementedError("Phase 1.5")
