from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Settings:
    vcon_store_url: str
    inbox: Path
    archive: Path

def load_settings() -> Settings:
    vcon_store_url = os.environ.get("VCON_STORE_URL", "http://localhost:8000")
    inbox = Path(os.environ.get("SIPREC_INBOX", "/data/inbox"))
    archive = Path(os.environ.get("SIPREC_ARCHIVE", "/data/archive"))
    inbox.mkdir(parents=True, exist_ok=True)
    archive.mkdir(parents=True, exist_ok=True)
    return Settings(vcon_store_url=vcon_store_url, inbox=inbox, archive=archive)
