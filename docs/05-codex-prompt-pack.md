# Codex Prompt Pack

These prompts are designed to generate clean, testable code and specs.

## Prompt 1: System-level functional spec

You are a principal engineer. Write a Functional Requirements Specification for a PoC that integrates:
- SIPREC (simulated) -> vCon
- Teams ad hoc calls -> vCon (fixture-based)
- vCon store with basic governance (RBAC/retention placeholders)
- MQTT publishing to a Unified Namespace (pointer + summary events)
- Optional consumers for Neo4j/Timescale and GraphQL

Include:
- personas + user journeys
- system boundaries + trust zones
- data model (vCon + UNS event schema)
- acceptance tests / demo criteria
Output Markdown.

## Prompt 2: Build siprec_sim_adapter (Python 3.12)

Create a Python 3.12 service called siprec_sim_adapter:
- Watches /data/inbox for session folders
- Each session contains session.json and audio.wav
- Builds a vCon using the vcon library
- Stores vCon JSON + attachment references
- Posts to VCON_STORE_URL via REST
- Emits structured logs and health endpoint

Constraints:
- ruff, mypy, pytest
- Dockerfile/Containerfile + podman-compose snippet
- README with run/test commands

## Prompt 3: Build vcon_uns_bridge

Create a Python 3.12 service called vcon_uns_bridge:
- Polls VCON_STORE_URL for new/updated vCons
- Computes a revision_hash to prevent duplicate publishing
- Maps vCons to asset_path via:
  - extensions.okf.asset_path (preferred)
  - fallback mapping file asset_map.yaml
- Publishes MQTT events:
  - /vcon/created
  - /vcon/summary
- Uses pointer-not-payload rule (no transcripts on MQTT)
- Includes /healthz and /metrics

## Prompt 4 (stretch): radio_sip_adapter

Create a service that ingests:
- half-duplex PTT style audio segments
- a talkgroup identifier

Normalizes into vCons:
- separate dialog segments by PTT boundaries
- publishes into UNS under asset_path or talkgroup_path
