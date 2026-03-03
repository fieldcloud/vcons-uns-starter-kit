# Data model

This starter kit keeps data modeling intentionally simple.

## 1) vCon minimum fields (PoC)

For PoC, treat vCons as JSON documents with:

- `uuid`: stable identifier
- `parties`: participants (use roles, not personal identities)
- `start_time`, `end_time`
- `dialogs`: transcript or placeholder dialog entries
- `attachments`: references to media/transcripts
- `extensions.okf`: OKF-specific context (asset mapping, conversation type)

### OKF extension (suggested)

```json
{
  "extensions": {
    "okf": {
      "asset_path": "acme/site1/areaA/line3/pump07",
      "conversation_type": "troubleshooting",
      "source": "siprec_sim",
      "source_ref": "call-id-or-meeting-id"
    }
  }
}
```

## 2) UNS topic conventions

We recommend ISA-95 style hierarchy:

```text
enterprise/site/area/line/asset/...
```

Add vCon events under an asset path:

```text
acme/site1/areaA/line3/pump07/vcon/created
acme/site1/areaA/line3/pump07/vcon/summary
acme/site1/areaA/line3/pump07/vcon/linked/workorder/12345
```

## 3) UNS event payload (pointer + summary)

Keep MQTT payload small:

Required:
- `vcon_id`
- `asset_path`
- `conversation_type`
- `vcon_ref` (URL to vCon store)
- `start`, `end` (ISO 8601)

Optional:
- `summary`
- `participants` (roles only)
- `tags`
- `revision_hash`

A JSON Schema is provided in `schemas/uns_vcon_event.schema.json`.

## 4) Asset mapping (asset_map.yaml)

For PoC, mapping can be static:

```yaml
# config/asset_map.yaml
defaults:
  enterprise: acme
  site: site1

assets:
  pump07:
    asset_path: "acme/site1/areaA/line3/pump07"
```

The bridge can map from:
- `extensions.okf.asset_path` (preferred)
- a simple `asset_hint` in SIPREC metadata
- (later) NLP extraction
