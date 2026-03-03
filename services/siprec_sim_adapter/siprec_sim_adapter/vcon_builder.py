from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from .models import SiprecSessionMetadata

def build_vcon(meta: SiprecSessionMetadata, audio_path: Path) -> Dict[str, Any]:
    """Build a minimal vCon JSON document.

    NOTE: This is intentionally minimal for PoC. In a production build,
    you should use vcon-lib to construct and validate the vCon object.
    """

    vcon: Dict[str, Any] = {
        "uuid": f"{meta.call_id}",
        "parties": [
            {"name": "Operator", "role": "operator", "contact": meta.from_uri},
            {"name": "Support", "role": "vendor", "contact": meta.to_uri},
        ],
        "start_time": meta.start_time,
        "end_time": meta.end_time,
        "dialogs": [
            {
                "speaker": 0,
                "text": "(Audio captured via SIPREC simulation; transcript pending)",
            }
        ],
        "attachments": [
            {
                "type": "audio/wav",
                "name": audio_path.name,
                "url": f"file://{audio_path}",
            }
        ],
        "extensions": {
            "okf": {
                "source": "siprec_sim",
                "source_ref": meta.call_id,
                "asset_hint": meta.asset_hint,
                "conversation_type": meta.conversation_type or "troubleshooting",
            }
        }
    }
    return vcon
