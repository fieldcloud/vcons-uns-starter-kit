from __future__ import annotations

import json
from typing import Any, Dict, Optional

import paho.mqtt.client as mqtt

class MqttPublisher:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    def connect(self) -> None:
        self.client.connect(self.host, self.port, keepalive=30)

    def publish_json(self, topic: str, payload: Dict[str, Any], qos: int = 1) -> None:
        data = json.dumps(payload, ensure_ascii=False)
        result = self.client.publish(topic, data, qos=qos)
        result.wait_for_publish()
