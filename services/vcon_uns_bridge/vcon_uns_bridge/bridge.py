from __future__ import annotations

import time
from hashlib import sha256
from typing import Any, Dict, Optional

from .mapping import AssetMap, resolve_asset_path
from .mqtt_pub import MqttPublisher

def _iso(v: Any) -> str:
    return str(v) if v is not None else ""

def _revision_hash(vcon: Dict[str, Any]) -> str:
    # Use store-provided revision if present, else hash canonical-ish repr
    if vcon.get("_revision_hash"):
        return str(vcon["_revision_hash"])
    raw = repr(sorted(vcon.items())).encode("utf-8")
    return sha256(raw).hexdigest()

def build_uns_payload(vcon: Dict[str, Any], asset_path: str, vcon_store_url: str) -> Dict[str, Any]:
    okf = ((vcon.get("extensions") or {}).get("okf") or {})
    start = vcon.get("start_time") or okf.get("start_time") or ""
    end = vcon.get("end_time") or okf.get("end_time") or ""

    # PoC summary: first dialog text
    dialogs = vcon.get("dialogs") or []
    summary = ""
    if dialogs and isinstance(dialogs, list):
        d0 = dialogs[0] if dialogs else {}
        summary = (d0.get("text") or "")[:240]

    return {
        "vcon_id": vcon.get("uuid") or vcon.get("vcon_id"),
        "asset_path": asset_path,
        "conversation_type": okf.get("conversation_type") or "unknown",
        "vcon_ref": f"{vcon_store_url}/vcons/{vcon.get('uuid') or vcon.get('vcon_id')}",
        "start": start,
        "end": end,
        "summary": summary,
        "revision_hash": _revision_hash(vcon),
    }

def publish_vcon_events(
    publisher: MqttPublisher,
    asset_map: AssetMap,
    vcon: Dict[str, Any],
    vcon_store_url: str,
    default_topic_root: str,
) -> Optional[str]:
    asset_path = resolve_asset_path(vcon, asset_map)
    if asset_path is None:
        return None

    payload = build_uns_payload(vcon, asset_path, vcon_store_url)

    topic_prefix = asset_path
    # If asset_path is just a key, prefix it
    if "/" not in topic_prefix:
        topic_prefix = f"{default_topic_root}/{topic_prefix}"

    publisher.publish_json(f"{topic_prefix}/vcon/created", payload)
    publisher.publish_json(f"{topic_prefix}/vcon/summary", payload)

    return topic_prefix
