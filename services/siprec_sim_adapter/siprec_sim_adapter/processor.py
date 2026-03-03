from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Optional

from .config import Settings
from .models import SiprecSessionMetadata
from .store_client import post_vcon
from .vcon_builder import build_vcon

def _load_meta(session_dir: Path) -> SiprecSessionMetadata:
    meta_path = session_dir / "session.json"
    meta_obj = json.loads(meta_path.read_text(encoding="utf-8"))
    return SiprecSessionMetadata.model_validate(meta_obj)

def find_audio(session_dir: Path) -> Optional[Path]:
    # PoC: expect audio.wav, but allow any .wav
    candidates = list(session_dir.glob("*.wav"))
    if candidates:
        return candidates[0]
    wav = session_dir / "audio.wav"
    return wav if wav.exists() else None

def process_session(settings: Settings, session_dir: Path) -> str:
    meta = _load_meta(session_dir)
    audio = find_audio(session_dir)
    if audio is None or not audio.exists():
        raise FileNotFoundError(f"Missing audio wav in {session_dir}")

    vcon = build_vcon(meta, audio)
    result = post_vcon(settings.vcon_store_url, vcon)

    # Archive session after successful upload
    dest = settings.archive / session_dir.name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.move(str(session_dir), str(dest))

    return result.get("vcon_id", meta.call_id)
