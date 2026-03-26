"""
Bet recommender -- given an evaluated market, decides whether to bet
and at what size.  Only activated after Phase 3 gate passes.

Implemented in Phase 3+.
"""


class BetRecommender:
    def recommend(self, evaluation: dict) -> dict:
        raise NotImplementedError("Phase 3+")
