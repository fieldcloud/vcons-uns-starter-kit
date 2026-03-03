from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Settings:
    vcon_store_url: str
    mqtt_host: str
    mqtt_port: int
    mqtt_topic_root: str
    asset_map_path: Path

def load_settings() -> Settings:
    return Settings(
        vcon_store_url=os.environ.get("VCON_STORE_URL", "http://localhost:8000"),
        mqtt_host=os.environ.get("MQTT_HOST", "localhost"),
        mqtt_port=int(os.environ.get("MQTT_PORT", "1883")),
        mqtt_topic_root=os.environ.get("MQTT_TOPIC_ROOT", "acme/site1"),
        asset_map_path=Path(os.environ.get("ASSET_MAP_PATH", "/app/config/asset_map.yaml")),
    )
