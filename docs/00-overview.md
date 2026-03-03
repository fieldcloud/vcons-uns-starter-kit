# Overview

## What is the Operational Knowledge Fabric (OKF)?

OKF is a practical way to treat **human conversations** as part of the same contextual fabric as
**machine data** in industrial environments.

The idea is simple:

- Machines produce events (telemetry, alarms, state)
- Humans produce *understanding* (reasoning, coordination, intent)
- Today, we capture the first category very well — and largely discard the second

OKF uses two building blocks:

1) **vCons** (virtualized conversations)  
   A structured, machine-readable container for a conversation:
   metadata + transcript/dialog + attachments + governance.

2) **Unified Namespace (UNS)**  
   A pub/sub event backbone (typically MQTT) organized by a semantic hierarchy (often ISA-95):
   `enterprise/site/area/line/asset/...`

## The “pointer-not-payload” rule

MQTT is great for small, routable events.
It is usually the wrong place to put:
- large media
- long transcripts
- sensitive attachments

So OKF uses MQTT to publish **pointers + summaries**, while storing
the full vCon content in a **governed vCon store**.

## Who benefits?

- **Telecom builders**: adapters and mediation become high-value industrial integrations
- **OT practitioners**: faster troubleshooting, less repeated failure, preserved know-how
- **IT/security**: traceability, evidence, and governance aligned to modern compliance requirements

## What this repo is (and isn’t)

This repo is:
- a public starter kit for PoCs and hackathon builds
- documentation + skeleton code + prompts

This repo is not:
- a surveillance toolkit
- a production-ready industrial capture platform

Use synthetic/anonymized data only.
