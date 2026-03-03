# VCONIC TADHack Challenge Brief (1 page)
## Operational Knowledge Fabric: vCons + Unified Namespace for Industry

### One-line challenge
Build a small, working component (or mini end-to-end PoC) that turns **real-world conversations**
(starting with **SIPREC + Microsoft Teams**) into **governed vCons**, then publishes **human events**
into a **Unified Namespace (UNS)** — so industrial sites can preserve *understanding*, not just *data*.

---

## Why this challenge exists
Industrial sites are full of telemetry, alarms, and dashboards — yet the real “why” behind incidents,
workarounds, and decisions is trapped in conversations: shift handovers, vendor calls, radio traffic,
Teams calls.

When those conversations disappear, so does institutional memory — and modernization, cybersecurity,
and continuity all suffer.

---

## Build targets (pick one “Quest”)
- SIPREC (simulated) → vCon adapter
- Teams ad hoc calls → vCon adapter
- vCon → UNS publisher (MQTT pointer + summary)
- UNS consumer → Graph (Neo4j)
- Minimal UI (asset → conversations)
- Stretch: trunked/two-way radio via SIP bridge
- Optional: vCon lifecycle receipts (integrity / audit)

---

## Design rules (keep it safe and buildable)
- MQTT carries **pointer + summary**, not full transcripts/media
- Store full vCons in a governed store (RBAC/retention placeholders)
- Use synthetic/anonymized data only (no real numbers, no private recordings)
- Prefer participant roles (operator, engineer, vendor), not personal identities

---

## Useful links
- vCons repo: https://github.com/vcon-dev/vcon
- Unified Namespace repo: https://github.com/mkashwin/unifiednamespace
- VCONIC TADHack: https://blog.tadhack.com/2025/12/19/vconic-tadhack/
