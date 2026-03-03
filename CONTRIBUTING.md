# Contributing

Thanks for your interest in contributing to the Operational Knowledge Fabric (OKF) starter kit.

This repo is intentionally **builder-friendly**:
- small, readable services
- strong defaults for testing and linting
- easy to run with Podman Compose
- easy to extend using code-generation tools (Codex-style)

## Ways to contribute

- **Adapters**
  - SIPREC (simulated) → vCon
  - Teams ad hoc calls → vCon (fixture-based first)
  - Radio via SIP bridge (stretch)
- **Glue**
  - vCon → MQTT UNS publisher (pointer + summary)
  - UNS consumers (Neo4j / TimescaleDB)
  - GraphQL schema / resolvers
- **Docs**
  - better threat model / governance examples
  - clearer industrial mappings (ISA-95 paths, asset naming)
  - demo scripts and sample datasets

## Dev workflow (recommended)

1) Fork + create a feature branch
```bash
git checkout -b feat/my-change
```

2) Keep changes small and testable

3) Run formatting / lint / tests for the service you changed (see each service README)

4) Open a PR describing:
- what you changed
- how to run it locally
- what problem it solves

## Coding conventions

- Prefer **Python 3.12**
- Use **type hints**
- Use **structured logging** (JSON logs preferred)
- Keep “plumbing” code small and well-commented
- Add a small test for any non-trivial logic

## Safety & privacy

Do **not** submit real private recordings, phone numbers, or customer data.
Use synthetic or anonymized data only.

If your change affects data handling, include a note in `docs/03-governance-security.md`.

## License

By contributing, you agree your contributions are licensed under the MIT License (see `LICENSE`).
