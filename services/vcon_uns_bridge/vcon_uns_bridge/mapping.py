from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

import yaml

@dataclass
class AssetMap:
    topic_root: str
    assets: Dict[str, str]  # key -> asset_path

def load_asset_map(path: Path, default_topic_root: str) -> AssetMap:
    obj = yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}
    defaults = obj.get("defaults", {})
    topic_root = defaults.get("topic_root", default_topic_root)

    assets: Dict[str, str] = {}
    for key, entry in (obj.get("assets", {}) or {}).items():
        if isinstance(entry, dict) and entry.get("asset_path"):
            assets[key] = entry["asset_path"]
    return AssetMap(topic_root=topic_root, assets=assets)

def resolve_asset_path(vcon: Dict[str, Any], asset_map: AssetMap) -> Optional[str]:
    okf = ((vcon.get("extensions") or {}).get("okf") or {})
    # preferred: explicit asset_path
    asset_path = okf.get("asset_path")
    if asset_path:
        return asset_path

    # fallback: asset_hint -> mapping file
    asset_hint = okf.get("asset_hint")
    if asset_hint and asset_hint in asset_map.assets:
        return asset_map.assets[asset_hint]

    return None
