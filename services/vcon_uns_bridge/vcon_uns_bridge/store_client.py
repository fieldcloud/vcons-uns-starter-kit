from __future__ import annotations

import requests
from typing import Any, Dict, List

def list_changes(vcon_store_url: str, since_ts: int) -> List[Dict[str, Any]]:
    resp = requests.get(f"{vcon_store_url}/vcons/changes", params={"since": since_ts}, timeout=10)
    resp.raise_for_status()
    return resp.json()

def fetch_vcon(vcon_store_url: str, vcon_id: str) -> Dict[str, Any]:
    resp = requests.get(f"{vcon_store_url}/vcons/{vcon_id}", timeout=10)
    resp.raise_for_status()
    return resp.json()
