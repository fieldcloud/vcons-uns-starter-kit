# SIPREC Simulation Adapter

This service simulates ingesting SIPREC recordings by watching a folder drop:

- `session.json` (metadata)
- `audio.wav` (media)

It creates a minimal vCon JSON document and posts it to the vCon Store Stub.

## Run (container)

This service is wired into `podman-compose.yml`.

## Run (local)

```bash
pip install -e .
export VCON_STORE_URL=http://localhost:8000
export SIPREC_INBOX=./runtime/inbox
export SIPREC_ARCHIVE=./runtime/archive
uvicorn siprec_sim_adapter.api:app --reload --port 8080
```

## Ingest

```bash
curl -X POST http://localhost:8080/ingest
```

## Notes

This is PoC-grade code.
In a production build, use vcon-lib to construct and validate vCons and attach transcripts using the WTF extension.
