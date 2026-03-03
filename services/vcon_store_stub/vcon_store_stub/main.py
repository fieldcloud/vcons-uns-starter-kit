from __future__ import annotations

import json
import os
import time
import uuid
from hashlib import sha256
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

app = FastAPI(title="vCon Store Stub", version="0.1.0")

def _store_path() -> Path:
    p = Path(os.environ.get("STORE_PATH", "/data"))
    p.mkdir(parents=True, exist_ok=True)
    return p

def _canonical_json(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def _revision_hash(vcon_obj: Dict[str, Any]) -> str:
    return sha256(_canonical_json(vcon_obj)).hexdigest()

@app.get("/healthz")
def healthz() -> Dict[str, str]:
    return {"status": "ok"}

@app.get("/vcons")
def list_vcons(limit: int = 200) -> List[Dict[str, Any]]:
    files = sorted(_store_path().glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    out: List[Dict[str, Any]] = []
    for p in files[:limit]:
        out.append({
            "vcon_id": p.stem,
            "modified_at": int(p.stat().st_mtime),
        })
    return out

@app.get("/vcons/changes")
def changes_since(
    since: int = Query(..., description="Unix timestamp (seconds). Return vCons modified after this time."),
    limit: int = 200,
) -> List[Dict[str, Any]]:
    files = sorted(_store_path().glob("*.json"), key=lambda p: p.stat().st_mtime)
    out: List[Dict[str, Any]] = []
    for p in files:
        mtime = int(p.stat().st_mtime)
        if mtime > since:
            out.append({"vcon_id": p.stem, "modified_at": mtime})
    return out[-limit:]

@app.get("/vcons/{vcon_id}")
def get_vcon(vcon_id: str) -> Dict[str, Any]:
    p = _store_path() / f"{vcon_id}.json"
    if not p.exists():
        raise HTTPException(status_code=404, detail="vCon not found")
    return json.loads(p.read_text(encoding="utf-8"))

@app.post("/vcons")
def create_or_update_vcon(vcon: Dict[str, Any]) -> JSONResponse:
    vcon_id = vcon.get("uuid") or vcon.get("vcon_id") or str(uuid.uuid4())

    # Minimal metadata we add in the stub
    vcon.setdefault("uuid", vcon_id)
    vcon["_stored_at"] = int(time.time())
    vcon["_revision_hash"] = _revision_hash(vcon)

    p = _store_path() / f"{vcon_id}.json"
    p.write_text(json.dumps(vcon, indent=2, ensure_ascii=False), encoding="utf-8")

    return JSONResponse({"vcon_id": vcon_id, "revision_hash": vcon["_revision_hash"]}, status_code=201)
