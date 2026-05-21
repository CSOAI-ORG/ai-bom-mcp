<div align="center">

# Ai Bom MCP


> ## Buy Starter — £29/mo
> **Signed attestations + unlimited audits + email support.**
> 👉 **[Subscribe at meok.ai](https://buy.stripe.com/bJeeVf3K428agYR9mE8k83S)** — instant HMAC signing key + Stripe-managed billing.
>
> Free tier remains MIT-licensed and zero-config. Upgrade only when you need signed compliance artefacts for audit.

**MCP server for ai bom mcp operations**

[![PyPI](https://img.shields.io/pypi/v/meok-ai-bom-mcp)](https://pypi.org/project/meok-ai-bom-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MEOK AI Labs](https://img.shields.io/badge/MEOK_AI_Labs-MCP_Server-purple)](https://meok.ai)

</div>


## Quick Install

| Client | Install |
|--------|---------|
| **Claude Desktop** | [![Install in Claude](https://img.shields.io/badge/Install-Claude-blue)](https://claude.ai) |
| **Cursor** | [![Install in Cursor](https://img.shields.io/badge/Install-Cursor-black)](https://cursor.com) |
| **VS Code** | [![Install in VS Code](https://img.shields.io/badge/Install-VS_Code-blue)](https://code.visualstudio.com) |
| **Windsurf** | [![Install in Windsurf](https://img.shields.io/badge/Install-Windsurf-purple)](https://codeium.com/windsurf) |
| **Docker** | `docker run -p 8000:8000 ai-bom-mcp` |
| **pip** | `pip install ai-bom-mcp` |

## Overview

Ai Bom MCP provides AI-powered tools via the Model Context Protocol (MCP).

## Tools

| Tool | Description |
|------|-------------|
| `generate_ai_bom` | Generate an AI-BOM in CycloneDX ML-BOM format (or SPDX 3.0) with all 10 required |
| `audit_ai_bom_completeness` | Audit an existing AI-BOM for completeness against the 10 required field categori |
| `map_to_regulation` | Map an AI-BOM against a specific regulatory framework's technical documentation |
| `required_fields` | List the 10 required AI-BOM field categories and their fields. |
| `sign_ai_bom_attestation` | Generate a cryptographically signed AI-BOM completeness attestation (Pro/Enterpr |

## Installation

```bash
pip install meok-ai-bom-mcp
```

## Usage with Claude Desktop

Add to your Claude Desktop MCP config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "ai-bom-mcp": {
      "command": "python",
      "args": ["-m", "meok_ai_bom_mcp.server"]
    }
  }
}
```

## Usage with FastMCP

```python
from mcp.server.fastmcp import FastMCP

# This server exposes 5 tool(s) via MCP
# See server.py for full implementation
```

## License

MIT © [MEOK AI Labs](https://meok.ai)

<<<<<<< Updated upstream
=======
<!-- meok-faq-schema-v1 -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is this MCP server free to use?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The free tier gives you 10 calls per day with no API key required. Pro tier is £79/mo for unlimited calls plus cryptographically signed attestations your auditor can verify independently."
      }
    },
    {
      "@type": "Question",
      "name": "How does the signed attestation work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Every Pro tier audit produces a HMAC-SHA256 signed certificate with a unique ID and a public verify URL. Your auditor pastes the cert into https://meok-attestation-api.vercel.app/verify and gets an independent valid/invalid response. No contact with MEOK required."
      }
    },
    {
      "@type": "Question",
      "name": "Which MCP clients does this work with?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "All standard MCP clients: Claude Desktop, Claude Code, Cursor, VS Code with MCP extension, Windsurf, Cline, and any custom MCP-compatible agent. Install via npx meok-setup or pip install for the underlying Python package."
      }
    },
    {
      "@type": "Question",
      "name": "Can I install all MEOK governance MCPs at once?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Run npx meok-setup --pack governance to install all 10 governance MCPs and write the configs for Claude Desktop, Cursor, or Windsurf in one command."
      }
    },
    {
      "@type": "Question",
      "name": "Is the regulation text authoritative?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. MEOK syncs daily from the EUR-Lex Cellar SPARQL endpoint, the canonical EU regulation publication system. The text is verbatim with no LLM summarization. Every quote is auditor-defensible and includes the exact article number plus relevance score."
      }
    }
  ]
}
</script>

>>>>>>> Stashed changes

## Sister MCPs

Part of the MEOK **Governance** pack — designed to work together as a fleet. Install the whole pack with `npx meok-setup --pack governance`, or pick the ones you need:

- **EU AI Act** → `uvx eu-ai-act-compliance-mcp` · [PyPI](https://pypi.org/project/eu-ai-act-compliance-mcp/) · [GitHub](https://github.com/CSOAI-ORG/eu-ai-act-compliance-mcp)
- **DORA** → `uvx dora-compliance-mcp` · [PyPI](https://pypi.org/project/dora-compliance-mcp/) · [GitHub](https://github.com/CSOAI-ORG/dora-compliance-mcp)
- **NIS2** → `uvx nis2-compliance-mcp` · [PyPI](https://pypi.org/project/nis2-compliance-mcp/) · [GitHub](https://github.com/CSOAI-ORG/nis2-compliance-mcp)
- **Cyber Resilience Act** → `uvx cra-compliance-mcp` · [PyPI](https://pypi.org/project/cra-compliance-mcp/) · [GitHub](https://github.com/CSOAI-ORG/cra-compliance-mcp)
- **AI Incident Reporting** → `uvx ai-incident-reporting-mcp` · [PyPI](https://pypi.org/project/ai-incident-reporting-mcp/) · [GitHub](https://github.com/CSOAI-ORG/ai-incident-reporting-mcp)
- **DORA × NIS2 Crosswalk** → `uvx dora-nis2-crosswalk-mcp` · [PyPI](https://pypi.org/project/dora-nis2-crosswalk-mcp/) · [GitHub](https://github.com/CSOAI-ORG/dora-nis2-crosswalk-mcp)

Full catalogue + Anthropic Registry verify links: [meok.ai/anthropic-registry](https://meok.ai/anthropic-registry)

<!-- mcp-name: io.github.CSOAI-ORG/ai-bom-mcp -->
