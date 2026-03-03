# PoC Playbook (Podman Compose)

This is a practical step-by-step to validate the starter kit.

## 0) Prerequisites

- Podman + podman-compose installed
- `mosquitto-clients` installed locally (for MQTT subscribe testing)

## 1) Configure

```bash
cp .env.example .env
```

## 2) Run the stack

```bash
podman-compose up -d --build
```

Check services:
- EMQX dashboard: http://localhost:18083
- vCon store stub: http://localhost:8000/docs

## 3) Feed a simulated SIPREC session

Copy sample session into the inbox:

```bash
mkdir -p runtime/inbox runtime/archive
cp -r samples/siprec_sessions/session_001 runtime/inbox/
```

The SIPREC adapter should:
- detect the session folder
- create a vCon JSON
- POST to the vCon store stub

## 4) Confirm vCon stored

List vCons:

```bash
curl -s http://localhost:8000/vcons | jq .
```

Fetch by id:

```bash
curl -s http://localhost:8000/vcons/<id> | jq .
```

## 5) Confirm MQTT UNS events

Subscribe:

```bash
mosquitto_sub -h localhost -p 1883 -t "acme/#" -v
```

You should see:
- `.../vcon/created`
- `.../vcon/summary`

## 6) Next steps

- implement a real Teams adapter (fixture-based first)
- add a Neo4j consumer for vCon topics
- add a minimal UI (asset → conversations)
