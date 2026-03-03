from __future__ import annotations

from typing import Any, Dict
import requests

def post_vcon(vcon_store_url: str, vcon: Dict[str, Any]) -> Dict[str, Any]:
    resp = requests.post(f"{vcon_store_url}/vcons", json=vcon, timeout=10)
    resp.raise_for_status()
    return resp.json()
