# Architecture

This document describes the reference architecture used by this starter kit.

## Layers (conceptual)

1) Capture Layer  
   - SIPREC (simulated feed for PoC)
   - Microsoft Teams ad hoc calls (fixture-based first)
   - (Stretch) trunked/two-way radio via SIP bridge

2) Linkage & Enrichment Layer  
   - attach transcripts (WTF)
   - classify conversation type (handover, troubleshooting, vendor support)
   - map to industrial context (asset path, work order id, alarm id)

3) Storage & Federation Layer  
   - vCon store: governed storage for vCon JSON + media/transcripts
   - metadata index (optional): accelerate search and discovery

4) Application Layer  
   - UNS consumers (graph/historian)
   - GraphQL API
   - UI / search / RCA / training
   - later: copilots / AI agents

## Core dataflow

```text
[SIPREC/Teams capture] -> [adapter] -> [vCon store]
                                    |
                                    +-> publish pointer+summary -> [MQTT UNS]
                                                              |
                                                              +-> [graph/historian/query/UI]
```

### Why “pointer + summary” to MQTT?

Because it:
- keeps MQTT payloads small and reliable
- avoids pushing sensitive transcripts everywhere
- aligns with zones/conduits thinking (don’t leak data across boundaries)

## Service map in this repo

- `services/vcon_store_stub`  
  A minimal PoC REST API for storing and retrieving vCon documents.

- `services/siprec_sim_adapter`  
  Watches a folder for `session.json + audio.wav`, creates a vCon, stores it.

- `services/vcon_uns_bridge`  
  Polls vCon store for new/updated vCons, maps to UNS topics, publishes MQTT events.

## Stretch targets

- Radio via SIP bridge  
  Treat talkgroups as SIP endpoints → capture audio → normalize into vCons.

- UNS consumers  
  Subscribe to `.../vcon/*` topics and persist into Neo4j/Timescale for queries.

- Integrity receipts (SCITT-inspired)  
  Append-only lifecycle events for auditability across transcription/redaction/publication.
