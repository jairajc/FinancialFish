"""
Centralised configuration for the Prediction Market Oracle wrapper.

Loads values from the project-root .env file (shared with MiroFish)
and exposes them as plain attributes on a frozen Config dataclass.
"""

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJECT_ROOT / ".env", override=True)


@dataclass(frozen=True)
class Config:
    mirofish_base_url: str = os.environ.get(
        "MIROFISH_BASE_URL", "http://localhost:5001"
    )
    polymarket_gamma_url: str = os.environ.get(
        "POLYMARKET_GAMMA_URL", "https://gamma-api.polymarket.com"
    )
    polymarket_clob_url: str = os.environ.get(
        "POLYMARKET_CLOB_URL", "https://clob.polymarket.com"
    )

    llm_api_key: str = os.environ.get("LLM_API_KEY", "")
    llm_base_url: str = os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1")
    llm_model_name: str = os.environ.get("LLM_MODEL_NAME", "gpt-4o-mini")

    data_dir: Path = Path(
        os.environ.get("WRAPPER_DATA_DIR", str(_PROJECT_ROOT / "wrapper" / "data"))
    )

    @property
    def runs_dir(self) -> Path:
        return self.data_dir / "runs"

    @property
    def journal_path(self) -> Path:
        return self.data_dir / "journal.jsonl"

    @property
    def baselines_path(self) -> Path:
        return self.data_dir / "baselines.jsonl"


cfg = Config()
