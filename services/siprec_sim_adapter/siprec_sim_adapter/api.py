from __future__ import annotations

import time
from pathlib import Path
from typing import Dict, List

from fastapi import FastAPI, HTTPException

from .config import load_settings
from .processor import process_session

app = FastAPI(title="SIPREC Simulation Adapter", version="0.1.0")
settings = load_settings()

@app.get("/healthz")
def healthz() -> Dict[str, str]:
    return {"status": "ok"}

@app.post("/ingest")
def ingest_once() -> Dict[str, List[str]]:
    # Scan inbox for directories containing session.json
    processed: List[str] = []
    for d in sorted(settings.inbox.glob("*")):
        if d.is_dir() and (d / "session.json").exists():
            try:
                vcon_id = process_session(settings, d)
                processed.append(vcon_id)
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))
    return {"processed": processed}

@app.post("/run-once")
def run_once() -> Dict[str, List[str]]:
    # alias to /ingest
    return ingest_once()

@app.post("/poll")
def poll_loop(seconds: int = 30, interval: float = 2.0) -> Dict[str, int]:
    # PoC helper: run a short poll loop
    end = time.time() + seconds
    loops = 0
    while time.time() < end:
        ingest_once()
        time.sleep(interval)
        loops += 1
    return {"loops": loops}
