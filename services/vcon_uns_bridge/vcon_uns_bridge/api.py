from __future__ import annotations

import time
from typing import Dict, List

from fastapi import FastAPI

from .config import load_settings
from .mapping import load_asset_map
from .mqtt_pub import MqttPublisher
from .store_client import list_changes, fetch_vcon
from .bridge import publish_vcon_events

app = FastAPI(title="vCon -> UNS Bridge", version="0.1.0")
settings = load_settings()
asset_map = load_asset_map(settings.asset_map_path, settings.mqtt_topic_root)

publisher = MqttPublisher(settings.mqtt_host, settings.mqtt_port)
publisher.connect()

# naive in-memory cursor for PoC
LAST_TS = int(time.time()) - 3600

@app.get("/healthz")
def healthz() -> Dict[str, str]:
    return {"status": "ok"}

@app.post("/poll-once")
def poll_once() -> Dict[str, List[str]]:
    global LAST_TS
    changes = list_changes(settings.vcon_store_url, LAST_TS)
    published: List[str] = []

    # Update cursor to "now" before processing to avoid tight loops on failure
    LAST_TS = int(time.time())

    for item in changes:
        vcon_id = item["vcon_id"]
        vcon = fetch_vcon(settings.vcon_store_url, vcon_id)
        topic_prefix = publish_vcon_events(
            publisher=publisher,
            asset_map=asset_map,
            vcon=vcon,
            vcon_store_url=settings.vcon_store_url,
            default_topic_root=settings.mqtt_topic_root,
        )
        if topic_prefix:
            published.append(topic_prefix)

    return {"published": published}
