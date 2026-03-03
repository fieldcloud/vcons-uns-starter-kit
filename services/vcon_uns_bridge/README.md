# vCon -> UNS Bridge

This service polls the vCon store and publishes **pointer + summary** events into an MQTT Unified Namespace.

## Endpoints

- `GET /healthz`
- `POST /poll-once` — poll for new/updated vCons and publish MQTT events

## MQTT Topics

By default:

```text
<asset_path>/vcon/created
<asset_path>/vcon/summary
```

Payload is validated conceptually against `schemas/uns_vcon_event.schema.json`.

## Notes

- This is PoC-grade code.
- Idempotency is minimal (revision hash is included but not persisted yet).
- A production bridge should persist a cursor and dedupe state.
