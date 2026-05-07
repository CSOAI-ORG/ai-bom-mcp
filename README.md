[![ai-bom-mcp MCP server](https://glama.ai/mcp/servers/CSOAI-ORG/ai-bom-mcp/badges/card.svg)](https://glama.ai/mcp/servers/CSOAI-ORG/ai-bom-mcp)

<div align="center">

[![PyPI](https://img.shields.io/pypi/v/ai-bom-mcp)](https://pypi.org/project/ai-bom-mcp/)
[![Downloads](https://img.shields.io/pypi/dm/ai-bom-mcp)](https://pypi.org/project/ai-bom-mcp/)
[![GitHub stars](https://img.shields.io/github/stars/CSOAI-ORG/ai-bom-mcp)](https://github.com/CSOAI-ORG/ai-bom-mcp/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

# AI Bill of Materials MCP

**Generate and audit AI Bills of Materials for EU AI Act Annex IV, US EO 14028, NIST AI RMF, and ISO 42001. CycloneDX-compatible output.**

[![MEOK AI Labs](https://img.shields.io/badge/MEOK_AI_Labs-224+_servers-purple)](https://meok.ai)

[Install](#install) · [Tools](#tools) · [Pricing](#pricing) · [Attestation API](#attestation-api)

</div>

---

## Why This Exists

AI Bills of Materials (AI-BOMs) are becoming mandatory. EU AI Act Annex IV requires high-risk AI providers to document training data, model architecture, evaluation metrics, and deployment constraints. US Executive Order 14028 requires software supply chain transparency for federal procurement. NIST and ISO 42001 both reference BOM-style documentation.

No standard format exists yet. CycloneDX has proposed an ML-BOM extension, SPDX is exploring AI metadata, and the EU AI Office is developing Annex IV templates. This MCP generates structured AI-BOMs that satisfy all four frameworks, audits existing BOMs for completeness, and maps required fields to specific regulatory articles.

## Install

```bash
pip install ai-bom-mcp
```

## Tools

| Tool | Regulation Reference | What it does |
|------|---------------------|--------------|
| `generate_ai_bom` | Annex IV, EO 14028, NIST, ISO 42001 | Generate a structured AI Bill of Materials |
| `audit_ai_bom_completeness` | All frameworks | Audit an existing AI-BOM for missing required fields |
| `map_to_regulation` | EU AI Act / EO 14028 / NIST / ISO 42001 | Map AI-BOM fields to specific regulatory requirements |
| `required_fields` | All frameworks | List all required BOM fields per regulation |

## Example

```
Prompt: "Generate an AI-BOM for our fraud detection model. It uses
XGBoost trained on 2M transactions from our data warehouse, deployed
as a REST API in AWS eu-west-1, with weekly retraining."

Result: Structured AI-BOM with: model card (XGBoost, version, hyperparams),
training data provenance (2M records, internal data warehouse, no PII
confirmed), deployment spec (REST API, eu-west-1, auto-scaling),
monitoring (weekly retrain, drift detection status), regulatory mapping
(Annex IV sections covered, EO 14028 SBOM requirements met, NIST AI RMF
MAP subcategories addressed). Completeness score with gaps flagged.
```

## Pricing

| Tier | Price | What you get |
|------|-------|-------------|
| **Free** | £0 | 10 calls/day — BOM generation + field listing |
| **Pro** | £199/mo | Unlimited + HMAC-signed attestations + verify URLs |
| **Enterprise** | £1,499/mo | Multi-tenant + co-branded reports + webhooks |

[Subscribe to Pro](https://buy.stripe.com/14A4gB3K4eUWgYR56o8k836) · [Enterprise](https://buy.stripe.com/4gM9AV80kaEG0ZT42k8k837)

## Attestation API

Every Pro/Enterprise audit produces a cryptographically signed certificate:

```
POST https://meok-attestation-api.vercel.app/sign
GET  https://meok-attestation-api.vercel.app/verify/{cert_id}
```

Zero-dep verifier: `pip install meok-attestation-verify`

## Links

- Website: [meok.ai](https://meok.ai)
- All MCP servers: [meok.ai/labs/mcp/servers](https://meok.ai/labs/mcp/servers)
- Enterprise support: nicholas@csoai.org

## License

MIT
