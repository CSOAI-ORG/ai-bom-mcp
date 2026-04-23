# AI-BOM MCP

**Generate + audit AI Bills of Materials** for US federal procurement (EO 14028), EU AI Act Annex IV, NIST AI RMF, and ISO 42001.

Built by [MEOK AI Labs](https://meok.ai).

## What it does

- **`generate_ai_bom`** — produce a CycloneDX ML-BOM 1.6 or SPDX 3.0.1 AI profile document for any model
- **`audit_ai_bom_completeness`** — check an existing AI-BOM against the 10 required field categories
- **`map_to_regulation`** — cross-walk an AI-BOM to EU AI Act / NIST AI RMF / US EO 14028 / ISO 42001
- **`required_fields`** — reference the authoritative field list

## Install

```bash
pip install ai-bom-mcp
```

## Why it matters

- **US federal procurement** requires SBOM/AI-BOM per OMB M-22-18 + EO 14028
- **EU AI Act Article 11 + Annex IV** mandates technical documentation of training data, architecture, evaluation — an AI-BOM in all but name
- **Enterprise buyers** increasingly ask for AI-BOM in security questionnaires
- **No turnkey tool exists** — every AI vendor reinvents this manually

## Tiers

- Free: 10 calls/day, generate + audit
- Pro £199/mo: unlimited, signed attestation, multi-format export
- Enterprise £1,499/mo: auto-scans training data for provenance, Trust Centre push

## License

MIT. MEOK AI Labs, 2026.
