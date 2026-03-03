# Roadmap

This repo is a starter kit. Suggested phases:

## Phase 0 — Starter kit (this repo)
- vCon store stub
- SIPREC simulation adapter skeleton
- vCon → UNS bridge skeleton
- basic docs + prompt pack

## Phase 1 — Capture adapters
- SIPREC adapter improvements (real SIPREC metadata ingestion)
- Teams ad hoc adapter (fixture-based -> real API)
- radio via SIP bridge (stretch)

## Phase 2 — UNS persistence
- Neo4j consumer for vCon topics
- TimescaleDB consumer for vCon events
- Basic GraphQL queries

## Phase 3 — Minimal UI
- asset → vCons list
- vCon detail view
- participant masking toggle

## Phase 4 — Governance hardening
- RBAC + auth
- retention policies
- redaction workflow
- audit logs

## Phase 5 — Integrity receipts (SCITT-inspired)
- lifecycle events: created/transcribed/redacted/published/deleted
- append-only log for provenance and transparency

## Phase 6 — Production candidate (beyond this repo)
- hardened deployment
- multi-site patterns
- integrations to real OT/IT systems
