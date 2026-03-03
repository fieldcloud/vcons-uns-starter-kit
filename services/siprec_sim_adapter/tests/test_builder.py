from siprec_sim_adapter.models import SiprecSessionMetadata
from siprec_sim_adapter.vcon_builder import build_vcon
from pathlib import Path

def test_build_vcon_minimal():
    meta = SiprecSessionMetadata.model_validate({
        "call_id": "CALL-TEST",
        "from": "sip:a@example",
        "to": "sip:b@example",
        "start_time": "2026-01-01T00:00:00Z",
        "end_time": "2026-01-01T00:01:00Z",
        "asset_hint": "pump07",
        "conversation_type": "troubleshooting",
    })
    v = build_vcon(meta, Path("/tmp/audio.wav"))
    assert v["uuid"] == "CALL-TEST"
    assert v["extensions"]["okf"]["asset_hint"] == "pump07"
