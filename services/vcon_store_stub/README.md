# vCon Store Stub

This is a **minimal** REST API used to store and retrieve vCon JSON documents for the OKF PoC.

It is intentionally simple and **not** production-ready.

## Endpoints

- `GET /healthz`
- `POST /vcons` — store a vCon JSON (generates uuid if missing)
- `GET /vcons` — list stored vCons
- `GET /vcons/{id}` — fetch a vCon
- `GET /vcons/changes?since=<unix_ts>` — list vCons modified after timestamp (used for polling)

## Local dev

```bash
pip install -e .
uvicorn vcon_store_stub.main:app --reload
```
