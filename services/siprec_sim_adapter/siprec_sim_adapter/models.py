from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional

class SiprecSessionMetadata(BaseModel):
    call_id: str = Field(..., description="Unique id for the SIPREC session (simulated)")
    from_uri: str = Field(..., alias="from", description="Caller SIP URI")
    to_uri: str = Field(..., alias="to", description="Callee SIP URI")
    start_time: str
    end_time: str
    asset_hint: Optional[str] = Field(default=None, description="Optional asset key like pump07")
    conversation_type: Optional[str] = Field(default="troubleshooting")
    notes: Optional[str] = None
