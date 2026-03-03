# Governance & Security

This repo is designed to *demonstrate* governance principles early, even in PoC mode.

## 1) What this is NOT

- surveillance
- productivity scoring
- secret monitoring

## 2) What this IS

- institutional memory (traceable reasoning)
- decision context for operational events
- governed evidence for audits, incident response, and continuity

## 3) Minimum governance controls (PoC)

- **Consent / lawful basis flags** stored with vCons
- **Role-based access control** (at least: admin vs viewer)
- **Retention** (time-bound; easy deletion in PoC)
- **Redaction / pseudonymization** capability (even if manual in PoC)
- **Audit logging** of read/write access (stretch)

## 4) Zones & conduits (industrial acceptance)

Industrial environments commonly separate systems into zones (e.g., safety, control, supervisory, enterprise).
A safe rule of thumb:

- Safety-critical zones: **no direct capture**, metadata-only links
- Supervisory/IT zones: controlled capture and storage with explicit conduits
- Cross-zone information flow must be explicit and minimal

## 5) Pointer-not-payload (security-friendly)

Publish small UNS events to MQTT:
- id
- pointer
- summary
- timestamps

Store full content under access control:
- transcripts
- media
- attachments

## 6) Data hygiene rules (for contributors)

- Use synthetic/anonymized data only
- Don’t commit phone numbers, emails, or real identities
- Prefer participant **roles** (operator, engineer, vendor)
