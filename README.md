# Operational Knowledge Fabric (OKF) Starter Kit
### vCons + Unified Namespace (UNS) for Industry — built by telecom makers

This repository is a **starter kit** for building proof-of-concept components that turn **human conversations**
(SIP calls, Teams calls, radio traffic) into **governed, structured vCons**, and then publish **human events**
into a **Unified Namespace (UNS)**.

It is designed for:
- telecom application developers / makers (CPaaS, SIP, WebRTC, VoIP, SBC ecosystems)
- OT/IT-curious builders who want to learn industrial patterns (UNS, asset context, event-driven architectures)
- hackathons (e.g., **VCONIC TADHack**)

## The idea (in one minute)

Factories are full of telemetry and alarms — but the *reasoning* behind decisions lives in conversations:
shift handovers, troubleshooting calls, vendor escalations, and Teams chats.

**OKF** treats conversations as a first-class, governed data type:
- **vCon** is the structured conversation container (metadata + transcript + attachments + governance)
- **UNS** is the event backbone (MQTT topics + consumers that persist/query context)

## What’s in this repo

- `docs/` — short READMEs that explain architecture, data models, governance, and PoC steps
- `services/` — skeleton code for adapters and glue services (Python-first, easy to generate/extend with Codex)
- `samples/` — sample inputs for simulated SIPREC sessions (metadata + placeholder audio)
- `podman-compose.yml` — a local stack you can run to validate flows (MQTT + stores + bridge)

## Quickstart (conceptual PoC)

> Goal: take a simulated SIPREC session (metadata + WAV), create a vCon, store it, publish a UNS event.

1) Install prerequisites
- Podman + podman-compose
- (Optional) Python 3.12 if you want to run services outside containers

2) Copy env template
```bash
cp .env.example .env
```

3) Bring up the stack
```bash
podman-compose up -d --build
```

4) Drop a simulated SIPREC session
```bash
cp -r samples/siprec_sessions/session_001 ./runtime/inbox/
```

5) Observe MQTT topics (example)
```bash
# install mosquitto-clients locally, then:
mosquitto_sub -h localhost -p 1883 -t "acme/#" -v
```

## Repo layout

```text
.
├── docs/
│   ├── 00-overview.md
│   ├── 01-architecture.md
│   ├── 02-data-model.md
│   ├── 03-governance-security.md
│   ├── 04-poc-playbook.md
│   ├── 05-codex-prompt-pack.md
│   ├── 06-tadhack-challenge-brief.md
│   └── 07-roadmap.md
├── services/
│   ├── vcon_store_stub/        # simple REST store for PoC
│   ├── siprec_sim_adapter/     # folder-watch SIPREC simulation -> vCon
│   └── vcon_uns_bridge/        # publish pointer+summary to MQTT UNS
├── samples/
│   └── siprec_sessions/
├── schemas/
│   └── uns_vcon_event.schema.json
├── podman-compose.yml
└── .env.example
```

## Design principles (Legacy Lift aligned)

- **Non-disruptive**: don’t replace OT systems — add context
- **Pointer-not-payload**: MQTT carries small event messages; the vCon store carries transcripts/media
- **Governance-first**: consent/retention/RBAC/redaction are part of the design, not a bolt-on
- **Zones & conduits aware**: don’t move sensitive data across boundaries accidentally

## Contributing

See:
- `CONTRIBUTING.md` (how to contribute)
- `docs/06-tadhack-challenge-brief.md` (hack targets)
- `docs/05-codex-prompt-pack.md` (prompts to generate clean services/specs)

## License

MIT — see `LICENSE`.

## Links

- vCon project: https://github.com/vcon-dev/vcon
- Unified Namespace reference implementation: https://github.com/mkashwin/unifiednamespace
- VCONIC TADHack: https://blog.tadhack.com/2025/12/19/vconic-tadhack/
